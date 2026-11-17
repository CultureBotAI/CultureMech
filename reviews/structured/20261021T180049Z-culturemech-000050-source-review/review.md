# Source and formulation review: asw (CultureMech:000050)

- Review: 20261021T180049Z-culturemech-000050-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T17:54:28Z
- Finished UTC: 2026-10-21T18:00:49Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

ASW is identifiable as the exact CCAP medium, but both local layers flatten salt and vitamin stock strengths into final-medium ingredients and omit stock doses and soil extract. The nitrate row is grounded to Azimilide. The maintained algae owner has already restored three preparation instructions; the generated target remains stale. General light and temperature recommendations lack record-specific evidence. Source stereochemical limits and the natural-seawater/artificial-salt alternative remain explicit.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 317; batch 032 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-one task batches contain 310 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 313 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000050 | data/merge_yaml/merged/ASW.yaml | generated | asw |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000050 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000050 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-032/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch032/317/strict.tsv |
| validate-terms | passed | True | CultureMech:000050 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000050 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000050 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: ccapSE1 | unavailable | False | CultureMech:000050 | An older SE1 candidate URL returned 404; the official current recipe index resolves a separately captured successful SE1 PDF. This failed attempt does not leave the required soil-stock source unavailable. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000050.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary chemical identifiers

grounding: concern. Targets: CultureMech:000050.

12 distinct primary/current-secondary IDs resolve to nonobsolete terms; exact stored/canonical labels are recorded separately in each term evidence item. Target direct-ingredient linkage is 12/13 primary (92.31%) and 0/13 current CHEBI-based secondary (0.00%), on a 0–100 linkage scale, not an accuracy score. Current secondary keys without pinned index rows: []. Legacy slot count 0 is separate and does not enter that current-key claim. Supplied-form correspondence is assessed separately.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:000050.

21 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact source and single maintained owner

identity: supported. Targets: CultureMech:000050.

CCAP:ASW and the exact MR_ASW PDF identify Artificial Seawater. The unique stable-ID owner is algae/asw.yaml, not its bacterial namesake. The source is the current CCAP adaptation, not proof of identity to every historical version or to ASWP.

### Chemical identity and source specificity

grounding: concern. Targets: CultureMech:000050.

NaNO3 is sodium nitrate, whereas CHEBI:34545 is Azimilide with an unrelated organic formula. The two phosphate salts, biotin, cyanocobalamin, folic acid, nicotinic acid, thiamine hydrochloride, thymine and tricine agree at the named source level. Source calcium pantothenate does not state stereochemistry, while CHEBI:31345 encodes it; source Inositol does not establish the myo configuration of CHEBI:17268. These last two are specificity limits, not proof of alternate isomers. All primary labels resolve, and both layers assert zero secondary MIM links.

### Classification, use and preparation scope

scope: concern. Targets: CultureMech:000050.

Complex/undefined liquid medium is reasonable for seawater and soil extract. The primary supports a marine-algae medium, not the numeric growth temperature or light recommendations. No strain-level growth or optimum follows from the title. The soil extraction temperatures and resting periods belong only to SE1.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:000050.

35 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "label": "NaNO3 stock strength",
    "decision": "correct",
    "source_stage": "Extra-salt stock 1",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "15.00",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "15.00",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Stock-table heading",
        "exact_source_quote": "Stocks         per litre",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      },
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Extra-salt stock 1 exact ingredient row",
        "exact_source_quote": "NaNO3       15.00 g",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing numeric strength matches the stock recipe per litre, but is falsely positioned as a direct medium ingredient. Retain the original stock amount and unit, then represent its separate 7.50 ml per litre dose. Do not treat the full stock recipe as a final-medium quantity."
  },
  {
    "decision_id": "q2",
    "label": "Na2HPO4 stock strength",
    "decision": "correct",
    "source_stage": "Extra-salt stock 1",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.60",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.60",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Stock-table heading",
        "exact_source_quote": "Stocks         per litre",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      },
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Extra-salt stock 1 exact ingredient row",
        "exact_source_quote": "Na2HPO4      0.60 g",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing numeric strength matches the stock recipe per litre, but is falsely positioned as a direct medium ingredient. Retain the original stock amount and unit, then represent its separate 7.50 ml per litre dose. Do not treat the full stock recipe as a final-medium quantity."
  },
  {
    "decision_id": "q3",
    "label": "K2HPO4 stock strength",
    "decision": "correct",
    "source_stage": "Extra-salt stock 1",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.50",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.50",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Stock-table heading",
        "exact_source_quote": "Stocks         per litre",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      },
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Extra-salt stock 1 exact ingredient row",
        "exact_source_quote": "K2HPO4      0.50 g",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing numeric strength matches the stock recipe per litre, but is falsely positioned as a direct medium ingredient. Retain the original stock amount and unit, then represent its separate 7.50 ml per litre dose. Do not treat the full stock recipe as a final-medium quantity."
  },
  {
    "decision_id": "q4",
    "label": "Biotin stock strength",
    "decision": "correct",
    "source_stage": "Vitamin stock 2",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.0002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.0002",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Stock-table heading",
        "exact_source_quote": "Stocks         per litre",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      },
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Vitamin stock 2 exact ingredient row",
        "exact_source_quote": "Biotin       0.0002 g",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing numeric strength matches the stock recipe per litre, but is falsely positioned as a direct medium ingredient. Retain the original stock amount and unit, then represent its separate 2.50 ml per litre dose. Do not treat the full stock recipe as a final-medium quantity."
  },
  {
    "decision_id": "q5",
    "label": "Calcium pantothenate stock strength",
    "decision": "correct",
    "source_stage": "Vitamin stock 2",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Stock-table heading",
        "exact_source_quote": "Stocks         per litre",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      },
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Vitamin stock 2 exact ingredient row",
        "exact_source_quote": "Calcium pantothenate    0.02 g",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing numeric strength matches the stock recipe per litre, but is falsely positioned as a direct medium ingredient. Retain the original stock amount and unit, then represent its separate 2.50 ml per litre dose. Do not treat the full stock recipe as a final-medium quantity."
  },
  {
    "decision_id": "q6",
    "label": "Cyanocobalamin stock strength",
    "decision": "correct",
    "source_stage": "Vitamin stock 2",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Stock-table heading",
        "exact_source_quote": "Stocks         per litre",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      },
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Vitamin stock 2 exact ingredient row",
        "exact_source_quote": "Cyanocobalamin     0.004 g",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing numeric strength matches the stock recipe per litre, but is falsely positioned as a direct medium ingredient. Retain the original stock amount and unit, then represent its separate 2.50 ml per litre dose. Do not treat the full stock recipe as a final-medium quantity."
  },
  {
    "decision_id": "q7",
    "label": "Folic acid stock strength",
    "decision": "correct",
    "source_stage": "Vitamin stock 2",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Stock-table heading",
        "exact_source_quote": "Stocks         per litre",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      },
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Vitamin stock 2 exact ingredient row",
        "exact_source_quote": "Folic acid      0.0004 g",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing numeric strength matches the stock recipe per litre, but is falsely positioned as a direct medium ingredient. Retain the original stock amount and unit, then represent its separate 2.50 ml per litre dose. Do not treat the full stock recipe as a final-medium quantity."
  },
  {
    "decision_id": "q8",
    "label": "Inositol stock strength",
    "decision": "correct",
    "source_stage": "Vitamin stock 2",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Stock-table heading",
        "exact_source_quote": "Stocks         per litre",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      },
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Vitamin stock 2 exact ingredient row",
        "exact_source_quote": "Inositol      1.0 g",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing numeric strength matches the stock recipe per litre, but is falsely positioned as a direct medium ingredient. Retain the original stock amount and unit, then represent its separate 2.50 ml per litre dose. Do not treat the full stock recipe as a final-medium quantity."
  },
  {
    "decision_id": "q9",
    "label": "Nicotinic acid stock strength",
    "decision": "correct",
    "source_stage": "Vitamin stock 2",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Stock-table heading",
        "exact_source_quote": "Stocks         per litre",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      },
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Vitamin stock 2 exact ingredient row",
        "exact_source_quote": "Nicotinic acid      0.02 g",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing numeric strength matches the stock recipe per litre, but is falsely positioned as a direct medium ingredient. Retain the original stock amount and unit, then represent its separate 2.50 ml per litre dose. Do not treat the full stock recipe as a final-medium quantity."
  },
  {
    "decision_id": "q10",
    "label": "Thiamine HCl stock strength",
    "decision": "correct",
    "source_stage": "Vitamin stock 2",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Stock-table heading",
        "exact_source_quote": "Stocks         per litre",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      },
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Vitamin stock 2 exact ingredient row",
        "exact_source_quote": "Thiamine HCl      0.1 g",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing numeric strength matches the stock recipe per litre, but is falsely positioned as a direct medium ingredient. Retain the original stock amount and unit, then represent its separate 2.50 ml per litre dose. Do not treat the full stock recipe as a final-medium quantity."
  },
  {
    "decision_id": "q11",
    "label": "Thymine stock strength",
    "decision": "correct",
    "source_stage": "Vitamin stock 2",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Stock-table heading",
        "exact_source_quote": "Stocks         per litre",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      },
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Vitamin stock 2 exact ingredient row",
        "exact_source_quote": "Thymine      0.6 g",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing numeric strength matches the stock recipe per litre, but is falsely positioned as a direct medium ingredient. Retain the original stock amount and unit, then represent its separate 2.50 ml per litre dose. Do not treat the full stock recipe as a final-medium quantity."
  },
  {
    "decision_id": "q12",
    "label": "Tricine main-medium quantity",
    "decision": "evidence_only",
    "source_stage": "Final medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.50",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.50",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Main-medium heading",
        "exact_source_quote": "Medium         per litre",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      },
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Main-medium tricine row",
        "exact_source_quote": "Tricine       0.50 g",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing 0.50 g/L matches the final-medium table; no claim-level amount evidence is attached in either layer."
  },
  {
    "decision_id": "q13",
    "label": "Extra-salt stock dose",
    "decision": "add",
    "source_stage": "Final-medium stock 1 addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Medium per litre, Extra-salt stock dose",
        "exact_source_quote": "Stock solution 1       7.50 ml",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "Restore this explicit stock addition and its distinct composition/provenance. The stock recipe denominator is separate from the receiving medium denominator."
  },
  {
    "decision_id": "q14",
    "label": "Vitamin stock dose",
    "decision": "add",
    "source_stage": "Final-medium stock 2 addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Medium per litre, Vitamin stock dose",
        "exact_source_quote": "Stock solution 2      2.50 ml",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "Restore this explicit stock addition and its distinct composition/provenance. The stock recipe denominator is separate from the receiving medium denominator."
  },
  {
    "decision_id": "q15",
    "label": "SE1 dose",
    "decision": "add",
    "source_stage": "Final-medium soil-extract addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Medium per litre, SE1 dose",
        "exact_source_quote": "Stock solution 3 (SE1)     25.00 ml",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "Restore this explicit stock addition and its distinct composition/provenance. The stock recipe denominator is separate from the receiving medium denominator."
  },
  {
    "decision_id": "q16",
    "label": "Target instruction masquerading as an ingredient",
    "decision": "correct",
    "source_stage": "Final volume",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[12].preferred_term",
        "stored": "Make up to"
      },
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Final-medium make-up sentence",
        "exact_source_quote": "Make up to 1 Litre with filtered natural seawater.* Adjust pH 7.6 – 7.8 to with 1M NaOH or 1M",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The value 1 L is a final make-up instruction, not a reagent or a standalone water addition. The maintained owner already removed this row."
  },
  {
    "decision_id": "q17",
    "label": "Owner final make-up instruction",
    "decision": "evidence_only",
    "source_stage": "Final volume",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "MIX",
          "description": "Bring to 1 L with filtered natural seawater."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Final-medium make-up sentence",
        "exact_source_quote": "Make up to 1 Litre with filtered natural seawater.* Adjust pH 7.6 – 7.8 to with 1M NaOH or 1M",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The maintained owner correctly specifies final volume 1 L using filtered natural seawater; attach the literal source. This is not adding 1 L after the stock aliquots."
  },
  {
    "decision_id": "q18",
    "label": "Target missing pH and titrant strength",
    "decision": "add",
    "source_stage": "Main-medium pH adjustment",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Final-medium pH and titrant sentence",
        "exact_source_quote": "Make up to 1 Litre with filtered natural seawater.* Adjust pH 7.6 – 7.8 to with 1M NaOH or 1M \nHCl, prior to autoclaving. Autoclave at 15 psi for 15 minutes.",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "Restore pH 7.6–7.8 and the alternative 1 M NaOH or 1 M HCl titrants; volumes are not quantified. These are preparation values, not measured growth optima."
  },
  {
    "decision_id": "q19",
    "label": "Owner pH and titrant strength",
    "decision": "evidence_only",
    "source_stage": "Main-medium pH adjustment",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "preparation_steps[1]",
        "stored": {
          "step_number": 2,
          "action": "ADJUST_PH",
          "description": "Adjust pH to 7.6-7.8 with 1 M NaOH or 1 M HCl before autoclaving."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Final-medium pH and titrant sentence",
        "exact_source_quote": "Make up to 1 Litre with filtered natural seawater.* Adjust pH 7.6 – 7.8 to with 1M NaOH or 1M \nHCl, prior to autoclaving. Autoclave at 15 psi for 15 minutes.",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The existing instruction retains pH 7.6–7.8 and both 1 M titrants correctly, without attached evidence."
  },
  {
    "decision_id": "q20",
    "label": "Titrant volumes",
    "decision": "not_quantified",
    "source_stage": "Main-medium titration",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Main-medium pH sentence",
        "exact_source_quote": "Make up to 1 Litre with filtered natural seawater.* Adjust pH 7.6 – 7.8 to with 1M NaOH or 1M \nHCl, prior to autoclaving. Autoclave at 15 psi for 15 minutes.",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "Neither titrant addition volume is supplied; do not infer a dose from its 1 M stock strength."
  },
  {
    "decision_id": "q21",
    "label": "Target sterilization",
    "decision": "add",
    "source_stage": "Main-medium sterilization",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Main-medium sterilization sentence",
        "exact_source_quote": "HCl, prior to autoclaving. Autoclave at 15 psi for 15 minutes.",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "Restore 15 psi for 15 minutes. The exact main page does not specify temperature or gauge/absolute pressure basis."
  },
  {
    "decision_id": "q22",
    "label": "Owner sterilization",
    "decision": "evidence_only",
    "source_stage": "Main-medium sterilization",
    "local_fields": [
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "preparation_steps[2]",
        "stored": {
          "step_number": 3,
          "action": "AUTOCLAVE",
          "description": "Autoclave at 15 psi for 15 minutes."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Main-medium sterilization sentence",
        "exact_source_quote": "HCl, prior to autoclaving. Autoclave at 15 psi for 15 minutes.",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The maintained owner correctly preserves 15 psi and 15 minutes. Attach source evidence without importing a temperature from the soil stock."
  },
  {
    "decision_id": "q23",
    "label": "Alternative artificial-seawater branch",
    "decision": "add",
    "source_stage": "Alternative final-medium branch",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Footnoted alternative make-up",
        "exact_source_quote": "*Alternatively, use deionised water to 1 litre and 33.6 g “Instant Ocean” sea salts.",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "Preserve the explicitly alternative deionized-water make-up to 1 litre with 33.6 g Instant Ocean. This is not an additional salt dose in the natural-seawater branch; no commercial constituent breakdown is inferred."
  },
  {
    "decision_id": "q24",
    "label": "Unsupported temperature_range",
    "decision": "unsupported",
    "source_stage": "Unsupported growth conditions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "temperature_range",
        "stored": "15-30°C depending on species"
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "temperature_range",
        "stored": "15-30°C depending on species"
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Source identity; entire exact page checked for growth conditions",
        "exact_source_quote": "ASW (Artificial Seawater)",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The current primary contains no corresponding growth condition. The current importer writes general defaults; this is context, not historical authentication or experimental evidence. Remove or qualify these ungrounded numeric recommendations rather than derive conditions from SE1 processing."
  },
  {
    "decision_id": "q25",
    "label": "Unsupported light_intensity",
    "decision": "unsupported",
    "source_stage": "Unsupported growth conditions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "light_intensity",
        "stored": "Varies by species; typically 50-100 µmol photons m⁻² s⁻¹"
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "light_intensity",
        "stored": "Varies by species; typically 50-100 µmol photons m⁻² s⁻¹"
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Source identity; entire exact page checked for growth conditions",
        "exact_source_quote": "ASW (Artificial Seawater)",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The current primary contains no corresponding growth condition. The current importer writes general defaults; this is context, not historical authentication or experimental evidence. Remove or qualify these ungrounded numeric recommendations rather than derive conditions from SE1 processing."
  },
  {
    "decision_id": "q26",
    "label": "Unsupported light_cycle",
    "decision": "unsupported",
    "source_stage": "Unsupported growth conditions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ASW.yaml",
        "field_path": "light_cycle",
        "stored": "Varies by species; commonly 12:12 or 16:8 light:dark"
      },
      {
        "input": "data/normalized_yaml/algae/asw.yaml",
        "field_path": "light_cycle",
        "stored": "Varies by species; commonly 12:12 or 16:8 light:dark"
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapASW",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf",
        "source_locator": "Source identity; entire exact page checked for growth conditions",
        "exact_source_quote": "ASW (Artificial Seawater)",
        "snapshot_sha256": "381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6",
        "parsed_text_sha256": "dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721"
      }
    ],
    "interpretation": "The current primary contains no corresponding growth condition. The current importer writes general defaults; this is context, not historical authentication or experimental evidence. Remove or qualify these ungrounded numeric recommendations rather than derive conditions from SE1 processing."
  },
  {
    "decision_id": "q27",
    "label": "SE1 Initial sieve",
    "decision": "add",
    "source_stage": "SE1 preparation",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "ccapSE1current",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf",
        "source_locator": "SE1 Initial sieve sentence",
        "exact_source_quote": "should be removed during an initial sieving through a 1 cm mesh. The sieved soil should be",
        "snapshot_sha256": "a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934",
        "parsed_text_sha256": "3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661"
      }
    ],
    "interpretation": "Retain the 1 cm mesh only for preparing soil. This applies only to the referenced SE1 stock."
  },
  {
    "decision_id": "q28",
    "label": "SE1 Optional oven drying",
    "decision": "add",
    "source_stage": "SE1 preparation",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "ccapSE1current",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf",
        "source_locator": "SE1 Optional oven drying sentence",
        "exact_source_quote": "spread to air dry or placed in a drying oven at around 50°C. When dry, the soil is sieved again",
        "snapshot_sha256": "a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934",
        "parsed_text_sha256": "3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661"
      }
    ],
    "interpretation": "Around 50°C applies to drying soil, not cultivation. This applies only to the referenced SE1 stock."
  },
  {
    "decision_id": "q29",
    "label": "SE1 Second sieve",
    "decision": "add",
    "source_stage": "SE1 preparation",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "ccapSE1current",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf",
        "source_locator": "SE1 Second sieve sentence",
        "exact_source_quote": "through a finer mesh (2-4 mm) and stored in an airtight container away from light and heat.",
        "snapshot_sha256": "a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934",
        "parsed_text_sha256": "3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661"
      }
    ],
    "interpretation": "Retain the 2–4 mm sieve only for dry soil. This applies only to the referenced SE1 stock."
  },
  {
    "decision_id": "q30",
    "label": "SE1 Soil-to-water volume ratio",
    "decision": "add",
    "source_stage": "SE1 preparation",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "ccapSE1current",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf",
        "source_locator": "SE1 Soil-to-water volume ratio sentence",
        "exact_source_quote": "Soil is prepared as above. Dried soil and twice its volume of supernatant d eionised water are",
        "snapshot_sha256": "a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934",
        "parsed_text_sha256": "3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661"
      }
    ],
    "interpretation": "Twice the soil volume of water is a volume ratio, not an asserted soil g/L concentration. This applies only to the referenced SE1 stock."
  },
  {
    "decision_id": "q31",
    "label": "SE1 First soil cycle",
    "decision": "add",
    "source_stage": "SE1 preparation",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "ccapSE1current",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf",
        "source_locator": "SE1 First soil cycle sentence",
        "exact_source_quote": "autoclaved together at 15 psi and 126°C for 20 minutes. After the mixture has cooled, it is then",
        "snapshot_sha256": "a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934",
        "parsed_text_sha256": "3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661"
      }
    ],
    "interpretation": "Retain the exact printed 15 psi, 126°C and 20 minutes. This applies only to the referenced SE1 stock."
  },
  {
    "decision_id": "q32",
    "label": "SE1 Second soil cycle",
    "decision": "add",
    "source_stage": "SE1 preparation",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "ccapSE1current",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf",
        "source_locator": "SE1 Second soil cycle sentence",
        "exact_source_quote": "autoclaved for a second time at 15 psi and 126°C for 20 minutes. After the mixture has cooled,",
        "snapshot_sha256": "a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934",
        "parsed_text_sha256": "3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661"
      }
    ],
    "interpretation": "Preserve the second 15 psi, 126°C, 20-minute cycle after cooling. This applies only to the referenced SE1 stock."
  },
  {
    "decision_id": "q33",
    "label": "SE1 Soil settling",
    "decision": "add",
    "source_stage": "SE1 preparation",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "ccapSE1current",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf",
        "source_locator": "SE1 Soil settling sentence",
        "exact_source_quote": "the bottle is sealed with parafilm and left undisturbed on a shelf for around two to three weeks",
        "snapshot_sha256": "a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934",
        "parsed_text_sha256": "3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661"
      }
    ],
    "interpretation": "Around two to three weeks is stock settling, not incubation. This applies only to the referenced SE1 stock."
  },
  {
    "decision_id": "q34",
    "label": "SE1 Final extract sterilization",
    "decision": "add",
    "source_stage": "SE1 preparation",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "ccapSE1current",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf",
        "source_locator": "SE1 Final extract sterilization sentence",
        "exact_source_quote": "After decanting, the final soil extract is autoclaved for a third time at 15 psi and 121 °C for 15 \nminutes. After the soil extract has cooled, the bottle is sealed with parafilm and stored in the",
        "snapshot_sha256": "a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934",
        "parsed_text_sha256": "3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661"
      }
    ],
    "interpretation": "Preserve the third cycle at 15 psi and 121°C for 15 minutes; do not silently reconcile pressure/temperature typography. This applies only to the referenced SE1 stock."
  },
  {
    "decision_id": "q35",
    "label": "SE1 unspecified soil strength and refrigeration temperature",
    "decision": "not_quantified",
    "source_stage": "SE1 stock limits",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "ccapSE1current",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf",
        "source_locator": "SE1 soil/water sentence",
        "exact_source_quote": "Soil is prepared as above. Dried soil and twice its volume of supernatant d eionised water are",
        "snapshot_sha256": "a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934",
        "parsed_text_sha256": "3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661"
      },
      {
        "source_key": "ccapSE1current",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf",
        "source_locator": "SE1 storage sentence",
        "exact_source_quote": "fridge.",
        "snapshot_sha256": "a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934",
        "parsed_text_sha256": "3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661"
      }
    ],
    "interpretation": "No soil mass per litre or numerical refrigeration temperature is given. Keep qualitative woodland-loam selection, cooling, aseptic decanting and refrigerated storage."
  }
]

## Findings

### f1: Stock strengths are flattened and their medium doses are missing

blocker / open / confirmed; issue key: cm000050-stocks.

The first eleven ingredient values are stock-table strengths, not final-medium concentrations. Neither layer represents the separate 7.50 ml salt stock, 2.50 ml vitamin stock and 25 ml SE1 doses per litre.

### f2: Sodium nitrate is linked to the unrelated drug Azimilide

major / open / confirmed; issue key: cm000050-nitrate.

The source explicitly prints NaNO3. Local NaNO is linked to CHEBI:34545, whose canonical identity and structure are Azimilide; canonical label validation does not detect this source mismatch.

### f3: Generated instructions are stale and the alternative formulation is missing

major / open / confirmed; issue key: cm000050-preparation.

The target retains Make up to as an ingredient and no preparation, while the maintained owner has correct make-up, pH and sterilization instructions. Both omit the explicit deionized-water/33.6 g Instant Ocean alternative and the scoped soil-extract process.

### f4: Generic light and temperature values lack recipe-specific support

major / open / confirmed; issue key: cm000050-growth-defaults.

Both layers assert 50–100 light intensity, 12:12 or 16:8 light cycles and 15–30°C. The exact primary does not supply these values; current importer defaults are not growth evidence.

### f5: Two stereochemical selections exceed the printed source

major / open / confirmed; issue key: cm000050-specificity.

The source says calcium pantothenate and inositol. Existing CHEBI:31345 and myo-inositol encode specificity not established by those source words. This does not prove a different stereoisomer was used.

### f6: Curation confidence is not claim-level scientific evidence

minor / open / confirmed; issue key: cm000050-provenance.

Source references and LLM confidence values do not attach exact stock-stage amount evidence. Several historical timestamps lack timezone information; the current PDF revision postdates the original import.

## Recommended Actions And Acceptance Checks

### a1

Restore stock composition, dose and final-medium relationships in the maintained owner; preserve SE1 as a source-scoped constituent and regenerate only through the authorized workflow.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Correct the name and chemical identity using separately verified sodium-nitrate grounding; do not invent a replacement identifier in this review.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Keep the owner’s valid instructions, add narrow evidence and missing source branches/stocks, then address generated staleness without editing the target directly.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Remove or explicitly qualify unsupported recommendations; require actual source evidence for any retained organism-specific condition.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Seek exact product or source-form evidence, or qualify the unresolved specificity without asserting a guessed alternative.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Attach exact versioned source claims and preserve historical events, adding timezone/provenance clarification only when supported.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ASW.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/algae/asw.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ASW.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ASW.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch032/317/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-032/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch032/317/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ASW.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ASW.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ASW.yaml:1:id: CultureMech:000050<br>./data/normalized_yaml/algae/asw.yaml:1:id: CultureMech:000050<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch032/source-preflight-bound/317/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 18 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf; Complete one-page revision 002, stock and final-medium tables and preparation | supports | Exact ASW primary visually inspected; salt and vitamin tables are stocks per litre, with distinct medium doses. |
| soil | https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf; Complete SE1 recipe, preparing soil and Medium sections | supports | The currently indexed SE1 recipe supplies the referenced stock process; these conditions are not main-medium growth conditions. |
| soil-index | https://www.ccap.ac.uk/index.php/media-recipes/; Official recipe list links ASW and SE1 | supports | Exact official index resolves the moved soil-extract PDF; an obsolete candidate URL returned 404. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Stored labels: ['dipotassium hydrogen phosphate']. Exact label correspondence is separate from source chemical-form support. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:15940 resolves to nicotinic acid. Stored labels: ['nicotinic acid']. Exact label correspondence is separate from source chemical-form support. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:15956 resolves to biotin. Stored labels: ['biotin']. Exact label correspondence is separate from source chemical-form support. |
| chebi17268 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17268; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:17268 resolves to myo-inositol. Stored labels: ['myo-inositol']. Exact label correspondence is separate from source chemical-form support. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:17439 resolves to cyanocob(III)alamin. Stored labels: ['cyanocob(III)alamin']. Exact label correspondence is separate from source chemical-form support. |
| chebi17821 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17821; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:17821 resolves to thymine. Stored labels: ['thymine']. Exact label correspondence is separate from source chemical-form support. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:27470 resolves to folic acid. Stored labels: ['folic acid']. Exact label correspondence is separate from source chemical-form support. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:31345 resolves to Calcium pantothenate. Stored labels: ['Calcium pantothenate']. Exact label correspondence is separate from source chemical-form support. |
| chebi34545 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34545; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:34545 resolves to Azimilide. Stored labels: ['Azimilide']. Exact label correspondence is separate from source chemical-form support. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Stored labels: ['disodium hydrogenphosphate']. Exact label correspondence is separate from source chemical-form support. |
| chebi46760 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46760; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:46760 resolves to tricine. Stored labels: ['tricine']. Exact label correspondence is separate from source chemical-form support. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:49105 resolves to thiamine hydrochloride. Stored labels: ['thiamine hydrochloride']. Exact label correspondence is separate from source chemical-form support. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned index exact identifier lookup; adjacent snapshot metadata | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows": {}, "missing_current_keys": []} |
| history-metadata | data/merge_yaml/merged/ASW.yaml; data/normalized_yaml/algae/asw.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": [{"index": 2, "issue": "timezone absent", "value": "2026-02-03T11:26:43.465115"}, {"index": 5, "issue": "timezone absent", "value": "2026-04-04T12:54:54.898350"}]}, {"input": "data/normalized_yaml/algae/asw.yaml", "events": 11, "timestamp_issues": [{"index": 2, "issue": "timezone absent", "value": "2026-02-03T11:26:43.465115"}, {"index": 5, "issue": "timezone absent", "value": "2026-04-04T12:54:54.898350"}]}] |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current exact CCAP import, instruction repair, source normalization and merge context inspected. The repair explicitly excludes stock-strength remediation; current functions do not prove historical causation. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current exact CCAP import, instruction repair, source normalization and merge context inspected. The repair explicitly excludes stock-strength remediation; current functions do not prove historical causation. |
| writer-2 | scripts/repair_ccap_instruction_rows.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current exact CCAP import, instruction repair, source normalization and merge context inspected. The repair explicitly excludes stock-strength remediation; current functions do not prove historical causation. |
| writer-3 | scripts/repair_ccap_sources_score10.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current exact CCAP import, instruction repair, source normalization and merge context inspected. The repair explicitly excludes stock-strength remediation; current functions do not prove historical causation. |
| writer-4 | src/culturemech/import/ccap_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current exact CCAP import, instruction repair, source normalization and merge context inspected. The repair explicitly excludes stock-strength remediation; current functions do not prove historical causation. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch032/317/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| ccapSE1-attempt | https://www.ccap.ac.uk/wp-content/uploads/MR_SE1.pdf; Preserved exact public retrieval result | context_only | An older SE1 candidate URL returned 404; the official current recipe index resolves a separately captured successful SE1 PDF. This failed attempt does not leave the required soil-stock source unavailable. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- An older SE1 candidate URL returned 404; the official current recipe index resolves a separately captured successful SE1 PDF. This failed attempt does not leave the required soil-stock source unavailable.
- The current CCAP adaptation is assessed as captured. Historical PDF byte equivalence, unspecified titrant volumes, pressure basis and source-unspecified stereochemistry are not inferred; the referenced 1957 paper is not used to authenticate the current CCAP adaptation.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T180049Z-culturemech-000050-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: asw (CultureMech:000050)'
started_at: '2026-10-21T17:54:28Z'
finished_at: '2026-10-21T18:00:49Z'
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
summary: ASW is identifiable as the exact CCAP medium, but both local layers flatten
  salt and vitamin stock strengths into final-medium ingredients and omit stock doses
  and soil extract. The nitrate row is grounded to Azimilide. The maintained algae
  owner has already restored three preparation instructions; the generated target
  remains stale. General light and temperature recommendations lack record-specific
  evidence. Source stereochemical limits and the natural-seawater/artificial-salt
  alternative remain explicit.
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
  - path: data/merge_yaml/merged/ASW.yaml
    sha256: 2c380b758966c1b5cf520e6b6d56de2d56776cbb2d9ade69f2819c90ca2bb890
    role: target
  - path: data/normalized_yaml/algae/asw.yaml
    sha256: e22df35f43210d4fddaeab19ab37a75582bc6580ca362228a53ea54daa7a1d6d
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
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
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
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/ccap_raw_yaml.py
    sha256: f2c119c4f67bd245c9fbd2b7480c1c6454a64b79922599cb583203628f476a8c
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
  - path: src/culturemech/fetch/ccap_fetcher.py
    sha256: 09e297722639216f5211096bcac559fae674a03a46e0d324f8360996836368e8
    role: context
  - path: src/culturemech/import/ccap_importer.py
    sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
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
  selection: Task review 317; batch 032 item 7 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-one task batches
    contain 310 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 313 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000050
targets:
- target_id: CultureMech:000050
  path: data/merge_yaml/merged/ASW.yaml
  label: asw
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ASW.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000050
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ASW.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch032/317/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-032/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch032/317/strict.tsv"
  target_ids:
  - CultureMech:000050
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ASW.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000050
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ASW.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000050
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
  - CultureMech:000050
- check_id: ccapSE1-source-access
  name: 'Exact source content access: ccapSE1'
  required: false
  status: unavailable
  summary: An older SE1 candidate URL returned 404; the official current recipe index
    resolves a separately captured successful SE1 PDF. This failed attempt does not
    leave the required soil-stock source unavailable.
  target_ids:
  - CultureMech:000050
  evidence_ids:
  - ccapSE1-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ASW.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T18:00:48Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/algae/asw.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T18:00:48Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ASW.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:55:22.133395Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ASW.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch032/317/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T17:55:23.230274Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-032/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch032/317/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ASW.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:55:24.486905Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ASW.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:55:25.356353Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T18:00:48Z'
  support: supports
  summary: './data/merge_yaml/merged/ASW.yaml:1:id: CultureMech:000050

    ./data/normalized_yaml/algae/asw.yaml:1:id: CultureMech:000050

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch032/source-preflight-bound/317/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T18:00:48Z'
  support: supports
  summary: 18 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: a8a122cb03e6f0aece5d6fe3e052404139183e2afce811223cb83514d0ceee17
- evidence_id: primary
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf
  locator: Complete one-page revision 002, stock and final-medium tables and preparation
  accessed_at: '2026-10-21T17:38:20.424774Z'
  support: supports
  summary: Exact ASW primary visually inspected; salt and vitamin tables are stocks
    per litre, with distinct medium doses.
  quote: Stock solution 1       7.50 ml
  snapshot_sha256: 381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6
- evidence_id: soil
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf
  locator: Complete SE1 recipe, preparing soil and Medium sections
  accessed_at: '2026-10-21T07:18:30.190899Z'
  support: supports
  summary: The currently indexed SE1 recipe supplies the referenced stock process;
    these conditions are not main-medium growth conditions.
  quote: autoclaved together at 15 psi and 126°C for 20 minutes. After the mixture
    has cooled, it is then
  snapshot_sha256: a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934
- evidence_id: soil-index
  kind: primary_source
  reference: https://www.ccap.ac.uk/index.php/media-recipes/
  locator: Official recipe list links ASW and SE1
  accessed_at: '2026-10-21T17:40:19.055901Z'
  support: supports
  summary: Exact official index resolves the moved soil-extract PDF; an obsolete candidate
    URL returned 404.
  snapshot_sha256: 4b852c1459cfe0aa8c80d91a3282b6aef37c3a979be6dd9a49268afa286a0a38
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: 'CHEBI:131527 resolves to dipotassium hydrogen phosphate. Stored labels:
    [''dipotassium hydrogen phosphate'']. Exact label correspondence is separate from
    source chemical-form support.'
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: 'CHEBI:15940 resolves to nicotinic acid. Stored labels: [''nicotinic acid''].
    Exact label correspondence is separate from source chemical-form support.'
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: 'CHEBI:15956 resolves to biotin. Stored labels: [''biotin'']. Exact label
    correspondence is separate from source chemical-form support.'
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi17268
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17268
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T07:16:23.488883Z'
  support: supports
  summary: 'CHEBI:17268 resolves to myo-inositol. Stored labels: [''myo-inositol''].
    Exact label correspondence is separate from source chemical-form support.'
  snapshot_sha256: 0b0cce127edf288993722217ac5a9c05a0bb876b8c34a481b3a41a20ed847888
- evidence_id: chebi17439
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T07:16:23.574834Z'
  support: supports
  summary: 'CHEBI:17439 resolves to cyanocob(III)alamin. Stored labels: [''cyanocob(III)alamin''].
    Exact label correspondence is separate from source chemical-form support.'
  snapshot_sha256: 210a9fbc1db1c75e6053f4e23d098851ad5c63f087c736061f7664d9a393dbdd
- evidence_id: chebi17821
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17821
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T07:16:24.079737Z'
  support: supports
  summary: 'CHEBI:17821 resolves to thymine. Stored labels: [''thymine'']. Exact label
    correspondence is separate from source chemical-form support.'
  snapshot_sha256: fa842c97ef37eb7149260a49f37f93a747804bf52c8534ddc616c9c2e0bdbba4
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: 'CHEBI:27470 resolves to folic acid. Stored labels: [''folic acid'']. Exact
    label correspondence is separate from source chemical-form support.'
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: 'CHEBI:31345 resolves to Calcium pantothenate. Stored labels: [''Calcium
    pantothenate'']. Exact label correspondence is separate from source chemical-form
    support.'
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi34545
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34545
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T17:38:21.396213Z'
  support: supports
  summary: 'CHEBI:34545 resolves to Azimilide. Stored labels: [''Azimilide'']. Exact
    label correspondence is separate from source chemical-form support.'
  snapshot_sha256: 7428ebe8819bde10a59ec0490021b3d056e688351b91e01e783e037de23ade79
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: 'CHEBI:34683 resolves to disodium hydrogenphosphate. Stored labels: [''disodium
    hydrogenphosphate'']. Exact label correspondence is separate from source chemical-form
    support.'
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi46760
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46760
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T07:16:24.837633Z'
  support: supports
  summary: 'CHEBI:46760 resolves to tricine. Stored labels: [''tricine'']. Exact label
    correspondence is separate from source chemical-form support.'
  snapshot_sha256: 209acf0fe4e8f79f96615834a69b6a113baf59b37f08ecedb1a154b6ada66c27
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: 'CHEBI:49105 resolves to thiamine hydrochloride. Stored labels: [''thiamine
    hydrochloride'']. Exact label correspondence is separate from source chemical-form
    support.'
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned index exact identifier lookup; adjacent snapshot metadata
  accessed_at: '2026-10-21T18:00:48Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows":
    {}, "missing_current_keys": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ASW.yaml; data/normalized_yaml/algae/asw.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T18:00:48Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": [{"index": 2, "issue":
    "timezone absent", "value": "2026-02-03T11:26:43.465115"}, {"index": 5, "issue":
    "timezone absent", "value": "2026-04-04T12:54:54.898350"}]}, {"input": "data/normalized_yaml/algae/asw.yaml",
    "events": 11, "timestamp_issues": [{"index": 2, "issue": "timezone absent", "value":
    "2026-02-03T11:26:43.465115"}, {"index": 5, "issue": "timezone absent", "value":
    "2026-04-04T12:54:54.898350"}]}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:00:48Z'
  support: context_only
  summary: Current exact CCAP import, instruction repair, source normalization and
    merge context inspected. The repair explicitly excludes stock-strength remediation;
    current functions do not prove historical causation.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:00:48Z'
  support: context_only
  summary: Current exact CCAP import, instruction repair, source normalization and
    merge context inspected. The repair explicitly excludes stock-strength remediation;
    current functions do not prove historical causation.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: scripts/repair_ccap_instruction_rows.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:00:48Z'
  support: context_only
  summary: Current exact CCAP import, instruction repair, source normalization and
    merge context inspected. The repair explicitly excludes stock-strength remediation;
    current functions do not prove historical causation.
  snapshot_sha256: eb1a4c8c46eb45dcdde6a5d2f0f6833792dd0802c45603eefa1b63a3ff96fca5
- evidence_id: writer-3
  kind: record_content
  reference: scripts/repair_ccap_sources_score10.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:00:48Z'
  support: context_only
  summary: Current exact CCAP import, instruction repair, source normalization and
    merge context inspected. The repair explicitly excludes stock-strength remediation;
    current functions do not prove historical causation.
  snapshot_sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
- evidence_id: writer-4
  kind: record_content
  reference: src/culturemech/import/ccap_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:00:48Z'
  support: context_only
  summary: Current exact CCAP import, instruction repair, source normalization and
    merge context inspected. The repair explicitly excludes stock-strength remediation;
    current functions do not prove historical causation.
  snapshot_sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch032/317/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T18:00:48Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: d378a7bd6878e5b14919b164de9676b52bdfa03121b768a314bdcd17c3169ba6
- evidence_id: ccapSE1-attempt
  kind: database
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_SE1.pdf
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:39:19.133128Z'
  support: context_only
  summary: An older SE1 candidate URL returned 404; the official current recipe index
    resolves a separately captured successful SE1 PDF. This failed attempt does not
    leave the required soil-stock source unavailable.
  snapshot_sha256: c97d3e2df370d89ca7069bd2fc081f0d9a9c3bd8ac5de7dddc24da325daea639
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000050
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary chemical identifiers
  outcome: concern
  summary: '12 distinct primary/current-secondary IDs resolve to nonobsolete terms;
    exact stored/canonical labels are recorded separately in each term evidence item.
    Target direct-ingredient linkage is 12/13 primary (92.31%) and 0/13 current CHEBI-based
    secondary (0.00%), on a 0–100 linkage scale, not an accuracy score. Current secondary
    keys without pinned index rows: []. Legacy slot count 0 is separate and does not
    enter that current-key claim. Supplied-form correspondence is assessed separately.'
  target_ids:
  - CultureMech:000050
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi15940
  - chebi15956
  - chebi17268
  - chebi17439
  - chebi17821
  - chebi27470
  - chebi31345
  - chebi34545
  - chebi34683
  - chebi46760
  - chebi49105
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 21 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:000050
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact source and single maintained owner
  outcome: supported
  summary: CCAP:ASW and the exact MR_ASW PDF identify Artificial Seawater. The unique
    stable-ID owner is algae/asw.yaml, not its bacterial namesake. The source is the
    current CCAP adaptation, not proof of identity to every historical version or
    to ASWP.
  target_ids:
  - CultureMech:000050
  evidence_ids:
  - record
  - owner-0
  - primary
  - soil-index
- assessment_id: forms
  area: grounding
  topic: Chemical identity and source specificity
  outcome: concern
  summary: NaNO3 is sodium nitrate, whereas CHEBI:34545 is Azimilide with an unrelated
    organic formula. The two phosphate salts, biotin, cyanocobalamin, folic acid,
    nicotinic acid, thiamine hydrochloride, thymine and tricine agree at the named
    source level. Source calcium pantothenate does not state stereochemistry, while
    CHEBI:31345 encodes it; source Inositol does not establish the myo configuration
    of CHEBI:17268. These last two are specificity limits, not proof of alternate
    isomers. All primary labels resolve, and both layers assert zero secondary MIM
    links.
  target_ids:
  - CultureMech:000050
  evidence_ids:
  - primary
  - chebi34545
  - chebi31345
  - chebi17268
  - mim
- assessment_id: scope
  area: scope
  topic: Classification, use and preparation scope
  outcome: concern
  summary: Complex/undefined liquid medium is reasonable for seawater and soil extract.
    The primary supports a marine-algae medium, not the numeric growth temperature
    or light recommendations. No strain-level growth or optimum follows from the title.
    The soil extraction temperatures and resting periods belong only to SE1.
  target_ids:
  - CultureMech:000050
  evidence_ids:
  - record
  - primary
  - soil
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 35 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:000050
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"label\": \"NaNO3 stock strength\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Extra-salt stock 1\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15.00\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15.00\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Stock-table heading\",\n        \"exact_source_quote\"\
    : \"Stocks         per litre\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      },\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Extra-salt stock 1 exact ingredient row\",\n        \"exact_source_quote\"\
    : \"NaNO3       15.00 g\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing numeric strength matches\
    \ the stock recipe per litre, but is falsely positioned as a direct medium ingredient.\
    \ Retain the original stock amount and unit, then represent its separate 7.50\
    \ ml per litre dose. Do not treat the full stock recipe as a final-medium quantity.\"\
    \n  },\n  {\n    \"decision_id\": \"q2\",\n    \"label\": \"Na2HPO4 stock strength\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Extra-salt stock 1\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.60\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.60\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Stock-table heading\",\n        \"exact_source_quote\"\
    : \"Stocks         per litre\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      },\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Extra-salt stock 1 exact ingredient row\",\n        \"exact_source_quote\"\
    : \"Na2HPO4      0.60 g\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing numeric strength matches\
    \ the stock recipe per litre, but is falsely positioned as a direct medium ingredient.\
    \ Retain the original stock amount and unit, then represent its separate 7.50\
    \ ml per litre dose. Do not treat the full stock recipe as a final-medium quantity.\"\
    \n  },\n  {\n    \"decision_id\": \"q3\",\n    \"label\": \"K2HPO4 stock strength\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Extra-salt stock 1\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.50\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.50\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Stock-table heading\",\n        \"exact_source_quote\"\
    : \"Stocks         per litre\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      },\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Extra-salt stock 1 exact ingredient row\",\n        \"exact_source_quote\"\
    : \"K2HPO4      0.50 g\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing numeric strength matches\
    \ the stock recipe per litre, but is falsely positioned as a direct medium ingredient.\
    \ Retain the original stock amount and unit, then represent its separate 7.50\
    \ ml per litre dose. Do not treat the full stock recipe as a final-medium quantity.\"\
    \n  },\n  {\n    \"decision_id\": \"q4\",\n    \"label\": \"Biotin stock strength\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Vitamin stock 2\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0002\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0002\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Stock-table heading\",\n        \"exact_source_quote\"\
    : \"Stocks         per litre\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      },\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Vitamin stock 2 exact ingredient row\",\n        \"exact_source_quote\": \"\
    Biotin       0.0002 g\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing numeric strength matches\
    \ the stock recipe per litre, but is falsely positioned as a direct medium ingredient.\
    \ Retain the original stock amount and unit, then represent its separate 2.50\
    \ ml per litre dose. Do not treat the full stock recipe as a final-medium quantity.\"\
    \n  },\n  {\n    \"decision_id\": \"q5\",\n    \"label\": \"Calcium pantothenate\
    \ stock strength\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"\
    Vitamin stock 2\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Stock-table heading\",\n        \"exact_source_quote\"\
    : \"Stocks         per litre\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      },\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Vitamin stock 2 exact ingredient row\",\n        \"exact_source_quote\": \"\
    Calcium pantothenate    0.02 g\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing numeric strength matches\
    \ the stock recipe per litre, but is falsely positioned as a direct medium ingredient.\
    \ Retain the original stock amount and unit, then represent its separate 2.50\
    \ ml per litre dose. Do not treat the full stock recipe as a final-medium quantity.\"\
    \n  },\n  {\n    \"decision_id\": \"q6\",\n    \"label\": \"Cyanocobalamin stock\
    \ strength\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Vitamin\
    \ stock 2\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Stock-table heading\",\n        \"exact_source_quote\"\
    : \"Stocks         per litre\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      },\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Vitamin stock 2 exact ingredient row\",\n        \"exact_source_quote\": \"\
    Cyanocobalamin     0.004 g\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing numeric strength matches\
    \ the stock recipe per litre, but is falsely positioned as a direct medium ingredient.\
    \ Retain the original stock amount and unit, then represent its separate 2.50\
    \ ml per litre dose. Do not treat the full stock recipe as a final-medium quantity.\"\
    \n  },\n  {\n    \"decision_id\": \"q7\",\n    \"label\": \"Folic acid stock strength\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Vitamin stock 2\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Stock-table heading\",\n        \"exact_source_quote\"\
    : \"Stocks         per litre\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      },\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Vitamin stock 2 exact ingredient row\",\n        \"exact_source_quote\": \"\
    Folic acid      0.0004 g\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing numeric strength matches\
    \ the stock recipe per litre, but is falsely positioned as a direct medium ingredient.\
    \ Retain the original stock amount and unit, then represent its separate 2.50\
    \ ml per litre dose. Do not treat the full stock recipe as a final-medium quantity.\"\
    \n  },\n  {\n    \"decision_id\": \"q8\",\n    \"label\": \"Inositol stock strength\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Vitamin stock 2\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Stock-table heading\",\n        \"exact_source_quote\"\
    : \"Stocks         per litre\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      },\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Vitamin stock 2 exact ingredient row\",\n        \"exact_source_quote\": \"\
    Inositol      1.0 g\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing numeric strength matches\
    \ the stock recipe per litre, but is falsely positioned as a direct medium ingredient.\
    \ Retain the original stock amount and unit, then represent its separate 2.50\
    \ ml per litre dose. Do not treat the full stock recipe as a final-medium quantity.\"\
    \n  },\n  {\n    \"decision_id\": \"q9\",\n    \"label\": \"Nicotinic acid stock\
    \ strength\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Vitamin\
    \ stock 2\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Stock-table heading\",\n        \"exact_source_quote\"\
    : \"Stocks         per litre\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      },\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Vitamin stock 2 exact ingredient row\",\n        \"exact_source_quote\": \"\
    Nicotinic acid      0.02 g\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing numeric strength matches\
    \ the stock recipe per litre, but is falsely positioned as a direct medium ingredient.\
    \ Retain the original stock amount and unit, then represent its separate 2.50\
    \ ml per litre dose. Do not treat the full stock recipe as a final-medium quantity.\"\
    \n  },\n  {\n    \"decision_id\": \"q10\",\n    \"label\": \"Thiamine HCl stock\
    \ strength\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Vitamin\
    \ stock 2\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Stock-table heading\",\n        \"exact_source_quote\"\
    : \"Stocks         per litre\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      },\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Vitamin stock 2 exact ingredient row\",\n        \"exact_source_quote\": \"\
    Thiamine HCl      0.1 g\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing numeric strength matches\
    \ the stock recipe per litre, but is falsely positioned as a direct medium ingredient.\
    \ Retain the original stock amount and unit, then represent its separate 2.50\
    \ ml per litre dose. Do not treat the full stock recipe as a final-medium quantity.\"\
    \n  },\n  {\n    \"decision_id\": \"q11\",\n    \"label\": \"Thymine stock strength\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Vitamin stock 2\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Stock-table heading\",\n        \"exact_source_quote\"\
    : \"Stocks         per litre\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      },\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Vitamin stock 2 exact ingredient row\",\n        \"exact_source_quote\": \"\
    Thymine      0.6 g\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing numeric strength matches\
    \ the stock recipe per litre, but is falsely positioned as a direct medium ingredient.\
    \ Retain the original stock amount and unit, then represent its separate 2.50\
    \ ml per litre dose. Do not treat the full stock recipe as a final-medium quantity.\"\
    \n  },\n  {\n    \"decision_id\": \"q12\",\n    \"label\": \"Tricine main-medium\
    \ quantity\",\n    \"decision\": \"evidence_only\",\n    \"source_stage\": \"\
    Final medium\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.50\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.50\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Main-medium heading\",\n        \"exact_source_quote\"\
    : \"Medium         per litre\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      },\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Main-medium tricine row\",\n        \"exact_source_quote\": \"Tricine    \
    \   0.50 g\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing 0.50 g/L matches the\
    \ final-medium table; no claim-level amount evidence is attached in either layer.\"\
    \n  },\n  {\n    \"decision_id\": \"q13\",\n    \"label\": \"Extra-salt stock\
    \ dose\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Final-medium stock\
    \ 1 addition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Medium per litre, Extra-salt stock dose\",\n\
    \        \"exact_source_quote\": \"Stock solution 1       7.50 ml\",\n       \
    \ \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore this explicit stock addition\
    \ and its distinct composition/provenance. The stock recipe denominator is separate\
    \ from the receiving medium denominator.\"\n  },\n  {\n    \"decision_id\": \"\
    q14\",\n    \"label\": \"Vitamin stock dose\",\n    \"decision\": \"add\",\n \
    \   \"source_stage\": \"Final-medium stock 2 addition\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\",\n      \
    \  \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"presence\"\
    : \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Medium per litre, Vitamin stock dose\",\n   \
    \     \"exact_source_quote\": \"Stock solution 2      2.50 ml\",\n        \"snapshot_sha256\"\
    : \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\",\n    \
    \    \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore this explicit stock addition\
    \ and its distinct composition/provenance. The stock recipe denominator is separate\
    \ from the receiving medium denominator.\"\n  },\n  {\n    \"decision_id\": \"\
    q15\",\n    \"label\": \"SE1 dose\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"Final-medium soil-extract addition\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ASW.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null,\n        \"presence\": \"absent\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Medium per litre, SE1 dose\",\n        \"exact_source_quote\"\
    : \"Stock solution 3 (SE1)     25.00 ml\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore this explicit stock addition\
    \ and its distinct composition/provenance. The stock recipe denominator is separate\
    \ from the receiving medium denominator.\"\n  },\n  {\n    \"decision_id\": \"\
    q16\",\n    \"label\": \"Target instruction masquerading as an ingredient\",\n\
    \    \"decision\": \"correct\",\n    \"source_stage\": \"Final volume\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].preferred_term\",\n        \"stored\"\
    : \"Make up to\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        }\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"ccapASW\"\
    ,\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Final-medium make-up sentence\",\n        \"\
    exact_source_quote\": \"Make up to 1 Litre with filtered natural seawater.* Adjust\
    \ pH 7.6 – 7.8 to with 1M NaOH or 1M\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The value 1 L is a final make-up\
    \ instruction, not a reagent or a standalone water addition. The maintained owner\
    \ already removed this row.\"\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"\
    label\": \"Owner final make-up instruction\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"Final volume\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/algae/asw.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0]\",\n        \"stored\": {\n          \"step_number\"\
    : 1,\n          \"action\": \"MIX\",\n          \"description\": \"Bring to 1\
    \ L with filtered natural seawater.\"\n        }\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\": \"\
    https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\",\n        \"source_locator\"\
    : \"Final-medium make-up sentence\",\n        \"exact_source_quote\": \"Make up\
    \ to 1 Litre with filtered natural seawater.* Adjust pH 7.6 – 7.8 to with 1M NaOH\
    \ or 1M\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The maintained owner correctly specifies\
    \ final volume 1 L using filtered natural seawater; attach the literal source.\
    \ This is not adding 1 L after the stock aliquots.\"\n  },\n  {\n    \"decision_id\"\
    : \"q18\",\n    \"label\": \"Target missing pH and titrant strength\",\n    \"\
    decision\": \"add\",\n    \"source_stage\": \"Main-medium pH adjustment\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Final-medium pH and titrant sentence\",\n   \
    \     \"exact_source_quote\": \"Make up to 1 Litre with filtered natural seawater.*\
    \ Adjust pH 7.6 – 7.8 to with 1M NaOH or 1M \\nHCl, prior to autoclaving. Autoclave\
    \ at 15 psi for 15 minutes.\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore pH 7.6–7.8 and the alternative\
    \ 1 M NaOH or 1 M HCl titrants; volumes are not quantified. These are preparation\
    \ values, not measured growth optima.\"\n  },\n  {\n    \"decision_id\": \"q19\"\
    ,\n    \"label\": \"Owner pH and titrant strength\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"Main-medium pH adjustment\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\",\n  \
    \      \"field_path\": \"preparation_steps[1]\",\n        \"stored\": {\n    \
    \      \"step_number\": 2,\n          \"action\": \"ADJUST_PH\",\n          \"\
    description\": \"Adjust pH to 7.6-7.8 with 1 M NaOH or 1 M HCl before autoclaving.\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Final-medium pH and titrant sentence\",\n   \
    \     \"exact_source_quote\": \"Make up to 1 Litre with filtered natural seawater.*\
    \ Adjust pH 7.6 – 7.8 to with 1M NaOH or 1M \\nHCl, prior to autoclaving. Autoclave\
    \ at 15 psi for 15 minutes.\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing instruction retains\
    \ pH 7.6–7.8 and both 1 M titrants correctly, without attached evidence.\"\n \
    \ },\n  {\n    \"decision_id\": \"q20\",\n    \"label\": \"Titrant volumes\",\n\
    \    \"decision\": \"not_quantified\",\n    \"source_stage\": \"Main-medium titration\"\
    ,\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Main-medium pH sentence\",\n        \"exact_source_quote\"\
    : \"Make up to 1 Litre with filtered natural seawater.* Adjust pH 7.6 – 7.8 to\
    \ with 1M NaOH or 1M \\nHCl, prior to autoclaving. Autoclave at 15 psi for 15\
    \ minutes.\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"Neither titrant addition volume is\
    \ supplied; do not infer a dose from its 1 M stock strength.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q21\",\n    \"label\": \"Target sterilization\",\n    \"\
    decision\": \"add\",\n    \"source_stage\": \"Main-medium sterilization\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Main-medium sterilization sentence\",\n     \
    \   \"exact_source_quote\": \"HCl, prior to autoclaving. Autoclave at 15 psi for\
    \ 15 minutes.\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore 15 psi for 15 minutes. The\
    \ exact main page does not specify temperature or gauge/absolute pressure basis.\"\
    \n  },\n  {\n    \"decision_id\": \"q22\",\n    \"label\": \"Owner sterilization\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_stage\": \"Main-medium sterilization\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2]\",\n        \"stored\": {\n\
    \          \"step_number\": 3,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Autoclave at 15 psi for 15 minutes.\"\n        }\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Main-medium sterilization sentence\",\n     \
    \   \"exact_source_quote\": \"HCl, prior to autoclaving. Autoclave at 15 psi for\
    \ 15 minutes.\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The maintained owner correctly preserves\
    \ 15 psi and 15 minutes. Attach source evidence without importing a temperature\
    \ from the soil stock.\"\n  },\n  {\n    \"decision_id\": \"q23\",\n    \"label\"\
    : \"Alternative artificial-seawater branch\",\n    \"decision\": \"add\",\n  \
    \  \"source_stage\": \"Alternative final-medium branch\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"ccapASW\"\
    ,\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Footnoted alternative make-up\",\n        \"\
    exact_source_quote\": \"*Alternatively, use deionised water to 1 litre and 33.6\
    \ g “Instant Ocean” sea salts.\",\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the explicitly alternative\
    \ deionized-water make-up to 1 litre with 33.6 g Instant Ocean. This is not an\
    \ additional salt dose in the natural-seawater branch; no commercial constituent\
    \ breakdown is inferred.\"\n  },\n  {\n    \"decision_id\": \"q24\",\n    \"label\"\
    : \"Unsupported temperature_range\",\n    \"decision\": \"unsupported\",\n   \
    \ \"source_stage\": \"Unsupported growth conditions\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\",\n      \
    \  \"field_path\": \"temperature_range\",\n        \"stored\": \"15-30°C depending\
    \ on species\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/asw.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": \"15-30°C\
    \ depending on species\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Source identity; entire exact page checked for\
    \ growth conditions\",\n        \"exact_source_quote\": \"ASW (Artificial Seawater)\"\
    ,\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The current primary contains no corresponding\
    \ growth condition. The current importer writes general defaults; this is context,\
    \ not historical authentication or experimental evidence. Remove or qualify these\
    \ ungrounded numeric recommendations rather than derive conditions from SE1 processing.\"\
    \n  },\n  {\n    \"decision_id\": \"q25\",\n    \"label\": \"Unsupported light_intensity\"\
    ,\n    \"decision\": \"unsupported\",\n    \"source_stage\": \"Unsupported growth\
    \ conditions\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"light_intensity\",\n        \"stored\": \"Varies\
    \ by species; typically 50-100 µmol photons m⁻² s⁻¹\"\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/algae/asw.yaml\",\n        \"field_path\"\
    : \"light_intensity\",\n        \"stored\": \"Varies by species; typically 50-100\
    \ µmol photons m⁻² s⁻¹\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Source identity; entire exact page checked for\
    \ growth conditions\",\n        \"exact_source_quote\": \"ASW (Artificial Seawater)\"\
    ,\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The current primary contains no corresponding\
    \ growth condition. The current importer writes general defaults; this is context,\
    \ not historical authentication or experimental evidence. Remove or qualify these\
    \ ungrounded numeric recommendations rather than derive conditions from SE1 processing.\"\
    \n  },\n  {\n    \"decision_id\": \"q26\",\n    \"label\": \"Unsupported light_cycle\"\
    ,\n    \"decision\": \"unsupported\",\n    \"source_stage\": \"Unsupported growth\
    \ conditions\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ASW.yaml\"\
    ,\n        \"field_path\": \"light_cycle\",\n        \"stored\": \"Varies by species;\
    \ commonly 12:12 or 16:8 light:dark\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/algae/asw.yaml\",\n        \"field_path\": \"light_cycle\"\
    ,\n        \"stored\": \"Varies by species; commonly 12:12 or 16:8 light:dark\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapASW\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_ASW.pdf\"\
    ,\n        \"source_locator\": \"Source identity; entire exact page checked for\
    \ growth conditions\",\n        \"exact_source_quote\": \"ASW (Artificial Seawater)\"\
    ,\n        \"snapshot_sha256\": \"381d399b9245d205b55ace4a65ee118239ab56e941d45ed7fea140a89e1813b6\"\
    ,\n        \"parsed_text_sha256\": \"dc7ace9f28511a353597ed142125c41fe16c9364b685de9345f5747e11f2c721\"\
    \n      }\n    ],\n    \"interpretation\": \"The current primary contains no corresponding\
    \ growth condition. The current importer writes general defaults; this is context,\
    \ not historical authentication or experimental evidence. Remove or qualify these\
    \ ungrounded numeric recommendations rather than derive conditions from SE1 processing.\"\
    \n  },\n  {\n    \"decision_id\": \"q27\",\n    \"label\": \"SE1 Initial sieve\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"SE1 preparation\",\n  \
    \  \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapSE1current\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf\"\
    ,\n        \"source_locator\": \"SE1 Initial sieve sentence\",\n        \"exact_source_quote\"\
    : \"should be removed during an initial sieving through a 1 cm mesh. The sieved\
    \ soil should be\",\n        \"snapshot_sha256\": \"a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934\"\
    ,\n        \"parsed_text_sha256\": \"3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the 1 cm mesh only for preparing\
    \ soil. This applies only to the referenced SE1 stock.\"\n  },\n  {\n    \"decision_id\"\
    : \"q28\",\n    \"label\": \"SE1 Optional oven drying\",\n    \"decision\": \"\
    add\",\n    \"source_stage\": \"SE1 preparation\",\n    \"local_fields\": [],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"ccapSE1current\"\
    ,\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf\"\
    ,\n        \"source_locator\": \"SE1 Optional oven drying sentence\",\n      \
    \  \"exact_source_quote\": \"spread to air dry or placed in a drying oven at around\
    \ 50°C. When dry, the soil is sieved again\",\n        \"snapshot_sha256\": \"\
    a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934\",\n        \"\
    parsed_text_sha256\": \"3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661\"\
    \n      }\n    ],\n    \"interpretation\": \"Around 50°C applies to drying soil,\
    \ not cultivation. This applies only to the referenced SE1 stock.\"\n  },\n  {\n\
    \    \"decision_id\": \"q29\",\n    \"label\": \"SE1 Second sieve\",\n    \"decision\"\
    : \"add\",\n    \"source_stage\": \"SE1 preparation\",\n    \"local_fields\":\
    \ [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"ccapSE1current\"\
    ,\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf\"\
    ,\n        \"source_locator\": \"SE1 Second sieve sentence\",\n        \"exact_source_quote\"\
    : \"through a finer mesh (2-4 mm) and stored in an airtight container away from\
    \ light and heat.\",\n        \"snapshot_sha256\": \"a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934\"\
    ,\n        \"parsed_text_sha256\": \"3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the 2–4 mm sieve only for\
    \ dry soil. This applies only to the referenced SE1 stock.\"\n  },\n  {\n    \"\
    decision_id\": \"q30\",\n    \"label\": \"SE1 Soil-to-water volume ratio\",\n\
    \    \"decision\": \"add\",\n    \"source_stage\": \"SE1 preparation\",\n    \"\
    local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapSE1current\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf\"\
    ,\n        \"source_locator\": \"SE1 Soil-to-water volume ratio sentence\",\n\
    \        \"exact_source_quote\": \"Soil is prepared as above. Dried soil and twice\
    \ its volume of supernatant d eionised water are\",\n        \"snapshot_sha256\"\
    : \"a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934\",\n    \
    \    \"parsed_text_sha256\": \"3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661\"\
    \n      }\n    ],\n    \"interpretation\": \"Twice the soil volume of water is\
    \ a volume ratio, not an asserted soil g/L concentration. This applies only to\
    \ the referenced SE1 stock.\"\n  },\n  {\n    \"decision_id\": \"q31\",\n    \"\
    label\": \"SE1 First soil cycle\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"SE1 preparation\",\n    \"local_fields\": [],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"ccapSE1current\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf\",\n        \"\
    source_locator\": \"SE1 First soil cycle sentence\",\n        \"exact_source_quote\"\
    : \"autoclaved together at 15 psi and 126°C for 20 minutes. After the mixture\
    \ has cooled, it is then\",\n        \"snapshot_sha256\": \"a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934\"\
    ,\n        \"parsed_text_sha256\": \"3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact printed 15 psi,\
    \ 126°C and 20 minutes. This applies only to the referenced SE1 stock.\"\n  },\n\
    \  {\n    \"decision_id\": \"q32\",\n    \"label\": \"SE1 Second soil cycle\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"SE1 preparation\",\n  \
    \  \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapSE1current\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf\"\
    ,\n        \"source_locator\": \"SE1 Second soil cycle sentence\",\n        \"\
    exact_source_quote\": \"autoclaved for a second time at 15 psi and 126°C for 20\
    \ minutes. After the mixture has cooled,\",\n        \"snapshot_sha256\": \"a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934\"\
    ,\n        \"parsed_text_sha256\": \"3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the second 15 psi, 126°C,\
    \ 20-minute cycle after cooling. This applies only to the referenced SE1 stock.\"\
    \n  },\n  {\n    \"decision_id\": \"q33\",\n    \"label\": \"SE1 Soil settling\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"SE1 preparation\",\n  \
    \  \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapSE1current\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf\"\
    ,\n        \"source_locator\": \"SE1 Soil settling sentence\",\n        \"exact_source_quote\"\
    : \"the bottle is sealed with parafilm and left undisturbed on a shelf for around\
    \ two to three weeks\",\n        \"snapshot_sha256\": \"a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934\"\
    ,\n        \"parsed_text_sha256\": \"3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661\"\
    \n      }\n    ],\n    \"interpretation\": \"Around two to three weeks is stock\
    \ settling, not incubation. This applies only to the referenced SE1 stock.\"\n\
    \  },\n  {\n    \"decision_id\": \"q34\",\n    \"label\": \"SE1 Final extract\
    \ sterilization\",\n    \"decision\": \"add\",\n    \"source_stage\": \"SE1 preparation\"\
    ,\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"ccapSE1current\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf\"\
    ,\n        \"source_locator\": \"SE1 Final extract sterilization sentence\",\n\
    \        \"exact_source_quote\": \"After decanting, the final soil extract is\
    \ autoclaved for a third time at 15 psi and 121 °C for 15 \\nminutes. After the\
    \ soil extract has cooled, the bottle is sealed with parafilm and stored in the\"\
    ,\n        \"snapshot_sha256\": \"a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934\"\
    ,\n        \"parsed_text_sha256\": \"3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the third cycle at 15 psi\
    \ and 121°C for 15 minutes; do not silently reconcile pressure/temperature typography.\
    \ This applies only to the referenced SE1 stock.\"\n  },\n  {\n    \"decision_id\"\
    : \"q35\",\n    \"label\": \"SE1 unspecified soil strength and refrigeration temperature\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"source_stage\": \"SE1 stock limits\"\
    ,\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"ccapSE1current\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf\"\
    ,\n        \"source_locator\": \"SE1 soil/water sentence\",\n        \"exact_source_quote\"\
    : \"Soil is prepared as above. Dried soil and twice its volume of supernatant\
    \ d eionised water are\",\n        \"snapshot_sha256\": \"a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934\"\
    ,\n        \"parsed_text_sha256\": \"3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661\"\
    \n      },\n      {\n        \"source_key\": \"ccapSE1current\",\n        \"source_url\"\
    : \"https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf\",\n        \"\
    source_locator\": \"SE1 storage sentence\",\n        \"exact_source_quote\": \"\
    fridge.\",\n        \"snapshot_sha256\": \"a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934\"\
    ,\n        \"parsed_text_sha256\": \"3490ed31480436276ccda818f7b7fe2c2f1a7de774a96922cea96683b1f83661\"\
    \n      }\n    ],\n    \"interpretation\": \"No soil mass per litre or numerical\
    \ refrigeration temperature is given. Keep qualitative woodland-loam selection,\
    \ cooling, aseptic decanting and refrigerated storage.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: cm000050-stocks
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock strengths are flattened and their medium doses are missing
  description: The first eleven ingredient values are stock-table strengths, not final-medium
    concentrations. Neither layer represents the separate 7.50 ml salt stock, 2.50
    ml vitamin stock and 25 ml SE1 doses per litre.
  target_ids:
  - CultureMech:000050
  field_paths:
  - ingredients[0:11]
  - solutions
  evidence_ids:
  - primary
  - soil
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
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
  issue_key: cm000050-nitrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium nitrate is linked to the unrelated drug Azimilide
  description: The source explicitly prints NaNO3. Local NaNO is linked to CHEBI:34545,
    whose canonical identity and structure are Azimilide; canonical label validation
    does not detect this source mismatch.
  target_ids:
  - CultureMech:000050
  field_paths:
  - ingredients[0].preferred_term
  - ingredients[0].term
  evidence_ids:
  - primary
  - chebi34545
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
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
  issue_key: cm000050-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated instructions are stale and the alternative formulation is missing
  description: The target retains Make up to as an ingredient and no preparation,
    while the maintained owner has correct make-up, pH and sterilization instructions.
    Both omit the explicit deionized-water/33.6 g Instant Ocean alternative and the
    scoped soil-extract process.
  target_ids:
  - CultureMech:000050
  field_paths:
  - ingredients
  - preparation_steps
  - medium_variants
  evidence_ids:
  - primary
  - soil
  - owner-0
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
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
  issue_key: cm000050-growth-defaults
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generic light and temperature values lack recipe-specific support
  description: Both layers assert 50–100 light intensity, 12:12 or 16:8 light cycles
    and 15–30°C. The exact primary does not supply these values; current importer
    defaults are not growth evidence.
  target_ids:
  - CultureMech:000050
  field_paths:
  - light_intensity
  - light_cycle
  - temperature_range
  evidence_ids:
  - primary
  - record
  - writer-4
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
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
  issue_key: cm000050-specificity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two stereochemical selections exceed the printed source
  description: The source says calcium pantothenate and inositol. Existing CHEBI:31345
    and myo-inositol encode specificity not established by those source words. This
    does not prove a different stereoisomer was used.
  target_ids:
  - CultureMech:000050
  field_paths:
  - ingredients[4].term
  - ingredients[7].term
  evidence_ids:
  - primary
  - chebi31345
  - chebi17268
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: cm000050-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Curation confidence is not claim-level scientific evidence
  description: Source references and LLM confidence values do not attach exact stock-stage
    amount evidence. Several historical timestamps lack timezone information; the
    current PDF revision postdates the original import.
  target_ids:
  - CultureMech:000050
  field_paths:
  - ingredients[*].curation_metadata
  - ingredients[*].evidence
  - curation_history
  evidence_ids:
  - primary
  - history-metadata
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
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
  description: Restore stock composition, dose and final-medium relationships in the
    maintained owner; preserve SE1 as a source-scoped constituent and regenerate only
    through the authorized workflow.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000050
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
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
  description: Correct the name and chemical identity using separately verified sodium-nitrate
    grounding; do not invent a replacement identifier in this review.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000050
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
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
  description: Keep the owner’s valid instructions, add narrow evidence and missing
    source branches/stocks, then address generated staleness without editing the target
    directly.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000050
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
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
  description: Remove or explicitly qualify unsupported recommendations; require actual
    source evidence for any retained organism-specific condition.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000050
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
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
  description: Seek exact product or source-form evidence, or qualify the unresolved
    specificity without asserting a guessed alternative.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:000050
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
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
- action_id: a6
  description: Attach exact versioned source claims and preserve historical events,
    adding timezone/provenance clarification only when supported.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:000050
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/asw.yaml
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
- An older SE1 candidate URL returned 404; the official current recipe index resolves
  a separately captured successful SE1 PDF. This failed attempt does not leave the
  required soil-stock source unavailable.
- The current CCAP adaptation is assessed as captured. Historical PDF byte equivalence,
  unspecified titrant volumes, pressure basis and source-unspecified stereochemistry
  are not inferred; the referenced 1957 paper is not used to authenticate the current
  CCAP adaptation.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-032
- generated-medium
```
