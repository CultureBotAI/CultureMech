# Source and formulation review: arcobacter_anaerophilus_medium (CultureMech:000992)

- Review: 20261021T172702Z-culturemech-000992-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T17:21:18Z
- Finished UTC: 2026-10-21T17:27:02Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 1521 verifies the initial one-litre formulation and explicitly separates three later additions per 10 mL receiving medium. The local SL10 mass unit and final bicarbonate/sulfide/B12 rates do not preserve that source scope. Eleven later owner amount claims survive as exact local derivative quotations, but their cited historical raw response is unavailable. The named SL10 stock has a current standard candidate whose historical applicability is unestablished. Those required source checks keep this review partial; no unknown stock strength or final supplemented volume is invented.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 303; batch 031 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty task batches contain 300 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 303 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000992 | data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml | generated | arcobacter_anaerophilus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000992 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000992 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-031/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch031/303/strict.tsv |
| validate-terms | passed | True | CultureMech:000992 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000992 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000992 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive1521api | unavailable | False | CultureMech:000992 | Current exact API attempt returned HTTP 503. The current primary remains available; original historical-response authentication is a distinct required check below. |
| Exact source content access: mediadive1521api_retry | unavailable | False | CultureMech:000992 | Current exact API attempt returned HTTP 503. The current primary remains available; original historical-response authentication is a distinct required check below. |
| Required source-scope verification | unavailable | True | CultureMech:000992 | Required authentication of the eleven cited historical amount snippets against original response bytes is unavailable after the bounded ignored-inclusive search. Derivative matches and current primary agreement do not authenticate that response. |
| Required source-scope verification | unavailable | True | CultureMech:000992 | The exact version/composition correspondence of DSMZ 1521 SL10 to the captured current DSMZ 320 candidate remains unestablished; required complete-stock identity review is therefore partial. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000992.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:000992.

28 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "KH2PO4 initial-medium amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "initial_batch_amount": "0.50",
      "source_unit": "g",
      "initial_medium_volume_L": 1,
      "later_supplemented_volume_L": null
    },
    "rationale": "The current primary independently supports this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks evidence; owner has a historical quoted claim whose raw response is not authenticated. Preserve it and add current primary stage evidence rather than marking historical bytes verified or treating the value as a final supplemented-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial table: KH2PO4",
        "exact_source_quote": "KH2PO4 0.50 g",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      },
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial make-up instruction",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "NaCl initial-medium amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "initial_batch_amount": "20.00",
      "source_unit": "g",
      "initial_medium_volume_L": 1,
      "later_supplemented_volume_L": null
    },
    "rationale": "The current primary independently supports this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks evidence; owner has a historical quoted claim whose raw response is not authenticated. Preserve it and add current primary stage evidence rather than marking historical bytes verified or treating the value as a final supplemented-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial table: NaCl",
        "exact_source_quote": "NaCl 20.00 g",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      },
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial make-up instruction",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "CaCl2 x 2 H2O initial-medium amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "initial_batch_amount": "0.25",
      "source_unit": "g",
      "initial_medium_volume_L": 1,
      "later_supplemented_volume_L": null
    },
    "rationale": "The current primary independently supports this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks evidence; owner has a historical quoted claim whose raw response is not authenticated. Preserve it and add current primary stage evidence rather than marking historical bytes verified or treating the value as a final supplemented-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial table: CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl2 x 2 H2O 0.25 g",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      },
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial make-up instruction",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "MgSO4 x 7 H2O initial-medium amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "initial_batch_amount": "1.00",
      "source_unit": "g",
      "initial_medium_volume_L": 1,
      "later_supplemented_volume_L": null
    },
    "rationale": "The current primary independently supports this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks evidence; owner has a historical quoted claim whose raw response is not authenticated. Preserve it and add current primary stage evidence rather than marking historical bytes verified or treating the value as a final supplemented-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial table: MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO4 x 7 H2O 1.00 g",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      },
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial make-up instruction",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "NH4Cl initial-medium amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "initial_batch_amount": "0.50",
      "source_unit": "g",
      "initial_medium_volume_L": 1,
      "later_supplemented_volume_L": null
    },
    "rationale": "The current primary independently supports this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks evidence; owner has a historical quoted claim whose raw response is not authenticated. Preserve it and add current primary stage evidence rather than marking historical bytes verified or treating the value as a final supplemented-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial table: NH4Cl",
        "exact_source_quote": "NH4Cl 0.50 g",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      },
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial make-up instruction",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Sodium citrate initial-medium amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "initial_batch_amount": "0.3",
      "source_unit": "g",
      "initial_medium_volume_L": 1,
      "later_supplemented_volume_L": null
    },
    "rationale": "The current primary independently supports this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks evidence; owner has a historical quoted claim whose raw response is not authenticated. Preserve it and add current primary stage evidence rather than marking historical bytes verified or treating the value as a final supplemented-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial table: Sodium citrate",
        "exact_source_quote": "Sodium citrate 0.3 g",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      },
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial make-up instruction",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Yeast extract initial-medium amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "initial_batch_amount": "0.50",
      "source_unit": "g",
      "initial_medium_volume_L": 1,
      "later_supplemented_volume_L": null
    },
    "rationale": "The current primary independently supports this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks evidence; owner has a historical quoted claim whose raw response is not authenticated. Preserve it and add current primary stage evidence rather than marking historical bytes verified or treating the value as a final supplemented-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial table: Yeast extract",
        "exact_source_quote": "Yeast extract 0.50 g",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      },
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial make-up instruction",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Ammonium acetate initial-medium amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "initial_batch_amount": "1.00",
      "source_unit": "g",
      "initial_medium_volume_L": 1,
      "later_supplemented_volume_L": null
    },
    "rationale": "The current primary independently supports this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks evidence; owner has a historical quoted claim whose raw response is not authenticated. Preserve it and add current primary stage evidence rather than marking historical bytes verified or treating the value as a final supplemented-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial table: Ammonium acetate",
        "exact_source_quote": "Ammonium acetate 1.00 g",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      },
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial make-up instruction",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Lactate initial-medium amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "initial_batch_amount": "1.00",
      "source_unit": "g",
      "initial_medium_volume_L": 1,
      "later_supplemented_volume_L": null
    },
    "rationale": "The current primary independently supports this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks evidence; owner has a historical quoted claim whose raw response is not authenticated. Preserve it and add current primary stage evidence rather than marking historical bytes verified or treating the value as a final supplemented-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial table: Lactate",
        "exact_source_quote": "Lactate 1.00 g",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      },
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial make-up instruction",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Pyruvate initial-medium amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "initial_batch_amount": "1.00",
      "source_unit": "g",
      "initial_medium_volume_L": 1,
      "later_supplemented_volume_L": null
    },
    "rationale": "The current primary independently supports this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks evidence; owner has a historical quoted claim whose raw response is not authenticated. Preserve it and add current primary stage evidence rather than marking historical bytes verified or treating the value as a final supplemented-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial table: Pyruvate",
        "exact_source_quote": "Pyruvate 1.00 g",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      },
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial make-up instruction",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Resazurin initial-medium amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "initial_batch_amount": "1.00",
      "source_unit": "mg",
      "initial_medium_volume_L": 1,
      "later_supplemented_volume_L": null
    },
    "rationale": "The current primary independently supports this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks evidence; owner has a historical quoted claim whose raw response is not authenticated. Preserve it and add current primary stage evidence rather than marking historical bytes verified or treating the value as a final supplemented-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial table: Resazurin",
        "exact_source_quote": "Resazurin 1.00 mg",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      },
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial make-up instruction",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "SL10 stock receiving dose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "dose_ml": 1,
      "initial_medium_volume_L": 1,
      "stock_formula_historical_identity": "unresolved"
    },
    "rationale": "The source gives a stock volume, not a gram. Restore the one-millilitre dose and separately resolve the stock identity; the initial litre basis does not authenticate a candidate stock version.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial table SL10 row",
        "exact_source_quote": "SL10 1.0 ml",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      },
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, initial make-up",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Bicarbonate addition",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "stock_percent": 10,
      "percent_basis": null,
      "dose_uL": 150,
      "receiving_medium_ml": 10,
      "completed_final_volume_ml": null
    },
    "rationale": "Preserve the source stock strength where given and the receiving-medium basis. Unqualified 10% cannot establish a mass concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, post-autoclave additions",
        "exact_source_quote": "NaHCO3 (10%) 150 µl/10 ml",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Sulfide addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "2.40182",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "2.40182",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stock_molarity_M": 1,
      "dose_uL": 10,
      "receiving_medium_ml": 10,
      "delivered_micromoles": 10,
      "completed_final_volume_ml": null
    },
    "rationale": "Preserve the source stock strength where given and the receiving-medium basis. 1 M × 10 microlitres = 10 micromoles delivered; this is not the asserted main g/L rate and no final-volume/mass conversion is invented.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, post-autoclave additions",
        "exact_source_quote": "Na2S x 9 H2O (1 M) 10 µl/10 ml",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "B12 addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "dose_uL": 10,
      "receiving_medium_ml": 10,
      "stock_strength": null,
      "delivered_mass": null
    },
    "rationale": "Preserve the source stock strength where given and the receiving-medium basis. Ten microlitres is a volume dose, not 10 g/L; the stock has no supplied strength.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, post-autoclave additions",
        "exact_source_quote": "Vitamin B12 10 µl/10 ml",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Initial medium make-up",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add distilled water to 1 liter, boil the medium and cool under N2, distribute under N2 and autoclave. After autoclaving the following sterilized solutions are added:",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add distilled water to 1 liter, boil the medium and cool under N2, distribute under N2 and autoclave. After autoclaving the following sterilized solutions are added:",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "initial_final_volume_L": 1,
      "stage": "Before post-autoclave additions"
    },
    "rationale": "This explicit make-up survives locally. Preserve the stage and add evidence; later receiving doses do not retroactively establish a final supplemented litre.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, preparation sentence",
        "exact_source_quote": "Add distilled water to 1 liter",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Unspecified B12 stock strength",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "B12_stock_strength": null
    },
    "rationale": "No fixed stock strength is supplied. The missing mass is unknown, not zero and not a generic vitamin convention.",
    "source_snippets": [
      {
        "source_key": "dsmz1521",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf",
        "source_locator": "Page 1, final addition",
        "exact_source_quote": "Vitamin B12 10 µl/10 ml",
        "snapshot_sha256": "d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1",
        "parsed_text_sha256": "556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3",
        "accessed_at": "2026-10-21T17:04:21.789162Z"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Candidate standard SL10: HCl (25%)",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "candidate_source": "DSMZ 320 SL10",
      "candidate_batch_amount": "10.00",
      "source_unit": "ml",
      "transfer_to_DSM1521": "not established"
    },
    "rationale": "Record the inspected candidate exactly, without inserting its composition into this target until the named historical stock correspondence is resolved. Other parent stocks and basal procedures are excluded; the HCl percent basis remains unstated.",
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "Pages 1–2, Trace element solution SL-10 subsection",
        "exact_source_quote": "HCl (25%) 10.00 ml",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6",
        "accessed_at": "2026-10-21T13:20:08.151265Z"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Candidate standard SL10: FeCl2 x 4 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "candidate_source": "DSMZ 320 SL10",
      "candidate_batch_amount": "1.50",
      "source_unit": "g",
      "transfer_to_DSM1521": "not established"
    },
    "rationale": "Record the inspected candidate exactly, without inserting its composition into this target until the named historical stock correspondence is resolved. Other parent stocks and basal procedures are excluded; the HCl percent basis remains unstated.",
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "Pages 1–2, Trace element solution SL-10 subsection",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6",
        "accessed_at": "2026-10-21T13:20:08.151265Z"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Candidate standard SL10: ZnCl2",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "candidate_source": "DSMZ 320 SL10",
      "candidate_batch_amount": "70.00",
      "source_unit": "mg",
      "transfer_to_DSM1521": "not established"
    },
    "rationale": "Record the inspected candidate exactly, without inserting its composition into this target until the named historical stock correspondence is resolved. Other parent stocks and basal procedures are excluded; the HCl percent basis remains unstated.",
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "Pages 1–2, Trace element solution SL-10 subsection",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6",
        "accessed_at": "2026-10-21T13:20:08.151265Z"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Candidate standard SL10: MnCl2 x 4 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "candidate_source": "DSMZ 320 SL10",
      "candidate_batch_amount": "100.00",
      "source_unit": "mg",
      "transfer_to_DSM1521": "not established"
    },
    "rationale": "Record the inspected candidate exactly, without inserting its composition into this target until the named historical stock correspondence is resolved. Other parent stocks and basal procedures are excluded; the HCl percent basis remains unstated.",
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "Pages 1–2, Trace element solution SL-10 subsection",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6",
        "accessed_at": "2026-10-21T13:20:08.151265Z"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Candidate standard SL10: H3BO3",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "candidate_source": "DSMZ 320 SL10",
      "candidate_batch_amount": "6.00",
      "source_unit": "mg",
      "transfer_to_DSM1521": "not established"
    },
    "rationale": "Record the inspected candidate exactly, without inserting its composition into this target until the named historical stock correspondence is resolved. Other parent stocks and basal procedures are excluded; the HCl percent basis remains unstated.",
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "Pages 1–2, Trace element solution SL-10 subsection",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6",
        "accessed_at": "2026-10-21T13:20:08.151265Z"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "Candidate standard SL10: CoCl2 x 6 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "candidate_source": "DSMZ 320 SL10",
      "candidate_batch_amount": "190.00",
      "source_unit": "mg",
      "transfer_to_DSM1521": "not established"
    },
    "rationale": "Record the inspected candidate exactly, without inserting its composition into this target until the named historical stock correspondence is resolved. Other parent stocks and basal procedures are excluded; the HCl percent basis remains unstated.",
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "Pages 1–2, Trace element solution SL-10 subsection",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6",
        "accessed_at": "2026-10-21T13:20:08.151265Z"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "Candidate standard SL10: CuCl2 x 2 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "candidate_source": "DSMZ 320 SL10",
      "candidate_batch_amount": "2.00",
      "source_unit": "mg",
      "transfer_to_DSM1521": "not established"
    },
    "rationale": "Record the inspected candidate exactly, without inserting its composition into this target until the named historical stock correspondence is resolved. Other parent stocks and basal procedures are excluded; the HCl percent basis remains unstated.",
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "Pages 1–2, Trace element solution SL-10 subsection",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6",
        "accessed_at": "2026-10-21T13:20:08.151265Z"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Candidate standard SL10: NiCl2 x 6 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "candidate_source": "DSMZ 320 SL10",
      "candidate_batch_amount": "24.00",
      "source_unit": "mg",
      "transfer_to_DSM1521": "not established"
    },
    "rationale": "Record the inspected candidate exactly, without inserting its composition into this target until the named historical stock correspondence is resolved. Other parent stocks and basal procedures are excluded; the HCl percent basis remains unstated.",
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "Pages 1–2, Trace element solution SL-10 subsection",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6",
        "accessed_at": "2026-10-21T13:20:08.151265Z"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Candidate standard SL10: Na2MoO4 x 2 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "candidate_source": "DSMZ 320 SL10",
      "candidate_batch_amount": "36.00",
      "source_unit": "mg",
      "transfer_to_DSM1521": "not established"
    },
    "rationale": "Record the inspected candidate exactly, without inserting its composition into this target until the named historical stock correspondence is resolved. Other parent stocks and basal procedures are excluded; the HCl percent basis remains unstated.",
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "Pages 1–2, Trace element solution SL-10 subsection",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6",
        "accessed_at": "2026-10-21T13:20:08.151265Z"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Candidate standard SL10: Distilled water",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "candidate_source": "DSMZ 320 SL10",
      "candidate_batch_amount": "990.00",
      "source_unit": "ml",
      "transfer_to_DSM1521": "not established"
    },
    "rationale": "Record the inspected candidate exactly, without inserting its composition into this target until the named historical stock correspondence is resolved. Other parent stocks and basal procedures are excluded; the HCl percent basis remains unstated.",
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "Pages 1–2, Trace element solution SL-10 subsection",
        "exact_source_quote": "Distilled water 990.00 ml",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6",
        "accessed_at": "2026-10-21T13:20:08.151265Z"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Candidate SL10 final make-up",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "candidate_final_stock_volume_ml": 1000,
      "transfer_to_DSM1521": "not established"
    },
    "rationale": "This is an explicit make-up for the candidate stock, not proof of the missing target stock version. Retain iron-in-acid dissolution order only within that candidate context.",
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "Page 2, continuation of SL10 preparation",
        "exact_source_quote": "make up to 1000.00 ml.",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6",
        "accessed_at": "2026-10-21T13:20:08.151265Z"
      }
    ]
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:000992.

13 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 13/15 primary and 13/15 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 15: primary 86.67%; secondary 86.67%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:000992.

14 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact accession and named dependency

identity: concern. Targets: CultureMech:000992.

Stable ID and DSMZ 1521 identity resolve. The source names SL10 but does not establish that the captured DSMZ 320 standard is the exact dependency version. Preserve the available candidate and resolve only this stock identity, not a whole parent recipe.

### Later owner claims and unavailable original response

evidence: concern. Targets: CultureMech:000992.

Eleven owner-only claims match the pinned local derivative report and are separately corroborated for initial-medium amounts by the current primary. The original October 7 response SHA 13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b is not recovered. The bounded search included hidden/ignored candidates; no universal absence claim is made. Target has none of these later evidence objects.

### Supplied generic forms and exact hydrate limits

grounding: supported. Targets: CultureMech:000992.

Explicit calcium, magnesium and sulfide hydrate names agree with their terms. Source lactate and pyruvate do not specify a counterion or stereoisomer, so no replacement salt or D/L claim is inferred. Resazurin is unsalted in this primary; the sodium-resazurin finding from other media does not transfer. Sodium citrate hydration remains unspecified; no unverified molecular-weight conversion is used.

### Initial make-up versus later receiving additions

completeness: concern. Targets: CultureMech:000992.

Local preparation retains the initial one-litre make-up, boiling/cooling under N2 and autoclaving but ends before the later dose rows. No gas purity, main pH, incubation temperature or numerical autoclave cycle is supplied. Keep later additions per 10 mL of receiving medium, not an assumed completed volume.

### Mixture category and organism scope

scope: supported. Targets: CultureMech:000992.

Yeast extract supports COMPLEX/UNDEFINED and the source is liquid. The medium title and generic cultivation application are not independent growth evidence. No new organism, phenotype or optimum claim is inferred.

### Current writers and follow-up ownership

provenance: concern. Targets: CultureMech:000992.

Current importer primary/stock separation and fallback unit maps do not prove which historical writer generated these persisted values. Preserve the later owner evidence/history, correct stage-specific stock representation with primary evidence and regenerate only after separately authorized maintained-input changes.

## Findings

### f1: Stock receiving doses are represented as unsupported main mass rates

blocker / open / confirmed; issue key: culturemech.000992.stock-dose-representation.

SL10 is 1 mL, not 1 g/L. Post-autoclave bicarbonate, sulfide and B12 are receiving-volume additions; B12 strength is absent, so its stored 10 g/L is unsupported. Sulfide strength/dose does not preserve the stored rate; bicarbonate percent basis is unknown.

### f2: Named SL10 addition lacks a resolved stock identity

major / open / confirmed; issue key: culturemech.000992.sl10-identity-scope.

The record stores SL10 as a direct mass ingredient and contains no resolved stock composition. A standard current SL10 subsection is available but exact historical transfer is not established.

### f3: Later owner quotations lack recoverable original response bytes

minor / open / confirmed; issue key: culturemech.000992.historical-evidence-limit.

Eleven October 7 amount claims and the reference survive only through attached quotations and local derivative reports. Their literal matches are confirmed, but raw response authentication is unavailable; generated target also lacks the later evidence.

## Recommended Actions And Acceptance Checks

### a1

Represent the exact volume doses, supplied strengths and receiving bases with source evidence. Keep unknown B12 strength and percent/final-volume limits explicit; do not manufacture replacement mass concentrations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve the precise named stock version from authoritative source linkage before populating its composition. Preserve the candidate as context and do not transfer other parent formulas.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve old evidence and history, add current primary claim-level support with exact initial-stage scope, and retain the historical raw limitation until exact bytes are recovered. Regenerate evidence only after authorized owner verification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch031/303/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-031/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch031/303/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml:1:id: CultureMech:000992<br>./data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml:1:id: CultureMech:000992<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch031/source-preflight-bound/303/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 17 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch031/source-preflight-bound/303/evidence-context-original.json; Whole target, all maintained owners and scoped dependencies | context_only | All frozen local-record objects match fresh inspected YAML. Source interpretations are separately checked against actual bound raw/text bytes. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf; Page 1 entire main table, initial make-up sentence and three post-autoclave rows | supports | Initial water make-up is explicitly to one litre; later stocks are dosed per 10 mL of receiving medium. Bicarbonate percent basis and B12 stock strength are unspecified. |
| sl10-candidate | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf; Trace element solution SL-10 subsection only | context_only | Current standard candidate has ten listed ingredients/reagents, including water, and explicit final stock make-up. DSMZ 1521 does not name DSMZ 320 or authenticate this exact historical dependency version. No other DSMZ 320 section transfers. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch031/303/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15361 resolves to pyruvate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi24996 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_24996; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:24996 resolves to lactate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53258 resolves to sodium citrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62947 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62947; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62947 resolves to ammonium acetate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15361": [{"label": "Pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:15361", "preferred_term": "Pyruvate", "ontology_id": "CHEBI:15361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:24996": [{"label": "Lactate", "match_type": "preferred_term", "identifier": "CHEBI:24996", "preferred_term": "Lactate", "ontology_id": "CHEBI:24996", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53258": [{"label": "Trisodium citrate", "match_type": "preferred_term", "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:62947": [{"label": "Ammonium acetate", "match_type": "preferred_term", "identifier": "CHEBI:62947", "preferred_term": "Ammonium acetate", "ontology_id": "CHEBI:62947", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml", "events": 7, "timestamp_issues": []}] |
| historical-derivatives | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/arcobacter_anaerophilus_medium.yaml.md; Full derivative report and eleven matching owner snippets, decoded &lt;br&gt; line breaks; source hash/time retained | context_only | {"owner_claims": [{"field_path": "ingredients[0].evidence[0]", "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 3.67417,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[0].concentration (KH2PO4) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.", "decoded_source_object": {"recipe_order": 1, "compound": "KH2PO4", "compound_id": 11, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 3.67417, "optional": 0}}, {"field_path": "ingredients[1].evidence[0]", "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 342.231,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[1].concentration (NaCl) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=20; check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) = 20 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.", "decoded_source_object": {"recipe_order": 2, "compound": "NaCl", "compound_id": 43, "amount": 20, "unit": "g", "g_l": 20, "mmol_l": 342.231, "optional": 0}}, {"field_path": "ingredients[2].evidence[0]", "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.70051,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[2].concentration (CaCl2 x 2 H2O) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=0.25; check: 0.25 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.25 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.", "decoded_source_object": {"recipe_order": 3, "compound": "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.25, "unit": "g", "g_l": 0.25, "mmol_l": 1.70051, "optional": 0}}, {"field_path": "ingredients[3].evidence[0]", "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.05719,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[3].concentration (MgSO4 x 7 H2O) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=1; check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.", "decoded_source_object": {"recipe_order": 4, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 4.05719, "optional": 0}}, {"field_path": "ingredients[4].evidence[0]", "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 9.34754,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[4].concentration (NH4Cl) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.", "decoded_source_object": {"recipe_order": 5, "compound": "NH4Cl", "compound_id": 42, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 9.34754, "optional": 0}}, {"field_path": "ingredients[5].evidence[0]", "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Sodium citrate\",\n                        \"compound_id\": 792,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.16248,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[5].concentration (Sodium citrate) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=0.3; check: 0.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.", "decoded_source_object": {"recipe_order": 6, "compound": "Sodium citrate", "compound_id": 792, "amount": 0.3, "unit": "g", "g_l": 0.3, "mmol_l": 1.16248, "optional": 0}}, {"field_path": "ingredients[6].evidence[0]", "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[6].concentration (Yeast extract) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.", "decoded_source_object": {"recipe_order": 7, "compound": "Yeast extract", "compound_id": 16, "amount": 0.5, "unit": "g", "g_l": 0.5, "optional": 0}}, {"field_path": "ingredients[7].evidence[0]", "snippet": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Ammonium acetate\",\n                        \"compound_id\": 58,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 12.9735,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[7].concentration (Ammonium acetate) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[7]. Provider explicitly reports g_l=1; check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.", "decoded_source_object": {"recipe_order": 8, "compound": "Ammonium acetate", "compound_id": 58, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 12.9735, "optional": 0}}, {"field_path": "ingredients[8].evidence[0]", "snippet": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Lactate\",\n                        \"compound_id\": 1385,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 11.2271,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[8].concentration (Lactate) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[8]. Provider explicitly reports g_l=1; check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.", "decoded_source_object": {"recipe_order": 9, "compound": "Lactate", "compound_id": 1385, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 11.2271, "optional": 0}}, {"field_path": "ingredients[9].evidence[0]", "snippet": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Pyruvate\",\n                        \"compound_id\": 1386,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 11.4877,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[9].concentration (Pyruvate) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[9]. Provider explicitly reports g_l=1; check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.", "decoded_source_object": {"recipe_order": 10, "compound": "Pyruvate", "compound_id": 1386, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 11.4877, "optional": 0}}, {"field_path": "ingredients[11].evidence[0]", "snippet": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00436319,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[11].concentration (Resazurin) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[11]. Provider explicitly reports g_l=0.001; check: 1 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.001 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.", "decoded_source_object": {"recipe_order": 12, "compound": "Resazurin", "compound_id": 25, "amount": 1, "unit": "mg", "g_l": 0.001, "mmol_l": 0.00436319, "optional": 0}}], "raw_search": {"receipt_path": "/private/tmp/culturemech-review-source-preflight-batch031/historical-1521-1482-search.json", "receipt_sha256": "88203761e99c7dca822676e95b916c7c099d15cf3b2d4112153f6ca0ad138388", "result": "No exact raw or embedded body matches among4590 candidates across107 owned roots, ignored/hidden included. Candidate scope only; no universal absence claim."}, "limit": "Derivative equality is not recovery or authentication of original response bytes."} |
| current-code-0 | src/culturemech/import/mediadive_importer.py; Current scoped code; no historical-version inference | context_only | Current importer primary/stock separation and fallback unit maps do not prove which historical writer generated these persisted values. Preserve the later owner evidence/history, correct stage-specific stock representation with primary evidence and regenerate only after separately authorized maintained-input changes. |
| current-code-1 | scripts/cleanup_media_quality.py; Current scoped code; no historical-version inference | context_only | Current importer primary/stock separation and fallback unit maps do not prove which historical writer generated these persisted values. Preserve the later owner evidence/history, correct stage-specific stock representation with primary evidence and regenerate only after separately authorized maintained-input changes. |
| current-code-2 | src/culturemech/merge/merge_recipes.py; Current scoped code; no historical-version inference | context_only | Current importer primary/stock separation and fallback unit maps do not prove which historical writer generated these persisted values. Preserve the later owner evidence/history, correct stage-specific stock representation with primary evidence and regenerate only after separately authorized maintained-input changes. |
| mediadive1521api-attempt | https://mediadive.dsmz.de/rest/medium/1521; Preserved exact public retrieval result | context_only | Current exact API attempt returned HTTP 503. The current primary remains available; original historical-response authentication is a distinct required check below. |
| mediadive1521api_retry-attempt | https://mediadive.dsmz.de/rest/medium/1521; Preserved exact public retrieval result | context_only | Current exact API attempt returned HTTP 503. The current primary remains available; original historical-response authentication is a distinct required check below. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Current exact API attempt returned HTTP 503. The current primary remains available; original historical-response authentication is a distinct required check below.
- Current exact API attempt returned HTTP 503. The current primary remains available; original historical-response authentication is a distinct required check below.
- Required authentication of the eleven cited historical amount snippets against original response bytes is unavailable after the bounded ignored-inclusive search. Derivative matches and current primary agreement do not authenticate that response.
- The exact version/composition correspondence of DSMZ 1521 SL10 to the captured current DSMZ 320 candidate remains unestablished; required complete-stock identity review is therefore partial.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T172702Z-culturemech-000992-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: arcobacter_anaerophilus_medium (CultureMech:000992)'
started_at: '2026-10-21T17:21:18Z'
finished_at: '2026-10-21T17:27:02Z'
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
summary: DSMZ 1521 verifies the initial one-litre formulation and explicitly separates
  three later additions per 10 mL receiving medium. The local SL10 mass unit and final
  bicarbonate/sulfide/B12 rates do not preserve that source scope. Eleven later owner
  amount claims survive as exact local derivative quotations, but their cited historical
  raw response is unavailable. The named SL10 stock has a current standard candidate
  whose historical applicability is unestablished. Those required source checks keep
  this review partial; no unknown stock strength or final supplemented volume is invented.
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
  - path: data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml
    sha256: deba19c4fd58ffea20ef63a2951f02adc345f84d1c0219dc4db227225825fbf2
    role: target
  - path: data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml
    sha256: 96cb6a4c7e9e75b15a8d1c6fcf4ec3e89bc9199226becd9145870bedefd36e64
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
    sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/arcobacter_anaerophilus_medium.yaml.md
    sha256: 4f94693bef32944157cc9fd3affe8e03c95e19498a948ccf9b93fb2248fc69b6
    role: context
  - path: reports/ingredient_concentration_curation/20261007-medium-source-fetch-1500-2000.json
    sha256: b6856e96be7c57a5ae4f670acf8869af50abbd0b8b52aa087ebe850b48fc7472
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
  selection: Task review 303; batch 031 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty task batches contain
    300 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 303 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000992
targets:
- target_id: CultureMech:000992
  path: data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml
  label: arcobacter_anaerophilus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch031/303/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-031/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch031/303/strict.tsv"
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000992
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
  - CultureMech:000992
- check_id: mediadive1521api-source-access
  name: 'Exact source content access: mediadive1521api'
  required: false
  status: unavailable
  summary: Current exact API attempt returned HTTP 503. The current primary remains
    available; original historical-response authentication is a distinct required
    check below.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - mediadive1521api-attempt
- check_id: mediadive1521api_retry-source-access
  name: 'Exact source content access: mediadive1521api_retry'
  required: false
  status: unavailable
  summary: Current exact API attempt returned HTTP 503. The current primary remains
    available; original historical-response authentication is a distinct required
    check below.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - mediadive1521api_retry-attempt
- check_id: historical-raw-authentication
  name: Required source-scope verification
  required: true
  status: unavailable
  summary: Required authentication of the eleven cited historical amount snippets
    against original response bytes is unavailable after the bounded ignored-inclusive
    search. Derivative matches and current primary agreement do not authenticate that
    response.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - historical-derivatives
- check_id: sl10-version-correspondence
  name: Required source-scope verification
  required: true
  status: unavailable
  summary: The exact version/composition correspondence of DSMZ 1521 SL10 to the captured
    current DSMZ 320 candidate remains unestablished; required complete-stock identity
    review is therefore partial.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - primary
  - sl10-candidate
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T17:27:01Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T17:27:01Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:21:40.524241Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch031/303/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T17:21:41.719147Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-031/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch031/303/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:21:43.033306Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:21:43.875978Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T17:27:01Z'
  support: supports
  summary: './data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml:1:id: CultureMech:000992

    ./data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml:1:id: CultureMech:000992

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch031/source-preflight-bound/303/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T17:27:01Z'
  support: supports
  summary: 17 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 040a2baca80be42c65e4a9d6a8c0d5eba731ba879ec1861df18cc45f4bddfc7a
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch031/source-preflight-bound/303/evidence-context-original.json
  locator: Whole target, all maintained owners and scoped dependencies
  accessed_at: '2026-10-21T17:27:01Z'
  support: context_only
  summary: All frozen local-record objects match fresh inspected YAML. Source interpretations
    are separately checked against actual bound raw/text bytes.
  snapshot_sha256: c80e56065f88b449225b916d9a060b723a1eea31a2c866ad0bfc154189b916d0
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf
  locator: Page 1 entire main table, initial make-up sentence and three post-autoclave
    rows
  accessed_at: '2026-10-21T17:04:21.789162Z'
  support: supports
  summary: Initial water make-up is explicitly to one litre; later stocks are dosed
    per 10 mL of receiving medium. Bicarbonate percent basis and B12 stock strength
    are unspecified.
  snapshot_sha256: d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1
- evidence_id: sl10-candidate
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf
  locator: Trace element solution SL-10 subsection only
  accessed_at: '2026-10-21T13:20:08.151265Z'
  support: context_only
  summary: Current standard candidate has ten listed ingredients/reagents, including
    water, and explicit final stock make-up. DSMZ 1521 does not name DSMZ 320 or authenticate
    this exact historical dependency version. No other DSMZ 320 section transfers.
  snapshot_sha256: d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch031/303/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T17:27:01Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 29d92983bde573af1b4bcf5334067aa5faaf375d442282f756ec1a89b0bae997
- evidence_id: chebi15361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15361
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T17:04:22.664513Z'
  support: supports
  summary: CHEBI:15361 resolves to pyruvate. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 961a069a15db5bfd8c497d805e6d3cfb6ac1dc89ca248f4f22e208c407b993d2
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
- evidence_id: chebi24996
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_24996
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T17:04:23.023259Z'
  support: supports
  summary: CHEBI:24996 resolves to lactate. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b3a9204504070e4fb25b8b870fd28f2b813d300dfc972c575fe520fe3fb71fb3
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
- evidence_id: chebi62947
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62947
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T17:04:23.300088Z'
  support: supports
  summary: CHEBI:62947 resolves to ammonium acetate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: caa2e7e9de39722329ac91e1aa80b75bd295aba5348f48c2380c0ffc0795434b
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T17:27:01Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15361":
    [{"label": "Pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:15361",
    "preferred_term": "Pyruvate", "ontology_id": "CHEBI:15361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:24996": [{"label": "Lactate", "match_type": "preferred_term", "identifier":
    "CHEBI:24996", "preferred_term": "Lactate", "ontology_id": "CHEBI:24996", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type":
    "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id":
    "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53258":
    [{"label": "Trisodium citrate", "match_type": "preferred_term", "identifier":
    "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:62947": [{"label":
    "Ammonium acetate", "match_type": "preferred_term", "identifier": "CHEBI:62947",
    "preferred_term": "Ammonium acetate", "ontology_id": "CHEBI:62947", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209":
    [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term",
    "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T17:27:01Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: historical-derivatives
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/arcobacter_anaerophilus_medium.yaml.md
  locator: Full derivative report and eleven matching owner snippets, decoded <br>
    line breaks; source hash/time retained
  accessed_at: '2026-10-21T17:27:01Z'
  support: context_only
  summary: '{"owner_claims": [{"field_path": "ingredients[0].evidence[0]", "snippet":
    "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 3.67417,\n                        \"optional\":
    0\n                    }", "explanation": "Concentration evidence for ingredients[0].concentration
    (KH2PO4) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[0]. Provider
    explicitly reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) =
    0.5 g/L. This supports the provider-declared main-recipe concentration, not an
    independently measured final volume, a stock composition, or a downstream assay
    dilution. Water alone does not establish final volume. Exact source ingredient
    labels/forms are matched; secondary ontology mappings are not validated by this
    evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved
    2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.",
    "decoded_source_object": {"recipe_order": 1, "compound": "KH2PO4", "compound_id":
    11, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 3.67417, "optional": 0}},
    {"field_path": "ingredients[1].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\":
    342.231,\n                        \"optional\": 0\n                    }", "explanation":
    "Concentration evidence for ingredients[1].concentration (NaCl) in MediaDive medium
    1521; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=20;
    check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) = 20 g/L. This supports the provider-declared
    main-recipe concentration, not an independently measured final volume, a stock
    composition, or a downstream assay dilution. Water alone does not establish final
    volume. Exact source ingredient labels/forms are matched; secondary ontology mappings
    are not validated by this evidence. Additional exact value at $.data.solutions[0].volume
    (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.",
    "decoded_source_object": {"recipe_order": 2, "compound": "NaCl", "compound_id":
    43, "amount": 20, "unit": "g", "g_l": 20, "mmol_l": 342.231, "optional": 0}},
    {"field_path": "ingredients[2].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.70051,\n                        \"optional\": 0\n                    }", "explanation":
    "Concentration evidence for ingredients[2].concentration (CaCl2 x 2 H2O) in MediaDive
    medium 1521; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports
    g_l=0.25; check: 0.25 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.25 g/L. This supports
    the provider-declared main-recipe concentration, not an independently measured
    final volume, a stock composition, or a downstream assay dilution. Water alone
    does not establish final volume. Exact source ingredient labels/forms are matched;
    secondary ontology mappings are not validated by this evidence. Additional exact
    value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00;
    response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.",
    "decoded_source_object": {"recipe_order": 3, "compound": "CaCl2 x 2 H2O", "compound_id":
    7, "amount": 0.25, "unit": "g", "g_l": 0.25, "mmol_l": 1.70051, "optional": 0}},
    {"field_path": "ingredients[3].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    4.05719,\n                        \"optional\": 0\n                    }", "explanation":
    "Concentration evidence for ingredients[3].concentration (MgSO4 x 7 H2O) in MediaDive
    medium 1521; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports
    g_l=1; check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L. This supports the
    provider-declared main-recipe concentration, not an independently measured final
    volume, a stock composition, or a downstream assay dilution. Water alone does
    not establish final volume. Exact source ingredient labels/forms are matched;
    secondary ontology mappings are not validated by this evidence. Additional exact
    value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00;
    response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.",
    "decoded_source_object": {"recipe_order": 4, "compound": "MgSO4 x 7 H2O", "compound_id":
    8, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 4.05719, "optional": 0}}, {"field_path":
    "ingredients[4].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    9.34754,\n                        \"optional\": 0\n                    }", "explanation":
    "Concentration evidence for ingredients[4].concentration (NH4Cl) in MediaDive
    medium 1521; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports
    g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports
    the provider-declared main-recipe concentration, not an independently measured
    final volume, a stock composition, or a downstream assay dilution. Water alone
    does not establish final volume. Exact source ingredient labels/forms are matched;
    secondary ontology mappings are not validated by this evidence. Additional exact
    value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00;
    response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.",
    "decoded_source_object": {"recipe_order": 5, "compound": "NH4Cl", "compound_id":
    42, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 9.34754, "optional": 0}},
    {"field_path": "ingredients[5].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Sodium citrate\",\n                        \"compound_id\":
    792,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.16248,\n                        \"optional\": 0\n                    }", "explanation":
    "Concentration evidence for ingredients[5].concentration (Sodium citrate) in MediaDive
    medium 1521; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports
    g_l=0.3; check: 0.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.3 g/L. This supports
    the provider-declared main-recipe concentration, not an independently measured
    final volume, a stock composition, or a downstream assay dilution. Water alone
    does not establish final volume. Exact source ingredient labels/forms are matched;
    secondary ontology mappings are not validated by this evidence. Additional exact
    value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00;
    response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.",
    "decoded_source_object": {"recipe_order": 6, "compound": "Sodium citrate", "compound_id":
    792, "amount": 0.3, "unit": "g", "g_l": 0.3, "mmol_l": 1.16248, "optional": 0}},
    {"field_path": "ingredients[6].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\":
    0\n                    }", "explanation": "Concentration evidence for ingredients[6].concentration
    (Yeast extract) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[6].
    Provider explicitly reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml
    per L) = 0.5 g/L. This supports the provider-declared main-recipe concentration,
    not an independently measured final volume, a stock composition, or a downstream
    assay dilution. Water alone does not establish final volume. Exact source ingredient
    labels/forms are matched; secondary ontology mappings are not validated by this
    evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved
    2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.",
    "decoded_source_object": {"recipe_order": 7, "compound": "Yeast extract", "compound_id":
    16, "amount": 0.5, "unit": "g", "g_l": 0.5, "optional": 0}}, {"field_path": "ingredients[7].evidence[0]",
    "snippet": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Ammonium acetate\",\n                        \"compound_id\": 58,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 12.9735,\n                        \"optional\":
    0\n                    }", "explanation": "Concentration evidence for ingredients[7].concentration
    (Ammonium acetate) in MediaDive medium 1521; locator=$.data.solutions[0].recipe[7].
    Provider explicitly reports g_l=1; check: 1 g * 1 g/g / (1000 ml / 1000 ml per
    L) = 1 g/L. This supports the provider-declared main-recipe concentration, not
    an independently measured final volume, a stock composition, or a downstream assay
    dilution. Water alone does not establish final volume. Exact source ingredient
    labels/forms are matched; secondary ontology mappings are not validated by this
    evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved
    2026-10-07T13:43:00.338973+00:00; response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.",
    "decoded_source_object": {"recipe_order": 8, "compound": "Ammonium acetate", "compound_id":
    58, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 12.9735, "optional": 0}}, {"field_path":
    "ingredients[8].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Lactate\",\n                        \"compound_id\":
    1385,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    11.2271,\n                        \"optional\": 0\n                    }", "explanation":
    "Concentration evidence for ingredients[8].concentration (Lactate) in MediaDive
    medium 1521; locator=$.data.solutions[0].recipe[8]. Provider explicitly reports
    g_l=1; check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L. This supports the
    provider-declared main-recipe concentration, not an independently measured final
    volume, a stock composition, or a downstream assay dilution. Water alone does
    not establish final volume. Exact source ingredient labels/forms are matched;
    secondary ontology mappings are not validated by this evidence. Additional exact
    value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00;
    response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.",
    "decoded_source_object": {"recipe_order": 9, "compound": "Lactate", "compound_id":
    1385, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 11.2271, "optional": 0}},
    {"field_path": "ingredients[9].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Pyruvate\",\n                        \"compound_id\":
    1386,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    11.4877,\n                        \"optional\": 0\n                    }", "explanation":
    "Concentration evidence for ingredients[9].concentration (Pyruvate) in MediaDive
    medium 1521; locator=$.data.solutions[0].recipe[9]. Provider explicitly reports
    g_l=1; check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L. This supports the
    provider-declared main-recipe concentration, not an independently measured final
    volume, a stock composition, or a downstream assay dilution. Water alone does
    not establish final volume. Exact source ingredient labels/forms are matched;
    secondary ontology mappings are not validated by this evidence. Additional exact
    value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00;
    response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.",
    "decoded_source_object": {"recipe_order": 10, "compound": "Pyruvate", "compound_id":
    1386, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 11.4877, "optional": 0}},
    {"field_path": "ingredients[11].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00436319,\n                        \"optional\": 0\n                    }",
    "explanation": "Concentration evidence for ingredients[11].concentration (Resazurin)
    in MediaDive medium 1521; locator=$.data.solutions[0].recipe[11]. Provider explicitly
    reports g_l=0.001; check: 1 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.001
    g/L. This supports the provider-declared main-recipe concentration, not an independently
    measured final volume, a stock composition, or a downstream assay dilution. Water
    alone does not establish final volume. Exact source ingredient labels/forms are
    matched; secondary ontology mappings are not validated by this evidence. Additional
    exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:00.338973+00:00;
    response SHA256=13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b.",
    "decoded_source_object": {"recipe_order": 12, "compound": "Resazurin", "compound_id":
    25, "amount": 1, "unit": "mg", "g_l": 0.001, "mmol_l": 0.00436319, "optional":
    0}}], "raw_search": {"receipt_path": "/private/tmp/culturemech-review-source-preflight-batch031/historical-1521-1482-search.json",
    "receipt_sha256": "88203761e99c7dca822676e95b916c7c099d15cf3b2d4112153f6ca0ad138388",
    "result": "No exact raw or embedded body matches among4590 candidates across107
    owned roots, ignored/hidden included. Candidate scope only; no universal absence
    claim."}, "limit": "Derivative equality is not recovery or authentication of original
    response bytes."}'
  snapshot_sha256: 4f94693bef32944157cc9fd3affe8e03c95e19498a948ccf9b93fb2248fc69b6
- evidence_id: current-code-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current scoped code; no historical-version inference
  accessed_at: '2026-10-21T17:27:01Z'
  support: context_only
  summary: Current importer primary/stock separation and fallback unit maps do not
    prove which historical writer generated these persisted values. Preserve the later
    owner evidence/history, correct stage-specific stock representation with primary
    evidence and regenerate only after separately authorized maintained-input changes.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: current-code-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current scoped code; no historical-version inference
  accessed_at: '2026-10-21T17:27:01Z'
  support: context_only
  summary: Current importer primary/stock separation and fallback unit maps do not
    prove which historical writer generated these persisted values. Preserve the later
    owner evidence/history, correct stage-specific stock representation with primary
    evidence and regenerate only after separately authorized maintained-input changes.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: current-code-2
  kind: record_content
  reference: src/culturemech/merge/merge_recipes.py
  locator: Current scoped code; no historical-version inference
  accessed_at: '2026-10-21T17:27:01Z'
  support: context_only
  summary: Current importer primary/stock separation and fallback unit maps do not
    prove which historical writer generated these persisted values. Preserve the later
    owner evidence/history, correct stage-specific stock representation with primary
    evidence and regenerate only after separately authorized maintained-input changes.
  snapshot_sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
- evidence_id: mediadive1521api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1521
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:04:20.932591Z'
  support: context_only
  summary: Current exact API attempt returned HTTP 503. The current primary remains
    available; original historical-response authentication is a distinct required
    check below.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive1521api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1521
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:05:12.222916Z'
  support: context_only
  summary: Current exact API attempt returned HTTP 503. The current primary remains
    available; original historical-response authentication is a distinct required
    check below.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 28 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    KH2PO4 initial-medium amount\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[0].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_batch_amount\": \"0.50\",\n      \"source_unit\": \"g\",\n\
    \      \"initial_medium_volume_L\": 1,\n      \"later_supplemented_volume_L\"\
    : null\n    },\n    \"rationale\": \"The current primary independently supports\
    \ this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks\
    \ evidence; owner has a historical quoted claim whose raw response is not authenticated.\
    \ Preserve it and add current primary stage evidence rather than marking historical\
    \ bytes verified or treating the value as a final supplemented-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial table: KH2PO4\",\n        \"\
    exact_source_quote\": \"KH2PO4 0.50 g\",\n        \"snapshot_sha256\": \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\"\
    ,\n        \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial make-up instruction\",\n    \
    \    \"exact_source_quote\": \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\": \"NaCl\
    \ initial-medium amount\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[1].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_batch_amount\": \"20.00\",\n      \"source_unit\": \"g\"\
    ,\n      \"initial_medium_volume_L\": 1,\n      \"later_supplemented_volume_L\"\
    : null\n    },\n    \"rationale\": \"The current primary independently supports\
    \ this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks\
    \ evidence; owner has a historical quoted claim whose raw response is not authenticated.\
    \ Preserve it and add current primary stage evidence rather than marking historical\
    \ bytes verified or treating the value as a final supplemented-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial table: NaCl\",\n        \"exact_source_quote\"\
    : \"NaCl 20.00 g\",\n        \"snapshot_sha256\": \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\"\
    ,\n        \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial make-up instruction\",\n    \
    \    \"exact_source_quote\": \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\": \"CaCl2\
    \ x 2 H2O initial-medium amount\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[2].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_batch_amount\": \"0.25\",\n      \"source_unit\": \"g\",\n\
    \      \"initial_medium_volume_L\": 1,\n      \"later_supplemented_volume_L\"\
    : null\n    },\n    \"rationale\": \"The current primary independently supports\
    \ this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks\
    \ evidence; owner has a historical quoted claim whose raw response is not authenticated.\
    \ Preserve it and add current primary stage evidence rather than marking historical\
    \ bytes verified or treating the value as a final supplemented-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial table: CaCl2 x 2 H2O\",\n   \
    \     \"exact_source_quote\": \"CaCl2 x 2 H2O 0.25 g\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial make-up instruction\",\n    \
    \    \"exact_source_quote\": \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\": \"MgSO4\
    \ x 7 H2O initial-medium amount\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[3].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_batch_amount\": \"1.00\",\n      \"source_unit\": \"g\",\n\
    \      \"initial_medium_volume_L\": 1,\n      \"later_supplemented_volume_L\"\
    : null\n    },\n    \"rationale\": \"The current primary independently supports\
    \ this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks\
    \ evidence; owner has a historical quoted claim whose raw response is not authenticated.\
    \ Preserve it and add current primary stage evidence rather than marking historical\
    \ bytes verified or treating the value as a final supplemented-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial table: MgSO4 x 7 H2O\",\n   \
    \     \"exact_source_quote\": \"MgSO4 x 7 H2O 1.00 g\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial make-up instruction\",\n    \
    \    \"exact_source_quote\": \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\": \"NH4Cl\
    \ initial-medium amount\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[4].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_batch_amount\": \"0.50\",\n      \"source_unit\": \"g\",\n\
    \      \"initial_medium_volume_L\": 1,\n      \"later_supplemented_volume_L\"\
    : null\n    },\n    \"rationale\": \"The current primary independently supports\
    \ this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks\
    \ evidence; owner has a historical quoted claim whose raw response is not authenticated.\
    \ Preserve it and add current primary stage evidence rather than marking historical\
    \ bytes verified or treating the value as a final supplemented-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial table: NH4Cl\",\n        \"exact_source_quote\"\
    : \"NH4Cl 0.50 g\",\n        \"snapshot_sha256\": \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\"\
    ,\n        \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial make-up instruction\",\n    \
    \    \"exact_source_quote\": \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\": \"Sodium\
    \ citrate initial-medium amount\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[5].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_batch_amount\": \"0.3\",\n      \"source_unit\": \"g\",\n\
    \      \"initial_medium_volume_L\": 1,\n      \"later_supplemented_volume_L\"\
    : null\n    },\n    \"rationale\": \"The current primary independently supports\
    \ this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks\
    \ evidence; owner has a historical quoted claim whose raw response is not authenticated.\
    \ Preserve it and add current primary stage evidence rather than marking historical\
    \ bytes verified or treating the value as a final supplemented-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial table: Sodium citrate\",\n  \
    \      \"exact_source_quote\": \"Sodium citrate 0.3 g\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial make-up instruction\",\n    \
    \    \"exact_source_quote\": \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\": \"Yeast\
    \ extract initial-medium amount\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[6].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_batch_amount\": \"0.50\",\n      \"source_unit\": \"g\",\n\
    \      \"initial_medium_volume_L\": 1,\n      \"later_supplemented_volume_L\"\
    : null\n    },\n    \"rationale\": \"The current primary independently supports\
    \ this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks\
    \ evidence; owner has a historical quoted claim whose raw response is not authenticated.\
    \ Preserve it and add current primary stage evidence rather than marking historical\
    \ bytes verified or treating the value as a final supplemented-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial table: Yeast extract\",\n   \
    \     \"exact_source_quote\": \"Yeast extract 0.50 g\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial make-up instruction\",\n    \
    \    \"exact_source_quote\": \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\": \"Ammonium\
    \ acetate initial-medium amount\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[7].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_batch_amount\": \"1.00\",\n      \"source_unit\": \"g\",\n\
    \      \"initial_medium_volume_L\": 1,\n      \"later_supplemented_volume_L\"\
    : null\n    },\n    \"rationale\": \"The current primary independently supports\
    \ this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks\
    \ evidence; owner has a historical quoted claim whose raw response is not authenticated.\
    \ Preserve it and add current primary stage evidence rather than marking historical\
    \ bytes verified or treating the value as a final supplemented-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial table: Ammonium acetate\",\n\
    \        \"exact_source_quote\": \"Ammonium acetate 1.00 g\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial make-up instruction\",\n    \
    \    \"exact_source_quote\": \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\": \"Lactate\
    \ initial-medium amount\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[8].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_batch_amount\": \"1.00\",\n      \"source_unit\": \"g\",\n\
    \      \"initial_medium_volume_L\": 1,\n      \"later_supplemented_volume_L\"\
    : null\n    },\n    \"rationale\": \"The current primary independently supports\
    \ this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks\
    \ evidence; owner has a historical quoted claim whose raw response is not authenticated.\
    \ Preserve it and add current primary stage evidence rather than marking historical\
    \ bytes verified or treating the value as a final supplemented-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial table: Lactate\",\n        \"\
    exact_source_quote\": \"Lactate 1.00 g\",\n        \"snapshot_sha256\": \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\"\
    ,\n        \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial make-up instruction\",\n    \
    \    \"exact_source_quote\": \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\": \"Pyruvate\
    \ initial-medium amount\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[9].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_batch_amount\": \"1.00\",\n      \"source_unit\": \"g\",\n\
    \      \"initial_medium_volume_L\": 1,\n      \"later_supplemented_volume_L\"\
    : null\n    },\n    \"rationale\": \"The current primary independently supports\
    \ this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks\
    \ evidence; owner has a historical quoted claim whose raw response is not authenticated.\
    \ Preserve it and add current primary stage evidence rather than marking historical\
    \ bytes verified or treating the value as a final supplemented-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial table: Pyruvate\",\n        \"\
    exact_source_quote\": \"Pyruvate 1.00 g\",\n        \"snapshot_sha256\": \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\"\
    ,\n        \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial make-up instruction\",\n    \
    \    \"exact_source_quote\": \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\": \"Resazurin\
    \ initial-medium amount\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_batch_amount\": \"1.00\",\n      \"source_unit\": \"mg\"\
    ,\n      \"initial_medium_volume_L\": 1,\n      \"later_supplemented_volume_L\"\
    : null\n    },\n    \"rationale\": \"The current primary independently supports\
    \ this initial-medium value, including 1 mg = 0.001 g resazurin. Target lacks\
    \ evidence; owner has a historical quoted claim whose raw response is not authenticated.\
    \ Preserve it and add current primary stage evidence rather than marking historical\
    \ bytes verified or treating the value as a final supplemented-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial table: Resazurin\",\n       \
    \ \"exact_source_quote\": \"Resazurin 1.00 mg\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial make-up instruction\",\n    \
    \    \"exact_source_quote\": \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\": \"SL10\
    \ stock receiving dose\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"dose_ml\": 1,\n      \"initial_medium_volume_L\": 1,\n      \"stock_formula_historical_identity\"\
    : \"unresolved\"\n    },\n    \"rationale\": \"The source gives a stock volume,\
    \ not a gram. Restore the one-millilitre dose and separately resolve the stock\
    \ identity; the initial litre basis does not authenticate a candidate stock version.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial table SL10 row\",\n        \"\
    exact_source_quote\": \"SL10 1.0 ml\",\n        \"snapshot_sha256\": \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\"\
    ,\n        \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, initial make-up\",\n        \"exact_source_quote\"\
    : \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\": \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\"\
    ,\n        \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\": \"Bicarbonate\
    \ addition\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_percent\": 10,\n      \"percent_basis\": null,\n      \"dose_uL\"\
    : 150,\n      \"receiving_medium_ml\": 10,\n      \"completed_final_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Preserve the source stock strength where\
    \ given and the receiving-medium basis. Unqualified 10% cannot establish a mass\
    \ concentration.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, post-autoclave additions\",\n       \
    \ \"exact_source_quote\": \"NaHCO3 (10%) 150 µl/10 ml\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\": \"Sulfide\
    \ addition\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.40182\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.40182\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_molarity_M\": 1,\n      \"dose_uL\": 10,\n      \"receiving_medium_ml\"\
    : 10,\n      \"delivered_micromoles\": 10,\n      \"completed_final_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Preserve the source stock strength where\
    \ given and the receiving-medium basis. 1 M × 10 microlitres = 10 micromoles delivered;\
    \ this is not the asserted main g/L rate and no final-volume/mass conversion is\
    \ invented.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, post-autoclave additions\",\n       \
    \ \"exact_source_quote\": \"Na2S x 9 H2O (1 M) 10 µl/10 ml\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\": \"B12\
    \ addition\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"dose_uL\": 10,\n      \"receiving_medium_ml\": 10,\n      \"stock_strength\"\
    : null,\n      \"delivered_mass\": null\n    },\n    \"rationale\": \"Preserve\
    \ the source stock strength where given and the receiving-medium basis. Ten microlitres\
    \ is a volume dose, not 10 g/L; the stock has no supplied strength.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, post-autoclave additions\",\n       \
    \ \"exact_source_quote\": \"Vitamin B12 10 µl/10 ml\",\n        \"snapshot_sha256\"\
    : \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\",\n    \
    \    \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\": \"Initial\
    \ medium make-up\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add distilled water to 1 liter, boil the medium and cool under N2, distribute\
    \ under N2 and autoclave. After autoclaving the following sterilized solutions\
    \ are added:\",\n        \"decision\": \"evidence_only\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add distilled water to 1 liter, boil the medium and cool under N2, distribute\
    \ under N2 and autoclave. After autoclaving the following sterilized solutions\
    \ are added:\",\n        \"decision\": \"evidence_only\"\n      }\n    ],\n  \
    \  \"proposed_source_representation\": {\n      \"initial_final_volume_L\": 1,\n\
    \      \"stage\": \"Before post-autoclave additions\"\n    },\n    \"rationale\"\
    : \"This explicit make-up survives locally. Preserve the stage and add evidence;\
    \ later receiving doses do not retroactively establish a final supplemented litre.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1521\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, preparation sentence\",\n        \"exact_source_quote\"\
    : \"Add distilled water to 1 liter\",\n        \"snapshot_sha256\": \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\"\
    ,\n        \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\": \"Unspecified\
    \ B12 stock strength\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"B12_stock_strength\": null\n    },\n    \"rationale\": \"No fixed\
    \ stock strength is supplied. The missing mass is unknown, not zero and not a\
    \ generic vitamin convention.\",\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz1521\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1521.pdf\"\
    ,\n        \"source_locator\": \"Page 1, final addition\",\n        \"exact_source_quote\"\
    : \"Vitamin B12 10 µl/10 ml\",\n        \"snapshot_sha256\": \"d333b27ad691af2f1aa41120e09c8b531018f755d9f8186342f12a19808987e1\"\
    ,\n        \"parsed_text_sha256\": \"556985a626252ddc1d7b42a474de953f390e8c0b9989c05870a70fca3c1192b3\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:21.789162Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\": \"Candidate\
    \ standard SL10: HCl (25%)\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"candidate_source\": \"DSMZ 320 SL10\",\n      \"candidate_batch_amount\"\
    : \"10.00\",\n      \"source_unit\": \"ml\",\n      \"transfer_to_DSM1521\": \"\
    not established\"\n    },\n    \"rationale\": \"Record the inspected candidate\
    \ exactly, without inserting its composition into this target until the named\
    \ historical stock correspondence is resolved. Other parent stocks and basal procedures\
    \ are excluded; the HCl percent basis remains unstated.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz320\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\",\n        \"\
    source_locator\": \"Pages 1–2, Trace element solution SL-10 subsection\",\n  \
    \      \"exact_source_quote\": \"HCl (25%) 10.00 ml\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:20:08.151265Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\": \"Candidate\
    \ standard SL10: FeCl2 x 4 H2O\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"candidate_source\": \"DSMZ 320 SL10\",\n      \"candidate_batch_amount\"\
    : \"1.50\",\n      \"source_unit\": \"g\",\n      \"transfer_to_DSM1521\": \"\
    not established\"\n    },\n    \"rationale\": \"Record the inspected candidate\
    \ exactly, without inserting its composition into this target until the named\
    \ historical stock correspondence is resolved. Other parent stocks and basal procedures\
    \ are excluded; the HCl percent basis remains unstated.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz320\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\",\n        \"\
    source_locator\": \"Pages 1–2, Trace element solution SL-10 subsection\",\n  \
    \      \"exact_source_quote\": \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:20:08.151265Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\": \"Candidate\
    \ standard SL10: ZnCl2\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"candidate_source\": \"DSMZ 320 SL10\",\n      \"candidate_batch_amount\"\
    : \"70.00\",\n      \"source_unit\": \"mg\",\n      \"transfer_to_DSM1521\": \"\
    not established\"\n    },\n    \"rationale\": \"Record the inspected candidate\
    \ exactly, without inserting its composition into this target until the named\
    \ historical stock correspondence is resolved. Other parent stocks and basal procedures\
    \ are excluded; the HCl percent basis remains unstated.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz320\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\",\n        \"\
    source_locator\": \"Pages 1–2, Trace element solution SL-10 subsection\",\n  \
    \      \"exact_source_quote\": \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:20:08.151265Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\": \"Candidate\
    \ standard SL10: MnCl2 x 4 H2O\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"candidate_source\": \"DSMZ 320 SL10\",\n      \"candidate_batch_amount\"\
    : \"100.00\",\n      \"source_unit\": \"mg\",\n      \"transfer_to_DSM1521\":\
    \ \"not established\"\n    },\n    \"rationale\": \"Record the inspected candidate\
    \ exactly, without inserting its composition into this target until the named\
    \ historical stock correspondence is resolved. Other parent stocks and basal procedures\
    \ are excluded; the HCl percent basis remains unstated.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz320\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\",\n        \"\
    source_locator\": \"Pages 1–2, Trace element solution SL-10 subsection\",\n  \
    \      \"exact_source_quote\": \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:20:08.151265Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\": \"Candidate\
    \ standard SL10: H3BO3\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"candidate_source\": \"DSMZ 320 SL10\",\n      \"candidate_batch_amount\"\
    : \"6.00\",\n      \"source_unit\": \"mg\",\n      \"transfer_to_DSM1521\": \"\
    not established\"\n    },\n    \"rationale\": \"Record the inspected candidate\
    \ exactly, without inserting its composition into this target until the named\
    \ historical stock correspondence is resolved. Other parent stocks and basal procedures\
    \ are excluded; the HCl percent basis remains unstated.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz320\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\",\n        \"\
    source_locator\": \"Pages 1–2, Trace element solution SL-10 subsection\",\n  \
    \      \"exact_source_quote\": \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:20:08.151265Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\": \"Candidate\
    \ standard SL10: CoCl2 x 6 H2O\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"candidate_source\": \"DSMZ 320 SL10\",\n      \"candidate_batch_amount\"\
    : \"190.00\",\n      \"source_unit\": \"mg\",\n      \"transfer_to_DSM1521\":\
    \ \"not established\"\n    },\n    \"rationale\": \"Record the inspected candidate\
    \ exactly, without inserting its composition into this target until the named\
    \ historical stock correspondence is resolved. Other parent stocks and basal procedures\
    \ are excluded; the HCl percent basis remains unstated.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz320\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\",\n        \"\
    source_locator\": \"Pages 1–2, Trace element solution SL-10 subsection\",\n  \
    \      \"exact_source_quote\": \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:20:08.151265Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\": \"Candidate\
    \ standard SL10: CuCl2 x 2 H2O\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"candidate_source\": \"DSMZ 320 SL10\",\n      \"candidate_batch_amount\"\
    : \"2.00\",\n      \"source_unit\": \"mg\",\n      \"transfer_to_DSM1521\": \"\
    not established\"\n    },\n    \"rationale\": \"Record the inspected candidate\
    \ exactly, without inserting its composition into this target until the named\
    \ historical stock correspondence is resolved. Other parent stocks and basal procedures\
    \ are excluded; the HCl percent basis remains unstated.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz320\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\",\n        \"\
    source_locator\": \"Pages 1–2, Trace element solution SL-10 subsection\",\n  \
    \      \"exact_source_quote\": \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:20:08.151265Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\": \"Candidate\
    \ standard SL10: NiCl2 x 6 H2O\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"candidate_source\": \"DSMZ 320 SL10\",\n      \"candidate_batch_amount\"\
    : \"24.00\",\n      \"source_unit\": \"mg\",\n      \"transfer_to_DSM1521\": \"\
    not established\"\n    },\n    \"rationale\": \"Record the inspected candidate\
    \ exactly, without inserting its composition into this target until the named\
    \ historical stock correspondence is resolved. Other parent stocks and basal procedures\
    \ are excluded; the HCl percent basis remains unstated.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz320\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\",\n        \"\
    source_locator\": \"Pages 1–2, Trace element solution SL-10 subsection\",\n  \
    \      \"exact_source_quote\": \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:20:08.151265Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\": \"Candidate\
    \ standard SL10: Na2MoO4 x 2 H2O\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"candidate_source\": \"DSMZ 320 SL10\",\n      \"candidate_batch_amount\"\
    : \"36.00\",\n      \"source_unit\": \"mg\",\n      \"transfer_to_DSM1521\": \"\
    not established\"\n    },\n    \"rationale\": \"Record the inspected candidate\
    \ exactly, without inserting its composition into this target until the named\
    \ historical stock correspondence is resolved. Other parent stocks and basal procedures\
    \ are excluded; the HCl percent basis remains unstated.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz320\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\",\n        \"\
    source_locator\": \"Pages 1–2, Trace element solution SL-10 subsection\",\n  \
    \      \"exact_source_quote\": \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:20:08.151265Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\": \"Candidate\
    \ standard SL10: Distilled water\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"candidate_source\": \"DSMZ 320 SL10\",\n      \"candidate_batch_amount\"\
    : \"990.00\",\n      \"source_unit\": \"ml\",\n      \"transfer_to_DSM1521\":\
    \ \"not established\"\n    },\n    \"rationale\": \"Record the inspected candidate\
    \ exactly, without inserting its composition into this target until the named\
    \ historical stock correspondence is resolved. Other parent stocks and basal procedures\
    \ are excluded; the HCl percent basis remains unstated.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz320\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\",\n        \"\
    source_locator\": \"Pages 1–2, Trace element solution SL-10 subsection\",\n  \
    \      \"exact_source_quote\": \"Distilled water 990.00 ml\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:20:08.151265Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\": \"Candidate\
    \ SL10 final make-up\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"candidate_final_stock_volume_ml\": 1000,\n      \"transfer_to_DSM1521\"\
    : \"not established\"\n    },\n    \"rationale\": \"This is an explicit make-up\
    \ for the candidate stock, not proof of the missing target stock version. Retain\
    \ iron-in-acid dissolution order only within that candidate context.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz320\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\"\
    ,\n        \"source_locator\": \"Page 2, continuation of SL10 preparation\",\n\
    \        \"exact_source_quote\": \"make up to 1000.00 ml.\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:20:08.151265Z\"\n      }\n    ]\n\
    \  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '13 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 13/15
    primary and 13/15 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15361
  - chebi176843
  - chebi24996
  - chebi26710
  - chebi31206
  - chebi31795
  - chebi32139
  - chebi53258
  - chebi62947
  - chebi63036
  - chebi76209
  - chebi86158
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 15: primary 86.67%;
    secondary 86.67%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 14 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact accession and named dependency
  outcome: concern
  summary: Stable ID and DSMZ 1521 identity resolve. The source names SL10 but does
    not establish that the captured DSMZ 320 standard is the exact dependency version.
    Preserve the available candidate and resolve only this stock identity, not a whole
    parent recipe.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - record
  - owner-0
  - primary
  - sl10-candidate
- assessment_id: history-evidence
  area: evidence
  topic: Later owner claims and unavailable original response
  outcome: concern
  summary: Eleven owner-only claims match the pinned local derivative report and are
    separately corroborated for initial-medium amounts by the current primary. The
    original October 7 response SHA 13a000ccff149511952b84d730e4fed4c4c0fcca2728b99655446f7c104a866b
    is not recovered. The bounded search included hidden/ignored candidates; no universal
    absence claim is made. Target has none of these later evidence objects.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - historical-derivatives
  - primary
  - record
  - owner-0
- assessment_id: forms
  area: grounding
  topic: Supplied generic forms and exact hydrate limits
  outcome: supported
  summary: Explicit calcium, magnesium and sulfide hydrate names agree with their
    terms. Source lactate and pyruvate do not specify a counterion or stereoisomer,
    so no replacement salt or D/L claim is inferred. Resazurin is unsalted in this
    primary; the sodium-resazurin finding from other media does not transfer. Sodium
    citrate hydration remains unspecified; no unverified molecular-weight conversion
    is used.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - primary
  - chebi15361
  - chebi24996
  - chebi53258
  - chebi8806
- assessment_id: preparation
  area: completeness
  topic: Initial make-up versus later receiving additions
  outcome: concern
  summary: Local preparation retains the initial one-litre make-up, boiling/cooling
    under N2 and autoclaving but ends before the later dose rows. No gas purity, main
    pH, incubation temperature or numerical autoclave cycle is supplied. Keep later
    additions per 10 mL of receiving medium, not an assumed completed volume.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - primary
  - quantity-inventory
  - record
  - owner-0
- assessment_id: classification
  area: scope
  topic: Mixture category and organism scope
  outcome: supported
  summary: Yeast extract supports COMPLEX/UNDEFINED and the source is liquid. The
    medium title and generic cultivation application are not independent growth evidence.
    No new organism, phenotype or optimum claim is inferred.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - primary
  - record
- assessment_id: current-writers
  area: provenance
  topic: Current writers and follow-up ownership
  outcome: concern
  summary: Current importer primary/stock separation and fallback unit maps do not
    prove which historical writer generated these persisted values. Preserve the later
    owner evidence/history, correct stage-specific stock representation with primary
    evidence and regenerate only after separately authorized maintained-input changes.
  target_ids:
  - CultureMech:000992
  evidence_ids:
  - record
  - current-code-0
  - current-code-1
  - current-code-2
findings:
- finding_id: f1
  issue_key: culturemech.000992.stock-dose-representation
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock receiving doses are represented as unsupported main mass rates
  description: SL10 is 1 mL, not 1 g/L. Post-autoclave bicarbonate, sulfide and B12
    are receiving-volume additions; B12 strength is absent, so its stored 10 g/L is
    unsupported. Sulfide strength/dose does not preserve the stored rate; bicarbonate
    percent basis is unknown.
  target_ids:
  - CultureMech:000992
  field_paths:
  - ingredients[10].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
  - ingredients[14].concentration
  evidence_ids:
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml
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
  issue_key: culturemech.000992.sl10-identity-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Named SL10 addition lacks a resolved stock identity
  description: The record stores SL10 as a direct mass ingredient and contains no
    resolved stock composition. A standard current SL10 subsection is available but
    exact historical transfer is not established.
  target_ids:
  - CultureMech:000992
  field_paths:
  - ingredients[10]
  - solutions
  evidence_ids:
  - primary
  - sl10-candidate
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml
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
  issue_key: culturemech.000992.historical-evidence-limit
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Later owner quotations lack recoverable original response bytes
  description: Eleven October 7 amount claims and the reference survive only through
    attached quotations and local derivative reports. Their literal matches are confirmed,
    but raw response authentication is unavailable; generated target also lacks the
    later evidence.
  target_ids:
  - CultureMech:000992
  field_paths:
  - ingredients
  - curation_history
  evidence_ids:
  - historical-derivatives
  - primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml
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
  description: Represent the exact volume doses, supplied strengths and receiving
    bases with source evidence. Keep unknown B12 strength and percent/final-volume
    limits explicit; do not manufacture replacement mass concentrations.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000992
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml
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
  description: Resolve the precise named stock version from authoritative source linkage
    before populating its composition. Preserve the candidate as context and do not
    transfer other parent formulas.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000992
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml
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
  description: Preserve old evidence and history, add current primary claim-level
    support with exact initial-stage scope, and retain the historical raw limitation
    until exact bytes are recovered. Regenerate evidence only after authorized owner
    verification.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000992
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml
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
- Current exact API attempt returned HTTP 503. The current primary remains available;
  original historical-response authentication is a distinct required check below.
- Current exact API attempt returned HTTP 503. The current primary remains available;
  original historical-response authentication is a distinct required check below.
- Required authentication of the eleven cited historical amount snippets against original
  response bytes is unavailable after the bounded ignored-inclusive search. Derivative
  matches and current primary agreement do not authenticate that response.
- The exact version/composition correspondence of DSMZ 1521 SL10 to the captured current
  DSMZ 320 candidate remains unestablished; required complete-stock identity review
  is therefore partial.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-031
- generated-medium
```
