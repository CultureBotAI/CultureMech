# Source and formulation review: BG11 TES no bicarb (CultureMech:015453)

- Review: 20261021T231529Z-culturemech-015453-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T23:07:35Z
- Finished UTC: 2026-10-21T23:15:29Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact named FEBA formulation supports every listed numerical rate, including the A5 dilution. Citric acid is grounded to sodium citrate, EDTA source metadata does not settle hydration, and source evidence and later owner annotations are missing from the generated record. Historical CultureBotHT byte equivalence remains unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 407; batch 041 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty task batches contain 400 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 403 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015453 | data/merge_yaml/merged/BG11_TES_no_bicarb.yaml | generated | BG11 TES no bicarb |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015453 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:015453 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-041/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch041/407/strict.tsv |
| validate-terms | passed | True | CultureMech:015453 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:015453 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:015453 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: culturebothtRepository | unavailable | True | CultureMech:015453 | The exact public CultureBotHT endpoint returned HTTP 404 at its retained actual access time. The March import bytes and their historical equivalence to the later FEBA recipe remain unverified. Current named FEBA amounts are independently assessable; the missing historical source is a partial-completion limit. |
| Exact source content access: culturebothtExactBG11_TES_no_bicarb | unavailable | True | CultureMech:015453 | The exact public CultureBotHT endpoint returned HTTP 404 at its retained actual access time. The March import bytes and their historical equivalence to the later FEBA recipe remain unverified. Current named FEBA amounts are independently assessable; the missing historical source is a partial-completion limit. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:015453.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:015453.

14 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 14/14 primary and 0/14 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 14: primary 100.00%; secondary 0.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:015453.

64 source-scoped decisions, including every local concentration and explicit source-only quantities. Evidence-only marks source-supported numerals whose scoped evidence must be attached; verified is reserved for an existing value, unit and basis with matching attached evidence.

[
  {
    "decision_id": "q1",
    "name": "Sodium nitrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "17.6",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": "17.6",
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row Sodium nitrate",
        "exact_source_quote": "Sodium nitrate\t17.6\tmM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion."
  },
  {
    "decision_id": "q2",
    "name": "Sodium nitrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "17.6",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": "17.6",
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row Sodium nitrate",
        "exact_source_quote": "Sodium nitrate\t17.6\tmM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion."
  },
  {
    "decision_id": "q3",
    "name": "Potassium phosphate dibasic",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": "0.2",
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row Potassium phosphate dibasic",
        "exact_source_quote": "Potassium phosphate dibasic\t0.2\tmM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion."
  },
  {
    "decision_id": "q4",
    "name": "Potassium phosphate dibasic",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": "0.2",
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row Potassium phosphate dibasic",
        "exact_source_quote": "Potassium phosphate dibasic\t0.2\tmM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion."
  },
  {
    "decision_id": "q5",
    "name": "Magnesium Sulfate Heptahydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.3",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": "0.3",
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row Magnesium Sulfate Heptahydrate",
        "exact_source_quote": "Magnesium Sulfate Heptahydrate\t0.3\tmM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion."
  },
  {
    "decision_id": "q6",
    "name": "Magnesium Sulfate Heptahydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.3",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": "0.3",
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row Magnesium Sulfate Heptahydrate",
        "exact_source_quote": "Magnesium Sulfate Heptahydrate\t0.3\tmM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion."
  },
  {
    "decision_id": "q7",
    "name": "Calcium chloride dihydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.24",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": "0.24",
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row Calcium chloride dihydrate",
        "exact_source_quote": "Calcium chloride dihydrate\t0.24\tmM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion."
  },
  {
    "decision_id": "q8",
    "name": "Calcium chloride dihydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.24",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": "0.24",
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row Calcium chloride dihydrate",
        "exact_source_quote": "Calcium chloride dihydrate\t0.24\tmM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion."
  },
  {
    "decision_id": "q9",
    "name": "Citric Acid",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "28.5",
          "unit": "MICROMOLAR"
        }
      }
    ],
    "desired": {
      "value": "28.5",
      "unit": "MICROMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row Citric Acid",
        "exact_source_quote": "Citric Acid\t28.5\tuM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion. This does not validate the sodium-citrate identifier assigned to source citric acid."
  },
  {
    "decision_id": "q10",
    "name": "Citric Acid",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "28.5",
          "unit": "MICROMOLAR"
        }
      }
    ],
    "desired": {
      "value": "28.5",
      "unit": "MICROMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row Citric Acid",
        "exact_source_quote": "Citric Acid\t28.5\tuM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion. This does not validate the sodium-citrate identifier assigned to source citric acid."
  },
  {
    "decision_id": "q11",
    "name": "Ferric ammonium citrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.006",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row Ferric ammonium citrate",
        "exact_source_quote": "Ferric ammonium citrate\t0.006\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion."
  },
  {
    "decision_id": "q12",
    "name": "Ferric ammonium citrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.006",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row Ferric ammonium citrate",
        "exact_source_quote": "Ferric ammonium citrate\t0.006\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion."
  },
  {
    "decision_id": "q13",
    "name": "EDTA (disodium salt)",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.4",
          "unit": "MICROMOLAR"
        }
      }
    ],
    "desired": {
      "value": "2.4",
      "unit": "MICROMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row EDTA (disodium salt)",
        "exact_source_quote": "EDTA (disodium salt)\t2.4\tuM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion. Hydration remains unresolved independently of the verified source numeral."
  },
  {
    "decision_id": "q14",
    "name": "EDTA (disodium salt)",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.4",
          "unit": "MICROMOLAR"
        }
      }
    ],
    "desired": {
      "value": "2.4",
      "unit": "MICROMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row EDTA (disodium salt)",
        "exact_source_quote": "EDTA (disodium salt)\t2.4\tuM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion. Hydration remains unresolved independently of the verified source numeral."
  },
  {
    "decision_id": "q15",
    "name": "TES",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "20",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": "20",
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row TES",
        "exact_source_quote": "TES\t20\tmM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion."
  },
  {
    "decision_id": "q16",
    "name": "TES",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "20",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": "20",
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb direct row TES",
        "exact_source_quote": "TES\t20\tmM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. Direct source concentration, without batch-volume or mass-to-molar conversion."
  },
  {
    "decision_id": "q17",
    "name": "Boric Acid",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.00286",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.00286",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock row Boric Acid",
        "exact_source_quote": "Boric Acid\t2.86\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb A5 receiving-strength row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock-strength declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. The stock rate is divided by 1000 for 1 X in the receiving medium; decimal floating serialization is not a substantive discrepancy. No ml dose or measured final volume is inferred."
  },
  {
    "decision_id": "q18",
    "name": "Boric Acid",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.00286",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.00286",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock row Boric Acid",
        "exact_source_quote": "Boric Acid\t2.86\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb A5 receiving-strength row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock-strength declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. The stock rate is divided by 1000 for 1 X in the receiving medium; decimal floating serialization is not a substantive discrepancy. No ml dose or measured final volume is inferred."
  },
  {
    "decision_id": "q19",
    "name": "Manganese (II) chloride tetrahydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.0018100000000000002",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.00181",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock row Manganese (II) chloride tetrahydrate",
        "exact_source_quote": "Manganese (II) chloride tetrahydrate\t1.81\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb A5 receiving-strength row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock-strength declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. The stock rate is divided by 1000 for 1 X in the receiving medium; decimal floating serialization is not a substantive discrepancy. No ml dose or measured final volume is inferred."
  },
  {
    "decision_id": "q20",
    "name": "Manganese (II) chloride tetrahydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.0018100000000000002",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.00181",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock row Manganese (II) chloride tetrahydrate",
        "exact_source_quote": "Manganese (II) chloride tetrahydrate\t1.81\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb A5 receiving-strength row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock-strength declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. The stock rate is divided by 1000 for 1 X in the receiving medium; decimal floating serialization is not a substantive discrepancy. No ml dose or measured final volume is inferred."
  },
  {
    "decision_id": "q21",
    "name": "Zinc sulfate heptahydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.000222",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.000222",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock row Zinc sulfate heptahydrate",
        "exact_source_quote": "Zinc sulfate heptahydrate\t0.222\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb A5 receiving-strength row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock-strength declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. The stock rate is divided by 1000 for 1 X in the receiving medium; decimal floating serialization is not a substantive discrepancy. No ml dose or measured final volume is inferred."
  },
  {
    "decision_id": "q22",
    "name": "Zinc sulfate heptahydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.000222",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.000222",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock row Zinc sulfate heptahydrate",
        "exact_source_quote": "Zinc sulfate heptahydrate\t0.222\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb A5 receiving-strength row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock-strength declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. The stock rate is divided by 1000 for 1 X in the receiving medium; decimal floating serialization is not a substantive discrepancy. No ml dose or measured final volume is inferred."
  },
  {
    "decision_id": "q23",
    "name": "Sodium Molybdate Dihydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.00039000000000000005",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.00039",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock row Sodium Molybdate Dihydrate",
        "exact_source_quote": "Sodium Molybdate Dihydrate\t0.39\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb A5 receiving-strength row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock-strength declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. The stock rate is divided by 1000 for 1 X in the receiving medium; decimal floating serialization is not a substantive discrepancy. No ml dose or measured final volume is inferred."
  },
  {
    "decision_id": "q24",
    "name": "Sodium Molybdate Dihydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.00039000000000000005",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.00039",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock row Sodium Molybdate Dihydrate",
        "exact_source_quote": "Sodium Molybdate Dihydrate\t0.39\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb A5 receiving-strength row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock-strength declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. The stock rate is divided by 1000 for 1 X in the receiving medium; decimal floating serialization is not a substantive discrepancy. No ml dose or measured final volume is inferred."
  },
  {
    "decision_id": "q25",
    "name": "Copper (II) sulfate pentahydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "7.9e-05",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.000079",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock row Copper (II) sulfate pentahydrate",
        "exact_source_quote": "Copper (II) sulfate pentahydrate\t0.079\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb A5 receiving-strength row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock-strength declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. The stock rate is divided by 1000 for 1 X in the receiving medium; decimal floating serialization is not a substantive discrepancy. No ml dose or measured final volume is inferred."
  },
  {
    "decision_id": "q26",
    "name": "Copper (II) sulfate pentahydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "7.9e-05",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.000079",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock row Copper (II) sulfate pentahydrate",
        "exact_source_quote": "Copper (II) sulfate pentahydrate\t0.079\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb A5 receiving-strength row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock-strength declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. The stock rate is divided by 1000 for 1 X in the receiving medium; decimal floating serialization is not a substantive discrepancy. No ml dose or measured final volume is inferred."
  },
  {
    "decision_id": "q27",
    "name": "Cobalt(II) nitrate hexahydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.0494",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.0494",
      "unit": "MG_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock row Cobalt(II) nitrate hexahydrate",
        "exact_source_quote": "Cobalt(II) nitrate hexahydrate\t49.4\tmg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb A5 receiving-strength row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock-strength declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. The stock rate is divided by 1000 for 1 X in the receiving medium; decimal floating serialization is not a substantive discrepancy. No ml dose or measured final volume is inferred."
  },
  {
    "decision_id": "q28",
    "name": "Cobalt(II) nitrate hexahydrate",
    "stage": "Main medium rate, exact named FEBA variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.0494",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.0494",
      "unit": "MG_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock row Cobalt(II) nitrate hexahydrate",
        "exact_source_quote": "Cobalt(II) nitrate hexahydrate\t49.4\tmg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BG11_TES_no_bicarb A5 receiving-strength row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock-strength declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Numerical value and unit are supported for the named ingredient. The stock rate is divided by 1000 for 1 X in the receiving medium; decimal floating serialization is not a substantive discrepancy. No ml dose or measured final volume is inferred."
  },
  {
    "decision_id": "q29",
    "name": "Boric Acid",
    "stage": "Source-only A5 stock concentration",
    "decision": "evidence_only",
    "local_fields": [],
    "desired": {
      "stock_value": "2.86",
      "stock_unit": "g/L",
      "stock_strength_X": 1000
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 exact constituent row",
        "exact_source_quote": "Boric Acid\t2.86\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock strength",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Retain the stock stage in attached dilution evidence or a separately curated stock; never substitute this undiluted value into the main medium."
  },
  {
    "decision_id": "q30",
    "name": "Manganese (II) chloride tetrahydrate",
    "stage": "Source-only A5 stock concentration",
    "decision": "evidence_only",
    "local_fields": [],
    "desired": {
      "stock_value": "1.81",
      "stock_unit": "g/L",
      "stock_strength_X": 1000
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 exact constituent row",
        "exact_source_quote": "Manganese (II) chloride tetrahydrate\t1.81\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock strength",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Retain the stock stage in attached dilution evidence or a separately curated stock; never substitute this undiluted value into the main medium."
  },
  {
    "decision_id": "q31",
    "name": "Zinc sulfate heptahydrate",
    "stage": "Source-only A5 stock concentration",
    "decision": "evidence_only",
    "local_fields": [],
    "desired": {
      "stock_value": "0.222",
      "stock_unit": "g/L",
      "stock_strength_X": 1000
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 exact constituent row",
        "exact_source_quote": "Zinc sulfate heptahydrate\t0.222\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock strength",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Retain the stock stage in attached dilution evidence or a separately curated stock; never substitute this undiluted value into the main medium."
  },
  {
    "decision_id": "q32",
    "name": "Sodium Molybdate Dihydrate",
    "stage": "Source-only A5 stock concentration",
    "decision": "evidence_only",
    "local_fields": [],
    "desired": {
      "stock_value": "0.39",
      "stock_unit": "g/L",
      "stock_strength_X": 1000
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 exact constituent row",
        "exact_source_quote": "Sodium Molybdate Dihydrate\t0.39\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock strength",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Retain the stock stage in attached dilution evidence or a separately curated stock; never substitute this undiluted value into the main medium."
  },
  {
    "decision_id": "q33",
    "name": "Copper (II) sulfate pentahydrate",
    "stage": "Source-only A5 stock concentration",
    "decision": "evidence_only",
    "local_fields": [],
    "desired": {
      "stock_value": "0.079",
      "stock_unit": "g/L",
      "stock_strength_X": 1000
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 exact constituent row",
        "exact_source_quote": "Copper (II) sulfate pentahydrate\t0.079\tg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock strength",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Retain the stock stage in attached dilution evidence or a separately curated stock; never substitute this undiluted value into the main medium."
  },
  {
    "decision_id": "q34",
    "name": "Cobalt(II) nitrate hexahydrate",
    "stage": "Source-only A5 stock concentration",
    "decision": "evidence_only",
    "local_fields": [],
    "desired": {
      "stock_value": "49.4",
      "stock_unit": "mg/L",
      "stock_strength_X": 1000
    },
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 exact constituent row",
        "exact_source_quote": "Cobalt(II) nitrate hexahydrate\t49.4\tmg/L\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "A5 stock strength",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Retain the stock stage in attached dilution evidence or a separately curated stock; never substitute this undiluted value into the main medium."
  },
  {
    "decision_id": "q35",
    "name": "A5 receiving dose",
    "stage": "Source relative stock strength",
    "decision": "evidence_only",
    "local_fields": [],
    "desired": {
      "receiving_strength_X": 1,
      "stock_strength_X": 1000,
      "liquid_dose_ml": null
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "Exact main A5 row",
        "exact_source_quote": "Trace metal mix A5\t1\tX\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Exact stock X declaration",
        "exact_source_quote": "X\t1000\t\n",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Explicit relative strengths justify the ratio only. No liquid addition volume is printed, and no extra final-volume claim is made."
  },
  {
    "decision_id": "q36",
    "name": "Sodium nitrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7631-99-4; MW: 84.99"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Sodium nitrate",
        "CAS": "7631-99-4",
        "Company": "Sigma",
        "CatalogNumber": "S8170",
        "FW": "84.99",
        "Synonyms": "NaNO3",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "yes",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "yes",
        "FEBA_stress": "yes",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 400",
        "exact_source_quote": "Sodium nitrate\t7631-99-4\tSigma\tS8170\t84.99\tNaNO3\t\t\tyes\t\tyes\tyes\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q37",
    "name": "Potassium phosphate dibasic",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "CAS: 7758-11-4; MW: 174.18"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Potassium phosphate dibasic",
        "CAS": "7758-11-4",
        "Company": "Sigma",
        "CatalogNumber": "P3786",
        "FW": "174.18",
        "Synonyms": "K2HPO4, dibasic anhydrous sodium phosphate",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 337",
        "exact_source_quote": "Potassium phosphate dibasic\t7758-11-4\tSigma\tP3786\t174.18\tK2HPO4, dibasic anhydrous sodium phosphate\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source preferred name, K2HPO4, CAS 7758-11-4 and FW 174.18 support dipotassium hydrogen phosphate. Source synonym dibasic anhydrous sodium phosphate is internally inconsistent. OLS has a trihydrate synonym but its formula/mass encode the unhydrated salt; neither stray synonym establishes an actual source hydrate or sodium salt. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q38",
    "name": "Magnesium Sulfate Heptahydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "CAS: 10034-99-8; MW: 246.47"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Magnesium Sulfate Heptahydrate",
        "CAS": "10034-99-8",
        "Company": "Sigma",
        "CatalogNumber": "M1880",
        "FW": "246.47",
        "Synonyms": "Epsom salts, MgSO4 7H2O",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 277",
        "exact_source_quote": "Magnesium Sulfate Heptahydrate\t10034-99-8\tSigma\tM1880\t246.47\tEpsom salts, MgSO4 7H2O\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q39",
    "name": "Calcium chloride dihydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 10035-04-8; MW: 147.01"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Calcium chloride dihydrate",
        "CAS": "10035-04-8",
        "Company": "Sigma",
        "CatalogNumber": "C5080",
        "FW": "147.01",
        "Synonyms": "Calcium Chloride Dihydrate, CaCl2*2H2O",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "yes",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 90",
        "exact_source_quote": "Calcium chloride dihydrate\t10035-04-8\tSigma\tC5080\t147.01\tCalcium Chloride Dihydrate, CaCl2*2H2O\t\t\tyes\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q40",
    "name": "Citric Acid",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 77-92-9; MW: 192.12"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Citric Acid",
        "CAS": "77-92-9",
        "Company": "Sigma",
        "CatalogNumber": "251275",
        "FW": "192.12",
        "Synonyms": "",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "no",
        "FEBA_carbon": "yes",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 119",
        "exact_source_quote": "Citric Acid\t77-92-9\tSigma\t251275\t192.12\t\t\t\tno\tyes\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source citric acid and CAS 77-92-9 differ from CHEBI:53258, the trisodium citrate salt. CHEBI:30769 is the supported acid candidate; retain the source amount. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q41",
    "name": "Ferric ammonium citrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 1185-57-5"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Ferric ammonium citrate",
        "CAS": "1185-57-5",
        "Company": "Sigma",
        "CatalogNumber": "F5879",
        "FW": "",
        "Synonyms": "",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 186",
        "exact_source_quote": "Ferric ammonium citrate\t1185-57-5\tSigma\tF5879\t\t\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source ferric ammonium citrate matches the asserted mixture identity. OLS describes indefinite composition; no fixed molar mass or molecular concentration is inferred. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q42",
    "name": "EDTA (disodium salt)",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "CAS: 6381-92-6; MW: 336.206"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "EDTA (disodium salt)",
        "CAS": "6381-92-6",
        "Company": "Sigma",
        "CatalogNumber": "E6635",
        "FW": "336.206",
        "Synonyms": "",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 178",
        "exact_source_quote": "EDTA (disodium salt)\t6381-92-6\tSigma\tE6635\t336.206\t\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source EDTA disodium name does not specify hydration. CAS 6381-92-6 conflicts with the anhydrous term CAS 139-33-3, while source FW 336.206 is consistent with the anhydrous term mass 336.208. Supplier-specific hydration remains unresolved; do not silently choose a hydrate or recalculate the amount. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q43",
    "name": "Boric Acid",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "CAS: 10043-35-3; MW: 61.83; From Trace metal mix A5"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Boric Acid",
        "CAS": "10043-35-3",
        "Company": "",
        "CatalogNumber": "0084-01 (JT*)",
        "FW": "61.83",
        "Synonyms": "H3BO3",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "no",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 84",
        "exact_source_quote": "Boric Acid\t10043-35-3\t\t0084-01 (JT*)\t61.83\tH3BO3\t\t\tno\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q44",
    "name": "Manganese (II) chloride tetrahydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[8].notes",
        "stored": "CAS: 13446-34-9; MW: 197.91; From Trace metal mix A5; Ontology enriched via CAS-RN lookup"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Manganese (II) chloride tetrahydrate",
        "CAS": "13446-34-9",
        "Company": "Sigma",
        "CatalogNumber": "M3634",
        "FW": "197.91",
        "Synonyms": "MnCl2, manganese chloride, MnCl2 4H2O",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "yes",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 278",
        "exact_source_quote": "Manganese (II) chloride tetrahydrate\t13446-34-9\tSigma\tM3634\t197.91\tMnCl2, manganese chloride, MnCl2 4H2O\t\t\tyes\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q45",
    "name": "Zinc sulfate heptahydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[9].notes",
        "stored": "CAS: 7446-20-0; MW: 287.56; From Trace metal mix A5; Ontology enriched via CAS-RN lookup"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Zinc sulfate heptahydrate",
        "CAS": "7446-20-0",
        "Company": "Sigma",
        "CatalogNumber": "Z0251",
        "FW": "287.56",
        "Synonyms": "zinc sulfate, ZnSO4 7H2O",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "yes",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 474",
        "exact_source_quote": "Zinc sulfate heptahydrate\t7446-20-0\tSigma\tZ0251\t287.56\tzinc sulfate, ZnSO4 7H2O\t\t\t\t\t\tyes\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q46",
    "name": "Sodium Molybdate Dihydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[10].notes",
        "stored": "CAS: 10102-40-6; MW: 241.95; From Trace metal mix A5; Ontology enriched via CAS-RN lookup"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Sodium Molybdate Dihydrate",
        "CAS": "10102-40-6",
        "Company": "Sigma",
        "CatalogNumber": "331058",
        "FW": "241.95",
        "Synonyms": "Na2MoO4 2H2O, Na2MoO4-2H2O",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 399",
        "exact_source_quote": "Sodium Molybdate Dihydrate\t10102-40-6\tSigma\t331058\t241.95\tNa2MoO4 2H2O, Na2MoO4-2H2O\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q47",
    "name": "Copper (II) sulfate pentahydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[11].notes",
        "stored": "CAS: 7758-99-8; MW: 249.69; From Trace metal mix A5; Ontology enriched via CAS-RN lookup"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Copper (II) sulfate pentahydrate",
        "CAS": "7758-99-8",
        "Company": "Sigma",
        "CatalogNumber": "C8027",
        "FW": "249.69",
        "Synonyms": "Blue Vitriol, Cupric sulfate pentahydrate, Sulfuric acid, copper(II) salt (1:1) pentahydrate, CuSO4 5H2O, Cupric Sulfate",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 129",
        "exact_source_quote": "Copper (II) sulfate pentahydrate\t7758-99-8\tSigma\tC8027\t249.69\tBlue Vitriol, Cupric sulfate pentahydrate, Sulfuric acid, copper(II) salt (1:1) pentahydrate, CuSO4 5H2O, Cupric Sulfate\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q48",
    "name": "Cobalt(II) nitrate hexahydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[12].notes",
        "stored": "CAS: 10026-22-9; MW: 291.03; From Trace metal mix A5; Ontology enriched via CAS-RN lookup"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Cobalt(II) nitrate hexahydrate",
        "CAS": "10026-22-9",
        "Company": "",
        "CatalogNumber": "",
        "FW": "291.03",
        "Synonyms": "Co(NO3)2 6H2O",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 124",
        "exact_source_quote": "Cobalt(II) nitrate hexahydrate\t10026-22-9\t\t\t291.03\tCo(NO3)2 6H2O\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q49",
    "name": "TES",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BG11_TES_no_bicarb.yaml",
        "field_path": "ingredients[13].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7365-44-8; MW: 229.25"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "TES",
        "CAS": "7365-44-8",
        "Company": "",
        "CatalogNumber": "",
        "FW": "229.25",
        "Synonyms": "2-[(2-Hydroxy-1,1-bis(hydroxymethyl)ethyl)amino]ethanesulfonic acid, N-[Tris(hydroxymethyl)methyl]-2-aminoethanesulfonic acid",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 1372",
        "exact_source_quote": "TES\t7365-44-8\t\t\t229.25\t2-[(2-Hydroxy-1,1-bis(hydroxymethyl)ethyl)amino]ethanesulfonic acid, N-[Tris(hydroxymethyl)methyl]-2-aminoethanesulfonic acid\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q50",
    "name": "Sodium nitrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7631-99-4; MW: 84.99"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Sodium nitrate",
        "CAS": "7631-99-4",
        "Company": "Sigma",
        "CatalogNumber": "S8170",
        "FW": "84.99",
        "Synonyms": "NaNO3",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "yes",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "yes",
        "FEBA_stress": "yes",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 400",
        "exact_source_quote": "Sodium nitrate\t7631-99-4\tSigma\tS8170\t84.99\tNaNO3\t\t\tyes\t\tyes\tyes\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q51",
    "name": "Potassium phosphate dibasic",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "CAS: 7758-11-4; MW: 174.18"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Potassium phosphate dibasic",
        "CAS": "7758-11-4",
        "Company": "Sigma",
        "CatalogNumber": "P3786",
        "FW": "174.18",
        "Synonyms": "K2HPO4, dibasic anhydrous sodium phosphate",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 337",
        "exact_source_quote": "Potassium phosphate dibasic\t7758-11-4\tSigma\tP3786\t174.18\tK2HPO4, dibasic anhydrous sodium phosphate\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source preferred name, K2HPO4, CAS 7758-11-4 and FW 174.18 support dipotassium hydrogen phosphate. Source synonym dibasic anhydrous sodium phosphate is internally inconsistent. OLS has a trihydrate synonym but its formula/mass encode the unhydrated salt; neither stray synonym establishes an actual source hydrate or sodium salt. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q52",
    "name": "Magnesium Sulfate Heptahydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "CAS: 10034-99-8; MW: 246.47"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Magnesium Sulfate Heptahydrate",
        "CAS": "10034-99-8",
        "Company": "Sigma",
        "CatalogNumber": "M1880",
        "FW": "246.47",
        "Synonyms": "Epsom salts, MgSO4 7H2O",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 277",
        "exact_source_quote": "Magnesium Sulfate Heptahydrate\t10034-99-8\tSigma\tM1880\t246.47\tEpsom salts, MgSO4 7H2O\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q53",
    "name": "Calcium chloride dihydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 10035-04-8; MW: 147.01"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Calcium chloride dihydrate",
        "CAS": "10035-04-8",
        "Company": "Sigma",
        "CatalogNumber": "C5080",
        "FW": "147.01",
        "Synonyms": "Calcium Chloride Dihydrate, CaCl2*2H2O",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "yes",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 90",
        "exact_source_quote": "Calcium chloride dihydrate\t10035-04-8\tSigma\tC5080\t147.01\tCalcium Chloride Dihydrate, CaCl2*2H2O\t\t\tyes\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q54",
    "name": "Citric Acid",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 77-92-9; MW: 192.12"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Citric Acid",
        "CAS": "77-92-9",
        "Company": "Sigma",
        "CatalogNumber": "251275",
        "FW": "192.12",
        "Synonyms": "",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "no",
        "FEBA_carbon": "yes",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 119",
        "exact_source_quote": "Citric Acid\t77-92-9\tSigma\t251275\t192.12\t\t\t\tno\tyes\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source citric acid and CAS 77-92-9 differ from CHEBI:53258, the trisodium citrate salt. CHEBI:30769 is the supported acid candidate; retain the source amount. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q55",
    "name": "Ferric ammonium citrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 1185-57-5"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Ferric ammonium citrate",
        "CAS": "1185-57-5",
        "Company": "Sigma",
        "CatalogNumber": "F5879",
        "FW": "",
        "Synonyms": "",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 186",
        "exact_source_quote": "Ferric ammonium citrate\t1185-57-5\tSigma\tF5879\t\t\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source ferric ammonium citrate matches the asserted mixture identity. OLS describes indefinite composition; no fixed molar mass or molecular concentration is inferred. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q56",
    "name": "EDTA (disodium salt)",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "CAS: 6381-92-6; MW: 336.206"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "EDTA (disodium salt)",
        "CAS": "6381-92-6",
        "Company": "Sigma",
        "CatalogNumber": "E6635",
        "FW": "336.206",
        "Synonyms": "",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 178",
        "exact_source_quote": "EDTA (disodium salt)\t6381-92-6\tSigma\tE6635\t336.206\t\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source EDTA disodium name does not specify hydration. CAS 6381-92-6 conflicts with the anhydrous term CAS 139-33-3, while source FW 336.206 is consistent with the anhydrous term mass 336.208. Supplier-specific hydration remains unresolved; do not silently choose a hydrate or recalculate the amount. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q57",
    "name": "Boric Acid",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "CAS: 10043-35-3; MW: 61.83; From Trace metal mix A5"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Boric Acid",
        "CAS": "10043-35-3",
        "Company": "",
        "CatalogNumber": "0084-01 (JT*)",
        "FW": "61.83",
        "Synonyms": "H3BO3",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "no",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 84",
        "exact_source_quote": "Boric Acid\t10043-35-3\t\t0084-01 (JT*)\t61.83\tH3BO3\t\t\tno\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q58",
    "name": "Manganese (II) chloride tetrahydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[8].notes",
        "stored": "CAS: 13446-34-9; MW: 197.91; From Trace metal mix A5; Ontology enriched via CAS-RN lookup"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Manganese (II) chloride tetrahydrate",
        "CAS": "13446-34-9",
        "Company": "Sigma",
        "CatalogNumber": "M3634",
        "FW": "197.91",
        "Synonyms": "MnCl2, manganese chloride, MnCl2 4H2O",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "yes",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 278",
        "exact_source_quote": "Manganese (II) chloride tetrahydrate\t13446-34-9\tSigma\tM3634\t197.91\tMnCl2, manganese chloride, MnCl2 4H2O\t\t\tyes\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q59",
    "name": "Zinc sulfate heptahydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[9].notes",
        "stored": "CAS: 7446-20-0; MW: 287.56; From Trace metal mix A5; Ontology enriched via CAS-RN lookup"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Zinc sulfate heptahydrate",
        "CAS": "7446-20-0",
        "Company": "Sigma",
        "CatalogNumber": "Z0251",
        "FW": "287.56",
        "Synonyms": "zinc sulfate, ZnSO4 7H2O",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "yes",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 474",
        "exact_source_quote": "Zinc sulfate heptahydrate\t7446-20-0\tSigma\tZ0251\t287.56\tzinc sulfate, ZnSO4 7H2O\t\t\t\t\t\tyes\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q60",
    "name": "Sodium Molybdate Dihydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[10].notes",
        "stored": "CAS: 10102-40-6; MW: 241.95; From Trace metal mix A5; Ontology enriched via CAS-RN lookup"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Sodium Molybdate Dihydrate",
        "CAS": "10102-40-6",
        "Company": "Sigma",
        "CatalogNumber": "331058",
        "FW": "241.95",
        "Synonyms": "Na2MoO4 2H2O, Na2MoO4-2H2O",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 399",
        "exact_source_quote": "Sodium Molybdate Dihydrate\t10102-40-6\tSigma\t331058\t241.95\tNa2MoO4 2H2O, Na2MoO4-2H2O\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q61",
    "name": "Copper (II) sulfate pentahydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[11].notes",
        "stored": "CAS: 7758-99-8; MW: 249.69; From Trace metal mix A5; Ontology enriched via CAS-RN lookup"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Copper (II) sulfate pentahydrate",
        "CAS": "7758-99-8",
        "Company": "Sigma",
        "CatalogNumber": "C8027",
        "FW": "249.69",
        "Synonyms": "Blue Vitriol, Cupric sulfate pentahydrate, Sulfuric acid, copper(II) salt (1:1) pentahydrate, CuSO4 5H2O, Cupric Sulfate",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 129",
        "exact_source_quote": "Copper (II) sulfate pentahydrate\t7758-99-8\tSigma\tC8027\t249.69\tBlue Vitriol, Cupric sulfate pentahydrate, Sulfuric acid, copper(II) salt (1:1) pentahydrate, CuSO4 5H2O, Cupric Sulfate\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q62",
    "name": "Cobalt(II) nitrate hexahydrate",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[12].notes",
        "stored": "CAS: 10026-22-9; MW: 291.03; From Trace metal mix A5; Ontology enriched via CAS-RN lookup"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "Cobalt(II) nitrate hexahydrate",
        "CAS": "10026-22-9",
        "Company": "",
        "CatalogNumber": "",
        "FW": "291.03",
        "Synonyms": "Co(NO3)2 6H2O",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 124",
        "exact_source_quote": "Cobalt(II) nitrate hexahydrate\t10026-22-9\t\t\t291.03\tCo(NO3)2 6H2O\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q63",
    "name": "TES",
    "stage": "Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
        "field_path": "ingredients[13].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7365-44-8; MW: 229.25"
      }
    ],
    "desired": {
      "source_compound_fields": {
        "Compound": "TES",
        "CAS": "7365-44-8",
        "Company": "",
        "CatalogNumber": "",
        "FW": "229.25",
        "Synonyms": "2-[(2-Hydroxy-1,1-bis(hydroxymethyl)ethyl)amino]ethanesulfonic acid, N-[Tris(hydroxymethyl)methyl]-2-aminoethanesulfonic acid",
        "Notes": "",
        "Hans80Anti": "",
        "Hans80metals": "",
        "FEBA_carbon": "",
        "FEBA_nitrogen": "",
        "FEBA_stress": "",
        "All_star": ""
      }
    },
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compound row 1372",
        "exact_source_quote": "TES\t7365-44-8\t\t\t229.25\t2-[(2-Hydroxy-1,1-bis(hydroxymethyl)ethyl)amino]ethanesulfonic acid, N-[Tris(hydroxymethyl)methyl]-2-aminoethanesulfonic acid\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "Source named salt, hydrate or buffer agrees with the asserted chemical identity. Explicit hydration is retained; source compound identifiers and formula metadata do not supply new preparation conditions. Historical mapping confidence 0.90, where present, is a local algorithm assertion, not externally verified probability."
  },
  {
    "decision_id": "q64",
    "name": "Unspecified preparation and cultivation conditions",
    "stage": "Exact named FEBA recipe only",
    "decision": "not_quantified",
    "local_fields": [],
    "desired": {
      "water_or_final_batch_volume": null,
      "ph_value": null,
      "temperature_value": null,
      "sterilization_cycle": null,
      "light_intensity": null,
      "light_cycle": null
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "Complete named recipe and description",
        "exact_source_quote": "Media\tBG11_TES_no_bicarb\t\nDescription\tFor growing cyanobacteria, from Luis; no sodium bicarbonate; with TES buffer\t\nMinimal\tTRUE\t\nControlled vocabulary\tConcentration\tUnits\nSodium nitrate\t17.6\tmM\nPotassium phosphate dibasic\t0.2\tmM\nMagnesium Sulfate Heptahydrate\t0.3\tmM\nCalcium chloride dihydrate\t0.24\tmM\nCitric Acid\t28.5\tuM\nFerric ammonium citrate\t0.006\tg/L\nEDTA (disodium salt)\t2.4\tuM\nTrace metal mix A5\t1\tX\nTES\t20\tmM\n\t\t\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "UTF-8 source decoded with universal newlines; tabs and all other characters retained. Raw external evidence preserves original CRLF."
      }
    ],
    "interpretation": "The inspected block supplies concentrations and intended cyanobacterial use, not measured final volume, water make-up, pH, light, temperature or sterilization. Preparation is absent in both target and owner, so no documented preparation loss is inferred. Do not borrow neighboring BG11 conditions."
  }
]

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:015453.

8 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact named variant and contribution membership

identity: supported. Targets: CultureMech:015453.

BG11_TES_no_bicarb is resolved to its exact maintained owner and native inspected merge contribution. All 14 ingredient amounts match the named FEBA block plus the correctly diluted A5 stock. Neighboring BG11, BG11R, nitrogen-free, carbonate-free and TES variants remain distinct.

### Source identity versus canonical ontology metadata

grounding: concern. Targets: CultureMech:015453.

Citric acid is incorrectly mapped to sodium citrate. EDTA hydration is unresolved by conflicting source CAS and formula-weight metadata. All other named forms, including the explicit trace hydrates, agree at the supported source level; misleading potassium-phosphate synonyms do not override its name, CAS and formula.

### Source versions and current repair scope

provenance: concern. Targets: CultureMech:015453.

The September FEBA revision supports the exact current numerical recipe but does not authenticate the March CultureBotHT import. Current owner has later repair metadata and two broad references; target lacks these later fields. An ingredients_curated flag is not proof that chemical forms or evidence have been checked. No universal historical-merger causal claim is made.

### Protocol, culture conditions and source-only information

completeness: unknown. Targets: CultureMech:015453.

The FEBA block has no water make-up, sterilization procedure, temperature, light or final pH. These required protocol details remain unknown, rather than being imported from another BG11 recipe. There is no local solution reference to validate and no existing nested stock; the A5 source ratio is retained in the inventory.

### Growth claims and comparison-only BG11 literature

evidence: not_applicable. Targets: CultureMech:015453.

Neither target nor maintained owner asserts a target organism, strain metric, genome accession or experimental variant. Intended cyanobacterial use is not a strain-specific growth demonstration. Captured sibling BG11 literature, taxonomy and marker evidence is comparison context only and is not transferred to this selected variant.

### Existing physical and organizational classifications

scope: unknown. Targets: CultureMech:015453.

The named formulation supports a liquid mineral-medium representation and cyanobacterial intended use. FEBA Minimal TRUE is not a complete chemical-definition proof, particularly for ferric ammonium citrate of indefinite composition. Preserve category context without inferring cultivation oxygen, strain taxonomy or a replacement classification solely from the name.

### Identifier and reference roles

evidence: concern. Targets: CultureMech:015453.

The owner references a CultureBotHT internal identifier and repository URL, not claim-level concentration evidence. No DOI, PMID, KG match, genome accession, nested solution reference, legacy MIM identifier or current secondary MIM slot is asserted in these selected layers. Optional missing secondary links are not invalid links.

## Findings

### f1: Citric acid is represented by a sodium-citrate identifier

major / open / confirmed; issue key: culturemech.015453.citric-acid-salt.

Both target and maintained owner name Citric Acid and retain acid CAS 77-92-9/FW 192.12, but their primary term is CHEBI:53258 sodium citrate. This is a chemical-form mismatch despite canonical label validity.

### f2: EDTA hydration is asserted more specifically than the reconciled source metadata

major / open / confirmed; issue key: culturemech.015453.edta-hydration.

CHEBI:64734 explicitly asserts anhydrous disodium EDTA. The source name is unqualified; its CAS differs from the anhydrous OLS CAS while its formula weight agrees closely with the anhydrous form. The unresolved source metadata conflict must not be presented as verified hydration.

### f3: Correct numerical amounts lack attached source and stock-dilution evidence

minor / open / confirmed; issue key: culturemech.015453.amount-evidence.

Every selected ingredient concentration is numerically supported by the exact FEBA variant or the explicit A5 1000 X to 1 X dilution, but neither target nor maintained owner carries claim-level concentration evidence. Broad source links and the curated flag omit the verified version, exact rows and arithmetic.

### f4: Generated projection omits later owner source metadata

minor / open / confirmed; issue key: culturemech.015453.stale-owner-metadata.

The generated record predates the maintained owner repair and lacks its media_term and references. Reconciliation must retain append-only chronology and qualify curated status against the actual evidence, rather than assuming the current generator caused every historical difference.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained owner to the supported acid identity with source evidence, preserve its concentration and provenance, then regenerate only under separately authorized workflow.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve the exact supplier/source form or record the hydration uncertainty explicitly without guessing a replacement ID, quantity or molar conversion.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach exact versioned source evidence and explicit A5 stock-to-medium arithmetic in the owner, preserving direct units and uncertainty. Do not replace these correct rates with undiluted stock values.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

After owner scientific corrections, reconcile generated metadata using the authorized generator and preserve the existing historical events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BG11_TES_no_bicarb.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BG11_TES_no_bicarb.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BG11_TES_no_bicarb.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch041/407/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-041/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch041/407/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BG11_TES_no_bicarb.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BG11_TES_no_bicarb.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml:1:id: CultureMech:015453<br>./data/merge_yaml/merged/BG11_TES_no_bicarb.yaml:1:id: CultureMech:015453<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch041/source-preflight-bound/407/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 27 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| feba-main | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media; Named block BG11_TES_no_bicarb, starting line 136 | supports | Exact variant-specific main recipe; later FEBA revision is independent formula evidence, not an authenticated historical CultureBotHT copy. |
| feba-a5 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes; Trace metal mix A5, complete 1000 X block | supports | Six stock rows and explicit 1000 X strength; the main recipe requests 1 X. |
| feba-version | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commit/803273865ea9e83fab770ec4f13670db80e1180b; $.hash and $.date | supports | Exact FEBA revision 803273865ea9e83fab770ec4f13670db80e1180b dated 2026-09-10T16:27:42+00:00 postdates the March import. |
| compound-0 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 400 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-1 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 337 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-2 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 277 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-3 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 90 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-4 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 119 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-5 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 186 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-6 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 178 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-7 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 1372 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-8 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 84 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-9 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 278 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-10 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 474 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-11 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 399 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-12 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 129 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| compound-13 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact named compound row 124 | supports | Source compound metadata; internal synonym and hydration tensions remain explicit. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31604 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31604 resolves to ferric ammonium citrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi39035 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_39035; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:39035 resolves to TES. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53258 resolves to sodium citrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63005 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63005 resolves to sodium nitrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64734; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:64734 resolves to EDTA disodium salt (anhydrous). Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86214 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86214; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86214 resolves to cobalt dinitrate hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {}} |
| citric-acid-candidate | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30769; Exact OLS CHEBI:30769 scientific properties | supports | Citric acid is a distinct nonobsolete acid entity, CAS 77-92-9, formula C6H8O7; candidate correction is separate from this read-only review. |
| culturebothtRepository-attempt | https://api.github.com/repos/CultureBotAI/CultureBotHT; Preserved exact public retrieval result | context_only | The exact public CultureBotHT endpoint returned HTTP 404 at its retained actual access time. The March import bytes and their historical equivalence to the later FEBA recipe remain unverified. Current named FEBA amounts are independently assessable; the missing historical source is a partial-completion limit. |
| culturebothtExactBG11_TES_no_bicarb-attempt | https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BG11_TES_no_bicarb.yaml; Preserved exact public retrieval result | context_only | The exact public CultureBotHT endpoint returned HTTP 404 at its retained actual access time. The March import bytes and their historical equivalence to the later FEBA recipe remain unverified. Current named FEBA amounts are independently assessable; the missing historical source is a partial-completion limit. |
| forms | /private/tmp/culturemech-review-work-batch041/407/chemical-form-inventory.json; Every target and maintained-owner ingredient form, exact source compound fields and OLS scientific properties | context_only | All supplied-form decisions are explicit; exact identifier/label validity is separate from source correspondence. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch041/407/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| history-metadata | data/merge_yaml/merged/BG11_TES_no_bicarb.yaml; data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 4, "timestamp_issues": []}, {"input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml", "events": 4, "timestamp_issues": []}] |
| writer-0 | scripts/repair_culturebotht_bg11_score15.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Full current repair inspected: exact ID/source/name signature guards, media_term/references/flags/history updates; it does not validate amounts, chemical forms, historical source availability or attached claim evidence. No execution or inferred past causation. |
| historical-report-0 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/bg11_tes_no_bicarb.md; Exact matching historical report header and all ingredient decision rows | context_only | Derivative diagnostic reports missing attached source evidence and not-performed source checks. Current FEBA comparison supersedes that absence of assessment, not the immutable report bytes. |
| historical-report-1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BG11_TES_no_bicarb.md; Exact matching historical report header and all ingredient decision rows | context_only | Derivative diagnostic reports missing attached source evidence and not-performed source checks. Current FEBA comparison supersedes that absence of assessment, not the immutable report bytes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact public CultureBotHT endpoint returned HTTP 404 at its retained actual access time. The March import bytes and their historical equivalence to the later FEBA recipe remain unverified. Current named FEBA amounts are independently assessable; the missing historical source is a partial-completion limit.
- Coverage is partial because historical CultureBotHT source identity and complete preparation conditions remain unresolved. All current target/owner concentrations and supplied-form assertions were nevertheless assessed. Comparison-only source failures do not become extra required checks for this variant.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T231529Z-culturemech-015453-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: BG11 TES no bicarb (CultureMech:015453)'
started_at: '2026-10-21T23:07:35Z'
finished_at: '2026-10-21T23:15:29Z'
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
summary: The exact named FEBA formulation supports every listed numerical rate, including
  the A5 dilution. Citric acid is grounded to sodium citrate, EDTA source metadata
  does not settle hydration, and source evidence and later owner annotations are missing
  from the generated record. Historical CultureBotHT byte equivalence remains unavailable.
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
  - path: data/merge_yaml/merged/BG11_TES_no_bicarb.yaml
    sha256: b84d058a78d55715dd537a002ee73e23db707bd0d632a4a9018ad115ba6d4252
    role: target
  - path: data/normalized_yaml/algae/bg11.yaml
    sha256: 50cf10be2d7e6c7eec48f0d9ad0911b27e4d6e52b8386cfe43924339a304c468
    role: context
  - path: data/normalized_yaml/algae/bg11_no_bicarb.yaml
    sha256: d22f6c303cef0440c5182310528655bc1bdb7b9d5d8a6aeb1d62010b232ce47f
    role: context
  - path: data/normalized_yaml/algae/bg11_nonitrogen.yaml
    sha256: 70c0b3756ed421754ff565455b8ad742a0131b86cb84f2531fa710951fbedb21
    role: context
  - path: data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
    sha256: 8b47248a8605be05777c32a1034484710f0962dd91350dc66b994ee97656d815
    role: context
  - path: data/normalized_yaml/algae/bg11c.yaml
    sha256: ea5ea6408a4783f757081d74d318df4c084936509cc2e549ab5bed5e774b864f
    role: context
  - path: data/normalized_yaml/algae/bg11c_tes.yaml
    sha256: c401a2ac26be5861818f429ae6edf4a2de4d45052298f22e5c23f56d0eb797ac
    role: context
  - path: data/normalized_yaml/algae/bg11r.yaml
    sha256: e0e7da1e0ffeea246c52a38eff9a18a5fbb95208d85e2e409743ac5e7ccd3807
    role: context
  - path: data/normalized_yaml/bacterial/CCAP_C18_BG11₀.yaml
    sha256: 35323936b16e681de153b059fe9fc7aba19935c5b39c98cd7f273776963bef59
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M3120_BG11_medium.yaml
    sha256: 7be6bd727b51c11cc3e54373c18393fb10f93008a3eed744b42a7f06abcc6a35
    role: context
  - path: data/normalized_yaml/bacterial/bg11.yaml
    sha256: 8bdcb2736d5e786086ddce316a057ab341dd4ffe17598fc0f6f733343b972453
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BG11_TES_no_bicarb.md
    sha256: 7ed18dba7aae4f2a5e41b0f156a5ea511fdd0bb24f2cc8aa1bfd39a3d0b9dfb6
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/bg11_tes_no_bicarb.md
    sha256: d008359198e9feb9976b0649a86181a73e5a2b83cdae957f593c47f803ae6b96
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/curate_organism_culture_type.py
    sha256: 8686de3d3736eaaf3702e2009a299a53819a5ba321966ab2ea01104538ca6a65
    role: context
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
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
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_culturebotht_bg11_score15.py
    sha256: dd0fdb7eeb89759865c968f788c900aa2d6b2f42c60dc2aef93afc14b33c4f36
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
  selection: Task review 407; batch 041 item 7 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding forty task batches contain
    400 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 403 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015453
targets:
- target_id: CultureMech:015453
  path: data/merge_yaml/merged/BG11_TES_no_bicarb.yaml
  label: BG11 TES no bicarb
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BG11_TES_no_bicarb.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BG11_TES_no_bicarb.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch041/407/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-041/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch041/407/strict.tsv"
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BG11_TES_no_bicarb.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BG11_TES_no_bicarb.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:015453
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
  - CultureMech:015453
- check_id: culturebothtRepository-source-access
  name: 'Exact source content access: culturebothtRepository'
  required: true
  status: unavailable
  summary: The exact public CultureBotHT endpoint returned HTTP 404 at its retained
    actual access time. The March import bytes and their historical equivalence to
    the later FEBA recipe remain unverified. Current named FEBA amounts are independently
    assessable; the missing historical source is a partial-completion limit.
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - culturebothtRepository-attempt
- check_id: culturebothtExactBG11_TES_no_bicarb-source-access
  name: 'Exact source content access: culturebothtExactBG11_TES_no_bicarb'
  required: true
  status: unavailable
  summary: The exact public CultureBotHT endpoint returned HTTP 404 at its retained
    actual access time. The March import bytes and their historical equivalence to
    the later FEBA recipe remain unverified. Current named FEBA amounts are independently
    assessable; the missing historical source is a partial-completion limit.
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - culturebothtExactBG11_TES_no_bicarb-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BG11_TES_no_bicarb.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T23:12:10Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T23:12:10Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BG11_TES_no_bicarb.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:08:03.922840Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BG11_TES_no_bicarb.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch041/407/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T23:08:04.958616Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-041/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch041/407/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BG11_TES_no_bicarb.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:08:06.033446Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BG11_TES_no_bicarb.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:08:06.910655Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T23:12:10Z'
  support: supports
  summary: './data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml:1:id: CultureMech:015453

    ./data/merge_yaml/merged/BG11_TES_no_bicarb.yaml:1:id: CultureMech:015453

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch041/source-preflight-bound/407/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T23:12:10Z'
  support: supports
  summary: 27 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 2482c4a9c2ba8884c1c43b5f11cdeb332338e90565ecd5bbf524500fe32d0c10
- evidence_id: feba-main
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media
  locator: Named block BG11_TES_no_bicarb, starting line 136
  accessed_at: '2026-10-21T07:58:53.930003Z'
  support: supports
  summary: Exact variant-specific main recipe; later FEBA revision is independent
    formula evidence, not an authenticated historical CultureBotHT copy.
  quote: "Media\tBG11_TES_no_bicarb\t\r\nDescription\tFor growing cyanobacteria, from\
    \ Luis; no sodium bicarbonate; with TES buffer\t\r\nMinimal\tTRUE\t\r\nControlled\
    \ vocabulary\tConcentration\tUnits\r\nSodium nitrate\t17.6\tmM\r\nPotassium phosphate\
    \ dibasic\t0.2\tmM\r\nMagnesium Sulfate Heptahydrate\t0.3\tmM\r\nCalcium chloride\
    \ dihydrate\t0.24\tmM\r\nCitric Acid\t28.5\tuM\r\nFerric ammonium citrate\t0.006\t\
    g/L\r\nEDTA (disodium salt)\t2.4\tuM\r\nTrace metal mix A5\t1\tX\r\nTES\t20\t\
    mM\r\n\t\t\r\n"
  snapshot_sha256: a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848
- evidence_id: feba-a5
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes
  locator: Trace metal mix A5, complete 1000 X block
  accessed_at: '2026-10-21T07:58:53.930648Z'
  support: supports
  summary: Six stock rows and explicit 1000 X strength; the main recipe requests 1
    X.
  quote: "Media\tTrace metal mix A5\t\r\nDescription\t1000X trace metal solution for\
    \ Synechococcus elongatus PCC 7942\t\r\nX\t1000\t\r\nControlled vocabulary\tConcentration\t\
    Units\r\nBoric Acid\t2.86\tg/L\r\nManganese (II) chloride tetrahydrate\t1.81\t\
    g/L\r\nZinc sulfate heptahydrate\t0.222\tg/L\r\nSodium Molybdate Dihydrate\t0.39\t\
    g/L\r\nCopper (II) sulfate pentahydrate\t0.079\tg/L\r\nCobalt(II) nitrate hexahydrate\t\
    49.4\tmg/L\r\n\t\t\r\n"
  snapshot_sha256: b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4
- evidence_id: feba-version
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commit/803273865ea9e83fab770ec4f13670db80e1180b
  locator: $.hash and $.date
  accessed_at: '2026-10-21T07:59:41.378955Z'
  support: supports
  summary: Exact FEBA revision 803273865ea9e83fab770ec4f13670db80e1180b dated 2026-09-10T16:27:42+00:00
    postdates the March import.
  snapshot_sha256: 0a4998d61b96db10c549512e2fe06718e04b687e6bbc6b2c1ea121c3c11a53ca
- evidence_id: compound-0
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 400
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "Sodium nitrate\t7631-99-4\tSigma\tS8170\t84.99\tNaNO3\t\t\tyes\t\tyes\t\
    yes\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-1
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 337
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "Potassium phosphate dibasic\t7758-11-4\tSigma\tP3786\t174.18\tK2HPO4, dibasic\
    \ anhydrous sodium phosphate\t\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-2
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 277
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "Magnesium Sulfate Heptahydrate\t10034-99-8\tSigma\tM1880\t246.47\tEpsom\
    \ salts, MgSO4 7H2O\t\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-3
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 90
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "Calcium chloride dihydrate\t10035-04-8\tSigma\tC5080\t147.01\tCalcium Chloride\
    \ Dihydrate, CaCl2*2H2O\t\t\tyes\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-4
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 119
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "Citric Acid\t77-92-9\tSigma\t251275\t192.12\t\t\t\tno\tyes\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-5
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 186
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "Ferric ammonium citrate\t1185-57-5\tSigma\tF5879\t\t\t\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-6
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 178
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "EDTA (disodium salt)\t6381-92-6\tSigma\tE6635\t336.206\t\t\t\t\t\t\t\t\r\
    \n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-7
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 1372
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "TES\t7365-44-8\t\t\t229.25\t2-[(2-Hydroxy-1,1-bis(hydroxymethyl)ethyl)amino]ethanesulfonic\
    \ acid, N-[Tris(hydroxymethyl)methyl]-2-aminoethanesulfonic acid\t\t\t\t\t\t\t\
    \r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-8
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 84
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "Boric Acid\t10043-35-3\t\t0084-01 (JT*)\t61.83\tH3BO3\t\t\tno\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-9
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 278
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "Manganese (II) chloride tetrahydrate\t13446-34-9\tSigma\tM3634\t197.91\t\
    MnCl2, manganese chloride, MnCl2 4H2O\t\t\tyes\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-10
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 474
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "Zinc sulfate heptahydrate\t7446-20-0\tSigma\tZ0251\t287.56\tzinc sulfate,\
    \ ZnSO4 7H2O\t\t\t\t\t\tyes\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-11
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 399
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "Sodium Molybdate Dihydrate\t10102-40-6\tSigma\t331058\t241.95\tNa2MoO4 2H2O,\
    \ Na2MoO4-2H2O\t\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-12
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 129
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "Copper (II) sulfate pentahydrate\t7758-99-8\tSigma\tC8027\t249.69\tBlue\
    \ Vitriol, Cupric sulfate pentahydrate, Sulfuric acid, copper(II) salt (1:1) pentahydrate,\
    \ CuSO4 5H2O, Cupric Sulfate\t\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-13
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact named compound row 124
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Source compound metadata; internal synonym and hydration tensions remain
    explicit.
  quote: "Cobalt(II) nitrate hexahydrate\t10026-22-9\t\t\t291.03\tCo(NO3)2 6H2O\t\t\
    \t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
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
- evidence_id: chebi39035
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_39035
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T22:43:54.221724Z'
  support: supports
  summary: CHEBI:39035 resolves to TES. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: ad10bad6679ad29e6afbe99ad6333c68e3dd241d4f1163fb5c5c469b3b2ca426
- evidence_id: chebi53258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:54.823692Z'
  support: supports
  summary: CHEBI:53258 resolves to sodium citrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2a35c6dc3532c2276c6b19aef0992260e14b1fc36423fa3eb812bb94f63c4371
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
- evidence_id: chebi64734
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64734
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.449302Z'
  support: supports
  summary: CHEBI:64734 resolves to EDTA disodium salt (anhydrous). Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 95b7557b1867dcce37a69714dbad0a6a6a6c11c66dde39c6793a2307a7fb0e1c
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
- evidence_id: chebi86214
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86214
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.123051Z'
  support: supports
  summary: CHEBI:86214 resolves to cobalt dinitrate hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 90cf3337643bc22bd3940bfbdee70a144b13af549ea12534184385f036b4633c
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T23:12:10Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: citric-acid-candidate
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30769
  locator: Exact OLS CHEBI:30769 scientific properties
  accessed_at: '2026-10-21T11:01:47.015892Z'
  support: supports
  summary: Citric acid is a distinct nonobsolete acid entity, CAS 77-92-9, formula
    C6H8O7; candidate correction is separate from this read-only review.
  snapshot_sha256: caa0ca256c3120bc99d649d132215c88d06cdff463dffac90dcecef930e7c429
- evidence_id: culturebothtRepository-attempt
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/CultureBotHT
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:53:13.557900Z'
  support: context_only
  summary: The exact public CultureBotHT endpoint returned HTTP 404 at its retained
    actual access time. The March import bytes and their historical equivalence to
    the later FEBA recipe remain unverified. Current named FEBA amounts are independently
    assessable; the missing historical source is a partial-completion limit.
  snapshot_sha256: 4f50e254a719a6b1b06b529bdaa08980e4acf0878aad0090cba7771f6ebdf0b9
- evidence_id: culturebothtExactBG11_TES_no_bicarb-attempt
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BG11_TES_no_bicarb.yaml
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:53:14.091165Z'
  support: context_only
  summary: The exact public CultureBotHT endpoint returned HTTP 404 at its retained
    actual access time. The March import bytes and their historical equivalence to
    the later FEBA recipe remain unverified. Current named FEBA amounts are independently
    assessable; the missing historical source is a partial-completion limit.
  snapshot_sha256: d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed
- evidence_id: forms
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch041/407/chemical-form-inventory.json
  locator: Every target and maintained-owner ingredient form, exact source compound
    fields and OLS scientific properties
  accessed_at: '2026-10-21T23:12:10Z'
  support: context_only
  summary: All supplied-form decisions are explicit; exact identifier/label validity
    is separate from source correspondence.
  snapshot_sha256: 2310325c8b9c4806be1762ec34d34674fbb753ab11529bb85415908e12ef45ba
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch041/407/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T23:12:10Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: ed51c35f03aaf213ad197651ff332a520cc924ff39a95c32a5c926708015891b
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BG11_TES_no_bicarb.yaml; data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T23:12:10Z'
  support: context_only
  summary: '[{"input": "target", "events": 4, "timestamp_issues": []}, {"input": "data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml",
    "events": 4, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_culturebotht_bg11_score15.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:12:10Z'
  support: context_only
  summary: 'Full current repair inspected: exact ID/source/name signature guards,
    media_term/references/flags/history updates; it does not validate amounts, chemical
    forms, historical source availability or attached claim evidence. No execution
    or inferred past causation.'
  snapshot_sha256: dd0fdb7eeb89759865c968f788c900aa2d6b2f42c60dc2aef93afc14b33c4f36
- evidence_id: historical-report-0
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/bg11_tes_no_bicarb.md
  locator: Exact matching historical report header and all ingredient decision rows
  accessed_at: '2026-10-21T23:12:10Z'
  support: context_only
  summary: Derivative diagnostic reports missing attached source evidence and not-performed
    source checks. Current FEBA comparison supersedes that absence of assessment,
    not the immutable report bytes.
  snapshot_sha256: d008359198e9feb9976b0649a86181a73e5a2b83cdae957f593c47f803ae6b96
- evidence_id: historical-report-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BG11_TES_no_bicarb.md
  locator: Exact matching historical report header and all ingredient decision rows
  accessed_at: '2026-10-21T23:12:10Z'
  support: context_only
  summary: Derivative diagnostic reports missing attached source evidence and not-performed
    source checks. Current FEBA comparison supersedes that absence of assessment,
    not the immutable report bytes.
  snapshot_sha256: 7ed18dba7aae4f2a5e41b0f156a5ea511fdd0bb24f2cc8aa1bfd39a3d0b9dfb6
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '14 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 14/14
    primary and 0/14 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi31440
  - chebi31604
  - chebi31795
  - chebi32312
  - chebi33118
  - chebi39035
  - chebi53258
  - chebi63005
  - chebi64734
  - chebi75213
  - chebi86158
  - chebi86214
  - chebi86368
  details: 'Instance coverage on a 0–100 percent scale, denominator 14: primary 100.00%;
    secondary 0.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 64 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Evidence-only marks source-supported numerals whose scoped
    evidence must be attached; verified is reserved for an existing value, unit and
    basis with matching attached evidence.
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Sodium nitrate\"\
    ,\n    \"stage\": \"Main medium rate, exact named FEBA variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\",\n        \"field_path\": \"\
    ingredients[0].concentration\",\n        \"stored\": {\n          \"value\": \"\
    17.6\",\n          \"unit\": \"MILLIMOLAR\"\n        }\n      }\n    ],\n    \"\
    desired\": {\n      \"value\": \"17.6\",\n      \"unit\": \"MILLIMOLAR\"\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_media\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row Sodium nitrate\"\
    ,\n        \"exact_source_quote\": \"Sodium nitrate\\t17.6\\tmM\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion.\"\n  },\n  {\n    \"decision_id\"\
    : \"q2\",\n    \"name\": \"Sodium nitrate\",\n    \"stage\": \"Main medium rate,\
    \ exact named FEBA variant\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"17.6\",\n          \"unit\": \"MILLIMOLAR\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"17.6\",\n    \
    \  \"unit\": \"MILLIMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row Sodium nitrate\"\
    ,\n        \"exact_source_quote\": \"Sodium nitrate\\t17.6\\tmM\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion.\"\n  },\n  {\n    \"decision_id\"\
    : \"q3\",\n    \"name\": \"Potassium phosphate dibasic\",\n    \"stage\": \"Main\
    \ medium rate, exact named FEBA variant\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"MILLIMOLAR\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.2\",\n      \"\
    unit\": \"MILLIMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row Potassium phosphate\
    \ dibasic\",\n        \"exact_source_quote\": \"Potassium phosphate dibasic\\\
    t0.2\\tmM\\n\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion.\"\n  },\n  {\n    \"decision_id\"\
    : \"q4\",\n    \"name\": \"Potassium phosphate dibasic\",\n    \"stage\": \"Main\
    \ medium rate, exact named FEBA variant\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"MILLIMOLAR\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.2\",\n      \"\
    unit\": \"MILLIMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row Potassium phosphate\
    \ dibasic\",\n        \"exact_source_quote\": \"Potassium phosphate dibasic\\\
    t0.2\\tmM\\n\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion.\"\n  },\n  {\n    \"decision_id\"\
    : \"q5\",\n    \"name\": \"Magnesium Sulfate Heptahydrate\",\n    \"stage\": \"\
    Main medium rate, exact named FEBA variant\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"MILLIMOLAR\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.3\",\n      \"\
    unit\": \"MILLIMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row Magnesium Sulfate\
    \ Heptahydrate\",\n        \"exact_source_quote\": \"Magnesium Sulfate Heptahydrate\\\
    t0.3\\tmM\\n\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion.\"\n  },\n  {\n    \"decision_id\"\
    : \"q6\",\n    \"name\": \"Magnesium Sulfate Heptahydrate\",\n    \"stage\": \"\
    Main medium rate, exact named FEBA variant\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"MILLIMOLAR\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.3\",\n      \"\
    unit\": \"MILLIMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row Magnesium Sulfate\
    \ Heptahydrate\",\n        \"exact_source_quote\": \"Magnesium Sulfate Heptahydrate\\\
    t0.3\\tmM\\n\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion.\"\n  },\n  {\n    \"decision_id\"\
    : \"q7\",\n    \"name\": \"Calcium chloride dihydrate\",\n    \"stage\": \"Main\
    \ medium rate, exact named FEBA variant\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.24\",\n          \"unit\": \"MILLIMOLAR\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.24\",\n    \
    \  \"unit\": \"MILLIMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row Calcium chloride\
    \ dihydrate\",\n        \"exact_source_quote\": \"Calcium chloride dihydrate\\\
    t0.24\\tmM\\n\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion.\"\n  },\n  {\n    \"decision_id\"\
    : \"q8\",\n    \"name\": \"Calcium chloride dihydrate\",\n    \"stage\": \"Main\
    \ medium rate, exact named FEBA variant\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.24\",\n          \"unit\": \"MILLIMOLAR\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.24\",\n    \
    \  \"unit\": \"MILLIMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row Calcium chloride\
    \ dihydrate\",\n        \"exact_source_quote\": \"Calcium chloride dihydrate\\\
    t0.24\\tmM\\n\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion.\"\n  },\n  {\n    \"decision_id\"\
    : \"q9\",\n    \"name\": \"Citric Acid\",\n    \"stage\": \"Main medium rate,\
    \ exact named FEBA variant\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"28.5\",\n          \"unit\": \"MICROMOLAR\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"28.5\",\n    \
    \  \"unit\": \"MICROMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row Citric Acid\",\n\
    \        \"exact_source_quote\": \"Citric Acid\\t28.5\\tuM\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion. This does not validate the sodium-citrate\
    \ identifier assigned to source citric acid.\"\n  },\n  {\n    \"decision_id\"\
    : \"q10\",\n    \"name\": \"Citric Acid\",\n    \"stage\": \"Main medium rate,\
    \ exact named FEBA variant\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"28.5\",\n          \"unit\": \"MICROMOLAR\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"28.5\",\n    \
    \  \"unit\": \"MICROMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row Citric Acid\",\n\
    \        \"exact_source_quote\": \"Citric Acid\\t28.5\\tuM\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion. This does not validate the sodium-citrate\
    \ identifier assigned to source citric acid.\"\n  },\n  {\n    \"decision_id\"\
    : \"q11\",\n    \"name\": \"Ferric ammonium citrate\",\n    \"stage\": \"Main\
    \ medium rate, exact named FEBA variant\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.006\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row Ferric ammonium\
    \ citrate\",\n        \"exact_source_quote\": \"Ferric ammonium citrate\\t0.006\\\
    tg/L\\n\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion.\"\n  },\n  {\n    \"decision_id\"\
    : \"q12\",\n    \"name\": \"Ferric ammonium citrate\",\n    \"stage\": \"Main\
    \ medium rate, exact named FEBA variant\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.006\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row Ferric ammonium\
    \ citrate\",\n        \"exact_source_quote\": \"Ferric ammonium citrate\\t0.006\\\
    tg/L\\n\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion.\"\n  },\n  {\n    \"decision_id\"\
    : \"q13\",\n    \"name\": \"EDTA (disodium salt)\",\n    \"stage\": \"Main medium\
    \ rate, exact named FEBA variant\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.4\",\n          \"unit\": \"MICROMOLAR\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"2.4\",\n      \"\
    unit\": \"MICROMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row EDTA (disodium\
    \ salt)\",\n        \"exact_source_quote\": \"EDTA (disodium salt)\\t2.4\\tuM\\\
    n\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion. Hydration remains unresolved independently\
    \ of the verified source numeral.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n\
    \    \"name\": \"EDTA (disodium salt)\",\n    \"stage\": \"Main medium rate, exact\
    \ named FEBA variant\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.4\",\n          \"unit\": \"MICROMOLAR\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"2.4\",\n      \"\
    unit\": \"MICROMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row EDTA (disodium\
    \ salt)\",\n        \"exact_source_quote\": \"EDTA (disodium salt)\\t2.4\\tuM\\\
    n\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion. Hydration remains unresolved independently\
    \ of the verified source numeral.\"\n  },\n  {\n    \"decision_id\": \"q15\",\n\
    \    \"name\": \"TES\",\n    \"stage\": \"Main medium rate, exact named FEBA variant\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\",\n      \
    \  \"field_path\": \"ingredients[13].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"20\",\n          \"unit\": \"MILLIMOLAR\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"20\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row TES\",\n      \
    \  \"exact_source_quote\": \"TES\\t20\\tmM\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion.\"\n  },\n  {\n    \"decision_id\"\
    : \"q16\",\n    \"name\": \"TES\",\n    \"stage\": \"Main medium rate, exact named\
    \ FEBA variant\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"MILLIMOLAR\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"20\",\n      \"\
    unit\": \"MILLIMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb direct row TES\",\n      \
    \  \"exact_source_quote\": \"TES\\t20\\tmM\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. Direct source concentration, without\
    \ batch-volume or mass-to-molar conversion.\"\n  },\n  {\n    \"decision_id\"\
    : \"q17\",\n    \"name\": \"Boric Acid\",\n    \"stage\": \"Main medium rate,\
    \ exact named FEBA variant\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00286\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.00286\",\n \
    \     \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock row Boric Acid\",\n        \"exact_source_quote\"\
    : \"Boric Acid\\t2.86\\tg/L\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_media\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb A5 receiving-strength row\"\
    ,\n        \"exact_source_quote\": \"Trace metal mix A5\\t1\\tX\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock-strength declaration\",\n        \"\
    exact_source_quote\": \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. The stock rate is divided by 1000 for\
    \ 1 X in the receiving medium; decimal floating serialization is not a substantive\
    \ discrepancy. No ml dose or measured final volume is inferred.\"\n  },\n  {\n\
    \    \"decision_id\": \"q18\",\n    \"name\": \"Boric Acid\",\n    \"stage\":\
    \ \"Main medium rate, exact named FEBA variant\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00286\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.00286\",\n \
    \     \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock row Boric Acid\",\n        \"exact_source_quote\"\
    : \"Boric Acid\\t2.86\\tg/L\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_media\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb A5 receiving-strength row\"\
    ,\n        \"exact_source_quote\": \"Trace metal mix A5\\t1\\tX\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock-strength declaration\",\n        \"\
    exact_source_quote\": \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. The stock rate is divided by 1000 for\
    \ 1 X in the receiving medium; decimal floating serialization is not a substantive\
    \ discrepancy. No ml dose or measured final volume is inferred.\"\n  },\n  {\n\
    \    \"decision_id\": \"q19\",\n    \"name\": \"Manganese (II) chloride tetrahydrate\"\
    ,\n    \"stage\": \"Main medium rate, exact named FEBA variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\",\n        \"field_path\": \"\
    ingredients[8].concentration\",\n        \"stored\": {\n          \"value\": \"\
    0.0018100000000000002\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": \"0.00181\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock row Manganese (II) chloride tetrahydrate\"\
    ,\n        \"exact_source_quote\": \"Manganese (II) chloride tetrahydrate\\t1.81\\\
    tg/L\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_media\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb A5 receiving-strength row\"\
    ,\n        \"exact_source_quote\": \"Trace metal mix A5\\t1\\tX\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock-strength declaration\",\n        \"\
    exact_source_quote\": \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. The stock rate is divided by 1000 for\
    \ 1 X in the receiving medium; decimal floating serialization is not a substantive\
    \ discrepancy. No ml dose or measured final volume is inferred.\"\n  },\n  {\n\
    \    \"decision_id\": \"q20\",\n    \"name\": \"Manganese (II) chloride tetrahydrate\"\
    ,\n    \"stage\": \"Main medium rate, exact named FEBA variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\",\n        \"field_path\"\
    : \"ingredients[8].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0018100000000000002\",\n          \"unit\": \"G_PER_L\"\n        }\n   \
    \   }\n    ],\n    \"desired\": {\n      \"value\": \"0.00181\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock row Manganese (II) chloride tetrahydrate\"\
    ,\n        \"exact_source_quote\": \"Manganese (II) chloride tetrahydrate\\t1.81\\\
    tg/L\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_media\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb A5 receiving-strength row\"\
    ,\n        \"exact_source_quote\": \"Trace metal mix A5\\t1\\tX\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock-strength declaration\",\n        \"\
    exact_source_quote\": \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. The stock rate is divided by 1000 for\
    \ 1 X in the receiving medium; decimal floating serialization is not a substantive\
    \ discrepancy. No ml dose or measured final volume is inferred.\"\n  },\n  {\n\
    \    \"decision_id\": \"q21\",\n    \"name\": \"Zinc sulfate heptahydrate\",\n\
    \    \"stage\": \"Main medium rate, exact named FEBA variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\",\n        \"field_path\": \"\
    ingredients[9].concentration\",\n        \"stored\": {\n          \"value\": \"\
    0.000222\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n   \
    \ \"desired\": {\n      \"value\": \"0.000222\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock row Zinc sulfate heptahydrate\",\n \
    \       \"exact_source_quote\": \"Zinc sulfate heptahydrate\\t0.222\\tg/L\\n\"\
    ,\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_media\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb A5 receiving-strength row\"\
    ,\n        \"exact_source_quote\": \"Trace metal mix A5\\t1\\tX\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock-strength declaration\",\n        \"\
    exact_source_quote\": \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. The stock rate is divided by 1000 for\
    \ 1 X in the receiving medium; decimal floating serialization is not a substantive\
    \ discrepancy. No ml dose or measured final volume is inferred.\"\n  },\n  {\n\
    \    \"decision_id\": \"q22\",\n    \"name\": \"Zinc sulfate heptahydrate\",\n\
    \    \"stage\": \"Main medium rate, exact named FEBA variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\",\n        \"field_path\"\
    : \"ingredients[9].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.000222\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n\
    \    \"desired\": {\n      \"value\": \"0.000222\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock row Zinc sulfate heptahydrate\",\n \
    \       \"exact_source_quote\": \"Zinc sulfate heptahydrate\\t0.222\\tg/L\\n\"\
    ,\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_media\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb A5 receiving-strength row\"\
    ,\n        \"exact_source_quote\": \"Trace metal mix A5\\t1\\tX\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock-strength declaration\",\n        \"\
    exact_source_quote\": \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. The stock rate is divided by 1000 for\
    \ 1 X in the receiving medium; decimal floating serialization is not a substantive\
    \ discrepancy. No ml dose or measured final volume is inferred.\"\n  },\n  {\n\
    \    \"decision_id\": \"q23\",\n    \"name\": \"Sodium Molybdate Dihydrate\",\n\
    \    \"stage\": \"Main medium rate, exact named FEBA variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\",\n        \"field_path\": \"\
    ingredients[10].concentration\",\n        \"stored\": {\n          \"value\":\
    \ \"0.00039000000000000005\",\n          \"unit\": \"G_PER_L\"\n        }\n  \
    \    }\n    ],\n    \"desired\": {\n      \"value\": \"0.00039\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock row Sodium Molybdate Dihydrate\",\n\
    \        \"exact_source_quote\": \"Sodium Molybdate Dihydrate\\t0.39\\tg/L\\n\"\
    ,\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_media\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb A5 receiving-strength row\"\
    ,\n        \"exact_source_quote\": \"Trace metal mix A5\\t1\\tX\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock-strength declaration\",\n        \"\
    exact_source_quote\": \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. The stock rate is divided by 1000 for\
    \ 1 X in the receiving medium; decimal floating serialization is not a substantive\
    \ discrepancy. No ml dose or measured final volume is inferred.\"\n  },\n  {\n\
    \    \"decision_id\": \"q24\",\n    \"name\": \"Sodium Molybdate Dihydrate\",\n\
    \    \"stage\": \"Main medium rate, exact named FEBA variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\",\n        \"field_path\"\
    : \"ingredients[10].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.00039000000000000005\",\n          \"unit\": \"G_PER_L\"\n        }\n  \
    \    }\n    ],\n    \"desired\": {\n      \"value\": \"0.00039\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock row Sodium Molybdate Dihydrate\",\n\
    \        \"exact_source_quote\": \"Sodium Molybdate Dihydrate\\t0.39\\tg/L\\n\"\
    ,\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_media\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb A5 receiving-strength row\"\
    ,\n        \"exact_source_quote\": \"Trace metal mix A5\\t1\\tX\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock-strength declaration\",\n        \"\
    exact_source_quote\": \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. The stock rate is divided by 1000 for\
    \ 1 X in the receiving medium; decimal floating serialization is not a substantive\
    \ discrepancy. No ml dose or measured final volume is inferred.\"\n  },\n  {\n\
    \    \"decision_id\": \"q25\",\n    \"name\": \"Copper (II) sulfate pentahydrate\"\
    ,\n    \"stage\": \"Main medium rate, exact named FEBA variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\",\n        \"field_path\": \"\
    ingredients[11].concentration\",\n        \"stored\": {\n          \"value\":\
    \ \"7.9e-05\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n\
    \    \"desired\": {\n      \"value\": \"0.000079\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock row Copper (II) sulfate pentahydrate\"\
    ,\n        \"exact_source_quote\": \"Copper (II) sulfate pentahydrate\\t0.079\\\
    tg/L\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_media\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb A5 receiving-strength row\"\
    ,\n        \"exact_source_quote\": \"Trace metal mix A5\\t1\\tX\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock-strength declaration\",\n        \"\
    exact_source_quote\": \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. The stock rate is divided by 1000 for\
    \ 1 X in the receiving medium; decimal floating serialization is not a substantive\
    \ discrepancy. No ml dose or measured final volume is inferred.\"\n  },\n  {\n\
    \    \"decision_id\": \"q26\",\n    \"name\": \"Copper (II) sulfate pentahydrate\"\
    ,\n    \"stage\": \"Main medium rate, exact named FEBA variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\",\n        \"field_path\"\
    : \"ingredients[11].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"7.9e-05\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n\
    \    \"desired\": {\n      \"value\": \"0.000079\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock row Copper (II) sulfate pentahydrate\"\
    ,\n        \"exact_source_quote\": \"Copper (II) sulfate pentahydrate\\t0.079\\\
    tg/L\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_media\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb A5 receiving-strength row\"\
    ,\n        \"exact_source_quote\": \"Trace metal mix A5\\t1\\tX\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock-strength declaration\",\n        \"\
    exact_source_quote\": \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. The stock rate is divided by 1000 for\
    \ 1 X in the receiving medium; decimal floating serialization is not a substantive\
    \ discrepancy. No ml dose or measured final volume is inferred.\"\n  },\n  {\n\
    \    \"decision_id\": \"q27\",\n    \"name\": \"Cobalt(II) nitrate hexahydrate\"\
    ,\n    \"stage\": \"Main medium rate, exact named FEBA variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\",\n        \"field_path\": \"\
    ingredients[12].concentration\",\n        \"stored\": {\n          \"value\":\
    \ \"0.0494\",\n          \"unit\": \"MG_PER_L\"\n        }\n      }\n    ],\n\
    \    \"desired\": {\n      \"value\": \"0.0494\",\n      \"unit\": \"MG_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock row Cobalt(II) nitrate hexahydrate\"\
    ,\n        \"exact_source_quote\": \"Cobalt(II) nitrate hexahydrate\\t49.4\\tmg/L\\\
    n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_media\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb A5 receiving-strength row\"\
    ,\n        \"exact_source_quote\": \"Trace metal mix A5\\t1\\tX\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock-strength declaration\",\n        \"\
    exact_source_quote\": \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. The stock rate is divided by 1000 for\
    \ 1 X in the receiving medium; decimal floating serialization is not a substantive\
    \ discrepancy. No ml dose or measured final volume is inferred.\"\n  },\n  {\n\
    \    \"decision_id\": \"q28\",\n    \"name\": \"Cobalt(II) nitrate hexahydrate\"\
    ,\n    \"stage\": \"Main medium rate, exact named FEBA variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\",\n        \"field_path\"\
    : \"ingredients[12].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0494\",\n          \"unit\": \"MG_PER_L\"\n        }\n      }\n    ],\n\
    \    \"desired\": {\n      \"value\": \"0.0494\",\n      \"unit\": \"MG_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock row Cobalt(II) nitrate hexahydrate\"\
    ,\n        \"exact_source_quote\": \"Cobalt(II) nitrate hexahydrate\\t49.4\\tmg/L\\\
    n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_media\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BG11_TES_no_bicarb A5 receiving-strength row\"\
    ,\n        \"exact_source_quote\": \"Trace metal mix A5\\t1\\tX\\n\",\n      \
    \  \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock-strength declaration\",\n        \"\
    exact_source_quote\": \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Numerical value and unit\
    \ are supported for the named ingredient. The stock rate is divided by 1000 for\
    \ 1 X in the receiving medium; decimal floating serialization is not a substantive\
    \ discrepancy. No ml dose or measured final volume is inferred.\"\n  },\n  {\n\
    \    \"decision_id\": \"q29\",\n    \"name\": \"Boric Acid\",\n    \"stage\":\
    \ \"Source-only A5 stock concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [],\n    \"desired\": {\n      \"stock_value\": \"2.86\"\
    ,\n      \"stock_unit\": \"g/L\",\n      \"stock_strength_X\": 1000\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\",\n\
    \        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 exact constituent row\",\n        \"exact_source_quote\"\
    : \"Boric Acid\\t2.86\\tg/L\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock strength\",\n        \"exact_source_quote\"\
    : \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Retain the stock stage in\
    \ attached dilution evidence or a separately curated stock; never substitute this\
    \ undiluted value into the main medium.\"\n  },\n  {\n    \"decision_id\": \"\
    q30\",\n    \"name\": \"Manganese (II) chloride tetrahydrate\",\n    \"stage\"\
    : \"Source-only A5 stock concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [],\n    \"desired\": {\n      \"stock_value\": \"1.81\"\
    ,\n      \"stock_unit\": \"g/L\",\n      \"stock_strength_X\": 1000\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\",\n\
    \        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 exact constituent row\",\n        \"exact_source_quote\"\
    : \"Manganese (II) chloride tetrahydrate\\t1.81\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock strength\",\n        \"exact_source_quote\"\
    : \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Retain the stock stage in\
    \ attached dilution evidence or a separately curated stock; never substitute this\
    \ undiluted value into the main medium.\"\n  },\n  {\n    \"decision_id\": \"\
    q31\",\n    \"name\": \"Zinc sulfate heptahydrate\",\n    \"stage\": \"Source-only\
    \ A5 stock concentration\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [],\n    \"desired\": {\n      \"stock_value\": \"0.222\",\n      \"stock_unit\"\
    : \"g/L\",\n      \"stock_strength_X\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 exact constituent row\",\n        \"exact_source_quote\"\
    : \"Zinc sulfate heptahydrate\\t0.222\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock strength\",\n        \"exact_source_quote\"\
    : \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Retain the stock stage in\
    \ attached dilution evidence or a separately curated stock; never substitute this\
    \ undiluted value into the main medium.\"\n  },\n  {\n    \"decision_id\": \"\
    q32\",\n    \"name\": \"Sodium Molybdate Dihydrate\",\n    \"stage\": \"Source-only\
    \ A5 stock concentration\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [],\n    \"desired\": {\n      \"stock_value\": \"0.39\",\n      \"stock_unit\"\
    : \"g/L\",\n      \"stock_strength_X\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 exact constituent row\",\n        \"exact_source_quote\"\
    : \"Sodium Molybdate Dihydrate\\t0.39\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock strength\",\n        \"exact_source_quote\"\
    : \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Retain the stock stage in\
    \ attached dilution evidence or a separately curated stock; never substitute this\
    \ undiluted value into the main medium.\"\n  },\n  {\n    \"decision_id\": \"\
    q33\",\n    \"name\": \"Copper (II) sulfate pentahydrate\",\n    \"stage\": \"\
    Source-only A5 stock concentration\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [],\n    \"desired\": {\n      \"stock_value\": \"0.079\"\
    ,\n      \"stock_unit\": \"g/L\",\n      \"stock_strength_X\": 1000\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\",\n\
    \        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 exact constituent row\",\n        \"exact_source_quote\"\
    : \"Copper (II) sulfate pentahydrate\\t0.079\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock strength\",\n        \"exact_source_quote\"\
    : \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Retain the stock stage in\
    \ attached dilution evidence or a separately curated stock; never substitute this\
    \ undiluted value into the main medium.\"\n  },\n  {\n    \"decision_id\": \"\
    q34\",\n    \"name\": \"Cobalt(II) nitrate hexahydrate\",\n    \"stage\": \"Source-only\
    \ A5 stock concentration\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [],\n    \"desired\": {\n      \"stock_value\": \"49.4\",\n      \"stock_unit\"\
    : \"mg/L\",\n      \"stock_strength_X\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 exact constituent row\",\n        \"exact_source_quote\"\
    : \"Cobalt(II) nitrate hexahydrate\\t49.4\\tmg/L\\n\",\n        \"snapshot_sha256\"\
    : \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"A5 stock strength\",\n        \"exact_source_quote\"\
    : \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Retain the stock stage in\
    \ attached dilution evidence or a separately curated stock; never substitute this\
    \ undiluted value into the main medium.\"\n  },\n  {\n    \"decision_id\": \"\
    q35\",\n    \"name\": \"A5 receiving dose\",\n    \"stage\": \"Source relative\
    \ stock strength\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [],\n    \"desired\": {\n      \"receiving_strength_X\": 1,\n      \"stock_strength_X\"\
    : 1000,\n      \"liquid_dose_ml\": null\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"feba_media\",\n        \"source_url\": \"\
    https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"Exact main A5 row\",\n        \"exact_source_quote\"\
    : \"Trace metal mix A5\\t1\\tX\\n\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      },\n      {\n        \"source_key\": \"feba_mixes\",\n      \
    \  \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Exact stock X declaration\",\n        \"exact_source_quote\"\
    : \"X\\t1000\\t\\n\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Explicit relative strengths\
    \ justify the ratio only. No liquid addition volume is printed, and no extra final-volume\
    \ claim is made.\"\n  },\n  {\n    \"decision_id\": \"q36\",\n    \"name\": \"\
    Sodium nitrate\",\n    \"stage\": \"Stored ingredient identity metadata; numerical\
    \ CAS/MW and mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 7631-99-4; MW: 84.99\"\n   \
    \   }\n    ],\n    \"desired\": {\n      \"source_compound_fields\": {\n     \
    \   \"Compound\": \"Sodium nitrate\",\n        \"CAS\": \"7631-99-4\",\n     \
    \   \"Company\": \"Sigma\",\n        \"CatalogNumber\": \"S8170\",\n        \"\
    FW\": \"84.99\",\n        \"Synonyms\": \"NaNO3\",\n        \"Notes\": \"\",\n\
    \        \"Hans80Anti\": \"\",\n        \"Hans80metals\": \"yes\",\n        \"\
    FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"yes\",\n        \"FEBA_stress\"\
    : \"yes\",\n        \"All_star\": \"\"\n      }\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 400\",\n        \"exact_source_quote\"\
    : \"Sodium nitrate\\t7631-99-4\\tSigma\\tS8170\\t84.99\\tNaNO3\\t\\t\\tyes\\t\\\
    tyes\\tyes\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q37\",\n    \"name\": \"Potassium phosphate dibasic\"\
    ,\n    \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and\
    \ mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"CAS:\
    \ 7758-11-4; MW: 174.18\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Potassium phosphate dibasic\",\n        \"CAS\":\
    \ \"7758-11-4\",\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\":\
    \ \"P3786\",\n        \"FW\": \"174.18\",\n        \"Synonyms\": \"K2HPO4, dibasic\
    \ anhydrous sodium phosphate\",\n        \"Notes\": \"\",\n        \"Hans80Anti\"\
    : \"\",\n        \"Hans80metals\": \"\",\n        \"FEBA_carbon\": \"\",\n   \
    \     \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\"\
    : \"\"\n      }\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 337\",\n        \"exact_source_quote\"\
    : \"Potassium phosphate dibasic\\t7758-11-4\\tSigma\\tP3786\\t174.18\\tK2HPO4,\
    \ dibasic anhydrous sodium phosphate\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source preferred name, K2HPO4,\
    \ CAS 7758-11-4 and FW 174.18 support dipotassium hydrogen phosphate. Source synonym\
    \ dibasic anhydrous sodium phosphate is internally inconsistent. OLS has a trihydrate\
    \ synonym but its formula/mass encode the unhydrated salt; neither stray synonym\
    \ establishes an actual source hydrate or sodium salt. Historical mapping confidence\
    \ 0.90, where present, is a local algorithm assertion, not externally verified\
    \ probability.\"\n  },\n  {\n    \"decision_id\": \"q38\",\n    \"name\": \"Magnesium\
    \ Sulfate Heptahydrate\",\n    \"stage\": \"Stored ingredient identity metadata;\
    \ numerical CAS/MW and mapping-confidence text\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"CAS:\
    \ 10034-99-8; MW: 246.47\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Magnesium Sulfate Heptahydrate\",\n        \"CAS\"\
    : \"10034-99-8\",\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\"\
    : \"M1880\",\n        \"FW\": \"246.47\",\n        \"Synonyms\": \"Epsom salts,\
    \ MgSO4 7H2O\",\n        \"Notes\": \"\",\n        \"Hans80Anti\": \"\",\n   \
    \     \"Hans80metals\": \"\",\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\"\
    : \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\": \"\"\n      }\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 277\",\n        \"exact_source_quote\"\
    : \"Magnesium Sulfate Heptahydrate\\t10034-99-8\\tSigma\\tM1880\\t246.47\\tEpsom\
    \ salts, MgSO4 7H2O\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"\
    25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n        \"\
    quote_representation\": \"UTF-8 source decoded with universal newlines; tabs and\
    \ all other characters retained. Raw external evidence preserves original CRLF.\"\
    \n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate or buffer\
    \ agrees with the asserted chemical identity. Explicit hydration is retained;\
    \ source compound identifiers and formula metadata do not supply new preparation\
    \ conditions. Historical mapping confidence 0.90, where present, is a local algorithm\
    \ assertion, not externally verified probability.\"\n  },\n  {\n    \"decision_id\"\
    : \"q39\",\n    \"name\": \"Calcium chloride dihydrate\",\n    \"stage\": \"Stored\
    \ ingredient identity metadata; numerical CAS/MW and mapping-confidence text\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\",\n      \
    \  \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 10035-04-8; MW: 147.01\"\n      }\n    ],\n    \"desired\"\
    : {\n      \"source_compound_fields\": {\n        \"Compound\": \"Calcium chloride\
    \ dihydrate\",\n        \"CAS\": \"10035-04-8\",\n        \"Company\": \"Sigma\"\
    ,\n        \"CatalogNumber\": \"C5080\",\n        \"FW\": \"147.01\",\n      \
    \  \"Synonyms\": \"Calcium Chloride Dihydrate, CaCl2*2H2O\",\n        \"Notes\"\
    : \"\",\n        \"Hans80Anti\": \"\",\n        \"Hans80metals\": \"yes\",\n \
    \       \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\"\
    : \"\",\n        \"All_star\": \"\"\n      }\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 90\",\n        \"exact_source_quote\"\
    : \"Calcium chloride dihydrate\\t10035-04-8\\tSigma\\tC5080\\t147.01\\tCalcium\
    \ Chloride Dihydrate, CaCl2*2H2O\\t\\t\\tyes\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q40\",\n    \"name\": \"Citric Acid\",\n    \"stage\"\
    : \"Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence\
    \ text\",\n    \"decision\": \"conflict\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\",\n    \
    \    \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 77-92-9; MW: 192.12\"\n    \
    \  }\n    ],\n    \"desired\": {\n      \"source_compound_fields\": {\n      \
    \  \"Compound\": \"Citric Acid\",\n        \"CAS\": \"77-92-9\",\n        \"Company\"\
    : \"Sigma\",\n        \"CatalogNumber\": \"251275\",\n        \"FW\": \"192.12\"\
    ,\n        \"Synonyms\": \"\",\n        \"Notes\": \"\",\n        \"Hans80Anti\"\
    : \"\",\n        \"Hans80metals\": \"no\",\n        \"FEBA_carbon\": \"yes\",\n\
    \        \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\": \"\",\n        \"\
    All_star\": \"\"\n      }\n    },\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 119\",\n        \"exact_source_quote\"\
    : \"Citric Acid\\t77-92-9\\tSigma\\t251275\\t192.12\\t\\t\\t\\tno\\tyes\\t\\t\\\
    t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source citric acid and CAS\
    \ 77-92-9 differ from CHEBI:53258, the trisodium citrate salt. CHEBI:30769 is\
    \ the supported acid candidate; retain the source amount. Historical mapping confidence\
    \ 0.90, where present, is a local algorithm assertion, not externally verified\
    \ probability.\"\n  },\n  {\n    \"decision_id\": \"q41\",\n    \"name\": \"Ferric\
    \ ammonium citrate\",\n    \"stage\": \"Stored ingredient identity metadata; numerical\
    \ CAS/MW and mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 1185-57-5\"\n      }\n    ],\n\
    \    \"desired\": {\n      \"source_compound_fields\": {\n        \"Compound\"\
    : \"Ferric ammonium citrate\",\n        \"CAS\": \"1185-57-5\",\n        \"Company\"\
    : \"Sigma\",\n        \"CatalogNumber\": \"F5879\",\n        \"FW\": \"\",\n \
    \       \"Synonyms\": \"\",\n        \"Notes\": \"\",\n        \"Hans80Anti\"\
    : \"\",\n        \"Hans80metals\": \"\",\n        \"FEBA_carbon\": \"\",\n   \
    \     \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\"\
    : \"\"\n      }\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 186\",\n        \"exact_source_quote\"\
    : \"Ferric ammonium citrate\\t1185-57-5\\tSigma\\tF5879\\t\\t\\t\\t\\t\\t\\t\\\
    t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source ferric ammonium citrate\
    \ matches the asserted mixture identity. OLS describes indefinite composition;\
    \ no fixed molar mass or molecular concentration is inferred. Historical mapping\
    \ confidence 0.90, where present, is a local algorithm assertion, not externally\
    \ verified probability.\"\n  },\n  {\n    \"decision_id\": \"q42\",\n    \"name\"\
    : \"EDTA (disodium salt)\",\n    \"stage\": \"Stored ingredient identity metadata;\
    \ numerical CAS/MW and mapping-confidence text\",\n    \"decision\": \"conflict\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"CAS:\
    \ 6381-92-6; MW: 336.206\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"EDTA (disodium salt)\",\n        \"CAS\": \"6381-92-6\"\
    ,\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\": \"E6635\",\n  \
    \      \"FW\": \"336.206\",\n        \"Synonyms\": \"\",\n        \"Notes\": \"\
    \",\n        \"Hans80Anti\": \"\",\n        \"Hans80metals\": \"\",\n        \"\
    FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\"\
    : \"\",\n        \"All_star\": \"\"\n      }\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 178\",\n        \"exact_source_quote\"\
    : \"EDTA (disodium salt)\\t6381-92-6\\tSigma\\tE6635\\t336.206\\t\\t\\t\\t\\t\\\
    t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source EDTA disodium name\
    \ does not specify hydration. CAS 6381-92-6 conflicts with the anhydrous term\
    \ CAS 139-33-3, while source FW 336.206 is consistent with the anhydrous term\
    \ mass 336.208. Supplier-specific hydration remains unresolved; do not silently\
    \ choose a hydrate or recalculate the amount. Historical mapping confidence 0.90,\
    \ where present, is a local algorithm assertion, not externally verified probability.\"\
    \n  },\n  {\n    \"decision_id\": \"q43\",\n    \"name\": \"Boric Acid\",\n  \
    \  \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence\
    \ text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\",\n\
    \        \"field_path\": \"ingredients[7].notes\",\n        \"stored\": \"CAS:\
    \ 10043-35-3; MW: 61.83; From Trace metal mix A5\"\n      }\n    ],\n    \"desired\"\
    : {\n      \"source_compound_fields\": {\n        \"Compound\": \"Boric Acid\"\
    ,\n        \"CAS\": \"10043-35-3\",\n        \"Company\": \"\",\n        \"CatalogNumber\"\
    : \"0084-01 (JT*)\",\n        \"FW\": \"61.83\",\n        \"Synonyms\": \"H3BO3\"\
    ,\n        \"Notes\": \"\",\n        \"Hans80Anti\": \"\",\n        \"Hans80metals\"\
    : \"no\",\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"\",\n\
    \        \"FEBA_stress\": \"\",\n        \"All_star\": \"\"\n      }\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 84\",\n        \"exact_source_quote\"\
    : \"Boric Acid\\t10043-35-3\\t\\t0084-01 (JT*)\\t61.83\\tH3BO3\\t\\t\\tno\\t\\\
    t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q44\",\n    \"name\": \"Manganese (II) chloride tetrahydrate\"\
    ,\n    \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and\
    \ mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].notes\",\n        \"stored\": \"CAS:\
    \ 13446-34-9; MW: 197.91; From Trace metal mix A5; Ontology enriched via CAS-RN\
    \ lookup\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Manganese (II) chloride tetrahydrate\",\n       \
    \ \"CAS\": \"13446-34-9\",\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\"\
    : \"M3634\",\n        \"FW\": \"197.91\",\n        \"Synonyms\": \"MnCl2, manganese\
    \ chloride, MnCl2 4H2O\",\n        \"Notes\": \"\",\n        \"Hans80Anti\": \"\
    \",\n        \"Hans80metals\": \"yes\",\n        \"FEBA_carbon\": \"\",\n    \
    \    \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\"\
    : \"\"\n      }\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 278\",\n        \"exact_source_quote\"\
    : \"Manganese (II) chloride tetrahydrate\\t13446-34-9\\tSigma\\tM3634\\t197.91\\\
    tMnCl2, manganese chloride, MnCl2 4H2O\\t\\t\\tyes\\t\\t\\t\\t\\n\",\n       \
    \ \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q45\",\n    \"name\": \"Zinc sulfate heptahydrate\"\
    ,\n    \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and\
    \ mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].notes\",\n        \"stored\": \"CAS:\
    \ 7446-20-0; MW: 287.56; From Trace metal mix A5; Ontology enriched via CAS-RN\
    \ lookup\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Zinc sulfate heptahydrate\",\n        \"CAS\": \"\
    7446-20-0\",\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\": \"Z0251\"\
    ,\n        \"FW\": \"287.56\",\n        \"Synonyms\": \"zinc sulfate, ZnSO4 7H2O\"\
    ,\n        \"Notes\": \"\",\n        \"Hans80Anti\": \"\",\n        \"Hans80metals\"\
    : \"\",\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"\",\n  \
    \      \"FEBA_stress\": \"yes\",\n        \"All_star\": \"\"\n      }\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 474\",\n        \"exact_source_quote\"\
    : \"Zinc sulfate heptahydrate\\t7446-20-0\\tSigma\\tZ0251\\t287.56\\tzinc sulfate,\
    \ ZnSO4 7H2O\\t\\t\\t\\t\\t\\tyes\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q46\",\n    \"name\": \"Sodium Molybdate Dihydrate\"\
    ,\n    \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and\
    \ mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].notes\",\n        \"stored\": \"\
    CAS: 10102-40-6; MW: 241.95; From Trace metal mix A5; Ontology enriched via CAS-RN\
    \ lookup\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Sodium Molybdate Dihydrate\",\n        \"CAS\": \"\
    10102-40-6\",\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\": \"\
    331058\",\n        \"FW\": \"241.95\",\n        \"Synonyms\": \"Na2MoO4 2H2O,\
    \ Na2MoO4-2H2O\",\n        \"Notes\": \"\",\n        \"Hans80Anti\": \"\",\n \
    \       \"Hans80metals\": \"\",\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\"\
    : \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\": \"\"\n      }\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 399\",\n        \"exact_source_quote\"\
    : \"Sodium Molybdate Dihydrate\\t10102-40-6\\tSigma\\t331058\\t241.95\\tNa2MoO4\
    \ 2H2O, Na2MoO4-2H2O\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\":\
    \ \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q47\",\n    \"name\": \"Copper (II) sulfate pentahydrate\"\
    ,\n    \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and\
    \ mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].notes\",\n        \"stored\": \"\
    CAS: 7758-99-8; MW: 249.69; From Trace metal mix A5; Ontology enriched via CAS-RN\
    \ lookup\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Copper (II) sulfate pentahydrate\",\n        \"CAS\"\
    : \"7758-99-8\",\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\":\
    \ \"C8027\",\n        \"FW\": \"249.69\",\n        \"Synonyms\": \"Blue Vitriol,\
    \ Cupric sulfate pentahydrate, Sulfuric acid, copper(II) salt (1:1) pentahydrate,\
    \ CuSO4 5H2O, Cupric Sulfate\",\n        \"Notes\": \"\",\n        \"Hans80Anti\"\
    : \"\",\n        \"Hans80metals\": \"\",\n        \"FEBA_carbon\": \"\",\n   \
    \     \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\"\
    : \"\"\n      }\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 129\",\n        \"exact_source_quote\"\
    : \"Copper (II) sulfate pentahydrate\\t7758-99-8\\tSigma\\tC8027\\t249.69\\tBlue\
    \ Vitriol, Cupric sulfate pentahydrate, Sulfuric acid, copper(II) salt (1:1) pentahydrate,\
    \ CuSO4 5H2O, Cupric Sulfate\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q48\",\n    \"name\": \"Cobalt(II) nitrate hexahydrate\"\
    ,\n    \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and\
    \ mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].notes\",\n        \"stored\": \"\
    CAS: 10026-22-9; MW: 291.03; From Trace metal mix A5; Ontology enriched via CAS-RN\
    \ lookup\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Cobalt(II) nitrate hexahydrate\",\n        \"CAS\"\
    : \"10026-22-9\",\n        \"Company\": \"\",\n        \"CatalogNumber\": \"\"\
    ,\n        \"FW\": \"291.03\",\n        \"Synonyms\": \"Co(NO3)2 6H2O\",\n   \
    \     \"Notes\": \"\",\n        \"Hans80Anti\": \"\",\n        \"Hans80metals\"\
    : \"\",\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"\",\n  \
    \      \"FEBA_stress\": \"\",\n        \"All_star\": \"\"\n      }\n    },\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 124\",\n        \"exact_source_quote\"\
    : \"Cobalt(II) nitrate hexahydrate\\t10026-22-9\\t\\t\\t291.03\\tCo(NO3)2 6H2O\\\
    t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q49\",\n    \"name\": \"TES\",\n    \"stage\": \"\
    Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BG11_TES_no_bicarb.yaml\",\n      \
    \  \"field_path\": \"ingredients[13].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 7365-44-8; MW: 229.25\"\n  \
    \    }\n    ],\n    \"desired\": {\n      \"source_compound_fields\": {\n    \
    \    \"Compound\": \"TES\",\n        \"CAS\": \"7365-44-8\",\n        \"Company\"\
    : \"\",\n        \"CatalogNumber\": \"\",\n        \"FW\": \"229.25\",\n     \
    \   \"Synonyms\": \"2-[(2-Hydroxy-1,1-bis(hydroxymethyl)ethyl)amino]ethanesulfonic\
    \ acid, N-[Tris(hydroxymethyl)methyl]-2-aminoethanesulfonic acid\",\n        \"\
    Notes\": \"\",\n        \"Hans80Anti\": \"\",\n        \"Hans80metals\": \"\"\
    ,\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"\",\n        \"\
    FEBA_stress\": \"\",\n        \"All_star\": \"\"\n      }\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 1372\",\n        \"exact_source_quote\"\
    : \"TES\\t7365-44-8\\t\\t\\t229.25\\t2-[(2-Hydroxy-1,1-bis(hydroxymethyl)ethyl)amino]ethanesulfonic\
    \ acid, N-[Tris(hydroxymethyl)methyl]-2-aminoethanesulfonic acid\\t\\t\\t\\t\\\
    t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q50\",\n    \"name\": \"Sodium nitrate\",\n    \"\
    stage\": \"Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence\
    \ text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 7631-99-4; MW: 84.99\"\n   \
    \   }\n    ],\n    \"desired\": {\n      \"source_compound_fields\": {\n     \
    \   \"Compound\": \"Sodium nitrate\",\n        \"CAS\": \"7631-99-4\",\n     \
    \   \"Company\": \"Sigma\",\n        \"CatalogNumber\": \"S8170\",\n        \"\
    FW\": \"84.99\",\n        \"Synonyms\": \"NaNO3\",\n        \"Notes\": \"\",\n\
    \        \"Hans80Anti\": \"\",\n        \"Hans80metals\": \"yes\",\n        \"\
    FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"yes\",\n        \"FEBA_stress\"\
    : \"yes\",\n        \"All_star\": \"\"\n      }\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 400\",\n        \"exact_source_quote\"\
    : \"Sodium nitrate\\t7631-99-4\\tSigma\\tS8170\\t84.99\\tNaNO3\\t\\t\\tyes\\t\\\
    tyes\\tyes\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q51\",\n    \"name\": \"Potassium phosphate dibasic\"\
    ,\n    \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and\
    \ mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"CAS:\
    \ 7758-11-4; MW: 174.18\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Potassium phosphate dibasic\",\n        \"CAS\":\
    \ \"7758-11-4\",\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\":\
    \ \"P3786\",\n        \"FW\": \"174.18\",\n        \"Synonyms\": \"K2HPO4, dibasic\
    \ anhydrous sodium phosphate\",\n        \"Notes\": \"\",\n        \"Hans80Anti\"\
    : \"\",\n        \"Hans80metals\": \"\",\n        \"FEBA_carbon\": \"\",\n   \
    \     \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\"\
    : \"\"\n      }\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 337\",\n        \"exact_source_quote\"\
    : \"Potassium phosphate dibasic\\t7758-11-4\\tSigma\\tP3786\\t174.18\\tK2HPO4,\
    \ dibasic anhydrous sodium phosphate\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source preferred name, K2HPO4,\
    \ CAS 7758-11-4 and FW 174.18 support dipotassium hydrogen phosphate. Source synonym\
    \ dibasic anhydrous sodium phosphate is internally inconsistent. OLS has a trihydrate\
    \ synonym but its formula/mass encode the unhydrated salt; neither stray synonym\
    \ establishes an actual source hydrate or sodium salt. Historical mapping confidence\
    \ 0.90, where present, is a local algorithm assertion, not externally verified\
    \ probability.\"\n  },\n  {\n    \"decision_id\": \"q52\",\n    \"name\": \"Magnesium\
    \ Sulfate Heptahydrate\",\n    \"stage\": \"Stored ingredient identity metadata;\
    \ numerical CAS/MW and mapping-confidence text\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"CAS:\
    \ 10034-99-8; MW: 246.47\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Magnesium Sulfate Heptahydrate\",\n        \"CAS\"\
    : \"10034-99-8\",\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\"\
    : \"M1880\",\n        \"FW\": \"246.47\",\n        \"Synonyms\": \"Epsom salts,\
    \ MgSO4 7H2O\",\n        \"Notes\": \"\",\n        \"Hans80Anti\": \"\",\n   \
    \     \"Hans80metals\": \"\",\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\"\
    : \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\": \"\"\n      }\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 277\",\n        \"exact_source_quote\"\
    : \"Magnesium Sulfate Heptahydrate\\t10034-99-8\\tSigma\\tM1880\\t246.47\\tEpsom\
    \ salts, MgSO4 7H2O\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"\
    25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n        \"\
    quote_representation\": \"UTF-8 source decoded with universal newlines; tabs and\
    \ all other characters retained. Raw external evidence preserves original CRLF.\"\
    \n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate or buffer\
    \ agrees with the asserted chemical identity. Explicit hydration is retained;\
    \ source compound identifiers and formula metadata do not supply new preparation\
    \ conditions. Historical mapping confidence 0.90, where present, is a local algorithm\
    \ assertion, not externally verified probability.\"\n  },\n  {\n    \"decision_id\"\
    : \"q53\",\n    \"name\": \"Calcium chloride dihydrate\",\n    \"stage\": \"Stored\
    \ ingredient identity metadata; numerical CAS/MW and mapping-confidence text\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\",\n  \
    \      \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 10035-04-8; MW: 147.01\"\n \
    \     }\n    ],\n    \"desired\": {\n      \"source_compound_fields\": {\n   \
    \     \"Compound\": \"Calcium chloride dihydrate\",\n        \"CAS\": \"10035-04-8\"\
    ,\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\": \"C5080\",\n  \
    \      \"FW\": \"147.01\",\n        \"Synonyms\": \"Calcium Chloride Dihydrate,\
    \ CaCl2*2H2O\",\n        \"Notes\": \"\",\n        \"Hans80Anti\": \"\",\n   \
    \     \"Hans80metals\": \"yes\",\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\"\
    : \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\": \"\"\n      }\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 90\",\n        \"exact_source_quote\"\
    : \"Calcium chloride dihydrate\\t10035-04-8\\tSigma\\tC5080\\t147.01\\tCalcium\
    \ Chloride Dihydrate, CaCl2*2H2O\\t\\t\\tyes\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q54\",\n    \"name\": \"Citric Acid\",\n    \"stage\"\
    : \"Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence\
    \ text\",\n    \"decision\": \"conflict\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\",\n\
    \        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 77-92-9; MW: 192.12\"\n    \
    \  }\n    ],\n    \"desired\": {\n      \"source_compound_fields\": {\n      \
    \  \"Compound\": \"Citric Acid\",\n        \"CAS\": \"77-92-9\",\n        \"Company\"\
    : \"Sigma\",\n        \"CatalogNumber\": \"251275\",\n        \"FW\": \"192.12\"\
    ,\n        \"Synonyms\": \"\",\n        \"Notes\": \"\",\n        \"Hans80Anti\"\
    : \"\",\n        \"Hans80metals\": \"no\",\n        \"FEBA_carbon\": \"yes\",\n\
    \        \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\": \"\",\n        \"\
    All_star\": \"\"\n      }\n    },\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 119\",\n        \"exact_source_quote\"\
    : \"Citric Acid\\t77-92-9\\tSigma\\t251275\\t192.12\\t\\t\\t\\tno\\tyes\\t\\t\\\
    t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source citric acid and CAS\
    \ 77-92-9 differ from CHEBI:53258, the trisodium citrate salt. CHEBI:30769 is\
    \ the supported acid candidate; retain the source amount. Historical mapping confidence\
    \ 0.90, where present, is a local algorithm assertion, not externally verified\
    \ probability.\"\n  },\n  {\n    \"decision_id\": \"q55\",\n    \"name\": \"Ferric\
    \ ammonium citrate\",\n    \"stage\": \"Stored ingredient identity metadata; numerical\
    \ CAS/MW and mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 1185-57-5\"\n      }\n    ],\n\
    \    \"desired\": {\n      \"source_compound_fields\": {\n        \"Compound\"\
    : \"Ferric ammonium citrate\",\n        \"CAS\": \"1185-57-5\",\n        \"Company\"\
    : \"Sigma\",\n        \"CatalogNumber\": \"F5879\",\n        \"FW\": \"\",\n \
    \       \"Synonyms\": \"\",\n        \"Notes\": \"\",\n        \"Hans80Anti\"\
    : \"\",\n        \"Hans80metals\": \"\",\n        \"FEBA_carbon\": \"\",\n   \
    \     \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\"\
    : \"\"\n      }\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 186\",\n        \"exact_source_quote\"\
    : \"Ferric ammonium citrate\\t1185-57-5\\tSigma\\tF5879\\t\\t\\t\\t\\t\\t\\t\\\
    t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source ferric ammonium citrate\
    \ matches the asserted mixture identity. OLS describes indefinite composition;\
    \ no fixed molar mass or molecular concentration is inferred. Historical mapping\
    \ confidence 0.90, where present, is a local algorithm assertion, not externally\
    \ verified probability.\"\n  },\n  {\n    \"decision_id\": \"q56\",\n    \"name\"\
    : \"EDTA (disodium salt)\",\n    \"stage\": \"Stored ingredient identity metadata;\
    \ numerical CAS/MW and mapping-confidence text\",\n    \"decision\": \"conflict\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"CAS:\
    \ 6381-92-6; MW: 336.206\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"EDTA (disodium salt)\",\n        \"CAS\": \"6381-92-6\"\
    ,\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\": \"E6635\",\n  \
    \      \"FW\": \"336.206\",\n        \"Synonyms\": \"\",\n        \"Notes\": \"\
    \",\n        \"Hans80Anti\": \"\",\n        \"Hans80metals\": \"\",\n        \"\
    FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\"\
    : \"\",\n        \"All_star\": \"\"\n      }\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 178\",\n        \"exact_source_quote\"\
    : \"EDTA (disodium salt)\\t6381-92-6\\tSigma\\tE6635\\t336.206\\t\\t\\t\\t\\t\\\
    t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source EDTA disodium name\
    \ does not specify hydration. CAS 6381-92-6 conflicts with the anhydrous term\
    \ CAS 139-33-3, while source FW 336.206 is consistent with the anhydrous term\
    \ mass 336.208. Supplier-specific hydration remains unresolved; do not silently\
    \ choose a hydrate or recalculate the amount. Historical mapping confidence 0.90,\
    \ where present, is a local algorithm assertion, not externally verified probability.\"\
    \n  },\n  {\n    \"decision_id\": \"q57\",\n    \"name\": \"Boric Acid\",\n  \
    \  \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence\
    \ text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].notes\",\n        \"stored\": \"CAS:\
    \ 10043-35-3; MW: 61.83; From Trace metal mix A5\"\n      }\n    ],\n    \"desired\"\
    : {\n      \"source_compound_fields\": {\n        \"Compound\": \"Boric Acid\"\
    ,\n        \"CAS\": \"10043-35-3\",\n        \"Company\": \"\",\n        \"CatalogNumber\"\
    : \"0084-01 (JT*)\",\n        \"FW\": \"61.83\",\n        \"Synonyms\": \"H3BO3\"\
    ,\n        \"Notes\": \"\",\n        \"Hans80Anti\": \"\",\n        \"Hans80metals\"\
    : \"no\",\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"\",\n\
    \        \"FEBA_stress\": \"\",\n        \"All_star\": \"\"\n      }\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 84\",\n        \"exact_source_quote\"\
    : \"Boric Acid\\t10043-35-3\\t\\t0084-01 (JT*)\\t61.83\\tH3BO3\\t\\t\\tno\\t\\\
    t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q58\",\n    \"name\": \"Manganese (II) chloride tetrahydrate\"\
    ,\n    \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and\
    \ mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].notes\",\n        \"stored\": \"CAS:\
    \ 13446-34-9; MW: 197.91; From Trace metal mix A5; Ontology enriched via CAS-RN\
    \ lookup\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Manganese (II) chloride tetrahydrate\",\n       \
    \ \"CAS\": \"13446-34-9\",\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\"\
    : \"M3634\",\n        \"FW\": \"197.91\",\n        \"Synonyms\": \"MnCl2, manganese\
    \ chloride, MnCl2 4H2O\",\n        \"Notes\": \"\",\n        \"Hans80Anti\": \"\
    \",\n        \"Hans80metals\": \"yes\",\n        \"FEBA_carbon\": \"\",\n    \
    \    \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\"\
    : \"\"\n      }\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 278\",\n        \"exact_source_quote\"\
    : \"Manganese (II) chloride tetrahydrate\\t13446-34-9\\tSigma\\tM3634\\t197.91\\\
    tMnCl2, manganese chloride, MnCl2 4H2O\\t\\t\\tyes\\t\\t\\t\\t\\n\",\n       \
    \ \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q59\",\n    \"name\": \"Zinc sulfate heptahydrate\"\
    ,\n    \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and\
    \ mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].notes\",\n        \"stored\": \"CAS:\
    \ 7446-20-0; MW: 287.56; From Trace metal mix A5; Ontology enriched via CAS-RN\
    \ lookup\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Zinc sulfate heptahydrate\",\n        \"CAS\": \"\
    7446-20-0\",\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\": \"Z0251\"\
    ,\n        \"FW\": \"287.56\",\n        \"Synonyms\": \"zinc sulfate, ZnSO4 7H2O\"\
    ,\n        \"Notes\": \"\",\n        \"Hans80Anti\": \"\",\n        \"Hans80metals\"\
    : \"\",\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"\",\n  \
    \      \"FEBA_stress\": \"yes\",\n        \"All_star\": \"\"\n      }\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 474\",\n        \"exact_source_quote\"\
    : \"Zinc sulfate heptahydrate\\t7446-20-0\\tSigma\\tZ0251\\t287.56\\tzinc sulfate,\
    \ ZnSO4 7H2O\\t\\t\\t\\t\\t\\tyes\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q60\",\n    \"name\": \"Sodium Molybdate Dihydrate\"\
    ,\n    \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and\
    \ mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].notes\",\n        \"stored\": \"\
    CAS: 10102-40-6; MW: 241.95; From Trace metal mix A5; Ontology enriched via CAS-RN\
    \ lookup\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Sodium Molybdate Dihydrate\",\n        \"CAS\": \"\
    10102-40-6\",\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\": \"\
    331058\",\n        \"FW\": \"241.95\",\n        \"Synonyms\": \"Na2MoO4 2H2O,\
    \ Na2MoO4-2H2O\",\n        \"Notes\": \"\",\n        \"Hans80Anti\": \"\",\n \
    \       \"Hans80metals\": \"\",\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\"\
    : \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\": \"\"\n      }\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 399\",\n        \"exact_source_quote\"\
    : \"Sodium Molybdate Dihydrate\\t10102-40-6\\tSigma\\t331058\\t241.95\\tNa2MoO4\
    \ 2H2O, Na2MoO4-2H2O\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\":\
    \ \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q61\",\n    \"name\": \"Copper (II) sulfate pentahydrate\"\
    ,\n    \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and\
    \ mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].notes\",\n        \"stored\": \"\
    CAS: 7758-99-8; MW: 249.69; From Trace metal mix A5; Ontology enriched via CAS-RN\
    \ lookup\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Copper (II) sulfate pentahydrate\",\n        \"CAS\"\
    : \"7758-99-8\",\n        \"Company\": \"Sigma\",\n        \"CatalogNumber\":\
    \ \"C8027\",\n        \"FW\": \"249.69\",\n        \"Synonyms\": \"Blue Vitriol,\
    \ Cupric sulfate pentahydrate, Sulfuric acid, copper(II) salt (1:1) pentahydrate,\
    \ CuSO4 5H2O, Cupric Sulfate\",\n        \"Notes\": \"\",\n        \"Hans80Anti\"\
    : \"\",\n        \"Hans80metals\": \"\",\n        \"FEBA_carbon\": \"\",\n   \
    \     \"FEBA_nitrogen\": \"\",\n        \"FEBA_stress\": \"\",\n        \"All_star\"\
    : \"\"\n      }\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 129\",\n        \"exact_source_quote\"\
    : \"Copper (II) sulfate pentahydrate\\t7758-99-8\\tSigma\\tC8027\\t249.69\\tBlue\
    \ Vitriol, Cupric sulfate pentahydrate, Sulfuric acid, copper(II) salt (1:1) pentahydrate,\
    \ CuSO4 5H2O, Cupric Sulfate\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q62\",\n    \"name\": \"Cobalt(II) nitrate hexahydrate\"\
    ,\n    \"stage\": \"Stored ingredient identity metadata; numerical CAS/MW and\
    \ mapping-confidence text\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].notes\",\n        \"stored\": \"\
    CAS: 10026-22-9; MW: 291.03; From Trace metal mix A5; Ontology enriched via CAS-RN\
    \ lookup\"\n      }\n    ],\n    \"desired\": {\n      \"source_compound_fields\"\
    : {\n        \"Compound\": \"Cobalt(II) nitrate hexahydrate\",\n        \"CAS\"\
    : \"10026-22-9\",\n        \"Company\": \"\",\n        \"CatalogNumber\": \"\"\
    ,\n        \"FW\": \"291.03\",\n        \"Synonyms\": \"Co(NO3)2 6H2O\",\n   \
    \     \"Notes\": \"\",\n        \"Hans80Anti\": \"\",\n        \"Hans80metals\"\
    : \"\",\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"\",\n  \
    \      \"FEBA_stress\": \"\",\n        \"All_star\": \"\"\n      }\n    },\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 124\",\n        \"exact_source_quote\"\
    : \"Cobalt(II) nitrate hexahydrate\\t10026-22-9\\t\\t\\t291.03\\tCo(NO3)2 6H2O\\\
    t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q63\",\n    \"name\": \"TES\",\n    \"stage\": \"\
    Stored ingredient identity metadata; numerical CAS/MW and mapping-confidence text\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml\",\n  \
    \      \"field_path\": \"ingredients[13].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 7365-44-8; MW: 229.25\"\n  \
    \    }\n    ],\n    \"desired\": {\n      \"source_compound_fields\": {\n    \
    \    \"Compound\": \"TES\",\n        \"CAS\": \"7365-44-8\",\n        \"Company\"\
    : \"\",\n        \"CatalogNumber\": \"\",\n        \"FW\": \"229.25\",\n     \
    \   \"Synonyms\": \"2-[(2-Hydroxy-1,1-bis(hydroxymethyl)ethyl)amino]ethanesulfonic\
    \ acid, N-[Tris(hydroxymethyl)methyl]-2-aminoethanesulfonic acid\",\n        \"\
    Notes\": \"\",\n        \"Hans80Anti\": \"\",\n        \"Hans80metals\": \"\"\
    ,\n        \"FEBA_carbon\": \"\",\n        \"FEBA_nitrogen\": \"\",\n        \"\
    FEBA_stress\": \"\",\n        \"All_star\": \"\"\n      }\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compound row 1372\",\n        \"exact_source_quote\"\
    : \"TES\\t7365-44-8\\t\\t\\t229.25\\t2-[(2-Hydroxy-1,1-bis(hydroxymethyl)ethyl)amino]ethanesulfonic\
    \ acid, N-[Tris(hydroxymethyl)methyl]-2-aminoethanesulfonic acid\\t\\t\\t\\t\\\
    t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"Source named salt, hydrate\
    \ or buffer agrees with the asserted chemical identity. Explicit hydration is\
    \ retained; source compound identifiers and formula metadata do not supply new\
    \ preparation conditions. Historical mapping confidence 0.90, where present, is\
    \ a local algorithm assertion, not externally verified probability.\"\n  },\n\
    \  {\n    \"decision_id\": \"q64\",\n    \"name\": \"Unspecified preparation and\
    \ cultivation conditions\",\n    \"stage\": \"Exact named FEBA recipe only\",\n\
    \    \"decision\": \"not_quantified\",\n    \"local_fields\": [],\n    \"desired\"\
    : {\n      \"water_or_final_batch_volume\": null,\n      \"ph_value\": null,\n\
    \      \"temperature_value\": null,\n      \"sterilization_cycle\": null,\n  \
    \    \"light_intensity\": null,\n      \"light_cycle\": null\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"Complete named recipe and description\",\n  \
    \      \"exact_source_quote\": \"Media\\tBG11_TES_no_bicarb\\t\\nDescription\\\
    tFor growing cyanobacteria, from Luis; no sodium bicarbonate; with TES buffer\\\
    t\\nMinimal\\tTRUE\\t\\nControlled vocabulary\\tConcentration\\tUnits\\nSodium\
    \ nitrate\\t17.6\\tmM\\nPotassium phosphate dibasic\\t0.2\\tmM\\nMagnesium Sulfate\
    \ Heptahydrate\\t0.3\\tmM\\nCalcium chloride dihydrate\\t0.24\\tmM\\nCitric Acid\\\
    t28.5\\tuM\\nFerric ammonium citrate\\t0.006\\tg/L\\nEDTA (disodium salt)\\t2.4\\\
    tuM\\nTrace metal mix A5\\t1\\tX\\nTES\\t20\\tmM\\n\\t\\t\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"UTF-8 source decoded with universal newlines;\
    \ tabs and all other characters retained. Raw external evidence preserves original\
    \ CRLF.\"\n      }\n    ],\n    \"interpretation\": \"The inspected block supplies\
    \ concentrations and intended cyanobacterial use, not measured final volume, water\
    \ make-up, pH, light, temperature or sterilization. Preparation is absent in both\
    \ target and owner, so no documented preparation loss is inferred. Do not borrow\
    \ neighboring BG11 conditions.\"\n  }\n]"
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 8 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact named variant and contribution membership
  outcome: supported
  summary: BG11_TES_no_bicarb is resolved to its exact maintained owner and native
    inspected merge contribution. All 14 ingredient amounts match the named FEBA block
    plus the correctly diluted A5 stock. Neighboring BG11, BG11R, nitrogen-free, carbonate-free
    and TES variants remain distinct.
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - record
  - feba-main
  - feba-a5
  - owner-0
- assessment_id: chemical-forms
  area: grounding
  topic: Source identity versus canonical ontology metadata
  outcome: concern
  summary: Citric acid is incorrectly mapped to sodium citrate. EDTA hydration is
    unresolved by conflicting source CAS and formula-weight metadata. All other named
    forms, including the explicit trace hydrates, agree at the supported source level;
    misleading potassium-phosphate synonyms do not override its name, CAS and formula.
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - forms
  - citric-acid-candidate
  - chebi53258
  - chebi64734
  - chebi131527
  - compound-0
  - compound-1
  - compound-2
  - compound-3
  - compound-4
  - compound-5
  - compound-6
  - compound-7
  - compound-8
  - compound-9
  - compound-10
  - compound-11
  - compound-12
  - compound-13
- assessment_id: provenance-scope
  area: provenance
  topic: Source versions and current repair scope
  outcome: concern
  summary: The September FEBA revision supports the exact current numerical recipe
    but does not authenticate the March CultureBotHT import. Current owner has later
    repair metadata and two broad references; target lacks these later fields. An
    ingredients_curated flag is not proof that chemical forms or evidence have been
    checked. No universal historical-merger causal claim is made.
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - record
  - feba-version
  - writer-0
  - owner-0
- assessment_id: preparation
  area: completeness
  topic: Protocol, culture conditions and source-only information
  outcome: unknown
  summary: The FEBA block has no water make-up, sterilization procedure, temperature,
    light or final pH. These required protocol details remain unknown, rather than
    being imported from another BG11 recipe. There is no local solution reference
    to validate and no existing nested stock; the A5 source ratio is retained in the
    inventory.
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - feba-main
  - feba-a5
  - quantity-inventory
- assessment_id: growth
  area: evidence
  topic: Growth claims and comparison-only BG11 literature
  outcome: not_applicable
  summary: Neither target nor maintained owner asserts a target organism, strain metric,
    genome accession or experimental variant. Intended cyanobacterial use is not a
    strain-specific growth demonstration. Captured sibling BG11 literature, taxonomy
    and marker evidence is comparison context only and is not transferred to this
    selected variant.
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - record
  - feba-main
  - owner-0
- assessment_id: classification
  area: scope
  topic: Existing physical and organizational classifications
  outcome: unknown
  summary: The named formulation supports a liquid mineral-medium representation and
    cyanobacterial intended use. FEBA Minimal TRUE is not a complete chemical-definition
    proof, particularly for ferric ammonium citrate of indefinite composition. Preserve
    category context without inferring cultivation oxygen, strain taxonomy or a replacement
    classification solely from the name.
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - feba-main
  - chebi31604
  - record
- assessment_id: links
  area: evidence
  topic: Identifier and reference roles
  outcome: concern
  summary: The owner references a CultureBotHT internal identifier and repository
    URL, not claim-level concentration evidence. No DOI, PMID, KG match, genome accession,
    nested solution reference, legacy MIM identifier or current secondary MIM slot
    is asserted in these selected layers. Optional missing secondary links are not
    invalid links.
  target_ids:
  - CultureMech:015453
  evidence_ids:
  - record
  - mim
  - owner-0
findings:
- finding_id: f1
  issue_key: culturemech.015453.citric-acid-salt
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Citric acid is represented by a sodium-citrate identifier
  description: Both target and maintained owner name Citric Acid and retain acid CAS
    77-92-9/FW 192.12, but their primary term is CHEBI:53258 sodium citrate. This
    is a chemical-form mismatch despite canonical label validity.
  target_ids:
  - CultureMech:015453
  field_paths:
  - ingredients[4].term
  - ingredients[4].notes
  evidence_ids:
  - feba-main
  - forms
  - chebi53258
  - citric-acid-candidate
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: culturemech.015453.edta-hydration
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: EDTA hydration is asserted more specifically than the reconciled source metadata
  description: CHEBI:64734 explicitly asserts anhydrous disodium EDTA. The source
    name is unqualified; its CAS differs from the anhydrous OLS CAS while its formula
    weight agrees closely with the anhydrous form. The unresolved source metadata
    conflict must not be presented as verified hydration.
  target_ids:
  - CultureMech:015453
  field_paths:
  - ingredients[6].term
  - ingredients[6].notes
  evidence_ids:
  - forms
  - chebi64734
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.015453.amount-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct numerical amounts lack attached source and stock-dilution evidence
  description: Every selected ingredient concentration is numerically supported by
    the exact FEBA variant or the explicit A5 1000 X to 1 X dilution, but neither
    target nor maintained owner carries claim-level concentration evidence. Broad
    source links and the curated flag omit the verified version, exact rows and arithmetic.
  target_ids:
  - CultureMech:015453
  field_paths:
  - ingredients
  - references
  - data_quality_flags
  evidence_ids:
  - feba-main
  - feba-a5
  - quantity-inventory
  - writer-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: 'P4.3 is normalized to minor as a concrete traceability exception:
    the exact named formulation and dilution support all numerical rates, so no wrong
    amount is alleged, but every selected concentration lacks attached claim-level
    evidence needed to reproduce those source and stock-stage decisions.'
- finding_id: f4
  issue_key: culturemech.015453.stale-owner-metadata
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated projection omits later owner source metadata
  description: The generated record predates the maintained owner repair and lacks
    its media_term and references. Reconciliation must retain append-only chronology
    and qualify curated status against the actual evidence, rather than assuming the
    current generator caused every historical difference.
  target_ids:
  - CultureMech:015453
  field_paths:
  - media_term
  - references
  - curation_history
  - data_quality_flags
  evidence_ids:
  - record
  - writer-0
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.4
  native_severity: P4
  normalization_reason: P4.4 is normalized to minor because the generated projection
    omits actual later owner media identity, references and append-only repair context.
    This is a bounded metadata-reconciliation defect; it does not establish a wrong
    numerical formulation or prove historical generator causation.
actions:
- action_id: a1
  description: Correct the maintained owner to the supported acid identity with source
    evidence, preserve its concentration and provenance, then regenerate only under
    separately authorized workflow.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015453
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
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
  description: Resolve the exact supplier/source form or record the hydration uncertainty
    explicitly without guessing a replacement ID, quantity or molar conversion.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015453
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
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
  description: Attach exact versioned source evidence and explicit A5 stock-to-medium
    arithmetic in the owner, preserving direct units and uncertainty. Do not replace
    these correct rates with undiluted stock values.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:015453
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
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
  description: After owner scientific corrections, reconcile generated metadata using
    the authorized generator and preserve the existing historical events.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:015453
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
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
- The exact public CultureBotHT endpoint returned HTTP 404 at its retained actual
  access time. The March import bytes and their historical equivalence to the later
  FEBA recipe remain unverified. Current named FEBA amounts are independently assessable;
  the missing historical source is a partial-completion limit.
- Coverage is partial because historical CultureBotHT source identity and complete
  preparation conditions remain unresolved. All current target/owner concentrations
  and supplied-form assertions were nevertheless assessed. Comparison-only source
  failures do not become extra required checks for this variant.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-041
- generated-medium
```
