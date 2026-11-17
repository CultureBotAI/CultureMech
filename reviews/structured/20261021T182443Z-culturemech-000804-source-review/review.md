# Source and formulation review: aurantimonas_medium (CultureMech:000804)

- Review: 20261021T182443Z-culturemech-000804-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T18:20:17Z
- Finished UTC: 2026-10-21T18:24:43Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 1346 supports the ingredient names, literal batch masses, pH 7 and retained autoclaving procedure. Both local layers already preserve preparation and optional 20 g/L agar. Water and claim-level evidence are absent; the five main G_PER_L values lack an established final-volume basis and the solid branch needs explicit qualification.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 325; batch 033 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-two task batches contain 320 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 323 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000804 | data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml | generated | aurantimonas_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000804 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000804 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-033/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch033/325/strict.tsv |
| validate-terms | passed | True | CultureMech:000804 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000804 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000804 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive1346api | unavailable | False | CultureMech:000804 | Optional current mediadive1346api attempt returned no usable recipe. The complete exact DSMZ primary supports the bounded assessment; no historical owner amount attachment requires authentication. |
| Exact source content access: mediadive1346api_retry | unavailable | False | CultureMech:000804 | Optional current mediadive1346api_retry attempt returned no usable recipe. The complete exact DSMZ primary supports the bounded assessment; no historical owner amount attachment requires authentication. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000804.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:000804.

11 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "ingredient_or_context": "Tryptone",
    "field_path": "ingredients[0].concentration",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_amount": 10,
    "source_unit": "g",
    "source_stage": "Main batch",
    "primary_source_evidence_id": "dsmz1346",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "dsmz1346",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf",
        "source_locator": "Mineral Salts Solution table",
        "exact_source_quote": "Tryptone 10.000 g",
        "snapshot_sha256": "661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b",
        "parsed_text_sha256": "128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
      }
    ],
    "arithmetic_and_scope": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
  },
  {
    "quantity_id": "q2",
    "ingredient_or_context": "Yeast extract",
    "field_path": "ingredients[1].concentration",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_amount": 5,
    "source_unit": "g",
    "source_stage": "Main batch",
    "primary_source_evidence_id": "dsmz1346",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "dsmz1346",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf",
        "source_locator": "Mineral Salts Solution table",
        "exact_source_quote": "Yeast Extract 5.000 g",
        "snapshot_sha256": "661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b",
        "parsed_text_sha256": "128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
      }
    ],
    "arithmetic_and_scope": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
  },
  {
    "quantity_id": "q3",
    "ingredient_or_context": "NaCl",
    "field_path": "ingredients[2].concentration",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_amount": 5,
    "source_unit": "g",
    "source_stage": "Main batch",
    "primary_source_evidence_id": "dsmz1346",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "dsmz1346",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf",
        "source_locator": "Mineral Salts Solution table",
        "exact_source_quote": "NaCl 5.000 g",
        "snapshot_sha256": "661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b",
        "parsed_text_sha256": "128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
      }
    ],
    "arithmetic_and_scope": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
  },
  {
    "quantity_id": "q4",
    "ingredient_or_context": "D-glucose",
    "field_path": "ingredients[3].concentration",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_amount": 1,
    "source_unit": "g",
    "source_stage": "Main batch",
    "primary_source_evidence_id": "dsmz1346",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "dsmz1346",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf",
        "source_locator": "Mineral Salts Solution table",
        "exact_source_quote": "D-Glucose 1.000 g",
        "snapshot_sha256": "661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b",
        "parsed_text_sha256": "128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
      }
    ],
    "arithmetic_and_scope": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
  },
  {
    "quantity_id": "q5",
    "ingredient_or_context": "Calcium chloride dihydrate",
    "field_path": "ingredients[4].concentration",
    "local": {
      "value": "0.345",
      "unit": "G_PER_L"
    },
    "source_amount": 0.345,
    "source_unit": "g",
    "source_stage": "Main batch",
    "primary_source_evidence_id": "dsmz1346",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "dsmz1346",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf",
        "source_locator": "Mineral Salts Solution table",
        "exact_source_quote": "CaCl2 x 2 H2O 0.345 g",
        "snapshot_sha256": "661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b",
        "parsed_text_sha256": "128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.345",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.345",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
      }
    ],
    "arithmetic_and_scope": "The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume basis not established by 1000 mL water alone. No numeric transcription error is asserted. Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation must be labeled as such rather than measured final volume."
  },
  {
    "quantity_id": "q6",
    "ingredient_or_context": "Optional agar",
    "field_path": "ingredients[5].concentration",
    "local": {
      "value": "20",
      "unit": "G_PER_L"
    },
    "source_amount": 20,
    "source_unit": "g/l",
    "source_stage": "Optional solid branch",
    "primary_source_evidence_id": "dsmz1346",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1346",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf",
        "source_locator": "Preparation final sentence",
        "exact_source_quote": "20.0 g/l agar.",
        "snapshot_sha256": "661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b",
        "parsed_text_sha256": "128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The concentration is explicit and the ingredient note retains the solid-medium condition. Attach this conditional source evidence; do not extend the amount to the liquid branch."
      },
      {
        "input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The concentration is explicit and the ingredient note retains the solid-medium condition. Attach this conditional source evidence; do not extend the amount to the liquid branch."
      }
    ],
    "arithmetic_and_scope": "The concentration is explicit and the ingredient note retains the solid-medium condition. Attach this conditional source evidence; do not extend the amount to the liquid branch."
  },
  {
    "quantity_id": "q7",
    "ingredient_or_context": "Water input",
    "field_path": "preparation_steps",
    "local": [
      {
        "step_number": 1,
        "action": "MIX",
        "description": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar."
      }
    ],
    "source_amount": 1000,
    "source_unit": "ml",
    "source_stage": "Main batch input",
    "primary_source_evidence_id": "dsmz1346",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "dsmz1346",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf",
        "source_locator": "Mineral Salts Solution table",
        "exact_source_quote": "Distilled Water 1000.000 ml",
        "snapshot_sha256": "661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b",
        "parsed_text_sha256": "128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar."
          }
        ],
        "decision": "add",
        "rationale": "Water is absent from the local preparation although the preparation container is present. Add the literal 1000 mL water input to the existing procedure; do not replace that procedure or declare it missing. Water is not a measured final-volume statement."
      },
      {
        "input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar."
          }
        ],
        "decision": "add",
        "rationale": "Water is absent from the local preparation although the preparation container is present. Add the literal 1000 mL water input to the existing procedure; do not replace that procedure or declare it missing. Water is not a measured final-volume statement."
      }
    ],
    "arithmetic_and_scope": "Water is absent from the local preparation although the preparation container is present. Add the literal 1000 mL water input to the existing procedure; do not replace that procedure or declare it missing. Water is not a measured final-volume statement."
  },
  {
    "quantity_id": "q8",
    "ingredient_or_context": "Main pH field",
    "field_path": "ph_value",
    "local": 7.0,
    "source_amount": 7,
    "source_unit": "pH",
    "source_stage": "Main preparation",
    "primary_source_evidence_id": "dsmz1346",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1346",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf",
        "source_locator": "Preparation opening",
        "exact_source_quote": "Adjust to pH 7.0",
        "snapshot_sha256": "661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b",
        "parsed_text_sha256": "128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only",
        "rationale": "The scalar pH value agrees in both layers but has no attached claim evidence. No incubation optimum is inferred."
      },
      {
        "input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only",
        "rationale": "The scalar pH value agrees in both layers but has no attached claim evidence. No incubation optimum is inferred."
      }
    ],
    "arithmetic_and_scope": "The scalar pH value agrees in both layers but has no attached claim evidence. No incubation optimum is inferred."
  },
  {
    "quantity_id": "q9",
    "ingredient_or_context": "Main pH in retained preparation",
    "field_path": "preparation_steps[0].description",
    "local": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar.",
    "source_amount": 7,
    "source_unit": "pH",
    "source_stage": "Main preparation",
    "primary_source_evidence_id": "dsmz1346",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1346",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf",
        "source_locator": "Preparation opening",
        "exact_source_quote": "Adjust to pH 7.0",
        "snapshot_sha256": "661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b",
        "parsed_text_sha256": "128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar.",
        "decision": "evidence_only",
        "rationale": "Both layers already preserve this text. Retain it and add exact source linkage; no preparation-restoration action is required."
      },
      {
        "input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar.",
        "decision": "evidence_only",
        "rationale": "Both layers already preserve this text. Retain it and add exact source linkage; no preparation-restoration action is required."
      }
    ],
    "arithmetic_and_scope": "Both layers already preserve this text. Retain it and add exact source linkage; no preparation-restoration action is required."
  },
  {
    "quantity_id": "q10",
    "ingredient_or_context": "Optional agar in retained preparation",
    "field_path": "preparation_steps[0].description",
    "local": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar.",
    "source_amount": 20,
    "source_unit": "g/l",
    "source_stage": "Optional solid branch",
    "primary_source_evidence_id": "dsmz1346",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1346",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf",
        "source_locator": "Preparation final sentence",
        "exact_source_quote": "20.0 g/l agar.",
        "snapshot_sha256": "661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b",
        "parsed_text_sha256": "128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar.",
        "decision": "evidence_only",
        "rationale": "Both layers already preserve the conditional agar sentence. The standalone physical_state still needs an explicit selected-branch interpretation."
      },
      {
        "input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar.",
        "decision": "evidence_only",
        "rationale": "Both layers already preserve the conditional agar sentence. The standalone physical_state still needs an explicit selected-branch interpretation."
      }
    ],
    "arithmetic_and_scope": "Both layers already preserve the conditional agar sentence. The standalone physical_state still needs an explicit selected-branch interpretation."
  },
  {
    "quantity_id": "q11",
    "ingredient_or_context": "Unresolved final-volume denominator",
    "field_path": "preparation_steps",
    "local": [
      {
        "step_number": 1,
        "action": "MIX",
        "description": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar."
      }
    ],
    "source_amount": null,
    "source_unit": "measured final volume not supplied",
    "source_stage": "Prepared main medium",
    "primary_source_evidence_id": "dsmz1346",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "dsmz1346",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf",
        "source_locator": "Mineral Salts Solution table",
        "exact_source_quote": "Distilled Water 1000.000 ml",
        "snapshot_sha256": "661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b",
        "parsed_text_sha256": "128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar."
          }
        ],
        "decision": "unsupported",
        "rationale": "The source gives 1000 mL input water, not a make-up-to-volume instruction or measured final litre. No solute-volume or agar-volume correction is guessed."
      },
      {
        "input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar."
          }
        ],
        "decision": "unsupported",
        "rationale": "The source gives 1000 mL input water, not a make-up-to-volume instruction or measured final litre. No solute-volume or agar-volume correction is guessed."
      }
    ],
    "arithmetic_and_scope": "The source gives 1000 mL input water, not a make-up-to-volume instruction or measured final litre. No solute-volume or agar-volume correction is guessed."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:000804.

4 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 4/6 primary and 4/6 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 6: primary 66.67%; secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:000804.

11 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact DSMZ accession and sole maintained owner

identity: supported. Targets: CultureMech:000804.

CultureMech:000804 is DSMZ 1346, with the exact collection title and URL. Its sole maintained owner shares the stable ID and complete scientific content; the generated record adds merge metadata. The source heading Mineral Salts Solution does not identify an additional recoverable stock or a different formulation.

### Batch masses, explicit conditional concentration and denominator limits

consistency: concern. Targets: CultureMech:000804.

All twelve target/owner ingredient concentration occurrences and every numeric preparation claim are covered. Five numbers match literal gram inputs but lack an established final G_PER_L basis; agar alone is explicitly expressed per litre for the optional solid branch. No current amount is marked verified because neither layer attaches supporting evidence.

### Preparation is retained in both layers

completeness: supported. Targets: CultureMech:000804.

Both layers explicitly retain adjustment to pH 7.0, autoclaving and optional 20.0 g/L agar. The frozen preparatory absence statement is not used as scientific evidence. The primary supplies no autoclave temperature or duration; omission of those unstated parameters is a source limitation, not a local transcription failure.

### Missing input water and source evidence

completeness: concern. Targets: CultureMech:000804.

The source 1000 mL water input is absent from the retained procedure. Ingredient-level evidence and a structured primary reference are also absent; a URL in notes is only a source lead. Preserve the existing preparation while adding the precise water and claim linkage.

### Exact named chemical forms and mixtures

grounding: supported. Targets: CultureMech:000804.

D-glucose is explicitly D-specific and calcium chloride explicitly the dihydrate, agreeing with CHEBI:17634 and CHEBI:86158. Sodium chloride and agar match their captured terms; tryptone and yeast extract remain complex materials without invented pure-compound IDs. Current CHEBI-based secondary keys resolve separately from historical legacy schemes; no legacy key is asserted here.

### Complex medium and optional solid branch

scope: concern. Targets: CultureMech:000804.

COMPLEX/UNDEFINED is supported by tryptone and yeast extract despite the primary heading Mineral Salts Solution. The agar note and preparation accurately state optional solidification; SOLID_AGAR alone does not document which branch was selected. No organism, strain, growth evidence, DOI/PMID, variant relationship, high_metal label or KG graph match is asserted. No species-level cultivation claim is inferred from the name.

### Owner curation and regenerated output

provenance: supported. Targets: CultureMech:000804.

Correct or qualify only the maintained DSMZ owner quantities and evidence after source resolution, then regenerate the derived record. Current import/merge/export code is context, not proof of the historical API response or an inferred final volume. All retained history events were read and their timestamps inspected; no history rewrite is proposed.

## Findings

### f1: Unqualified final concentrations lack a documented volume basis

major / open / confirmed; issue key: cm000804-quantity-basis-and-water.

The five main ingredient fields use G_PER_L although DSMZ 1346 supplies gram amounts and 1000 mL input water without measured final-volume or make-up wording. Their numeric masses agree, so no different gram amount is proposed. Water is omitted from the otherwise retained preparation and no quantity has attached source evidence.

### f2: The conditional agar formulation needs an explicit branch interpretation

minor / open / confirmed; issue key: cm000804-optional-solid-branch.

Both local layers correctly retain the optional 20 g/L agar note and preparation, but the unconditional SOLID_AGAR field does not itself document a selected source branch. The source also permits the unsolidified formulation.

## Recommended Actions And Acceptance Checks

### a1

Preserve the five literal batch masses, add input water to the existing preparation, and attach exact claim evidence. Establish or explicitly qualify the concentration denominator before endorsing G_PER_L; do not invent final volume. Regenerate only from the maintained owner.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain the conditional agar amount and existing preparation, and document that this record represents the selected solid branch or model the branch explicitly under the existing schema. Do not remove or rewrite supported preparation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/aurantimonas_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch033/325/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-033/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch033/325/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml:1:id: CultureMech:000804<br>./data/normalized_yaml/bacterial/aurantimonas_medium.yaml:1:id: CultureMech:000804<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch033/source-preflight-bound/325/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 9 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| dsmz1346 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf; Page 1 complete Mineral Salts Solution table and preparation paragraph; page image independently read | supports | The collection recipe includes complex nutrients despite the subsection heading. It specifies water input, pH, autoclaving and optional agar, but no measured final volume or numeric sterilization cycle. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch033/325/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml; data/normalized_yaml/bacterial/aurantimonas_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml", "events": 5, "timestamp_issues": []}] |
| preparation-context-correction | /private/tmp/culturemech-review-work-batch033/source-preflight-bound/325/evidence-context-original.json; source_context[1] checked against both complete local YAML preparation_steps[0] and exact primary | refutes | The preparatory context sentence claiming preparation absent is rejected. Both target and owner retain pH 7, autoclaving and optional 20 g/L agar. Only water and attached source evidence are missing; no numeric cycle is supplied by the primary. |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant functions read without execution: importer unit normalization and water omission do not establish final volume, merge compatibility preserves supported evidence only if supplied, and export does not validate recipe denominators. No historical import replay is claimed. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant functions read without execution: importer unit normalization and water omission do not establish final volume, merge compatibility preserves supported evidence only if supplied, and export does not validate recipe denominators. No historical import replay is claimed. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant functions read without execution: importer unit normalization and water omission do not establish final volume, merge compatibility preserves supported evidence only if supplied, and export does not validate recipe denominators. No historical import replay is claimed. |
| writer-3 | src/culturemech/export/kgx_export.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant functions read without execution: importer unit normalization and water omission do not establish final volume, merge compatibility preserves supported evidence only if supplied, and export does not validate recipe denominators. No historical import replay is claimed. |
| mediadive1346api-attempt | https://mediadive.dsmz.de/rest/medium/1346; Preserved exact public retrieval result | context_only | Optional current mediadive1346api attempt returned no usable recipe. The complete exact DSMZ primary supports the bounded assessment; no historical owner amount attachment requires authentication. |
| mediadive1346api_retry-attempt | https://mediadive.dsmz.de/rest/medium/1346; Preserved exact public retrieval result | context_only | Optional current mediadive1346api_retry attempt returned no usable recipe. The complete exact DSMZ primary supports the bounded assessment; no historical owner amount attachment requires authentication. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Optional current mediadive1346api attempt returned no usable recipe. The complete exact DSMZ primary supports the bounded assessment; no historical owner amount attachment requires authentication.
- Optional current mediadive1346api_retry attempt returned no usable recipe. The complete exact DSMZ primary supports the bounded assessment; no historical owner amount attachment requires authentication.
- The review is completed within its stated scope: no required check is unavailable. Current optional API failures remain recorded and do not invalidate the available exact primary.
- No measured final volume, numeric autoclave cycle, incubation conditions or growth result was supplied. These are retained as source limits, not filled from common practice.
- The frozen preparatory sentence claiming preparation absent was contradicted by the exact current target and owner; this correction is explicit and the frozen cache is unchanged.
- This scientific assessment preceded formal review validation and saving; their results are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T182443Z-culturemech-000804-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: aurantimonas_medium (CultureMech:000804)'
started_at: '2026-10-21T18:20:17Z'
finished_at: '2026-10-21T18:24:43Z'
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
summary: DSMZ 1346 supports the ingredient names, literal batch masses, pH 7 and retained
  autoclaving procedure. Both local layers already preserve preparation and optional
  20 g/L agar. Water and claim-level evidence are absent; the five main G_PER_L values
  lack an established final-volume basis and the solid branch needs explicit qualification.
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
  - path: data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml
    sha256: 52c7ef7d9118f39e4d114ed88285cbcf313fe406f5dea48356ca265225ebc869
    role: target
  - path: data/normalized_yaml/bacterial/aurantimonas_medium.yaml
    sha256: edb7cd1853243cccdf5e6ae487b9df8c803e01c9ae06e09147e3ac148e4a7b14
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/aurantimonas_medium.yaml.md
    sha256: d1c6aaadde8c3cac8c55026182610004d6b706622aedc7919891646fabd7a7a4
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
  selection: Task review 325; batch 033 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-two task batches
    contain 320 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 323 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000804
targets:
- target_id: CultureMech:000804
  path: data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml
  label: aurantimonas_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aurantimonas_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch033/325/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-033/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch033/325/strict.tsv"
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000804
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
  - CultureMech:000804
- check_id: mediadive1346api-source-access
  name: 'Exact source content access: mediadive1346api'
  required: false
  status: unavailable
  summary: Optional current mediadive1346api attempt returned no usable recipe. The
    complete exact DSMZ primary supports the bounded assessment; no historical owner
    amount attachment requires authentication.
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - mediadive1346api-attempt
- check_id: mediadive1346api_retry-source-access
  name: 'Exact source content access: mediadive1346api_retry'
  required: false
  status: unavailable
  summary: Optional current mediadive1346api_retry attempt returned no usable recipe.
    The complete exact DSMZ primary supports the bounded assessment; no historical
    owner amount attachment requires authentication.
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - mediadive1346api_retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T18:24:42Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/aurantimonas_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T18:24:42Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T18:20:50.921716Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch033/325/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T18:20:52.004228Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-033/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch033/325/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T18:20:53.177873Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T18:20:53.887651Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T18:24:42Z'
  support: supports
  summary: './data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml:1:id: CultureMech:000804

    ./data/normalized_yaml/bacterial/aurantimonas_medium.yaml:1:id: CultureMech:000804

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch033/source-preflight-bound/325/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T18:24:42Z'
  support: supports
  summary: 9 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 0000947f3421308b0b0ebed06a6ca7115fc3f1019766448c93d811e03d5ee9ce
- evidence_id: dsmz1346
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf
  locator: Page 1 complete Mineral Salts Solution table and preparation paragraph;
    page image independently read
  accessed_at: '2026-10-21T18:05:05.015875Z'
  support: supports
  summary: The collection recipe includes complex nutrients despite the subsection
    heading. It specifies water input, pH, autoclaving and optional agar, but no measured
    final volume or numeric sterilization cycle.
  quote: Adjust to pH 7.0 and sterilize by autoclaving.
  snapshot_sha256: 661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch033/325/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T18:24:42Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 0c88332158ff89e31e2623d4eda94f3db0784e7001ef95624ff01100e6b58c32
- evidence_id: chebi17634
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:33.425023Z'
  support: supports
  summary: CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
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
  accessed_at: '2026-10-21T18:24:42Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17634":
    [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634",
    "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:2509": [{"label": "Agar", "match_type":
    "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O",
    "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml; data/normalized_yaml/bacterial/aurantimonas_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T18:24:42Z'
  support: context_only
  summary: '[{"input": "target", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/aurantimonas_medium.yaml",
    "events": 5, "timestamp_issues": []}]'
- evidence_id: preparation-context-correction
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch033/source-preflight-bound/325/evidence-context-original.json
  locator: source_context[1] checked against both complete local YAML preparation_steps[0]
    and exact primary
  accessed_at: '2026-10-21T18:24:42Z'
  support: refutes
  summary: The preparatory context sentence claiming preparation absent is rejected.
    Both target and owner retain pH 7, autoclaving and optional 20 g/L agar. Only
    water and attached source evidence are missing; no numeric cycle is supplied by
    the primary.
  snapshot_sha256: 7859f86a967e481c4d8dfad89fdcdec32e3f17461e31317d36d31c90285f0b58
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:24:42Z'
  support: context_only
  summary: 'Current relevant functions read without execution: importer unit normalization
    and water omission do not establish final volume, merge compatibility preserves
    supported evidence only if supplied, and export does not validate recipe denominators.
    No historical import replay is claimed.'
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:24:42Z'
  support: context_only
  summary: 'Current relevant functions read without execution: importer unit normalization
    and water omission do not establish final volume, merge compatibility preserves
    supported evidence only if supplied, and export does not validate recipe denominators.
    No historical import replay is claimed.'
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:24:42Z'
  support: context_only
  summary: 'Current relevant functions read without execution: importer unit normalization
    and water omission do not establish final volume, merge compatibility preserves
    supported evidence only if supplied, and export does not validate recipe denominators.
    No historical import replay is claimed.'
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/export/kgx_export.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:24:42Z'
  support: context_only
  summary: 'Current relevant functions read without execution: importer unit normalization
    and water omission do not establish final volume, merge compatibility preserves
    supported evidence only if supplied, and export does not validate recipe denominators.
    No historical import replay is claimed.'
  snapshot_sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
- evidence_id: mediadive1346api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1346
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T18:05:03.270247Z'
  support: context_only
  summary: Optional current mediadive1346api attempt returned no usable recipe. The
    complete exact DSMZ primary supports the bounded assessment; no historical owner
    amount attachment requires authentication.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive1346api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1346
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T18:06:00.248664Z'
  support: context_only
  summary: Optional current mediadive1346api_retry attempt returned no usable recipe.
    The complete exact DSMZ primary supports the bounded assessment; no historical
    owner amount attachment requires authentication.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 11 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"ingredient_or_context\": \"\
    Tryptone\",\n    \"field_path\": \"ingredients[0].concentration\",\n    \"local\"\
    : {\n      \"value\": \"10\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : 10,\n    \"source_unit\": \"g\",\n    \"source_stage\": \"Main batch\",\n  \
    \  \"primary_source_evidence_id\": \"dsmz1346\",\n    \"decision\": \"unsupported\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1346\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf\"\
    ,\n        \"source_locator\": \"Mineral Salts Solution table\",\n        \"exact_source_quote\"\
    : \"Tryptone 10.000 g\",\n        \"snapshot_sha256\": \"661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b\"\
    ,\n        \"parsed_text_sha256\": \"128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[0].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"\
    The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume\
    \ basis not established by 1000 mL water alone. No numeric transcription error\
    \ is asserted. Preserve the literal gram amount and attach evidence; a nominal\
    \ one-litre interpretation must be labeled as such rather than measured final\
    \ volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aurantimonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The numeric\
    \ mass matches the primary batch amount, but G_PER_L requires a final-volume basis\
    \ not established by 1000 mL water alone. No numeric transcription error is asserted.\
    \ Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation\
    \ must be labeled as such rather than measured final volume.\"\n      }\n    ],\n\
    \    \"arithmetic_and_scope\": \"The numeric mass matches the primary batch amount,\
    \ but G_PER_L requires a final-volume basis not established by 1000 mL water alone.\
    \ No numeric transcription error is asserted. Preserve the literal gram amount\
    \ and attach evidence; a nominal one-litre interpretation must be labeled as such\
    \ rather than measured final volume.\"\n  },\n  {\n    \"quantity_id\": \"q2\"\
    ,\n    \"ingredient_or_context\": \"Yeast extract\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"5\",\n      \"unit\": \"G_PER_L\"\n  \
    \  },\n    \"source_amount\": 5,\n    \"source_unit\": \"g\",\n    \"source_stage\"\
    : \"Main batch\",\n    \"primary_source_evidence_id\": \"dsmz1346\",\n    \"decision\"\
    : \"unsupported\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1346\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf\"\
    ,\n        \"source_locator\": \"Mineral Salts Solution table\",\n        \"exact_source_quote\"\
    : \"Yeast Extract 5.000 g\",\n        \"snapshot_sha256\": \"661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b\"\
    ,\n        \"parsed_text_sha256\": \"128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[1].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"\
    The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume\
    \ basis not established by 1000 mL water alone. No numeric transcription error\
    \ is asserted. Preserve the literal gram amount and attach evidence; a nominal\
    \ one-litre interpretation must be labeled as such rather than measured final\
    \ volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aurantimonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The numeric\
    \ mass matches the primary batch amount, but G_PER_L requires a final-volume basis\
    \ not established by 1000 mL water alone. No numeric transcription error is asserted.\
    \ Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation\
    \ must be labeled as such rather than measured final volume.\"\n      }\n    ],\n\
    \    \"arithmetic_and_scope\": \"The numeric mass matches the primary batch amount,\
    \ but G_PER_L requires a final-volume basis not established by 1000 mL water alone.\
    \ No numeric transcription error is asserted. Preserve the literal gram amount\
    \ and attach evidence; a nominal one-litre interpretation must be labeled as such\
    \ rather than measured final volume.\"\n  },\n  {\n    \"quantity_id\": \"q3\"\
    ,\n    \"ingredient_or_context\": \"NaCl\",\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"5\",\n      \"unit\": \"G_PER_L\"\n  \
    \  },\n    \"source_amount\": 5,\n    \"source_unit\": \"g\",\n    \"source_stage\"\
    : \"Main batch\",\n    \"primary_source_evidence_id\": \"dsmz1346\",\n    \"decision\"\
    : \"unsupported\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1346\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf\"\
    ,\n        \"source_locator\": \"Mineral Salts Solution table\",\n        \"exact_source_quote\"\
    : \"NaCl 5.000 g\",\n        \"snapshot_sha256\": \"661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b\"\
    ,\n        \"parsed_text_sha256\": \"128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[2].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"\
    The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume\
    \ basis not established by 1000 mL water alone. No numeric transcription error\
    \ is asserted. Preserve the literal gram amount and attach evidence; a nominal\
    \ one-litre interpretation must be labeled as such rather than measured final\
    \ volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aurantimonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The numeric\
    \ mass matches the primary batch amount, but G_PER_L requires a final-volume basis\
    \ not established by 1000 mL water alone. No numeric transcription error is asserted.\
    \ Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation\
    \ must be labeled as such rather than measured final volume.\"\n      }\n    ],\n\
    \    \"arithmetic_and_scope\": \"The numeric mass matches the primary batch amount,\
    \ but G_PER_L requires a final-volume basis not established by 1000 mL water alone.\
    \ No numeric transcription error is asserted. Preserve the literal gram amount\
    \ and attach evidence; a nominal one-litre interpretation must be labeled as such\
    \ rather than measured final volume.\"\n  },\n  {\n    \"quantity_id\": \"q4\"\
    ,\n    \"ingredient_or_context\": \"D-glucose\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n  \
    \  },\n    \"source_amount\": 1,\n    \"source_unit\": \"g\",\n    \"source_stage\"\
    : \"Main batch\",\n    \"primary_source_evidence_id\": \"dsmz1346\",\n    \"decision\"\
    : \"unsupported\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1346\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf\"\
    ,\n        \"source_locator\": \"Mineral Salts Solution table\",\n        \"exact_source_quote\"\
    : \"D-Glucose 1.000 g\",\n        \"snapshot_sha256\": \"661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b\"\
    ,\n        \"parsed_text_sha256\": \"128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[3].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"\
    The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume\
    \ basis not established by 1000 mL water alone. No numeric transcription error\
    \ is asserted. Preserve the literal gram amount and attach evidence; a nominal\
    \ one-litre interpretation must be labeled as such rather than measured final\
    \ volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aurantimonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The numeric\
    \ mass matches the primary batch amount, but G_PER_L requires a final-volume basis\
    \ not established by 1000 mL water alone. No numeric transcription error is asserted.\
    \ Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation\
    \ must be labeled as such rather than measured final volume.\"\n      }\n    ],\n\
    \    \"arithmetic_and_scope\": \"The numeric mass matches the primary batch amount,\
    \ but G_PER_L requires a final-volume basis not established by 1000 mL water alone.\
    \ No numeric transcription error is asserted. Preserve the literal gram amount\
    \ and attach evidence; a nominal one-litre interpretation must be labeled as such\
    \ rather than measured final volume.\"\n  },\n  {\n    \"quantity_id\": \"q5\"\
    ,\n    \"ingredient_or_context\": \"Calcium chloride dihydrate\",\n    \"field_path\"\
    : \"ingredients[4].concentration\",\n    \"local\": {\n      \"value\": \"0.345\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 0.345,\n    \"\
    source_unit\": \"g\",\n    \"source_stage\": \"Main batch\",\n    \"primary_source_evidence_id\"\
    : \"dsmz1346\",\n    \"decision\": \"unsupported\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz1346\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf\",\n       \
    \ \"source_locator\": \"Mineral Salts Solution table\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O 0.345 g\",\n        \"snapshot_sha256\": \"661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b\"\
    ,\n        \"parsed_text_sha256\": \"128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[4].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"0.345\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"\
    The numeric mass matches the primary batch amount, but G_PER_L requires a final-volume\
    \ basis not established by 1000 mL water alone. No numeric transcription error\
    \ is asserted. Preserve the literal gram amount and attach evidence; a nominal\
    \ one-litre interpretation must be labeled as such rather than measured final\
    \ volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aurantimonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.345\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"The numeric\
    \ mass matches the primary batch amount, but G_PER_L requires a final-volume basis\
    \ not established by 1000 mL water alone. No numeric transcription error is asserted.\
    \ Preserve the literal gram amount and attach evidence; a nominal one-litre interpretation\
    \ must be labeled as such rather than measured final volume.\"\n      }\n    ],\n\
    \    \"arithmetic_and_scope\": \"The numeric mass matches the primary batch amount,\
    \ but G_PER_L requires a final-volume basis not established by 1000 mL water alone.\
    \ No numeric transcription error is asserted. Preserve the literal gram amount\
    \ and attach evidence; a nominal one-litre interpretation must be labeled as such\
    \ rather than measured final volume.\"\n  },\n  {\n    \"quantity_id\": \"q6\"\
    ,\n    \"ingredient_or_context\": \"Optional agar\",\n    \"field_path\": \"ingredients[5].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"20\",\n      \"unit\": \"G_PER_L\"\n \
    \   },\n    \"source_amount\": 20,\n    \"source_unit\": \"g/l\",\n    \"source_stage\"\
    : \"Optional solid branch\",\n    \"primary_source_evidence_id\": \"dsmz1346\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1346\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf\"\
    ,\n        \"source_locator\": \"Preparation final sentence\",\n        \"exact_source_quote\"\
    : \"20.0 g/l agar.\",\n        \"snapshot_sha256\": \"661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b\"\
    ,\n        \"parsed_text_sha256\": \"128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[5].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The concentration is explicit and the ingredient note retains the solid-medium\
    \ condition. Attach this conditional source evidence; do not extend the amount\
    \ to the liquid branch.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aurantimonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The concentration\
    \ is explicit and the ingredient note retains the solid-medium condition. Attach\
    \ this conditional source evidence; do not extend the amount to the liquid branch.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"The concentration is explicit\
    \ and the ingredient note retains the solid-medium condition. Attach this conditional\
    \ source evidence; do not extend the amount to the liquid branch.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q7\",\n    \"ingredient_or_context\": \"Water input\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"local\": [\n      {\n   \
    \     \"step_number\": 1,\n        \"action\": \"MIX\",\n        \"description\"\
    : \"Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified\
    \ by adding 20.0 g/l agar.\"\n      }\n    ],\n    \"source_amount\": 1000,\n\
    \    \"source_unit\": \"ml\",\n    \"source_stage\": \"Main batch input\",\n \
    \   \"primary_source_evidence_id\": \"dsmz1346\",\n    \"decision\": \"add\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1346\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf\"\
    ,\n        \"source_locator\": \"Mineral Salts Solution table\",\n        \"exact_source_quote\"\
    : \"Distilled Water 1000.000 ml\",\n        \"snapshot_sha256\": \"661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b\"\
    ,\n        \"parsed_text_sha256\": \"128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : [\n          {\n            \"step_number\": 1,\n            \"action\": \"\
    MIX\",\n            \"description\": \"Adjust to pH 7.0 and sterilize by autoclaving.\
    \ The medium may be solidified by adding 20.0 g/l agar.\"\n          }\n     \
    \   ],\n        \"decision\": \"add\",\n        \"rationale\": \"Water is absent\
    \ from the local preparation although the preparation container is present. Add\
    \ the literal 1000 mL water input to the existing procedure; do not replace that\
    \ procedure or declare it missing. Water is not a measured final-volume statement.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aurantimonas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"Adjust to pH 7.0 and sterilize by autoclaving.\
    \ The medium may be solidified by adding 20.0 g/l agar.\"\n          }\n     \
    \   ],\n        \"decision\": \"add\",\n        \"rationale\": \"Water is absent\
    \ from the local preparation although the preparation container is present. Add\
    \ the literal 1000 mL water input to the existing procedure; do not replace that\
    \ procedure or declare it missing. Water is not a measured final-volume statement.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Water is absent from the local\
    \ preparation although the preparation container is present. Add the literal 1000\
    \ mL water input to the existing procedure; do not replace that procedure or declare\
    \ it missing. Water is not a measured final-volume statement.\"\n  },\n  {\n \
    \   \"quantity_id\": \"q8\",\n    \"ingredient_or_context\": \"Main pH field\"\
    ,\n    \"field_path\": \"ph_value\",\n    \"local\": 7.0,\n    \"source_amount\"\
    : 7,\n    \"source_unit\": \"pH\",\n    \"source_stage\": \"Main preparation\"\
    ,\n    \"primary_source_evidence_id\": \"dsmz1346\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1346\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf\"\
    ,\n        \"source_locator\": \"Preparation opening\",\n        \"exact_source_quote\"\
    : \"Adjust to pH 7.0\",\n        \"snapshot_sha256\": \"661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b\"\
    ,\n        \"parsed_text_sha256\": \"128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n \
    \       \"decision\": \"evidence_only\",\n        \"rationale\": \"The scalar\
    \ pH value agrees in both layers but has no attached claim evidence. No incubation\
    \ optimum is inferred.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aurantimonas_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"The scalar pH value agrees\
    \ in both layers but has no attached claim evidence. No incubation optimum is\
    \ inferred.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"The scalar pH\
    \ value agrees in both layers but has no attached claim evidence. No incubation\
    \ optimum is inferred.\"\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"ingredient_or_context\"\
    : \"Main pH in retained preparation\",\n    \"field_path\": \"preparation_steps[0].description\"\
    ,\n    \"local\": \"Adjust to pH 7.0 and sterilize by autoclaving. The medium\
    \ may be solidified by adding 20.0 g/l agar.\",\n    \"source_amount\": 7,\n \
    \   \"source_unit\": \"pH\",\n    \"source_stage\": \"Main preparation\",\n  \
    \  \"primary_source_evidence_id\": \"dsmz1346\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1346\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf\"\
    ,\n        \"source_locator\": \"Preparation opening\",\n        \"exact_source_quote\"\
    : \"Adjust to pH 7.0\",\n        \"snapshot_sha256\": \"661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b\"\
    ,\n        \"parsed_text_sha256\": \"128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps[0].description\",\n   \
    \     \"stored\": \"Adjust to pH 7.0 and sterilize by autoclaving. The medium\
    \ may be solidified by adding 20.0 g/l agar.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Both layers already preserve this text. Retain it\
    \ and add exact source linkage; no preparation-restoration action is required.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aurantimonas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified\
    \ by adding 20.0 g/l agar.\",\n        \"decision\": \"evidence_only\",\n    \
    \    \"rationale\": \"Both layers already preserve this text. Retain it and add\
    \ exact source linkage; no preparation-restoration action is required.\"\n   \
    \   }\n    ],\n    \"arithmetic_and_scope\": \"Both layers already preserve this\
    \ text. Retain it and add exact source linkage; no preparation-restoration action\
    \ is required.\"\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"ingredient_or_context\"\
    : \"Optional agar in retained preparation\",\n    \"field_path\": \"preparation_steps[0].description\"\
    ,\n    \"local\": \"Adjust to pH 7.0 and sterilize by autoclaving. The medium\
    \ may be solidified by adding 20.0 g/l agar.\",\n    \"source_amount\": 20,\n\
    \    \"source_unit\": \"g/l\",\n    \"source_stage\": \"Optional solid branch\"\
    ,\n    \"primary_source_evidence_id\": \"dsmz1346\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1346\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf\"\
    ,\n        \"source_locator\": \"Preparation final sentence\",\n        \"exact_source_quote\"\
    : \"20.0 g/l agar.\",\n        \"snapshot_sha256\": \"661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b\"\
    ,\n        \"parsed_text_sha256\": \"128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps[0].description\",\n   \
    \     \"stored\": \"Adjust to pH 7.0 and sterilize by autoclaving. The medium\
    \ may be solidified by adding 20.0 g/l agar.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Both layers already preserve the conditional agar\
    \ sentence. The standalone physical_state still needs an explicit selected-branch\
    \ interpretation.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aurantimonas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified\
    \ by adding 20.0 g/l agar.\",\n        \"decision\": \"evidence_only\",\n    \
    \    \"rationale\": \"Both layers already preserve the conditional agar sentence.\
    \ The standalone physical_state still needs an explicit selected-branch interpretation.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Both layers already preserve\
    \ the conditional agar sentence. The standalone physical_state still needs an\
    \ explicit selected-branch interpretation.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q11\",\n    \"ingredient_or_context\": \"Unresolved final-volume denominator\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"local\": [\n      {\n   \
    \     \"step_number\": 1,\n        \"action\": \"MIX\",\n        \"description\"\
    : \"Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified\
    \ by adding 20.0 g/l agar.\"\n      }\n    ],\n    \"source_amount\": null,\n\
    \    \"source_unit\": \"measured final volume not supplied\",\n    \"source_stage\"\
    : \"Prepared main medium\",\n    \"primary_source_evidence_id\": \"dsmz1346\"\
    ,\n    \"decision\": \"unsupported\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz1346\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1346.pdf\"\
    ,\n        \"source_locator\": \"Mineral Salts Solution table\",\n        \"exact_source_quote\"\
    : \"Distilled Water 1000.000 ml\",\n        \"snapshot_sha256\": \"661b7d5d4a348fa71fccd78f110f0f56c3b2350129354003db0ef8421286b90b\"\
    ,\n        \"parsed_text_sha256\": \"128991e60290b8fa87ea80a3826e1032970370b48017c1e2836f8e8dc2a61cbb\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : [\n          {\n            \"step_number\": 1,\n            \"action\": \"\
    MIX\",\n            \"description\": \"Adjust to pH 7.0 and sterilize by autoclaving.\
    \ The medium may be solidified by adding 20.0 g/l agar.\"\n          }\n     \
    \   ],\n        \"decision\": \"unsupported\",\n        \"rationale\": \"The source\
    \ gives 1000 mL input water, not a make-up-to-volume instruction or measured final\
    \ litre. No solute-volume or agar-volume correction is guessed.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/aurantimonas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"Adjust to pH 7.0 and sterilize by autoclaving.\
    \ The medium may be solidified by adding 20.0 g/l agar.\"\n          }\n     \
    \   ],\n        \"decision\": \"unsupported\",\n        \"rationale\": \"The source\
    \ gives 1000 mL input water, not a make-up-to-volume instruction or measured final\
    \ litre. No solute-volume or agar-volume correction is guessed.\"\n      }\n \
    \   ],\n    \"arithmetic_and_scope\": \"The source gives 1000 mL input water,\
    \ not a make-up-to-volume instruction or measured final litre. No solute-volume\
    \ or agar-volume correction is guessed.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '4 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 4/6 primary
    and 4/6 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi17634
  - chebi2509
  - chebi26710
  - chebi86158
  details: 'Instance coverage on a 0–100 percent scale, denominator 6: primary 66.67%;
    secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 11 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact DSMZ accession and sole maintained owner
  outcome: supported
  summary: CultureMech:000804 is DSMZ 1346, with the exact collection title and URL.
    Its sole maintained owner shares the stable ID and complete scientific content;
    the generated record adds merge metadata. The source heading Mineral Salts Solution
    does not identify an additional recoverable stock or a different formulation.
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - record
  - dsmz1346
  - id-search
  - owner-0
- assessment_id: source-amounts
  area: consistency
  topic: Batch masses, explicit conditional concentration and denominator limits
  outcome: concern
  summary: All twelve target/owner ingredient concentration occurrences and every
    numeric preparation claim are covered. Five numbers match literal gram inputs
    but lack an established final G_PER_L basis; agar alone is explicitly expressed
    per litre for the optional solid branch. No current amount is marked verified
    because neither layer attaches supporting evidence.
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - record
  - dsmz1346
  - quantity-inventory
  - owner-0
- assessment_id: preparation
  area: completeness
  topic: Preparation is retained in both layers
  outcome: supported
  summary: Both layers explicitly retain adjustment to pH 7.0, autoclaving and optional
    20.0 g/L agar. The frozen preparatory absence statement is not used as scientific
    evidence. The primary supplies no autoclave temperature or duration; omission
    of those unstated parameters is a source limitation, not a local transcription
    failure.
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - record
  - dsmz1346
  - preparation-context-correction
  - owner-0
- assessment_id: water
  area: completeness
  topic: Missing input water and source evidence
  outcome: concern
  summary: The source 1000 mL water input is absent from the retained procedure. Ingredient-level
    evidence and a structured primary reference are also absent; a URL in notes is
    only a source lead. Preserve the existing preparation while adding the precise
    water and claim linkage.
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - dsmz1346
  - record
  - quantity-inventory
  - owner-0
- assessment_id: forms
  area: grounding
  topic: Exact named chemical forms and mixtures
  outcome: supported
  summary: D-glucose is explicitly D-specific and calcium chloride explicitly the
    dihydrate, agreeing with CHEBI:17634 and CHEBI:86158. Sodium chloride and agar
    match their captured terms; tryptone and yeast extract remain complex materials
    without invented pure-compound IDs. Current CHEBI-based secondary keys resolve
    separately from historical legacy schemes; no legacy key is asserted here.
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - dsmz1346
  - chebi17634
  - chebi86158
  - chebi26710
  - chebi2509
  - mim
- assessment_id: classification
  area: scope
  topic: Complex medium and optional solid branch
  outcome: concern
  summary: COMPLEX/UNDEFINED is supported by tryptone and yeast extract despite the
    primary heading Mineral Salts Solution. The agar note and preparation accurately
    state optional solidification; SOLID_AGAR alone does not document which branch
    was selected. No organism, strain, growth evidence, DOI/PMID, variant relationship,
    high_metal label or KG graph match is asserted. No species-level cultivation claim
    is inferred from the name.
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - record
  - dsmz1346
  - owner-0
- assessment_id: ownership
  area: provenance
  topic: Owner curation and regenerated output
  outcome: supported
  summary: Correct or qualify only the maintained DSMZ owner quantities and evidence
    after source resolution, then regenerate the derived record. Current import/merge/export
    code is context, not proof of the historical API response or an inferred final
    volume. All retained history events were read and their timestamps inspected;
    no history rewrite is proposed.
  target_ids:
  - CultureMech:000804
  evidence_ids:
  - writer-0
  - writer-1
  - writer-2
  - writer-3
  - history-metadata
  - owner-0
findings:
- finding_id: f1
  issue_key: cm000804-quantity-basis-and-water
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Unqualified final concentrations lack a documented volume basis
  description: The five main ingredient fields use G_PER_L although DSMZ 1346 supplies
    gram amounts and 1000 mL input water without measured final-volume or make-up
    wording. Their numeric masses agree, so no different gram amount is proposed.
    Water is omitted from the otherwise retained preparation and no quantity has attached
    source evidence.
  target_ids:
  - CultureMech:000804
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[2].concentration
  - ingredients[3].concentration
  - ingredients[4].concentration
  - preparation_steps
  - references
  evidence_ids:
  - record
  - dsmz1346
  - quantity-inventory
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aurantimonas_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2.3
  normalization_reason: P2.3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: cm000804-optional-solid-branch
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: The conditional agar formulation needs an explicit branch interpretation
  description: Both local layers correctly retain the optional 20 g/L agar note and
    preparation, but the unconditional SOLID_AGAR field does not itself document a
    selected source branch. The source also permits the unsolidified formulation.
  target_ids:
  - CultureMech:000804
  field_paths:
  - physical_state
  - ingredients[5]
  - preparation_steps[0].description
  evidence_ids:
  - record
  - dsmz1346
  - quantity-inventory
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aurantimonas_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.4
  native_severity: P2.4
  normalization_reason: Native P2.4 is normalized to minor because the correct optional
    qualifier is already retained in both the ingredient and preparation; the remaining
    issue is explicit branch documentation, not an incorrect agar amount.
actions:
- action_id: a1
  description: Preserve the five literal batch masses, add input water to the existing
    preparation, and attach exact claim evidence. Establish or explicitly qualify
    the concentration denominator before endorsing G_PER_L; do not invent final volume.
    Regenerate only from the maintained owner.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000804
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aurantimonas_medium.yaml
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
  description: Retain the conditional agar amount and existing preparation, and document
    that this record represents the selected solid branch or model the branch explicitly
    under the existing schema. Do not remove or rewrite supported preparation.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000804
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aurantimonas_medium.yaml
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
- Optional current mediadive1346api attempt returned no usable recipe. The complete
  exact DSMZ primary supports the bounded assessment; no historical owner amount attachment
  requires authentication.
- Optional current mediadive1346api_retry attempt returned no usable recipe. The complete
  exact DSMZ primary supports the bounded assessment; no historical owner amount attachment
  requires authentication.
- 'The review is completed within its stated scope: no required check is unavailable.
  Current optional API failures remain recorded and do not invalidate the available
  exact primary.'
- No measured final volume, numeric autoclave cycle, incubation conditions or growth
  result was supplied. These are retained as source limits, not filled from common
  practice.
- The frozen preparatory sentence claiming preparation absent was contradicted by
  the exact current target and owner; this correction is explicit and the frozen cache
  is unchanged.
- This scientific assessment preceded formal review validation and saving; their results
  are recorded separately.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-033
- generated-medium
```
