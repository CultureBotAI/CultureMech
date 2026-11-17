# Source and formulation review: artificial_seawater_for_halophiles (CultureMech:000298)

- Review: 20261021T175835Z-culturemech-000298-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T17:54:21Z
- Finished UTC: 2026-10-21T17:58:35Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 457 supports all eleven nominal ingredient masses and explicitly separates an initial one-litre preparation from filtered bicarbonate and pyruvate additions. Local prose preserves much of this staging, but the structured main G_PER_L fields do not distinguish the later stock amounts or establish a completed final volume. Required historical correspondence of nitrate legacy MediaIngredientMech:000171 remains unresolved despite a completed current negative lookup. The exact archaea owner is retained; the bacterial namesake is not a contributor.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 312; batch 032 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-one task batches contain 310 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 313 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000298 | data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml | generated | artificial_seawater_for_halophiles |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000298 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000298 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-032/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch032/312/strict.tsv |
| validate-terms | passed | True | CultureMech:000298 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000298 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000298 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Required source-scope verification | unavailable | True | CultureMech:000298 | Required historical correspondence of the asserted MediaIngredientMech:000171 identifier remains unverified. Current catalog/tree absence is already a completed negative lookup, and primary formulation evidence remains available. |
| Exact source content access: mediadiveJ457api | unavailable | False | CultureMech:000298 | Exact current MediaDive J457 attempt returned HTTP 503. Primary JCM 457 formulation is available; this optional provider failure does not itself make the scientific comparison unavailable. |
| Exact source content access: mediadiveJ457api_retry | unavailable | False | CultureMech:000298 | Exact current MediaDive J457 attempt returned HTTP 503. Primary JCM 457 formulation is available; this optional provider failure does not itself make the scientific comparison unavailable. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000298.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:000298.

21 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "NaCl initial batch amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "195",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "195",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, NaCl",
        "exact_source_quote": "NaCl 195.0 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, initial mixture before subsequent additions",
        "exact_source_quote": "bring volume to 1.0 L.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "195.0",
      "initial_makeup_L": 1,
      "completed_medium_volume_L": null
    },
    "rationale": "The mass matches the local numeric value and the initial one-litre make-up supports an initial-stage basis. No local amount evidence is attached. Add exact stage-specific evidence, without treating this as a measured final concentration after Tris and later stocks."
  },
  {
    "quantity_id": "q2",
    "component_or_context": "MgCl2 x 6 H2O initial batch amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "35",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "35",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, MgCl 2 ·6H 2 O",
        "exact_source_quote": "MgCl 2 ·6H 2 O 35.0 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, initial mixture before subsequent additions",
        "exact_source_quote": "bring volume to 1.0 L.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "35.0",
      "initial_makeup_L": 1,
      "completed_medium_volume_L": null
    },
    "rationale": "The mass matches the local numeric value and the initial one-litre make-up supports an initial-stage basis. No local amount evidence is attached. Add exact stage-specific evidence, without treating this as a measured final concentration after Tris and later stocks."
  },
  {
    "quantity_id": "q3",
    "component_or_context": "MgSO4 x 7 H2O initial batch amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, MgSO 4 ·7H 2 O",
        "exact_source_quote": "MgSO 4 ·7H 2 O 50.0 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, initial mixture before subsequent additions",
        "exact_source_quote": "bring volume to 1.0 L.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "50.0",
      "initial_makeup_L": 1,
      "completed_medium_volume_L": null
    },
    "rationale": "The mass matches the local numeric value and the initial one-litre make-up supports an initial-stage basis. No local amount evidence is attached. Add exact stage-specific evidence, without treating this as a measured final concentration after Tris and later stocks."
  },
  {
    "quantity_id": "q4",
    "component_or_context": "KCl initial batch amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, KCl",
        "exact_source_quote": "KCl 5.0 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, initial mixture before subsequent additions",
        "exact_source_quote": "bring volume to 1.0 L.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "5.0",
      "initial_makeup_L": 1,
      "completed_medium_volume_L": null
    },
    "rationale": "The mass matches the local numeric value and the initial one-litre make-up supports an initial-stage basis. No local amount evidence is attached. Add exact stage-specific evidence, without treating this as a measured final concentration after Tris and later stocks."
  },
  {
    "quantity_id": "q5",
    "component_or_context": "NaNO3 initial batch amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, NaNO 3",
        "exact_source_quote": "NaNO 3 1.0 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, initial mixture before subsequent additions",
        "exact_source_quote": "bring volume to 1.0 L.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "1.0",
      "initial_makeup_L": 1,
      "completed_medium_volume_L": null
    },
    "rationale": "The mass matches the local numeric value and the initial one-litre make-up supports an initial-stage basis. No local amount evidence is attached. Add exact stage-specific evidence, without treating this as a measured final concentration after Tris and later stocks."
  },
  {
    "quantity_id": "q6",
    "component_or_context": "CaCl2 x 2 H2O initial batch amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, CaCl 2 ·2H 2 O",
        "exact_source_quote": "CaCl 2 ·2H 2 O 0.5 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, initial mixture before subsequent additions",
        "exact_source_quote": "bring volume to 1.0 L.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "0.5",
      "initial_makeup_L": 1,
      "completed_medium_volume_L": null
    },
    "rationale": "The mass matches the local numeric value and the initial one-litre make-up supports an initial-stage basis. No local amount evidence is attached. Add exact stage-specific evidence, without treating this as a measured final concentration after Tris and later stocks."
  },
  {
    "quantity_id": "q7",
    "component_or_context": "KH2PO4 initial batch amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, KH 2 PO 4",
        "exact_source_quote": "KH 2 PO 4 0.05 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, initial mixture before subsequent additions",
        "exact_source_quote": "bring volume to 1.0 L.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "0.05",
      "initial_makeup_L": 1,
      "completed_medium_volume_L": null
    },
    "rationale": "The mass matches the local numeric value and the initial one-litre make-up supports an initial-stage basis. No local amount evidence is attached. Add exact stage-specific evidence, without treating this as a measured final concentration after Tris and later stocks."
  },
  {
    "quantity_id": "q8",
    "component_or_context": "NH4Cl initial batch amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, NH 4 Cl",
        "exact_source_quote": "NH 4 Cl 0.03 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, initial mixture before subsequent additions",
        "exact_source_quote": "bring volume to 1.0 L.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "0.03",
      "initial_makeup_L": 1,
      "completed_medium_volume_L": null
    },
    "rationale": "The mass matches the local numeric value and the initial one-litre make-up supports an initial-stage basis. No local amount evidence is attached. Add exact stage-specific evidence, without treating this as a measured final concentration after Tris and later stocks."
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Yeast extract initial batch amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, Yeast extract",
        "exact_source_quote": "Yeast extract 0.05 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, initial mixture before subsequent additions",
        "exact_source_quote": "bring volume to 1.0 L.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "0.05",
      "initial_makeup_L": 1,
      "completed_medium_volume_L": null
    },
    "rationale": "The mass matches the local numeric value and the initial one-litre make-up supports an initial-stage basis. No local amount evidence is attached. Add exact stage-specific evidence, without treating this as a measured final concentration after Tris and later stocks."
  },
  {
    "quantity_id": "q10",
    "component_or_context": "NaHCO3 late addition mass",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, NaHCO3",
        "exact_source_quote": "NaHCO 3 0.25 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, later stock additions",
        "exact_source_quote": "Filter-sterilize 8% (w/v) NaHCO 3 and 25% (w/v) sodium pyruvate solutions",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "nominal_mass_g": "0.25",
      "stock_percent_w_v": 8,
      "calculated_stock_dose_ml": 3.125,
      "final_g_per_L": null
    },
    "rationale": "The source withholds this ingredient from the initial litre and adds it later as a filtered stock. Preserve the stated mass, stock strength and separately calculated receiving dose; this is a correction of structured stage/basis, not a change to the source mass. No completed final-volume denominator is supplied."
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Sodium pyruvate late addition mass",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, Sodium pyruvate",
        "exact_source_quote": "Sodium pyruvate 1.0 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, later stock additions",
        "exact_source_quote": "Filter-sterilize 8% (w/v) NaHCO 3 and 25% (w/v) sodium pyruvate solutions",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "nominal_mass_g": "1.0",
      "stock_percent_w_v": 25,
      "calculated_stock_dose_ml": 4,
      "final_g_per_L": null
    },
    "rationale": "The source withholds this ingredient from the initial litre and adds it later as a filtered stock. Preserve the stated mass, stock strength and separately calculated receiving dose; this is a correction of structured stage/basis, not a change to the source mass. No completed final-volume denominator is supplied."
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Initial medium make-up",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, initial make-up",
        "exact_source_quote": "bring volume to 1.0 L.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "initial_volume_L": 1,
      "later_supplemented_volume_L": null
    },
    "rationale": "Already retained in local prose; attach evidence and preserve its position before Tris and filtered additions."
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Preparation pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "ph_value",
        "stored": 7.4,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "ph_value",
        "stored": 7.4,
        "decision": "evidence_only"
      },
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, initial pH adjustment",
        "exact_source_quote": "Adjust pH to 7.4 with 1 M Tris base and autoclave.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "pH": 7.4,
      "stage": "Initial mixture before autoclaving and late filtered additions"
    },
    "rationale": "The source supports the scalar only with this preparation scope; it does not explicitly report a later measured pH or organism-specific optimum."
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Tris adjustment stock strength",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, pH adjustment reagent",
        "exact_source_quote": "1 M Tris base",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "stock_molarity_M": 1,
      "dose_ml": null
    },
    "rationale": "The strength is present in both local descriptions; the dose remains unquantified, not one mole or one litre."
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Tris adjustment dose",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "not_quantified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, pH adjustment",
        "exact_source_quote": "Adjust pH to 7.4 with 1 M Tris base and autoclave.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "dose_ml": null,
      "target_pH": 7.4
    },
    "rationale": "No Tris dose is stated. Do not invent an amount or include a guessed contribution in the final-volume calculation."
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Bicarbonate stock strength",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, filtered stock strength",
        "exact_source_quote": "8% (w/v) NaHCO 3",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "percent_w_v": 8,
      "g_per_100_ml": 8
    },
    "rationale": "The w/v basis is explicit and already preserved in prose. Keep stock strength separate from main composition."
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Bicarbonate calculated stock dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, filtered stock strength",
        "exact_source_quote": "8% (w/v) NaHCO 3",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, nominal mass",
        "exact_source_quote": "NaHCO 3 0.25 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "derived_dose_ml": 3.125,
      "calculation": "0.25 g / (8 g / 100 mL) = 3.125 mL",
      "derivation_status": "calculated, not printed source dose"
    },
    "rationale": "This conditional dose follows exactly from the supplied mass and w/v strength. It belongs in a separately identified stock addition with arithmetic outside quotes; it does not establish final medium volume or license division by an assumed total."
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Pyruvate stock strength",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, filtered stock strength",
        "exact_source_quote": "25% (w/v) sodium pyruvate",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "percent_w_v": 25,
      "g_per_100_ml": 25
    },
    "rationale": "The w/v basis is explicit and already preserved in prose. Keep stock strength separate from main composition."
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Pyruvate calculated stock dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Preparation, filtered stock strength",
        "exact_source_quote": "25% (w/v) sodium pyruvate",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      },
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Main table, nominal mass",
        "exact_source_quote": "Sodium pyruvate 1.0 g",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "derived_dose_ml": 4,
      "calculation": "1 g / (25 g / 100 mL) = 4 mL",
      "derivation_status": "calculated, not printed source dose"
    },
    "rationale": "This conditional dose follows exactly from the supplied mass and w/v strength. It belongs in a separately identified stock addition with arithmetic outside quotes; it does not establish final medium volume or license division by an assumed total."
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Autoclave temperature collection default",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Collection default preceding medium 457",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "temperature_C": 121,
      "stage": "Initial mixture only; later bicarbonate and pyruvate are filter-sterilized"
    },
    "rationale": "The source default applies to this page without a contradictory exception. Local prose says autoclave but omits these numerical parameters; do not apply the cycle to the explicitly filtered stocks."
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Autoclave duration collection default",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Add components except NaHCO3 and sodium pyruvate to distilled water and bring volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium aseptically.",
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm457",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457",
        "source_locator": "Collection default preceding medium 457",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a",
        "parsed_text_sha256": "740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2",
        "accessed_at": "2026-10-21T17:37:00.399501Z"
      }
    ],
    "proposed_source_representation": {
      "duration_min": 15,
      "stage": "Initial mixture only; later bicarbonate and pyruvate are filter-sterilized"
    },
    "rationale": "The source default applies to this page without a contradictory exception. Local prose says autoclave but omits these numerical parameters; do not apply the cycle to the explicitly filtered stocks."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:000298.

10 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 10/11 primary and 9/11 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 11: primary 90.91%; secondary 81.82%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:000298.

15 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Current nitrate key versus historical legacy correspondence

grounding: concern. Targets: CultureMech:000298.

Both target and owner assert MediaIngredientMech:000171 for nitrate. The complete current pinned catalog/tree lookup is negative, while CHEBI:63005 correctly identifies sodium nitrate. Historical legacy correspondence remains unresolved; current absence is a completed lookup, not an unavailable current search or proof of historical invalidity.

### Exact owner and exclusion of a namesake

identity: supported. Targets: CultureMech:000298.

CultureMech:000298 denotes the archaea JCM 457 record. Its complete merge provenance and stable ID select only data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml. The same-basename bacterial CultureMech:009844 is excluded; no claims or evidence are transferred from it.

### Source-specific salt and mixture identities

grounding: supported. Targets: CultureMech:000298.

The exact sodium/potassium/ammonium salts, magnesium/calcium hydrates and sodium pyruvate match the asserted current chemical forms. Yeast extract remains an undefined mixture without a fabricated single-compound ID. The source distinguishes Tris base in preparation; no Tris hydrochloride or dose is inferred.

### Initial litre and separately filtered additions

completeness: concern. Targets: CultureMech:000298.

The local paragraph faithfully retains initial make-up, pH adjustment and separate filtering but omits the numerical collection autoclave default. Structured main rates do not encode late stock stages; the two calculated stock doses total 7.125 mL, but Tris dose and completed measured volume remain unspecified. No final denominator or final pH measurement is invented.

### Mixture classification and growth claims

scope: supported. Targets: CultureMech:000298.

Yeast extract supports a complex, semi-defined mixture and the primary describes liquid medium. The collection title and generic cultivation application do not establish a target taxon, phenotype, growth optimum or strain-specific performance. No unsupported organism claim is added.

### Meaning and limits of high_metal

scope: unknown. Targets: CultureMech:000298.

The primary independently establishes substantial Na/Mg/K/Ca salt inputs. Current metal analysis uses compound-name matching and an approximate aggregate, including fallback handling for enum units, with a cohort 90th-percentile cutoff; the writer keys by basename. This is not measured elemental concentration, and neither historical classifier inputs nor exact provenance of this flag is established here. The same-basename collision warrants stable-ID/path-scoped follow-up, but does not justify asserting high_metal false.

### Maintained inputs and append-only follow-up

ownership: supported. Targets: CultureMech:000298.

Only the exact archaea owner should receive any separately authorized correction. Preserve its history and legacy uncertainty; regenerate the derived target after stage-aware evidence is attached. Do not merge with the bacterial namesake or rewrite earlier import statements.

## Findings

### f1: Late filtered additions lack explicit structured stock scope

major / open / confirmed; issue key: culturemech.000298.late-stock-stage-basis.

Both layers list bicarbonate 0.25 and sodium pyruvate 1 G_PER_L as main concentrations while source preparation excludes them from the initial litre and adds filtered 8% (w/v) and 25% (w/v) stocks afterward. Existing prose retains the instruction, but completed final medium volume is unspecified.

### f2: Legacy nitrate mapping is unresolved in historical scope

minor / open / confirmed; issue key: culturemech.000298.legacy-nitrate-correspondence.

The exact legacy key survives in both layers and is absent from the current pinned catalog/tree. The primary nitrate and CHEBI identity are supported, but historical legacy correspondence is not recovered.

### f3: Numerical collection sterilization default is omitted

minor / open / confirmed; issue key: culturemech.000298.autoclave-default-context.

The local method names autoclaving but omits the exact page default 121 C for 15 minutes. That default concerns the initial mixture; the later stocks are explicitly filtered.

## Recommended Actions And Acceptance Checks

### a1

Retain nominal masses and the source preparation order, represent the late filtered stocks separately, and attach exact evidence for their strengths and derived 3.125 mL/4 mL doses. Scope the other values to the initial batch; do not rescale to a guessed completed volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the existing key and record the historical correspondence gap. Resolve it with version-specific provenance before changing secondary linkage; do not call current absence proof of historical invalidity.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add claim-level source context for the initial-mixture autoclave parameters while preserving the separate filtered-stock handling. Do not apply the cycle indiscriminately to every component.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch032/312/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-032/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch032/312/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml:1:id: CultureMech:000298<br>./data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml:1:id: CultureMech:000298<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch032/source-preflight-bound/312/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 15 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch032/source-preflight-bound/312/evidence-context-original.json; Complete frozen source context and full local objects | context_only | Frozen target/owner objects match freshly inspected records. Source interpretations are assessed against actual bound capture bytes; historical limitations remain separate. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457; Complete JCM 457 table, preparation paragraph and collection default | supports | Exact primary supplies the eleven batch masses, initial 1.0 L make-up, pH adjustment with 1 M Tris, late filter-sterilized 8% (w/v) bicarbonate and 25% (w/v) pyruvate, and the collection default 121 C for 15 minutes. It does not declare a measured final supplemented volume. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch032/312/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:50144 resolves to sodium pyruvate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63005 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63005 resolves to sodium nitrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml; data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml", "events": 7, "timestamp_issues": []}] |
| legacy-tree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Full pinned tree at exact source commit | context_only | The full current tree is not truncated; no exact legacy 000171 path is present. This completes a current negative lookup, not historical identity recovery. |
| legacy-catalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Full pinned current ingredient catalog | context_only | No exact MediaIngredientMech:000171 catalog identity was found. Existing nitrate CHEBI metadata resolves independently; do not infer that the old ID was invalid or assign a replacement legacy number. |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code read without execution or historical replay: metal analysis uses name-matched compounds, approximate/fallback unit weighting and a cohort percentile; label writer applies basename membership. Importer and merge code are context for future maintained-input corrections, not proof of historical causal execution. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code read without execution or historical replay: metal analysis uses name-matched compounds, approximate/fallback unit weighting and a cohort percentile; label writer applies basename membership. Importer and merge code are context for future maintained-input corrections, not proof of historical causal execution. |
| writer-2 | scripts/analyze_metal_concentrations.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code read without execution or historical replay: metal analysis uses name-matched compounds, approximate/fallback unit weighting and a cohort percentile; label writer applies basename membership. Importer and merge code are context for future maintained-input corrections, not proof of historical causal execution. |
| writer-3 | scripts/add_metal_ree_labels.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code read without execution or historical replay: metal analysis uses name-matched compounds, approximate/fallback unit weighting and a cohort percentile; label writer applies basename membership. Importer and merge code are context for future maintained-input corrections, not proof of historical causal execution. |
| writer-4 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code read without execution or historical replay: metal analysis uses name-matched compounds, approximate/fallback unit weighting and a cohort percentile; label writer applies basename membership. Importer and merge code are context for future maintained-input corrections, not proof of historical causal execution. |
| mediadiveJ457api-attempt | https://mediadive.dsmz.de/rest/medium/J457; Preserved exact public retrieval result | context_only | Exact current MediaDive J457 attempt returned HTTP 503. Primary JCM 457 formulation is available; this optional provider failure does not itself make the scientific comparison unavailable. |
| mediadiveJ457api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J457; Preserved exact public retrieval result | context_only | Exact current MediaDive J457 attempt returned HTTP 503. Primary JCM 457 formulation is available; this optional provider failure does not itself make the scientific comparison unavailable. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Required historical correspondence of the asserted MediaIngredientMech:000171 identifier remains unverified. Current catalog/tree absence is already a completed negative lookup, and primary formulation evidence remains available.
- Exact current MediaDive J457 attempt returned HTTP 503. Primary JCM 457 formulation is available; this optional provider failure does not itself make the scientific comparison unavailable.
- Exact current MediaDive J457 attempt returned HTTP 503. Primary JCM 457 formulation is available; this optional provider failure does not itself make the scientific comparison unavailable.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T175835Z-culturemech-000298-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: artificial_seawater_for_halophiles (CultureMech:000298)'
started_at: '2026-10-21T17:54:21Z'
finished_at: '2026-10-21T17:58:35Z'
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
summary: JCM 457 supports all eleven nominal ingredient masses and explicitly separates
  an initial one-litre preparation from filtered bicarbonate and pyruvate additions.
  Local prose preserves much of this staging, but the structured main G_PER_L fields
  do not distinguish the later stock amounts or establish a completed final volume.
  Required historical correspondence of nitrate legacy MediaIngredientMech:000171
  remains unresolved despite a completed current negative lookup. The exact archaea
  owner is retained; the bacterial namesake is not a contributor.
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
  - path: data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml
    sha256: 0f553fffb62a1b9e2be5d538460917ddddb173694c21245e2ba3cc98e6733ba1
    role: target
  - path: data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml
    sha256: 5ca0d3ace0aaf658c568de419e5962951f61c966db785342e71fdcf743792175
    role: context
  - path: data/normalized_yaml/bacterial/artificial_seawater_for_halophiles.yaml
    sha256: 8377a320fb2db597006d0c3e6c8c2b105f6e192451a40bd6da57678a5b88db49
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/archaea/artificial_seawater_for_halophiles.yaml.md
    sha256: 714b02e630a2f9fcce470884da07a1bac7b60fea625d76d12f36749e41324833
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_metal_ree_labels.py
    sha256: f4d45eaf1e633af60de15629b7b85371ea6d509052b6161fad63f7b607853b10
    role: context
  - path: scripts/analyze_metal_concentrations.py
    sha256: d9e414741123d14bf7350f57bd280eb2188bc9fc1a87917ce3d96a45c9d826cf
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
  selection: Task review 312; batch 032 item 2 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-one task batches
    contain 310 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 313 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000298
targets:
- target_id: CultureMech:000298
  path: data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml
  label: artificial_seawater_for_halophiles
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch032/312/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-032/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch032/312/strict.tsv"
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000298
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
  - CultureMech:000298
- check_id: legacy-000171-history
  name: Required source-scope verification
  required: true
  status: unavailable
  summary: Required historical correspondence of the asserted MediaIngredientMech:000171
    identifier remains unverified. Current catalog/tree absence is already a completed
    negative lookup, and primary formulation evidence remains available.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - legacy-tree
  - legacy-catalog
  - record
- check_id: mediadiveJ457api-source-access
  name: 'Exact source content access: mediadiveJ457api'
  required: false
  status: unavailable
  summary: Exact current MediaDive J457 attempt returned HTTP 503. Primary JCM 457
    formulation is available; this optional provider failure does not itself make
    the scientific comparison unavailable.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - mediadiveJ457api-attempt
- check_id: mediadiveJ457api_retry-source-access
  name: 'Exact source content access: mediadiveJ457api_retry'
  required: false
  status: unavailable
  summary: Exact current MediaDive J457 attempt returned HTTP 503. Primary JCM 457
    formulation is available; this optional provider failure does not itself make
    the scientific comparison unavailable.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - mediadiveJ457api_retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T17:58:33Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T17:58:33Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:54:52.425069Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch032/312/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T17:54:56.232179Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-032/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch032/312/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:55:00.298359Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:55:01.544549Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T17:58:33Z'
  support: supports
  summary: './data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml:1:id:
    CultureMech:000298

    ./data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml:1:id: CultureMech:000298

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch032/source-preflight-bound/312/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T17:58:33Z'
  support: supports
  summary: 15 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: e5fbf8e026b1ef5cdb9ffac5a2f1244604eed4214138b2c33d55b6c4bd609e0b
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch032/source-preflight-bound/312/evidence-context-original.json
  locator: Complete frozen source context and full local objects
  accessed_at: '2026-10-21T17:58:33Z'
  support: context_only
  summary: Frozen target/owner objects match freshly inspected records. Source interpretations
    are assessed against actual bound capture bytes; historical limitations remain
    separate.
  snapshot_sha256: 72fc26def343f656aa8aa7ab88704ecc49536d593702ab0dfeb2fed23d46f362
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457
  locator: Complete JCM 457 table, preparation paragraph and collection default
  accessed_at: '2026-10-21T17:37:00.399501Z'
  support: supports
  summary: Exact primary supplies the eleven batch masses, initial 1.0 L make-up,
    pH adjustment with 1 M Tris, late filter-sterilized 8% (w/v) bicarbonate and 25%
    (w/v) pyruvate, and the collection default 121 C for 15 minutes. It does not declare
    a measured final supplemented volume.
  snapshot_sha256: 04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch032/312/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T17:58:33Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 59e6b05c9666d9441f9b606aa81819f1b95dcd76907efb755576633f2e2bc31e
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
- evidence_id: chebi50144
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:22:07.440767Z'
  support: supports
  summary: CHEBI:50144 resolves to sodium pyruvate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 457ed29adfdea68c420ea0c094d7d75593958fc70f908f6809348e4e12e7e15d
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T17:58:33Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label":
    "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label":
    "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type":
    "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate",
    "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml; data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T17:58:33Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: legacy-tree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Full pinned tree at exact source commit
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: context_only
  summary: The full current tree is not truncated; no exact legacy 000171 path is
    present. This completes a current negative lookup, not historical identity recovery.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: legacy-catalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Full pinned current ingredient catalog
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: context_only
  summary: No exact MediaIngredientMech:000171 catalog identity was found. Existing
    nitrate CHEBI metadata resolves independently; do not infer that the old ID was
    invalid or assign a replacement legacy number.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T17:58:33Z'
  support: context_only
  summary: 'Current code read without execution or historical replay: metal analysis
    uses name-matched compounds, approximate/fallback unit weighting and a cohort
    percentile; label writer applies basename membership. Importer and merge code
    are context for future maintained-input corrections, not proof of historical causal
    execution.'
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T17:58:33Z'
  support: context_only
  summary: 'Current code read without execution or historical replay: metal analysis
    uses name-matched compounds, approximate/fallback unit weighting and a cohort
    percentile; label writer applies basename membership. Importer and merge code
    are context for future maintained-input corrections, not proof of historical causal
    execution.'
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: scripts/analyze_metal_concentrations.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T17:58:33Z'
  support: context_only
  summary: 'Current code read without execution or historical replay: metal analysis
    uses name-matched compounds, approximate/fallback unit weighting and a cohort
    percentile; label writer applies basename membership. Importer and merge code
    are context for future maintained-input corrections, not proof of historical causal
    execution.'
  snapshot_sha256: d9e414741123d14bf7350f57bd280eb2188bc9fc1a87917ce3d96a45c9d826cf
- evidence_id: writer-3
  kind: record_content
  reference: scripts/add_metal_ree_labels.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T17:58:33Z'
  support: context_only
  summary: 'Current code read without execution or historical replay: metal analysis
    uses name-matched compounds, approximate/fallback unit weighting and a cohort
    percentile; label writer applies basename membership. Importer and merge code
    are context for future maintained-input corrections, not proof of historical causal
    execution.'
  snapshot_sha256: f4d45eaf1e633af60de15629b7b85371ea6d509052b6161fad63f7b607853b10
- evidence_id: writer-4
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T17:58:33Z'
  support: context_only
  summary: 'Current code read without execution or historical replay: metal analysis
    uses name-matched compounds, approximate/fallback unit weighting and a cohort
    percentile; label writer applies basename membership. Importer and merge code
    are context for future maintained-input corrections, not proof of historical causal
    execution.'
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: mediadiveJ457api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J457
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:36:58.847220Z'
  support: context_only
  summary: Exact current MediaDive J457 attempt returned HTTP 503. Primary JCM 457
    formulation is available; this optional provider failure does not itself make
    the scientific comparison unavailable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ457api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J457
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:38:20.163877Z'
  support: context_only
  summary: Exact current MediaDive J457 attempt returned HTTP 503. Primary JCM 457
    formulation is available; this optional provider failure does not itself make
    the scientific comparison unavailable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 21 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    NaCl initial batch amount\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"195\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\",\n\
    \        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"195\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Main table, NaCl\",\n        \"exact_source_quote\": \"NaCl 195.0 g\",\n \
    \       \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, initial mixture before subsequent\
    \ additions\",\n        \"exact_source_quote\": \"bring volume to 1.0 L.\",\n\
    \        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"batch_amount_g\": \"195.0\"\
    ,\n      \"initial_makeup_L\": 1,\n      \"completed_medium_volume_L\": null\n\
    \    },\n    \"rationale\": \"The mass matches the local numeric value and the\
    \ initial one-litre make-up supports an initial-stage basis. No local amount evidence\
    \ is attached. Add exact stage-specific evidence, without treating this as a measured\
    \ final concentration after Tris and later stocks.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q2\",\n    \"component_or_context\": \"MgCl2 x 6 H2O initial batch amount\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"35\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\",\n\
    \        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"35\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Main table, MgCl 2 ·6H 2 O\",\n        \"exact_source_quote\": \"MgCl 2 ·6H\
    \ 2 O 35.0 g\",\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, initial mixture before subsequent\
    \ additions\",\n        \"exact_source_quote\": \"bring volume to 1.0 L.\",\n\
    \        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"batch_amount_g\": \"35.0\"\
    ,\n      \"initial_makeup_L\": 1,\n      \"completed_medium_volume_L\": null\n\
    \    },\n    \"rationale\": \"The mass matches the local numeric value and the\
    \ initial one-litre make-up supports an initial-stage basis. No local amount evidence\
    \ is attached. Add exact stage-specific evidence, without treating this as a measured\
    \ final concentration after Tris and later stocks.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q3\",\n    \"component_or_context\": \"MgSO4 x 7 H2O initial batch amount\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\",\n\
    \        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Main table, MgSO 4 ·7H 2 O\",\n        \"exact_source_quote\": \"MgSO 4 ·7H\
    \ 2 O 50.0 g\",\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, initial mixture before subsequent\
    \ additions\",\n        \"exact_source_quote\": \"bring volume to 1.0 L.\",\n\
    \        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"batch_amount_g\": \"50.0\"\
    ,\n      \"initial_makeup_L\": 1,\n      \"completed_medium_volume_L\": null\n\
    \    },\n    \"rationale\": \"The mass matches the local numeric value and the\
    \ initial one-litre make-up supports an initial-stage basis. No local amount evidence\
    \ is attached. Add exact stage-specific evidence, without treating this as a measured\
    \ final concentration after Tris and later stocks.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q4\",\n    \"component_or_context\": \"KCl initial batch amount\",\n    \"\
    decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\",\n      \
    \  \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\",\n\
    \        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Main table, KCl\",\n        \"exact_source_quote\": \"KCl 5.0 g\",\n     \
    \   \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, initial mixture before subsequent\
    \ additions\",\n        \"exact_source_quote\": \"bring volume to 1.0 L.\",\n\
    \        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"batch_amount_g\": \"5.0\"\
    ,\n      \"initial_makeup_L\": 1,\n      \"completed_medium_volume_L\": null\n\
    \    },\n    \"rationale\": \"The mass matches the local numeric value and the\
    \ initial one-litre make-up supports an initial-stage basis. No local amount evidence\
    \ is attached. Add exact stage-specific evidence, without treating this as a measured\
    \ final concentration after Tris and later stocks.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q5\",\n    \"component_or_context\": \"NaNO3 initial batch amount\",\n   \
    \ \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\",\n\
    \        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Main table, NaNO 3\",\n        \"exact_source_quote\": \"NaNO 3 1.0 g\",\n\
    \        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, initial mixture before subsequent\
    \ additions\",\n        \"exact_source_quote\": \"bring volume to 1.0 L.\",\n\
    \        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"batch_amount_g\": \"1.0\"\
    ,\n      \"initial_makeup_L\": 1,\n      \"completed_medium_volume_L\": null\n\
    \    },\n    \"rationale\": \"The mass matches the local numeric value and the\
    \ initial one-litre make-up supports an initial-stage basis. No local amount evidence\
    \ is attached. Add exact stage-specific evidence, without treating this as a measured\
    \ final concentration after Tris and later stocks.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q6\",\n    \"component_or_context\": \"CaCl2 x 2 H2O initial batch amount\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\",\n\
    \        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Main table, CaCl 2 ·2H 2 O\",\n        \"exact_source_quote\": \"CaCl 2 ·2H\
    \ 2 O 0.5 g\",\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, initial mixture before subsequent\
    \ additions\",\n        \"exact_source_quote\": \"bring volume to 1.0 L.\",\n\
    \        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"batch_amount_g\": \"0.5\"\
    ,\n      \"initial_makeup_L\": 1,\n      \"completed_medium_volume_L\": null\n\
    \    },\n    \"rationale\": \"The mass matches the local numeric value and the\
    \ initial one-litre make-up supports an initial-stage basis. No local amount evidence\
    \ is attached. Add exact stage-specific evidence, without treating this as a measured\
    \ final concentration after Tris and later stocks.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q7\",\n    \"component_or_context\": \"KH2PO4 initial batch amount\",\n  \
    \  \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\",\n\
    \        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Main table, KH 2 PO 4\",\n        \"exact_source_quote\": \"KH 2 PO 4 0.05\
    \ g\",\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, initial mixture before subsequent\
    \ additions\",\n        \"exact_source_quote\": \"bring volume to 1.0 L.\",\n\
    \        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"batch_amount_g\": \"0.05\"\
    ,\n      \"initial_makeup_L\": 1,\n      \"completed_medium_volume_L\": null\n\
    \    },\n    \"rationale\": \"The mass matches the local numeric value and the\
    \ initial one-litre make-up supports an initial-stage basis. No local amount evidence\
    \ is attached. Add exact stage-specific evidence, without treating this as a measured\
    \ final concentration after Tris and later stocks.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q8\",\n    \"component_or_context\": \"NH4Cl initial batch amount\",\n   \
    \ \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\",\n\
    \        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Main table, NH 4 Cl\",\n        \"exact_source_quote\": \"NH 4 Cl 0.03 g\"\
    ,\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, initial mixture before subsequent\
    \ additions\",\n        \"exact_source_quote\": \"bring volume to 1.0 L.\",\n\
    \        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"batch_amount_g\": \"0.03\"\
    ,\n      \"initial_makeup_L\": 1,\n      \"completed_medium_volume_L\": null\n\
    \    },\n    \"rationale\": \"The mass matches the local numeric value and the\
    \ initial one-litre make-up supports an initial-stage basis. No local amount evidence\
    \ is attached. Add exact stage-specific evidence, without treating this as a measured\
    \ final concentration after Tris and later stocks.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q9\",\n    \"component_or_context\": \"Yeast extract initial batch amount\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\",\n\
    \        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Main table, Yeast extract\",\n        \"exact_source_quote\": \"Yeast extract\
    \ 0.05 g\",\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, initial mixture before subsequent\
    \ additions\",\n        \"exact_source_quote\": \"bring volume to 1.0 L.\",\n\
    \        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"batch_amount_g\": \"0.05\"\
    ,\n      \"initial_makeup_L\": 1,\n      \"completed_medium_volume_L\": null\n\
    \    },\n    \"rationale\": \"The mass matches the local numeric value and the\
    \ initial one-litre make-up supports an initial-stage basis. No local amount evidence\
    \ is attached. Add exact stage-specific evidence, without treating this as a measured\
    \ final concentration after Tris and later stocks.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q10\",\n    \"component_or_context\": \"NaHCO3 late addition mass\",\n   \
    \ \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\",\n      \
    \  \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Main table, NaHCO3\",\n        \"exact_source_quote\": \"NaHCO 3 0.25 g\"\
    ,\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, later stock additions\",\n     \
    \   \"exact_source_quote\": \"Filter-sterilize 8% (w/v) NaHCO 3 and 25% (w/v)\
    \ sodium pyruvate solutions\",\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"nominal_mass_g\": \"0.25\"\
    ,\n      \"stock_percent_w_v\": 8,\n      \"calculated_stock_dose_ml\": 3.125,\n\
    \      \"final_g_per_L\": null\n    },\n    \"rationale\": \"The source withholds\
    \ this ingredient from the initial litre and adds it later as a filtered stock.\
    \ Preserve the stated mass, stock strength and separately calculated receiving\
    \ dose; this is a correction of structured stage/basis, not a change to the source\
    \ mass. No completed final-volume denominator is supplied.\"\n  },\n  {\n    \"\
    quantity_id\": \"q11\",\n    \"component_or_context\": \"Sodium pyruvate late\
    \ addition mass\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Main table, Sodium pyruvate\",\n        \"exact_source_quote\": \"Sodium pyruvate\
    \ 1.0 g\",\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, later stock additions\",\n     \
    \   \"exact_source_quote\": \"Filter-sterilize 8% (w/v) NaHCO 3 and 25% (w/v)\
    \ sodium pyruvate solutions\",\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"nominal_mass_g\": \"1.0\"\
    ,\n      \"stock_percent_w_v\": 25,\n      \"calculated_stock_dose_ml\": 4,\n\
    \      \"final_g_per_L\": null\n    },\n    \"rationale\": \"The source withholds\
    \ this ingredient from the initial litre and adds it later as a filtered stock.\
    \ Preserve the stated mass, stock strength and separately calculated receiving\
    \ dose; this is a correction of structured stage/basis, not a change to the source\
    \ mass. No completed final-volume denominator is supplied.\"\n  },\n  {\n    \"\
    quantity_id\": \"q12\",\n    \"component_or_context\": \"Initial medium make-up\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"evidence_only\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"evidence_only\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm457\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, initial make-up\",\n        \"exact_source_quote\"\
    : \"bring volume to 1.0 L.\",\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"initial_volume_L\": 1,\n \
    \     \"later_supplemented_volume_L\": null\n    },\n    \"rationale\": \"Already\
    \ retained in local prose; attach evidence and preserve its position before Tris\
    \ and filtered additions.\"\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"\
    component_or_context\": \"Preparation pH\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.4,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.4,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"evidence_only\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"evidence_only\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm457\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, initial pH adjustment\",\n     \
    \   \"exact_source_quote\": \"Adjust pH to 7.4 with 1 M Tris base and autoclave.\"\
    ,\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"pH\": 7.4,\n      \"stage\"\
    : \"Initial mixture before autoclaving and late filtered additions\"\n    },\n\
    \    \"rationale\": \"The source supports the scalar only with this preparation\
    \ scope; it does not explicitly report a later measured pH or organism-specific\
    \ optimum.\"\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Tris adjustment stock strength\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"evidence_only\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"evidence_only\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm457\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, pH adjustment reagent\",\n     \
    \   \"exact_source_quote\": \"1 M Tris base\",\n        \"snapshot_sha256\": \"\
    04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\",\n        \"\
    parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_molarity_M\": 1,\n \
    \     \"dose_ml\": null\n    },\n    \"rationale\": \"The strength is present\
    \ in both local descriptions; the dose remains unquantified, not one mole or one\
    \ litre.\"\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"Tris adjustment dose\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"not_quantified\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"not_quantified\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm457\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, pH adjustment\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 7.4 with 1 M Tris base and autoclave.\",\n        \"snapshot_sha256\"\
    : \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\",\n    \
    \    \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"dose_ml\": null,\n      \"\
    target_pH\": 7.4\n    },\n    \"rationale\": \"No Tris dose is stated. Do not\
    \ invent an amount or include a guessed contribution in the final-volume calculation.\"\
    \n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\": \"Bicarbonate\
    \ stock strength\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"evidence_only\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"evidence_only\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm457\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, filtered stock strength\",\n   \
    \     \"exact_source_quote\": \"8% (w/v) NaHCO 3\",\n        \"snapshot_sha256\"\
    : \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\",\n    \
    \    \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"percent_w_v\": 8,\n      \"\
    g_per_100_ml\": 8\n    },\n    \"rationale\": \"The w/v basis is explicit and\
    \ already preserved in prose. Keep stock strength separate from main composition.\"\
    \n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\": \"Bicarbonate\
    \ calculated stock dose\",\n    \"decision\": \"add\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, filtered stock strength\",\n   \
    \     \"exact_source_quote\": \"8% (w/v) NaHCO 3\",\n        \"snapshot_sha256\"\
    : \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\",\n    \
    \    \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Main table, nominal mass\",\n        \"exact_source_quote\"\
    : \"NaHCO 3 0.25 g\",\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"derived_dose_ml\": 3.125,\n\
    \      \"calculation\": \"0.25 g / (8 g / 100 mL) = 3.125 mL\",\n      \"derivation_status\"\
    : \"calculated, not printed source dose\"\n    },\n    \"rationale\": \"This conditional\
    \ dose follows exactly from the supplied mass and w/v strength. It belongs in\
    \ a separately identified stock addition with arithmetic outside quotes; it does\
    \ not establish final medium volume or license division by an assumed total.\"\
    \n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\": \"Pyruvate\
    \ stock strength\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"evidence_only\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"evidence_only\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm457\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, filtered stock strength\",\n   \
    \     \"exact_source_quote\": \"25% (w/v) sodium pyruvate\",\n        \"snapshot_sha256\"\
    : \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\",\n    \
    \    \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"percent_w_v\": 25,\n     \
    \ \"g_per_100_ml\": 25\n    },\n    \"rationale\": \"The w/v basis is explicit\
    \ and already preserved in prose. Keep stock strength separate from main composition.\"\
    \n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\": \"Pyruvate\
    \ calculated stock dose\",\n    \"decision\": \"add\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Preparation, filtered stock strength\",\n   \
    \     \"exact_source_quote\": \"25% (w/v) sodium pyruvate\",\n        \"snapshot_sha256\"\
    : \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\",\n    \
    \    \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      },\n      {\n\
    \        \"source_key\": \"jcm457\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\"\
    ,\n        \"source_locator\": \"Main table, nominal mass\",\n        \"exact_source_quote\"\
    : \"Sodium pyruvate 1.0 g\",\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"derived_dose_ml\": 4,\n  \
    \    \"calculation\": \"1 g / (25 g / 100 mL) = 4 mL\",\n      \"derivation_status\"\
    : \"calculated, not printed source dose\"\n    },\n    \"rationale\": \"This conditional\
    \ dose follows exactly from the supplied mass and w/v strength. It belongs in\
    \ a separately identified stock addition with arithmetic outside quotes; it does\
    \ not establish final medium volume or license division by an assumed total.\"\
    \n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\": \"Autoclave\
    \ temperature collection default\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"add\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Collection default preceding medium 457\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"temperature_C\": 121,\n  \
    \    \"stage\": \"Initial mixture only; later bicarbonate and pyruvate are filter-sterilized\"\
    \n    },\n    \"rationale\": \"The source default applies to this page without\
    \ a contradictory exception. Local prose says autoclave but omits these numerical\
    \ parameters; do not apply the cycle to the explicitly filtered stocks.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\": \"Autoclave\
    \ duration collection default\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"add\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Add components except NaHCO3 and sodium pyruvate to distilled water and bring\
    \ volume to 1.0 L. Adjust pH to 7.4 with 1 M Tris base and autoclave. Filter-sterilize\
    \ 8% (w/v) NaHCO3 and 25% (w/v) sodium pyruvate solutions and add to the medium\
    \ aseptically.\",\n        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm457\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=457\",\n        \"source_locator\"\
    : \"Collection default preceding medium 457\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"04c75c538119081b1ee864a123c3c039a819f6917c26b7815a97b63c2700183a\"\
    ,\n        \"parsed_text_sha256\": \"740736915b3a0ccdd8130607785e9c608664e37d1dab58a90f33f62c45afdae2\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:37:00.399501Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"duration_min\": 15,\n    \
    \  \"stage\": \"Initial mixture only; later bicarbonate and pyruvate are filter-sterilized\"\
    \n    },\n    \"rationale\": \"The source default applies to this page without\
    \ a contradictory exception. Local prose says autoclave but omits these numerical\
    \ parameters; do not apply the cycle to the explicitly filtered stocks.\"\n  }\n\
    ]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '10 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 10/11
    primary and 9/11 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi26710
  - chebi31206
  - chebi31795
  - chebi32139
  - chebi32588
  - chebi50144
  - chebi63005
  - chebi63036
  - chebi86158
  - chebi86345
  details: 'Instance coverage on a 0–100 percent scale, denominator 11: primary 90.91%;
    secondary 81.82%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 15 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: legacy-grounding
  area: grounding
  topic: Current nitrate key versus historical legacy correspondence
  outcome: concern
  summary: Both target and owner assert MediaIngredientMech:000171 for nitrate. The
    complete current pinned catalog/tree lookup is negative, while CHEBI:63005 correctly
    identifies sodium nitrate. Historical legacy correspondence remains unresolved;
    current absence is a completed lookup, not an unavailable current search or proof
    of historical invalidity.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - record
  - owner-0
  - legacy-tree
  - legacy-catalog
  - chebi63005
- assessment_id: identity
  area: identity
  topic: Exact owner and exclusion of a namesake
  outcome: supported
  summary: CultureMech:000298 denotes the archaea JCM 457 record. Its complete merge
    provenance and stable ID select only data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml.
    The same-basename bacterial CultureMech:009844 is excluded; no claims or evidence
    are transferred from it.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - record
  - owner-0
  - id-search
  - bound-context
  - primary
- assessment_id: forms
  area: grounding
  topic: Source-specific salt and mixture identities
  outcome: supported
  summary: The exact sodium/potassium/ammonium salts, magnesium/calcium hydrates and
    sodium pyruvate match the asserted current chemical forms. Yeast extract remains
    an undefined mixture without a fabricated single-compound ID. The source distinguishes
    Tris base in preparation; no Tris hydrochloride or dose is inferred.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - primary
  - record
  - chebi50144
  - chebi31795
  - chebi86345
  - chebi86158
- assessment_id: preparation
  area: completeness
  topic: Initial litre and separately filtered additions
  outcome: concern
  summary: The local paragraph faithfully retains initial make-up, pH adjustment and
    separate filtering but omits the numerical collection autoclave default. Structured
    main rates do not encode late stock stages; the two calculated stock doses total
    7.125 mL, but Tris dose and completed measured volume remain unspecified. No final
    denominator or final pH measurement is invented.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - primary
  - quantity-inventory
  - record
  - owner-0
- assessment_id: classification
  area: scope
  topic: Mixture classification and growth claims
  outcome: supported
  summary: Yeast extract supports a complex, semi-defined mixture and the primary
    describes liquid medium. The collection title and generic cultivation application
    do not establish a target taxon, phenotype, growth optimum or strain-specific
    performance. No unsupported organism claim is added.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - primary
  - record
- assessment_id: metal-classification
  area: scope
  topic: Meaning and limits of high_metal
  outcome: unknown
  summary: The primary independently establishes substantial Na/Mg/K/Ca salt inputs.
    Current metal analysis uses compound-name matching and an approximate aggregate,
    including fallback handling for enum units, with a cohort 90th-percentile cutoff;
    the writer keys by basename. This is not measured elemental concentration, and
    neither historical classifier inputs nor exact provenance of this flag is established
    here. The same-basename collision warrants stable-ID/path-scoped follow-up, but
    does not justify asserting high_metal false.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - primary
  - record
  - writer-2
  - writer-3
  - bound-context
- assessment_id: ownership
  area: ownership
  topic: Maintained inputs and append-only follow-up
  outcome: supported
  summary: Only the exact archaea owner should receive any separately authorized correction.
    Preserve its history and legacy uncertainty; regenerate the derived target after
    stage-aware evidence is attached. Do not merge with the bacterial namesake or
    rewrite earlier import statements.
  target_ids:
  - CultureMech:000298
  evidence_ids:
  - record
  - owner-0
  - writer-0
  - writer-4
findings:
- finding_id: f1
  issue_key: culturemech.000298.late-stock-stage-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Late filtered additions lack explicit structured stock scope
  description: Both layers list bicarbonate 0.25 and sodium pyruvate 1 G_PER_L as
    main concentrations while source preparation excludes them from the initial litre
    and adds filtered 8% (w/v) and 25% (w/v) stocks afterward. Existing prose retains
    the instruction, but completed final medium volume is unspecified.
  target_ids:
  - CultureMech:000298
  field_paths:
  - ingredients[4].concentration
  - ingredients[10].concentration
  - solutions
  - preparation_steps[0].description
  evidence_ids:
  - primary
  - quantity-inventory
  - record
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml
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
  issue_key: culturemech.000298.legacy-nitrate-correspondence
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Legacy nitrate mapping is unresolved in historical scope
  description: The exact legacy key survives in both layers and is absent from the
    current pinned catalog/tree. The primary nitrate and CHEBI identity are supported,
    but historical legacy correspondence is not recovered.
  target_ids:
  - CultureMech:000298
  field_paths:
  - ingredients[5].mediaingredientmech_term
  evidence_ids:
  - legacy-tree
  - legacy-catalog
  - chebi63005
  - record
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.000298.autoclave-default-context
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Numerical collection sterilization default is omitted
  description: The local method names autoclaving but omits the exact page default
    121 C for 15 minutes. That default concerns the initial mixture; the later stocks
    are explicitly filtered.
  target_ids:
  - CultureMech:000298
  field_paths:
  - preparation_steps[0]
  evidence_ids:
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml
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
  description: Retain nominal masses and the source preparation order, represent the
    late filtered stocks separately, and attach exact evidence for their strengths
    and derived 3.125 mL/4 mL doses. Scope the other values to the initial batch;
    do not rescale to a guessed completed volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000298
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml
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
  description: Preserve the existing key and record the historical correspondence
    gap. Resolve it with version-specific provenance before changing secondary linkage;
    do not call current absence proof of historical invalidity.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000298
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml
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
  description: Add claim-level source context for the initial-mixture autoclave parameters
    while preserving the separate filtered-stock handling. Do not apply the cycle
    indiscriminately to every component.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000298
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml
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
- Required historical correspondence of the asserted MediaIngredientMech:000171 identifier
  remains unverified. Current catalog/tree absence is already a completed negative
  lookup, and primary formulation evidence remains available.
- Exact current MediaDive J457 attempt returned HTTP 503. Primary JCM 457 formulation
  is available; this optional provider failure does not itself make the scientific
  comparison unavailable.
- Exact current MediaDive J457 attempt returned HTTP 503. Primary JCM 457 formulation
  is available; this optional provider failure does not itself make the scientific
  comparison unavailable.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-032
- generated-medium
```
