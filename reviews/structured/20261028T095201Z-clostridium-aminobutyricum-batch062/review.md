# Clostridium aminobutyricum medium: source stock boundaries and preparation retention

- Review: 20261028T095201Z-clostridium-aminobutyricum-batch062
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T09:27:38.194300Z
- Finished UTC: 2026-10-28T09:52:01.482683Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Three major findings concern omitted preparation, flattened stocks/unresolved volume basis and sodium-resazurin grounding; two minor findings concern evidence placement and history timestamps. All 33 quantity fields and 57 chemical-ID slots were assessed. Native checks pass, but fresh KOMODO accession access 403 prevents complete source verification.

## Scope And Provenance

One complete generated target, two maintained contributors and exact DSMZ 286 source formulation; all 16 quantity decisions retained.

Selection: Batch 062 item 10 in Python path order, selected after 543 of 6325 targets had coverage from successful native validated lists.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:004743 | data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml | generated | clostridium_aminobutyricum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:004743 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:004743 | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch062/record10/strict.tsv |
| validate-terms | passed | True | CultureMech:004743 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:004743 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| check-mim-label-index | passed | True | CultureMech:004743 | MIM label index OK: 9,077 rows, 8,733 labels, commit 6643131b0f12ab40b66f98135245fca04027e0e9<br>Decisions: ambiguous=23, hydrate_conflict=12, mapped=8,347, undecided=1, unmapped=350<br>uv run python scripts/check_mim_label_index.py |
| Embedded history and internal reference review | failed | False | CultureMech:004743 | Parent/child IDs and paths resolve. KOMODO import history has literal .fZ and resolver history lacks timezone; no focused native history validator is claimed. |
| Full-corpus ID/product/merge gates | skipped | False | CultureMech:004743 | No scientific records/schema/generators changed. Full-corpus assign-ids-check, validate-products, verify-merges and audit-merge-freshness were not run; in-memory pair rejection is only a scoped diagnostic. |

## Scientific And Domain Assessments

### DSMZ286 source identity and KOMODO duplicate relationship

identity: supported. Targets: CultureMech:004743.

Stable selected target and its two maintained owners resolve. DSMZ source name/pH/composition and historical KOMODO row support the intended source identity; fresh KOMODO access 403 limits current accession verification.

Ingredient signatures match, but not all scientific/provenance content does. This is one unambiguous target; two contributor records are context, not separate reviewed targets.

### Every existing amount and source-only dose boundary

quantity: concern. Targets: CultureMech:004743.

All 33 local amounts match provider g_l, but the provider volume and primary-source water/addition basis conflict. Two explicit percentage stocks and post-sterilization sulfide delivery are flattened.

{
  "created_at": "2026-10-28T09:36:11.055156Z",
  "target": "data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml",
  "scope": "All 33 concentration fields across selected target and two maintained contributors, plus solvent, two stock strengths, unquantified sulfide dosing and provider volume.",
  "decisions": [
    {
      "decision_id": "Q01",
      "ingredient": "KH2PO4",
      "decision": "unsupported",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml",
          "field": "ingredients[0].concentration",
          "value": {
            "value": "1.3",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml",
          "field": "ingredients[0].concentration",
          "value": {
            "value": "1.3",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml",
          "field": "ingredients[0].concentration",
          "value": {
            "value": "1.3",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[0]; DSMZ PDF p1 corresponding row",
      "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.3,\n                        \"mmol_l\": 9.55285,\n                        \"optional\": 0\n                    }",
      "explanation": "Exact source mass and provider g_l are retained; the source specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata does not establish an actual final volume. No rescaling to 1001 ml or 1001.5 ml is endorsed.",
      "calculation": "1.3 g is directly reported for the batch. Provider g_l=1.3; division by its volume 1.001 L would yield 1.298701299 g/L, an inconsistency diagnostic only.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q02",
      "ingredient": "K2HPO4",
      "decision": "unsupported",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml",
          "field": "ingredients[1].concentration",
          "value": {
            "value": "7",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml",
          "field": "ingredients[1].concentration",
          "value": {
            "value": "7",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml",
          "field": "ingredients[1].concentration",
          "value": {
            "value": "7",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[1]; DSMZ PDF p1 corresponding row",
      "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 7,\n                        \"unit\": \"g\",\n                        \"g_l\": 7,\n                        \"mmol_l\": 40.1892,\n                        \"optional\": 0\n                    }",
      "explanation": "Exact source mass and provider g_l are retained; the source specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata does not establish an actual final volume. No rescaling to 1001 ml or 1001.5 ml is endorsed.",
      "calculation": "7 g is directly reported for the batch. Provider g_l=7; division by its volume 1.001 L would yield 6.993006993 g/L, an inconsistency diagnostic only.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q03",
      "ingredient": "MgCl2 x 6 H2O",
      "decision": "unsupported",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml",
          "field": "ingredients[2].concentration",
          "value": {
            "value": "0.2",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml",
          "field": "ingredients[2].concentration",
          "value": {
            "value": "0.2",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml",
          "field": "ingredients[2].concentration",
          "value": {
            "value": "0.2",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[2]; DSMZ PDF p1 corresponding row",
      "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.983753,\n                        \"optional\": 0\n                    }",
      "explanation": "Exact source mass and provider g_l are retained; the source specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata does not establish an actual final volume. No rescaling to 1001 ml or 1001.5 ml is endorsed.",
      "calculation": "0.2 g is directly reported for the batch. Provider g_l=0.2; division by its volume 1.001 L would yield 0.1998001998 g/L, an inconsistency diagnostic only.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q04",
      "ingredient": "FeCl3 x 6 H2O",
      "decision": "unsupported",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml",
          "field": "ingredients[3].concentration",
          "value": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml",
          "field": "ingredients[3].concentration",
          "value": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml",
          "field": "ingredients[3].concentration",
          "value": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[3]; DSMZ PDF p1 corresponding row",
      "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0369965,\n                        \"optional\": 0\n                    }",
      "explanation": "Exact source mass and provider g_l are retained; the source specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata does not establish an actual final volume. No rescaling to 1001 ml or 1001.5 ml is endorsed.",
      "calculation": "0.01 g is directly reported for the batch. Provider g_l=0.01; division by its volume 1.001 L would yield 0.00999000999 g/L, an inconsistency diagnostic only.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q05",
      "ingredient": "CaCl2 x 2 H2O",
      "decision": "unsupported",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml",
          "field": "ingredients[4].concentration",
          "value": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml",
          "field": "ingredients[4].concentration",
          "value": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml",
          "field": "ingredients[4].concentration",
          "value": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[4]; DSMZ PDF p1 corresponding row",
      "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0680203,\n                        \"optional\": 0\n                    }",
      "explanation": "Exact source mass and provider g_l are retained; the source specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata does not establish an actual final volume. No rescaling to 1001 ml or 1001.5 ml is endorsed.",
      "calculation": "0.01 g is directly reported for the batch. Provider g_l=0.01; division by its volume 1.001 L would yield 0.00999000999 g/L, an inconsistency diagnostic only.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q06",
      "ingredient": "Na2MoO4 x 2 H2O",
      "decision": "conflict",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml",
          "field": "ingredients[5].concentration",
          "value": {
            "value": "0.001",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml",
          "field": "ingredients[5].concentration",
          "value": {
            "value": "0.001",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml",
          "field": "ingredients[5].concentration",
          "value": {
            "value": "0.001",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[5]; DSMZ PDF p1 corresponding row",
      "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00413309,\n                        \"optional\": 0\n                    }",
      "explanation": "Source is a measured dose of 0.1% w/v stock; direct g/L representation loses stock composition and addition stage. Provider g_l equals the added mass per nominal liter, but final volume is not explicitly made up. Preserve both stock and receiving-dose identities.",
      "calculation": "0.1 g/100 ml =1 mg/ml; 1 ml supplies 1 mg. Dividing by an assumed 1 L reproduces 0.001 g/L; the final-volume assumption is not established.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q07",
      "ingredient": "Yeast extract",
      "decision": "unsupported",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml",
          "field": "ingredients[6].concentration",
          "value": {
            "value": "3",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml",
          "field": "ingredients[6].concentration",
          "value": {
            "value": "3",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml",
          "field": "ingredients[6].concentration",
          "value": {
            "value": "3",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[6]; DSMZ PDF p1 corresponding row",
      "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }",
      "explanation": "Exact source mass and provider g_l are retained; the source specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata does not establish an actual final volume. No rescaling to 1001 ml or 1001.5 ml is endorsed.",
      "calculation": "3 g is directly reported for the batch. Provider g_l=3; division by its volume 1.001 L would yield 2.997002997 g/L, an inconsistency diagnostic only.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q08",
      "ingredient": "gamma-Aminobutyric acid",
      "decision": "unsupported",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml",
          "field": "ingredients[7].concentration",
          "value": {
            "value": "5",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml",
          "field": "ingredients[7].concentration",
          "value": {
            "value": "5",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml",
          "field": "ingredients[7].concentration",
          "value": {
            "value": "5",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[7]; DSMZ PDF p1 corresponding row",
      "snippet": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"gamma-Aminobutyric acid\",\n                        \"compound_id\": 355,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 48.4872,\n                        \"optional\": 0\n                    }",
      "explanation": "Exact source mass and provider g_l are retained; the source specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata does not establish an actual final volume. No rescaling to 1001 ml or 1001.5 ml is endorsed.",
      "calculation": "5 g is directly reported for the batch. Provider g_l=5; division by its volume 1.001 L would yield 4.995004995 g/L, an inconsistency diagnostic only.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q09",
      "ingredient": "Agar",
      "decision": "unsupported",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml",
          "field": "ingredients[8].concentration",
          "value": {
            "value": "1.5",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml",
          "field": "ingredients[8].concentration",
          "value": {
            "value": "1.5",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml",
          "field": "ingredients[8].concentration",
          "value": {
            "value": "1.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[8]; DSMZ PDF p1 corresponding row",
      "snippet": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 4.45991,\n                        \"optional\": 0\n                    }",
      "explanation": "Exact source mass and provider g_l are retained; the source specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata does not establish an actual final volume. No rescaling to 1001 ml or 1001.5 ml is endorsed.",
      "calculation": "1.5 g is directly reported for the batch. Provider g_l=1.5; division by its volume 1.001 L would yield 1.498501499 g/L, an inconsistency diagnostic only.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q10",
      "ingredient": "Sodium resazurin",
      "decision": "conflict",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml",
          "field": "ingredients[9].concentration",
          "value": {
            "value": "0.0005",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml",
          "field": "ingredients[9].concentration",
          "value": {
            "value": "0.0005",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml",
          "field": "ingredients[9].concentration",
          "value": {
            "value": "0.0005",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[9]; DSMZ PDF p1 corresponding row",
      "snippet": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }",
      "explanation": "Source is a measured dose of 0.1% w/v stock; direct g/L representation loses stock composition and addition stage. Provider g_l equals the added mass per nominal liter, but final volume is not explicitly made up. Preserve both stock and receiving-dose identities.",
      "calculation": "0.1 g/100 ml =1 mg/ml; 0.5 ml supplies 0.5 mg. Dividing by an assumed 1 L reproduces 0.0005 g/L; the final-volume assumption is not established.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q11",
      "ingredient": "Na2S x 9 H2O",
      "decision": "conflict",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml",
          "field": "ingredients[10].concentration",
          "value": {
            "value": "0.3",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml",
          "field": "ingredients[10].concentration",
          "value": {
            "value": "0.3",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml",
          "field": "ingredients[10].concentration",
          "value": {
            "value": "0.3",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[10]; DSMZ PDF p1 corresponding row",
      "snippet": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.24905,\n                        \"optional\": 0\n                    }",
      "explanation": "Exact source mass and provider g_l are retained; the source specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata does not establish an actual final volume. No rescaling to 1001 ml or 1001.5 ml is endorsed. Source separately requires post-sterilization delivery from sterile anoxic sulfide stock; its strength and dose are unspecified.",
      "calculation": "0.3 g is directly reported for the batch. Provider g_l=0.3; division by its volume 1.001 L would yield 0.2997002997 g/L, an inconsistency diagnostic only.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q12",
      "ingredient": "Distilled water",
      "decision": "evidence_only",
      "fields": [],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[11]; PDF p1 water row",
      "snippet": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
      "explanation": "The solvent batch amount is 1000 ml, not an explicit instruction to make the completed medium to a final volume. Omission as a nutrient edge alone is not a defect.",
      "calculation": "No final-volume conversion is certified.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q13",
      "ingredient": "Na2MoO4 x 2 H2O stock strength",
      "decision": "evidence_only",
      "fields": [],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[5].attribute",
      "snippet": "\"attribute\": \"0.1% w/v\"",
      "explanation": "Exact source stock strength; keep distinct from its receiving volume and final-medium concentration.",
      "calculation": "0.1 g per 100 ml stock =1 g/L stock; no density is assumed.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q14",
      "ingredient": "Sodium resazurin stock strength",
      "decision": "evidence_only",
      "fields": [],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].recipe[9].attribute",
      "snippet": "\"attribute\": \"0.1% w/v\"",
      "explanation": "Exact source stock strength; keep distinct from its receiving volume and final-medium concentration.",
      "calculation": "0.1 g per 100 ml stock =1 g/L stock; no density is assumed.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q15",
      "ingredient": "Sulfide stock strength and dose",
      "decision": "not_quantified",
      "fields": [],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].steps[0].step",
      "snippet": "After sterilization add sulfide from a sterile anoxic stock solution prepared under 100% N2 gas atmosphere.",
      "explanation": "Source requires a separate addition stage but supplies no stock concentration or dispensing volume. Neither is inferred from the total sulfide mass.",
      "calculation": "No final-volume conversion is certified.",
      "proposed": "No replacement final-medium concentration asserted."
    },
    {
      "decision_id": "Q16",
      "ingredient": "Provider solution volume",
      "decision": "conflict",
      "fields": [],
      "reference": "https://mediadive.dsmz.de/rest/medium/286",
      "locator": "$.data.solutions[0].volume",
      "snippet": "\"volume\": 1001",
      "explanation": "Provider volume 1001 ml conflicts with a naive sum 1000 + 1 + 0.5 ml, and neither number proves final volume after dissolved solids and sulfide stock. Preserve the disagreement and nominal basis.",
      "calculation": "1000 + 1 + 0.5=1001.5 ml is only a source-input sum, not a validated final volume.",
      "proposed": "No replacement final-medium concentration asserted."
    }
  ],
  "local_concentration_field_count": 33,
  "decision_count": 16,
  "conditions": {
    "preparation_ph": 7.2,
    "atmosphere": "100%N2 in source preparation, not a growth-rate assertion",
    "sterilization": "autoclave; no temperature/time asserted by this source",
    "physical_state": "Agar1.5g per1000ml-water batch; SOLID_AGAR remains unverified as a phase assignment. SEMISOLID is not substituted by assumption.",
    "growth": "No strain, incubation temperature or experimental growth assertion in target/source."
  }
}

### Retained DSMZ preparation versus generated omission

completeness: concern. Targets: CultureMech:004743.

The DSMZ owner retains the complete source paragraph under AUTOCLAVE. The KOMODO owner and merged record omit it; their parent path resolves to that content, which is credited. The stored merge is not lossless, and the current merger rejects the pair.

Source supports preparation pH 7.2, anaerobic handling and post-sterilization addition. No time/temperature is invented. Complex/undefined bacterial classification is consistent with yeast extract; solid-agar phase remains unverified rather than automatically changed to semisolid.

### Exact forms, IDs and MIM coverage

grounding: concern. Targets: CultureMech:004743.

Ten asserted ChEBI IDs resolve and labels match;57 primary/MIM slots across three documents were inspected. Nine exact-form chemical identities are supported, but sodium resazurin maps to neutral resazurin. The MIM snapshot repeats that synonym mismatch.

Selected record:10/11 primary ChEBI labels and 9/11 dedicated MIM CHEBI links;11/11 resolver answers include FOODON for yeast extract. These are linkage counts only. Yeast-extract FOODON is a diagnostic resolver result, not a new externally validated assignment. No replacement ChEBI for the sodium salt is invented.

### Source evidence placement and historical reports

evidence: concern. Targets: CultureMech:004743.

No formulation evidence/reference entries are attached to these three YAMLs; native reference validation checks zero. Five exact historical reports were fully read, including all 14 source/formulation objects in each October 7 report. Current API hash equals the historical source hash.

Historical rows preserve unresolved questions; no previous structured issue is resolved or retired. Fresh exact KOMODO access is unavailable; source identity is supported indirectly by retained historical row and current DSMZ content.

### Timestamp fidelity

provenance: concern. Targets: CultureMech:004743.

Literal .fZ is invalid fractional-second history; timezone-naive enrichment timestamp is ambiguous. Current KOMODO writer uses time.strftime(%f), and resolver uses datetime.now().isoformat() without timezone.

Preserve earlier events append-only; any separately authorized correction should explain the historic ambiguity rather than fabricate an exact time.

### Required checks and source-review scope

schema: supported. Targets: CultureMech:004743.

Four canonical record checks and MIM integrity pass. Chemical scientific correspondence and source recipe support were checked separately.

No explicit target organism, gene, locus, protein or transcriptomic claim is asserted. iModulonDB is not applicable; no negative literature claim or new growth assertion is made.

## Findings

### F1: Stored merged record drops source preparation retained by its DSMZ owner

major / open / confirmed; issue key: cm004743-preparation-omission-in-merged-record.

Generated and KOMODO records lack the source preparation paragraph. DSMZ owner and reachable parent record retain it, including anoxic handling and deferred sulfide addition. Current resolver copying omits preparation; current merger correctly rejects unequal full content, so the historical generated record needs source reconciliation and regeneration.

### F2: Stock additions are flattened onto an unresolved final-volume basis

major / open / confirmed; issue key: cm004743-stock-topology-and-volume-basis.

Molybdate and sodium-resazurin stocks are represented only as direct mass concentrations; sulfide stock staging is absent in selected target. API g_l agrees with stored values but conflicts with API 1001 ml volume, while PDF gives 1000 ml water plus additions without final makeup. These are unresolved source/basis issues, not a license to divide everything by 1001 or 1001.5 ml.

### F3: Sodium resazurin is grounded to the neutral parent

major / open / confirmed; issue key: cm004743-sodium-resazurin-neutral-grounding.

The source names sodium resazurin. CHEBI:8806 is the neutral C12H7NO4 parent, whereas authoritative sodium-salt identity has C12H6NNaO4. The exact MIM synonym lookup repeats the neutral mapping and cannot independently validate supplied chemical form.

### F4: Recoverable sources lack claim-level formulation evidence

minor / open / confirmed; issue key: cm004743-formulation-evidence-placement.

Source identity can be recovered through DSMZ parent notes and historical mapping, but no structured formulation evidence or bibliography is attached. Reference validation therefore checks zero objects.

### F5: Import history contains malformed or timezone-ambiguous timestamps

minor / open / confirmed; issue key: cm004743-import-history-timestamp.

KOMODO history uses 2026-01-27T01:15:02.fZ; enrichment history is timezone-naive. Current corresponding writer bodies show the unsupported time.strftime fractional directive and naive datetime generation.

## Recommended Actions And Acceptance Checks

### A1

Reconcile source-specific stock and preparation representation in both maintained contributors, preserving DSMZ paragraph, source batch amounts, nominal provider values and unresolved final volume. Add narrow evidence and bibliography; document exact salt-form grounding as unresolved until a suitable identifier is verified.

- Account for all 33 local amount fields and all 16 retained source decisions; separate two percentage-stock strengths and receiving doses from direct ingredients.
- Retain the source post-sterilization sulfide stage without inventing stock strength/dose or autoclave time/temperature.
- Do not treat neutral CHEBI:8806 or a matching MIM synonym as proof of sodium-salt identity.
- Preserve actual preparation and current parent relationship; verify physical-state labeling before any enum change.
- Attach source-located evidence, then run schema, strict, term and reference validators for each edited owner.

### A2

After maintained inputs are reconciled, regenerate with the current formulation-aware merge path and verify that preparation/provenance survive or incompatible records remain separate.

- No direct patch of generated YAML; preserve all contributor scientific content.
- Run verify-merges and audit-merge-freshness plus applicable product gates after the separately authorized change.

### A3

Correct future timestamp generation in the maintained import/enrichment writers; retain historic entries and append an explanation if chronology is later curated.

- New timestamps use timezone-aware UTC without a literal fractional directive.
- Do not rewrite history or invent original timezone/fractional precision.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml; entire file | supports | Entire YAML read including all amounts, identifiers, source notes, relationships and history. |
| komodo-owner | data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml; entire file | supports | Entire YAML read including all amounts, identifiers, source notes, relationships and history. |
| dsmz-owner | data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml; entire file | supports | Entire YAML read including all amounts, identifiers, source notes, relationships and history. |
| dsm286 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium286.pdf; page1, complete table and preparation paragraph | supports | Official DSMZ 286 PDF, one page visually read and text cross-checked. It establishes supplied forms, batch amounts, stock strength/doses and preparation; it does not establish organism-specific growth. |
| api286 | https://mediadive.dsmz.de/rest/medium/286; complete captured response | supports | Entire medium 286 JSON read: medium identity/pH, one solution, all 12 recipe rows, volume 1001 and preparation/equipment. Distinguish provider g_l from explicit source batch amounts. |
| komodo-access | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=286; complete captured response | supports | Exact historical /komodo/servlet MediaInfo=286 route returned HTTP 403. The response records access failure only; current accession contents remain unverified. |
| pubchem-salt | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/112939/property/MolecularFormula,IUPACName/JSON; complete captured response | supports | Authoritative PubChem CID 112939 response identifies sodium resazurin with molecular formula C12H6NNaO4; this supports the counterion distinction only. |
| ols63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; _embedded.terms[0]: obo_id, label, is_obsolete, description, annotation | supports | Exact ChEBI ID/label, active status, supplied chemical form and formula inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount is inferred from ontology identity. |
| ols131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; _embedded.terms[0]: obo_id, label, is_obsolete, description, annotation | supports | Exact ChEBI ID/label, active status, supplied chemical form and formula inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount is inferred from ontology identity. |
| ols86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; _embedded.terms[0]: obo_id, label, is_obsolete, description, annotation | supports | Exact ChEBI ID/label, active status, supplied chemical form and formula inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount is inferred from ontology identity. |
| ols86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86254; _embedded.terms[0]: obo_id, label, is_obsolete, description, annotation | supports | Exact ChEBI ID/label, active status, supplied chemical form and formula inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount is inferred from ontology identity. |
| ols86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; _embedded.terms[0]: obo_id, label, is_obsolete, description, annotation | supports | Exact ChEBI ID/label, active status, supplied chemical form and formula inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount is inferred from ontology identity. |
| ols75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; _embedded.terms[0]: obo_id, label, is_obsolete, description, annotation | supports | Exact ChEBI ID/label, active status, supplied chemical form and formula inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount is inferred from ontology identity. |
| ols16865 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16865; _embedded.terms[0]: obo_id, label, is_obsolete, description, annotation | supports | Exact ChEBI ID/label, active status, supplied chemical form and formula inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount is inferred from ontology identity. |
| ols2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; _embedded.terms[0]: obo_id, label, is_obsolete, description, annotation | supports | Exact ChEBI ID/label, active status, supplied chemical form and formula inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount is inferred from ontology identity. |
| ols8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; _embedded.terms[0]: obo_id, label, is_obsolete, description, annotation | supports | Exact ChEBI ID/label, active status, supplied chemical form and formula inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount is inferred from ontology identity. |
| ols76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; _embedded.terms[0]: obo_id, label, is_obsolete, description, annotation | supports | Exact ChEBI ID/label, active status, supplied chemical form and formula inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount is inferred from ontology identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; entire file | supports | Exact 11 input-label resolutions and matching rows inspected. Sodium-resazurin synonym maps to neutral CHEBI:8806, so snapshot integrity is not exact-form scientific approval. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; entire file | supports | Pinned source commit, SHA 256,9077 rows and consumer contract retained. |
| importer | src/culturemech/import/mediadive_importer.py; entire file | supports | Current conversion, composition, percentage-stock detection and solution extraction read. Current percentage-stock branches preserve these two additions; stored direct-only rows must not be attributed to an unfixed percentage-stock parser. Remaining g/ml unit normalization still assumes per-liter basis. |
| resolver | src/culturemech/enrich/dsmz_resolver.py; entire file | supports | merge_composition copies ingredients, solutions, pH and type/state but omits preparation; resolve_recipe skips nonempty targets. This current behavior is consistent with lost KOMODO preparation, without proving historical execution inputs. |
| komodo-writer | src/culturemech/import/komodo_web_importer.py; entire file | supports | Actual _convert_to_culturemech calls time.strftime with %f and supplies placeholder composition; literal .fZ history is not a real fractional-second timestamp. |
| merger | src/culturemech/merge/merger.py; entire file | supports | Current merge_group and canonical selection read. Pair is rejected by current formulation equality. |
| formulation | src/culturemech/merge/formulation.py; entire file | supports | Entire current formulation projection and merge function read. Preparation/relationship/notes differences remain significant. |
| state-writer | src/culturemech/enrich/fix_unnamed_and_physical_state.py; entire file | supports | has_agar_ingredient and fix_file classify any detected agar as SOLID_AGAR without amount or phase testing. This is a live heuristic, not proof of historical cause or actual gel state. |
| registry | data/culturemech_id_registry.tsv; entire file | supports | Exact CM001383 and CM004743 rows resolve the maintained owners; parent and child IDs/path labels match their target records. |
| project-recipes | project.justfile; entire file | supports | Actual focused checks and limits inspected; ingredient chemistry term slots are not bound by the term-validation gate. |
| diagnostics | REVIEW_WORK/batch062/record10/diagnostics.json; entire file | supports | Every 33 local amount fields,57 asserted chemical-ID slots, registry links, exact MIM answers and in-memory current-merger rejection inventoried. |
| history1 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/clostridium_aminobutyricum_medium.yaml.md; entire file | supports | Complete exact-target/owner historical report read. October 5 rows are unreviewed leads; October 7 retains unresolved provider-volume and stock questions. Current source response hash matches the captured October 7 hash; no prior finding is silently closed. |
| history2 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml.md; entire file | supports | Complete exact-target/owner historical report read. October 5 rows are unreviewed leads; October 7 retains unresolved provider-volume and stock questions. Current source response hash matches the captured October 7 hash; no prior finding is silently closed. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.md; entire file | supports | Complete exact-target/owner historical report read. October 5 rows are unreviewed leads; October 7 retains unresolved provider-volume and stock questions. Current source response hash matches the captured October 7 hash; no prior finding is silently closed. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.md; entire file | supports | Complete exact-target/owner historical report read. October 5 rows are unreviewed leads; October 7 retains unresolved provider-volume and stock questions. Current source response hash matches the captured October 7 hash; no prior finding is silently closed. |
| history5 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.md; entire file | supports | Complete exact-target/owner historical report read. October 5 rows are unreviewed leads; October 7 retains unresolved provider-volume and stock questions. Current source response hash matches the captured October 7 hash; no prior finding is silently closed. |
| quantity-inventory | REVIEW_WORK/batch062/record10/quantity-inventory.json; entire file | supports | Sixteen decisions cover all 33 local concentration fields and every source-only quantity boundary. Quoted source text is separate from interpretation/arithmetic. |
| validate-schema | REVIEW_WORK/batch062/record10/validate-schema-result.json; entire file | supports | Complete actual result and streams read. |
| validate-strict | REVIEW_WORK/batch062/record10/validate-strict-result.json; entire file | supports | Complete actual result and streams read. |
| validate-terms | REVIEW_WORK/batch062/record10/validate-terms-result.json; entire file | supports | Complete actual result and streams read. |
| validate-references | REVIEW_WORK/batch062/record10/validate-references-result.json; entire file | supports | Complete actual result and streams read. |
| check-mim-label-index | REVIEW_WORK/batch062/record10/check-mim-label-index-result.json; entire file | supports | Complete actual result and streams read. |
| komodo-short-route-lead | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=286; complete captured response | supports | Initial shorter MediaInfo route without the historical /komodo prefix returned 403. It is retained as a failed discovery lead and does not verify the historical endpoint or accession contents. |

## Limits And Additional Notes

- Exact historical /komodo/servlet MediaInfo=286 route returned HTTP 403. Historical source mapping remains indirect evidence; current accession contents could not be fetched. Both earlier shorter/alternate KOMODO routes returned 403 and the obsolete MediaDive /api route returned 404; those failed leads are preserved. The correct MediaDive /rest response returned 200 and supports the scientific source assessment.
- Primary source does not establish final volume, sulfide stock strength/dose, autoclave temperature/time or experimentally observed medium phase. No unsupported conversion, growth condition or phase replacement is proposed.
- All 57 existing chemical slots were examined using 10 active ChEBI records. Incidental CHEBI:32145 capture is sodium hydroxide and is excluded from conclusions; no matching replacement sodium-resazurin ChEBI was verified.
- Original raw-import files are absent at the exact three documented diagnostic paths in this private checkout (lexists includes ignored paths); this does not establish absence elsewhere. Current-writer attribution is bounded to inspected functions, not asserted as reconstructed historical execution.
- Four native record checks apply to selected target; contributors are scientific context. Full-corpus gates and experimental growth validation were not run. No structured finding is retired, no record history is changed and no scientific status is promoted.
- All five exact historical reports were read; retained source objects were reconciled with fresh API bytes rather than counted as new coverage.
- Scientific records and generated products remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T095201Z-clostridium-aminobutyricum-batch062
kind: record
repository: CultureBotAI/CultureMech
title: 'Clostridium aminobutyricum medium: source stock boundaries and preparation
  retention'
started_at: '2026-10-28T09:27:38.194300Z'
finished_at: '2026-10-28T09:52:01.482683Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or edit target or maintained scientific
    records; source-grounded review without experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Three major findings concern omitted preparation, flattened stocks/unresolved
  volume basis and sodium-resazurin grounding; two minor findings concern evidence
  placement and history timestamps. All 33 quantity fields and 57 chemical-ID slots
  were assessed. Native checks pass, but fresh KOMODO accession access 403 prevents
  complete source verification.
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
  - path: data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml
    sha256: 0b36ef231bc6a4c91635cde2062ad666bb4d86e3ff5990da90f2c7a74f37e3e3
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml
    sha256: ac6e7668b8cb40732f58c885662cdf31714bca2f0120a6aef56e7579d779b8fb
    role: context
  - path: data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml
    sha256: 79ea6d0765c9b4154fc8964b64faf1cc7f72805dced50d3db202e91cf20f6eed
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml.md
    sha256: da53784d7bb77a59318110d50888b4fcac1077927e35ed040c30826477aeb75f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/clostridium_aminobutyricum_medium.yaml.md
    sha256: 2adc79c27d2a9e2a65aae13e74f692f5d3f3544451cfefd500a3b55369d30d9e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.md
    sha256: a43efe821e3b612dd333c1656c2950d3a0eda7551c4259c2491de96e999d072c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.md
    sha256: dfde8f4cb3eed51403ccc72b10a9d4391f50663cef4ea4febc57c41ae554f240
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.md
    sha256: 7c20777696846e4a185c94132a4cadfa6ad3349b160ffaa44184794b458adf05
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/enrich_with_kg_microbe_matches.py
    sha256: 61351f99ef2cb0cef03e74ad92d21dcf3b38df77a06602bdac814974e7728eeb
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
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
  - path: src/culturemech/enrich/fix_unnamed_and_physical_state.py
    sha256: 3b652deb9cfdf2e32ad2cdda4488f4c1582bce2e54ed1b0b8970f6f54543af7f
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
  description: One complete generated target, two maintained contributors and exact
    DSMZ 286 source formulation; all 16 quantity decisions retained.
  selection: Batch 062 item 10 in Python path order, selected after 543 of 6325 targets
    had coverage from successful native validated lists.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:004743
  exclusions:
  - target: Other recipes, organism-specific culture claims and experimental optimization
    reason: No other scientific target or tested strain is asserted in this review.
targets:
- target_id: CultureMech:004743
  path: data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml
  label: clostridium_aminobutyricum_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:004743
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch062/record10/strict.tsv
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:004743
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch062/record10/strict.tsv"
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:004743
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:004743
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  evidence_ids:
  - validate-references
- check_id: check-mim-label-index
  name: check-mim-label-index
  command: just check-mim-label-index
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:004743
  summary: 'MIM label index OK: 9,077 rows, 8,733 labels, commit 6643131b0f12ab40b66f98135245fca04027e0e9

    Decisions: ambiguous=23, hydrate_conflict=12, mapped=8,347, undecided=1, unmapped=350

    uv run python scripts/check_mim_label_index.py'
  evidence_ids:
  - check-mim-label-index
- check_id: history-reference-read
  name: Embedded history and internal reference review
  status: failed
  required: false
  target_ids:
  - CultureMech:004743
  summary: Parent/child IDs and paths resolve. KOMODO import history has literal .fZ
    and resolver history lacks timezone; no focused native history validator is claimed.
  evidence_ids:
  - target
  - komodo-owner
  - dsmz-owner
  - registry
  - komodo-writer
  - resolver
- check_id: corpus-gates
  name: Full-corpus ID/product/merge gates
  status: skipped
  required: false
  target_ids:
  - CultureMech:004743
  summary: No scientific records/schema/generators changed. Full-corpus assign-ids-check,
    validate-products, verify-merges and audit-merge-freshness were not run; in-memory
    pair rejection is only a scoped diagnostic.
  evidence_ids:
  - project-recipes
  - diagnostics
evidence:
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.050317Z'
  support: supports
  summary: Entire YAML read including all amounts, identifiers, source notes, relationships
    and history.
  snapshot_sha256: 0b36ef231bc6a4c91635cde2062ad666bb4d86e3ff5990da90f2c7a74f37e3e3
- evidence_id: komodo-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.050346Z'
  support: supports
  summary: Entire YAML read including all amounts, identifiers, source notes, relationships
    and history.
  snapshot_sha256: ac6e7668b8cb40732f58c885662cdf31714bca2f0120a6aef56e7579d779b8fb
- evidence_id: dsmz-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.050368Z'
  support: supports
  summary: Entire YAML read including all amounts, identifiers, source notes, relationships
    and history.
  snapshot_sha256: 79ea6d0765c9b4154fc8964b64faf1cc7f72805dced50d3db202e91cf20f6eed
- evidence_id: dsm286
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium286.pdf
  locator: page1, complete table and preparation paragraph
  accessed_at: '2026-10-28T09:28:01.030784Z'
  support: supports
  summary: Official DSMZ 286 PDF, one page visually read and text cross-checked. It
    establishes supplied forms, batch amounts, stock strength/doses and preparation;
    it does not establish organism-specific growth.
  snapshot_sha256: 38f59ab68af03bff5f0a198303520db10d206e511ec3b16f3d5b8b543d69bb5e
- evidence_id: api286
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/286
  locator: complete captured response
  accessed_at: '2026-10-28T09:28:00.685714Z'
  support: supports
  summary: 'Entire medium 286 JSON read: medium identity/pH, one solution, all 12
    recipe rows, volume 1001 and preparation/equipment. Distinguish provider g_l from
    explicit source batch amounts.'
  snapshot_sha256: d89986c8b26ae72127c98e4e2d2b260b6f4eb8d0a1cd654bd7d9c477c7b8c906
- evidence_id: komodo-access
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=286
  locator: complete captured response
  accessed_at: '2026-10-28T09:50:22.590077Z'
  support: supports
  summary: Exact historical /komodo/servlet MediaInfo=286 route returned HTTP 403.
    The response records access failure only; current accession contents remain unverified.
  snapshot_sha256: a0dda48617600ce655c540513fbb3f438af8a532955f021f0aa4dfcc82eab7b1
  search_scope: One request to the exact MediaInfo=286 endpoint linked in the retained
    historical KOMODO source-mapping row. No other accessions or catalog contents
    were searched.
- evidence_id: pubchem-salt
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/112939/property/MolecularFormula,IUPACName/JSON
  locator: complete captured response
  accessed_at: '2026-10-28T09:31:48.966643Z'
  support: supports
  summary: Authoritative PubChem CID 112939 response identifies sodium resazurin with
    molecular formula C12H6NNaO4; this supports the counterion distinction only.
  snapshot_sha256: 43b65dadad8580dff243fb7ae7827036a1a2a3610d5adb38f27c5eaf89f6dca9
- evidence_id: ols63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: '_embedded.terms[0]: obo_id, label, is_obsolete, description, annotation'
  accessed_at: '2026-10-28T09:28:00.892988Z'
  support: supports
  summary: Exact ChEBI ID/label, active status, supplied chemical form and formula
    inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount
    is inferred from ontology identity.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: ols131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: '_embedded.terms[0]: obo_id, label, is_obsolete, description, annotation'
  accessed_at: '2026-10-28T09:28:01.306890Z'
  support: supports
  summary: Exact ChEBI ID/label, active status, supplied chemical form and formula
    inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount
    is inferred from ontology identity.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: ols86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: '_embedded.terms[0]: obo_id, label, is_obsolete, description, annotation'
  accessed_at: '2026-10-28T09:28:01.508705Z'
  support: supports
  summary: Exact ChEBI ID/label, active status, supplied chemical form and formula
    inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount
    is inferred from ontology identity.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: ols86254
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86254
  locator: '_embedded.terms[0]: obo_id, label, is_obsolete, description, annotation'
  accessed_at: '2026-10-28T09:28:01.538906Z'
  support: supports
  summary: Exact ChEBI ID/label, active status, supplied chemical form and formula
    inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount
    is inferred from ontology identity.
  snapshot_sha256: 89afba545ad02f24a850933df154af25dee37357b583f82de13866b44f18d683
- evidence_id: ols86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: '_embedded.terms[0]: obo_id, label, is_obsolete, description, annotation'
  accessed_at: '2026-10-28T09:28:01.695776Z'
  support: supports
  summary: Exact ChEBI ID/label, active status, supplied chemical form and formula
    inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount
    is inferred from ontology identity.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: ols75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: '_embedded.terms[0]: obo_id, label, is_obsolete, description, annotation'
  accessed_at: '2026-10-28T09:28:01.925180Z'
  support: supports
  summary: Exact ChEBI ID/label, active status, supplied chemical form and formula
    inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount
    is inferred from ontology identity.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: ols16865
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16865
  locator: '_embedded.terms[0]: obo_id, label, is_obsolete, description, annotation'
  accessed_at: '2026-10-28T09:28:02.204325Z'
  support: supports
  summary: Exact ChEBI ID/label, active status, supplied chemical form and formula
    inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount
    is inferred from ontology identity.
  snapshot_sha256: dce8c48945eb48cc092a1941a266bbf4c41427d96b7064dac7cb0cb358f43a86
- evidence_id: ols2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: '_embedded.terms[0]: obo_id, label, is_obsolete, description, annotation'
  accessed_at: '2026-10-28T09:28:02.138194Z'
  support: supports
  summary: Exact ChEBI ID/label, active status, supplied chemical form and formula
    inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount
    is inferred from ontology identity.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: ols8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: '_embedded.terms[0]: obo_id, label, is_obsolete, description, annotation'
  accessed_at: '2026-10-28T09:28:02.317606Z'
  support: supports
  summary: Exact ChEBI ID/label, active status, supplied chemical form and formula
    inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount
    is inferred from ontology identity.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: ols76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: '_embedded.terms[0]: obo_id, label, is_obsolete, description, annotation'
  accessed_at: '2026-10-28T09:28:02.521448Z'
  support: supports
  summary: Exact ChEBI ID/label, active status, supplied chemical form and formula
    inspected. Neutral CHEBI:8806 does not represent the source sodium salt. No amount
    is inferred from ontology identity.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.053542Z'
  support: supports
  summary: Exact 11 input-label resolutions and matching rows inspected. Sodium-resazurin
    synonym maps to neutral CHEBI:8806, so snapshot integrity is not exact-form scientific
    approval.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.053834Z'
  support: supports
  summary: Pinned source commit, SHA 256,9077 rows and consumer contract retained.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.053853Z'
  support: supports
  summary: Current conversion, composition, percentage-stock detection and solution
    extraction read. Current percentage-stock branches preserve these two additions;
    stored direct-only rows must not be attributed to an unfixed percentage-stock
    parser. Remaining g/ml unit normalization still assumes per-liter basis.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.053882Z'
  support: supports
  summary: merge_composition copies ingredients, solutions, pH and type/state but
    omits preparation; resolve_recipe skips nonempty targets. This current behavior
    is consistent with lost KOMODO preparation, without proving historical execution
    inputs.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: komodo-writer
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.053903Z'
  support: supports
  summary: Actual _convert_to_culturemech calls time.strftime with %f and supplies
    placeholder composition; literal .fZ history is not a real fractional-second timestamp.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.053925Z'
  support: supports
  summary: Current merge_group and canonical selection read. Pair is rejected by current
    formulation equality.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.053945Z'
  support: supports
  summary: Entire current formulation projection and merge function read. Preparation/relationship/notes
    differences remain significant.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: state-writer
  kind: record_content
  reference: src/culturemech/enrich/fix_unnamed_and_physical_state.py
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.053962Z'
  support: supports
  summary: has_agar_ingredient and fix_file classify any detected agar as SOLID_AGAR
    without amount or phase testing. This is a live heuristic, not proof of historical
    cause or actual gel state.
  snapshot_sha256: 3b652deb9cfdf2e32ad2cdda4488f4c1582bce2e54ed1b0b8970f6f54543af7f
- evidence_id: registry
  kind: record_content
  reference: data/culturemech_id_registry.tsv
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.053981Z'
  support: supports
  summary: Exact CM001383 and CM004743 rows resolve the maintained owners; parent
    and child IDs/path labels match their target records.
  snapshot_sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
- evidence_id: project-recipes
  kind: record_content
  reference: project.justfile
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.054446Z'
  support: supports
  summary: Actual focused checks and limits inspected; ingredient chemistry term slots
    are not bound by the term-validation gate.
  snapshot_sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
- evidence_id: diagnostics
  kind: record_content
  reference: REVIEW_WORK/batch062/record10/diagnostics.json
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.054500Z'
  support: supports
  summary: Every 33 local amount fields,57 asserted chemical-ID slots, registry links,
    exact MIM answers and in-memory current-merger rejection inventoried.
  snapshot_sha256: bd72ef2df0fc4a9f44fc9c26a78bc7d48c62820f5072e8af2b86dcee7ce0f891
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/clostridium_aminobutyricum_medium.yaml.md
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.054724Z'
  support: supports
  summary: Complete exact-target/owner historical report read. October 5 rows are
    unreviewed leads; October 7 retains unresolved provider-volume and stock questions.
    Current source response hash matches the captured October 7 hash; no prior finding
    is silently closed.
  snapshot_sha256: 2adc79c27d2a9e2a65aae13e74f692f5d3f3544451cfefd500a3b55369d30d9e
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml.md
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.054753Z'
  support: supports
  summary: Complete exact-target/owner historical report read. October 5 rows are
    unreviewed leads; October 7 retains unresolved provider-volume and stock questions.
    Current source response hash matches the captured October 7 hash; no prior finding
    is silently closed.
  snapshot_sha256: da53784d7bb77a59318110d50888b4fcac1077927e35ed040c30826477aeb75f
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.md
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.054777Z'
  support: supports
  summary: Complete exact-target/owner historical report read. October 5 rows are
    unreviewed leads; October 7 retains unresolved provider-volume and stock questions.
    Current source response hash matches the captured October 7 hash; no prior finding
    is silently closed.
  snapshot_sha256: dfde8f4cb3eed51403ccc72b10a9d4391f50663cef4ea4febc57c41ae554f240
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.md
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.054796Z'
  support: supports
  summary: Complete exact-target/owner historical report read. October 5 rows are
    unreviewed leads; October 7 retains unresolved provider-volume and stock questions.
    Current source response hash matches the captured October 7 hash; no prior finding
    is silently closed.
  snapshot_sha256: 7c20777696846e4a185c94132a4cadfa6ad3349b160ffaa44184794b458adf05
- evidence_id: history5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.md
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.054815Z'
  support: supports
  summary: Complete exact-target/owner historical report read. October 5 rows are
    unreviewed leads; October 7 retains unresolved provider-volume and stock questions.
    Current source response hash matches the captured October 7 hash; no prior finding
    is silently closed.
  snapshot_sha256: a43efe821e3b612dd333c1656c2950d3a0eda7551c4259c2491de96e999d072c
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch062/record10/quantity-inventory.json
  locator: entire file
  accessed_at: '2026-10-28T09:52:01.479293Z'
  support: supports
  summary: Sixteen decisions cover all 33 local concentration fields and every source-only
    quantity boundary. Quoted source text is separate from interpretation/arithmetic.
  snapshot_sha256: c45d9a9edbe2b6744ad0bdda321c66a58b3b930f76389a7689f7f0b3f87cfe8b
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch062/record10/validate-schema-result.json
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.055644Z'
  support: supports
  summary: Complete actual result and streams read.
  snapshot_sha256: b144bb2d6f75dd573f9748c0ed671740038a611649f13c3db386abeba6f54a40
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch062/record10/validate-strict-result.json
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.055785Z'
  support: supports
  summary: Complete actual result and streams read.
  snapshot_sha256: d98702b7e5b21ccc568a2d5ce05af18cd2b09be5c41a7d475deb763ce00f44fc
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch062/record10/validate-terms-result.json
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.055902Z'
  support: supports
  summary: Complete actual result and streams read.
  snapshot_sha256: 4b8f04a588182614275bbce5f8b04f215f6f7f24cb4c38c59e39d03fa53147e9
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch062/record10/validate-references-result.json
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.056018Z'
  support: supports
  summary: Complete actual result and streams read.
  snapshot_sha256: c76244b32d46705f39b4fdb1f99acb20a473fb9582254b385a2d4ec22257ee8d
- evidence_id: check-mim-label-index
  kind: validation
  reference: REVIEW_WORK/batch062/record10/check-mim-label-index-result.json
  locator: entire file
  accessed_at: '2026-10-28T09:36:11.056143Z'
  support: supports
  summary: Complete actual result and streams read.
  snapshot_sha256: 1b2387d0cda58af2c8daf203a50d12e2f33d2dbfeb1368330be8b8c3d3790e0a
- evidence_id: komodo-short-route-lead
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=286
  locator: complete captured response
  accessed_at: '2026-10-28T09:31:48.513649Z'
  support: supports
  summary: Initial shorter MediaInfo route without the historical /komodo prefix returned
    403. It is retained as a failed discovery lead and does not verify the historical
    endpoint or accession contents.
  snapshot_sha256: 62f1cd18b4d5d95538a00510f22335c278a31ebe0694d8cc5dccdf6965a8e092
  search_scope: One request to the displayed shorter MediaInfo=286 URL; exact response
    bytes only. The historical /komodo/servlet endpoint was checked separately.
assessments:
- assessment_id: identity
  area: identity
  topic: DSMZ286 source identity and KOMODO duplicate relationship
  outcome: supported
  summary: Stable selected target and its two maintained owners resolve. DSMZ source
    name/pH/composition and historical KOMODO row support the intended source identity;
    fresh KOMODO access 403 limits current accession verification.
  target_ids:
  - CultureMech:004743
  evidence_ids:
  - target
  - komodo-owner
  - dsmz-owner
  - registry
  - dsm286
  - api286
  - history2
  - komodo-access
  details: Ingredient signatures match, but not all scientific/provenance content
    does. This is one unambiguous target; two contributor records are context, not
    separate reviewed targets.
- assessment_id: amounts
  area: quantity
  topic: Every existing amount and source-only dose boundary
  outcome: concern
  summary: All 33 local amounts match provider g_l, but the provider volume and primary-source
    water/addition basis conflict. Two explicit percentage stocks and post-sterilization
    sulfide delivery are flattened.
  target_ids:
  - CultureMech:004743
  evidence_ids:
  - quantity-inventory
  - dsm286
  - api286
  details: "{\n  \"created_at\": \"2026-10-28T09:36:11.055156Z\",\n  \"target\": \"\
    data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml\",\n  \"scope\"\
    : \"All 33 concentration fields across selected target and two maintained contributors,\
    \ plus solvent, two stock strengths, unquantified sulfide dosing and provider\
    \ volume.\",\n  \"decisions\": [\n    {\n      \"decision_id\": \"Q01\",\n   \
    \   \"ingredient\": \"KH2PO4\",\n      \"decision\": \"unsupported\",\n      \"\
    fields\": [\n        {\n          \"path\": \"data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[0].concentration\",\n          \"value\"\
    : {\n            \"value\": \"1.3\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml\"\
    ,\n          \"field\": \"ingredients[0].concentration\",\n          \"value\"\
    : {\n            \"value\": \"1.3\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml\"\
    ,\n          \"field\": \"ingredients[0].concentration\",\n          \"value\"\
    : {\n            \"value\": \"1.3\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        }\n      ],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[0]; DSMZ PDF p1 corresponding\
    \ row\",\n      \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 1,\\n                        \\\"compound\\\": \\\"KH2PO4\\\",\\n          \
    \              \\\"compound_id\\\": 11,\\n                        \\\"amount\\\
    \": 1.3,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 1.3,\\n                        \\\"mmol_l\\\": 9.55285,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \  \"explanation\": \"Exact source mass and provider g_l are retained; the source\
    \ specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata\
    \ does not establish an actual final volume. No rescaling to 1001 ml or 1001.5\
    \ ml is endorsed.\",\n      \"calculation\": \"1.3 g is directly reported for\
    \ the batch. Provider g_l=1.3; division by its volume 1.001 L would yield 1.298701299\
    \ g/L, an inconsistency diagnostic only.\",\n      \"proposed\": \"No replacement\
    \ final-medium concentration asserted.\"\n    },\n    {\n      \"decision_id\"\
    : \"Q02\",\n      \"ingredient\": \"K2HPO4\",\n      \"decision\": \"unsupported\"\
    ,\n      \"fields\": [\n        {\n          \"path\": \"data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[1].concentration\",\n          \"value\"\
    : {\n            \"value\": \"7\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml\"\
    ,\n          \"field\": \"ingredients[1].concentration\",\n          \"value\"\
    : {\n            \"value\": \"7\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml\"\
    ,\n          \"field\": \"ingredients[1].concentration\",\n          \"value\"\
    : {\n            \"value\": \"7\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        }\n      ],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[1]; DSMZ PDF p1 corresponding\
    \ row\",\n      \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 2,\\n                        \\\"compound\\\": \\\"K2HPO4\\\",\\n          \
    \              \\\"compound_id\\\": 10,\\n                        \\\"amount\\\
    \": 7,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 7,\\n                        \\\"mmol_l\\\": 40.1892,\\n\
    \                        \\\"optional\\\": 0\\n                    }\",\n    \
    \  \"explanation\": \"Exact source mass and provider g_l are retained; the source\
    \ specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata\
    \ does not establish an actual final volume. No rescaling to 1001 ml or 1001.5\
    \ ml is endorsed.\",\n      \"calculation\": \"7 g is directly reported for the\
    \ batch. Provider g_l=7; division by its volume 1.001 L would yield 6.993006993\
    \ g/L, an inconsistency diagnostic only.\",\n      \"proposed\": \"No replacement\
    \ final-medium concentration asserted.\"\n    },\n    {\n      \"decision_id\"\
    : \"Q03\",\n      \"ingredient\": \"MgCl2 x 6 H2O\",\n      \"decision\": \"unsupported\"\
    ,\n      \"fields\": [\n        {\n          \"path\": \"data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[2].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.2\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml\"\
    ,\n          \"field\": \"ingredients[2].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.2\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml\"\
    ,\n          \"field\": \"ingredients[2].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.2\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        }\n      ],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[2]; DSMZ PDF p1 corresponding\
    \ row\",\n      \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 3,\\n                        \\\"compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n   \
    \                     \\\"compound_id\\\": 79,\\n                        \\\"\
    amount\\\": 0.2,\\n                        \\\"unit\\\": \\\"g\\\",\\n       \
    \                 \\\"g_l\\\": 0.2,\\n                        \\\"mmol_l\\\":\
    \ 0.983753,\\n                        \\\"optional\\\": 0\\n                 \
    \   }\",\n      \"explanation\": \"Exact source mass and provider g_l are retained;\
    \ the source specifies 1000 ml water plus additions, while API volume is 1001\
    \ ml. That metadata does not establish an actual final volume. No rescaling to\
    \ 1001 ml or 1001.5 ml is endorsed.\",\n      \"calculation\": \"0.2 g is directly\
    \ reported for the batch. Provider g_l=0.2; division by its volume 1.001 L would\
    \ yield 0.1998001998 g/L, an inconsistency diagnostic only.\",\n      \"proposed\"\
    : \"No replacement final-medium concentration asserted.\"\n    },\n    {\n   \
    \   \"decision_id\": \"Q04\",\n      \"ingredient\": \"FeCl3 x 6 H2O\",\n    \
    \  \"decision\": \"unsupported\",\n      \"fields\": [\n        {\n          \"\
    path\": \"data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml\",\n \
    \         \"field\": \"ingredients[3].concentration\",\n          \"value\": {\n\
    \            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\n       \
    \   }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml\"\
    ,\n          \"field\": \"ingredients[3].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\n   \
    \       }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml\"\
    ,\n          \"field\": \"ingredients[3].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\n   \
    \       }\n        }\n      ],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[3]; DSMZ PDF p1 corresponding\
    \ row\",\n      \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 4,\\n                        \\\"compound\\\": \\\"FeCl3 x 6 H2O\\\",\\n   \
    \                     \\\"compound_id\\\": 82,\\n                        \\\"\
    amount\\\": 0.01,\\n                        \\\"unit\\\": \\\"g\\\",\\n      \
    \                  \\\"g_l\\\": 0.01,\\n                        \\\"mmol_l\\\"\
    : 0.0369965,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n      \"explanation\": \"Exact source mass and provider g_l are retained;\
    \ the source specifies 1000 ml water plus additions, while API volume is 1001\
    \ ml. That metadata does not establish an actual final volume. No rescaling to\
    \ 1001 ml or 1001.5 ml is endorsed.\",\n      \"calculation\": \"0.01 g is directly\
    \ reported for the batch. Provider g_l=0.01; division by its volume 1.001 L would\
    \ yield 0.00999000999 g/L, an inconsistency diagnostic only.\",\n      \"proposed\"\
    : \"No replacement final-medium concentration asserted.\"\n    },\n    {\n   \
    \   \"decision_id\": \"Q05\",\n      \"ingredient\": \"CaCl2 x 2 H2O\",\n    \
    \  \"decision\": \"unsupported\",\n      \"fields\": [\n        {\n          \"\
    path\": \"data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml\",\n \
    \         \"field\": \"ingredients[4].concentration\",\n          \"value\": {\n\
    \            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\n       \
    \   }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml\"\
    ,\n          \"field\": \"ingredients[4].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\n   \
    \       }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml\"\
    ,\n          \"field\": \"ingredients[4].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\n   \
    \       }\n        }\n      ],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[4]; DSMZ PDF p1 corresponding\
    \ row\",\n      \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 5,\\n                        \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n   \
    \                     \\\"compound_id\\\": 7,\\n                        \\\"amount\\\
    \": 0.01,\\n                        \\\"unit\\\": \\\"g\\\",\\n              \
    \          \\\"g_l\\\": 0.01,\\n                        \\\"mmol_l\\\": 0.0680203,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \  \"explanation\": \"Exact source mass and provider g_l are retained; the source\
    \ specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata\
    \ does not establish an actual final volume. No rescaling to 1001 ml or 1001.5\
    \ ml is endorsed.\",\n      \"calculation\": \"0.01 g is directly reported for\
    \ the batch. Provider g_l=0.01; division by its volume 1.001 L would yield 0.00999000999\
    \ g/L, an inconsistency diagnostic only.\",\n      \"proposed\": \"No replacement\
    \ final-medium concentration asserted.\"\n    },\n    {\n      \"decision_id\"\
    : \"Q06\",\n      \"ingredient\": \"Na2MoO4 x 2 H2O\",\n      \"decision\": \"\
    conflict\",\n      \"fields\": [\n        {\n          \"path\": \"data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[5].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.001\",\n            \"unit\": \"G_PER_L\"\n  \
    \        }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml\"\
    ,\n          \"field\": \"ingredients[5].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.001\",\n            \"unit\": \"G_PER_L\"\n  \
    \        }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml\"\
    ,\n          \"field\": \"ingredients[5].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.001\",\n            \"unit\": \"G_PER_L\"\n  \
    \        }\n        }\n      ],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[5]; DSMZ PDF p1 corresponding\
    \ row\",\n      \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 6,\\n                        \\\"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n \
    \                       \\\"compound_id\\\": 9,\\n                        \\\"\
    attribute\\\": \\\"0.1% w/v\\\",\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"g_l\\\": 0.001,\\n                        \\\"mmol_l\\\": 0.00413309,\\n   \
    \                     \\\"optional\\\": 0\\n                    }\",\n      \"\
    explanation\": \"Source is a measured dose of 0.1% w/v stock; direct g/L representation\
    \ loses stock composition and addition stage. Provider g_l equals the added mass\
    \ per nominal liter, but final volume is not explicitly made up. Preserve both\
    \ stock and receiving-dose identities.\",\n      \"calculation\": \"0.1 g/100\
    \ ml =1 mg/ml; 1 ml supplies 1 mg. Dividing by an assumed 1 L reproduces 0.001\
    \ g/L; the final-volume assumption is not established.\",\n      \"proposed\"\
    : \"No replacement final-medium concentration asserted.\"\n    },\n    {\n   \
    \   \"decision_id\": \"Q07\",\n      \"ingredient\": \"Yeast extract\",\n    \
    \  \"decision\": \"unsupported\",\n      \"fields\": [\n        {\n          \"\
    path\": \"data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml\",\n \
    \         \"field\": \"ingredients[6].concentration\",\n          \"value\": {\n\
    \            \"value\": \"3\",\n            \"unit\": \"G_PER_L\"\n          }\n\
    \        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml\"\
    ,\n          \"field\": \"ingredients[6].concentration\",\n          \"value\"\
    : {\n            \"value\": \"3\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml\"\
    ,\n          \"field\": \"ingredients[6].concentration\",\n          \"value\"\
    : {\n            \"value\": \"3\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        }\n      ],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[6]; DSMZ PDF p1 corresponding\
    \ row\",\n      \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 7,\\n                        \\\"compound\\\": \\\"Yeast extract\\\",\\n   \
    \                     \\\"compound_id\\\": 16,\\n                        \\\"\
    amount\\\": 3,\\n                        \\\"unit\\\": \\\"g\\\",\\n         \
    \               \\\"g_l\\\": 3,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n      \"explanation\": \"Exact source mass and provider\
    \ g_l are retained; the source specifies 1000 ml water plus additions, while API\
    \ volume is 1001 ml. That metadata does not establish an actual final volume.\
    \ No rescaling to 1001 ml or 1001.5 ml is endorsed.\",\n      \"calculation\"\
    : \"3 g is directly reported for the batch. Provider g_l=3; division by its volume\
    \ 1.001 L would yield 2.997002997 g/L, an inconsistency diagnostic only.\",\n\
    \      \"proposed\": \"No replacement final-medium concentration asserted.\"\n\
    \    },\n    {\n      \"decision_id\": \"Q08\",\n      \"ingredient\": \"gamma-Aminobutyric\
    \ acid\",\n      \"decision\": \"unsupported\",\n      \"fields\": [\n       \
    \ {\n          \"path\": \"data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[7].concentration\",\n          \"value\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml\"\
    ,\n          \"field\": \"ingredients[7].concentration\",\n          \"value\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml\"\
    ,\n          \"field\": \"ingredients[7].concentration\",\n          \"value\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        }\n      ],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[7]; DSMZ PDF p1 corresponding\
    \ row\",\n      \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 8,\\n                        \\\"compound\\\": \\\"gamma-Aminobutyric acid\\\
    \",\\n                        \\\"compound_id\\\": 355,\\n                   \
    \     \\\"amount\\\": 5,\\n                        \\\"unit\\\": \\\"g\\\",\\\
    n                        \\\"g_l\\\": 5,\\n                        \\\"mmol_l\\\
    \": 48.4872,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n      \"explanation\": \"Exact source mass and provider g_l are retained;\
    \ the source specifies 1000 ml water plus additions, while API volume is 1001\
    \ ml. That metadata does not establish an actual final volume. No rescaling to\
    \ 1001 ml or 1001.5 ml is endorsed.\",\n      \"calculation\": \"5 g is directly\
    \ reported for the batch. Provider g_l=5; division by its volume 1.001 L would\
    \ yield 4.995004995 g/L, an inconsistency diagnostic only.\",\n      \"proposed\"\
    : \"No replacement final-medium concentration asserted.\"\n    },\n    {\n   \
    \   \"decision_id\": \"Q09\",\n      \"ingredient\": \"Agar\",\n      \"decision\"\
    : \"unsupported\",\n      \"fields\": [\n        {\n          \"path\": \"data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[8].concentration\",\n          \"value\"\
    : {\n            \"value\": \"1.5\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml\"\
    ,\n          \"field\": \"ingredients[8].concentration\",\n          \"value\"\
    : {\n            \"value\": \"1.5\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml\"\
    ,\n          \"field\": \"ingredients[8].concentration\",\n          \"value\"\
    : {\n            \"value\": \"1.5\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        }\n      ],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[8]; DSMZ PDF p1 corresponding\
    \ row\",\n      \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 9,\\n                        \\\"compound\\\": \\\"Agar\\\",\\n            \
    \            \\\"compound_id\\\": 3,\\n                        \\\"amount\\\"\
    : 1.5,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 1.5,\\n                        \\\"mmol_l\\\": 4.45991,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \  \"explanation\": \"Exact source mass and provider g_l are retained; the source\
    \ specifies 1000 ml water plus additions, while API volume is 1001 ml. That metadata\
    \ does not establish an actual final volume. No rescaling to 1001 ml or 1001.5\
    \ ml is endorsed.\",\n      \"calculation\": \"1.5 g is directly reported for\
    \ the batch. Provider g_l=1.5; division by its volume 1.001 L would yield 1.498501499\
    \ g/L, an inconsistency diagnostic only.\",\n      \"proposed\": \"No replacement\
    \ final-medium concentration asserted.\"\n    },\n    {\n      \"decision_id\"\
    : \"Q10\",\n      \"ingredient\": \"Sodium resazurin\",\n      \"decision\": \"\
    conflict\",\n      \"fields\": [\n        {\n          \"path\": \"data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[9].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.0005\",\n            \"unit\": \"G_PER_L\"\n \
    \         }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml\"\
    ,\n          \"field\": \"ingredients[9].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.0005\",\n            \"unit\": \"G_PER_L\"\n \
    \         }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml\"\
    ,\n          \"field\": \"ingredients[9].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.0005\",\n            \"unit\": \"G_PER_L\"\n \
    \         }\n        }\n      ],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[9]; DSMZ PDF p1 corresponding\
    \ row\",\n      \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 10,\\n                        \\\"compound\\\": \\\"Sodium resazurin\\\",\\\
    n                        \\\"compound_id\\\": 1852,\\n                       \
    \ \\\"attribute\\\": \\\"0.1% w/v\\\",\\n                        \\\"amount\\\"\
    : 0.5,\\n                        \\\"unit\\\": \\\"ml\\\",\\n                \
    \        \\\"g_l\\\": 0.0005,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n      \"explanation\": \"Source is a measured dose\
    \ of 0.1% w/v stock; direct g/L representation loses stock composition and addition\
    \ stage. Provider g_l equals the added mass per nominal liter, but final volume\
    \ is not explicitly made up. Preserve both stock and receiving-dose identities.\"\
    ,\n      \"calculation\": \"0.1 g/100 ml =1 mg/ml; 0.5 ml supplies 0.5 mg. Dividing\
    \ by an assumed 1 L reproduces 0.0005 g/L; the final-volume assumption is not\
    \ established.\",\n      \"proposed\": \"No replacement final-medium concentration\
    \ asserted.\"\n    },\n    {\n      \"decision_id\": \"Q11\",\n      \"ingredient\"\
    : \"Na2S x 9 H2O\",\n      \"decision\": \"conflict\",\n      \"fields\": [\n\
    \        {\n          \"path\": \"data/merge_yaml/merged/CLOSTRIDIUM_AMINOBUTYRICUM_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[10].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.3\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml\"\
    ,\n          \"field\": \"ingredients[10].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.3\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml\"\
    ,\n          \"field\": \"ingredients[10].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.3\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        }\n      ],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[10]; DSMZ PDF p1 corresponding\
    \ row\",\n      \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 11,\\n                        \\\"compound\\\": \\\"Na2S x 9 H2O\\\",\\n   \
    \                     \\\"compound_id\\\": 54,\\n                        \\\"\
    amount\\\": 0.3,\\n                        \\\"unit\\\": \\\"g\\\",\\n       \
    \                 \\\"g_l\\\": 0.3,\\n                        \\\"mmol_l\\\":\
    \ 1.24905,\\n                        \\\"optional\\\": 0\\n                  \
    \  }\",\n      \"explanation\": \"Exact source mass and provider g_l are retained;\
    \ the source specifies 1000 ml water plus additions, while API volume is 1001\
    \ ml. That metadata does not establish an actual final volume. No rescaling to\
    \ 1001 ml or 1001.5 ml is endorsed. Source separately requires post-sterilization\
    \ delivery from sterile anoxic sulfide stock; its strength and dose are unspecified.\"\
    ,\n      \"calculation\": \"0.3 g is directly reported for the batch. Provider\
    \ g_l=0.3; division by its volume 1.001 L would yield 0.2997002997 g/L, an inconsistency\
    \ diagnostic only.\",\n      \"proposed\": \"No replacement final-medium concentration\
    \ asserted.\"\n    },\n    {\n      \"decision_id\": \"Q12\",\n      \"ingredient\"\
    : \"Distilled water\",\n      \"decision\": \"evidence_only\",\n      \"fields\"\
    : [],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\",\n \
    \     \"locator\": \"$.data.solutions[0].recipe[11]; PDF p1 water row\",\n   \
    \   \"snippet\": \"{\\n                        \\\"recipe_order\\\": 12,\\n  \
    \                      \\\"compound\\\": \\\"Distilled water\\\",\\n         \
    \               \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n      \"explanation\"\
    : \"The solvent batch amount is 1000 ml, not an explicit instruction to make the\
    \ completed medium to a final volume. Omission as a nutrient edge alone is not\
    \ a defect.\",\n      \"calculation\": \"No final-volume conversion is certified.\"\
    ,\n      \"proposed\": \"No replacement final-medium concentration asserted.\"\
    \n    },\n    {\n      \"decision_id\": \"Q13\",\n      \"ingredient\": \"Na2MoO4\
    \ x 2 H2O stock strength\",\n      \"decision\": \"evidence_only\",\n      \"\
    fields\": [],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[5].attribute\",\n      \"snippet\"\
    : \"\\\"attribute\\\": \\\"0.1% w/v\\\"\",\n      \"explanation\": \"Exact source\
    \ stock strength; keep distinct from its receiving volume and final-medium concentration.\"\
    ,\n      \"calculation\": \"0.1 g per 100 ml stock =1 g/L stock; no density is\
    \ assumed.\",\n      \"proposed\": \"No replacement final-medium concentration\
    \ asserted.\"\n    },\n    {\n      \"decision_id\": \"Q14\",\n      \"ingredient\"\
    : \"Sodium resazurin stock strength\",\n      \"decision\": \"evidence_only\"\
    ,\n      \"fields\": [],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].recipe[9].attribute\",\n      \"snippet\"\
    : \"\\\"attribute\\\": \\\"0.1% w/v\\\"\",\n      \"explanation\": \"Exact source\
    \ stock strength; keep distinct from its receiving volume and final-medium concentration.\"\
    ,\n      \"calculation\": \"0.1 g per 100 ml stock =1 g/L stock; no density is\
    \ assumed.\",\n      \"proposed\": \"No replacement final-medium concentration\
    \ asserted.\"\n    },\n    {\n      \"decision_id\": \"Q15\",\n      \"ingredient\"\
    : \"Sulfide stock strength and dose\",\n      \"decision\": \"not_quantified\"\
    ,\n      \"fields\": [],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].steps[0].step\",\n      \"snippet\"\
    : \"After sterilization add sulfide from a sterile anoxic stock solution prepared\
    \ under 100% N2 gas atmosphere.\",\n      \"explanation\": \"Source requires a\
    \ separate addition stage but supplies no stock concentration or dispensing volume.\
    \ Neither is inferred from the total sulfide mass.\",\n      \"calculation\":\
    \ \"No final-volume conversion is certified.\",\n      \"proposed\": \"No replacement\
    \ final-medium concentration asserted.\"\n    },\n    {\n      \"decision_id\"\
    : \"Q16\",\n      \"ingredient\": \"Provider solution volume\",\n      \"decision\"\
    : \"conflict\",\n      \"fields\": [],\n      \"reference\": \"https://mediadive.dsmz.de/rest/medium/286\"\
    ,\n      \"locator\": \"$.data.solutions[0].volume\",\n      \"snippet\": \"\\\
    \"volume\\\": 1001\",\n      \"explanation\": \"Provider volume 1001 ml conflicts\
    \ with a naive sum 1000 + 1 + 0.5 ml, and neither number proves final volume after\
    \ dissolved solids and sulfide stock. Preserve the disagreement and nominal basis.\"\
    ,\n      \"calculation\": \"1000 + 1 + 0.5=1001.5 ml is only a source-input sum,\
    \ not a validated final volume.\",\n      \"proposed\": \"No replacement final-medium\
    \ concentration asserted.\"\n    }\n  ],\n  \"local_concentration_field_count\"\
    : 33,\n  \"decision_count\": 16,\n  \"conditions\": {\n    \"preparation_ph\"\
    : 7.2,\n    \"atmosphere\": \"100%N2 in source preparation, not a growth-rate\
    \ assertion\",\n    \"sterilization\": \"autoclave; no temperature/time asserted\
    \ by this source\",\n    \"physical_state\": \"Agar1.5g per1000ml-water batch;\
    \ SOLID_AGAR remains unverified as a phase assignment. SEMISOLID is not substituted\
    \ by assumption.\",\n    \"growth\": \"No strain, incubation temperature or experimental\
    \ growth assertion in target/source.\"\n  }\n}"
- assessment_id: preparation
  area: completeness
  topic: Retained DSMZ preparation versus generated omission
  outcome: concern
  summary: The DSMZ owner retains the complete source paragraph under AUTOCLAVE. The
    KOMODO owner and merged record omit it; their parent path resolves to that content,
    which is credited. The stored merge is not lossless, and the current merger rejects
    the pair.
  target_ids:
  - CultureMech:004743
  evidence_ids:
  - target
  - komodo-owner
  - dsmz-owner
  - dsm286
  - resolver
  - merger
  - formulation
  - diagnostics
  details: Source supports preparation pH 7.2, anaerobic handling and post-sterilization
    addition. No time/temperature is invented. Complex/undefined bacterial classification
    is consistent with yeast extract; solid-agar phase remains unverified rather than
    automatically changed to semisolid.
- assessment_id: grounding
  area: grounding
  topic: Exact forms, IDs and MIM coverage
  outcome: concern
  summary: Ten asserted ChEBI IDs resolve and labels match;57 primary/MIM slots across
    three documents were inspected. Nine exact-form chemical identities are supported,
    but sodium resazurin maps to neutral resazurin. The MIM snapshot repeats that
    synonym mismatch.
  target_ids:
  - CultureMech:004743
  evidence_ids:
  - dsm286
  - api286
  - pubchem-salt
  - mim
  - mim-meta
  - diagnostics
  - check-mim-label-index
  - ols63036
  - ols131527
  - ols86345
  - ols86254
  - ols86158
  - ols75213
  - ols16865
  - ols2509
  - ols8806
  - ols76209
  details: Selected record:10/11 primary ChEBI labels and 9/11 dedicated MIM CHEBI
    links;11/11 resolver answers include FOODON for yeast extract. These are linkage
    counts only. Yeast-extract FOODON is a diagnostic resolver result, not a new externally
    validated assignment. No replacement ChEBI for the sodium salt is invented.
- assessment_id: provenance
  area: evidence
  topic: Source evidence placement and historical reports
  outcome: concern
  summary: No formulation evidence/reference entries are attached to these three YAMLs;
    native reference validation checks zero. Five exact historical reports were fully
    read, including all 14 source/formulation objects in each October 7 report. Current
    API hash equals the historical source hash.
  target_ids:
  - CultureMech:004743
  evidence_ids:
  - target
  - komodo-owner
  - dsmz-owner
  - validate-references
  - api286
  - history1
  - history2
  - history3
  - history4
  - history5
  details: Historical rows preserve unresolved questions; no previous structured issue
    is resolved or retired. Fresh exact KOMODO access is unavailable; source identity
    is supported indirectly by retained historical row and current DSMZ content.
- assessment_id: history
  area: provenance
  topic: Timestamp fidelity
  outcome: concern
  summary: Literal .fZ is invalid fractional-second history; timezone-naive enrichment
    timestamp is ambiguous. Current KOMODO writer uses time.strftime(%f), and resolver
    uses datetime.now().isoformat() without timezone.
  target_ids:
  - CultureMech:004743
  evidence_ids:
  - target
  - komodo-owner
  - komodo-writer
  - resolver
  details: Preserve earlier events append-only; any separately authorized correction
    should explain the historic ambiguity rather than fabricate an exact time.
- assessment_id: native
  area: schema
  topic: Required checks and source-review scope
  outcome: supported
  summary: Four canonical record checks and MIM integrity pass. Chemical scientific
    correspondence and source recipe support were checked separately.
  target_ids:
  - CultureMech:004743
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
  - check-mim-label-index
  details: No explicit target organism, gene, locus, protein or transcriptomic claim
    is asserted. iModulonDB is not applicable; no negative literature claim or new
    growth assertion is made.
findings:
- finding_id: F1
  issue_key: cm004743-preparation-omission-in-merged-record
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Stored merged record drops source preparation retained by its DSMZ owner
  description: Generated and KOMODO records lack the source preparation paragraph.
    DSMZ owner and reachable parent record retain it, including anoxic handling and
    deferred sulfide addition. Current resolver copying omits preparation; current
    merger correctly rejects unequal full content, so the historical generated record
    needs source reconciliation and regeneration.
  target_ids:
  - CultureMech:004743
  field_paths:
  - preparation_steps
  - sterilization
  - merged_from
  evidence_ids:
  - target
  - komodo-owner
  - dsmz-owner
  - dsm286
  - resolver
  - merger
  - formulation
  - diagnostics
  rule_id: P3.4
  native_severity: P3
  normalization_reason: Raised to major because loss of source handling/staging materially
    changes record usability; reachable parent content is explicitly credited.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
- finding_id: F2
  issue_key: cm004743-stock-topology-and-volume-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock additions are flattened onto an unresolved final-volume basis
  description: Molybdate and sodium-resazurin stocks are represented only as direct
    mass concentrations; sulfide stock staging is absent in selected target. API g_l
    agrees with stored values but conflicts with API 1001 ml volume, while PDF gives
    1000 ml water plus additions without final makeup. These are unresolved source/basis
    issues, not a license to divide everything by 1001 or 1001.5 ml.
  target_ids:
  - CultureMech:004743
  field_paths:
  - ingredients[*].concentration
  - solutions
  - preparation_steps
  evidence_ids:
  - quantity-inventory
  - dsm286
  - api286
  - importer
  rule_id: P2.3
  native_severity: P2
  normalization_reason: Material stock/final-medium representation conflict; preserve
    API nominal values and explicit source amounts without asserting a fabricated
    replacement.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml
    role: maintained normalized contributor
- finding_id: F3
  issue_key: cm004743-sodium-resazurin-neutral-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium resazurin is grounded to the neutral parent
  description: The source names sodium resazurin. CHEBI:8806 is the neutral C12H7NO4
    parent, whereas authoritative sodium-salt identity has C12H6NNaO4. The exact MIM
    synonym lookup repeats the neutral mapping and cannot independently validate supplied
    chemical form.
  target_ids:
  - CultureMech:004743
  field_paths:
  - ingredients[9].term
  evidence_ids:
  - target
  - dsm286
  - api286
  - ols8806
  - pubchem-salt
  - mim
  - diagnostics
  rule_id: exact-supplied-form
  native_severity: P2
  normalization_reason: Existing ID resolves, so this is a form mismatch rather than
    P 2.2 nonexistent-ID failure.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml
    role: maintained normalized contributor
- finding_id: F4
  issue_key: cm004743-formulation-evidence-placement
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Recoverable sources lack claim-level formulation evidence
  description: Source identity can be recovered through DSMZ parent notes and historical
    mapping, but no structured formulation evidence or bibliography is attached. Reference
    validation therefore checks zero objects.
  target_ids:
  - CultureMech:004743
  field_paths:
  - ingredients[*].evidence
  - evidence
  - references
  evidence_ids:
  - target
  - komodo-owner
  - dsmz-owner
  - validate-references
  - dsm286
  - api286
  rule_id: P4.3
  native_severity: P4
  normalization_reason: Minor traceability gap; missing optional evidence is not presented
    as a schema failure.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml
    role: maintained normalized contributor
- finding_id: F5
  issue_key: cm004743-import-history-timestamp
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Import history contains malformed or timezone-ambiguous timestamps
  description: KOMODO history uses 2026-01-27T01:15:02.fZ; enrichment history is timezone-naive.
    Current corresponding writer bodies show the unsupported time.strftime fractional
    directive and naive datetime generation.
  target_ids:
  - CultureMech:004743
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  evidence_ids:
  - target
  - komodo-owner
  - komodo-writer
  - resolver
  rule_id: history-timestamp-fidelity
  native_severity: P3
  normalization_reason: Non-blocking provenance fidelity issue; native schema checks
    pass and no historic time is guessed.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: A1
  description: Reconcile source-specific stock and preparation representation in both
    maintained contributors, preserving DSMZ paragraph, source batch amounts, nominal
    provider values and unresolved final volume. Add narrow evidence and bibliography;
    document exact salt-form grounding as unresolved until a suitable identifier is
    verified.
  finding_ids:
  - F1
  - F2
  - F3
  - F4
  target_ids:
  - CultureMech:004743
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Account for all 33 local amount fields and all 16 retained source decisions; separate
    two percentage-stock strengths and receiving doses from direct ingredients.
  - Retain the source post-sterilization sulfide stage without inventing stock strength/dose
    or autoclave time/temperature.
  - Do not treat neutral CHEBI:8806 or a matching MIM synonym as proof of sodium-salt
    identity.
  - Preserve actual preparation and current parent relationship; verify physical-state
    labeling before any enum change.
  - Attach source-located evidence, then run schema, strict, term and reference validators
    for each edited owner.
- action_id: A2
  description: After maintained inputs are reconciled, regenerate with the current
    formulation-aware merge path and verify that preparation/provenance survive or
    incompatible records remain separate.
  finding_ids:
  - F1
  target_ids:
  - CultureMech:004743
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
  depends_on:
  - A1
  generator: python -m culturemech.merge.merge_recipes
  acceptance_checks:
  - No direct patch of generated YAML; preserve all contributor scientific content.
  - Run verify-merges and audit-merge-freshness plus applicable product gates after
    the separately authorized change.
- action_id: A3
  description: Correct future timestamp generation in the maintained import/enrichment
    writers; retain historic entries and append an explanation if chronology is later
    curated.
  finding_ids:
  - F5
  target_ids:
  - CultureMech:004743
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: timestamp writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: timestamp writer
  acceptance_checks:
  - New timestamps use timezone-aware UTC without a literal fractional directive.
  - Do not rewrite history or invent original timezone/fractional precision.
limitations:
- Exact historical /komodo/servlet MediaInfo=286 route returned HTTP 403. Historical
  source mapping remains indirect evidence; current accession contents could not be
  fetched. Both earlier shorter/alternate KOMODO routes returned 403 and the obsolete
  MediaDive /api route returned 404; those failed leads are preserved. The correct
  MediaDive /rest response returned 200 and supports the scientific source assessment.
- Primary source does not establish final volume, sulfide stock strength/dose, autoclave
  temperature/time or experimentally observed medium phase. No unsupported conversion,
  growth condition or phase replacement is proposed.
- All 57 existing chemical slots were examined using 10 active ChEBI records. Incidental
  CHEBI:32145 capture is sodium hydroxide and is excluded from conclusions; no matching
  replacement sodium-resazurin ChEBI was verified.
- Original raw-import files are absent at the exact three documented diagnostic paths
  in this private checkout (lexists includes ignored paths); this does not establish
  absence elsewhere. Current-writer attribution is bounded to inspected functions,
  not asserted as reconstructed historical execution.
- Four native record checks apply to selected target; contributors are scientific
  context. Full-corpus gates and experimental growth validation were not run. No structured
  finding is retired, no record history is changed and no scientific status is promoted.
notes:
- All five exact historical reports were read; retained source objects were reconciled
  with fresh API bytes rather than counted as new coverage.
- Scientific records and generated products remain unchanged.
tags:
- review-only
- batch062
- source-boundaries
- quantity-inventory
```
