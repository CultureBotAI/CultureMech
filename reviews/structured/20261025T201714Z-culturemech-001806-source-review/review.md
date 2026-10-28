# Source and formulation review: cellulosilyticum_medium (CultureMech:001806)

- Review: 20261025T201714Z-culturemech-001806-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-25T20:08:35Z
- Finished UTC: 2026-10-25T20:17:14Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSM 666a PDF supports the listed batch masses and retained preparation, but the structured recipe omits clarified rumen fluid and water. Stock preparation is detached from its receiving dose, and exact final-volume rates are not authenticated by the currently unavailable API.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 525; batch 053 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fifty-two task batches contain 520 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 231e0ba71b41d45362168d539efebe7991823464 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 523 of 6325 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 231e0ba71b41d45362168d539efebe7991823464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001806 | data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml | generated | cellulosilyticum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001806 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001806 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch053/525/strict.tsv |
| validate-terms | passed | True | CultureMech:001806 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001806 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001806 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: api666a | unavailable | True | CultureMech:001806 | The exact MediaDive 666a API request returned HTTP 503. Current DSM PDF content is available and assessed separately; historical API g_l values and raw digest claims cannot be authenticated from this failed response. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001806.

The four documented recipes completed; interpret the scope of each separately.

### Exact DSM suffix accession and ownership

identity: supported. Targets: CultureMech:001806.

The source title is DSM 666a CELLULOSILYTICUM MEDIUM, matching the target and its single maintained owner. The a suffix is retained. The PDF supplies preparation and formulation, not strain-specific measured growth.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:001806.

12 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 12/13 primary and 12/13 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 13: primary 92.31%; secondary 92.31%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Source-specific salt and stereochemical precision

grounding: supported. Targets: CultureMech:001806.

The PDF explicitly supplies calcium chloride dihydrate, magnesium sulfate heptahydrate, L-cysteine hydrochloride monohydrate and DL-dithiothreitol. The asserted OLS definitions/synonyms support these stated forms; indigo carmine matches its supplied name. No molecular-weight conversion, yeast-extract molecule, or new stock identifier is inferred.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001806.

15 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Historical reviews and exact source authentication

provenance: concern. Targets: CultureMech:001806.

All four exact historical reports and the selected owner plan row were read. The October plan preserves thirteen conflict decisions and decoded provider rows, including g_l claims, but its cited raw 5d027f51… is not recovered by the bounded context. The September report assumes a final-litre formulation and links a provider stock; those statements remain derivative. The current complete PDF independently supports batch masses, missing liquids and scoped preparation, without converting the failed API into a successful source check.

### Retained main and stock preparation

completeness: supported. Targets: CultureMech:001806.

The full source prose is substantially retained, including separate gas stages, conditional final pH, delayed sterile stocks, cellobiose filtration and clarified-fluid treatment. The missing structured stock dose and weak section labeling remain separate defects; existing preparation is not absent.

### Mixture, agar and organism claims

scope: unknown. Targets: CultureMech:001806.

The recipe is complex because it uses yeast extract and rumen fluid. The source explicitly lists 1 g agar; this review does not infer gel strength or correct SOLID_AGAR to another physical state solely from that amount. No strain-specific growth evidence or incubation condition is supplied.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001806.

28 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "K2HPO4",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.23",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.23",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, K2HPO4 row",
        "exact_source_quote": "K2HPO4                                                 0.23      g",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate."
  },
  {
    "decision_id": "q2",
    "subject": "KH2PO4",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.23",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.23",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, KH2PO4 row",
        "exact_source_quote": "KH2PO4                                                 0.23      g",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate."
  },
  {
    "decision_id": "q3",
    "subject": "NaCl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.45",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.45",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, NaCl row",
        "exact_source_quote": "NaCl                                                   0.45      g",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate."
  },
  {
    "decision_id": "q4",
    "subject": "(NH4)2SO4",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.45",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.45",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, (NH4)2SO4 row",
        "exact_source_quote": "(NH4)2SO4                                              0.45      g",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate."
  },
  {
    "decision_id": "q5",
    "subject": "CaCl2 x 2 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.06",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.06",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, CaCl2 x 2 H2O row",
        "exact_source_quote": "CaCl2 x 2 H2O                                          0.06      g",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate."
  },
  {
    "decision_id": "q6",
    "subject": "MgSO4 x 7 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.09",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.09",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, MgSO4 x 7 H2O row",
        "exact_source_quote": "MgSO4 x 7 H2O                                          0.09      g",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate."
  },
  {
    "decision_id": "q7",
    "subject": "Agar",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, Agar row",
        "exact_source_quote": "Agar                                                   1.00      g",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate."
  },
  {
    "decision_id": "q8",
    "subject": "Indigocarmine",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, Indigocarmine row",
        "exact_source_quote": "Indigocarmine                                          5.00     mg",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate. The source 5 mg equals 0.005 g per batch; that conversion is sound without establishing a denominator."
  },
  {
    "decision_id": "q9",
    "subject": "NaHCO3",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "6.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "6.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, NaHCO3 row",
        "exact_source_quote": "NaHCO3                                                 6.40      g",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate."
  },
  {
    "decision_id": "q10",
    "subject": "Cellobiose",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, Cellobiose row",
        "exact_source_quote": "Cellobiose                                             2.50      g",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate."
  },
  {
    "decision_id": "q11",
    "subject": "Yeast extract",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, Yeast extract row",
        "exact_source_quote": "Yeast extract                                          5.00      g",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate."
  },
  {
    "decision_id": "q12",
    "subject": "L-Cysteine HCl x H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, L-Cysteine HCl x H2O row",
        "exact_source_quote": "L-Cysteine HCl x H2O                                   0.30      g",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate."
  },
  {
    "decision_id": "q13",
    "subject": "DL-Dithiothreitol",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, DL-Dithiothreitol (DTT) row",
        "exact_source_quote": "DL-Dithiothreitol (DTT)                                0.30      g",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The PDF supports this stated mass per recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume makeup or volumes of the later sterile stocks are given. The whole local G_PER_L rate is therefore not independently established. Preserve the supported batch mass and seek exact provider/version evidence before treating it as a final-medium rate."
  },
  {
    "decision_id": "q14",
    "subject": "Clarified rumen fluid batch input",
    "decision": "add",
    "local_fields": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, Clarified rumen fluid",
        "exact_source_quote": "Clarified rumen fluid                                400.00     ml",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "Add the missing structured 400 mL rumen-fluid batch input and connect only its embedded preparation. No parent basal formula or universal mL/L dose is inferred."
  },
  {
    "decision_id": "q15",
    "subject": "Distilled water batch input",
    "decision": "add",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine and DTT), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete medium to 6.7 - 6.8, if necessary."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine and DTT), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete medium to 6.7 - 6.8, if necessary."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main recipe table, Distilled water",
        "exact_source_quote": "Distilled water                                      600.00     ml",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "Add the explicit 600 mL water batch input to preparation context. Existing instructions are retained; this input is not a measured final volume."
  },
  {
    "decision_id": "q16",
    "subject": "Conditional complete-medium pH range",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ph_range.min",
        "stored": 6.7
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ph_range.min",
        "stored": 6.7
      },
      {
        "input": "target",
        "field_path": "ph_range.max",
        "stored": 6.8
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "ph_range.max",
        "stored": 6.8
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main preparation, final sentence",
        "exact_source_quote": "Adjust pH of complete medium to 6.7 - 6.8, if necessary.",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The retained 6.7–6.8 range is supported, conditional on adjustment being necessary; attach that exact stage-specific evidence."
  },
  {
    "decision_id": "q17",
    "subject": "Main atmosphere",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine and DTT), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete medium to 6.7 - 6.8, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine and DTT), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete medium to 6.7 - 6.8, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main preparation, cooling atmosphere",
        "exact_source_quote": "100% CO2 gas\natmosphere.",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "Retain the pure CO2 cooling atmosphere and the separate CO2 dispensing instruction; this is not an incubation-gas measurement."
  },
  {
    "decision_id": "q18",
    "subject": "Bicarbonate equilibration pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine and DTT), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete medium to 6.7 - 6.8, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine and DTT), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete medium to 6.7 - 6.8, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main preparation, after bicarbonate",
        "exact_source_quote": "equilibrate the medium with the CO2 gas to pH 6.8.",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "Retain the 6.8 equilibration target separately from the complete-medium 6.7–6.8 adjustment."
  },
  {
    "decision_id": "q19",
    "subject": "Sterile-stock atmosphere",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine and DTT), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete medium to 6.7 - 6.8, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine and DTT), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete medium to 6.7 - 6.8, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main preparation, delayed additions",
        "exact_source_quote": "anoxic stock solutions prepared under 100% N2 gas atmosphere.",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "Retain pure N2 for preparing the delayed sterile stocks; do not substitute it for the main CO2 atmosphere."
  },
  {
    "decision_id": "q20",
    "subject": "Rumen-fluid heat treatment",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 Clarified rumen fluid subsection",
        "exact_source_quote": "autoclaved at 121°C for 15 min",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "Retain 121°C for 15 min only for the clarified-fluid preparation. The main-medium autoclave cycle is not specified here."
  },
  {
    "decision_id": "q21",
    "subject": "Rumen-fluid centrifugation",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 Clarified rumen fluid subsection",
        "exact_source_quote": "centrifuged at 27,000 g\nfor 20 min.",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "Retain relative centrifugal force 27,000 g for 20 min at the stock stage; do not reinterpret g as a mass or rpm."
  },
  {
    "decision_id": "q22",
    "subject": "Rumen-fluid sparging",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 Clarified rumen fluid subsection",
        "exact_source_quote": "sparging with 100% N2 gas for 15 min,",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "Retain pure N2 and 15 min only for making the stock supernatant anoxic."
  },
  {
    "decision_id": "q23",
    "subject": "Rumen-fluid vial fill",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 Clarified rumen fluid subsection",
        "exact_source_quote": "anoxic serum vials to 30% of volume",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "Retain the 30% vial-fill instruction. It is not a rumen-fluid concentration in the receiving medium."
  },
  {
    "decision_id": "q24",
    "subject": "Rumen-fluid frozen storage",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 Clarified rumen fluid subsection",
        "exact_source_quote": "stored frozen at -20°C.",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "Retain −20°C as the prepared-stock storage temperature, not organism incubation temperature."
  },
  {
    "decision_id": "q25",
    "subject": "Main-medium autoclave cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].action",
        "stored": "AUTOCLAVE"
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[0].action",
        "stored": "AUTOCLAVE"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main preparation",
        "exact_source_quote": "and autoclave.",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "Main-medium autoclaving is stated without its own temperature or duration. Do not transfer 121°C/15 min from the separate rumen-fluid subsection."
  },
  {
    "decision_id": "q26",
    "subject": "Delayed stock strengths and addition volumes",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine and DTT), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete medium to 6.7 - 6.8, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine and DTT), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete medium to 6.7 - 6.8, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main preparation, delayed additions",
        "exact_source_quote": "add cellobiose, yeast extract, cysteine and DTT from sterile\nanoxic stock solutions",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The source requires separate sterile anoxic stocks but gives no stock strengths or individual added volumes. Listed batch masses remain separate; no dilution calculation or fixed stock rate is fabricated."
  },
  {
    "decision_id": "q27",
    "subject": "Cellobiose sterilization",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine and DTT), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete medium to 6.7 - 6.8, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine and DTT), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete medium to 6.7 - 6.8, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 main preparation",
        "exact_source_quote": "Cellobiose has to be\nsterilzed by filtration.",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The retained filtration requirement is supported. No filter pore size, temperature or duration is supplied."
  },
  {
    "decision_id": "q28",
    "subject": "Local instruction indexing",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].step_number",
        "stored": 1
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[0].step_number",
        "stored": 1
      },
      {
        "input": "target",
        "field_path": "preparation_steps[1].step_number",
        "stored": 2
      },
      {
        "input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
        "field_path": "preparation_steps[1].step_number",
        "stored": 2
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz666a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf",
        "source_locator": "Page 1 stock subsection heading",
        "exact_source_quote": "Clarified rumen fluid (from medium 1310)",
        "snapshot_sha256": "0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b",
        "parsed_text_sha256": "db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53"
      }
    ],
    "rationale": "The integers 1 and 2 are local ordering metadata, not source measurements. Preserve their distinct main/stock scopes; the second step must not be read as a second main-medium autoclave instruction."
  }
]

## Findings

### f1: The required clarified-fluid addition is absent

major / open / confirmed; issue key: cm001806-missing-rumen-fluid.

Both local layers retain the stock preparation prose but omit the 400 mL clarified-rumen-fluid entry and all structured solutions. The PDF places it first in the main table. Restore the missing stock topology while crediting the retained preparation.

### f2: Final-medium rate evidence and solvent context are incomplete

major / open / confirmed; issue key: cm001806-amount-basis-evidence.

The thirteen local G_PER_L values lack attached amount evidence. The PDF supports batch masses and 600 mL water but does not explicitly establish the final volume after later stock additions. The historical provider rows are derivative and the current API returns 503. Preserve source masses; do not silently endorse all final-medium rates.

### f3: Stock treatment is not labeled as a distinct preparation stage

minor / open / confirmed; issue key: cm001806-stock-stage-labeling.

The second AUTOCLAVE step contains a full rumen-fluid workflow but lacks the source subsection label and receiving-stock connection. Its 121°C/15 min, centrifugation, vial fill and frozen storage must not be transferred to the basal medium.

## Recommended Actions And Acceptance Checks

### a1

Represent the 400 mL batch input in a structured stock descriptor and attach the embedded clarified-fluid preparation without importing medium 1310 basal conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore solvent context and exact source evidence, distinguishing batch masses from rates whose denominator still requires source/version verification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Label or structure the clarified-fluid stage and preserve all existing source-supported prose; keep the unspecified main autoclave cycle unresolved.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch053/525/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch053/525/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml:1:id: CultureMech:001806<br>./data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml:1:id: CultureMech:001806<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch053/source-preflight-bound/525/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 16 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| dsm-recipe | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf; Page 1, main recipe table and both preparation sections; rendered page independently read | supports | Complete text and rendered page read. The main table lists 400 mL clarified rumen fluid, 600 mL water and thirteen masses. The separate clarified-rumen-fluid section is explicitly from medium 1310; only that embedded subsection is used. No separate parent-medium formula is transferred. |
| api666a-attempt | https://mediadive.dsmz.de/rest/medium/666a; Preserved exact public retrieval result | context_only | The exact MediaDive 666a API request returned HTTP 503. Current DSM PDF content is available and assessed separately; historical API g_l values and raw digest claims cannot be authenticated from this failed response. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17057 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17057 resolves to cellobiose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi18320 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18320; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:18320 resolves to 1,4-dithiothreitol. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31695 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31695; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31695 resolves to indigo carmine. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17057": [{"label": "Cellobiose", "match_type": "preferred_term", "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:18320": [{"label": "DL-Dithiothreitol", "match_type": "preferred_term", "identifier": "CHEBI:18320", "preferred_term": "DL-Dithiothreitol", "ontology_id": "CHEBI:18320", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31695": [{"label": "Indigocarmine", "match_type": "preferred_term", "identifier": "CHEBI:31695", "preferred_term": "Indigocarmine", "ontology_id": "CHEBI:31695", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| historical-context | /private/tmp/culturemech-review-work-batch053/525/historical-evidence-review.json; Exact current history arrays, header-matched report texts, parent locators and raw-authentication outcomes | context_only | All four exact historical reports and the selected owner plan row were read. The October plan preserves thirteen conflict decisions and decoded provider rows, including g_l claims, but its cited raw 5d027f51… is not recovered by the bounded context. The September report assumes a final-litre formulation and links a provider stock; those statements remain derivative. The current complete PDF independently supports batch masses, missing liquids and scoped preparation, without converting the failed API into a successful source check. |
| grounding-census | /private/tmp/culturemech-review-work-batch053/525/grounding-review.json; Every scoped asserted identifier and exact current CSV/catalog correspondence; excluded parent fields remain excluded | context_only | Bound independent census retains source/field membership and exact identifier matches. Current catalog presence does not authenticate historical use or a receiving-medium recipe. |
| field-census | /private/tmp/culturemech-review-work-batch053/525/local-field-census.json; Complete scalar census of the explicitly listed local documents | context_only | Exact values and locators retained for mechanical reconciliation; this census alone does not establish scientific support. |
| history-metadata | data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml; data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml", "events": 7, "timestamp_issues": []}] |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition and _parse_api_solutions | context_only | Current API parsing uses the primary solution only, keeps referenced stocks separately and excludes solvent volumes from direct chemical edges. This current separation deserves credit; omitted solvent context still needs explicit preservation, and the old selected recipe has no structured rumen-fluid stock. Current code is not proof of the historical execution that produced these bytes. |
| writer-merge | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | The single-owner branch copies the owner with merge metadata. Multi-owner inputs are delegated to merge_formulation_evidence for compatibility checks; no new source support is generated. Current code is not proof of the historical execution that produced these bytes. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch053/525/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact MediaDive 666a API request returned HTTP 503. Current DSM PDF content is available and assessed separately; historical API g_l values and raw digest claims cannot be authenticated from this failed response.
- The PDF was read both as extracted text and as its rendered single page. The strengths and addition volumes of the late cellobiose, yeast-extract, cysteine and DTT stocks are not supplied; the 400 mL clarified-rumen-fluid addition is explicitly supplied. Final-volume makeup and measured growth are not supplied. The historical API response digest remains a recorded claim, not authenticated current raw content.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T201714Z-culturemech-001806-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: cellulosilyticum_medium (CultureMech:001806)'
started_at: '2026-10-25T20:08:35Z'
finished_at: '2026-10-25T20:17:14Z'
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
summary: The exact DSM 666a PDF supports the listed batch masses and retained preparation,
  but the structured recipe omits clarified rumen fluid and water. Stock preparation
  is detached from its receiving dose, and exact final-volume rates are not authenticated
  by the currently unavailable API.
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
  - path: data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml
    sha256: d7dfe0c88b005ca82dde181bcd3af76de7a9e1beb545093045ebfb515ef8ab33
    role: target
  - path: data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml
    sha256: a5f47ebd648467e63277ec14fcbb5d2a8cff9bc668fbd1d7fed2b49e8e5aeb6d
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
  selection: Task review 525; batch 053 item 5 of 10, selected in Python lexicographic
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
  - CultureMech:001806
targets:
- target_id: CultureMech:001806
  path: data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml
  label: cellulosilyticum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch053/525/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch053/525/strict.tsv"
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001806
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
  - CultureMech:001806
- check_id: api666a-source-access
  name: 'Exact source content access: api666a'
  required: true
  status: unavailable
  summary: The exact MediaDive 666a API request returned HTTP 503. Current DSM PDF
    content is available and assessed separately; historical API g_l values and raw
    digest claims cannot be authenticated from this failed response.
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - api666a-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-25T20:14:25Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-25T20:14:25Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:04.084947Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch053/525/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:07.877850Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch053/525/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:12.687511Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:15.769278Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-25T20:14:25Z'
  support: supports
  summary: './data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml:1:id: CultureMech:001806

    ./data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml:1:id: CultureMech:001806

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/source-preflight-bound/525/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-25T20:14:25Z'
  support: supports
  summary: 16 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 1ed92eb556a676ff4c57fcc25ea2da3af1148eebc0485aa9e18074090f18351e
- evidence_id: dsm-recipe
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf
  locator: Page 1, main recipe table and both preparation sections; rendered page
    independently read
  accessed_at: '2026-10-22T09:27:18.248165Z'
  support: supports
  summary: Complete text and rendered page read. The main table lists 400 mL clarified
    rumen fluid, 600 mL water and thirteen masses. The separate clarified-rumen-fluid
    section is explicitly from medium 1310; only that embedded subsection is used.
    No separate parent-medium formula is transferred.
  snapshot_sha256: 0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b
- evidence_id: api666a-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/666a
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T09:27:19.576199Z'
  support: context_only
  summary: The exact MediaDive 666a API request returned HTTP 503. Current DSM PDF
    content is available and assessed separately; historical API g_l values and raw
    digest claims cannot be authenticated from this failed response.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
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
- evidence_id: chebi17057
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:39.796651Z'
  support: supports
  summary: CHEBI:17057 resolves to cellobiose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 3548f79d3274a33683125152944998cffa00bd4fce774c8d872db9003222ed06
- evidence_id: chebi18320
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18320
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:37:24.678779Z'
  support: supports
  summary: CHEBI:18320 resolves to 1,4-dithiothreitol. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 475ff3beab5570f7c37e9627477a11b45f76f0be7b4d04d07c310416b58c5e54
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
- evidence_id: chebi31695
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31695
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-22T09:27:33.172011Z'
  support: supports
  summary: CHEBI:31695 resolves to indigo carmine. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 6794d5fd7f7c03d30561811100441f99178363ed217827337d12fdad299b569b
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
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:08.324907Z'
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
  accessed_at: '2026-10-21T08:43:09.378884Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi91248
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:32.136441Z'
  support: supports
  summary: CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-25T20:14:25Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17057": [{"label": "Cellobiose", "match_type":
    "preferred_term", "identifier": "CHEBI:17057", "preferred_term": "Cellobiose",
    "ontology_id": "CHEBI:17057", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:18320": [{"label": "DL-Dithiothreitol", "match_type": "preferred_term",
    "identifier": "CHEBI:18320", "preferred_term": "DL-Dithiothreitol", "ontology_id":
    "CHEBI:18320", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509":
    [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31695": [{"label":
    "Indigocarmine", "match_type": "preferred_term", "identifier": "CHEBI:31695",
    "preferred_term": "Indigocarmine", "ontology_id": "CHEBI:31695", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type":
    "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id":
    "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946":
    [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946",
    "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x
    H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term":
    "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: historical-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/525/historical-evidence-review.json
  locator: Exact current history arrays, header-matched report texts, parent locators
    and raw-authentication outcomes
  accessed_at: '2026-10-25T20:14:25Z'
  support: context_only
  summary: All four exact historical reports and the selected owner plan row were
    read. The October plan preserves thirteen conflict decisions and decoded provider
    rows, including g_l claims, but its cited raw 5d027f51… is not recovered by the
    bounded context. The September report assumes a final-litre formulation and links
    a provider stock; those statements remain derivative. The current complete PDF
    independently supports batch masses, missing liquids and scoped preparation, without
    converting the failed API into a successful source check.
  snapshot_sha256: dc01017939364b3632e8e98236743b79380e03b7a15f50152b73c1d26a233b33
- evidence_id: grounding-census
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/525/grounding-review.json
  locator: Every scoped asserted identifier and exact current CSV/catalog correspondence;
    excluded parent fields remain excluded
  accessed_at: '2026-10-25T20:14:25Z'
  support: context_only
  summary: Bound independent census retains source/field membership and exact identifier
    matches. Current catalog presence does not authenticate historical use or a receiving-medium
    recipe.
  snapshot_sha256: fdd8244c6b235bb3f7568c010e51dc6da8a782262c8a7830367541251a063a48
- evidence_id: field-census
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/525/local-field-census.json
  locator: Complete scalar census of the explicitly listed local documents
  accessed_at: '2026-10-25T20:14:25Z'
  support: context_only
  summary: Exact values and locators retained for mechanical reconciliation; this
    census alone does not establish scientific support.
  snapshot_sha256: 836496dc6522b7a351a952613bf90377d7e450bbcf5b9fb9c7294f5363e14aea
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml; data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-25T20:14:25Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition and _parse_api_solutions
  accessed_at: '2026-10-25T20:14:25Z'
  support: context_only
  summary: Current API parsing uses the primary solution only, keeps referenced stocks
    separately and excludes solvent volumes from direct chemical edges. This current
    separation deserves credit; omitted solvent context still needs explicit preservation,
    and the old selected recipe has no structured rumen-fluid stock. Current code
    is not proof of the historical execution that produced these bytes.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-25T20:14:25Z'
  support: context_only
  summary: The single-owner branch copies the owner with merge metadata. Multi-owner
    inputs are delegated to merge_formulation_evidence for compatibility checks; no
    new source support is generated. Current code is not proof of the historical execution
    that produced these bytes.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/525/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-25T20:14:25Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 99323594eeade4409883831a99554bf0725ddb72bb4fe92b869dcc4d6109b060
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact DSM suffix accession and ownership
  outcome: supported
  summary: The source title is DSM 666a CELLULOSILYTICUM MEDIUM, matching the target
    and its single maintained owner. The a suffix is retained. The PDF supplies preparation
    and formulation, not strain-specific measured growth.
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - record
  - owner-0
  - dsm-recipe
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '12 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 12/13
    primary and 12/13 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi17057
  - chebi18320
  - chebi2509
  - chebi26710
  - chebi31695
  - chebi31795
  - chebi32139
  - chebi62946
  - chebi63036
  - chebi86158
  - chebi91248
  details: 'Instance coverage on a 0–100 percent scale, denominator 13: primary 92.31%;
    secondary 92.31%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: forms
  area: grounding
  topic: Source-specific salt and stereochemical precision
  outcome: supported
  summary: The PDF explicitly supplies calcium chloride dihydrate, magnesium sulfate
    heptahydrate, L-cysteine hydrochloride monohydrate and DL-dithiothreitol. The
    asserted OLS definitions/synonyms support these stated forms; indigo carmine matches
    its supplied name. No molecular-weight conversion, yeast-extract molecule, or
    new stock identifier is inferred.
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - dsm-recipe
  - chebi86158
  - chebi31795
  - chebi91248
  - chebi18320
  - chebi31695
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 15 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: historical-scope
  area: provenance
  topic: Historical reviews and exact source authentication
  outcome: concern
  summary: All four exact historical reports and the selected owner plan row were
    read. The October plan preserves thirteen conflict decisions and decoded provider
    rows, including g_l claims, but its cited raw 5d027f51… is not recovered by the
    bounded context. The September report assumes a final-litre formulation and links
    a provider stock; those statements remain derivative. The current complete PDF
    independently supports batch masses, missing liquids and scoped preparation, without
    converting the failed API into a successful source check.
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - historical-context
  - record
- assessment_id: preparation-credit
  area: completeness
  topic: Retained main and stock preparation
  outcome: supported
  summary: The full source prose is substantially retained, including separate gas
    stages, conditional final pH, delayed sterile stocks, cellobiose filtration and
    clarified-fluid treatment. The missing structured stock dose and weak section
    labeling remain separate defects; existing preparation is not absent.
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - record
  - owner-0
  - dsm-recipe
- assessment_id: classification
  area: scope
  topic: Mixture, agar and organism claims
  outcome: unknown
  summary: The recipe is complex because it uses yeast extract and rumen fluid. The
    source explicitly lists 1 g agar; this review does not infer gel strength or correct
    SOLID_AGAR to another physical state solely from that amount. No strain-specific
    growth evidence or incubation condition is supplied.
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - record
  - dsm-recipe
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 28 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001806
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"K2HPO4\",\n \
    \   \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.23\",\n          \"unit\":\
    \ \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.23\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, K2HPO4 row\",\n   \
    \     \"exact_source_quote\": \"K2HPO4                                       \
    \          0.23      g\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate.\"\n  },\n  {\n    \"decision_id\": \"q2\",\n    \"subject\": \"KH2PO4\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.23\",\n          \"unit\":\
    \ \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.23\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, KH2PO4 row\",\n   \
    \     \"exact_source_quote\": \"KH2PO4                                       \
    \          0.23      g\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n    \"subject\": \"NaCl\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.45\",\n          \"unit\":\
    \ \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.45\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, NaCl row\",\n     \
    \   \"exact_source_quote\": \"NaCl                                           \
    \        0.45      g\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n    \"subject\": \"(NH4)2SO4\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.45\",\n          \"unit\":\
    \ \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.45\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, (NH4)2SO4 row\",\n\
    \        \"exact_source_quote\": \"(NH4)2SO4                                 \
    \             0.45      g\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"subject\": \"CaCl2 x\
    \ 2 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.06\",\n          \"unit\":\
    \ \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.06\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, CaCl2 x 2 H2O row\"\
    ,\n        \"exact_source_quote\": \"CaCl2 x 2 H2O                           \
    \               0.06      g\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n    \"subject\": \"MgSO4 x\
    \ 7 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.09\",\n          \"unit\":\
    \ \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.09\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, MgSO4 x 7 H2O row\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O                           \
    \               0.09      g\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"subject\": \"Agar\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, Agar row\",\n     \
    \   \"exact_source_quote\": \"Agar                                           \
    \        1.00      g\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"subject\": \"Indigocarmine\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\"\
    : \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, Indigocarmine row\"\
    ,\n        \"exact_source_quote\": \"Indigocarmine                           \
    \               5.00     mg\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate. The source 5 mg equals 0.005 g per batch; that conversion is sound without\
    \ establishing a denominator.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n   \
    \ \"subject\": \"NaHCO3\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[8].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"6.4\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, NaHCO3 row\",\n   \
    \     \"exact_source_quote\": \"NaHCO3                                       \
    \          6.40      g\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate.\"\n  },\n  {\n    \"decision_id\": \"q10\",\n    \"subject\": \"Cellobiose\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"target\",\n        \"field_path\": \"ingredients[9].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2.5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, Cellobiose row\",\n\
    \        \"exact_source_quote\": \"Cellobiose                                \
    \             2.50      g\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"subject\": \"Yeast\
    \ extract\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, Yeast extract row\"\
    ,\n        \"exact_source_quote\": \"Yeast extract                           \
    \               5.00      g\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n    \"subject\": \"L-Cysteine\
    \ HCl x H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[11].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.3\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, L-Cysteine HCl x H2O\
    \ row\",\n        \"exact_source_quote\": \"L-Cysteine HCl x H2O             \
    \                      0.30      g\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"subject\": \"DL-Dithiothreitol\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"target\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.3\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, DL-Dithiothreitol (DTT)\
    \ row\",\n        \"exact_source_quote\": \"DL-Dithiothreitol (DTT)          \
    \                      0.30      g\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The PDF supports this stated mass per\
    \ recipe batch. Its 400 mL fluid plus 600 mL water are listed inputs; no final-volume\
    \ makeup or volumes of the later sterile stocks are given. The whole local G_PER_L\
    \ rate is therefore not independently established. Preserve the supported batch\
    \ mass and seek exact provider/version evidence before treating it as a final-medium\
    \ rate.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"subject\": \"Clarified\
    \ rumen fluid batch input\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz666a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, Clarified rumen fluid\"\
    ,\n        \"exact_source_quote\": \"Clarified rumen fluid                   \
    \             400.00     ml\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"Add the missing structured 400 mL rumen-fluid\
    \ batch input and connect only its embedded preparation. No parent basal formula\
    \ or universal mL/L dose is inferred.\"\n  },\n  {\n    \"decision_id\": \"q15\"\
    ,\n    \"subject\": \"Distilled water batch input\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"preparation_steps\",\n        \"stored\": [\n          {\n   \
    \         \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\",\n      \
    \      \"description\": \"Dissolve ingredients (except bicarbonate, cellobiose,\
    \ yeast extract, cysteine and DTT), bring medium to the boil, then cool to room\
    \ temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate\
    \ the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere\
    \ into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add\
    \ cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions\
    \ prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration.\
    \ Adjust pH of complete medium to 6.7 - 6.8, if necessary.\"\n          },\n \
    \         {\n            \"step_number\": 2,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Rumen fluid from cow or sheep (obtained from\
    \ fistulated animals or abattoir refuse) is filtered through muslin, autoclaved\
    \ at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant\
    \ is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same\
    \ gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen\
    \ at -20°C.\"\n          }\n        ]\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": [\n          {\n            \"step_number\"\
    : 1,\n            \"action\": \"AUTOCLAVE\",\n            \"description\": \"\
    Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine\
    \ and DTT), bring medium to the boil, then cool to room temperature under 100%\
    \ CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the\
    \ CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract,\
    \ cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2\
    \ gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete\
    \ medium to 6.7 - 6.8, if necessary.\"\n          },\n          {\n          \
    \  \"step_number\": 2,\n            \"action\": \"AUTOCLAVE\",\n            \"\
    description\": \"Rumen fluid from cow or sheep (obtained from fistulated animals\
    \ or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min\
    \ and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic\
    \ by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere\
    \ into anoxic serum vials to 30% of volume and then stored frozen at -20°C.\"\n\
    \          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe table, Distilled water\",\n\
    \        \"exact_source_quote\": \"Distilled water                           \
    \           600.00     ml\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"Add the explicit 600 mL water batch input\
    \ to preparation context. Existing instructions are retained; this input is not\
    \ a measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"\
    subject\": \"Conditional complete-medium pH range\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ph_range.min\",\n        \"stored\": 6.7\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range.min\",\n        \"stored\": 6.7\n      },\n\
    \      {\n        \"input\": \"target\",\n        \"field_path\": \"ph_range.max\"\
    ,\n        \"stored\": 6.8\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range.max\",\n        \"stored\": 6.8\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz666a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation, final sentence\",\n\
    \        \"exact_source_quote\": \"Adjust pH of complete medium to 6.7 - 6.8,\
    \ if necessary.\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The retained 6.7–6.8 range is supported,\
    \ conditional on adjustment being necessary; attach that exact stage-specific\
    \ evidence.\"\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"subject\": \"Main\
    \ atmosphere\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Dissolve ingredients (except bicarbonate, cellobiose,\
    \ yeast extract, cysteine and DTT), bring medium to the boil, then cool to room\
    \ temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate\
    \ the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere\
    \ into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add\
    \ cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions\
    \ prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration.\
    \ Adjust pH of complete medium to 6.7 - 6.8, if necessary.\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine\
    \ and DTT), bring medium to the boil, then cool to room temperature under 100%\
    \ CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the\
    \ CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract,\
    \ cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2\
    \ gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete\
    \ medium to 6.7 - 6.8, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz666a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main preparation, cooling atmosphere\",\n     \
    \   \"exact_source_quote\": \"100% CO2 gas\\natmosphere.\",\n        \"snapshot_sha256\"\
    : \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\",\n    \
    \    \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the pure CO2 cooling atmosphere\
    \ and the separate CO2 dispensing instruction; this is not an incubation-gas measurement.\"\
    \n  },\n  {\n    \"decision_id\": \"q18\",\n    \"subject\": \"Bicarbonate equilibration\
    \ pH\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Dissolve ingredients (except bicarbonate, cellobiose,\
    \ yeast extract, cysteine and DTT), bring medium to the boil, then cool to room\
    \ temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate\
    \ the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere\
    \ into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add\
    \ cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions\
    \ prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration.\
    \ Adjust pH of complete medium to 6.7 - 6.8, if necessary.\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine\
    \ and DTT), bring medium to the boil, then cool to room temperature under 100%\
    \ CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the\
    \ CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract,\
    \ cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2\
    \ gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete\
    \ medium to 6.7 - 6.8, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz666a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main preparation, after bicarbonate\",\n      \
    \  \"exact_source_quote\": \"equilibrate the medium with the CO2 gas to pH 6.8.\"\
    ,\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the 6.8 equilibration target separately\
    \ from the complete-medium 6.7–6.8 adjustment.\"\n  },\n  {\n    \"decision_id\"\
    : \"q19\",\n    \"subject\": \"Sterile-stock atmosphere\",\n    \"decision\":\
    \ \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps[0].description\",\n   \
    \     \"stored\": \"Dissolve ingredients (except bicarbonate, cellobiose, yeast\
    \ extract, cysteine and DTT), bring medium to the boil, then cool to room temperature\
    \ under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium\
    \ with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose,\
    \ yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared\
    \ under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration.\
    \ Adjust pH of complete medium to 6.7 - 6.8, if necessary.\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine\
    \ and DTT), bring medium to the boil, then cool to room temperature under 100%\
    \ CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the\
    \ CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract,\
    \ cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2\
    \ gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete\
    \ medium to 6.7 - 6.8, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz666a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main preparation, delayed additions\",\n      \
    \  \"exact_source_quote\": \"anoxic stock solutions prepared under 100% N2 gas\
    \ atmosphere.\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"Retain pure N2 for preparing the delayed\
    \ sterile stocks; do not substitute it for the main CO2 atmosphere.\"\n  },\n\
    \  {\n    \"decision_id\": \"q20\",\n    \"subject\": \"Rumen-fluid heat treatment\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"Rumen fluid from cow or sheep (obtained from fistulated\
    \ animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C\
    \ for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made\
    \ anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere\
    \ into anoxic serum vials to 30% of volume and then stored frozen at -20°C.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir\
    \ refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then\
    \ centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging\
    \ with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic\
    \ serum vials to 30% of volume and then stored frozen at -20°C.\"\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz666a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Clarified rumen fluid subsection\",\n\
    \        \"exact_source_quote\": \"autoclaved at 121°C for 15 min\",\n       \
    \ \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 121°C for 15 min only for the clarified-fluid\
    \ preparation. The main-medium autoclave cycle is not specified here.\"\n  },\n\
    \  {\n    \"decision_id\": \"q21\",\n    \"subject\": \"Rumen-fluid centrifugation\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"Rumen fluid from cow or sheep (obtained from fistulated\
    \ animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C\
    \ for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made\
    \ anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere\
    \ into anoxic serum vials to 30% of volume and then stored frozen at -20°C.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir\
    \ refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then\
    \ centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging\
    \ with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic\
    \ serum vials to 30% of volume and then stored frozen at -20°C.\"\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz666a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Clarified rumen fluid subsection\",\n\
    \        \"exact_source_quote\": \"centrifuged at 27,000 g\\nfor 20 min.\",\n\
    \        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"Retain relative centrifugal force 27,000\
    \ g for 20 min at the stock stage; do not reinterpret g as a mass or rpm.\"\n\
    \  },\n  {\n    \"decision_id\": \"q22\",\n    \"subject\": \"Rumen-fluid sparging\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"Rumen fluid from cow or sheep (obtained from fistulated\
    \ animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C\
    \ for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made\
    \ anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere\
    \ into anoxic serum vials to 30% of volume and then stored frozen at -20°C.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir\
    \ refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then\
    \ centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging\
    \ with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic\
    \ serum vials to 30% of volume and then stored frozen at -20°C.\"\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz666a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Clarified rumen fluid subsection\",\n\
    \        \"exact_source_quote\": \"sparging with 100% N2 gas for 15 min,\",\n\
    \        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"Retain pure N2 and 15 min only for making\
    \ the stock supernatant anoxic.\"\n  },\n  {\n    \"decision_id\": \"q23\",\n\
    \    \"subject\": \"Rumen-fluid vial fill\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"preparation_steps[1].description\",\n        \"stored\": \"Rumen\
    \ fluid from cow or sheep (obtained from fistulated animals or abattoir refuse)\
    \ is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged\
    \ at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100%\
    \ N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials\
    \ to 30% of volume and then stored frozen at -20°C.\"\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir\
    \ refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then\
    \ centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging\
    \ with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic\
    \ serum vials to 30% of volume and then stored frozen at -20°C.\"\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz666a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Clarified rumen fluid subsection\",\n\
    \        \"exact_source_quote\": \"anoxic serum vials to 30% of volume\",\n  \
    \      \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the 30% vial-fill instruction.\
    \ It is not a rumen-fluid concentration in the receiving medium.\"\n  },\n  {\n\
    \    \"decision_id\": \"q24\",\n    \"subject\": \"Rumen-fluid frozen storage\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"Rumen fluid from cow or sheep (obtained from fistulated\
    \ animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C\
    \ for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made\
    \ anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere\
    \ into anoxic serum vials to 30% of volume and then stored frozen at -20°C.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir\
    \ refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then\
    \ centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging\
    \ with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic\
    \ serum vials to 30% of volume and then stored frozen at -20°C.\"\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz666a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Clarified rumen fluid subsection\",\n\
    \        \"exact_source_quote\": \"stored frozen at -20°C.\",\n        \"snapshot_sha256\"\
    : \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\",\n    \
    \    \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"Retain −20°C as the prepared-stock storage\
    \ temperature, not organism incubation temperature.\"\n  },\n  {\n    \"decision_id\"\
    : \"q25\",\n    \"subject\": \"Main-medium autoclave cycle\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps[0].action\",\n        \"\
    stored\": \"AUTOCLAVE\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].action\",\n        \"stored\"\
    : \"AUTOCLAVE\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"and autoclave.\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"Main-medium autoclaving is stated without\
    \ its own temperature or duration. Do not transfer 121°C/15 min from the separate\
    \ rumen-fluid subsection.\"\n  },\n  {\n    \"decision_id\": \"q26\",\n    \"\
    subject\": \"Delayed stock strengths and addition volumes\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps[0].description\",\n   \
    \     \"stored\": \"Dissolve ingredients (except bicarbonate, cellobiose, yeast\
    \ extract, cysteine and DTT), bring medium to the boil, then cool to room temperature\
    \ under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium\
    \ with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclave. Thereafter, add cellobiose,\
    \ yeast extract, cysteine and DTT from sterile anoxic stock solutions prepared\
    \ under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration.\
    \ Adjust pH of complete medium to 6.7 - 6.8, if necessary.\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine\
    \ and DTT), bring medium to the boil, then cool to room temperature under 100%\
    \ CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the\
    \ CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract,\
    \ cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2\
    \ gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete\
    \ medium to 6.7 - 6.8, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz666a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main preparation, delayed additions\",\n      \
    \  \"exact_source_quote\": \"add cellobiose, yeast extract, cysteine and DTT from\
    \ sterile\\nanoxic stock solutions\",\n        \"snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The source requires separate sterile anoxic\
    \ stocks but gives no stock strengths or individual added volumes. Listed batch\
    \ masses remain separate; no dilution calculation or fixed stock rate is fabricated.\"\
    \n  },\n  {\n    \"decision_id\": \"q27\",\n    \"subject\": \"Cellobiose sterilization\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Dissolve ingredients (except bicarbonate, cellobiose,\
    \ yeast extract, cysteine and DTT), bring medium to the boil, then cool to room\
    \ temperature under 100% CO2 gas atmosphere. Add the bicarbonate and equilibrate\
    \ the medium with the CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere\
    \ into anoxic Hungate-type tubes or serum vials and autoclave. Thereafter, add\
    \ cellobiose, yeast extract, cysteine and DTT from sterile anoxic stock solutions\
    \ prepared under 100% N2 gas atmosphere. Cellobiose has to be sterilzed by filtration.\
    \ Adjust pH of complete medium to 6.7 - 6.8, if necessary.\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, cellobiose, yeast extract, cysteine\
    \ and DTT), bring medium to the boil, then cool to room temperature under 100%\
    \ CO2 gas atmosphere. Add the bicarbonate and equilibrate the medium with the\
    \ CO2 gas to pH 6.8. Distribute under 100% CO2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Thereafter, add cellobiose, yeast extract,\
    \ cysteine and DTT from sterile anoxic stock solutions prepared under 100% N2\
    \ gas atmosphere. Cellobiose has to be sterilzed by filtration. Adjust pH of complete\
    \ medium to 6.7 - 6.8, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz666a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"Cellobiose has to be\\nsterilzed by filtration.\",\n        \"snapshot_sha256\"\
    : \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\",\n    \
    \    \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The retained filtration requirement is\
    \ supported. No filter pore size, temperature or duration is supplied.\"\n  },\n\
    \  {\n    \"decision_id\": \"q28\",\n    \"subject\": \"Local instruction indexing\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].step_number\"\
    ,\n        \"stored\": 1\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].step_number\",\n        \"stored\"\
    : 1\n      },\n      {\n        \"input\": \"target\",\n        \"field_path\"\
    : \"preparation_steps[1].step_number\",\n        \"stored\": 2\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].step_number\",\n        \"stored\"\
    : 2\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz666a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium666a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 stock subsection heading\",\n        \"\
    exact_source_quote\": \"Clarified rumen fluid (from medium 1310)\",\n        \"\
    snapshot_sha256\": \"0ad8fe361c85d7e40a525178decc417180e15f12239927ebc4a2bd7bbc8f282b\"\
    ,\n        \"parsed_text_sha256\": \"db5782bc1b4e39aafa09718143bd23947ea22a0cb6d02b63e2ac833654717f53\"\
    \n      }\n    ],\n    \"rationale\": \"The integers 1 and 2 are local ordering\
    \ metadata, not source measurements. Preserve their distinct main/stock scopes;\
    \ the second step must not be read as a second main-medium autoclave instruction.\"\
    \n  }\n]"
findings:
- finding_id: f1
  issue_key: cm001806-missing-rumen-fluid
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The required clarified-fluid addition is absent
  description: Both local layers retain the stock preparation prose but omit the 400
    mL clarified-rumen-fluid entry and all structured solutions. The PDF places it
    first in the main table. Restore the missing stock topology while crediting the
    retained preparation.
  target_ids:
  - CultureMech:001806
  field_paths:
  - ingredients
  - preparation_steps[1]
  evidence_ids:
  - record
  - owner-0
  - dsm-recipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: stock-dose-completeness
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: cm001806-amount-basis-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Final-medium rate evidence and solvent context are incomplete
  description: The thirteen local G_PER_L values lack attached amount evidence. The
    PDF supports batch masses and 600 mL water but does not explicitly establish the
    final volume after later stock additions. The historical provider rows are derivative
    and the current API returns 503. Preserve source masses; do not silently endorse
    all final-medium rates.
  target_ids:
  - CultureMech:001806
  field_paths:
  - ingredients
  - notes
  evidence_ids:
  - record
  - dsm-recipe
  - api666a-attempt
  - historical-context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml
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
  issue_key: cm001806-stock-stage-labeling
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Stock treatment is not labeled as a distinct preparation stage
  description: The second AUTOCLAVE step contains a full rumen-fluid workflow but
    lacks the source subsection label and receiving-stock connection. Its 121°C/15
    min, centrifugation, vial fill and frozen storage must not be transferred to the
    basal medium.
  target_ids:
  - CultureMech:001806
  field_paths:
  - preparation_steps[1]
  evidence_ids:
  - record
  - dsm-recipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: preparation-stage-boundary
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Represent the 400 mL batch input in a structured stock descriptor and
    attach the embedded clarified-fluid preparation without importing medium 1310
    basal conditions.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml
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
  description: Restore solvent context and exact source evidence, distinguishing batch
    masses from rates whose denominator still requires source/version verification.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml
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
  description: Label or structure the clarified-fluid stage and preserve all existing
    source-supported prose; keep the unspecified main autoclave cycle unresolved.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml
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
- The exact MediaDive 666a API request returned HTTP 503. Current DSM PDF content
  is available and assessed separately; historical API g_l values and raw digest claims
  cannot be authenticated from this failed response.
- The PDF was read both as extracted text and as its rendered single page. The strengths
  and addition volumes of the late cellobiose, yeast-extract, cysteine and DTT stocks
  are not supplied; the 400 mL clarified-rumen-fluid addition is explicitly supplied.
  Final-volume makeup and measured growth are not supplied. The historical API response
  digest remains a recorded claim, not authenticated current raw content.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-053
- generated-medium
```
