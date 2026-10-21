# Source and formulation review: anaerotignum_neopropionicum_medium (CultureMech:001418)

- Review: 20261021T155011Z-culturemech-001418-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T15:43:32Z
- Finished UTC: 2026-10-21T15:50:11Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSMZ 318b primary defines the main recipe and both stock recipes, but both local layers flatten trace and tenfold vitamin stocks into final ingredients, sum distinct main/stock salts, and encode ethanol volume as mass. Preparation text preserves important stage conditions. Nickel hydrate and sodium resazurin grounding need correction. Current MediaDive accession/payload verification remains unavailable after two preserved HTTP503 responses, so this full-scope review is partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 278; batch 028 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-seven task batches contain 270 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 273 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001418 | data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml | generated | anaerotignum_neopropionicum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001418 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001418 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch028/278/strict.tsv |
| validate-terms | passed | True | CultureMech:001418 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001418 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001418 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive318bapi | unavailable | True | CultureMech:001418 | The exact asserted MediaDive318b API returned HTTP503 on the original attempt and separately captured retry. Current provider accession/content and the origin of local normalized values are not authenticated. The exact DSMZ318b primary remains available and supports the bounded main/stock scientific comparison; derivative dated reports do not replace missing raw provider evidence. |
| Exact source content access: mediadive318bapi_retry | unavailable | True | CultureMech:001418 | The exact asserted MediaDive318b API returned HTTP503 on the original attempt and separately captured retry. Current provider accession/content and the origin of local normalized values are not authenticated. The exact DSMZ318b primary remains available and supports the bounded main/stock scientific comparison; derivative dated reports do not replace missing raw provider evidence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001418.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:001418.

31 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 31/33 primary and 29/33 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 33: primary 93.94%; secondary 87.88%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001418.

19 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Collection identity and current provider correspondence

identity: concern. Targets: CultureMech:001418.

The exact DSMZ 318b PDF names this recipe and defines its stocks directly. MediaDive medium318b is asserted locally, but both current API attempts returned HTTP503; exact provider identity/content and the provenance of normalized main numbers cannot be authenticated from a derivative local report. No sibling or whole parent medium318/120 formulation is transferred.

### Classification and biological claim boundaries

scope: supported. Targets: CultureMech:001418.

Yeast extract and Trypticase support complex/undefined classification. The source contains no agar and supports a liquid preparation. The title and bacterial catalog category are not a strain-specific growth test; the local generic cultivation application adds no organism or optimum claim. There are no asserted DOI/PMID, organism taxon or historical legacy MIM identifier fields. Source references to media318 and120 identify the stock recipes printed within this exact primary, not uninspected whole-medium transfers.

### Retained preparation and stage-qualified limits

completeness: concern. Targets: CultureMech:001418.

Both layers retain the full main preparation paragraph and the trace-stock preparation paragraph. Those values need evidence and explicit association with their correct stock/main stage, not invented replacements. Main pH7.0 and conditional final7.0–7.2 are distinct from trace pH6.5. Autoclave time/temperature, gas flow, later ethanol/cysteine/sulfide stock strengths, and pH-adjuster doses are not quantified by the source.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001418.

57 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "label": "Potassium dihydrogen phosphate",
    "decision": "correct",
    "source_stage": "Main source batch / named stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.29615",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.29615",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, exact named row",
        "exact_source_quote": "KH2PO4 0.30 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Restore the exact source batch quantity and its explicit unit. The local main G_PER_L value is not an authenticated measured final concentration; current API requests failed and no final batch volume is printed.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q2",
    "label": "Main sodium chloride",
    "decision": "correct",
    "source_stage": "Main source batch / named stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5923",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5923",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, exact named row",
        "exact_source_quote": "NaCl 0.60 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Restore the exact source batch quantity and its explicit unit. The local main G_PER_L value is not an authenticated measured final concentration; current API requests failed and no final batch volume is printed. The local value also sums a main contribution with an undiluted trace-stock contribution; split the two stages.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q3",
    "label": "Main magnesium chloride hexahydrate",
    "decision": "correct",
    "source_stage": "Main source batch / named stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.0987167",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.0987167",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, exact named row",
        "exact_source_quote": "MgCl2 x 6 H2O 0.10 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Restore the exact source batch quantity and its explicit unit. The local main G_PER_L value is not an authenticated measured final concentration; current API requests failed and no final batch volume is printed.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q4",
    "label": "Main calcium chloride dihydrate",
    "decision": "correct",
    "source_stage": "Main source batch / named stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1789733",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1789733",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, exact named row",
        "exact_source_quote": "CaCl2 x 2 H2O 0.08 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Restore the exact source batch quantity and its explicit unit. The local main G_PER_L value is not an authenticated measured final concentration; current API requests failed and no final batch volume is printed. The local value also sums a main contribution with an undiluted trace-stock contribution; split the two stages.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q5",
    "label": "Ammonium chloride",
    "decision": "correct",
    "source_stage": "Main source batch / named stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.987167",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.987167",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, exact named row",
        "exact_source_quote": "NH4Cl 1.00 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Restore the exact source batch quantity and its explicit unit. The local main G_PER_L value is not an authenticated measured final concentration; current API requests failed and no final batch volume is printed.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q6",
    "label": "Yeast extract",
    "decision": "correct",
    "source_stage": "Main source batch / named stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.493583",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.493583",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, exact named row",
        "exact_source_quote": "Yeast extract (OXOID) 0.50 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Restore the exact source batch quantity and its explicit unit. The local main G_PER_L value is not an authenticated measured final concentration; current API requests failed and no final batch volume is printed.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q7",
    "label": "Trypticase peptone",
    "decision": "correct",
    "source_stage": "Main source batch / named stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.493583",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.493583",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, exact named row",
        "exact_source_quote": "Trypticase peptone (BD BBL) 0.50 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Restore the exact source batch quantity and its explicit unit. The local main G_PER_L value is not an authenticated measured final concentration; current API requests failed and no final batch volume is printed.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q8",
    "label": "Sodium resazurin stock dose",
    "decision": "correct",
    "source_stage": "Main source batch / named stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.000493583",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.000493583",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, exact named row",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Represent 0.50 ml of 0.1% w/v sodium resazurin as a stock dose. Conditional delivered dye mass is 0.50 mg, not an authenticated final concentration; preserve the sodium salt.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q9",
    "label": "Potassium bicarbonate",
    "decision": "correct",
    "source_stage": "Main source batch / named stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3.94867",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3.94867",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, exact named row",
        "exact_source_quote": "KHCO3 4.00 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Restore the exact source batch quantity and its explicit unit. The local main G_PER_L value is not an authenticated measured final concentration; current API requests failed and no final batch volume is printed.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q10",
    "label": "Ethanol volume",
    "decision": "correct",
    "source_stage": "Main source batch / named stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, exact named row",
        "exact_source_quote": "Ethanol 1.30 ml",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Source 1.30 ml is ethanol volume, not 1.3 g/L. Do not infer a density or convert to a measured final concentration.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q11",
    "label": "L-cysteine hydrochloride monohydrate",
    "decision": "correct",
    "source_stage": "Main source batch / named stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.29615",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.29615",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, exact named row",
        "exact_source_quote": "L-Cysteine HCl x H2O 0.30 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Restore the exact source batch quantity and its explicit unit. The local main G_PER_L value is not an authenticated measured final concentration; current API requests failed and no final batch volume is printed.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q12",
    "label": "Sodium sulfide nonahydrate",
    "decision": "correct",
    "source_stage": "Main source batch / named stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.29615",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.29615",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, exact named row",
        "exact_source_quote": "Na2S x 9 H2O 0.30 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Restore the exact source batch quantity and its explicit unit. The local main G_PER_L value is not an authenticated measured final concentration; current API requests failed and no final batch volume is printed.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q13",
    "label": "NTA",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "12.8",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "12.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "Nitrilotriacetic acid (NTA) 12.80 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q14",
    "label": "Iron dichloride tetrahydrate",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "FeCl2 x 4 H2O 1.00 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q15",
    "label": "Manganese chloride tetrahydrate",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "MnCl2 x 4 H2O 0.10 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q16",
    "label": "Cobalt chloride hexahydrate",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "CoCl2 x 6 H2O 0.03 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q17",
    "label": "Trace calcium chloride dihydrate",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1789733",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1789733",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "CaCl2 x 2 H2O 0.10 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q18",
    "label": "Zinc chloride",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "ZnCl2 0.10 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q19",
    "label": "Copper chloride",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "CuCl2 0.02 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q20",
    "label": "Boric acid",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "H3BO3 0.01 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q21",
    "label": "Sodium molybdate dihydrate",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.03 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q22",
    "label": "Nickel chloride hexahydrate",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "NiCl2 x 6 H2O 0.10 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q23",
    "label": "Trace sodium chloride",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5923",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5923",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "NaCl 1.00 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q24",
    "label": "Sodium selenite pentahydrate",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "Na2SeO3 x 5 H2O 0.03 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q25",
    "label": "Sodium tungstate dihydrate",
    "decision": "correct",
    "source_stage": "Trace element stock, not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.04",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.04",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 trace element solution table, exact named row",
        "exact_source_quote": "Na2WO4 x 2 H2O 0.04 g",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "This mass belongs to the trace stock made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original mass/form and stock stage; the current flat main value is not this delivered contribution. Main/stock duplicate sums must be separated.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q26",
    "label": "Biotin",
    "decision": "correct",
    "source_stage": "Wolin vitamin stock (10x), not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 Wolin tenfold vitamin table, exact named row",
        "exact_source_quote": "Biotin 20.00 mg",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "The local number is a vitamin-stock strength promoted to a main concentration. Preserve the source milligram quantity per listed 1000 ml stock water, the tenfold formulation identity and the separate 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit source table.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q27",
    "label": "Folic acid",
    "decision": "correct",
    "source_stage": "Wolin vitamin stock (10x), not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 Wolin tenfold vitamin table, exact named row",
        "exact_source_quote": "Folic acid 20.00 mg",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "The local number is a vitamin-stock strength promoted to a main concentration. Preserve the source milligram quantity per listed 1000 ml stock water, the tenfold formulation identity and the separate 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit source table.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q28",
    "label": "Pyridoxine hydrochloride",
    "decision": "correct",
    "source_stage": "Wolin vitamin stock (10x), not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 Wolin tenfold vitamin table, exact named row",
        "exact_source_quote": "Pyridoxine hydrochloride 100.00 mg",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "The local number is a vitamin-stock strength promoted to a main concentration. Preserve the source milligram quantity per listed 1000 ml stock water, the tenfold formulation identity and the separate 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit source table.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q29",
    "label": "Thiamine HCl",
    "decision": "correct",
    "source_stage": "Wolin vitamin stock (10x), not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 Wolin tenfold vitamin table, exact named row",
        "exact_source_quote": "Thiamine HCl 50.00 mg",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "The local number is a vitamin-stock strength promoted to a main concentration. Preserve the source milligram quantity per listed 1000 ml stock water, the tenfold formulation identity and the separate 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit source table.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q30",
    "label": "Riboflavin",
    "decision": "correct",
    "source_stage": "Wolin vitamin stock (10x), not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 Wolin tenfold vitamin table, exact named row",
        "exact_source_quote": "Riboflavin 50.00 mg",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "The local number is a vitamin-stock strength promoted to a main concentration. Preserve the source milligram quantity per listed 1000 ml stock water, the tenfold formulation identity and the separate 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit source table.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q31",
    "label": "Nicotinic acid",
    "decision": "correct",
    "source_stage": "Wolin vitamin stock (10x), not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 Wolin tenfold vitamin table, exact named row",
        "exact_source_quote": "Nicotinic acid 50.00 mg",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "The local number is a vitamin-stock strength promoted to a main concentration. Preserve the source milligram quantity per listed 1000 ml stock water, the tenfold formulation identity and the separate 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit source table.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q32",
    "label": "Calcium D-(+)-pantothenate",
    "decision": "correct",
    "source_stage": "Wolin vitamin stock (10x), not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 Wolin tenfold vitamin table, exact named row",
        "exact_source_quote": "Calcium D-(+)-pantothenate 50.00 mg",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "The local number is a vitamin-stock strength promoted to a main concentration. Preserve the source milligram quantity per listed 1000 ml stock water, the tenfold formulation identity and the separate 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit source table.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q33",
    "label": "Vitamin B12",
    "decision": "correct",
    "source_stage": "Wolin vitamin stock (10x), not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 Wolin tenfold vitamin table, exact named row",
        "exact_source_quote": "Vitamin B12 1.00 mg",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "The local number is a vitamin-stock strength promoted to a main concentration. Preserve the source milligram quantity per listed 1000 ml stock water, the tenfold formulation identity and the separate 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit source table.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q34",
    "label": "p-Aminobenzoic acid",
    "decision": "correct",
    "source_stage": "Wolin vitamin stock (10x), not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 Wolin tenfold vitamin table, exact named row",
        "exact_source_quote": "p-Aminobenzoic acid 50.00 mg",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "The local number is a vitamin-stock strength promoted to a main concentration. Preserve the source milligram quantity per listed 1000 ml stock water, the tenfold formulation identity and the separate 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit source table.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q35",
    "label": "(DL)-alpha-Lipoic acid",
    "decision": "correct",
    "source_stage": "Wolin vitamin stock (10x), not main medium",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 Wolin tenfold vitamin table, exact named row",
        "exact_source_quote": "(DL)-alpha-Lipoic acid 50.00 mg",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "The local number is a vitamin-stock strength promoted to a main concentration. Preserve the source milligram quantity per listed 1000 ml stock water, the tenfold formulation identity and the separate 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit source table.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q36",
    "label": "Main trace-stock addition",
    "decision": "add",
    "source_stage": "Page1 main table",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table",
        "exact_source_quote": "Trace element solution 10.00 ml",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Add the explicit 10 ml trace-stock dose and an inline or verified stock recipe; no main-stock solution object is currently present.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q37",
    "label": "Main tenfold-vitamin addition",
    "decision": "add",
    "source_stage": "Page1 main table",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table",
        "exact_source_quote": "Wolin's vitamin solution (10x) 1.00 ml",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Add the explicit 1 ml dose of the printed tenfold stock, separate from its constituent strengths.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q38",
    "label": "Tenfold stock identity",
    "decision": "add",
    "source_stage": "Page2 vitamin heading",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 vitamin heading",
        "exact_source_quote": "Wolin's vitamin solution (10x) (from medium 120)",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Retain the 10x stock designation without guessing a parent whole-medium formulation or multiplying its printed masses again.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q39",
    "label": "Resazurin stock strength",
    "decision": "add",
    "source_stage": "Page1 main table",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[7].preferred_term",
        "stored": "Sodium resazurin"
      },
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.000493583",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[7].preferred_term",
        "stored": "Sodium resazurin"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.000493583",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Add the explicit 0.1% w/v stock basis. Arithmetic: 0.1 g/100 ml equals 1 mg/ml; 0.50 ml delivers 0.50 mg, without a measured final-medium denominator.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q40",
    "label": "Main water preparation amount",
    "decision": "add",
    "source_stage": "Main batch water",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main table, water before main preparation",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Preserve 1000 ml water as a main-batch preparation input, not an assumed final makeup and not a main mass ingredient.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q41",
    "label": "Trace stock water/final makeup",
    "decision": "evidence_only",
    "source_stage": "Trace stock final makeup",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 trace-stock preparation final sentence",
        "exact_source_quote": "mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "The exact 1000 ml final makeup is already in the local preparation description. Attach evidence and associate this existing field with the trace stock; do not claim it is absent or a main-medium final volume.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q42",
    "label": "Vitamin-stock water",
    "decision": "add",
    "source_stage": "Wolin10x stock water",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 vitamin table final row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Add the listed 1000 ml vitamin-stock water context. It does not create an extra 1000 ml main dose.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q43",
    "label": "Main gas mixture during sparging",
    "decision": "evidence_only",
    "source_stage": "Page1 first preparation sentence",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 first preparation sentence",
        "exact_source_quote": "sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Existing main preparation retains the 80% N2 / 20% CO2 gas mixture. Percentage basis is not explicitly printed; do not add a v/v qualifier.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q44",
    "label": "Main sparging time",
    "decision": "evidence_only",
    "source_stage": "Page1 first preparation sentence",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 first preparation sentence",
        "exact_source_quote": "sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Existing main preparation retains 30–45 minutes; no gas flow is supplied.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q45",
    "label": "Main pH before dispensing",
    "decision": "evidence_only",
    "source_stage": "Page1 preparation after sparging",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 preparation after sparging",
        "exact_source_quote": "Add and dissolve bicarbonate and adjust pH to 7.0",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Existing preparation retains pH 7.0 at this main-medium stage; it is not trace-stock pH 6.5.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q46",
    "label": "Main dispensing gas mixture",
    "decision": "evidence_only",
    "source_stage": "Page1 preparation dispensing clause continuing on next line",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 preparation dispensing clause continuing on next line",
        "exact_source_quote": "then dispense under 80% N2 and 20%",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Existing preparation retains the separate 80% N2 / 20% CO2 dispensing atmosphere. The full adjacent source line completes CO2; no source text is changed or gas flow invented.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q47",
    "label": "Later ethanol/cysteine/sulfide gas",
    "decision": "evidence_only",
    "source_stage": "Page1 post-sterilization stock clause",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 post-sterilization stock clause",
        "exact_source_quote": "sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared\nunder 100% N2 gas.",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "The existing preparation retains 100% N2 for these late stocks separately from main 80:20 gas.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q48",
    "label": "Vitamin-stock gas",
    "decision": "evidence_only",
    "source_stage": "Page1 vitamin preparation clause",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 vitamin preparation clause",
        "exact_source_quote": "Vitamins are prepared under 100% N2 gas and sterilized by filtration.",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Existing preparation retains the separate 100% N2 vitamin stock atmosphere and filtration.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q49",
    "label": "Conditional complete-medium pH",
    "decision": "evidence_only",
    "source_stage": "Page1 final preparation sentence",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.0,
          "max": 7.2
        }
      },
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.0,
          "max": 7.2
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 final preparation sentence",
        "exact_source_quote": "Adjust pH of complete medium to 7.0 - 7.2, if necessary.",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Both the numeric range and conditional preparation wording are retained correctly. Attach supporting evidence; do not claim this value or its condition is absent.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q50",
    "label": "Trace initial water",
    "decision": "evidence_only",
    "source_stage": "Page2 trace-stock first sentence",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 trace-stock first sentence",
        "exact_source_quote": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Existing 200 ml is an initial stock solvent amount before final makeup, not an additional main ingredient or final stock volume.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q51",
    "label": "Trace initial pH",
    "decision": "evidence_only",
    "source_stage": "Page2 trace-stock first sentence",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 trace-stock first sentence",
        "exact_source_quote": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Existing initial stock pH 6.5 is source-supported, separate from main pH.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q52",
    "label": "Trace final pH",
    "decision": "evidence_only",
    "source_stage": "Page2 trace-stock final sentence",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 trace-stock final sentence",
        "exact_source_quote": "mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Existing final stock pH 6.5 is a second source stage, with a separately stated 1000 ml makeup.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q53",
    "label": "Trace KOH dose",
    "decision": "not_quantified",
    "source_stage": "Page2 trace-stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page2 trace-stock preparation",
        "exact_source_quote": "mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "KOH identity and endpoint are explicit; no mass, molarity or added volume is specified.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q54",
    "label": "Later stock strengths and volumes",
    "decision": "not_quantified",
    "source_stage": "Page1 post-sterilization clause",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 post-sterilization clause",
        "exact_source_quote": "sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Main ethanol volume and cysteine/sulfide batch masses are given in the table, but the later source-stock strengths and delivery volumes are not. Do not infer them from the main amounts.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q55",
    "label": "Main autoclave cycle",
    "decision": "not_quantified",
    "source_stage": "Page1 dispensing/autoclaving clause",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 dispensing/autoclaving clause",
        "exact_source_quote": "CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Autoclaving is stated, but no temperature or duration is supplied; do not borrow a collection default.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q56",
    "label": "Main pH adjustment reagent/dose",
    "decision": "not_quantified",
    "source_stage": "Page1 main pH clause",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add ethanol, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main pH clause",
        "exact_source_quote": "Add and dissolve bicarbonate and adjust pH to 7.0",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "No separate titrant identity or dose is printed for the main pH adjustment. Trace KOH is not automatically the main titrant.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  },
  {
    "decision_id": "q57",
    "label": "Measured main final volume",
    "decision": "not_quantified",
    "source_stage": "Page1 main water row and explicit main stock additions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz318b",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf",
        "source_locator": "Page1 main water row and explicit main stock additions",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe",
        "parsed_text_sha256": "894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5"
      }
    ],
    "interpretation": "Listed liquids sum 1000 + 10 + 0.5 + 1.3 + 1 = 1012.8 ml before any unquantified later stock delivery/titrant volumes. This is not a measured final-volume statement. The local values resemble normalization to roughly 1013 ml, but no current API payload authenticates that basis.",
    "local_evidence_status": "No claim-level supporting evidence attached in either inspected layer; matching retained values are evidence_only, not verified."
  }
]

### Maintained source and generated follow-up

ownership: supported. Targets: CultureMech:001418.

The one normalized owner is the maintained correction surface. Its full bytes match the generated formulation, while the target adds merge metadata. Current importer/cleanup/merge code is context rather than historical causation evidence. No recipe, history, generated page or review bundle was changed.

## Findings

### f1: Trace and vitamin stock strengths are represented as main-medium amounts

blocker / open / confirmed; issue key: cm001418-flattened-stock-formulation.

Both layers flatten thirteen trace-stock solutes and ten tenfold-vitamin solutes into main ingredients, omitting the 10 ml and 1 ml stock doses. Sodium chloride and calcium chloride additionally sum contributions from different stages; the stored duplicate notes expose those sums. This materially changes the recipe even though the schema is valid.

### f2: Ethanol, indicator dose and main normalization lose source units or basis

major / open / confirmed; issue key: cm001418-volume-and-final-basis.

Source ethanol is 1.30 ml, not 1.3 g/L; sodium resazurin is a 0.50 ml dose of 0.1% w/v stock. The main recipe lists 1000 ml water without an explicit measured final volume, while several local main values are normalized to an unauthenticated denominator. Neither density nor final-volume correction is established by current source evidence.

### f3: Nickel hydrate and sodium resazurin do not match their asserted structures

major / open / confirmed; issue key: cm001418-chemical-form-mismatches.

Nickel chloride hexahydrate is mapped to anhydrous CHEBI:34887 in both primary and secondary slots. Sodium resazurin is mapped to neutral CHEBI:8806, which has no sodium counterion. In contrast, the calcium pantothenate structure is compatible with the source D-(+) qualifier, and non-stereospecific lipoic acid does not establish a false conflict with the source DL wording.

### f4: Retained amounts and preparation lack narrow supporting evidence

minor / open / confirmed; issue key: cm001418-claim-evidence.

Source URLs and import history are present, but no target/owner claim-level evidence supports concentration, stock scope or the otherwise retained preparation. The dated local review report remains derivative context and cannot authenticate missing MediaDive raw bytes.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the main recipe and the two explicit stock stages in the normalized owner. Split main/stock salt contributions, retain each stock batch and dose, and associate the already retained trace preparation with that stock. Regenerate only after source-backed correction.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the exact main batch amounts, ethanol volume and resazurin stock dose/strength. Qualify any nominal normalization and retain unresolved final-volume/density limits; do not compute new exact final concentrations without evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Reassess exact supplied-form mappings using primary labels and verified structures. Preserve source hydrate/salt/stereochemical wording and leave unresolved replacements unassigned; do not replace correctly compatible forms based on generic label appearance alone.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach exact current primary excerpts at the repaired or retained claim layer, preserving source stages and capture metadata. Keep the historical report and old history unchanged; append later authorized curation events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch028/278/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch028/278/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml:1:id: CultureMech:001418<br>./data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml:1:id: CultureMech:001418<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch028/source-preflight-bound/278/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 34 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf; Both complete PDF pages; main table, main preparation, trace stock and tenfold vitamin stock | supports | The exact collection document independently supports DSMZ 318b identity and all three source stages. Both PDF pages were visually inspected. |
| trace-dose | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf; Page1 main table, trace stock addition | supports | The main recipe adds 10 ml of the separately defined trace stock. |
| vitamin-dose | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf; Page1 main table, vitamin stock addition | supports | The main recipe adds 1 ml of the explicitly tenfold Wolin stock. |
| trace-stock | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf; Page1 trace table; page2 stock preparation | supports | The thirteen trace solutes are stock quantities, with explicit final makeup to 1000 ml. Main sodium chloride and calcium chloride remain separate. |
| vitamin-stock | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf; Page2 complete tenfold vitamin table | supports | Ten vitamin masses are specified for the listed 1000 ml stock water; they are not undiluted main concentrations. |
| ethanol | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf; Page1 main table, ethanol row | supports | The source specifies 1.30 ml ethanol, with no density supplied to justify a mass conversion. |
| resazurin | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf; Page1 main table, indicator row | supports | The source specifies 0.50 ml of 0.1% w/v sodium resazurin stock. |
| prep | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf; Page1 main preparation paragraph | supports | The existing local paragraph preserves the main gas mixture, timing, staged additions, later stock gas, vitamin filtration and conditional final pH. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16236 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16236; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16236 resolves to ethanol. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49553 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49553; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49553 resolves to copper(II) chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi81862 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_81862; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:81862 resolves to potassium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16236": [{"label": "Ethanol", "match_type": "preferred_term", "identifier": "CHEBI:16236", "preferred_term": "Ethanol", "ontology_id": "CHEBI:16236", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49553": [{"label": "CuCl2", "match_type": "preferred_term", "identifier": "CHEBI:49553", "preferred_term": "CuCl2", "ontology_id": "CHEBI:49553", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:81862": [{"label": "KHCO3", "match_type": "preferred_term", "identifier": "CHEBI:81862", "preferred_term": "KHCO3", "ontology_id": "CHEBI:81862", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml; data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml", "events": 9, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current primary-only composition and stock extraction, current duplicate handling and merge guards read. The current cleanup does not sum disagreeing duplicates; historical summed values are established by the actual stored notes, not attributed to a replay of current code. No writer was executed. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current primary-only composition and stock extraction, current duplicate handling and merge guards read. The current cleanup does not sum disagreeing duplicates; historical summed values are established by the actual stored notes, not attributed to a replay of current code. No writer was executed. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current primary-only composition and stock extraction, current duplicate handling and merge guards read. The current cleanup does not sum disagreeing duplicates; historical summed values are established by the actual stored notes, not attributed to a replay of current code. No writer was executed. |
| historical-report | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/anaerotignum_neopropionicum_medium.yaml.md; Complete dated local concentration-review table; preserved conflict/not-asserted rows | context_only | The local dated report records stock-topology conflicts and unavailable historical source assertions. It is derivative local context, not a substitute for original MediaDive raw bytes. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch028/278/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| mediadive318bapi-attempt | https://mediadive.dsmz.de/rest/medium/318b; Preserved exact public retrieval result | context_only | The exact asserted MediaDive318b API returned HTTP503 on the original attempt and separately captured retry. Current provider accession/content and the origin of local normalized values are not authenticated. The exact DSMZ318b primary remains available and supports the bounded main/stock scientific comparison; derivative dated reports do not replace missing raw provider evidence. |
| mediadive318bapi_retry-attempt | https://mediadive.dsmz.de/rest/medium/318b; Preserved exact public retrieval result | context_only | The exact asserted MediaDive318b API returned HTTP503 on the original attempt and separately captured retry. Current provider accession/content and the origin of local normalized values are not authenticated. The exact DSMZ318b primary remains available and supports the bounded main/stock scientific comparison; derivative dated reports do not replace missing raw provider evidence. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact asserted MediaDive318b API returned HTTP503 on the original attempt and separately captured retry. Current provider accession/content and the origin of local normalized values are not authenticated. The exact DSMZ318b primary remains available and supports the bounded main/stock scientific comparison; derivative dated reports do not replace missing raw provider evidence.
- The exact asserted MediaDive318b API returned HTTP503 on the original attempt and separately captured retry. Current provider accession/content and the origin of local normalized values are not authenticated. The exact DSMZ318b primary remains available and supports the bounded main/stock scientific comparison; derivative dated reports do not replace missing raw provider evidence.
- Source-only stock recipes printed inside DSMZ318b were read in full; no separate whole parent DSMZ318 or DSMZ120 recipe, growth phenotype or historical provider equivalence is inferred. All quoted source table units remain original; derived arithmetic is separately labeled.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T155011Z-culturemech-001418-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerotignum_neopropionicum_medium (CultureMech:001418)'
started_at: '2026-10-21T15:43:32Z'
finished_at: '2026-10-21T15:50:11Z'
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
summary: The exact DSMZ 318b primary defines the main recipe and both stock recipes,
  but both local layers flatten trace and tenfold vitamin stocks into final ingredients,
  sum distinct main/stock salts, and encode ethanol volume as mass. Preparation text
  preserves important stage conditions. Nickel hydrate and sodium resazurin grounding
  need correction. Current MediaDive accession/payload verification remains unavailable
  after two preserved HTTP503 responses, so this full-scope review is partial.
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
  - path: data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml
    sha256: 69230f0b13e0d7108f6acc0ff9c1431fa0fd3e138d74fc5423ee02937b78dce0
    role: target
  - path: data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml
    sha256: 12007ede449c22fe78c9bd2e700151bc0d4f13d260b3c3e89b5b2786b769cbff
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/anaerotignum_neopropionicum_medium.yaml.md
    sha256: 6c05972a3f8db012f34ba8feae03c77f56553e257f0b061da3fb64d76cde848d
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
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
    sha256: 64a778108fd3197a8cc08082f80c1de3ec33eda58350cee5df612ab61d23cea1
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 278; batch 028 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-seven task batches
    contain 270 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 273 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001418
targets:
- target_id: CultureMech:001418
  path: data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml
  label: anaerotignum_neopropionicum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch028/278/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch028/278/strict.tsv"
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001418
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
  - CultureMech:001418
- check_id: mediadive318bapi-source-access
  name: 'Exact source content access: mediadive318bapi'
  required: true
  status: unavailable
  summary: The exact asserted MediaDive318b API returned HTTP503 on the original attempt
    and separately captured retry. Current provider accession/content and the origin
    of local normalized values are not authenticated. The exact DSMZ318b primary remains
    available and supports the bounded main/stock scientific comparison; derivative
    dated reports do not replace missing raw provider evidence.
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - mediadive318bapi-attempt
- check_id: mediadive318bapi_retry-source-access
  name: 'Exact source content access: mediadive318bapi_retry'
  required: true
  status: unavailable
  summary: The exact asserted MediaDive318b API returned HTTP503 on the original attempt
    and separately captured retry. Current provider accession/content and the origin
    of local normalized values are not authenticated. The exact DSMZ318b primary remains
    available and supports the bounded main/stock scientific comparison; derivative
    dated reports do not replace missing raw provider evidence.
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - mediadive318bapi_retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T15:50:10Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:50:10Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:44:15.836187Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch028/278/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T15:44:17.160311Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch028/278/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:44:18.811773Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:44:19.862974Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T15:50:10Z'
  support: supports
  summary: './data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml:1:id:
    CultureMech:001418

    ./data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml:1:id:
    CultureMech:001418

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/source-preflight-bound/278/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T15:50:10Z'
  support: supports
  summary: 34 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 5742efa5f808122089fbec6350c0809a1f0a9694ab49778f9fc319181f9b6ee3
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf
  locator: Both complete PDF pages; main table, main preparation, trace stock and
    tenfold vitamin stock
  accessed_at: '2026-10-21T15:28:31.130022Z'
  support: supports
  summary: The exact collection document independently supports DSMZ 318b identity
    and all three source stages. Both PDF pages were visually inspected.
  quote: '318b: ANAEROTIGNUM NEOPROPIONICUM MEDIUM'
  snapshot_sha256: 6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe
- evidence_id: trace-dose
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf
  locator: Page1 main table, trace stock addition
  accessed_at: '2026-10-21T15:28:31.130022Z'
  support: supports
  summary: The main recipe adds 10 ml of the separately defined trace stock.
  quote: Trace element solution 10.00 ml
  snapshot_sha256: 6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe
- evidence_id: vitamin-dose
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf
  locator: Page1 main table, vitamin stock addition
  accessed_at: '2026-10-21T15:28:31.130022Z'
  support: supports
  summary: The main recipe adds 1 ml of the explicitly tenfold Wolin stock.
  quote: Wolin's vitamin solution (10x) 1.00 ml
  snapshot_sha256: 6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe
- evidence_id: trace-stock
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf
  locator: Page1 trace table; page2 stock preparation
  accessed_at: '2026-10-21T15:28:31.130022Z'
  support: supports
  summary: The thirteen trace solutes are stock quantities, with explicit final makeup
    to 1000 ml. Main sodium chloride and calcium chloride remain separate.
  quote: mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.
  snapshot_sha256: 6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe
- evidence_id: vitamin-stock
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf
  locator: Page2 complete tenfold vitamin table
  accessed_at: '2026-10-21T15:28:31.130022Z'
  support: supports
  summary: Ten vitamin masses are specified for the listed 1000 ml stock water; they
    are not undiluted main concentrations.
  quote: Wolin's vitamin solution (10x) (from medium 120)
  snapshot_sha256: 6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe
- evidence_id: ethanol
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf
  locator: Page1 main table, ethanol row
  accessed_at: '2026-10-21T15:28:31.130022Z'
  support: supports
  summary: The source specifies 1.30 ml ethanol, with no density supplied to justify
    a mass conversion.
  quote: Ethanol 1.30 ml
  snapshot_sha256: 6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe
- evidence_id: resazurin
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf
  locator: Page1 main table, indicator row
  accessed_at: '2026-10-21T15:28:31.130022Z'
  support: supports
  summary: The source specifies 0.50 ml of 0.1% w/v sodium resazurin stock.
  quote: Sodium resazurin (0.1% w/v) 0.50 ml
  snapshot_sha256: 6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe
- evidence_id: prep
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf
  locator: Page1 main preparation paragraph
  accessed_at: '2026-10-21T15:28:31.130022Z'
  support: supports
  summary: The existing local paragraph preserves the main gas mixture, timing, staged
    additions, later stock gas, vitamin filtration and conditional final pH.
  quote: sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make
    it anoxic.
  snapshot_sha256: 6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe
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
- evidence_id: chebi16236
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16236
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T10:07:16.961534Z'
  support: supports
  summary: CHEBI:16236 resolves to ethanol. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: afdacc5e401c6545f51974e897eb96eee2a5fa3aef15119edbd415cb7bb802b8
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
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
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
- evidence_id: chebi49553
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49553
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T10:07:17.608864Z'
  support: supports
  summary: CHEBI:49553 resolves to copper(II) chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 55d84961ae8c483bc2364cb9c5f159267161b61a3c77c93632021c6f4ea1810d
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to zinc dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
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
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
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
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi81862
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_81862
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T15:28:31.974482Z'
  support: supports
  summary: CHEBI:81862 resolves to potassium hydrogencarbonate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 2c3d1a8e50c12252fd027778aa005ce1a5a8d1be8868178c3353a83505684051
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
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
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
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
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
  accessed_at: '2026-10-21T15:50:10Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid",
    "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term":
    "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term",
    "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16236": [{"label":
    "Ethanol", "match_type": "preferred_term", "identifier": "CHEBI:16236", "preferred_term":
    "Ethanol", "ontology_id": "CHEBI:16236", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic
    acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term",
    "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label":
    "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label":
    "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961":
    [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier":
    "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label":
    "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term":
    "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label":
    "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id":
    "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105":
    [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:49553": [{"label": "CuCl2", "match_type":
    "preferred_term", "identifier": "CHEBI:49553", "preferred_term": "CuCl2", "ontology_id":
    "CHEBI:49553", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976":
    [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976",
    "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate",
    "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939":
    [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:81862":
    [{"label": "KHCO3", "match_type": "preferred_term", "identifier": "CHEBI:81862",
    "preferred_term": "KHCO3", "ontology_id": "CHEBI:81862", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O",
    "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label":
    "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345",
    "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368":
    [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x
    H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term":
    "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml; data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T15:50:10Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml", "events":
    9, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T15:50:10Z'
  support: context_only
  summary: Current primary-only composition and stock extraction, current duplicate
    handling and merge guards read. The current cleanup does not sum disagreeing duplicates;
    historical summed values are established by the actual stored notes, not attributed
    to a replay of current code. No writer was executed.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T15:50:10Z'
  support: context_only
  summary: Current primary-only composition and stock extraction, current duplicate
    handling and merge guards read. The current cleanup does not sum disagreeing duplicates;
    historical summed values are established by the actual stored notes, not attributed
    to a replay of current code. No writer was executed.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T15:50:10Z'
  support: context_only
  summary: Current primary-only composition and stock extraction, current duplicate
    handling and merge guards read. The current cleanup does not sum disagreeing duplicates;
    historical summed values are established by the actual stored notes, not attributed
    to a replay of current code. No writer was executed.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: historical-report
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/anaerotignum_neopropionicum_medium.yaml.md
  locator: Complete dated local concentration-review table; preserved conflict/not-asserted
    rows
  accessed_at: '2026-10-21T15:50:10Z'
  support: context_only
  summary: The local dated report records stock-topology conflicts and unavailable
    historical source assertions. It is derivative local context, not a substitute
    for original MediaDive raw bytes.
  snapshot_sha256: 6c05972a3f8db012f34ba8feae03c77f56553e257f0b061da3fb64d76cde848d
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/278/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T15:50:10Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 21857bcfbc1a5adcea9148082aeec474fa8b06235372a765b9ff385b79e0923c
- evidence_id: mediadive318bapi-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/318b
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:28:29.486851Z'
  support: context_only
  summary: The exact asserted MediaDive318b API returned HTTP503 on the original attempt
    and separately captured retry. Current provider accession/content and the origin
    of local normalized values are not authenticated. The exact DSMZ318b primary remains
    available and supports the bounded main/stock scientific comparison; derivative
    dated reports do not replace missing raw provider evidence.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive318bapi_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/318b
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:29:41.663268Z'
  support: context_only
  summary: The exact asserted MediaDive318b API returned HTTP503 on the original attempt
    and separately captured retry. Current provider accession/content and the origin
    of local normalized values are not authenticated. The exact DSMZ318b primary remains
    available and supports the bounded main/stock scientific comparison; derivative
    dated reports do not replace missing raw provider evidence.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '31 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 31/33
    primary and 29/33 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131361
  - chebi15940
  - chebi15956
  - chebi16236
  - chebi16494
  - chebi17015
  - chebi176843
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi33118
  - chebi34887
  - chebi44557
  - chebi49105
  - chebi49553
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi76209
  - chebi81862
  - chebi86158
  - chebi86249
  - chebi86345
  - chebi86368
  - chebi8806
  - chebi91248
  details: 'Instance coverage on a 0–100 percent scale, denominator 33: primary 93.94%;
    secondary 87.88%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 19 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Collection identity and current provider correspondence
  outcome: concern
  summary: The exact DSMZ 318b PDF names this recipe and defines its stocks directly.
    MediaDive medium318b is asserted locally, but both current API attempts returned
    HTTP503; exact provider identity/content and the provenance of normalized main
    numbers cannot be authenticated from a derivative local report. No sibling or
    whole parent medium318/120 formulation is transferred.
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - record
  - owner-0
  - primary
  - historical-report
- assessment_id: classification
  area: scope
  topic: Classification and biological claim boundaries
  outcome: supported
  summary: Yeast extract and Trypticase support complex/undefined classification.
    The source contains no agar and supports a liquid preparation. The title and bacterial
    catalog category are not a strain-specific growth test; the local generic cultivation
    application adds no organism or optimum claim. There are no asserted DOI/PMID,
    organism taxon or historical legacy MIM identifier fields. Source references to
    media318 and120 identify the stock recipes printed within this exact primary,
    not uninspected whole-medium transfers.
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - record
  - owner-0
  - primary
- assessment_id: preparation
  area: completeness
  topic: Retained preparation and stage-qualified limits
  outcome: concern
  summary: Both layers retain the full main preparation paragraph and the trace-stock
    preparation paragraph. Those values need evidence and explicit association with
    their correct stock/main stage, not invented replacements. Main pH7.0 and conditional
    final7.0–7.2 are distinct from trace pH6.5. Autoclave time/temperature, gas flow,
    later ethanol/cysteine/sulfide stock strengths, and pH-adjuster doses are not
    quantified by the source.
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - record
  - owner-0
  - prep
  - trace-stock
  - primary
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 57 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"label\": \"Potassium dihydrogen\
    \ phosphate\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Main source\
    \ batch / named stock dose\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\",\n      \
    \  \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.29615\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.29615\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, exact named row\",\n      \
    \  \"exact_source_quote\": \"KH2PO4 0.30 g\",\n        \"snapshot_sha256\": \"\
    6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n        \"\
    parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact source batch quantity\
    \ and its explicit unit. The local main G_PER_L value is not an authenticated\
    \ measured final concentration; current API requests failed and no final batch\
    \ volume is printed.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q2\",\n    \"label\": \"\
    Main sodium chloride\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Main source batch / named stock dose\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5923\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5923\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, exact named row\",\n      \
    \  \"exact_source_quote\": \"NaCl 0.60 g\",\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact source batch quantity\
    \ and its explicit unit. The local main G_PER_L value is not an authenticated\
    \ measured final concentration; current API requests failed and no final batch\
    \ volume is printed. The local value also sums a main contribution with an undiluted\
    \ trace-stock contribution; split the two stages.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q3\",\n    \"label\": \"Main magnesium chloride hexahydrate\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Main source batch / named stock dose\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0987167\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0987167\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, exact named row\",\n      \
    \  \"exact_source_quote\": \"MgCl2 x 6 H2O 0.10 g\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact source batch quantity\
    \ and its explicit unit. The local main G_PER_L value is not an authenticated\
    \ measured final concentration; current API requests failed and no final batch\
    \ volume is printed.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n    \"label\": \"\
    Main calcium chloride dihydrate\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Main source batch / named stock dose\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1789733\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1789733\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, exact named row\",\n      \
    \  \"exact_source_quote\": \"CaCl2 x 2 H2O 0.08 g\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact source batch quantity\
    \ and its explicit unit. The local main G_PER_L value is not an authenticated\
    \ measured final concentration; current API requests failed and no final batch\
    \ volume is printed. The local value also sums a main contribution with an undiluted\
    \ trace-stock contribution; split the two stages.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q5\",\n    \"label\": \"Ammonium chloride\",\n    \"decision\": \"correct\"\
    ,\n    \"source_stage\": \"Main source batch / named stock dose\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.987167\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.987167\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, exact named row\",\n      \
    \  \"exact_source_quote\": \"NH4Cl 1.00 g\",\n        \"snapshot_sha256\": \"\
    6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n        \"\
    parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact source batch quantity\
    \ and its explicit unit. The local main G_PER_L value is not an authenticated\
    \ measured final concentration; current API requests failed and no final batch\
    \ volume is printed.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n    \"label\": \"\
    Yeast extract\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Main\
    \ source batch / named stock dose\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.493583\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.493583\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, exact named row\",\n      \
    \  \"exact_source_quote\": \"Yeast extract (OXOID) 0.50 g\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact source batch quantity\
    \ and its explicit unit. The local main G_PER_L value is not an authenticated\
    \ measured final concentration; current API requests failed and no final batch\
    \ volume is printed.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"label\": \"\
    Trypticase peptone\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"\
    Main source batch / named stock dose\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.493583\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.493583\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, exact named row\",\n      \
    \  \"exact_source_quote\": \"Trypticase peptone (BD BBL) 0.50 g\",\n        \"\
    snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact source batch quantity\
    \ and its explicit unit. The local main G_PER_L value is not an authenticated\
    \ measured final concentration; current API requests failed and no final batch\
    \ volume is printed.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"label\": \"\
    Sodium resazurin stock dose\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Main source batch / named stock dose\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000493583\",\n          \"unit\": \"G_PER_L\"\n\
    \        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000493583\",\n          \"unit\": \"G_PER_L\"\n\
    \        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, exact named row\",\n      \
    \  \"exact_source_quote\": \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"\
    snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent 0.50 ml of 0.1% w/v sodium\
    \ resazurin as a stock dose. Conditional delivered dye mass is 0.50 mg, not an\
    \ authenticated final concentration; preserve the sodium salt.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q9\",\n    \"label\": \"Potassium bicarbonate\",\n    \"decision\": \"correct\"\
    ,\n    \"source_stage\": \"Main source batch / named stock dose\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.94867\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.94867\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, exact named row\",\n      \
    \  \"exact_source_quote\": \"KHCO3 4.00 g\",\n        \"snapshot_sha256\": \"\
    6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n        \"\
    parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact source batch quantity\
    \ and its explicit unit. The local main G_PER_L value is not an authenticated\
    \ measured final concentration; current API requests failed and no final batch\
    \ volume is printed.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q10\",\n    \"label\": \"\
    Ethanol volume\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Main\
    \ source batch / named stock dose\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, exact named row\",\n      \
    \  \"exact_source_quote\": \"Ethanol 1.30 ml\",\n        \"snapshot_sha256\":\
    \ \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Source 1.30 ml is ethanol volume,\
    \ not 1.3 g/L. Do not infer a density or convert to a measured final concentration.\"\
    ,\n    \"local_evidence_status\": \"No claim-level supporting evidence attached\
    \ in either inspected layer; matching retained values are evidence_only, not verified.\"\
    \n  },\n  {\n    \"decision_id\": \"q11\",\n    \"label\": \"L-cysteine hydrochloride\
    \ monohydrate\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Main\
    \ source batch / named stock dose\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.29615\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.29615\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, exact named row\",\n      \
    \  \"exact_source_quote\": \"L-Cysteine HCl x H2O 0.30 g\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact source batch quantity\
    \ and its explicit unit. The local main G_PER_L value is not an authenticated\
    \ measured final concentration; current API requests failed and no final batch\
    \ volume is printed.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n    \"label\": \"\
    Sodium sulfide nonahydrate\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Main source batch / named stock dose\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.29615\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.29615\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, exact named row\",\n      \
    \  \"exact_source_quote\": \"Na2S x 9 H2O 0.30 g\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact source batch quantity\
    \ and its explicit unit. The local main G_PER_L value is not an authenticated\
    \ measured final concentration; current API requests failed and no final batch\
    \ volume is printed.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"label\": \"\
    NTA\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Trace element\
    \ stock, not main medium\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\",\n      \
    \  \"field_path\": \"ingredients[12].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"12.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.8\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"Nitrilotriacetic acid (NTA) 12.80\
    \ g\",\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q14\",\n    \"label\": \"Iron dichloride tetrahydrate\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element stock, not main medium\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"FeCl2 x 4 H2O 1.00 g\",\n        \"\
    snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"label\": \"Manganese chloride tetrahydrate\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element stock, not main medium\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"MnCl2 x 4 H2O 0.10 g\",\n        \"\
    snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q16\",\n    \"label\": \"Cobalt chloride hexahydrate\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element stock, not main medium\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 0.03 g\",\n        \"\
    snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q17\",\n    \"label\": \"Trace calcium chloride dihydrate\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element stock, not main medium\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1789733\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1789733\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 0.10 g\",\n        \"\
    snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q18\",\n    \"label\": \"Zinc chloride\",\n    \"decision\": \"correct\",\n\
    \    \"source_stage\": \"Trace element stock, not main medium\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"ZnCl2 0.10 g\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q19\",\n    \"label\": \"Copper chloride\",\n    \"decision\": \"correct\"\
    ,\n    \"source_stage\": \"Trace element stock, not main medium\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"CuCl2 0.02 g\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q20\",\n    \"label\": \"Boric acid\",\n    \"decision\": \"correct\",\n \
    \   \"source_stage\": \"Trace element stock, not main medium\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"H3BO3 0.01 g\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q21\",\n    \"label\": \"Sodium molybdate dihydrate\",\n    \"decision\":\
    \ \"correct\",\n    \"source_stage\": \"Trace element stock, not main medium\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 0.03 g\",\n      \
    \  \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q22\",\n    \"label\": \"Nickel chloride hexahydrate\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element stock, not main medium\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"NiCl2 x 6 H2O 0.10 g\",\n        \"\
    snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q23\",\n    \"label\": \"Trace sodium chloride\",\n    \"decision\": \"correct\"\
    ,\n    \"source_stage\": \"Trace element stock, not main medium\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5923\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5923\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"NaCl 1.00 g\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q24\",\n    \"label\": \"Sodium selenite pentahydrate\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element stock, not main medium\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"Na2SeO3 x 5 H2O 0.03 g\",\n      \
    \  \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q25\",\n    \"label\": \"Sodium tungstate dihydrate\",\n    \"decision\":\
    \ \"correct\",\n    \"source_stage\": \"Trace element stock, not main medium\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.04\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.04\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 trace element solution table, exact named\
    \ row\",\n        \"exact_source_quote\": \"Na2WO4 x 2 H2O 0.04 g\",\n       \
    \ \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"This mass belongs to the trace stock\
    \ made up to 1000 ml, of which the main recipe adds only 10 ml. Retain the original\
    \ mass/form and stock stage; the current flat main value is not this delivered\
    \ contribution. Main/stock duplicate sums must be separated.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q26\",\n    \"label\": \"Biotin\",\n    \"decision\": \"correct\",\n    \"\
    source_stage\": \"Wolin vitamin stock (10x), not main medium\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 Wolin tenfold vitamin table, exact named\
    \ row\",\n        \"exact_source_quote\": \"Biotin 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"The local number is a vitamin-stock\
    \ strength promoted to a main concentration. Preserve the source milligram quantity\
    \ per listed 1000 ml stock water, the tenfold formulation identity and the separate\
    \ 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit\
    \ source table.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q27\",\n    \"label\": \"\
    Folic acid\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Wolin vitamin\
    \ stock (10x), not main medium\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 Wolin tenfold vitamin table, exact named\
    \ row\",\n        \"exact_source_quote\": \"Folic acid 20.00 mg\",\n        \"\
    snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"The local number is a vitamin-stock\
    \ strength promoted to a main concentration. Preserve the source milligram quantity\
    \ per listed 1000 ml stock water, the tenfold formulation identity and the separate\
    \ 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit\
    \ source table.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q28\",\n    \"label\": \"\
    Pyridoxine hydrochloride\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Wolin vitamin stock (10x), not main medium\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 Wolin tenfold vitamin table, exact named\
    \ row\",\n        \"exact_source_quote\": \"Pyridoxine hydrochloride 100.00 mg\"\
    ,\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"The local number is a vitamin-stock\
    \ strength promoted to a main concentration. Preserve the source milligram quantity\
    \ per listed 1000 ml stock water, the tenfold formulation identity and the separate\
    \ 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit\
    \ source table.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q29\",\n    \"label\": \"\
    Thiamine HCl\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Wolin\
    \ vitamin stock (10x), not main medium\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 Wolin tenfold vitamin table, exact named\
    \ row\",\n        \"exact_source_quote\": \"Thiamine HCl 50.00 mg\",\n       \
    \ \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"The local number is a vitamin-stock\
    \ strength promoted to a main concentration. Preserve the source milligram quantity\
    \ per listed 1000 ml stock water, the tenfold formulation identity and the separate\
    \ 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit\
    \ source table.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q30\",\n    \"label\": \"\
    Riboflavin\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Wolin vitamin\
    \ stock (10x), not main medium\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 Wolin tenfold vitamin table, exact named\
    \ row\",\n        \"exact_source_quote\": \"Riboflavin 50.00 mg\",\n        \"\
    snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"The local number is a vitamin-stock\
    \ strength promoted to a main concentration. Preserve the source milligram quantity\
    \ per listed 1000 ml stock water, the tenfold formulation identity and the separate\
    \ 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit\
    \ source table.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q31\",\n    \"label\": \"\
    Nicotinic acid\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Wolin\
    \ vitamin stock (10x), not main medium\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 Wolin tenfold vitamin table, exact named\
    \ row\",\n        \"exact_source_quote\": \"Nicotinic acid 50.00 mg\",\n     \
    \   \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"The local number is a vitamin-stock\
    \ strength promoted to a main concentration. Preserve the source milligram quantity\
    \ per listed 1000 ml stock water, the tenfold formulation identity and the separate\
    \ 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit\
    \ source table.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q32\",\n    \"label\": \"\
    Calcium D-(+)-pantothenate\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Wolin vitamin stock (10x), not main medium\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 Wolin tenfold vitamin table, exact named\
    \ row\",\n        \"exact_source_quote\": \"Calcium D-(+)-pantothenate 50.00 mg\"\
    ,\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"The local number is a vitamin-stock\
    \ strength promoted to a main concentration. Preserve the source milligram quantity\
    \ per listed 1000 ml stock water, the tenfold formulation identity and the separate\
    \ 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit\
    \ source table.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q33\",\n    \"label\": \"\
    Vitamin B12\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Wolin\
    \ vitamin stock (10x), not main medium\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 Wolin tenfold vitamin table, exact named\
    \ row\",\n        \"exact_source_quote\": \"Vitamin B12 1.00 mg\",\n        \"\
    snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"The local number is a vitamin-stock\
    \ strength promoted to a main concentration. Preserve the source milligram quantity\
    \ per listed 1000 ml stock water, the tenfold formulation identity and the separate\
    \ 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit\
    \ source table.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q34\",\n    \"label\": \"\
    p-Aminobenzoic acid\",\n    \"decision\": \"correct\",\n    \"source_stage\":\
    \ \"Wolin vitamin stock (10x), not main medium\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 Wolin tenfold vitamin table, exact named\
    \ row\",\n        \"exact_source_quote\": \"p-Aminobenzoic acid 50.00 mg\",\n\
    \        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"The local number is a vitamin-stock\
    \ strength promoted to a main concentration. Preserve the source milligram quantity\
    \ per listed 1000 ml stock water, the tenfold formulation identity and the separate\
    \ 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit\
    \ source table.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q35\",\n    \"label\": \"\
    (DL)-alpha-Lipoic acid\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Wolin vitamin stock (10x), not main medium\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 Wolin tenfold vitamin table, exact named\
    \ row\",\n        \"exact_source_quote\": \"(DL)-alpha-Lipoic acid 50.00 mg\"\
    ,\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"The local number is a vitamin-stock\
    \ strength promoted to a main concentration. Preserve the source milligram quantity\
    \ per listed 1000 ml stock water, the tenfold formulation identity and the separate\
    \ 1 ml main dose. Do not additionally apply a tenfold factor to the already explicit\
    \ source table.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q36\",\n    \"label\": \"\
    Main trace-stock addition\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"Page1 main table\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\",\n      \
    \  \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"presence\"\
    : \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table\",\n        \"exact_source_quote\"\
    : \"Trace element solution 10.00 ml\",\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Add the explicit 10 ml trace-stock\
    \ dose and an inline or verified stock recipe; no main-stock solution object is\
    \ currently present.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q37\",\n    \"label\": \"\
    Main tenfold-vitamin addition\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"Page1 main table\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\",\n      \
    \  \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"presence\"\
    : \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table\",\n        \"exact_source_quote\"\
    : \"Wolin's vitamin solution (10x) 1.00 ml\",\n        \"snapshot_sha256\": \"\
    6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n        \"\
    parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Add the explicit 1 ml dose of the\
    \ printed tenfold stock, separate from its constituent strengths.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q38\",\n    \"label\": \"Tenfold stock identity\",\n    \"decision\": \"add\"\
    ,\n    \"source_stage\": \"Page2 vitamin heading\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 vitamin heading\",\n        \"exact_source_quote\"\
    : \"Wolin's vitamin solution (10x) (from medium 120)\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the 10x stock designation\
    \ without guessing a parent whole-medium formulation or multiplying its printed\
    \ masses again.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q39\",\n    \"label\": \"\
    Resazurin stock strength\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"Page1 main table\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\",\n      \
    \  \"field_path\": \"ingredients[7].preferred_term\",\n        \"stored\": \"\
    Sodium resazurin\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000493583\",\n          \"unit\": \"G_PER_L\"\n\
    \        }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].preferred_term\",\n        \"stored\"\
    : \"Sodium resazurin\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000493583\",\n          \"unit\": \"G_PER_L\"\n\
    \        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table\",\n        \"exact_source_quote\"\
    : \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Add the explicit 0.1% w/v stock basis.\
    \ Arithmetic: 0.1 g/100 ml equals 1 mg/ml; 0.50 ml delivers 0.50 mg, without a\
    \ measured final-medium denominator.\",\n    \"local_evidence_status\": \"No claim-level\
    \ supporting evidence attached in either inspected layer; matching retained values\
    \ are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\": \"q40\"\
    ,\n    \"label\": \"Main water preparation amount\",\n    \"decision\": \"add\"\
    ,\n    \"source_stage\": \"Main batch water\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table, water before main preparation\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"\
    snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve 1000 ml water as a main-batch\
    \ preparation input, not an assumed final makeup and not a main mass ingredient.\"\
    ,\n    \"local_evidence_status\": \"No claim-level supporting evidence attached\
    \ in either inspected layer; matching retained values are evidence_only, not verified.\"\
    \n  },\n  {\n    \"decision_id\": \"q41\",\n    \"label\": \"Trace stock water/final\
    \ makeup\",\n    \"decision\": \"evidence_only\",\n    \"source_stage\": \"Trace\
    \ stock final makeup\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\",\n      \
    \  \"field_path\": \"preparation_steps[1].description\",\n        \"stored\":\
    \ \"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with\
    \ KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make\
    \ up to 1000.00 ml.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with\
    \ KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make\
    \ up to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 trace-stock preparation final sentence\"\
    ,\n        \"exact_source_quote\": \"mineral salts. Finally adjust pH to 6.5 with\
    \ KOH and make up to 1000.00 ml.\",\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"The exact 1000 ml final makeup is\
    \ already in the local preparation description. Attach evidence and associate\
    \ this existing field with the trace stock; do not claim it is absent or a main-medium\
    \ final volume.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q42\",\n    \"label\": \"\
    Vitamin-stock water\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Wolin10x\
    \ stock water\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 vitamin table final row\",\n        \"\
    exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Add the listed 1000 ml vitamin-stock\
    \ water context. It does not create an extra 1000 ml main dose.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q43\",\n    \"label\": \"Main gas mixture during sparging\",\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Page1 first preparation sentence\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\",\n       \
    \ \"source_locator\": \"Page1 first preparation sentence\",\n        \"exact_source_quote\"\
    : \"sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make\
    \ it anoxic.\",\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing main preparation retains\
    \ the 80% N2 / 20% CO2 gas mixture. Percentage basis is not explicitly printed;\
    \ do not add a v/v qualifier.\",\n    \"local_evidence_status\": \"No claim-level\
    \ supporting evidence attached in either inspected layer; matching retained values\
    \ are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\": \"q44\"\
    ,\n    \"label\": \"Main sparging time\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"Page1 first preparation sentence\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\",\n       \
    \ \"source_locator\": \"Page1 first preparation sentence\",\n        \"exact_source_quote\"\
    : \"sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make\
    \ it anoxic.\",\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing main preparation retains\
    \ 30–45 minutes; no gas flow is supplied.\",\n    \"local_evidence_status\": \"\
    No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q45\",\n    \"label\": \"Main pH before dispensing\",\n    \"decision\": \"\
    evidence_only\",\n    \"source_stage\": \"Page1 preparation after sparging\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\",\n       \
    \ \"source_locator\": \"Page1 preparation after sparging\",\n        \"exact_source_quote\"\
    : \"Add and dissolve bicarbonate and adjust pH to 7.0\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing preparation retains pH 7.0\
    \ at this main-medium stage; it is not trace-stock pH 6.5.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q46\",\n    \"label\": \"Main dispensing gas mixture\",\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Page1 preparation dispensing clause\
    \ continuing on next line\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\",\n      \
    \  \"field_path\": \"preparation_steps[0].description\",\n        \"stored\":\
    \ \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\",\n       \
    \ \"source_locator\": \"Page1 preparation dispensing clause continuing on next\
    \ line\",\n        \"exact_source_quote\": \"then dispense under 80% N2 and 20%\"\
    ,\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing preparation retains the\
    \ separate 80% N2 / 20% CO2 dispensing atmosphere. The full adjacent source line\
    \ completes CO2; no source text is changed or gas flow invented.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q47\",\n    \"label\": \"Later ethanol/cysteine/sulfide gas\",\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Page1 post-sterilization stock clause\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\",\n       \
    \ \"source_locator\": \"Page1 post-sterilization stock clause\",\n        \"exact_source_quote\"\
    : \"sterilization add ethanol, cysteine and sulfide from sterile anoxic stock\
    \ solutions prepared\\nunder 100% N2 gas.\",\n        \"snapshot_sha256\": \"\
    6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n        \"\
    parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing preparation retains\
    \ 100% N2 for these late stocks separately from main 80:20 gas.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q48\",\n    \"label\": \"Vitamin-stock gas\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"Page1 vitamin preparation clause\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\",\n       \
    \ \"source_locator\": \"Page1 vitamin preparation clause\",\n        \"exact_source_quote\"\
    : \"Vitamins are prepared under 100% N2 gas and sterilized by filtration.\",\n\
    \        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing preparation retains the\
    \ separate 100% N2 vitamin stock atmosphere and filtration.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q49\",\n    \"label\": \"Conditional complete-medium pH\",\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Page1 final preparation sentence\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.0,\n          \"max\": 7.2\n        }\n      },\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\",\n\
    \        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"min\"\
    : 7.0,\n          \"max\": 7.2\n        }\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\",\n       \
    \ \"source_locator\": \"Page1 final preparation sentence\",\n        \"exact_source_quote\"\
    : \"Adjust pH of complete medium to 7.0 - 7.2, if necessary.\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Both the numeric range and conditional\
    \ preparation wording are retained correctly. Attach supporting evidence; do not\
    \ claim this value or its condition is absent.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q50\",\n    \"label\": \"Trace initial water\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"Page2 trace-stock first sentence\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with\
    \ KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make\
    \ up to 1000.00 ml.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with\
    \ KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make\
    \ up to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 trace-stock first sentence\",\n       \
    \ \"exact_source_quote\": \"First dissolve NTA in 200 ml of distilled water and\
    \ adjust pH to 6.5 with KOH, then dissolve\",\n        \"snapshot_sha256\": \"\
    6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n        \"\
    parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing 200 ml is an initial stock\
    \ solvent amount before final makeup, not an additional main ingredient or final\
    \ stock volume.\",\n    \"local_evidence_status\": \"No claim-level supporting\
    \ evidence attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q51\",\n    \"label\": \"\
    Trace initial pH\",\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"Page2 trace-stock first sentence\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with\
    \ KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make\
    \ up to 1000.00 ml.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with\
    \ KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make\
    \ up to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 trace-stock first sentence\",\n       \
    \ \"exact_source_quote\": \"First dissolve NTA in 200 ml of distilled water and\
    \ adjust pH to 6.5 with KOH, then dissolve\",\n        \"snapshot_sha256\": \"\
    6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n        \"\
    parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing initial stock pH 6.5 is\
    \ source-supported, separate from main pH.\",\n    \"local_evidence_status\":\
    \ \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q52\",\n    \"label\": \"Trace final pH\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"Page2 trace-stock final sentence\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with\
    \ KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make\
    \ up to 1000.00 ml.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with\
    \ KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make\
    \ up to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 trace-stock final sentence\",\n       \
    \ \"exact_source_quote\": \"mineral salts. Finally adjust pH to 6.5 with KOH and\
    \ make up to 1000.00 ml.\",\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing final stock pH 6.5 is a\
    \ second source stage, with a separately stated 1000 ml makeup.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q53\",\n    \"label\": \"Trace KOH dose\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"source_stage\": \"Page2 trace-stock preparation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with\
    \ KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make\
    \ up to 1000.00 ml.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with\
    \ KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make\
    \ up to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page2 trace-stock preparation\",\n        \"\
    exact_source_quote\": \"mineral salts. Finally adjust pH to 6.5 with KOH and make\
    \ up to 1000.00 ml.\",\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"KOH identity and endpoint are explicit;\
    \ no mass, molarity or added volume is specified.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q54\",\n    \"label\": \"Later stock strengths and volumes\",\n    \"decision\"\
    : \"not_quantified\",\n    \"source_stage\": \"Page1 post-sterilization clause\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\",\n       \
    \ \"source_locator\": \"Page1 post-sterilization clause\",\n        \"exact_source_quote\"\
    : \"sterilization add ethanol, cysteine and sulfide from sterile anoxic stock\
    \ solutions prepared\",\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Main ethanol volume and cysteine/sulfide\
    \ batch masses are given in the table, but the later source-stock strengths and\
    \ delivery volumes are not. Do not infer them from the main amounts.\",\n    \"\
    local_evidence_status\": \"No claim-level supporting evidence attached in either\
    \ inspected layer; matching retained values are evidence_only, not verified.\"\
    \n  },\n  {\n    \"decision_id\": \"q55\",\n    \"label\": \"Main autoclave cycle\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"source_stage\": \"Page1 dispensing/autoclaving\
    \ clause\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\",\n       \
    \ \"source_locator\": \"Page1 dispensing/autoclaving clause\",\n        \"exact_source_quote\"\
    : \"CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\
    \ After\",\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Autoclaving is stated, but no temperature\
    \ or duration is supplied; do not borrow a collection default.\",\n    \"local_evidence_status\"\
    : \"No claim-level supporting evidence attached in either inspected layer; matching\
    \ retained values are evidence_only, not verified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q56\",\n    \"label\": \"Main pH adjustment reagent/dose\",\n    \"decision\"\
    : \"not_quantified\",\n    \"source_stage\": \"Page1 main pH clause\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, ethanol, vitamins, cysteine and\
    \ sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45\
    \ min to make it anoxic. Add and dissolve bicarbonate and adjust pH to 7.0, then\
    \ dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. After sterilization add ethanol, cysteine and\
    \ sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins\
    \ are prepared under 100% N2 gas and sterilized by filtration. Adjust pH of complete\
    \ medium to 7.0 - 7.2, if necessary.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\",\n       \
    \ \"source_locator\": \"Page1 main pH clause\",\n        \"exact_source_quote\"\
    : \"Add and dissolve bicarbonate and adjust pH to 7.0\",\n        \"snapshot_sha256\"\
    : \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\",\n    \
    \    \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"No separate titrant identity or dose\
    \ is printed for the main pH adjustment. Trace KOH is not automatically the main\
    \ titrant.\",\n    \"local_evidence_status\": \"No claim-level supporting evidence\
    \ attached in either inspected layer; matching retained values are evidence_only,\
    \ not verified.\"\n  },\n  {\n    \"decision_id\": \"q57\",\n    \"label\": \"\
    Measured main final volume\",\n    \"decision\": \"not_quantified\",\n    \"source_stage\"\
    : \"Page1 main water row and explicit main stock additions\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz318b\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318b.pdf\"\
    ,\n        \"source_locator\": \"Page1 main water row and explicit main stock\
    \ additions\",\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\"\
    ,\n        \"snapshot_sha256\": \"6043670ad18e4d87d541375a969fbe6b8f275382f63d44e281ddc6573ad0b3fe\"\
    ,\n        \"parsed_text_sha256\": \"894dcef266cda592b8044f80afa771740b43168bfdcb0dcfdc8357b99948b7f5\"\
    \n      }\n    ],\n    \"interpretation\": \"Listed liquids sum 1000 + 10 + 0.5\
    \ + 1.3 + 1 = 1012.8 ml before any unquantified later stock delivery/titrant volumes.\
    \ This is not a measured final-volume statement. The local values resemble normalization\
    \ to roughly 1013 ml, but no current API payload authenticates that basis.\",\n\
    \    \"local_evidence_status\": \"No claim-level supporting evidence attached\
    \ in either inspected layer; matching retained values are evidence_only, not verified.\"\
    \n  }\n]"
- assessment_id: ownership
  area: ownership
  topic: Maintained source and generated follow-up
  outcome: supported
  summary: The one normalized owner is the maintained correction surface. Its full
    bytes match the generated formulation, while the target adds merge metadata. Current
    importer/cleanup/merge code is context rather than historical causation evidence.
    No recipe, history, generated page or review bundle was changed.
  target_ids:
  - CultureMech:001418
  evidence_ids:
  - record
  - owner-0
  - writer-0
  - writer-1
  - writer-2
  - history-metadata
findings:
- finding_id: f1
  issue_key: cm001418-flattened-stock-formulation
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Trace and vitamin stock strengths are represented as main-medium amounts
  description: Both layers flatten thirteen trace-stock solutes and ten tenfold-vitamin
    solutes into main ingredients, omitting the 10 ml and 1 ml stock doses. Sodium
    chloride and calcium chloride additionally sum contributions from different stages;
    the stored duplicate notes expose those sums. This materially changes the recipe
    even though the schema is valid.
  target_ids:
  - CultureMech:001418
  field_paths:
  - ingredients
  - solutions
  - ingredients[1].concentration
  - ingredients[3].concentration
  - preparation_steps[1]
  evidence_ids:
  - record
  - owner-0
  - primary
  - trace-dose
  - vitamin-dose
  - trace-stock
  - vitamin-stock
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml
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
  issue_key: cm001418-volume-and-final-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Ethanol, indicator dose and main normalization lose source units or basis
  description: Source ethanol is 1.30 ml, not 1.3 g/L; sodium resazurin is a 0.50
    ml dose of 0.1% w/v stock. The main recipe lists 1000 ml water without an explicit
    measured final volume, while several local main values are normalized to an unauthenticated
    denominator. Neither density nor final-volume correction is established by current
    source evidence.
  target_ids:
  - CultureMech:001418
  field_paths:
  - ingredients[0:12].concentration
  - ingredients[9].concentration
  - ingredients[7]
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - ethanol
  - resazurin
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml
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
  issue_key: cm001418-chemical-form-mismatches
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and sodium resazurin do not match their asserted structures
  description: Nickel chloride hexahydrate is mapped to anhydrous CHEBI:34887 in both
    primary and secondary slots. Sodium resazurin is mapped to neutral CHEBI:8806,
    which has no sodium counterion. In contrast, the calcium pantothenate structure
    is compatible with the source D-(+) qualifier, and non-stereospecific lipoic acid
    does not establish a false conflict with the source DL wording.
  target_ids:
  - CultureMech:001418
  field_paths:
  - ingredients[20].term
  - ingredients[20].mediaingredientmech_chebi_term
  - ingredients[7].term
  evidence_ids:
  - record
  - owner-0
  - primary
  - chebi34887
  - chebi8806
  - chebi31345
  - chebi16494
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml
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
  issue_key: cm001418-claim-evidence
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Retained amounts and preparation lack narrow supporting evidence
  description: Source URLs and import history are present, but no target/owner claim-level
    evidence supports concentration, stock scope or the otherwise retained preparation.
    The dated local review report remains derivative context and cannot authenticate
    missing MediaDive raw bytes.
  target_ids:
  - CultureMech:001418
  field_paths:
  - ingredients[*].evidence
  - preparation_steps[*].evidence
  - ph_range
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - primary
  - historical-report
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml
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
  description: Reconstruct the main recipe and the two explicit stock stages in the
    normalized owner. Split main/stock salt contributions, retain each stock batch
    and dose, and associate the already retained trace preparation with that stock.
    Regenerate only after source-backed correction.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001418
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml
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
  description: Preserve the exact main batch amounts, ethanol volume and resazurin
    stock dose/strength. Qualify any nominal normalization and retain unresolved final-volume/density
    limits; do not compute new exact final concentrations without evidence.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001418
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml
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
  description: Reassess exact supplied-form mappings using primary labels and verified
    structures. Preserve source hydrate/salt/stereochemical wording and leave unresolved
    replacements unassigned; do not replace correctly compatible forms based on generic
    label appearance alone.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001418
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml
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
  description: Attach exact current primary excerpts at the repaired or retained claim
    layer, preserving source stages and capture metadata. Keep the historical report
    and old history unchanged; append later authorized curation events.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001418
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml
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
- The exact asserted MediaDive318b API returned HTTP503 on the original attempt and
  separately captured retry. Current provider accession/content and the origin of
  local normalized values are not authenticated. The exact DSMZ318b primary remains
  available and supports the bounded main/stock scientific comparison; derivative
  dated reports do not replace missing raw provider evidence.
- The exact asserted MediaDive318b API returned HTTP503 on the original attempt and
  separately captured retry. Current provider accession/content and the origin of
  local normalized values are not authenticated. The exact DSMZ318b primary remains
  available and supports the bounded main/stock scientific comparison; derivative
  dated reports do not replace missing raw provider evidence.
- Source-only stock recipes printed inside DSMZ318b were read in full; no separate
  whole parent DSMZ318 or DSMZ120 recipe, growth phenotype or historical provider
  equivalence is inferred. All quoted source table units remain original; derived
  arithmetic is separately labeled.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-028
- generated-medium
```
