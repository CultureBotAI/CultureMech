# Source and formulation review: azotobacter_medium (CultureMech:005190)

- Review: 20261021T185141Z-culturemech-005190-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T18:47:03Z
- Finished UTC: 2026-10-21T18:51:41Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSMZ 3 primary supports ten batch masses, pH 7.3 and separate 950 mL main-water / 50 mL sugar-solution stages. The generated record omits those stages; the DSMZ owner retains the preparation. Twenty owner amount claims remain derivative-only because their historical API bytes were not recovered. The DSM 44106 modification is not established by the shared ingredient signature, so variant equivalence and exact rate authentication remain partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 331; batch 034 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-three task batches contain 330 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 333 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:005190 | data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml | generated | azotobacter_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:005190 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:005190 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-034/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch034/331/strict.tsv |
| validate-terms | passed | True | CultureMech:005190 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:005190 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:005190 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive3api_retry | unavailable | True | CultureMech:005190 | Both bounded current MediaDive 3 requests returned HTTP 503. The exact historical raw digest cited by twenty owner amount claims was not recovered by the documented ignored-inclusive owned-file/report search. Primary batch amounts are usable, but exact historical rate/denominator authentication remains required and unavailable. |
| Exact source content access: komodo3_44106detail | unavailable | True | CultureMech:005190 | The exact KOMODO 3_44106 detail returned HTTP 403. The catalog establishes a named modified medium but does not resolve its recipe modification or equivalence to the base; this required variant-identity check remains unavailable. |
| Exact source content access: komodo3detail | unavailable | False | CultureMech:005190 | The exact KOMODO 3 detail returned HTTP 403; base identity is independently supported by the catalog and DSMZ primary. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:005190.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:005190.

15 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Glucose batch amount versus stored rate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "One-page primary, solute row 1",
        "exact_source_quote": "Glucose 5.00 g",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "source_batch_amount": 5.0,
      "unit": "g",
      "main_g_per_L": null,
      "variant_44106_transfer": "unresolved"
    },
    "rationale": "The base-recipe mass matches the local number after mg-to-g conversion where needed; this is not evidence that the stored rate is false. The primary gives 950 mL main water plus a separate 50 mL sugar solution, not an independent final make-up declaration. Two base owners have matching derivative claims of a provider 1000 mL denominator, but the cited raw response is unavailable. The generated target and variant owner have no attached amount evidence; the variant-specific formulation is unresolved. Preserve the numerical values pending explicit basis/variant authentication rather than inventing replacement rates."
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Mannitol batch amount versus stored rate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "One-page primary, solute row 2",
        "exact_source_quote": "Mannitol 5.00 g",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "source_batch_amount": 5.0,
      "unit": "g",
      "main_g_per_L": null,
      "variant_44106_transfer": "unresolved"
    },
    "rationale": "The base-recipe mass matches the local number after mg-to-g conversion where needed; this is not evidence that the stored rate is false. The primary gives 950 mL main water plus a separate 50 mL sugar solution, not an independent final make-up declaration. Two base owners have matching derivative claims of a provider 1000 mL denominator, but the cited raw response is unavailable. The generated target and variant owner have no attached amount evidence; the variant-specific formulation is unresolved. Preserve the numerical values pending explicit basis/variant authentication rather than inventing replacement rates."
  },
  {
    "quantity_id": "q3",
    "component_or_context": "CaCl2 x 2 H2O batch amount versus stored rate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "One-page primary, solute row 3",
        "exact_source_quote": "CaCl2 x 2 H2O 0.10 g",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "source_batch_amount": 0.1,
      "unit": "g",
      "main_g_per_L": null,
      "variant_44106_transfer": "unresolved"
    },
    "rationale": "The base-recipe mass matches the local number after mg-to-g conversion where needed; this is not evidence that the stored rate is false. The primary gives 950 mL main water plus a separate 50 mL sugar solution, not an independent final make-up declaration. Two base owners have matching derivative claims of a provider 1000 mL denominator, but the cited raw response is unavailable. The generated target and variant owner have no attached amount evidence; the variant-specific formulation is unresolved. Preserve the numerical values pending explicit basis/variant authentication rather than inventing replacement rates."
  },
  {
    "quantity_id": "q4",
    "component_or_context": "MgSO4 x 7 H2O batch amount versus stored rate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "One-page primary, solute row 4",
        "exact_source_quote": "MgSO4 x 7 H2O 0.10 g",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "source_batch_amount": 0.1,
      "unit": "g",
      "main_g_per_L": null,
      "variant_44106_transfer": "unresolved"
    },
    "rationale": "The base-recipe mass matches the local number after mg-to-g conversion where needed; this is not evidence that the stored rate is false. The primary gives 950 mL main water plus a separate 50 mL sugar solution, not an independent final make-up declaration. Two base owners have matching derivative claims of a provider 1000 mL denominator, but the cited raw response is unavailable. The generated target and variant owner have no attached amount evidence; the variant-specific formulation is unresolved. Preserve the numerical values pending explicit basis/variant authentication rather than inventing replacement rates."
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Na2MoO4 x 2 H2O batch amount versus stored rate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "One-page primary, solute row 5",
        "exact_source_quote": "Na2MoO4 x 2 H2O 5.00 mg",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "source_batch_amount": 5.0,
      "unit": "mg",
      "main_g_per_L": null,
      "variant_44106_transfer": "unresolved"
    },
    "rationale": "The base-recipe mass matches the local number after mg-to-g conversion where needed; this is not evidence that the stored rate is false. The primary gives 950 mL main water plus a separate 50 mL sugar solution, not an independent final make-up declaration. Two base owners have matching derivative claims of a provider 1000 mL denominator, but the cited raw response is unavailable. The generated target and variant owner have no attached amount evidence; the variant-specific formulation is unresolved. Preserve the numerical values pending explicit basis/variant authentication rather than inventing replacement rates."
  },
  {
    "quantity_id": "q6",
    "component_or_context": "K2HPO4 batch amount versus stored rate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.9",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.9",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.9",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.9",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "One-page primary, solute row 6",
        "exact_source_quote": "K2HPO4 0.90 g",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "source_batch_amount": 0.9,
      "unit": "g",
      "main_g_per_L": null,
      "variant_44106_transfer": "unresolved"
    },
    "rationale": "The base-recipe mass matches the local number after mg-to-g conversion where needed; this is not evidence that the stored rate is false. The primary gives 950 mL main water plus a separate 50 mL sugar solution, not an independent final make-up declaration. Two base owners have matching derivative claims of a provider 1000 mL denominator, but the cited raw response is unavailable. The generated target and variant owner have no attached amount evidence; the variant-specific formulation is unresolved. Preserve the numerical values pending explicit basis/variant authentication rather than inventing replacement rates."
  },
  {
    "quantity_id": "q7",
    "component_or_context": "KH2PO4 batch amount versus stored rate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "One-page primary, solute row 7",
        "exact_source_quote": "KH2PO4 0.10 g",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "source_batch_amount": 0.1,
      "unit": "g",
      "main_g_per_L": null,
      "variant_44106_transfer": "unresolved"
    },
    "rationale": "The base-recipe mass matches the local number after mg-to-g conversion where needed; this is not evidence that the stored rate is false. The primary gives 950 mL main water plus a separate 50 mL sugar solution, not an independent final make-up declaration. Two base owners have matching derivative claims of a provider 1000 mL denominator, but the cited raw response is unavailable. The generated target and variant owner have no attached amount evidence; the variant-specific formulation is unresolved. Preserve the numerical values pending explicit basis/variant authentication rather than inventing replacement rates."
  },
  {
    "quantity_id": "q8",
    "component_or_context": "FeSO4 x 7 H2O batch amount versus stored rate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "One-page primary, solute row 8",
        "exact_source_quote": "FeSO4 x 7 H2O 0.01 g",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "source_batch_amount": 0.01,
      "unit": "g",
      "main_g_per_L": null,
      "variant_44106_transfer": "unresolved"
    },
    "rationale": "The base-recipe mass matches the local number after mg-to-g conversion where needed; this is not evidence that the stored rate is false. The primary gives 950 mL main water plus a separate 50 mL sugar solution, not an independent final make-up declaration. Two base owners have matching derivative claims of a provider 1000 mL denominator, but the cited raw response is unavailable. The generated target and variant owner have no attached amount evidence; the variant-specific formulation is unresolved. Preserve the numerical values pending explicit basis/variant authentication rather than inventing replacement rates."
  },
  {
    "quantity_id": "q9",
    "component_or_context": "CaCO3 batch amount versus stored rate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "One-page primary, solute row 9",
        "exact_source_quote": "CaCO3 5.00 g",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "source_batch_amount": 5.0,
      "unit": "g",
      "main_g_per_L": null,
      "variant_44106_transfer": "unresolved"
    },
    "rationale": "The base-recipe mass matches the local number after mg-to-g conversion where needed; this is not evidence that the stored rate is false. The primary gives 950 mL main water plus a separate 50 mL sugar solution, not an independent final make-up declaration. Two base owners have matching derivative claims of a provider 1000 mL denominator, but the cited raw response is unavailable. The generated target and variant owner have no attached amount evidence; the variant-specific formulation is unresolved. Preserve the numerical values pending explicit basis/variant authentication rather than inventing replacement rates."
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Agar batch amount versus stored rate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "One-page primary, solute row 10",
        "exact_source_quote": "Agar 15.00 g",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "source_batch_amount": 15.0,
      "unit": "g",
      "main_g_per_L": null,
      "variant_44106_transfer": "unresolved"
    },
    "rationale": "The base-recipe mass matches the local number after mg-to-g conversion where needed; this is not evidence that the stored rate is false. The primary gives 950 mL main water plus a separate 50 mL sugar solution, not an independent final make-up declaration. Two base owners have matching derivative claims of a provider 1000 mL denominator, but the cited raw response is unavailable. The generated target and variant owner have no attached amount evidence; the variant-specific formulation is unresolved. Preserve the numerical values pending explicit basis/variant authentication rather than inventing replacement rates."
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Base main-water input",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "Primary main table, water row",
        "exact_source_quote": "Distilled water 950.00 ml",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "main_water_mL": 950
    },
    "rationale": "Add the omitted base-water context separately from the sugar solution. No automatic transfer to the unresolved DSM 44106 variant is proposed."
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Separate sugar-solution water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Sterilize glucose and mannitol separately (in 50 ml H2O) and add to the medium after autoclaving. Calcium carbonate in the medium serves as a buffer. The calcium carbonate will settle in agar plates before the agar has set, producing an opaque layer in the bottom. As the strain grows and acid is produced this will react with the calcium carbonate, causing it to dissolve and form zones of clearing immediately below the colonies.",
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "Primary preparation, first line of separate-sugar instruction",
        "exact_source_quote": "Sterilize glucose and mannitol separately (in 50 ml H 2O) and add to the medium after",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "sugar_solution_water_mL": 50,
      "addition_stage": "after base autoclaving"
    },
    "rationale": "The DSMZ owner already preserves this instruction and needs claim-level evidence. The target and KOMODO base owner omit it. The 50 mL applies to the two sugars together, not to each independently."
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Base pH and unresolved variant pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.3,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.3,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.3,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml",
        "field_path": "ph_value",
        "stored": 7.3,
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "Primary preparation",
        "exact_source_quote": "Adjust pH to 7.3.",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "base_pH": 7.3,
      "variant_specific_pH": null
    },
    "rationale": "The base pH is directly supported. The catalog variant row has null pH, and the source modification is unresolved; do not treat the local inherited variant pH as independently verified."
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Final denominator versus listed water inputs",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "Main water",
        "exact_source_quote": "Distilled water 950.00 ml",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      },
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "Separate sugar-water stage",
        "exact_source_quote": "Sterilize glucose and mannitol separately (in 50 ml H 2O) and add to the medium after",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "listed_water_sum_mL": 1000,
      "measured_final_volume_mL": null
    },
    "rationale": "950 + 50 = 1000 mL is a sum of listed inputs, not a measured final volume. The historical provider denominator remains a derivative claim and is not authenticated by this arithmetic."
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Numerical sterilization cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Sterilize glucose and mannitol separately (in 50 ml H2O) and add to the medium after autoclaving. Calcium carbonate in the medium serves as a buffer. The calcium carbonate will settle in agar plates before the agar has set, producing an opaque layer in the bottom. As the strain grows and acid is produced this will react with the calcium carbonate, causing it to dissolve and form zones of clearing immediately below the colonies.",
        "decision": "not_quantified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz3",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf",
        "source_locator": "Primary preparation, continuation of sugar instruction",
        "exact_source_quote": "autoclaving. Calcium carbonate in the medium serves as a buffer.",
        "snapshot_sha256": "5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193",
        "parsed_text_sha256": "335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff",
        "accessed_at": "2026-10-21T18:31:49.795248Z"
      }
    ],
    "proposed_source_representation": {
      "temperature_C": null,
      "duration_min": null
    },
    "rationale": "The primary specifies autoclaving and separate sugar sterilization but no numerical cycle. Retain the stage without inventing a temperature or duration."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:005190.

10 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 10/10 primary and 10/10 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 10: primary 100.00%; secondary 100.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:005190.

31 timestamp instances inspected; 6 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Attached evidence and raw-response authentication

evidence: concern. Targets: CultureMech:005190.

The generated target and variant owner have no ingredient amount evidence. The two base owners each retain ten claims citing the historical API response. All twenty match derivative report snippets, while the base KOMODO identity claim matches actual catalog bytes. Neither a decoded report nor a successful schema/reference command authenticates the unavailable historical recipe payload. Preserve all existing claims and append a narrow provenance clarification.

[{"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml", "field_path": "$.ingredients[0].evidence[0]", "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 27.7531,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[11].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[160].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json", "sha256": "5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0", "locator": "$.records[246].claims[7].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo650-752-762-preparations/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo650-752-762-preparations/plan.json", "sha256": "68583cbcf2c223c8fa34a4e926d3bd05e5682cc3a77d4ead74cfc91b2f42dbfe", "locator": "$.records[2].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[122].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[123].claims[4].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823", "locator": "$.records[365].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823", "locator": "$.records[448].claims[7].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json", "sha256": "65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934", "locator": "$[48].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json", "sha256": "65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934", "locator": "$[59].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[7].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[368].claims[7].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml", "field_path": "$.ingredients[1].evidence[0]", "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Mannitol\",\n                        \"compound_id\": 6,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 27.4469,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[1].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[12].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[1].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml", "field_path": "$.ingredients[2].evidence[0]", "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[2].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[13].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json", "sha256": "5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0", "locator": "$.records[242].claims[22].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[284].claims[20].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[285].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[286].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[307].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[308].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[418].claims[41].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json", "sha256": "0bb2da58a82dc2b4a90beef1224a7355fd5632db772be0ef053bde40754ded87", "locator": "$[25].claims[2].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[2].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[365].claims[22].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml", "field_path": "$.ingredients[3].evidence[0]", "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.405719,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[14].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[318].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[319].claims[13].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json", "sha256": "5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0", "locator": "$.records[241].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4", "locator": "$.records[183].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4", "locator": "$.records[184].claims[16].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4", "locator": "$.records[230].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4", "locator": "$.records[231].claims[14].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[231].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[269].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[270].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[271].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[272].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[273].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[431].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[436].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[437].claims[12].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json", "sha256": "0bb2da58a82dc2b4a90beef1224a7355fd5632db772be0ef053bde40754ded87", "locator": "$[42].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823", "locator": "$.records[8].claims[21].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[31].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[146].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[166].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[364].claims[19].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml", "field_path": "$.ingredients[4].evidence[0]", "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0206654,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[4].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[15].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[4].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml", "field_path": "$.ingredients[5].evidence[0]", "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.9,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.9,\n                        \"mmol_l\": 5.16719,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[5].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[16].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[5].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml", "field_path": "$.ingredients[6].evidence[0]", "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.734829,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[6].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[6].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml", "field_path": "$.ingredients[7].evidence[0]", "snippet": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0359693,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[7].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[7].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml", "field_path": "$.ingredients[8].evidence[0]", "snippet": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CaCO3\",\n                        \"compound_id\": 13,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 49.955,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[8].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[8].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml", "field_path": "$.ingredients[9].evidence[0]", "snippet": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[9].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[20].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823", "locator": "$.records[23].claims[22].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823", "locator": "$.records[91].claims[20].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[9].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml", "field_path": "$.ingredients[0].evidence[0]", "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 27.7531,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[11].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[160].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json", "sha256": "5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0", "locator": "$.records[246].claims[7].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo650-752-762-preparations/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo650-752-762-preparations/plan.json", "sha256": "68583cbcf2c223c8fa34a4e926d3bd05e5682cc3a77d4ead74cfc91b2f42dbfe", "locator": "$.records[2].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[122].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[123].claims[4].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823", "locator": "$.records[365].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823", "locator": "$.records[448].claims[7].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json", "sha256": "65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934", "locator": "$[48].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json", "sha256": "65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934", "locator": "$[59].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[7].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[368].claims[7].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml", "field_path": "$.ingredients[1].evidence[0]", "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Mannitol\",\n                        \"compound_id\": 6,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 27.4469,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[1].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[12].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[1].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml", "field_path": "$.ingredients[2].evidence[0]", "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[2].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[13].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json", "sha256": "5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0", "locator": "$.records[242].claims[22].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[284].claims[20].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[285].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[286].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[307].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[308].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[418].claims[41].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json", "sha256": "0bb2da58a82dc2b4a90beef1224a7355fd5632db772be0ef053bde40754ded87", "locator": "$[25].claims[2].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[2].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[365].claims[22].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml", "field_path": "$.ingredients[3].evidence[0]", "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.405719,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[14].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[318].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[319].claims[13].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json", "sha256": "5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0", "locator": "$.records[241].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4", "locator": "$.records[183].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4", "locator": "$.records[184].claims[16].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4", "locator": "$.records[230].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json", "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4", "locator": "$.records[231].claims[14].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[231].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[269].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[270].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[271].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[272].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[273].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[431].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[436].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json", "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508", "locator": "$.records[437].claims[12].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json", "sha256": "0bb2da58a82dc2b4a90beef1224a7355fd5632db772be0ef053bde40754ded87", "locator": "$[42].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823", "locator": "$.records[8].claims[21].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[31].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[146].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[166].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[364].claims[19].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml", "field_path": "$.ingredients[4].evidence[0]", "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0206654,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[4].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[15].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[4].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml", "field_path": "$.ingredients[5].evidence[0]", "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.9,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.9,\n                        \"mmol_l\": 5.16719,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[5].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[16].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[5].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml", "field_path": "$.ingredients[6].evidence[0]", "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.734829,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[6].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[6].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml", "field_path": "$.ingredients[7].evidence[0]", "snippet": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0359693,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[7].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[7].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml", "field_path": "$.ingredients[8].evidence[0]", "snippet": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CaCO3\",\n                        \"compound_id\": 13,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 49.955,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[8].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[8].snippet"}], "historical_raw_authenticated": false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml", "field_path": "$.ingredients[9].evidence[0]", "snippet": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }", "matches": [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[154].claims[9].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json", "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500", "locator": "$.records[155].claims[20].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823", "locator": "$.records[23].claims[22].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json", "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823", "locator": "$.records[91].claims[20].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json", "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c", "locator": "$.records[4].claims[9].snippet"}], "historical_raw_authenticated": false}]

### Base accessions and unresolved modified-medium relationship

identity: concern. Targets: CultureMech:005190.

CultureMech:005190, DSMZ owner CultureMech:001510 and modified-medium owner CultureMech:004778 are distinct stable records with existing exact paths. The catalog supports base KOMODO 3 to DSMZ 3 and separately names 3_44106. The latter catalog link to DSMZ 3 does not identify the modification. Matching local ingredients and concentration-independent fingerprints cannot establish SOURCE_DUPLICATE equivalence. No alternative variant formula is invented.

### Water, sugar stage and retained owner preparation

completeness: concern. Targets: CultureMech:005190.

The target omits both water contexts and all preparation. The DSMZ owner already retains pH adjustment, separate sugar sterilization and post-autoclave addition; the KOMODO base owner does not. Recover base source stages from the maintained owner/primary without copying unresolved variant conditions. Calcium-carbonate settling/clearing prose is a source description, not an independent new growth assertion.

### Exact supplied forms

grounding: supported. Targets: CultureMech:005190.

The explicit hydrates correspond to the inspected ontology formulas. The source K2HPO4 agrees with the anhydrous CHEBI:131527 formula; its trihydrate synonym alone does not establish a source hydrate. Generic glucose and mannitol do not establish a narrower stereoisomer. Agar resolves as a mixture.

### Defined basal formulation, agar and catalog oxygen metadata

scope: concern. Targets: CultureMech:005190.

The all-defined classification is unqualified despite agar being a mixture; distinguish a chemically specified basal recipe from the complete agar formulation. SOLID_AGAR is source-supported. The copied Aerobic: No text reflects the catalog Is Aerobic false flag and cannot independently establish anaerobic cultivation or organism-level growth. No taxon or cultivation-temperature claim is added.

### Authoritative repair scope and chronology

ownership: supported. Targets: CultureMech:005190.

Three exact maintained contributors resolve; do not edit only the generated record. The later base-owner amount evidence is absent from the generated layer. Preserve stable IDs, source names, historical imports and variant provenance; append verified clarifications and regenerate only after the unresolved branch and source basis are addressed. No statement here identifies current code as the historical cause.

## Findings

### f1: The DSM 44106 modification is classified as a source duplicate without source verification

major / open / confirmed; issue key: culturemech.005190.unresolved-modified-medium-equivalence.

The target merges a named modified medium and retains SOURCE_DUPLICATE relationship claims. Available catalog metadata identifies the modification but does not establish the same formulation; identical local signatures are insufficient.

### f2: The generated base recipe omits source water and separate sugar preparation

major / open / confirmed; issue key: culturemech.005190.missing-water-preparation-basis.

The primary uses 950 mL main water and separately sterilized sugars in 50 mL water after autoclaving; only the DSMZ owner retains the latter preparation. The omission obscures the basis of the stored rates and a material preparation stage. Historical rate claims are derivative-only, not proven false.

### f3: The defined classification does not distinguish agar from the basal formulation

minor / open / confirmed; issue key: culturemech.005190.unqualified-defined-classification.

The complete record asserts DEFINED composition while containing agar, whose exact ontology definition identifies a mixture. The basal named solutes can still be described separately as chemically specified.

## Recommended Actions And Acceptance Checks

### a1

Retain the modified record identity separately and qualify the duplicate/equivalence assertions until exact variant evidence establishes them. Do not infer or invent the missing modification from the title.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve or restore the two base-water stages and separate sugar handling with claim-level primary evidence, retaining the DSMZ owner instructions already present. Explicitly qualify the rate denominator until its historical basis is authenticated; do not invent a final make-up or numerical sterilization cycle.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Document the scope of the defined label or curate the complete-formulation classification consistently with the agar mixture. Keep the supported solid physical state; do not infer oxygen requirements from catalog flags.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/azotobacter_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch034/331/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-034/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch034/331/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml:1:id: CultureMech:005190<br>./data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml:1:id: CultureMech:005190<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch034/source-preflight-bound/331/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 18 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch034/source-preflight-bound/331/evidence-context-original.json; Complete frozen source context and full local objects | context_only | Frozen target/owner objects match freshly inspected records. Source interpretations are assessed against actual bound capture bytes; historical limitations remain separate. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf; Entire one-page recipe: ten solute rows, water and separate-sugar paragraph | supports | The current primary independently supports batch amounts and preparation, without a measured final-volume declaration or numerical autoclave cycle. |
| catalog-0 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact catalog row 3 | supports | The row establishes this catalog accession and source link; it does not establish experimental oxygen requirements or the specific modification. |
| catalog-1 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact catalog row 3_44106 | supports | The row establishes this catalog accession and source link; it does not establish experimental oxygen requirements or the specific modification. |
| catalog-header | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Catalog header | supports | Is Aerobic is a catalog flag, not a growth experiment. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch034/331/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29864 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29864; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29864 resolves to mannitol. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi3311 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3311; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:3311 resolves to calcium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29864": [{"label": "Mannitol", "match_type": "preferred_term", "identifier": "CHEBI:29864", "preferred_term": "Mannitol", "ontology_id": "CHEBI:29864", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3311": [{"label": "CaCO3", "match_type": "preferred_term", "identifier": "CHEBI:3311", "preferred_term": "CaCO3", "ontology_id": "CHEBI:3311", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/azotobacter_medium.yaml; data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:09.704756"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:09.704756"}]}, {"input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:00.732931"}]}] |
| historical-amount-provenance | /private/tmp/culturemech-review-work-batch034/source-preflight-bound/331/evidence-context-original.json; historical_derivative_comparisons: all twenty owner amount claims and exact decoded report locators | context_only | Twenty claims match decoded local report snippets; their cited 0005e3b4... raw response was not recovered in the documented ignored-inclusive owned-cache/report search. This authenticates local report correspondence only. Original owner evidence/timestamps remain historical assertions. |
| mediadive3api_retry-attempt | https://mediadive.dsmz.de/rest/medium/3; Preserved exact public retrieval result | context_only | Both bounded current MediaDive 3 requests returned HTTP 503. The exact historical raw digest cited by twenty owner amount claims was not recovered by the documented ignored-inclusive owned-file/report search. Primary batch amounts are usable, but exact historical rate/denominator authentication remains required and unavailable. |
| komodo3_44106detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=3_44106; Preserved exact public retrieval result | context_only | The exact KOMODO 3_44106 detail returned HTTP 403. The catalog establishes a named modified medium but does not resolve its recipe modification or equivalence to the base; this required variant-identity check remains unavailable. |
| komodo3detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=3; Preserved exact public retrieval result | context_only | The exact KOMODO 3 detail returned HTTP 403; base identity is independently supported by the catalog and DSMZ primary. |
| writer-0 | src/culturemech/merge/fingerprint.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current fingerprinter explicitly ignores amounts, pH and temperature and uses ingredient sets. It cannot prove the DSM 44106 modification absent. This is a current algorithm limit, not proof of the historical process that produced these records. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Both bounded current MediaDive 3 requests returned HTTP 503. The exact historical raw digest cited by twenty owner amount claims was not recovered by the documented ignored-inclusive owned-file/report search. Primary batch amounts are usable, but exact historical rate/denominator authentication remains required and unavailable.
- The exact KOMODO 3_44106 detail returned HTTP 403. The catalog establishes a named modified medium but does not resolve its recipe modification or equivalence to the base; this required variant-identity check remains unavailable.
- The exact KOMODO 3 detail returned HTTP 403; base identity is independently supported by the catalog and DSMZ primary.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T185141Z-culturemech-005190-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: azotobacter_medium (CultureMech:005190)'
started_at: '2026-10-21T18:47:03Z'
finished_at: '2026-10-21T18:51:41Z'
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
summary: The exact DSMZ 3 primary supports ten batch masses, pH 7.3 and separate 950
  mL main-water / 50 mL sugar-solution stages. The generated record omits those stages;
  the DSMZ owner retains the preparation. Twenty owner amount claims remain derivative-only
  because their historical API bytes were not recovered. The DSM 44106 modification
  is not established by the shared ingredient signature, so variant equivalence and
  exact rate authentication remain partial.
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
  - path: data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml
    sha256: d4bb9cc94d0ce39cdd062808052c7f3b35543685eee415328e16d6e07e91d3e6
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml
    sha256: 39b53834835d8bba9186caf80fc422d1c81da110eed264fb8fa7e561b071c5eb
    role: context
  - path: data/normalized_yaml/bacterial/azotobacter_medium.yaml
    sha256: 17e7b685a2dc83298f42bf069ac5a22e033b4207e9523596cf82af564fb57f97
    role: context
  - path: data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml
    sha256: 8fcf36aecd957222aa9cfe2edb121fbcdd1cc327a31654bc592df47e086fe70e
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
  - path: reports/ingredient_concentration_curation/20261007-dsmz111-preparation/plan.json
    sha256: 9a0531773dfcbc84558c856130401a30edd45a4b51e757eb93924464208dad5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-dsmz125-alternatives/plan.json
    sha256: 7aac345a1ffbce85471dc523a59dada02a6d77da60785978aab62eeb5cd11344
    role: context
  - path: reports/ingredient_concentration_curation/20261007-dsmz265-preparations/plan.json
    sha256: 98489d7ca416178ec64b070c0f99dbd8861ecbac2615eb425d93be875bc0d384
    role: context
  - path: reports/ingredient_concentration_curation/20261007-dsmz467-469-inputs/plan.json
    sha256: d49d8a45389010bd03b96cdfad8e6c2078a19cd872c6be78a2955ee40c656c9c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-dsmz489-stocks/plan.json
    sha256: 82bc1f406001639640d3817850a893fee3ecbe0c652d8ddc96ef2607880c5083
    role: context
  - path: reports/ingredient_concentration_curation/20261007-dsmz546-659-670-stocks/plan.json
    sha256: 3cd5480368b89753710871a2aeed202dd7014e8a00082953d7ab21542584ad2e
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/inspected-candidate-context.json
    sha256: b7c93f3e550e036ef9c2b49f25cc543e6a38e57fc628e6eb7159b00e39d2c7fb
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json
    sha256: 7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml.md
    sha256: d32576e6818ca94f4881210378a40061caa61509205a38ea64ce676bc57b3589
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_3_modified_for_dsm_44106.yaml.md
    sha256: 8527c5bfdc5524f21f96b9212c5d5021d3b745fe42461b270580045f4e05dbce
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json
    sha256: 6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/inspected-candidate-context.json
    sha256: bea184ce1f011e5714cef082c0341aaf001d16024ef7935d004cbc8899f74fd5
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json
    sha256: 5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/inspected-candidate-context.json
    sha256: 20c95f15dfdb08b3e7019d784339ef66641789e40579c7c51f9396092b007fba
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/plan.json
    sha256: 56e72694e73e28cee3666277d0f215973f770da991b4b42930105ec89d0ab6e3
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json
    sha256: 65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
    sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json
    sha256: 0bb2da58a82dc2b4a90beef1224a7355fd5632db772be0ef053bde40754ded87
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json
    sha256: 1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo12-extraction/plan.json
    sha256: ac26f0b1a0435303a9d4eb06960e8c6d1cdd8d35bbd40b025772773f0df44ae2
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo650-752-762-preparations/plan.json
    sha256: 68583cbcf2c223c8fa34a4e926d3bd05e5682cc3a77d4ead74cfc91b2f42dbfe
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo670-source-versions/plan.json
    sha256: 93a8393b5148717d902f75b9e418a5d602d9ef6480daea03e4c01acdffaf4a55
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/azotobacter_medium.yaml.md
    sha256: e9a0490084410967a999d8bfacb9a1ddbab312aacdc789e3bac5d587c86fb6e7
    role: context
  - path: reports/ingredient_concentration_curation/20261007-percent-supplements/plan.json
    sha256: 1e094d04ceb785ec5bef6f5fe5ec2e5d0085a991050a269dce442b127dd7d5bb
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
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
  - path: src/culturemech/convert/komodo_web_raw_yaml.py
    sha256: a1a37015b4e6bac657e49f375b39a319815cc6b02a02135674a858a8b6eab03a
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
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/fetch/komodo_web_fetcher.py
    sha256: 89c510caa08d989b7ec6cee9ac17cc2f0faab606fe8a29ca435df476e52ff004
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
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
    sha256: 64a778108fd3197a8cc08082f80c1de3ec33eda58350cee5df612ab61d23cea1
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 331; batch 034 item 1 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-three task batches
    contain 330 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 333 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:005190
targets:
- target_id: CultureMech:005190
  path: data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml
  label: azotobacter_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/azotobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch034/331/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-034/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch034/331/strict.tsv"
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:005190
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
  - CultureMech:005190
- check_id: mediadive3api_retry-source-access
  name: 'Exact source content access: mediadive3api_retry'
  required: true
  status: unavailable
  summary: Both bounded current MediaDive 3 requests returned HTTP 503. The exact
    historical raw digest cited by twenty owner amount claims was not recovered by
    the documented ignored-inclusive owned-file/report search. Primary batch amounts
    are usable, but exact historical rate/denominator authentication remains required
    and unavailable.
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - mediadive3api_retry-attempt
- check_id: komodo3_44106detail-source-access
  name: 'Exact source content access: komodo3_44106detail'
  required: true
  status: unavailable
  summary: The exact KOMODO 3_44106 detail returned HTTP 403. The catalog establishes
    a named modified medium but does not resolve its recipe modification or equivalence
    to the base; this required variant-identity check remains unavailable.
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - komodo3_44106detail-attempt
- check_id: komodo3detail-source-access
  name: 'Exact source content access: komodo3detail'
  required: false
  status: unavailable
  summary: The exact KOMODO 3 detail returned HTTP 403; base identity is independently
    supported by the catalog and DSMZ primary.
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - komodo3detail-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T18:51:38Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T18:51:38Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/azotobacter_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T18:51:38Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T18:51:38Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T18:47:22.485724Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch034/331/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T18:47:23.517838Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-034/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch034/331/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T18:47:25.174548Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T18:47:26.026849Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T18:51:38Z'
  support: supports
  summary: './data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml:1:id: CultureMech:005190

    ./data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml:1:id: CultureMech:005190

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch034/source-preflight-bound/331/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T18:51:38Z'
  support: supports
  summary: 18 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: faf46c5c89a1bb70a6779424f8fb678a579931976f4bb85308987d2b084fdc12
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch034/source-preflight-bound/331/evidence-context-original.json
  locator: Complete frozen source context and full local objects
  accessed_at: '2026-10-21T18:51:38Z'
  support: context_only
  summary: Frozen target/owner objects match freshly inspected records. Source interpretations
    are assessed against actual bound capture bytes; historical limitations remain
    separate.
  snapshot_sha256: 5d2ff39aeb42435aecc62817ad16d69273463b8190eece471973b1a92317ec5b
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf
  locator: 'Entire one-page recipe: ten solute rows, water and separate-sugar paragraph'
  accessed_at: '2026-10-21T18:31:49.795248Z'
  support: supports
  summary: The current primary independently supports batch amounts and preparation,
    without a measured final-volume declaration or numerical autoclave cycle.
  snapshot_sha256: 5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193
- evidence_id: catalog-0
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact catalog row 3
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The row establishes this catalog accession and source link; it does not
    establish experimental oxygen requirements or the specific modification.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=3'\
    \ >3</a></TD>\n\t\t\t\t\t<TD>AZOTOBACTER MEDIUM</TD>\n\t\t\t\t\t<TD> 7.3</TD>\n\
    \t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\
    <TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: catalog-1
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact catalog row 3_44106
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The row establishes this catalog accession and source link; it does not
    establish experimental oxygen requirements or the specific modification.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=3_44106'\
    \ >3_44106</a></TD>\n\t\t\t\t\t<TD>MEDIUM 3 MODIFIED FOR DSM 44106</TD>\n\t\t\t\
    \t\t<TD>null</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\
    \t<TD>false</TD>\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf</a></TD>\n\t\t\
    \t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: catalog-header
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Catalog header
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Is Aerobic is a catalog flag, not a growth experiment.
  quote: "<TR>\n\t\t\t\t\t<TD valign=\"top\" align=\"left\" width=\"50\">ID</TD>\n\
    \t\t\t\t\t<TD valign=\"top\" align=\"left\">Name</TD>\n\t\t\t\t\t<TD valign=\"\
    top\" align=\"left\">PH Info</TD>\n\t\t\t\t\t<TD valign=\"top\" align=\"left\"\
    >Is Complex</TD>\n\t\t\t\t\t<TD valign=\"top\" align=\"left\">Is Aerobic</TD>\n\
    \t\t\t\t\t<TD valign=\"top\" align=\"left\">Is SubMedium</TD>\n\t\t\t\t\t<TD valign=\"\
    top\" align=\"left\">Instructions</TD>\n\t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch034/331/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T18:51:38Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: e22967a6e1fe6f7999e9f4e5edebb6420a5a38e277075b09d0033eff68daf69c
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
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
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
- evidence_id: chebi29864
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29864
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T17:05:54.508350Z'
  support: supports
  summary: CHEBI:29864 resolves to mannitol. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b4a4ee12a98c8d4b77ed7735296503e802d79c420826547ff2fe174a96896d8c
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
- evidence_id: chebi3311
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3311
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.903210Z'
  support: supports
  summary: CHEBI:3311 resolves to calcium carbonate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 5413cec912ec253d62ba7a3f4ce7f0a9312ba8d1cb756713003f77a6e849d4b2
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
  accessed_at: '2026-10-21T18:51:38Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label":
    "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term":
    "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:29864": [{"label": "Mannitol", "match_type": "preferred_term",
    "identifier": "CHEBI:29864", "preferred_term": "Mannitol", "ontology_id": "CHEBI:29864",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:31795": [{"label":
    "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3311": [{"label":
    "CaCO3", "match_type": "preferred_term", "identifier": "CHEBI:3311", "preferred_term":
    "CaCO3", "ontology_id": "CHEBI:3311", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label":
    "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml;
    data/normalized_yaml/bacterial/azotobacter_medium.yaml; data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T18:51:38Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:09.704756"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:09.704756"}]}, {"input": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
    "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:00.732931"}]}]'
- evidence_id: historical-amount-provenance
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch034/source-preflight-bound/331/evidence-context-original.json
  locator: 'historical_derivative_comparisons: all twenty owner amount claims and
    exact decoded report locators'
  accessed_at: '2026-10-21T18:51:38Z'
  support: context_only
  summary: Twenty claims match decoded local report snippets; their cited 0005e3b4...
    raw response was not recovered in the documented ignored-inclusive owned-cache/report
    search. This authenticates local report correspondence only. Original owner evidence/timestamps
    remain historical assertions.
  snapshot_sha256: 5d2ff39aeb42435aecc62817ad16d69273463b8190eece471973b1a92317ec5b
- evidence_id: mediadive3api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/3
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T18:32:33.145750Z'
  support: context_only
  summary: Both bounded current MediaDive 3 requests returned HTTP 503. The exact
    historical raw digest cited by twenty owner amount claims was not recovered by
    the documented ignored-inclusive owned-file/report search. Primary batch amounts
    are usable, but exact historical rate/denominator authentication remains required
    and unavailable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo3_44106detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=3_44106
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T18:31:47.523952Z'
  support: context_only
  summary: The exact KOMODO 3_44106 detail returned HTTP 403. The catalog establishes
    a named modified medium but does not resolve its recipe modification or equivalence
    to the base; this required variant-identity check remains unavailable.
  snapshot_sha256: 64ced656dd1a22a1dfb6eb1b74337ebb11aa2e6f760580a36730ba648af512a3
- evidence_id: komodo3detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=3
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T18:31:47.524122Z'
  support: context_only
  summary: The exact KOMODO 3 detail returned HTTP 403; base identity is independently
    supported by the catalog and DSMZ primary.
  snapshot_sha256: 730b4d8459a9060a2298df3a536fb6d46fcc07d87fd8551daabb1c8ff58048c1
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/fingerprint.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:51:38Z'
  support: context_only
  summary: The current fingerprinter explicitly ignores amounts, pH and temperature
    and uses ingredient sets. It cannot prove the DSM 44106 modification absent. This
    is a current algorithm limit, not proof of the historical process that produced
    these records.
  snapshot_sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 15 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Glucose batch amount versus stored rate\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/azotobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"One-page primary, solute row 1\",\n        \"\
    exact_source_quote\": \"Glucose 5.00 g\",\n        \"snapshot_sha256\": \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\"\
    ,\n        \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_batch_amount\": 5.0,\n\
    \      \"unit\": \"g\",\n      \"main_g_per_L\": null,\n      \"variant_44106_transfer\"\
    : \"unresolved\"\n    },\n    \"rationale\": \"The base-recipe mass matches the\
    \ local number after mg-to-g conversion where needed; this is not evidence that\
    \ the stored rate is false. The primary gives 950 mL main water plus a separate\
    \ 50 mL sugar solution, not an independent final make-up declaration. Two base\
    \ owners have matching derivative claims of a provider 1000 mL denominator, but\
    \ the cited raw response is unavailable. The generated target and variant owner\
    \ have no attached amount evidence; the variant-specific formulation is unresolved.\
    \ Preserve the numerical values pending explicit basis/variant authentication\
    \ rather than inventing replacement rates.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q2\",\n    \"component_or_context\": \"Mannitol batch amount versus stored\
    \ rate\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/azotobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"One-page primary, solute row 2\",\n        \"\
    exact_source_quote\": \"Mannitol 5.00 g\",\n        \"snapshot_sha256\": \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\"\
    ,\n        \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_batch_amount\": 5.0,\n\
    \      \"unit\": \"g\",\n      \"main_g_per_L\": null,\n      \"variant_44106_transfer\"\
    : \"unresolved\"\n    },\n    \"rationale\": \"The base-recipe mass matches the\
    \ local number after mg-to-g conversion where needed; this is not evidence that\
    \ the stored rate is false. The primary gives 950 mL main water plus a separate\
    \ 50 mL sugar solution, not an independent final make-up declaration. Two base\
    \ owners have matching derivative claims of a provider 1000 mL denominator, but\
    \ the cited raw response is unavailable. The generated target and variant owner\
    \ have no attached amount evidence; the variant-specific formulation is unresolved.\
    \ Preserve the numerical values pending explicit basis/variant authentication\
    \ rather than inventing replacement rates.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q3\",\n    \"component_or_context\": \"CaCl2 x 2 H2O batch amount versus stored\
    \ rate\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/azotobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"One-page primary, solute row 3\",\n        \"\
    exact_source_quote\": \"CaCl2 x 2 H2O 0.10 g\",\n        \"snapshot_sha256\":\
    \ \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\",\n    \
    \    \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_batch_amount\": 0.1,\n\
    \      \"unit\": \"g\",\n      \"main_g_per_L\": null,\n      \"variant_44106_transfer\"\
    : \"unresolved\"\n    },\n    \"rationale\": \"The base-recipe mass matches the\
    \ local number after mg-to-g conversion where needed; this is not evidence that\
    \ the stored rate is false. The primary gives 950 mL main water plus a separate\
    \ 50 mL sugar solution, not an independent final make-up declaration. Two base\
    \ owners have matching derivative claims of a provider 1000 mL denominator, but\
    \ the cited raw response is unavailable. The generated target and variant owner\
    \ have no attached amount evidence; the variant-specific formulation is unresolved.\
    \ Preserve the numerical values pending explicit basis/variant authentication\
    \ rather than inventing replacement rates.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q4\",\n    \"component_or_context\": \"MgSO4 x 7 H2O batch amount versus stored\
    \ rate\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/azotobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"One-page primary, solute row 4\",\n        \"\
    exact_source_quote\": \"MgSO4 x 7 H2O 0.10 g\",\n        \"snapshot_sha256\":\
    \ \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\",\n    \
    \    \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_batch_amount\": 0.1,\n\
    \      \"unit\": \"g\",\n      \"main_g_per_L\": null,\n      \"variant_44106_transfer\"\
    : \"unresolved\"\n    },\n    \"rationale\": \"The base-recipe mass matches the\
    \ local number after mg-to-g conversion where needed; this is not evidence that\
    \ the stored rate is false. The primary gives 950 mL main water plus a separate\
    \ 50 mL sugar solution, not an independent final make-up declaration. Two base\
    \ owners have matching derivative claims of a provider 1000 mL denominator, but\
    \ the cited raw response is unavailable. The generated target and variant owner\
    \ have no attached amount evidence; the variant-specific formulation is unresolved.\
    \ Preserve the numerical values pending explicit basis/variant authentication\
    \ rather than inventing replacement rates.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q5\",\n    \"component_or_context\": \"Na2MoO4 x 2 H2O batch amount versus\
    \ stored rate\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/azotobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"One-page primary, solute row 5\",\n        \"\
    exact_source_quote\": \"Na2MoO4 x 2 H2O 5.00 mg\",\n        \"snapshot_sha256\"\
    : \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\",\n    \
    \    \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_batch_amount\": 5.0,\n\
    \      \"unit\": \"mg\",\n      \"main_g_per_L\": null,\n      \"variant_44106_transfer\"\
    : \"unresolved\"\n    },\n    \"rationale\": \"The base-recipe mass matches the\
    \ local number after mg-to-g conversion where needed; this is not evidence that\
    \ the stored rate is false. The primary gives 950 mL main water plus a separate\
    \ 50 mL sugar solution, not an independent final make-up declaration. Two base\
    \ owners have matching derivative claims of a provider 1000 mL denominator, but\
    \ the cited raw response is unavailable. The generated target and variant owner\
    \ have no attached amount evidence; the variant-specific formulation is unresolved.\
    \ Preserve the numerical values pending explicit basis/variant authentication\
    \ rather than inventing replacement rates.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q6\",\n    \"component_or_context\": \"K2HPO4 batch amount versus stored rate\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.9\",\n          \"unit\": \"G_PER_L\"\n        },\n     \
    \   \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.9\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/azotobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.9\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.9\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"One-page primary, solute row 6\",\n        \"\
    exact_source_quote\": \"K2HPO4 0.90 g\",\n        \"snapshot_sha256\": \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\"\
    ,\n        \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_batch_amount\": 0.9,\n\
    \      \"unit\": \"g\",\n      \"main_g_per_L\": null,\n      \"variant_44106_transfer\"\
    : \"unresolved\"\n    },\n    \"rationale\": \"The base-recipe mass matches the\
    \ local number after mg-to-g conversion where needed; this is not evidence that\
    \ the stored rate is false. The primary gives 950 mL main water plus a separate\
    \ 50 mL sugar solution, not an independent final make-up declaration. Two base\
    \ owners have matching derivative claims of a provider 1000 mL denominator, but\
    \ the cited raw response is unavailable. The generated target and variant owner\
    \ have no attached amount evidence; the variant-specific formulation is unresolved.\
    \ Preserve the numerical values pending explicit basis/variant authentication\
    \ rather than inventing replacement rates.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q7\",\n    \"component_or_context\": \"KH2PO4 batch amount versus stored rate\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n     \
    \   \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/azotobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"One-page primary, solute row 7\",\n        \"\
    exact_source_quote\": \"KH2PO4 0.10 g\",\n        \"snapshot_sha256\": \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\"\
    ,\n        \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_batch_amount\": 0.1,\n\
    \      \"unit\": \"g\",\n      \"main_g_per_L\": null,\n      \"variant_44106_transfer\"\
    : \"unresolved\"\n    },\n    \"rationale\": \"The base-recipe mass matches the\
    \ local number after mg-to-g conversion where needed; this is not evidence that\
    \ the stored rate is false. The primary gives 950 mL main water plus a separate\
    \ 50 mL sugar solution, not an independent final make-up declaration. Two base\
    \ owners have matching derivative claims of a provider 1000 mL denominator, but\
    \ the cited raw response is unavailable. The generated target and variant owner\
    \ have no attached amount evidence; the variant-specific formulation is unresolved.\
    \ Preserve the numerical values pending explicit basis/variant authentication\
    \ rather than inventing replacement rates.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q8\",\n    \"component_or_context\": \"FeSO4 x 7 H2O batch amount versus stored\
    \ rate\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/azotobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"One-page primary, solute row 8\",\n        \"\
    exact_source_quote\": \"FeSO4 x 7 H2O 0.01 g\",\n        \"snapshot_sha256\":\
    \ \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\",\n    \
    \    \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_batch_amount\": 0.01,\n\
    \      \"unit\": \"g\",\n      \"main_g_per_L\": null,\n      \"variant_44106_transfer\"\
    : \"unresolved\"\n    },\n    \"rationale\": \"The base-recipe mass matches the\
    \ local number after mg-to-g conversion where needed; this is not evidence that\
    \ the stored rate is false. The primary gives 950 mL main water plus a separate\
    \ 50 mL sugar solution, not an independent final make-up declaration. Two base\
    \ owners have matching derivative claims of a provider 1000 mL denominator, but\
    \ the cited raw response is unavailable. The generated target and variant owner\
    \ have no attached amount evidence; the variant-specific formulation is unresolved.\
    \ Preserve the numerical values pending explicit basis/variant authentication\
    \ rather than inventing replacement rates.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q9\",\n    \"component_or_context\": \"CaCO3 batch amount versus stored rate\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/azotobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[8].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"One-page primary, solute row 9\",\n        \"\
    exact_source_quote\": \"CaCO3 5.00 g\",\n        \"snapshot_sha256\": \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\"\
    ,\n        \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_batch_amount\": 5.0,\n\
    \      \"unit\": \"g\",\n      \"main_g_per_L\": null,\n      \"variant_44106_transfer\"\
    : \"unresolved\"\n    },\n    \"rationale\": \"The base-recipe mass matches the\
    \ local number after mg-to-g conversion where needed; this is not evidence that\
    \ the stored rate is false. The primary gives 950 mL main water plus a separate\
    \ 50 mL sugar solution, not an independent final make-up declaration. Two base\
    \ owners have matching derivative claims of a provider 1000 mL denominator, but\
    \ the cited raw response is unavailable. The generated target and variant owner\
    \ have no attached amount evidence; the variant-specific formulation is unresolved.\
    \ Preserve the numerical values pending explicit basis/variant authentication\
    \ rather than inventing replacement rates.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q10\",\n    \"component_or_context\": \"Agar batch amount versus stored rate\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[9].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n      \
    \  \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/azotobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[9].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\":\
    \ \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"One-page primary, solute row 10\",\n        \"\
    exact_source_quote\": \"Agar 15.00 g\",\n        \"snapshot_sha256\": \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\"\
    ,\n        \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_batch_amount\": 15.0,\n\
    \      \"unit\": \"g\",\n      \"main_g_per_L\": null,\n      \"variant_44106_transfer\"\
    : \"unresolved\"\n    },\n    \"rationale\": \"The base-recipe mass matches the\
    \ local number after mg-to-g conversion where needed; this is not evidence that\
    \ the stored rate is false. The primary gives 950 mL main water plus a separate\
    \ 50 mL sugar solution, not an independent final make-up declaration. Two base\
    \ owners have matching derivative claims of a provider 1000 mL denominator, but\
    \ the cited raw response is unavailable. The generated target and variant owner\
    \ have no attached amount evidence; the variant-specific formulation is unresolved.\
    \ Preserve the numerical values pending explicit basis/variant authentication\
    \ rather than inventing replacement rates.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q11\",\n    \"component_or_context\": \"Base main-water input\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/azotobacter_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"Primary main table, water row\",\n        \"\
    exact_source_quote\": \"Distilled water 950.00 ml\",\n        \"snapshot_sha256\"\
    : \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\",\n    \
    \    \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"main_water_mL\": 950\n   \
    \ },\n    \"rationale\": \"Add the omitted base-water context separately from\
    \ the sugar solution. No automatic transfer to the unresolved DSM 44106 variant\
    \ is proposed.\"\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"Separate sugar-solution water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/azotobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Sterilize glucose and mannitol separately (in 50 ml H2O) and add to the medium\
    \ after autoclaving. Calcium carbonate in the medium serves as a buffer. The calcium\
    \ carbonate will settle in agar plates before the agar has set, producing an opaque\
    \ layer in the bottom. As the strain grows and acid is produced this will react\
    \ with the calcium carbonate, causing it to dissolve and form zones of clearing\
    \ immediately below the colonies.\",\n        \"decision\": \"evidence_only\"\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"Primary preparation, first line of separate-sugar\
    \ instruction\",\n        \"exact_source_quote\": \"Sterilize glucose and mannitol\
    \ separately (in 50 ml H 2O) and add to the medium after\",\n        \"snapshot_sha256\"\
    : \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\",\n    \
    \    \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"sugar_solution_water_mL\"\
    : 50,\n      \"addition_stage\": \"after base autoclaving\"\n    },\n    \"rationale\"\
    : \"The DSMZ owner already preserves this instruction and needs claim-level evidence.\
    \ The target and KOMODO base owner omit it. The 50 mL applies to the two sugars\
    \ together, not to each independently.\"\n  },\n  {\n    \"quantity_id\": \"q13\"\
    ,\n    \"component_or_context\": \"Base pH and unresolved variant pH\",\n    \"\
    decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ph_value\",\n        \"stored\": 7.3,\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.3,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/azotobacter_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.3,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.3,\n        \"\
    decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"Primary preparation\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 7.3.\",\n        \"snapshot_sha256\": \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\"\
    ,\n        \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"base_pH\": 7.3,\n      \"\
    variant_specific_pH\": null\n    },\n    \"rationale\": \"The base pH is directly\
    \ supported. The catalog variant row has null pH, and the source modification\
    \ is unresolved; do not treat the local inherited variant pH as independently\
    \ verified.\"\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Final denominator versus listed water inputs\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/azotobacter_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"not_quantified\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"Main water\",\n        \"exact_source_quote\"\
    : \"Distilled water 950.00 ml\",\n        \"snapshot_sha256\": \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\"\
    ,\n        \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz3\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"Separate sugar-water stage\",\n        \"exact_source_quote\"\
    : \"Sterilize glucose and mannitol separately (in 50 ml H 2O) and add to the medium\
    \ after\",\n        \"snapshot_sha256\": \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\"\
    ,\n        \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"listed_water_sum_mL\": 1000,\n\
    \      \"measured_final_volume_mL\": null\n    },\n    \"rationale\": \"950 +\
    \ 50 = 1000 mL is a sum of listed inputs, not a measured final volume. The historical\
    \ provider denominator remains a derivative claim and is not authenticated by\
    \ this arithmetic.\"\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"Numerical sterilization cycle\",\n    \"decision\": \"not_quantified\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n      \
    \  \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/azotobacter_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[1].description\",\n        \"stored\": \"Sterilize glucose\
    \ and mannitol separately (in 50 ml H2O) and add to the medium after autoclaving.\
    \ Calcium carbonate in the medium serves as a buffer. The calcium carbonate will\
    \ settle in agar plates before the agar has set, producing an opaque layer in\
    \ the bottom. As the strain grows and acid is produced this will react with the\
    \ calcium carbonate, causing it to dissolve and form zones of clearing immediately\
    \ below the colonies.\",\n        \"decision\": \"not_quantified\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz3\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf\"\
    ,\n        \"source_locator\": \"Primary preparation, continuation of sugar instruction\"\
    ,\n        \"exact_source_quote\": \"autoclaving. Calcium carbonate in the medium\
    \ serves as a buffer.\",\n        \"snapshot_sha256\": \"5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193\"\
    ,\n        \"parsed_text_sha256\": \"335ee35ee330dd282c4663569401ed6cf6a620e2fcb4574f8a2be65d4f81eaff\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:31:49.795248Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"temperature_C\": null,\n \
    \     \"duration_min\": null\n    },\n    \"rationale\": \"The primary specifies\
    \ autoclaving and separate sugar sterilization but no numerical cycle. Retain\
    \ the stage without inventing a temperature or duration.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '10 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 10/10
    primary and 10/10 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - owner-2
  - chebi131527
  - chebi17234
  - chebi2509
  - chebi29864
  - chebi31795
  - chebi3311
  - chebi63036
  - chebi75213
  - chebi75836
  - chebi86158
  details: 'Instance coverage on a 0–100 percent scale, denominator 10: primary 100.00%;
    secondary 100.00%. These are linkage metrics, not correctness scores. Missing
    optional links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 31 timestamp instances inspected; 6 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
- assessment_id: historical-evidence
  area: evidence
  topic: Attached evidence and raw-response authentication
  outcome: concern
  summary: The generated target and variant owner have no ingredient amount evidence.
    The two base owners each retain ten claims citing the historical API response.
    All twenty match derivative report snippets, while the base KOMODO identity claim
    matches actual catalog bytes. Neither a decoded report nor a successful schema/reference
    command authenticates the unavailable historical recipe payload. Preserve all
    existing claims and append a narrow provenance clarification.
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - record
  - primary
  - catalog-0
  - historical-amount-provenance
  - bound-context
  details: '[{"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
    "field_path": "$.ingredients[0].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\":
    5,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    27.7531,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[11].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[160].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json",
    "sha256": "5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0",
    "locator": "$.records[246].claims[7].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo650-752-762-preparations/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo650-752-762-preparations/plan.json",
    "sha256": "68583cbcf2c223c8fa34a4e926d3bd05e5682cc3a77d4ead74cfc91b2f42dbfe",
    "locator": "$.records[2].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[122].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[123].claims[4].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823",
    "locator": "$.records[365].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823",
    "locator": "$.records[448].claims[7].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json",
    "sha256": "65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934",
    "locator": "$[48].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json",
    "sha256": "65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934",
    "locator": "$[59].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[7].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[368].claims[7].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
    "field_path": "$.ingredients[1].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Mannitol\",\n                        \"compound_id\":
    6,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    27.4469,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[1].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[12].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[1].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
    "field_path": "$.ingredients[2].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[2].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[13].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json",
    "sha256": "5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0",
    "locator": "$.records[242].claims[22].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[284].claims[20].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[285].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[286].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[307].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[308].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[418].claims[41].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json",
    "sha256": "0bb2da58a82dc2b4a90beef1224a7355fd5632db772be0ef053bde40754ded87",
    "locator": "$[25].claims[2].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[2].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[365].claims[22].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
    "field_path": "$.ingredients[3].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.405719,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[14].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[318].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[319].claims[13].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json",
    "sha256": "5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0",
    "locator": "$.records[241].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4",
    "locator": "$.records[183].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4",
    "locator": "$.records[184].claims[16].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4",
    "locator": "$.records[230].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4",
    "locator": "$.records[231].claims[14].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[231].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[269].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[270].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[271].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[272].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[273].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[431].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[436].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[437].claims[12].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json",
    "sha256": "0bb2da58a82dc2b4a90beef1224a7355fd5632db772be0ef053bde40754ded87",
    "locator": "$[42].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823",
    "locator": "$.records[8].claims[21].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[31].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[146].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[166].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[364].claims[19].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
    "field_path": "$.ingredients[4].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0206654,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[4].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[15].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[4].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
    "field_path": "$.ingredients[5].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.9,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.9,\n                        \"mmol_l\":
    5.16719,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[5].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[16].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[5].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
    "field_path": "$.ingredients[6].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.734829,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[6].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[6].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
    "field_path": "$.ingredients[7].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0359693,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[7].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[7].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
    "field_path": "$.ingredients[8].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CaCO3\",\n                        \"compound_id\":
    13,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    49.955,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[8].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[8].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml",
    "field_path": "$.ingredients[9].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\":
    44.5991,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[9].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[20].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823",
    "locator": "$.records[23].claims[22].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823",
    "locator": "$.records[91].claims[20].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[9].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
    "field_path": "$.ingredients[0].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\":
    5,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    27.7531,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[11].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[160].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json",
    "sha256": "5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0",
    "locator": "$.records[246].claims[7].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo650-752-762-preparations/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo650-752-762-preparations/plan.json",
    "sha256": "68583cbcf2c223c8fa34a4e926d3bd05e5682cc3a77d4ead74cfc91b2f42dbfe",
    "locator": "$.records[2].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[122].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[123].claims[4].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823",
    "locator": "$.records[365].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823",
    "locator": "$.records[448].claims[7].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json",
    "sha256": "65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934",
    "locator": "$[48].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json",
    "sha256": "65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934",
    "locator": "$[59].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[7].claims[0].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[368].claims[7].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
    "field_path": "$.ingredients[1].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Mannitol\",\n                        \"compound_id\":
    6,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    27.4469,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[1].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[12].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[1].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
    "field_path": "$.ingredients[2].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[2].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[13].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json",
    "sha256": "5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0",
    "locator": "$.records[242].claims[22].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[284].claims[20].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[285].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[286].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[307].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[308].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[418].claims[41].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json",
    "sha256": "0bb2da58a82dc2b4a90beef1224a7355fd5632db772be0ef053bde40754ded87",
    "locator": "$[25].claims[2].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[2].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[365].claims[22].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
    "field_path": "$.ingredients[3].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.405719,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[14].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[318].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[319].claims[13].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json",
    "sha256": "5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0",
    "locator": "$.records[241].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4",
    "locator": "$.records[183].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4",
    "locator": "$.records[184].claims[16].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4",
    "locator": "$.records[230].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json",
    "sha256": "6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4",
    "locator": "$.records[231].claims[14].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[231].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[269].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[270].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[271].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[272].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[273].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[431].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[436].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json",
    "sha256": "1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508",
    "locator": "$.records[437].claims[12].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json",
    "sha256": "0bb2da58a82dc2b4a90beef1224a7355fd5632db772be0ef053bde40754ded87",
    "locator": "$[42].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823",
    "locator": "$.records[8].claims[21].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[31].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[146].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[166].claims[3].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[364].claims[19].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
    "field_path": "$.ingredients[4].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0206654,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[4].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[15].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[4].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
    "field_path": "$.ingredients[5].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.9,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.9,\n                        \"mmol_l\":
    5.16719,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[5].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[16].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[5].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
    "field_path": "$.ingredients[6].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.734829,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[6].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[17].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[6].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
    "field_path": "$.ingredients[7].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0359693,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[7].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[18].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[7].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
    "field_path": "$.ingredients[8].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CaCO3\",\n                        \"compound_id\":
    13,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    49.955,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[8].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[19].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[8].snippet"}], "historical_raw_authenticated":
    false}, {"record_path": "data/normalized_yaml/bacterial/azotobacter_medium.yaml",
    "field_path": "$.ingredients[9].evidence[0]", "snippet": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\":
    44.5991,\n                        \"optional\": 0\n                    }", "matches":
    [{"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[154].claims[9].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json",
    "sha256": "7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500",
    "locator": "$.records[155].claims[20].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823",
    "locator": "$.records[23].claims[22].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json",
    "sha256": "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823",
    "locator": "$.records[91].claims[20].snippet"}, {"repository_path": "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "captured_path": "/private/tmp/culturemech-review-source-preflight-batch034/inputs/reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json",
    "sha256": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
    "locator": "$.records[4].claims[9].snippet"}], "historical_raw_authenticated":
    false}]'
- assessment_id: identity
  area: identity
  topic: Base accessions and unresolved modified-medium relationship
  outcome: concern
  summary: CultureMech:005190, DSMZ owner CultureMech:001510 and modified-medium owner
    CultureMech:004778 are distinct stable records with existing exact paths. The
    catalog supports base KOMODO 3 to DSMZ 3 and separately names 3_44106. The latter
    catalog link to DSMZ 3 does not identify the modification. Matching local ingredients
    and concentration-independent fingerprints cannot establish SOURCE_DUPLICATE equivalence.
    No alternative variant formula is invented.
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - id-search
  - catalog-0
  - catalog-1
  - primary
- assessment_id: preparation
  area: completeness
  topic: Water, sugar stage and retained owner preparation
  outcome: concern
  summary: The target omits both water contexts and all preparation. The DSMZ owner
    already retains pH adjustment, separate sugar sterilization and post-autoclave
    addition; the KOMODO base owner does not. Recover base source stages from the
    maintained owner/primary without copying unresolved variant conditions. Calcium-carbonate
    settling/clearing prose is a source description, not an independent new growth
    assertion.
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - record
  - primary
  - quantity-inventory
  - owner-0
  - owner-1
  - owner-2
- assessment_id: forms
  area: grounding
  topic: Exact supplied forms
  outcome: supported
  summary: The explicit hydrates correspond to the inspected ontology formulas. The
    source K2HPO4 agrees with the anhydrous CHEBI:131527 formula; its trihydrate synonym
    alone does not establish a source hydrate. Generic glucose and mannitol do not
    establish a narrower stereoisomer. Agar resolves as a mixture.
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - primary
  - chebi131527
  - chebi2509
  - chebi17234
  - chebi29864
  - chebi86158
  - chebi31795
  - chebi75213
  - chebi75836
- assessment_id: classification
  area: scope
  topic: Defined basal formulation, agar and catalog oxygen metadata
  outcome: concern
  summary: 'The all-defined classification is unqualified despite agar being a mixture;
    distinguish a chemically specified basal recipe from the complete agar formulation.
    SOLID_AGAR is source-supported. The copied Aerobic: No text reflects the catalog
    Is Aerobic false flag and cannot independently establish anaerobic cultivation
    or organism-level growth. No taxon or cultivation-temperature claim is added.'
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - record
  - primary
  - chebi2509
  - catalog-header
  - catalog-0
- assessment_id: ownership
  area: ownership
  topic: Authoritative repair scope and chronology
  outcome: supported
  summary: Three exact maintained contributors resolve; do not edit only the generated
    record. The later base-owner amount evidence is absent from the generated layer.
    Preserve stable IDs, source names, historical imports and variant provenance;
    append verified clarifications and regenerate only after the unresolved branch
    and source basis are addressed. No statement here identifies current code as the
    historical cause.
  target_ids:
  - CultureMech:005190
  evidence_ids:
  - record
  - id-search
  - writer-0
  - historical-amount-provenance
  - owner-0
  - owner-1
  - owner-2
findings:
- finding_id: f1
  issue_key: culturemech.005190.unresolved-modified-medium-equivalence
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The DSM 44106 modification is classified as a source duplicate without source
    verification
  description: The target merges a named modified medium and retains SOURCE_DUPLICATE
    relationship claims. Available catalog metadata identifies the modification but
    does not establish the same formulation; identical local signatures are insufficient.
  target_ids:
  - CultureMech:005190
  field_paths:
  - variant_children
  - parent_media
  - variant_relationship
  - variant_modifications
  - synonyms
  evidence_ids:
  - record
  - catalog-1
  - writer-0
  - komodo3_44106detail-attempt
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/azotobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml
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
  issue_key: culturemech.005190.missing-water-preparation-basis
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The generated base recipe omits source water and separate sugar preparation
  description: The primary uses 950 mL main water and separately sterilized sugars
    in 50 mL water after autoclaving; only the DSMZ owner retains the latter preparation.
    The omission obscures the basis of the stored rates and a material preparation
    stage. Historical rate claims are derivative-only, not proven false.
  target_ids:
  - CultureMech:005190
  field_paths:
  - ingredients
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - primary
  - quantity-inventory
  - historical-amount-provenance
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/azotobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml
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
  issue_key: culturemech.005190.unqualified-defined-classification
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: The defined classification does not distinguish agar from the basal formulation
  description: The complete record asserts DEFINED composition while containing agar,
    whose exact ontology definition identifies a mixture. The basal named solutes
    can still be described separately as chemically specified.
  target_ids:
  - CultureMech:005190
  field_paths:
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - primary
  - chebi2509
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/azotobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml
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
  description: Retain the modified record identity separately and qualify the duplicate/equivalence
    assertions until exact variant evidence establishes them. Do not infer or invent
    the missing modification from the title.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:005190
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/azotobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml
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
  description: Preserve or restore the two base-water stages and separate sugar handling
    with claim-level primary evidence, retaining the DSMZ owner instructions already
    present. Explicitly qualify the rate denominator until its historical basis is
    authenticated; do not invent a final make-up or numerical sterilization cycle.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:005190
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/azotobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml
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
  description: Document the scope of the defined label or curate the complete-formulation
    classification consistently with the agar mixture. Keep the supported solid physical
    state; do not infer oxygen requirements from catalog flags.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:005190
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/azotobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml
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
- Both bounded current MediaDive 3 requests returned HTTP 503. The exact historical
  raw digest cited by twenty owner amount claims was not recovered by the documented
  ignored-inclusive owned-file/report search. Primary batch amounts are usable, but
  exact historical rate/denominator authentication remains required and unavailable.
- The exact KOMODO 3_44106 detail returned HTTP 403. The catalog establishes a named
  modified medium but does not resolve its recipe modification or equivalence to the
  base; this required variant-identity check remains unavailable.
- The exact KOMODO 3 detail returned HTTP 403; base identity is independently supported
  by the catalog and DSMZ primary.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-034
- generated-medium
```
