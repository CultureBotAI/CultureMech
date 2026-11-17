# Source and formulation review: bb (CultureMech:000053)

- Review: 20261021T223702Z-culturemech-000053-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T22:32:17Z
- Finished UTC: 2026-10-21T22:37:02Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The algae BB record contains only six stock-level quantities from the complete CCAP Bold’s Basal formulation and presents them as main-medium rates. All ten stock stages and receiving doses need reconstruction. The source spells MoO3, whereas the local unmapped name is MoO. Generic temperature and lighting ranges are unsupported by this exact primary; the excluded bacterial BB record is not an owner.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 393; batch 040 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-nine task batches contain 390 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 393 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000053 | data/merge_yaml/merged/BB.yaml | generated | bb |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000053 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000053 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch040/393/strict.tsv |
| validate-terms | passed | True | CultureMech:000053 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000053 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000053 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000053.

The four documented recipes completed; interpret the scope of each separately.

### Exact algae BB owner and excluded namesake

identity: supported. Targets: CultureMech:000053.

CultureMech:000053 is the algae BB owner and sole merge contributor, corresponding to the exact CCAP MR_BB primary. Bacterial bb.yaml CultureMech:000320 has another source identity and is not an owner or a recipe-completion shortcut. The source title is a broad freshwater-algae medium description, not strain-specific growth evidence.

### Asserted and missing chemical identities

grounding: concern. Targets: CultureMech:000053.

All 10 asserted primary term instances across the two layers resolve with matching current labels. Target primary linkage is 5/6 (83.33%); no current or legacy secondary field is asserted (0/6 linkage, not a false missing-key lookup). MoO must be reconciled to the literal source MoO3, while the already corrected cobalt nitrate hexahydrate remains unchanged. No replacement identifier is invented.

### All stock constituents and receiving recipe

completeness: concern. Targets: CultureMech:000053.

Only the five trace-stock components and KOH are retained. Stocks 1–6, boric acid, EDTA, iron/acid stock, stock bases and all receiving doses are absent. Six stock-level values at root scope cannot stand in for this complete ten-stock medium.

### Composition and environmental assertions

consistency: concern. Targets: CultureMech:000053.

The complete source lists specified chemical stocks and is a chemically defined formulation, contrary to COMPLEX/UNDEFINED. LIQUID is consistent. Exact primary supports no numeric temperature, light intensity or photoperiod; no taxon, strain or salt/oxygen requirement is inferred.

### Source hints versus attached evidence and current writer scope

provenance: concern. Targets: CultureMech:000053.

Ingredient source strings and automated mapping metadata are not attached exact amount evidence. All recorded history and mapping timestamps are retained in the inventories; current source and stable owner identity permit a complete review. Preserve the prior cobalt repair while correcting independently demonstrated remaining issues.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:000053.

20 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:000053.

31 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Stock 1: NaNO3",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 1 component",
        "exact_source_quote": "NaNO3  10.0 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 1",
        "exact_source_quote": "per 400 ml",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 10.0,
      "unit": "g",
      "stock_number": 1,
      "stock_recipe_basis_ml": 400,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "This source component is missing; add it only within its numbered stock and preserve its recipe basis."
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Stock 2: MgSO4.7H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 2 component",
        "exact_source_quote": "MgSO4.7H2O  3.0 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 2",
        "exact_source_quote": "per 400 ml",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 3.0,
      "unit": "g",
      "stock_number": 2,
      "stock_recipe_basis_ml": 400,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "This source component is missing; add it only within its numbered stock and preserve its recipe basis."
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Stock 3: NaCl",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 3 component",
        "exact_source_quote": "NaCl  1.0 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 3",
        "exact_source_quote": "per 400 ml",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 1.0,
      "unit": "g",
      "stock_number": 3,
      "stock_recipe_basis_ml": 400,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "This source component is missing; add it only within its numbered stock and preserve its recipe basis."
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Stock 4: K2HPO4",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 4 component",
        "exact_source_quote": "K2HPO4  3.0 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 4",
        "exact_source_quote": "per 400 ml",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 3.0,
      "unit": "g",
      "stock_number": 4,
      "stock_recipe_basis_ml": 400,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "This source component is missing; add it only within its numbered stock and preserve its recipe basis."
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Stock 5: KH2PO4",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 5 component",
        "exact_source_quote": "KH2PO4  7.0 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 5",
        "exact_source_quote": "per 400 ml",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 7.0,
      "unit": "g",
      "stock_number": 5,
      "stock_recipe_basis_ml": 400,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "This source component is missing; add it only within its numbered stock and preserve its recipe basis."
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Stock 6: CaCl2.2H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 6 component",
        "exact_source_quote": "CaCl2.2H2O  1.0 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 6",
        "exact_source_quote": "per 400 ml",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 1.0,
      "unit": "g",
      "stock_number": 6,
      "stock_recipe_basis_ml": 400,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "This source component is missing; add it only within its numbered stock and preserve its recipe basis."
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Stock 7: ZnSO4.7H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "8.82",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "8.82",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 7 component",
        "exact_source_quote": "ZnSO4.7H2O  8.82 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 7",
        "exact_source_quote": "per litre",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 8.82,
      "unit": "g",
      "stock_number": 7,
      "stock_recipe_basis_ml": 1000,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "The local numeral is a stock-recipe amount presented at main-medium scope. Move it into the named stock and bind the receiving dose separately; no automatic main-medium interpretation is valid. For local MoO, also restore the exact source name MoO3 without inventing an ontology ID."
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Stock 7: MnCl2.4H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.44",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.44",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 7 component",
        "exact_source_quote": "MnCl2.4H2O  1.44 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 7",
        "exact_source_quote": "per litre",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 1.44,
      "unit": "g",
      "stock_number": 7,
      "stock_recipe_basis_ml": 1000,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "The local numeral is a stock-recipe amount presented at main-medium scope. Move it into the named stock and bind the receiving dose separately; no automatic main-medium interpretation is valid. For local MoO, also restore the exact source name MoO3 without inventing an ontology ID."
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Stock 7: MoO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.71",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.71",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 7 component",
        "exact_source_quote": "MoO3  0.71 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 7",
        "exact_source_quote": "per litre",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 0.71,
      "unit": "g",
      "stock_number": 7,
      "stock_recipe_basis_ml": 1000,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "The local numeral is a stock-recipe amount presented at main-medium scope. Move it into the named stock and bind the receiving dose separately; no automatic main-medium interpretation is valid. For local MoO, also restore the exact source name MoO3 without inventing an ontology ID."
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Stock 7: CuSO4.5H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.57",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.57",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 7 component",
        "exact_source_quote": "CuSO4.5H2O  1.57 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 7",
        "exact_source_quote": "per litre",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 1.57,
      "unit": "g",
      "stock_number": 7,
      "stock_recipe_basis_ml": 1000,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "The local numeral is a stock-recipe amount presented at main-medium scope. Move it into the named stock and bind the receiving dose separately; no automatic main-medium interpretation is valid. For local MoO, also restore the exact source name MoO3 without inventing an ontology ID."
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Stock 7: Co(NO3)2.6H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.49",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.49",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 7 component",
        "exact_source_quote": "Co(NO3)2.6H2O  0.49 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 7",
        "exact_source_quote": "per litre",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 0.49,
      "unit": "g",
      "stock_number": 7,
      "stock_recipe_basis_ml": 1000,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "The local numeral is a stock-recipe amount presented at main-medium scope. Move it into the named stock and bind the receiving dose separately; no automatic main-medium interpretation is valid. For local MoO, also restore the exact source name MoO3 without inventing an ontology ID."
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Stock 8: H3BO3",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 8 component",
        "exact_source_quote": "H3BO3  11.42 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 8",
        "exact_source_quote": "per litre",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 11.42,
      "unit": "g",
      "stock_number": 8,
      "stock_recipe_basis_ml": 1000,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "This source component is missing; add it only within its numbered stock and preserve its recipe basis."
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Stock 9: EDTA",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 9 component",
        "exact_source_quote": "EDTA  50.0 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 9",
        "exact_source_quote": "per litre",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 50.0,
      "unit": "g",
      "stock_number": 9,
      "stock_recipe_basis_ml": 1000,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "This source component is missing; add it only within its numbered stock and preserve its recipe basis."
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Stock 9: KOH",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "31.0",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "31.0",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 9 component",
        "exact_source_quote": "KOH  31.0 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 9",
        "exact_source_quote": "per litre",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 31.0,
      "unit": "g",
      "stock_number": 9,
      "stock_recipe_basis_ml": 1000,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "The local numeral is a stock-recipe amount presented at main-medium scope. Move it into the named stock and bind the receiving dose separately; no automatic main-medium interpretation is valid. For local MoO, also restore the exact source name MoO3 without inventing an ontology ID."
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Stock 10: FeSO4.7H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 10 component",
        "exact_source_quote": "FeSO4.7H2O  4.98 g",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 10",
        "exact_source_quote": "per litre",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 4.98,
      "unit": "g",
      "stock_number": 10,
      "stock_recipe_basis_ml": 1000,
      "stage": "stock preparation",
      "concentrated_acid_strength": "not applicable"
    },
    "rationale": "This source component is missing; add it only within its numbered stock and preserve its recipe basis."
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Stock 10: H2SO4 (conc)",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Numbered stock 10 component",
        "exact_source_quote": "H2SO4 (conc)  1.0 ml",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      },
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Basis heading governing stock 10",
        "exact_source_quote": "per litre",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 1.0,
      "unit": "ml",
      "stock_number": 10,
      "stock_recipe_basis_ml": 1000,
      "stage": "stock preparation",
      "concentrated_acid_strength": null
    },
    "rationale": "This source component is missing; add it only within its numbered stock and preserve its recipe basis."
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Receiving dose of stock 1",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Medium per litre; EACH numbered stock",
        "exact_source_quote": "Stock solutions 1 ­ 6  10.0 ml each",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "stock_number": 1,
      "dose": 10,
      "unit": "ml",
      "receiving_final_volume": 1,
      "receiving_volume_unit": "L"
    },
    "rationale": "Each numbered stock is dosed individually. The first six contribute 60 ml and the final four 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total for the group."
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Receiving dose of stock 2",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Medium per litre; EACH numbered stock",
        "exact_source_quote": "Stock solutions 1 ­ 6  10.0 ml each",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "stock_number": 2,
      "dose": 10,
      "unit": "ml",
      "receiving_final_volume": 1,
      "receiving_volume_unit": "L"
    },
    "rationale": "Each numbered stock is dosed individually. The first six contribute 60 ml and the final four 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total for the group."
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Receiving dose of stock 3",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Medium per litre; EACH numbered stock",
        "exact_source_quote": "Stock solutions 1 ­ 6  10.0 ml each",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "stock_number": 3,
      "dose": 10,
      "unit": "ml",
      "receiving_final_volume": 1,
      "receiving_volume_unit": "L"
    },
    "rationale": "Each numbered stock is dosed individually. The first six contribute 60 ml and the final four 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total for the group."
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Receiving dose of stock 4",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Medium per litre; EACH numbered stock",
        "exact_source_quote": "Stock solutions 1 ­ 6  10.0 ml each",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "stock_number": 4,
      "dose": 10,
      "unit": "ml",
      "receiving_final_volume": 1,
      "receiving_volume_unit": "L"
    },
    "rationale": "Each numbered stock is dosed individually. The first six contribute 60 ml and the final four 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total for the group."
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Receiving dose of stock 5",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Medium per litre; EACH numbered stock",
        "exact_source_quote": "Stock solutions 1 ­ 6  10.0 ml each",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "stock_number": 5,
      "dose": 10,
      "unit": "ml",
      "receiving_final_volume": 1,
      "receiving_volume_unit": "L"
    },
    "rationale": "Each numbered stock is dosed individually. The first six contribute 60 ml and the final four 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total for the group."
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Receiving dose of stock 6",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Medium per litre; EACH numbered stock",
        "exact_source_quote": "Stock solutions 1 ­ 6  10.0 ml each",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "stock_number": 6,
      "dose": 10,
      "unit": "ml",
      "receiving_final_volume": 1,
      "receiving_volume_unit": "L"
    },
    "rationale": "Each numbered stock is dosed individually. The first six contribute 60 ml and the final four 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total for the group."
  },
  {
    "quantity_id": "q23",
    "component_or_context": "Receiving dose of stock 7",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Medium per litre; EACH numbered stock",
        "exact_source_quote": "Stock solutions 7 ­ 10  1.0 ml each",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "stock_number": 7,
      "dose": 1,
      "unit": "ml",
      "receiving_final_volume": 1,
      "receiving_volume_unit": "L"
    },
    "rationale": "Each numbered stock is dosed individually. The first six contribute 60 ml and the final four 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total for the group."
  },
  {
    "quantity_id": "q24",
    "component_or_context": "Receiving dose of stock 8",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Medium per litre; EACH numbered stock",
        "exact_source_quote": "Stock solutions 7 ­ 10  1.0 ml each",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "stock_number": 8,
      "dose": 1,
      "unit": "ml",
      "receiving_final_volume": 1,
      "receiving_volume_unit": "L"
    },
    "rationale": "Each numbered stock is dosed individually. The first six contribute 60 ml and the final four 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total for the group."
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Receiving dose of stock 9",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Medium per litre; EACH numbered stock",
        "exact_source_quote": "Stock solutions 7 ­ 10  1.0 ml each",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "stock_number": 9,
      "dose": 1,
      "unit": "ml",
      "receiving_final_volume": 1,
      "receiving_volume_unit": "L"
    },
    "rationale": "Each numbered stock is dosed individually. The first six contribute 60 ml and the final four 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total for the group."
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Receiving dose of stock 10",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Medium per litre; EACH numbered stock",
        "exact_source_quote": "Stock solutions 7 ­ 10  1.0 ml each",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "stock_number": 10,
      "dose": 1,
      "unit": "ml",
      "receiving_final_volume": 1,
      "receiving_volume_unit": "L"
    },
    "rationale": "Each numbered stock is dosed individually. The first six contribute 60 ml and the final four 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total for the group."
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Receiving-medium water make-up",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Final medium paragraph",
        "exact_source_quote": "Make up to 1 litre with glass distilled or deionised water.",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "make_up_to": 1,
      "unit": "L",
      "water": "glass distilled or deionised",
      "stage": "after all ten stock additions"
    },
    "rationale": "The primary explicitly instructs make-up to 1 litre. Preserve that instruction rather than treating 1 litre as an additional water dose."
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Trace-stock autoclaving conditions",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Stock 7 trace element preparation",
        "exact_source_quote": "(autoclave to dissolve):",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "stage": "stock 7 autoclave to dissolve",
      "temperature_C": null,
      "duration_min": null
    },
    "rationale": "Add the exact stock-specific instruction; no numeric cycle or whole-medium sterilization default is supplied."
  },
  {
    "quantity_id": "q29",
    "component_or_context": "Generic temperature range",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "temperature_range",
        "stored": "15-30°C depending on species",
        "decision": "unsupported",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "temperature_range",
        "stored": "15-30°C depending on species",
        "decision": "unsupported",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Complete source page; no growth conditions",
        "exact_source_quote": "Bold's Basal Medium (BB) Freshwater algae \nStocks  per 400 ml (1) NaNO3  10.0 g (2) MgSO4.7H2O  3.0 g (3) NaCl  1.0 g (4) K2HPO4  3.0 g (5) KH2PO4  7.0 g (6) CaCl2.2H2O  1.0 g per litre (7) Trace elements solution (autoclave to dissolve): ZnSO4.7H2O  8.82 g MnCl2.4H2O  1.44 g MoO3  0.71 g CuSO4.5H2O  1.57 g Co(NO3)2.6H2O  0.49 g (8) H3BO3  11.42 g (9) EDTA  50.0 g KOH  31.0 g (10)FeSO4.7H2O  4.98 g H2SO4 (conc)  1.0 ml \nMedium  per litre Stock solutions 1 ­ 6  10.0 ml each Stock solutions 7 ­ 10  1.0 ml each Make up to 1 litre with glass distilled or deionised water. \nmedia recipes \nCCAP (Culture Collection of Algae and Protozoa), Dunstaffnage Marine Laboratory, Oban, Argyll, PA37 1QA, UK Tel: +44 (0)1631 559000  Fax: +44 (0)1631 559001  Email: ccap@sams.ac.uk  Web: www.ccap.ac.uk",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "local_assertion": "15–30 °C",
      "source_value": null,
      "stage": "cultivation conditions, unsupported by this recipe"
    },
    "rationale": "These numeric ranges are local generic guidance, not authenticated by the exact CCAP primary. Recover independent strain-specific evidence or qualify/remove the unsupported assertion; do not fabricate replacement values."
  },
  {
    "quantity_id": "q30",
    "component_or_context": "Generic light intensity",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "light_intensity",
        "stored": "Varies by species; typically 50-100 µmol photons m⁻² s⁻¹",
        "decision": "unsupported",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "light_intensity",
        "stored": "Varies by species; typically 50-100 µmol photons m⁻² s⁻¹",
        "decision": "unsupported",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Complete source page; no growth conditions",
        "exact_source_quote": "Bold's Basal Medium (BB) Freshwater algae \nStocks  per 400 ml (1) NaNO3  10.0 g (2) MgSO4.7H2O  3.0 g (3) NaCl  1.0 g (4) K2HPO4  3.0 g (5) KH2PO4  7.0 g (6) CaCl2.2H2O  1.0 g per litre (7) Trace elements solution (autoclave to dissolve): ZnSO4.7H2O  8.82 g MnCl2.4H2O  1.44 g MoO3  0.71 g CuSO4.5H2O  1.57 g Co(NO3)2.6H2O  0.49 g (8) H3BO3  11.42 g (9) EDTA  50.0 g KOH  31.0 g (10)FeSO4.7H2O  4.98 g H2SO4 (conc)  1.0 ml \nMedium  per litre Stock solutions 1 ­ 6  10.0 ml each Stock solutions 7 ­ 10  1.0 ml each Make up to 1 litre with glass distilled or deionised water. \nmedia recipes \nCCAP (Culture Collection of Algae and Protozoa), Dunstaffnage Marine Laboratory, Oban, Argyll, PA37 1QA, UK Tel: +44 (0)1631 559000  Fax: +44 (0)1631 559001  Email: ccap@sams.ac.uk  Web: www.ccap.ac.uk",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "local_assertion": "50–100 µmol photons m−2 s−1",
      "source_value": null,
      "stage": "cultivation conditions, unsupported by this recipe"
    },
    "rationale": "These numeric ranges are local generic guidance, not authenticated by the exact CCAP primary. Recover independent strain-specific evidence or qualify/remove the unsupported assertion; do not fabricate replacement values."
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Generic light/dark cycles",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BB.yaml",
        "field_path": "light_cycle",
        "stored": "Varies by species; commonly 12:12 or 16:8 light:dark",
        "decision": "unsupported",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/algae/bb.yaml",
        "field_path": "light_cycle",
        "stored": "Varies by species; commonly 12:12 or 16:8 light:dark",
        "decision": "unsupported",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "ccapBB",
        "source_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf",
        "source_locator": "Complete source page; no growth conditions",
        "exact_source_quote": "Bold's Basal Medium (BB) Freshwater algae \nStocks  per 400 ml (1) NaNO3  10.0 g (2) MgSO4.7H2O  3.0 g (3) NaCl  1.0 g (4) K2HPO4  3.0 g (5) KH2PO4  7.0 g (6) CaCl2.2H2O  1.0 g per litre (7) Trace elements solution (autoclave to dissolve): ZnSO4.7H2O  8.82 g MnCl2.4H2O  1.44 g MoO3  0.71 g CuSO4.5H2O  1.57 g Co(NO3)2.6H2O  0.49 g (8) H3BO3  11.42 g (9) EDTA  50.0 g KOH  31.0 g (10)FeSO4.7H2O  4.98 g H2SO4 (conc)  1.0 ml \nMedium  per litre Stock solutions 1 ­ 6  10.0 ml each Stock solutions 7 ­ 10  1.0 ml each Make up to 1 litre with glass distilled or deionised water. \nmedia recipes \nCCAP (Culture Collection of Algae and Protozoa), Dunstaffnage Marine Laboratory, Oban, Argyll, PA37 1QA, UK Tel: +44 (0)1631 559000  Fax: +44 (0)1631 559001  Email: ccap@sams.ac.uk  Web: www.ccap.ac.uk",
        "snapshot_sha256": "2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a",
        "parsed_text_sha256": "7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f",
        "accessed_at": "2026-10-21T22:14:59.189387Z"
      }
    ],
    "proposed_source_representation": {
      "local_assertion": "12:12 or 16:8 light:dark",
      "source_value": null,
      "stage": "cultivation conditions, unsupported by this recipe"
    },
    "rationale": "These numeric ranges are local generic guidance, not authenticated by the exact CCAP primary. Recover independent strain-specific evidence or qualify/remove the unsupported assertion; do not fabricate replacement values."
  }
]

## Findings

### f1: Six stock quantities replace the complete ten-stock medium

blocker / open / confirmed; issue key: culturemech.000053.incomplete-stock-recipe.

All local concentrations are stock amounts at receiving-medium scope; most source components, all ten doses and explicit make-up instruction are absent. This materially changes the recipe.

### f2: Unmapped MoO contradicts the source MoO3 formula

major / open / confirmed; issue key: culturemech.000053.moo-formula.

The retained amount 0.71 belongs to MoO3 in the trace stock. Local MoO is ungrounded; no existing chemical ID is being accused of mismatch.

### f3: Generic cultivation ranges lack exact-source support

major / open / confirmed; issue key: culturemech.000053.unsupported-growth-ranges.

Temperature 15–30 °C, light 50–100 µmol photons m−2 s−1 and photoperiod 12:12 or 16:8 are not supplied by the available primary and have no attached independent support.

### f4: A defined chemical formulation is labeled complex and undefined

major / open / confirmed; issue key: culturemech.000053.composition-classification.

The complete primary lists explicit chemical stocks without an undefined digest or biological mixture, while both layers are COMPLEX/UNDEFINED.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct all ten exact stocks, recipe bases, individual receiving doses and final make-up instruction in algae/bb.yaml with claim-level primary evidence, then regenerate under guarded ownership checks.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore the exact source formula in the correct stock and resolve its ontology grounding independently; preserve the already correct cobalt nitrate hexahydrate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Qualify or remove generic assertions unless independent applicable evidence is supplied. Keep recipe preparation distinct from organism cultivation conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Correct classification alongside full recipe reconstruction; retain the supported liquid physical state.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BB.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/algae/bb.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BB.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BB.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch040/393/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch040/393/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BB.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BB.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/algae/bb.yaml:1:id: CultureMech:000053<br>./data/merge_yaml/merged/BB.yaml:1:id: CultureMech:000053<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch040/source-preflight-bound/393/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 17 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf; Complete CCAP Bold’s Basal Medium page | supports | Exact BB source title, all ten stocks and receiving-medium preparation read. The separately named bacterial BB is excluded by stable ID and source identity. |
| stock-bases | https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf; Stocks heading and numbered stocks 1–10 | supports | Stocks 1–6 are per 400 ml; stocks 7–10 are per litre. These are stock recipe bases, not receiving-medium concentrations. |
| receiving | https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf; Medium per litre final paragraph | supports | Use 10 ml of each stock 1–6 and 1 ml of each stock 7–10, then make up to 1 litre. |
| makeup | https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf; Final medium preparation line | supports | The final receiving-medium make-up volume is explicit. |
| molybdenum-name | https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf; Trace stock7 MoO3 row | supports | The source formula is molybdenum trioxide; local MoO has no asserted identifier. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch040/393/grounding-inventory.json; Exact local term/history slots and bound source authentication ledger | context_only | Complete exact-field inventory; current metadata, historical evidence and source forms remain distinct. |
| history-inventory | /private/tmp/culturemech-review-work-batch040/393/history-inventory.json; Exact local term/history slots and bound source authentication ledger | context_only | Complete exact-field inventory; current metadata, historical evidence and source forms remain distinct. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi32035 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32035; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi86214 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86214; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact pinned current CHEBI preferred-key rows; metadata source commit/hash | context_only | {} |
| writer-0 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Both current target and maintained algae owner retain the same six incomplete root ingredients. Current guarded merging cannot reconstruct omitted source stocks; source curation belongs in the maintained algae owner. The historical cobalt-name repair is retained and does not imply that every stripped formula was corrected. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Both current target and maintained algae owner retain the same six incomplete root ingredients. Current guarded merging cannot reconstruct omitted source stocks; source curation belongs in the maintained algae owner. The historical cobalt-name repair is retained and does not imply that every stripped formula was corrected. |
| history-metadata | data/merge_yaml/merged/BB.yaml; data/normalized_yaml/algae/bb.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": [{"index": 2, "issue": "timezone absent", "value": "2026-02-03T11:26:43.470884"}, {"index": 5, "issue": "timezone absent", "value": "2026-04-04T12:54:54.842398"}]}, {"input": "data/normalized_yaml/algae/bb.yaml", "events": 10, "timestamp_issues": [{"index": 2, "issue": "timezone absent", "value": "2026-02-03T11:26:43.470884"}, {"index": 5, "issue": "timezone absent", "value": "2026-04-04T12:54:54.842398"}]}] |
| quantity-inventory | /private/tmp/culturemech-review-work-batch040/393/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T223702Z-culturemech-000053-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bb (CultureMech:000053)'
started_at: '2026-10-21T22:32:17Z'
finished_at: '2026-10-21T22:37:02Z'
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
summary: The algae BB record contains only six stock-level quantities from the complete
  CCAP Bold’s Basal formulation and presents them as main-medium rates. All ten stock
  stages and receiving doses need reconstruction. The source spells MoO3, whereas
  the local unmapped name is MoO. Generic temperature and lighting ranges are unsupported
  by this exact primary; the excluded bacterial BB record is not an owner.
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
  - path: data/merge_yaml/merged/BB.yaml
    sha256: 2931d9a8a4f3b17d3f74d1e2dce68e26fb7e9ece82f71e295ac3b1a958d44796
    role: target
  - path: data/normalized_yaml/algae/bb.yaml
    sha256: 746699aed1ad8d8078dd48d8d5fd4186ca99fc91cc9d2761ee01fe5ff598dc69
    role: context
  - path: data/normalized_yaml/bacterial/bb.yaml
    sha256: e0c2d5f6af2d3d7419343afddbe00db2ecf3bfe54b2f655531a3122e5935a70e
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/bb.yaml.md
    sha256: bd2be11438d37c691b3d73e3470721b2d1e503063ccd1c982af9588648392a3b
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6134_Bold_s_Basal_Medium_BB.yaml.md
    sha256: 3bc09df636861441d1b6d6934d4a6bd7a17f829ac91f347812db045c13e61536
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ABB.md
    sha256: 41fee02fefdecc458708d0575a94343990fb3f1605ac9a2705c250e4d966fd08
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BB.md
    sha256: 2d5b092408222fd21901d0599c5839b942836c4cdb50b932e7dfa543b4db36b2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/bb__9b6a7851.md
    sha256: 40281aef6e022aac5ca25d69c1282c543ced2c234cb6c7f88708e4b871a8b632
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/bsk_medium__d6555dbb.md
    sha256: bc9343fecdac39c4d3a89b2034d4ee3f28b073669b8013081458de323591dfe0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_cetonicum_medium__33e412bb.md
    sha256: a31fdbd78e2ccab69f98906dfd20aba678d0305736fcc8951781c6703521faff
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/modified_sour_dough_medium__38815cbb.md
    sha256: eb53420b9645556f8b3e72374f0e77210ac63295b3e4af8dcf3ed29e56c02e2e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/potato_dextrose_agar__04581fbb.md
    sha256: a02d94cfab60faf1f73842ab750aedaaa593dc865d2079da046eca29150eead1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrodictium_medium__705de4bb.md
    sha256: 5b7e058c7e89c46f0e1194d99d61fe58b56ad96554d90484dd8af3babe83dc93
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/bb.md
    sha256: c30521933c1f2c62a9f01ddb8e0617520508cf612b2d53844f5f52a830d84c26
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/bb.md
    sha256: 45e0771fe4095c732348ed6d30daf8466d00d1d8728a1cc78c1a61d88a5bb676
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6134_Bold_s_Basal_Medium_BB.md
    sha256: 32a0005913cf8adad76fc326ee6e3da91f7854ed47d8a5b5978e8302b7780c06
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/abb.md
    sha256: 580d0361989aed92df99fc5f4e8cba8ad449702ddc23240e7747581b14a2389d
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
  - path: scripts/migrate_data_quality_flags.py
    sha256: 592c531870ab22cbdeeed5fc8fc8d9d0b42d3a6a75c2c54acc3d0c77b566b693
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
  - path: scripts/repair_ccap_instruction_rows.py
    sha256: eb1a4c8c46eb45dcdde6a5d2f0f6833792dd0802c45603eefa1b63a3ff96fca5
    role: context
  - path: scripts/repair_ccap_sources_score10.py
    sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
    role: context
  - path: scripts/repair_subscript_stripped_names.py
    sha256: f8b53852e25ba74fad2c2865daa27784c17897a646ec2ee4a1edc5cb887df7ab
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
  selection: Task review 393; batch 040 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-nine task batches
    contain 390 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 393 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000053
targets:
- target_id: CultureMech:000053
  path: data/merge_yaml/merged/BB.yaml
  label: bb
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bb.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BB.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000053
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BB.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch040/393/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch040/393/strict.tsv"
  target_ids:
  - CultureMech:000053
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BB.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000053
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BB.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000053
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
  - CultureMech:000053
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BB.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T22:37:01Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/algae/bb.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:01Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BB.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:30.387425Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BB.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch040/393/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:31.388599Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch040/393/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BB.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:32.529927Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BB.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:33.316412Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T22:37:01Z'
  support: supports
  summary: './data/normalized_yaml/algae/bb.yaml:1:id: CultureMech:000053

    ./data/merge_yaml/merged/BB.yaml:1:id: CultureMech:000053

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/source-preflight-bound/393/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T22:37:01Z'
  support: supports
  summary: 17 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 054aa46966a9ce6a18d9b43726dbd3f9e1c58e75d5db1e7123fe74ed09d9f011
- evidence_id: primary
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf
  locator: Complete CCAP Bold’s Basal Medium page
  accessed_at: '2026-10-21T22:14:59.189387Z'
  support: supports
  summary: Exact BB source title, all ten stocks and receiving-medium preparation
    read. The separately named bacterial BB is excluded by stable ID and source identity.
  quote: Bold's Basal Medium (BB) Freshwater algae
  snapshot_sha256: 2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a
- evidence_id: stock-bases
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf
  locator: Stocks heading and numbered stocks 1–10
  accessed_at: '2026-10-21T22:14:59.189387Z'
  support: supports
  summary: Stocks 1–6 are per 400 ml; stocks 7–10 are per litre. These are stock recipe
    bases, not receiving-medium concentrations.
  quote: per 400 ml
  snapshot_sha256: 2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a
- evidence_id: receiving
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf
  locator: Medium per litre final paragraph
  accessed_at: '2026-10-21T22:14:59.189387Z'
  support: supports
  summary: Use 10 ml of each stock 1–6 and 1 ml of each stock 7–10, then make up to
    1 litre.
  quote: Stock solutions 1 ­ 6  10.0 ml each
  snapshot_sha256: 2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a
- evidence_id: makeup
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf
  locator: Final medium preparation line
  accessed_at: '2026-10-21T22:14:59.189387Z'
  support: supports
  summary: The final receiving-medium make-up volume is explicit.
  quote: Make up to 1 litre with glass distilled or deionised water.
  snapshot_sha256: 2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a
- evidence_id: molybdenum-name
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf
  locator: Trace stock7 MoO3 row
  accessed_at: '2026-10-21T22:14:59.189387Z'
  support: supports
  summary: The source formula is molybdenum trioxide; local MoO has no asserted identifier.
  quote: MoO3  0.71 g
  snapshot_sha256: 2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/393/grounding-inventory.json
  locator: Exact local term/history slots and bound source authentication ledger
  accessed_at: '2026-10-21T22:37:01Z'
  support: context_only
  summary: Complete exact-field inventory; current metadata, historical evidence and
    source forms remain distinct.
  snapshot_sha256: 38c80b7a5aad700d3c9202b1af34e02bc469dc00c0377abe3ded77203ddc8cf9
- evidence_id: history-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/393/history-inventory.json
  locator: Exact local term/history slots and bound source authentication ledger
  accessed_at: '2026-10-21T22:37:01Z'
  support: context_only
  summary: Complete exact-field inventory; current metadata, historical evidence and
    source forms remain distinct.
  snapshot_sha256: 4e55d5c3e4d0b970cfbfd270522fcafdfbc3d11fca195e69c36804c9c1a62927
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi32035
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32035
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T06:57:47.017507Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 6ed3df00965b4707265cfced80411c4b1937b727f8c2093addbc467f88ce2ec8
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi86214
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86214
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:30.123051Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 90cf3337643bc22bd3940bfbdee70a144b13af549ea12534184385f036b4633c
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact pinned current CHEBI preferred-key rows; metadata source commit/hash
  accessed_at: '2026-10-21T22:37:01Z'
  support: context_only
  summary: '{}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:01Z'
  support: context_only
  summary: Both current target and maintained algae owner retain the same six incomplete
    root ingredients. Current guarded merging cannot reconstruct omitted source stocks;
    source curation belongs in the maintained algae owner. The historical cobalt-name
    repair is retained and does not imply that every stripped formula was corrected.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:01Z'
  support: context_only
  summary: Both current target and maintained algae owner retain the same six incomplete
    root ingredients. Current guarded merging cannot reconstruct omitted source stocks;
    source curation belongs in the maintained algae owner. The historical cobalt-name
    repair is retained and does not imply that every stripped formula was corrected.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BB.yaml; data/normalized_yaml/algae/bb.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T22:37:01Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": [{"index": 2, "issue":
    "timezone absent", "value": "2026-02-03T11:26:43.470884"}, {"index": 5, "issue":
    "timezone absent", "value": "2026-04-04T12:54:54.842398"}]}, {"input": "data/normalized_yaml/algae/bb.yaml",
    "events": 10, "timestamp_issues": [{"index": 2, "issue": "timezone absent", "value":
    "2026-02-03T11:26:43.470884"}, {"index": 5, "issue": "timezone absent", "value":
    "2026-04-04T12:54:54.842398"}]}]'
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/393/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T22:37:01Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 7229c3a79861581b19021d37689ff7f430c282ae5c2f7d9b021217a0bc5f6de8
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000053
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact algae BB owner and excluded namesake
  outcome: supported
  summary: CultureMech:000053 is the algae BB owner and sole merge contributor, corresponding
    to the exact CCAP MR_BB primary. Bacterial bb.yaml CultureMech:000320 has another
    source identity and is not an owner or a recipe-completion shortcut. The source
    title is a broad freshwater-algae medium description, not strain-specific growth
    evidence.
  target_ids:
  - CultureMech:000053
  evidence_ids:
  - record
  - owner-0
  - id-search
  - primary
- assessment_id: grounding
  area: grounding
  topic: Asserted and missing chemical identities
  outcome: concern
  summary: All 10 asserted primary term instances across the two layers resolve with
    matching current labels. Target primary linkage is 5/6 (83.33%); no current or
    legacy secondary field is asserted (0/6 linkage, not a false missing-key lookup).
    MoO must be reconciled to the literal source MoO3, while the already corrected
    cobalt nitrate hexahydrate remains unchanged. No replacement identifier is invented.
  target_ids:
  - CultureMech:000053
  evidence_ids:
  - grounding-inventory
  - mim
  - molybdenum-name
  - primary
- assessment_id: recipe-completeness
  area: completeness
  topic: All stock constituents and receiving recipe
  outcome: concern
  summary: Only the five trace-stock components and KOH are retained. Stocks 1–6,
    boric acid, EDTA, iron/acid stock, stock bases and all receiving doses are absent.
    Six stock-level values at root scope cannot stand in for this complete ten-stock
    medium.
  target_ids:
  - CultureMech:000053
  evidence_ids:
  - record
  - owner-0
  - primary
  - stock-bases
  - receiving
  - makeup
  - quantity-inventory
- assessment_id: classification
  area: consistency
  topic: Composition and environmental assertions
  outcome: concern
  summary: The complete source lists specified chemical stocks and is a chemically
    defined formulation, contrary to COMPLEX/UNDEFINED. LIQUID is consistent. Exact
    primary supports no numeric temperature, light intensity or photoperiod; no taxon,
    strain or salt/oxygen requirement is inferred.
  target_ids:
  - CultureMech:000053
  evidence_ids:
  - record
  - owner-0
  - primary
  - quantity-inventory
- assessment_id: provenance
  area: provenance
  topic: Source hints versus attached evidence and current writer scope
  outcome: concern
  summary: Ingredient source strings and automated mapping metadata are not attached
    exact amount evidence. All recorded history and mapping timestamps are retained
    in the inventories; current source and stable owner identity permit a complete
    review. Preserve the prior cobalt repair while correcting independently demonstrated
    remaining issues.
  target_ids:
  - CultureMech:000053
  evidence_ids:
  - history-inventory
  - grounding-inventory
  - primary
  - writer-0
  - writer-1
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 20 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:000053
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 31 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:000053
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Stock 1: NaNO3\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null,\n        \"decision\": \"add\",\n\
    \        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n        \"\
    source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\",\n     \
    \   \"source_locator\": \"Numbered stock 1 component\",\n        \"exact_source_quote\"\
    : \"NaNO3  10.0 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 1\",\n        \"\
    exact_source_quote\": \"per 400 ml\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 10.0,\n      \"\
    unit\": \"g\",\n      \"stock_number\": 1,\n      \"stock_recipe_basis_ml\": 400,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"This source component is missing;\
    \ add it only within its numbered stock and preserve its recipe basis.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\": \"Stock 2: MgSO4.7H2O\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\": \"solutions\",\n\
    \        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n        \"\
    source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\",\n     \
    \   \"source_locator\": \"Numbered stock 2 component\",\n        \"exact_source_quote\"\
    : \"MgSO4.7H2O  3.0 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 2\",\n        \"\
    exact_source_quote\": \"per 400 ml\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 3.0,\n      \"unit\"\
    : \"g\",\n      \"stock_number\": 2,\n      \"stock_recipe_basis_ml\": 400,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"This source component is missing;\
    \ add it only within its numbered stock and preserve its recipe basis.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\": \"Stock 3: NaCl\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\": \"solutions\",\n\
    \        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n        \"\
    source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\",\n     \
    \   \"source_locator\": \"Numbered stock 3 component\",\n        \"exact_source_quote\"\
    : \"NaCl  1.0 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 3\",\n        \"\
    exact_source_quote\": \"per 400 ml\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 1.0,\n      \"unit\"\
    : \"g\",\n      \"stock_number\": 3,\n      \"stock_recipe_basis_ml\": 400,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"This source component is missing;\
    \ add it only within its numbered stock and preserve its recipe basis.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\": \"Stock 4: K2HPO4\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\": \"solutions\",\n\
    \        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n        \"\
    source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\",\n     \
    \   \"source_locator\": \"Numbered stock 4 component\",\n        \"exact_source_quote\"\
    : \"K2HPO4  3.0 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 4\",\n        \"\
    exact_source_quote\": \"per 400 ml\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 3.0,\n      \"unit\"\
    : \"g\",\n      \"stock_number\": 4,\n      \"stock_recipe_basis_ml\": 400,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"This source component is missing;\
    \ add it only within its numbered stock and preserve its recipe basis.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\": \"Stock 5: KH2PO4\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\": \"solutions\",\n\
    \        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n        \"\
    source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\",\n     \
    \   \"source_locator\": \"Numbered stock 5 component\",\n        \"exact_source_quote\"\
    : \"KH2PO4  7.0 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 5\",\n        \"\
    exact_source_quote\": \"per 400 ml\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 7.0,\n      \"unit\"\
    : \"g\",\n      \"stock_number\": 5,\n      \"stock_recipe_basis_ml\": 400,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"This source component is missing;\
    \ add it only within its numbered stock and preserve its recipe basis.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\": \"Stock 6: CaCl2.2H2O\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\": \"solutions\",\n\
    \        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n        \"\
    source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\",\n     \
    \   \"source_locator\": \"Numbered stock 6 component\",\n        \"exact_source_quote\"\
    : \"CaCl2.2H2O  1.0 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 6\",\n        \"\
    exact_source_quote\": \"per 400 ml\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 1.0,\n      \"unit\"\
    : \"g\",\n      \"stock_number\": 6,\n      \"stock_recipe_basis_ml\": 400,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"This source component is missing;\
    \ add it only within its numbered stock and preserve its recipe basis.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\": \"Stock 7: ZnSO4.7H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"8.82\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8.82\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\"\
    ,\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Numbered stock 7 component\",\n        \"exact_source_quote\"\
    : \"ZnSO4.7H2O  8.82 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 7\",\n        \"\
    exact_source_quote\": \"per litre\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 8.82,\n      \"\
    unit\": \"g\",\n      \"stock_number\": 7,\n      \"stock_recipe_basis_ml\": 1000,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"The local numeral is a stock-recipe\
    \ amount presented at main-medium scope. Move it into the named stock and bind\
    \ the receiving dose separately; no automatic main-medium interpretation is valid.\
    \ For local MoO, also restore the exact source name MoO3 without inventing an\
    \ ontology ID.\"\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Stock 7: MnCl2.4H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"1.44\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\",\n        \"\
    field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1.44\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n  \
    \      \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Numbered stock 7 component\",\n        \"exact_source_quote\"\
    : \"MnCl2.4H2O  1.44 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 7\",\n        \"\
    exact_source_quote\": \"per litre\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 1.44,\n      \"\
    unit\": \"g\",\n      \"stock_number\": 7,\n      \"stock_recipe_basis_ml\": 1000,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"The local numeral is a stock-recipe\
    \ amount presented at main-medium scope. Move it into the named stock and bind\
    \ the receiving dose separately; no automatic main-medium interpretation is valid.\
    \ For local MoO, also restore the exact source name MoO3 without inventing an\
    \ ontology ID.\"\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Stock 7: MoO3\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.71\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.71\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Numbered stock 7 component\",\n        \"exact_source_quote\"\
    : \"MoO3  0.71 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 7\",\n        \"\
    exact_source_quote\": \"per litre\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 0.71,\n      \"\
    unit\": \"g\",\n      \"stock_number\": 7,\n      \"stock_recipe_basis_ml\": 1000,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"The local numeral is a stock-recipe\
    \ amount presented at main-medium scope. Move it into the named stock and bind\
    \ the receiving dose separately; no automatic main-medium interpretation is valid.\
    \ For local MoO, also restore the exact source name MoO3 without inventing an\
    \ ontology ID.\"\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Stock 7: CuSO4.5H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"1.57\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\",\n        \"\
    field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1.57\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n  \
    \      \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Numbered stock 7 component\",\n        \"exact_source_quote\"\
    : \"CuSO4.5H2O  1.57 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 7\",\n        \"\
    exact_source_quote\": \"per litre\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 1.57,\n      \"\
    unit\": \"g\",\n      \"stock_number\": 7,\n      \"stock_recipe_basis_ml\": 1000,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"The local numeral is a stock-recipe\
    \ amount presented at main-medium scope. Move it into the named stock and bind\
    \ the receiving dose separately; no automatic main-medium interpretation is valid.\
    \ For local MoO, also restore the exact source name MoO3 without inventing an\
    \ ontology ID.\"\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Stock 7: Co(NO3)2.6H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.49\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\",\n        \"\
    field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.49\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n  \
    \      \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Numbered stock 7 component\",\n        \"exact_source_quote\"\
    : \"Co(NO3)2.6H2O  0.49 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 7\",\n        \"\
    exact_source_quote\": \"per litre\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 0.49,\n      \"\
    unit\": \"g\",\n      \"stock_number\": 7,\n      \"stock_recipe_basis_ml\": 1000,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"The local numeral is a stock-recipe\
    \ amount presented at main-medium scope. Move it into the named stock and bind\
    \ the receiving dose separately; no automatic main-medium interpretation is valid.\
    \ For local MoO, also restore the exact source name MoO3 without inventing an\
    \ ontology ID.\"\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"Stock 8: H3BO3\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null,\n        \"decision\": \"add\",\n\
    \        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n        \"\
    source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\",\n     \
    \   \"source_locator\": \"Numbered stock 8 component\",\n        \"exact_source_quote\"\
    : \"H3BO3  11.42 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 8\",\n        \"\
    exact_source_quote\": \"per litre\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 11.42,\n      \"\
    unit\": \"g\",\n      \"stock_number\": 8,\n      \"stock_recipe_basis_ml\": 1000,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"This source component is missing;\
    \ add it only within its numbered stock and preserve its recipe basis.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\": \"Stock 9:\
    \ EDTA\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\": \"\
    solutions\",\n        \"stored\": null,\n        \"decision\": \"add\",\n    \
    \    \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n        \"\
    source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\",\n     \
    \   \"source_locator\": \"Numbered stock 9 component\",\n        \"exact_source_quote\"\
    : \"EDTA  50.0 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 9\",\n        \"\
    exact_source_quote\": \"per litre\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 50.0,\n      \"\
    unit\": \"g\",\n      \"stock_number\": 9,\n      \"stock_recipe_basis_ml\": 1000,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"This source component is missing;\
    \ add it only within its numbered stock and preserve its recipe basis.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\": \"Stock 9:\
    \ KOH\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"31.0\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"31.0\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Numbered stock 9 component\",\n        \"exact_source_quote\"\
    : \"KOH  31.0 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 9\",\n        \"\
    exact_source_quote\": \"per litre\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 31.0,\n      \"\
    unit\": \"g\",\n      \"stock_number\": 9,\n      \"stock_recipe_basis_ml\": 1000,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"The local numeral is a stock-recipe\
    \ amount presented at main-medium scope. Move it into the named stock and bind\
    \ the receiving dose separately; no automatic main-medium interpretation is valid.\
    \ For local MoO, also restore the exact source name MoO3 without inventing an\
    \ ontology ID.\"\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"Stock 10: FeSO4.7H2O\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Numbered stock 10 component\",\n        \"exact_source_quote\"\
    : \"FeSO4.7H2O  4.98 g\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 10\",\n       \
    \ \"exact_source_quote\": \"per litre\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 4.98,\n      \"\
    unit\": \"g\",\n      \"stock_number\": 10,\n      \"stock_recipe_basis_ml\":\
    \ 1000,\n      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : \"not applicable\"\n    },\n    \"rationale\": \"This source component is missing;\
    \ add it only within its numbered stock and preserve its recipe basis.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\": \"Stock 10:\
    \ H2SO4 (conc)\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null,\n        \"decision\": \"add\",\n\
    \        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n        \"\
    source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\",\n     \
    \   \"source_locator\": \"Numbered stock 10 component\",\n        \"exact_source_quote\"\
    : \"H2SO4 (conc)  1.0 ml\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      },\n      {\n\
    \        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Basis heading governing stock 10\",\n       \
    \ \"exact_source_quote\": \"per litre\",\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 1.0,\n      \"unit\"\
    : \"ml\",\n      \"stock_number\": 10,\n      \"stock_recipe_basis_ml\": 1000,\n\
    \      \"stage\": \"stock preparation\",\n      \"concentrated_acid_strength\"\
    : null\n    },\n    \"rationale\": \"This source component is missing; add it\
    \ only within its numbered stock and preserve its recipe basis.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q17\",\n    \"component_or_context\": \"Receiving dose\
    \ of stock 1\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null,\n        \"decision\": \"add\",\n\
    \        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"ccapBB\",\n        \"\
    source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\",\n     \
    \   \"source_locator\": \"Medium per litre; EACH numbered stock\",\n        \"\
    exact_source_quote\": \"Stock solutions 1 ­ 6  10.0 ml each\",\n        \"snapshot_sha256\"\
    : \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\",\n    \
    \    \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_number\": 1,\n     \
    \ \"dose\": 10,\n      \"unit\": \"ml\",\n      \"receiving_final_volume\": 1,\n\
    \      \"receiving_volume_unit\": \"L\"\n    },\n    \"rationale\": \"Each numbered\
    \ stock is dosed individually. The first six contribute 60 ml and the final four\
    \ 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total\
    \ for the group.\"\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"Receiving dose of stock 2\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Medium per litre; EACH numbered stock\",\n  \
    \      \"exact_source_quote\": \"Stock solutions 1 ­ 6  10.0 ml each\",\n    \
    \    \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_number\": 2,\n     \
    \ \"dose\": 10,\n      \"unit\": \"ml\",\n      \"receiving_final_volume\": 1,\n\
    \      \"receiving_volume_unit\": \"L\"\n    },\n    \"rationale\": \"Each numbered\
    \ stock is dosed individually. The first six contribute 60 ml and the final four\
    \ 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total\
    \ for the group.\"\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"Receiving dose of stock 3\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Medium per litre; EACH numbered stock\",\n  \
    \      \"exact_source_quote\": \"Stock solutions 1 ­ 6  10.0 ml each\",\n    \
    \    \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_number\": 3,\n     \
    \ \"dose\": 10,\n      \"unit\": \"ml\",\n      \"receiving_final_volume\": 1,\n\
    \      \"receiving_volume_unit\": \"L\"\n    },\n    \"rationale\": \"Each numbered\
    \ stock is dosed individually. The first six contribute 60 ml and the final four\
    \ 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total\
    \ for the group.\"\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"Receiving dose of stock 4\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Medium per litre; EACH numbered stock\",\n  \
    \      \"exact_source_quote\": \"Stock solutions 1 ­ 6  10.0 ml each\",\n    \
    \    \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_number\": 4,\n     \
    \ \"dose\": 10,\n      \"unit\": \"ml\",\n      \"receiving_final_volume\": 1,\n\
    \      \"receiving_volume_unit\": \"L\"\n    },\n    \"rationale\": \"Each numbered\
    \ stock is dosed individually. The first six contribute 60 ml and the final four\
    \ 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total\
    \ for the group.\"\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"Receiving dose of stock 5\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Medium per litre; EACH numbered stock\",\n  \
    \      \"exact_source_quote\": \"Stock solutions 1 ­ 6  10.0 ml each\",\n    \
    \    \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_number\": 5,\n     \
    \ \"dose\": 10,\n      \"unit\": \"ml\",\n      \"receiving_final_volume\": 1,\n\
    \      \"receiving_volume_unit\": \"L\"\n    },\n    \"rationale\": \"Each numbered\
    \ stock is dosed individually. The first six contribute 60 ml and the final four\
    \ 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total\
    \ for the group.\"\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"Receiving dose of stock 6\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Medium per litre; EACH numbered stock\",\n  \
    \      \"exact_source_quote\": \"Stock solutions 1 ­ 6  10.0 ml each\",\n    \
    \    \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_number\": 6,\n     \
    \ \"dose\": 10,\n      \"unit\": \"ml\",\n      \"receiving_final_volume\": 1,\n\
    \      \"receiving_volume_unit\": \"L\"\n    },\n    \"rationale\": \"Each numbered\
    \ stock is dosed individually. The first six contribute 60 ml and the final four\
    \ 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total\
    \ for the group.\"\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"Receiving dose of stock 7\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Medium per litre; EACH numbered stock\",\n  \
    \      \"exact_source_quote\": \"Stock solutions 7 ­ 10  1.0 ml each\",\n    \
    \    \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_number\": 7,\n     \
    \ \"dose\": 1,\n      \"unit\": \"ml\",\n      \"receiving_final_volume\": 1,\n\
    \      \"receiving_volume_unit\": \"L\"\n    },\n    \"rationale\": \"Each numbered\
    \ stock is dosed individually. The first six contribute 60 ml and the final four\
    \ 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total\
    \ for the group.\"\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"Receiving dose of stock 8\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Medium per litre; EACH numbered stock\",\n  \
    \      \"exact_source_quote\": \"Stock solutions 7 ­ 10  1.0 ml each\",\n    \
    \    \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_number\": 8,\n     \
    \ \"dose\": 1,\n      \"unit\": \"ml\",\n      \"receiving_final_volume\": 1,\n\
    \      \"receiving_volume_unit\": \"L\"\n    },\n    \"rationale\": \"Each numbered\
    \ stock is dosed individually. The first six contribute 60 ml and the final four\
    \ 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total\
    \ for the group.\"\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"Receiving dose of stock 9\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Medium per litre; EACH numbered stock\",\n  \
    \      \"exact_source_quote\": \"Stock solutions 7 ­ 10  1.0 ml each\",\n    \
    \    \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_number\": 9,\n     \
    \ \"dose\": 1,\n      \"unit\": \"ml\",\n      \"receiving_final_volume\": 1,\n\
    \      \"receiving_volume_unit\": \"L\"\n    },\n    \"rationale\": \"Each numbered\
    \ stock is dosed individually. The first six contribute 60 ml and the final four\
    \ 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total\
    \ for the group.\"\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"Receiving dose of stock 10\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Medium per litre; EACH numbered stock\",\n  \
    \      \"exact_source_quote\": \"Stock solutions 7 ­ 10  1.0 ml each\",\n    \
    \    \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_number\": 10,\n    \
    \  \"dose\": 1,\n      \"unit\": \"ml\",\n      \"receiving_final_volume\": 1,\n\
    \      \"receiving_volume_unit\": \"L\"\n    },\n    \"rationale\": \"Each numbered\
    \ stock is dosed individually. The first six contribute 60 ml and the final four\
    \ 4 ml before water make-up; this arithmetic does not mean 10 ml or 1 ml total\
    \ for the group.\"\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"Receiving-medium water make-up\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n       \
    \ \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"ccapBB\",\n        \"source_url\": \"\
    https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\",\n        \"source_locator\"\
    : \"Final medium paragraph\",\n        \"exact_source_quote\": \"Make up to 1 litre with glass distilled or deionised water.\"\
    ,\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"make_up_to\": 1,\n      \"\
    unit\": \"L\",\n      \"water\": \"glass distilled or deionised\",\n      \"stage\"\
    : \"after all ten stock additions\"\n    },\n    \"rationale\": \"The primary\
    \ explicitly instructs make-up to 1 litre. Preserve that instruction rather than\
    \ treating 1 litre as an additional water dose.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q28\",\n    \"component_or_context\": \"Trace-stock autoclaving conditions\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null,\n        \"decision\": \"\
    add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Stock 7 trace element preparation\",\n      \
    \  \"exact_source_quote\": \"(autoclave to dissolve):\",\n        \"snapshot_sha256\"\
    : \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\",\n    \
    \    \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stage\": \"stock 7 autoclave\
    \ to dissolve\",\n      \"temperature_C\": null,\n      \"duration_min\": null\n\
    \    },\n    \"rationale\": \"Add the exact stock-specific instruction; no numeric\
    \ cycle or whole-medium sterilization default is supplied.\"\n  },\n  {\n    \"\
    quantity_id\": \"q29\",\n    \"component_or_context\": \"Generic temperature range\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\": \"\
    temperature_range\",\n        \"stored\": \"15-30°C depending on species\",\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\",\n       \
    \ \"field_path\": \"temperature_range\",\n        \"stored\": \"15-30°C depending\
    \ on species\",\n        \"decision\": \"unsupported\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Complete source page; no growth conditions\"\
    ,\n        \"exact_source_quote\": \"Bold's Basal Medium (BB) Freshwater algae \\\
    nStocks  per 400 ml (1) NaNO3  10.0 g (2) MgSO4.7H2O  3.0 g (3) NaCl  1.0 g (4) K2HPO4 \
    \ 3.0 g (5) KH2PO4  7.0 g (6) CaCl2.2H2O  1.0 g per litre (7) Trace elements solution (autoclave to dissolve): ZnSO4.7H2O \
    \ 8.82 g MnCl2.4H2O  1.44 g MoO3  0.71 g CuSO4.5H2O  1.57 g Co(NO3)2.6H2O  0.49 g (8) H3BO3 \
    \ 11.42 g (9) EDTA  50.0 g KOH  31.0 g (10)FeSO4.7H2O  4.98 g H2SO4 (conc)  1.0 ml \\\
    nMedium  per litre Stock solutions 1 ­ 6  10.0 ml each Stock solutions 7 ­ 10 \
    \ 1.0 ml each Make up to 1 litre with glass distilled or deionised water. \\nmedia recipes \\\
    nCCAP (Culture Collection of Algae and Protozoa), Dunstaffnage Marine Laboratory, Oban, Argyll, PA37 1QA, UK Tel: +44 (0)1631 559000  Fax: +44 (0)1631 559001  Email: ccap@sams.ac.uk  Web: www.ccap.ac.uk\"\
    ,\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"local_assertion\": \"15–30\
    \ °C\",\n      \"source_value\": null,\n      \"stage\": \"cultivation conditions,\
    \ unsupported by this recipe\"\n    },\n    \"rationale\": \"These numeric ranges\
    \ are local generic guidance, not authenticated by the exact CCAP primary. Recover\
    \ independent strain-specific evidence or qualify/remove the unsupported assertion;\
    \ do not fabricate replacement values.\"\n  },\n  {\n    \"quantity_id\": \"q30\"\
    ,\n    \"component_or_context\": \"Generic light intensity\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\"\
    ,\n        \"field_path\": \"light_intensity\",\n        \"stored\": \"Varies\
    \ by species; typically 50-100 µmol photons m⁻² s⁻¹\",\n        \"decision\":\
    \ \"unsupported\",\n        \"rationale\": \"\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/algae/bb.yaml\",\n        \"field_path\": \"light_intensity\"\
    ,\n        \"stored\": \"Varies by species; typically 50-100 µmol photons m⁻²\
    \ s⁻¹\",\n        \"decision\": \"unsupported\",\n        \"rationale\": \"\"\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Complete source page; no growth conditions\"\
    ,\n        \"exact_source_quote\": \"Bold's Basal Medium (BB) Freshwater algae \\\
    nStocks  per 400 ml (1) NaNO3  10.0 g (2) MgSO4.7H2O  3.0 g (3) NaCl  1.0 g (4) K2HPO4 \
    \ 3.0 g (5) KH2PO4  7.0 g (6) CaCl2.2H2O  1.0 g per litre (7) Trace elements solution (autoclave to dissolve): ZnSO4.7H2O \
    \ 8.82 g MnCl2.4H2O  1.44 g MoO3  0.71 g CuSO4.5H2O  1.57 g Co(NO3)2.6H2O  0.49 g (8) H3BO3 \
    \ 11.42 g (9) EDTA  50.0 g KOH  31.0 g (10)FeSO4.7H2O  4.98 g H2SO4 (conc)  1.0 ml \\\
    nMedium  per litre Stock solutions 1 ­ 6  10.0 ml each Stock solutions 7 ­ 10 \
    \ 1.0 ml each Make up to 1 litre with glass distilled or deionised water. \\nmedia recipes \\\
    nCCAP (Culture Collection of Algae and Protozoa), Dunstaffnage Marine Laboratory, Oban, Argyll, PA37 1QA, UK Tel: +44 (0)1631 559000  Fax: +44 (0)1631 559001  Email: ccap@sams.ac.uk  Web: www.ccap.ac.uk\"\
    ,\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"local_assertion\": \"50–100\
    \ µmol photons m−2 s−1\",\n      \"source_value\": null,\n      \"stage\": \"\
    cultivation conditions, unsupported by this recipe\"\n    },\n    \"rationale\"\
    : \"These numeric ranges are local generic guidance, not authenticated by the\
    \ exact CCAP primary. Recover independent strain-specific evidence or qualify/remove\
    \ the unsupported assertion; do not fabricate replacement values.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q31\",\n    \"component_or_context\": \"Generic light/dark\
    \ cycles\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/BB.yaml\",\n        \"field_path\"\
    : \"light_cycle\",\n        \"stored\": \"Varies by species; commonly 12:12 or\
    \ 16:8 light:dark\",\n        \"decision\": \"unsupported\",\n        \"rationale\"\
    : \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/algae/bb.yaml\"\
    ,\n        \"field_path\": \"light_cycle\",\n        \"stored\": \"Varies by species;\
    \ commonly 12:12 or 16:8 light:dark\",\n        \"decision\": \"unsupported\"\
    ,\n        \"rationale\": \"\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"ccapBB\",\n        \"source_url\": \"https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf\"\
    ,\n        \"source_locator\": \"Complete source page; no growth conditions\"\
    ,\n        \"exact_source_quote\": \"Bold's Basal Medium (BB) Freshwater algae \\\
    nStocks  per 400 ml (1) NaNO3  10.0 g (2) MgSO4.7H2O  3.0 g (3) NaCl  1.0 g (4) K2HPO4 \
    \ 3.0 g (5) KH2PO4  7.0 g (6) CaCl2.2H2O  1.0 g per litre (7) Trace elements solution (autoclave to dissolve): ZnSO4.7H2O \
    \ 8.82 g MnCl2.4H2O  1.44 g MoO3  0.71 g CuSO4.5H2O  1.57 g Co(NO3)2.6H2O  0.49 g (8) H3BO3 \
    \ 11.42 g (9) EDTA  50.0 g KOH  31.0 g (10)FeSO4.7H2O  4.98 g H2SO4 (conc)  1.0 ml \\\
    nMedium  per litre Stock solutions 1 ­ 6  10.0 ml each Stock solutions 7 ­ 10 \
    \ 1.0 ml each Make up to 1 litre with glass distilled or deionised water. \\nmedia recipes \\\
    nCCAP (Culture Collection of Algae and Protozoa), Dunstaffnage Marine Laboratory, Oban, Argyll, PA37 1QA, UK Tel: +44 (0)1631 559000  Fax: +44 (0)1631 559001  Email: ccap@sams.ac.uk  Web: www.ccap.ac.uk\"\
    ,\n        \"snapshot_sha256\": \"2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a\"\
    ,\n        \"parsed_text_sha256\": \"7273cde4b147f3df9d15868592b63cb58cf73bf0bb505811705a8f7ec087714f\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:14:59.189387Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"local_assertion\": \"12:12\
    \ or 16:8 light:dark\",\n      \"source_value\": null,\n      \"stage\": \"cultivation\
    \ conditions, unsupported by this recipe\"\n    },\n    \"rationale\": \"These\
    \ numeric ranges are local generic guidance, not authenticated by the exact CCAP\
    \ primary. Recover independent strain-specific evidence or qualify/remove the\
    \ unsupported assertion; do not fabricate replacement values.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.000053.incomplete-stock-recipe
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Six stock quantities replace the complete ten-stock medium
  description: All local concentrations are stock amounts at receiving-medium scope;
    most source components, all ten doses and explicit make-up instruction are absent.
    This materially changes the recipe.
  target_ids:
  - CultureMech:000053
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - primary
  - stock-bases
  - receiving
  - makeup
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bb.yaml
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
  issue_key: culturemech.000053.moo-formula
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: Unmapped MoO contradicts the source MoO3 formula
  description: The retained amount 0.71 belongs to MoO3 in the trace stock. Local
    MoO is ungrounded; no existing chemical ID is being accused of mismatch.
  target_ids:
  - CultureMech:000053
  field_paths:
  - ingredients[2].preferred_term
  evidence_ids:
  - record
  - owner-0
  - molybdenum-name
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bb.yaml
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
  issue_key: culturemech.000053.unsupported-growth-ranges
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Generic cultivation ranges lack exact-source support
  description: Temperature 15–30 °C, light 50–100 µmol photons m−2 s−1 and photoperiod
    12:12 or 16:8 are not supplied by the available primary and have no attached independent
    support.
  target_ids:
  - CultureMech:000053
  field_paths:
  - temperature_range
  - light_intensity
  - light_cycle
  evidence_ids:
  - record
  - owner-0
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bb.yaml
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
  issue_key: culturemech.000053.composition-classification
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: A defined chemical formulation is labeled complex and undefined
  description: The complete primary lists explicit chemical stocks without an undefined
    digest or biological mixture, while both layers are COMPLEX/UNDEFINED.
  target_ids:
  - CultureMech:000053
  field_paths:
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - owner-0
  - primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bb.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Reconstruct all ten exact stocks, recipe bases, individual receiving
    doses and final make-up instruction in algae/bb.yaml with claim-level primary
    evidence, then regenerate under guarded ownership checks.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000053
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bb.yaml
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
  description: Restore the exact source formula in the correct stock and resolve its
    ontology grounding independently; preserve the already correct cobalt nitrate
    hexahydrate.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000053
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bb.yaml
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
  description: Qualify or remove generic assertions unless independent applicable
    evidence is supplied. Keep recipe preparation distinct from organism cultivation
    conditions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000053
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bb.yaml
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
  description: Correct classification alongside full recipe reconstruction; retain
    the supported liquid physical state.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000053
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bb.yaml
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
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-040
- generated-medium
```
