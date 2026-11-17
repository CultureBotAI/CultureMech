# Source and formulation review: acidianus_manzaensis_medium_for_heterotrophic_growth (CultureMech:008184)

- Review: 20261021T185233Z-culturemech-008184-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T18:47:07Z
- Finished UTC: 2026-10-21T18:52:33Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact NBRC 831 and TOGO M1629 identities resolve. Seven milligram amounts and the water volume are represented with wrong units; source preparation and hydrate grounding also need curation. Printed source formula ambiguities remain explicit.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 338; batch 034 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-three task batches contain 330 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 333 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008184 | data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml | generated | acidianus_manzaensis_medium_for_heterotrophic_growth |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008184 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008184 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-034/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch034/338/strict.tsv |
| validate-terms | passed | True | CultureMech:008184 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008184 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008184 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: togoM1629 | unavailable | False | CultureMech:008184 | The alternate TOGO mediumapi request failed DNS; its real failed attempt is retained. The exact original TOGO endpoint and NBRC 831 primary are usable, so this optional access failure does not leave the current formulation review incomplete. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008184.

The four documented recipes completed; interpret the scope of each separately.

### Exact source accession and recipe boundary

identity: supported. Targets: CultureMech:008184.

NBRC 831 and TOGO M1629 name this heterotrophic medium. It contains yeast extract and is distinct from autotrophic NBRC 830; the other recipe’s ferric sulfate and gas requirements are not transferred. No supplier product, DOI, strain accession, KG match or structured growth assertion is present to authenticate.

### Single maintained source and generated correspondence

ownership: supported. Targets: CultureMech:008184.

The complete merge event, merged_from and exact stable ID resolve one maintained archaea owner. All scientific fields agree between target and owner. Current defects are present in both; corrections belong in the maintained source before separately authorized regeneration. A fingerprint is provenance, not external formulation evidence.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:008184.

17 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; Distilled water",
        "exact_source_quote": "Distilled water 1 L",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "Both layers store 1 G_PER_L. Restore the source quantity 1 L of preparation water; this is neither 1 g/L water nor a measured final volume."
  },
  {
    "decision_id": "q2",
    "ingredient": "MgSO4·7H2O",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.49",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.49",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; MgSO4·7H2O",
        "exact_source_quote": "MgSO 4 ·7H 2 O 0.49 g",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4·7H2O\",\n          \"volume\": 0.49,\n          \"unit\": \"g\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "The printed gram amount agrees numerically, but both layers label it G_PER_L. Preserve the source batch grams alongside the separately specified 1 L water and qualify the denominator rather than claim a measured final concentration. Neither layer has attached amount evidence."
  },
  {
    "decision_id": "q3",
    "ingredient": "Yeast extract",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; Yeast extract",
        "exact_source_quote": "Yeast extract 1 g",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "The printed gram amount agrees numerically, but both layers label it G_PER_L. Preserve the source batch grams alongside the separately specified 1 L water and qualify the denominator rather than claim a measured final concentration. Neither layer has attached amount evidence."
  },
  {
    "decision_id": "q4",
    "ingredient": "CaCl2·2H2O",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.009",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.009",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; CaCl2·2H2O",
        "exact_source_quote": "CaCl 2 ·2H 2 O 0.009 g",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"CaCl2·2H2O\",\n          \"volume\": 0.009,\n          \"unit\": \"g\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "The printed gram amount agrees numerically, but both layers label it G_PER_L. Preserve the source batch grams alongside the separately specified 1 L water and qualify the denominator rather than claim a measured final concentration. Neither layer has attached amount evidence."
  },
  {
    "decision_id": "q5",
    "ingredient": "KH2PO4",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.041",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.041",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; KH2PO4",
        "exact_source_quote": "KH 2 PO 4 0.041 g",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.041,\n          \"unit\": \"g\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "The printed gram amount agrees numerically, but both layers label it G_PER_L. Preserve the source batch grams alongside the separately specified 1 L water and qualify the denominator rather than claim a measured final concentration. Neither layer has attached amount evidence."
  },
  {
    "decision_id": "q6",
    "ingredient": "NaMoO4·2H2O",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; NaMoO4·2H2O",
        "exact_source_quote": "NaMoO 4 ·2H 2 O 0.5 mg",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"NaMoO4·2H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "Both layers retain the number 0.5 but use G_PER_L where the primary and provider print mg. Preserve the original milligram batch amount and source basis; merely relabeling to a final mg/L value would still need a justified denominator. The one-sodium printed formula is retained as a source ambiguity; the ontology sodium molybdate dihydrate formula has two sodium atoms."
  },
  {
    "decision_id": "q7",
    "ingredient": "FeSO4·7H2O",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; FeSO4·7H2O",
        "exact_source_quote": "FeSO 4 ·7H 2 O 5 mg",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"FeSO4·7H2O\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "Both layers retain the number 5 but use G_PER_L where the primary and provider print mg. Preserve the original milligram batch amount and source basis; merely relabeling to a final mg/L value would still need a justified denominator."
  },
  {
    "decision_id": "q8",
    "ingredient": "KCl",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.052",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.052",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; KCl",
        "exact_source_quote": "KCl 0.052 g",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.052,\n          \"unit\": \"g\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "The printed gram amount agrees numerically, but both layers label it G_PER_L. Preserve the source batch grams alongside the separately specified 1 L water and qualify the denominator rather than claim a measured final concentration. Neither layer has attached amount evidence."
  },
  {
    "decision_id": "q9",
    "ingredient": "CoCl2·6H2O",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; CoCl2·6H2O",
        "exact_source_quote": "CoCl 2 ·6H 2 O 0.5 mg",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"CoCl2·6H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "Both layers retain the number 0.5 but use G_PER_L where the primary and provider print mg. Preserve the original milligram batch amount and source basis; merely relabeling to a final mg/L value would still need a justified denominator."
  },
  {
    "decision_id": "q10",
    "ingredient": "NiCl2·6H2O",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; NiCl2·6H2O",
        "exact_source_quote": "NiCl 2 ·6H 2 O 1 mg",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"NiCl2·6H2O\",\n          \"volume\": 1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "Both layers retain the number 1 but use G_PER_L where the primary and provider print mg. Preserve the original milligram batch amount and source basis; merely relabeling to a final mg/L value would still need a justified denominator."
  },
  {
    "decision_id": "q11",
    "ingredient": "ZnSO4·7H2O",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; ZnSO4·7H2O",
        "exact_source_quote": "ZnSO 4 ·7H 2 O 1 mg",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"ZnSO4·7H2O\",\n          \"volume\": 1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "Both layers retain the number 1 but use G_PER_L where the primary and provider print mg. Preserve the original milligram batch amount and source basis; merely relabeling to a final mg/L value would still need a justified denominator."
  },
  {
    "decision_id": "q12",
    "ingredient": "CuSO4·5H2O",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; CuSO4·5H2O",
        "exact_source_quote": "CuSO 4 ·5H 2 O 2 mg",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[11]",
        "exact_source_quote": "\"component_name\": \"CuSO4·5H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "Both layers retain the number 2 but use G_PER_L where the primary and provider print mg. Preserve the original milligram batch amount and source basis; merely relabeling to a final mg/L value would still need a justified denominator."
  },
  {
    "decision_id": "q13",
    "ingredient": "MnSO4·5H2O",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; MnSO4·5H2O",
        "exact_source_quote": "MnSO 4 ·5H 2 O 1 mg",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[12]",
        "exact_source_quote": "\"component_name\": \"MnSO4·5H2O\",\n          \"volume\": 1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "Both layers retain the number 1 but use G_PER_L where the primary and provider print mg. Preserve the original milligram batch amount and source basis; merely relabeling to a final mg/L value would still need a justified denominator."
  },
  {
    "decision_id": "q14",
    "ingredient": "(NH4)2SO4·7H2O",
    "decision": "correct",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.132",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.132",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; (NH4)2SO4·7H2O",
        "exact_source_quote": "(NH4) 2 SO 4 ·7H 2 O 0.132 g",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[13]",
        "exact_source_quote": "\"component_name\": \"(NH4)2SO4·7H2O\",\n          \"volume\": 0.132,\n          \"unit\": \"g\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "The printed gram amount agrees numerically, but both layers label it G_PER_L. Preserve the source batch grams alongside the separately specified 1 L water and qualify the denominator rather than claim a measured final concentration. Neither layer has attached amount evidence. The source itself prints ammonium sulfate heptahydrate; do not silently replace it with anhydrous ammonium sulfate or assign a guessed term."
  },
  {
    "decision_id": "q15",
    "ingredient": "H2SO4",
    "decision": "not_quantified",
    "stage": "Main recipe batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Main recipe batch; H2SO4",
        "exact_source_quote": "Adjust pH to 1.3 with H 2 SO 4.",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      },
      {
        "source_key": "togoM1629original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629",
        "source_locator": "$.components[0].items[14]",
        "exact_source_quote": "\"component_name\": \"H2SO4\"",
        "snapshot_sha256": "59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a"
      }
    ],
    "interpretation": "The VARIABLE placeholder has no numerical source dose or acid stock strength. Preserve sulfuric acid as the pH-adjusting reagent and link the separately documented pH 1.3 endpoint; do not invent an amount."
  },
  {
    "decision_id": "q16",
    "ingredient": "Target pH",
    "decision": "add",
    "stage": "Sulfuric-acid adjustment",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; Sulfuric-acid adjustment; Target pH",
        "exact_source_quote": "Adjust pH to 1.3 with H 2 SO 4.",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      }
    ],
    "interpretation": "Both layers omit the explicit target pH 1.3. Add evidence at the stated adjustment stage; this is not a measured post-growth pH."
  },
  {
    "decision_id": "q17",
    "ingredient": "Final volume",
    "decision": "not_quantified",
    "stage": "After dissolution and acid adjustment",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc831",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831",
        "source_locator": "NBRC 831; After dissolution and acid adjustment; Final volume",
        "exact_source_quote": "Distilled water 1 L Adjust pH to 1.3 with H 2 SO 4.",
        "snapshot_sha256": "ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd",
        "parsed_text_sha256": "00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08"
      }
    ],
    "interpretation": "The source gives 1 L of water followed by acid adjustment, without a final make-up instruction or measured volume. Do not normalize all masses to an asserted final 1 L."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:008184.

13 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 13/15 primary and 11/15 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 15: primary 86.67%; secondary 73.33%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Supplied chemical forms versus ontology structures

grounding: concern. Targets: CultureMech:008184.

The source cobalt and nickel chlorides are hexahydrates, whereas CHEBI:35696 and CHEBI:34887 describe anhydrous chlorides; nickel repeats the mismatch in its current secondary key. Other specified Mg/Ca/Fe/Zn/Cu/Mn hydrates match their asserted labels and structures. The source-printed NaMoO4·2H2O disagrees with the two-sodium ontology formula, and (NH4)2SO4·7H2O remains an unresolved source formula. These ambiguities do not license guessed replacements or molar conversions.

### pH, conditional atmosphere and omitted details

completeness: concern. Targets: CultureMech:008184.

Both layers omit the explicit pH 1.3 adjustment. The exact heterotrophic source supplies no sterilization cycle, cultivation temperature, conditional gas requirement or final-volume measurement. Details from NBRC 830 must not be transferred here.

### Composition and growth-claim scope

scope: supported. Targets: CultureMech:008184.

Yeast extract supports COMPLEX and UNDEFINED classification, while the absence of agar agrees with LIQUID. The archaea category and heterotrophic title describe catalogue scope; no strain-specific experimental growth assertion or taxonomy accession is inferred.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:008184.

21 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Claim-level evidence and current transformation boundaries

evidence: concern. Targets: CultureMech:008184.

Both layers retain accession notes and import/enrichment history, but no ingredient amount, form or preparation claim has attached primary-source evidence. Exact current captures support this review; the original historical import bytes and historical writer behavior are not inferred.

## Findings

### f1: Seven milligram rows and water have wrong units

blocker / open / confirmed; issue key: wrong-source-units.

Seven source milligram amounts are stored as the same numeric values in G_PER_L in both layers. Water is 1 L in the source but 1 G_PER_L locally. Remaining gram values also require an explicit batch basis rather than an unproven final-volume denominator. These errors materially change the represented formulation.

### f2: Supplied hydrates are not represented by the asserted chloride terms

major / open / confirmed; issue key: hydrate-and-form-scope.

CoCl2·6H2O and NiCl2·6H2O are grounded to anhydrous chlorides. Nickel repeats the same form mismatch in its secondary link. Separately, preserve the source-printed molybdate and ammonium sulfate formula ambiguities without inventing corrected chemistry.

### f3: Source pH adjustment is absent

major / open / confirmed; issue key: preparation-and-ph.

Neither layer records the explicit pH 1.3 adjustment. The VARIABLE acid placeholder does not preserve this target or its preparation role.

### f4: Source notes do not supply claim-level formulation evidence

minor / open / confirmed; issue key: claim-evidence-gap.

The maintained and generated layers lack attached evidence for quantities, supplied forms and preparation. Valid current identifiers and import history cannot substitute for these claims.

## Recommended Actions And Acceptance Checks

### a1

Correct units and preserve original batch amounts and water volume in the maintained owner, attaching exact evidence and documenting the denominator. Regenerate only after owner corrections are independently checked.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve source-supplied forms before proposing replacement terms; independently verify each primary and secondary mapping. Keep the ambiguous source formulas explicit and retain original mass units.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add the exact source-scoped pH adjustment with claim-level evidence, retaining the unquantified sulfuric-acid dose. Do not transfer gas requirements or ferric sulfate from the autotrophic recipe.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach exact primary snippets, persistent URLs, original access times and snapshot hashes to each corrected or retained scientific claim; preserve append-only provenance.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch034/338/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-034/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch034/338/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml:1:id: CultureMech:008184<br>./data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml:1:id: CultureMech:008184<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch034/source-preflight-bound/338/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 17 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary-identity | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831; NBRC medium number and title | supports | Exact accession and title match the maintained owner and generated target. |
| primary-formulation | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831; NBRC 831 complete composition table | supports | Original grams, milligrams and 1 L water are retained; the source does not state a measured final volume. |
| primary-preparation | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831; NBRC 831 preparation paragraph | supports | The exact heterotrophic recipe specifies pH 1.3 adjustment with sulfuric acid. No conditional gas paragraph is present. |
| provider-identity | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629; $.meta and complete $.components[0], $.comments | supports | TOGO M1629 explicitly identifies NBRC_M831 and its primary URL; ingredient order and original units are independently compared. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch034/338/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131524 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131524; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131524 resolves to manganese(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131524": [{"label": "MnSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131524", "preferred_term": "MnSO4 x 5 H2O", "ontology_id": "CHEBI:131524", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml; data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml", "events": 10, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current _parse_unit maps mg to MG_PER_L and L to L, but promotes plain g to G_PER_L; _extract_ph reads a top-level field whereas this provider places pH in meta/comments. Current preparation extraction and formulation-equality merging were read. These current functions do not prove which historical version produced the stored errors. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current _parse_unit maps mg to MG_PER_L and L to L, but promotes plain g to G_PER_L; _extract_ph reads a top-level field whereas this provider places pH in meta/comments. Current preparation extraction and formulation-equality merging were read. These current functions do not prove which historical version produced the stored errors. |
| togoM1629-attempt | https://mediumapi.dbcls.jp/medium/M1629; Preserved exact public retrieval result | context_only | The alternate TOGO mediumapi request failed DNS; its real failed attempt is retained. The exact original TOGO endpoint and NBRC 831 primary are usable, so this optional access failure does not leave the current formulation review incomplete. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The alternate TOGO mediumapi request failed DNS; its real failed attempt is retained. The exact original TOGO endpoint and NBRC 831 primary are usable, so this optional access failure does not leave the current formulation review incomplete.
- Source formula ambiguities and absent preparation quantities remain explicit. No source correction, replacement term, sterilization cycle, molar concentration or measured final volume is invented. No historical import-byte equivalence is asserted.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T185233Z-culturemech-008184-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidianus_manzaensis_medium_for_heterotrophic_growth
  (CultureMech:008184)'
started_at: '2026-10-21T18:47:07Z'
finished_at: '2026-10-21T18:52:33Z'
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
summary: The exact NBRC 831 and TOGO M1629 identities resolve. Seven milligram amounts
  and the water volume are represented with wrong units; source preparation and hydrate
  grounding also need curation. Printed source formula ambiguities remain explicit.
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
  - path: data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml
    sha256: ddec898ee1fbdd234fb94cb8141a149fd3476b809bd5dc3a283be70132d05dcb
    role: target
  - path: data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml
    sha256: 3b80dd7343f6e7d741184ce250c1956b396d64c2b0d3bed8bdddba8e3163f980
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
  - path: src/culturemech/fetch/togo_fetcher.py
    sha256: 7aac40fe1d47e30810ae0be02f6e369ddb9bf657d630072595c62f46fb0bf339
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
  selection: Task review 338; batch 034 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-three task batches
    contain 330 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 333 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008184
targets:
- target_id: CultureMech:008184
  path: data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml
  label: acidianus_manzaensis_medium_for_heterotrophic_growth
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch034/338/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-034/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch034/338/strict.tsv"
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008184
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
  - CultureMech:008184
- check_id: togoM1629-source-access
  name: 'Exact source content access: togoM1629'
  required: false
  status: unavailable
  summary: The alternate TOGO mediumapi request failed DNS; its real failed attempt
    is retained. The exact original TOGO endpoint and NBRC 831 primary are usable,
    so this optional access failure does not leave the current formulation review
    incomplete.
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - togoM1629-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T18:52:32Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T18:52:32Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T18:47:48.570496Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch034/338/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T18:47:49.614747Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-034/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch034/338/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T18:47:50.831850Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T18:47:51.772549Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T18:52:32Z'
  support: supports
  summary: './data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml:1:id:
    CultureMech:008184

    ./data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml:1:id:
    CultureMech:008184

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch034/source-preflight-bound/338/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T18:52:32Z'
  support: supports
  summary: 17 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 5ee416b0f60152f0676a18e0e839c2abb5fb3ebda9e95993ed19bf80497af1e9
- evidence_id: primary-identity
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831
  locator: NBRC medium number and title
  accessed_at: '2026-10-21T18:28:16.138188Z'
  support: supports
  summary: Exact accession and title match the maintained owner and generated target.
  quote: Medium No. 831 Medium Acidianus manzaensis Medium for Heterotrophic Growth
  snapshot_sha256: ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd
- evidence_id: primary-formulation
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831
  locator: NBRC 831 complete composition table
  accessed_at: '2026-10-21T18:28:16.138188Z'
  support: supports
  summary: Original grams, milligrams and 1 L water are retained; the source does
    not state a measured final volume.
  quote: Yeast extract 1 g (NH4) 2 SO 4 ·7H 2 O 0.132 g KCl 0.052 g KH 2 PO 4 0.041
    g MgSO 4 ·7H 2 O 0.49 g CaCl 2 ·2H 2 O 0.009 g ZnSO 4 ·7H 2 O 1 mg CuSO 4 ·5H
    2 O 2 mg MnSO 4 ·5H 2 O 1 mg NaMoO 4 ·2H 2 O 0.5 mg CoCl 2 ·6H 2 O 0.5 mg NiCl
    2 ·6H 2 O 1 mg FeSO 4 ·7H 2 O 5 mg Distilled water 1 L
  snapshot_sha256: ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd
- evidence_id: primary-preparation
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831
  locator: NBRC 831 preparation paragraph
  accessed_at: '2026-10-21T18:28:16.138188Z'
  support: supports
  summary: The exact heterotrophic recipe specifies pH 1.3 adjustment with sulfuric
    acid. No conditional gas paragraph is present.
  quote: Adjust pH to 1.3 with H 2 SO 4.
  snapshot_sha256: ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd
- evidence_id: provider-identity
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629
  locator: $.meta and complete $.components[0], $.comments
  accessed_at: '2026-10-21T18:28:12.464316Z'
  support: supports
  summary: TOGO M1629 explicitly identifies NBRC_M831 and its primary URL; ingredient
    order and original units are independently compared.
  quote: '"original_media_id": "NBRC_M831"'
  snapshot_sha256: 59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch034/338/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T18:52:32Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 50cc5f242c649635de84c55239ec980ca3b1cb326b9eba04209c3bfe4e810070
- evidence_id: chebi131524
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131524
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T18:28:14.699620Z'
  support: supports
  summary: CHEBI:131524 resolves to manganese(II) sulfate pentahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: b6e1ac7c9f7986f57a65ad1b9a026b8815ed01e0fd8db968a1c85c39874a0c72
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
- evidence_id: chebi26836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:29:13.222926Z'
  support: supports
  summary: CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
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
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to nickel dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T18:52:32Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131524":
    [{"label": "MnSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131524",
    "preferred_term": "MnSO4 x 5 H2O", "ontology_id": "CHEBI:131524", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water",
    "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label":
    "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type":
    "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id":
    "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036":
    [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2
    H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml;
    data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T18:52:32Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml",
    "events": 10, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:52:32Z'
  support: context_only
  summary: Current _parse_unit maps mg to MG_PER_L and L to L, but promotes plain
    g to G_PER_L; _extract_ph reads a top-level field whereas this provider places
    pH in meta/comments. Current preparation extraction and formulation-equality merging
    were read. These current functions do not prove which historical version produced
    the stored errors.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:52:32Z'
  support: context_only
  summary: Current _parse_unit maps mg to MG_PER_L and L to L, but promotes plain
    g to G_PER_L; _extract_ph reads a top-level field whereas this provider places
    pH in meta/comments. Current preparation extraction and formulation-equality merging
    were read. These current functions do not prove which historical version produced
    the stored errors.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: togoM1629-attempt
  kind: database
  reference: https://mediumapi.dbcls.jp/medium/M1629
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T18:28:10.999516Z'
  support: context_only
  summary: The alternate TOGO mediumapi request failed DNS; its real failed attempt
    is retained. The exact original TOGO endpoint and NBRC 831 primary are usable,
    so this optional access failure does not leave the current formulation review
    incomplete.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact source accession and recipe boundary
  outcome: supported
  summary: NBRC 831 and TOGO M1629 name this heterotrophic medium. It contains yeast
    extract and is distinct from autotrophic NBRC 830; the other recipe’s ferric sulfate
    and gas requirements are not transferred. No supplier product, DOI, strain accession,
    KG match or structured growth assertion is present to authenticate.
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - record
  - owner-0
  - primary-identity
  - provider-identity
- assessment_id: ownership
  area: ownership
  topic: Single maintained source and generated correspondence
  outcome: supported
  summary: The complete merge event, merged_from and exact stable ID resolve one maintained
    archaea owner. All scientific fields agree between target and owner. Current defects
    are present in both; corrections belong in the maintained source before separately
    authorized regeneration. A fingerprint is provenance, not external formulation
    evidence.
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - record
  - owner-0
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 17 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"ingredient\": \"Distilled\
    \ water\",\n    \"decision\": \"correct\",\n    \"stage\": \"Main recipe batch\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; Distilled water\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1 L\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers store 1 G_PER_L. Restore\
    \ the source quantity 1 L of preparation water; this is neither 1 g/L water nor\
    \ a measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q2\",\n    \"\
    ingredient\": \"MgSO4·7H2O\",\n    \"decision\": \"correct\",\n    \"stage\":\
    \ \"Main recipe batch\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.49\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.49\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; MgSO4·7H2O\",\n\
    \        \"exact_source_quote\": \"MgSO 4 ·7H 2 O 0.49 g\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4·7H2O\\\",\\n          \\\"volume\\\": 0.49,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed gram amount agrees numerically,\
    \ but both layers label it G_PER_L. Preserve the source batch grams alongside\
    \ the separately specified 1 L water and qualify the denominator rather than claim\
    \ a measured final concentration. Neither layer has attached amount evidence.\"\
    \n  },\n  {\n    \"decision_id\": \"q3\",\n    \"ingredient\": \"Yeast extract\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Main recipe batch\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; Yeast extract\"\
    ,\n        \"exact_source_quote\": \"Yeast extract 1 g\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed gram amount agrees numerically,\
    \ but both layers label it G_PER_L. Preserve the source batch grams alongside\
    \ the separately specified 1 L water and qualify the denominator rather than claim\
    \ a measured final concentration. Neither layer has attached amount evidence.\"\
    \n  },\n  {\n    \"decision_id\": \"q4\",\n    \"ingredient\": \"CaCl2·2H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Main recipe batch\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.009\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.009\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; CaCl2·2H2O\",\n\
    \        \"exact_source_quote\": \"CaCl 2 ·2H 2 O 0.009 g\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2·2H2O\\\",\\n          \\\"volume\\\": 0.009,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed gram amount agrees numerically,\
    \ but both layers label it G_PER_L. Preserve the source batch grams alongside\
    \ the separately specified 1 L water and qualify the denominator rather than claim\
    \ a measured final concentration. Neither layer has attached amount evidence.\"\
    \n  },\n  {\n    \"decision_id\": \"q5\",\n    \"ingredient\": \"KH2PO4\",\n \
    \   \"decision\": \"correct\",\n    \"stage\": \"Main recipe batch\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.041\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.041\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; KH2PO4\",\n    \
    \    \"exact_source_quote\": \"KH 2 PO 4 0.041 g\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.041,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed gram amount agrees numerically,\
    \ but both layers label it G_PER_L. Preserve the source batch grams alongside\
    \ the separately specified 1 L water and qualify the denominator rather than claim\
    \ a measured final concentration. Neither layer has attached amount evidence.\"\
    \n  },\n  {\n    \"decision_id\": \"q6\",\n    \"ingredient\": \"NaMoO4·2H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Main recipe batch\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; NaMoO4·2H2O\",\n\
    \        \"exact_source_quote\": \"NaMoO 4 ·2H 2 O 0.5 mg\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaMoO4·2H2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers retain the number 0.5\
    \ but use G_PER_L where the primary and provider print mg. Preserve the original\
    \ milligram batch amount and source basis; merely relabeling to a final mg/L value\
    \ would still need a justified denominator. The one-sodium printed formula is\
    \ retained as a source ambiguity; the ontology sodium molybdate dihydrate formula\
    \ has two sodium atoms.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"ingredient\"\
    : \"FeSO4·7H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Main recipe\
    \ batch\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; FeSO4·7H2O\",\n\
    \        \"exact_source_quote\": \"FeSO 4 ·7H 2 O 5 mg\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4·7H2O\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers retain the number 5 but\
    \ use G_PER_L where the primary and provider print mg. Preserve the original milligram\
    \ batch amount and source basis; merely relabeling to a final mg/L value would\
    \ still need a justified denominator.\"\n  },\n  {\n    \"decision_id\": \"q8\"\
    ,\n    \"ingredient\": \"KCl\",\n    \"decision\": \"correct\",\n    \"stage\"\
    : \"Main recipe batch\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.052\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.052\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; KCl\",\n       \
    \ \"exact_source_quote\": \"KCl 0.052 g\",\n        \"snapshot_sha256\": \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\"\
    ,\n        \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.052,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed gram amount agrees numerically,\
    \ but both layers label it G_PER_L. Preserve the source batch grams alongside\
    \ the separately specified 1 L water and qualify the denominator rather than claim\
    \ a measured final concentration. Neither layer has attached amount evidence.\"\
    \n  },\n  {\n    \"decision_id\": \"q9\",\n    \"ingredient\": \"CoCl2·6H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Main recipe batch\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; CoCl2·6H2O\",\n\
    \        \"exact_source_quote\": \"CoCl 2 ·6H 2 O 0.5 mg\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2·6H2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers retain the number 0.5\
    \ but use G_PER_L where the primary and provider print mg. Preserve the original\
    \ milligram batch amount and source basis; merely relabeling to a final mg/L value\
    \ would still need a justified denominator.\"\n  },\n  {\n    \"decision_id\"\
    : \"q10\",\n    \"ingredient\": \"NiCl2·6H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"stage\": \"Main recipe batch\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; NiCl2·6H2O\",\n\
    \        \"exact_source_quote\": \"NiCl 2 ·6H 2 O 1 mg\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2·6H2O\\\",\\n          \\\"volume\\\": 1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers retain the number 1 but\
    \ use G_PER_L where the primary and provider print mg. Preserve the original milligram\
    \ batch amount and source basis; merely relabeling to a final mg/L value would\
    \ still need a justified denominator.\"\n  },\n  {\n    \"decision_id\": \"q11\"\
    ,\n    \"ingredient\": \"ZnSO4·7H2O\",\n    \"decision\": \"correct\",\n    \"\
    stage\": \"Main recipe batch\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; ZnSO4·7H2O\",\n\
    \        \"exact_source_quote\": \"ZnSO 4 ·7H 2 O 1 mg\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4·7H2O\\\",\\n          \\\"volume\\\": 1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers retain the number 1 but\
    \ use G_PER_L where the primary and provider print mg. Preserve the original milligram\
    \ batch amount and source basis; merely relabeling to a final mg/L value would\
    \ still need a justified denominator.\"\n  },\n  {\n    \"decision_id\": \"q12\"\
    ,\n    \"ingredient\": \"CuSO4·5H2O\",\n    \"decision\": \"correct\",\n    \"\
    stage\": \"Main recipe batch\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; CuSO4·5H2O\",\n\
    \        \"exact_source_quote\": \"CuSO 4 ·5H 2 O 2 mg\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuSO4·5H2O\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers retain the number 2 but\
    \ use G_PER_L where the primary and provider print mg. Preserve the original milligram\
    \ batch amount and source basis; merely relabeling to a final mg/L value would\
    \ still need a justified denominator.\"\n  },\n  {\n    \"decision_id\": \"q13\"\
    ,\n    \"ingredient\": \"MnSO4·5H2O\",\n    \"decision\": \"correct\",\n    \"\
    stage\": \"Main recipe batch\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; MnSO4·5H2O\",\n\
    \        \"exact_source_quote\": \"MnSO 4 ·5H 2 O 1 mg\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnSO4·5H2O\\\",\\n          \\\"volume\\\": 1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers retain the number 1 but\
    \ use G_PER_L where the primary and provider print mg. Preserve the original milligram\
    \ batch amount and source basis; merely relabeling to a final mg/L value would\
    \ still need a justified denominator.\"\n  },\n  {\n    \"decision_id\": \"q14\"\
    ,\n    \"ingredient\": \"(NH4)2SO4·7H2O\",\n    \"decision\": \"correct\",\n \
    \   \"stage\": \"Main recipe batch\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.132\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.132\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; (NH4)2SO4·7H2O\"\
    ,\n        \"exact_source_quote\": \"(NH4) 2 SO 4 ·7H 2 O 0.132 g\",\n       \
    \ \"snapshot_sha256\": \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\"\
    ,\n        \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"(NH4)2SO4·7H2O\\\",\\n          \\\"volume\\\"\
    : 0.132,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The printed gram amount agrees numerically,\
    \ but both layers label it G_PER_L. Preserve the source batch grams alongside\
    \ the separately specified 1 L water and qualify the denominator rather than claim\
    \ a measured final concentration. Neither layer has attached amount evidence.\
    \ The source itself prints ammonium sulfate heptahydrate; do not silently replace\
    \ it with anhydrous ammonium sulfate or assign a guessed term.\"\n  },\n  {\n\
    \    \"decision_id\": \"q15\",\n    \"ingredient\": \"H2SO4\",\n    \"decision\"\
    : \"not_quantified\",\n    \"stage\": \"Main recipe batch\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Main recipe batch; H2SO4\",\n     \
    \   \"exact_source_quote\": \"Adjust pH to 1.3 with H 2 SO 4.\",\n        \"snapshot_sha256\"\
    : \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\",\n    \
    \    \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      },\n      {\n        \"source_key\": \"togoM1629original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1629\"\
    ,\n        \"source_locator\": \"$.components[0].items[14]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H2SO4\\\"\",\n        \"snapshot_sha256\": \"\
    59174ae6234c9b9823bd61469164087b1cb88d966db2ab731e4cbc740babfe8a\"\n      }\n\
    \    ],\n    \"interpretation\": \"The VARIABLE placeholder has no numerical source\
    \ dose or acid stock strength. Preserve sulfuric acid as the pH-adjusting reagent\
    \ and link the separately documented pH 1.3 endpoint; do not invent an amount.\"\
    \n  },\n  {\n    \"decision_id\": \"q16\",\n    \"ingredient\": \"Target pH\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"Sulfuric-acid adjustment\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc831\"\
    ,\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; Sulfuric-acid adjustment; Target pH\"\
    ,\n        \"exact_source_quote\": \"Adjust pH to 1.3 with H 2 SO 4.\",\n    \
    \    \"snapshot_sha256\": \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\"\
    ,\n        \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers omit the explicit target\
    \ pH 1.3. Add evidence at the stated adjustment stage; this is not a measured\
    \ post-growth pH.\"\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"ingredient\"\
    : \"Final volume\",\n    \"decision\": \"not_quantified\",\n    \"stage\": \"\
    After dissolution and acid adjustment\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/Acidianus_manzaensis_Medium_for_Heterotrophic_Growth.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc831\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=831\"\
    ,\n        \"source_locator\": \"NBRC 831; After dissolution and acid adjustment;\
    \ Final volume\",\n        \"exact_source_quote\": \"Distilled water 1 L Adjust\
    \ pH to 1.3 with H 2 SO 4.\",\n        \"snapshot_sha256\": \"ce58faad25c14eaa6855304bbe804e80e0aa55a77ebf9c6c5614e22c2ffe89dd\"\
    ,\n        \"parsed_text_sha256\": \"00da6da89377d32baa82457290d2174235089cf84cf6dd08ce5f7eb60a39ad08\"\
    \n      }\n    ],\n    \"interpretation\": \"The source gives 1 L of water followed\
    \ by acid adjustment, without a final make-up instruction or measured volume.\
    \ Do not normalize all masses to an asserted final 1 L.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '13 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 13/15
    primary and 11/15 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131524
  - chebi15377
  - chebi26836
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi32588
  - chebi34887
  - chebi35696
  - chebi63036
  - chebi75213
  - chebi75836
  - chebi86158
  details: 'Instance coverage on a 0–100 percent scale, denominator 15: primary 86.67%;
    secondary 73.33%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: forms
  area: grounding
  topic: Supplied chemical forms versus ontology structures
  outcome: concern
  summary: The source cobalt and nickel chlorides are hexahydrates, whereas CHEBI:35696
    and CHEBI:34887 describe anhydrous chlorides; nickel repeats the mismatch in its
    current secondary key. Other specified Mg/Ca/Fe/Zn/Cu/Mn hydrates match their
    asserted labels and structures. The source-printed NaMoO4·2H2O disagrees with
    the two-sodium ontology formula, and (NH4)2SO4·7H2O remains an unresolved source
    formula. These ambiguities do not license guessed replacements or molar conversions.
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - primary-formulation
  - chebi35696
  - chebi34887
  - chebi75213
  - mim
- assessment_id: preparation
  area: completeness
  topic: pH, conditional atmosphere and omitted details
  outcome: concern
  summary: Both layers omit the explicit pH 1.3 adjustment. The exact heterotrophic
    source supplies no sterilization cycle, cultivation temperature, conditional gas
    requirement or final-volume measurement. Details from NBRC 830 must not be transferred
    here.
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - primary-preparation
  - record
  - owner-0
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Composition and growth-claim scope
  outcome: supported
  summary: Yeast extract supports COMPLEX and UNDEFINED classification, while the
    absence of agar agrees with LIQUID. The archaea category and heterotrophic title
    describe catalogue scope; no strain-specific experimental growth assertion or
    taxonomy accession is inferred.
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - primary-formulation
  - primary-identity
  - record
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 21 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: provenance
  area: evidence
  topic: Claim-level evidence and current transformation boundaries
  outcome: concern
  summary: Both layers retain accession notes and import/enrichment history, but no
    ingredient amount, form or preparation claim has attached primary-source evidence.
    Exact current captures support this review; the original historical import bytes
    and historical writer behavior are not inferred.
  target_ids:
  - CultureMech:008184
  evidence_ids:
  - record
  - owner-0
  - primary-formulation
  - provider-identity
  - writer-0
  - writer-1
findings:
- finding_id: f1
  issue_key: wrong-source-units
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Seven milligram rows and water have wrong units
  description: Seven source milligram amounts are stored as the same numeric values
    in G_PER_L in both layers. Water is 1 L in the source but 1 G_PER_L locally. Remaining
    gram values also require an explicit batch basis rather than an unproven final-volume
    denominator. These errors materially change the represented formulation.
  target_ids:
  - CultureMech:008184
  field_paths:
  - ingredients
  evidence_ids:
  - primary-formulation
  - quantity-inventory
  - record
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml
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
  issue_key: hydrate-and-form-scope
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Supplied hydrates are not represented by the asserted chloride terms
  description: CoCl2·6H2O and NiCl2·6H2O are grounded to anhydrous chlorides. Nickel
    repeats the same form mismatch in its secondary link. Separately, preserve the
    source-printed molybdate and ammonium sulfate formula ambiguities without inventing
    corrected chemistry.
  target_ids:
  - CultureMech:008184
  field_paths:
  - ingredients[8].term
  - ingredients[9].term
  - ingredients[9].mediaingredientmech_chebi_term
  - ingredients[5]
  - ingredients[13]
  evidence_ids:
  - primary-formulation
  - chebi35696
  - chebi34887
  - chebi75213
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml
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
  issue_key: preparation-and-ph
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source pH adjustment is absent
  description: Neither layer records the explicit pH 1.3 adjustment. The VARIABLE
    acid placeholder does not preserve this target or its preparation role.
  target_ids:
  - CultureMech:008184
  field_paths:
  - ph_value
  - preparation_steps
  - ingredients[14]
  evidence_ids:
  - primary-preparation
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml
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
  issue_key: claim-evidence-gap
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Source notes do not supply claim-level formulation evidence
  description: The maintained and generated layers lack attached evidence for quantities,
    supplied forms and preparation. Valid current identifiers and import history cannot
    substitute for these claims.
  target_ids:
  - CultureMech:008184
  field_paths:
  - ingredients
  - notes
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - primary-formulation
  - primary-preparation
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml
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
  description: Correct units and preserve original batch amounts and water volume
    in the maintained owner, attaching exact evidence and documenting the denominator.
    Regenerate only after owner corrections are independently checked.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008184
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml
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
  description: Resolve source-supplied forms before proposing replacement terms; independently
    verify each primary and secondary mapping. Keep the ambiguous source formulas
    explicit and retain original mass units.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008184
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml
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
  description: Add the exact source-scoped pH adjustment with claim-level evidence,
    retaining the unquantified sulfuric-acid dose. Do not transfer gas requirements
    or ferric sulfate from the autotrophic recipe.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008184
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml
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
  description: Attach exact primary snippets, persistent URLs, original access times
    and snapshot hashes to each corrected or retained scientific claim; preserve append-only
    provenance.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008184
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/acidianus_manzaensis_medium_for_heterotrophic_growth.yaml
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
- The alternate TOGO mediumapi request failed DNS; its real failed attempt is retained.
  The exact original TOGO endpoint and NBRC 831 primary are usable, so this optional
  access failure does not leave the current formulation review incomplete.
- Source formula ambiguities and absent preparation quantities remain explicit. No
  source correction, replacement term, sterilization cycle, molar concentration or
  measured final volume is invented. No historical import-byte equivalence is asserted.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-034
- generated-medium
```
