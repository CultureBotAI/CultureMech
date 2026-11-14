# Source and formulation review: astidious_anaerobe_agar (CultureMech:009091)

- Review: 20261021T201727Z-culturemech-009091-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T20:11:21Z
- Finished UTC: 2026-10-21T20:17:27Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSMZ1203/TOGO M2521 formulation is Fastidious Anaerobe Agar: 45.7 g product made up to 1 L before a later 5–10% sterile defibrinated horse-blood addition. The generated record is stale relative to the maintained owner and omits the blood, preparation and pH. The owner retains these claims but overtypes the unspecified blood percentage as volume/volume and needs claim-level evidence and water-makeup clarification.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 368; batch 037 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-six task batches contain 360 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 363 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009091 | data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml | generated | astidious_anaerobe_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009091 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009091 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch037/368/strict.tsv |
| validate-terms | passed | True | CultureMech:009091 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009091 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009091 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive1203api | unavailable | False | CultureMech:009091 | The preserved mediadive1203api response is HTTP 503. The exact DSMZ1203 PDF and original TOGO M2521 API are available and independently support this bounded formulation assessment. |
| Exact source content access: mediadive1203api_retry | unavailable | False | CultureMech:009091 | The preserved mediadive1203api_retry response is HTTP 503. The exact DSMZ1203 PDF and original TOGO M2521 API are available and independently support this bounded formulation assessment. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009091.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009091.

10 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "ingredient_or_context": "Base water makeup",
    "field_path": "ingredients[0].concentration",
    "local": {
      "value": "1000",
      "unit": "G_PER_L"
    },
    "source_amount": 1000,
    "source_unit": "mL makeup",
    "source_stage": "Base before blood",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "dsmz1203",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf",
        "source_locator": "PDF page 1, water-makeup row",
        "exact_source_quote": "add deionized water to 1000.0 ml",
        "snapshot_sha256": "782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89",
        "parsed_text_sha256": "993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b"
      },
      {
        "source_key": "togoM2521original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"add deionized water to\",\n          \"volume\": 1000,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "1000 G_PER_L is a mass-concentration error; restore makeup to 1 L before blood."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "1.0 L is numerically appropriate as the pre-blood base makeup marker, not a measured water dose or final blood-containing volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "TOGO M2521 lists 1000 ml deionized water.",
        "decision": "correct",
        "rationale": "Clarify add water to 1000 mL rather than an independently measured 1000 mL water addition."
      }
    ],
    "arithmetic_and_scope": "1000 mL = 1 L by unit conversion. Preserve the to wording and pre-blood stage; no water density or final-medium concentration is inferred."
  },
  {
    "quantity_id": "q2",
    "ingredient_or_context": "Acumedia agar base",
    "field_path": "ingredients[1].concentration",
    "local": {
      "value": "45.7",
      "unit": "G_PER_L"
    },
    "source_amount": 45.7,
    "source_unit": "g per 1 L base",
    "source_stage": "Before blood",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1203",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf",
        "source_locator": "PDF page 1, product row",
        "exact_source_quote": "Fastidious Anaerobe Agar (acumedia) 45.7 g",
        "snapshot_sha256": "782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89",
        "parsed_text_sha256": "993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b"
      },
      {
        "source_key": "dsmz1203",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf",
        "source_locator": "PDF page 1, water-makeup row",
        "exact_source_quote": "add deionized water to 1000.0 ml",
        "snapshot_sha256": "782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89",
        "parsed_text_sha256": "993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b"
      },
      {
        "source_key": "togoM2521original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Fastidious Anaerobe Agar (acumedia)\",\n          \"volume\": 45.7,\n          \"unit\": \"g\"",
        "snapshot_sha256": "2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "45.7",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "45.7 G_PER_L is supported for the base explicitly made up to 1 L; it has no attached concentration evidence and does not establish the final post-blood concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "45.7",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "45.7 G_PER_L is supported for the base explicitly made up to 1 L; it has no attached concentration evidence and does not establish the final post-blood concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "TOGO M2521 lists 45.7 g Fastidious Anaerobe Agar (Acumedia) per liter.",
        "decision": "evidence_only",
        "rationale": "Retain the per-litre product amount explicitly at the pre-blood stage."
      }
    ],
    "arithmetic_and_scope": "The explicit base makeup supports 45.7 g / 1 L = 45.7 g/L before blood. Product composition is not decomposed or authenticated from a different manufacturer recipe."
  },
  {
    "quantity_id": "q3",
    "ingredient_or_context": "Sterile defibrinated horse blood",
    "field_path": "ingredients[2].concentration",
    "local": null,
    "source_amount": "5-10",
    "source_unit": "percent, basis unspecified",
    "source_stage": "Aseptic addition after cooling to 47°C",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "togoM2521original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "Cool to 47°C then aseptically add 5-10% of sterile defibrinated horse blood, mix well and pour plates.",
        "snapshot_sha256": "2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "The generated target lacks the required source blood addition; restore its literal range and qualifications."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5-10",
          "unit": "PERCENT_V_V"
        },
        "decision": "correct",
        "rationale": "The source does not support PERCENT_V_V. Preserve the 5–10% text with an explicit unresolved basis; do not select another percentage enum by inference."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "TOGO M2521 instructs adding 5-10% sterile defibrinated horse blood after autoclaving and cooling to 47 C.",
        "decision": "evidence_only",
        "rationale": "The note retains the literal unqualified range and addition stage; it is not claim-level evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": "Aseptically add 5-10% sterile defibrinated horse blood, mix well, and pour plates.",
        "decision": "evidence_only",
        "rationale": "The source supports this literal unqualified range, aseptic mixing and pouring plates."
      }
    ],
    "arithmetic_and_scope": "No conversion to mL, mass or a measured final concentration is justified. The native enum offers only basis-specific percentage units; use source-qualified notes/evidence until the basis is established rather than a false fixed enum."
  },
  {
    "quantity_id": "q4",
    "ingredient_or_context": "Base soaking duration",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": 10,
    "source_unit": "minutes",
    "source_stage": "Ordered base preparation before blood",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "togoM2521original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "Allow to soak for 10 minutes",
        "snapshot_sha256": "2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Restore the source-supported preparation already present in the maintained owner after resolving its blood basis."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "preparation_steps[0].duration",
        "stored": "10 minutes",
        "decision": "evidence_only",
        "rationale": "Exact source numerical preparation claim is retained correctly; attach scoped evidence, not a new growth assertion."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Allow the agar powder to soak for 10 min, then swirl to mix.",
        "decision": "evidence_only",
        "rationale": "The description is source-consistent and remains preparation-only."
      }
    ],
    "arithmetic_and_scope": "Preserve the ordered 10 min soak, 121°C/15 min autoclave and cooling to 47°C. The blood is added afterward; this cycle does not sterilize the already blood-supplemented plates."
  },
  {
    "quantity_id": "q5",
    "ingredient_or_context": "Base autoclave temperature",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": 121,
    "source_unit": "degrees Celsius",
    "source_stage": "Ordered base preparation before blood",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "togoM2521original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "sterilize by autoclaving at 121°C for 15 minutes.",
        "snapshot_sha256": "2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Restore the source-supported preparation already present in the maintained owner after resolving its blood basis."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Autoclave the mixed medium at 121 C for 15 min.",
        "decision": "evidence_only",
        "rationale": "Exact source numerical preparation claim is retained correctly; attach scoped evidence, not a new growth assertion."
      }
    ],
    "arithmetic_and_scope": "Preserve the ordered 10 min soak, 121°C/15 min autoclave and cooling to 47°C. The blood is added afterward; this cycle does not sterilize the already blood-supplemented plates."
  },
  {
    "quantity_id": "q6",
    "ingredient_or_context": "Base autoclave duration",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": 15,
    "source_unit": "minutes",
    "source_stage": "Ordered base preparation before blood",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "togoM2521original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "sterilize by autoclaving at 121°C for 15 minutes.",
        "snapshot_sha256": "2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Restore the source-supported preparation already present in the maintained owner after resolving its blood basis."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Autoclave the mixed medium at 121 C for 15 min.",
        "decision": "evidence_only",
        "rationale": "Exact source numerical preparation claim is retained correctly; attach scoped evidence, not a new growth assertion."
      }
    ],
    "arithmetic_and_scope": "Preserve the ordered 10 min soak, 121°C/15 min autoclave and cooling to 47°C. The blood is added afterward; this cycle does not sterilize the already blood-supplemented plates."
  },
  {
    "quantity_id": "q7",
    "ingredient_or_context": "Cooling temperature before blood",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": 47,
    "source_unit": "degrees Celsius",
    "source_stage": "Ordered base preparation before blood",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "togoM2521original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "Cool to 47°C then aseptically add",
        "snapshot_sha256": "2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Restore the source-supported preparation already present in the maintained owner after resolving its blood basis."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "preparation_steps[2].temperature",
        "stored": {
          "value": 47.0,
          "unit": "CELSIUS"
        },
        "decision": "evidence_only",
        "rationale": "Exact source numerical preparation claim is retained correctly; attach scoped evidence, not a new growth assertion."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "Cool the sterilized medium to 47 C.",
        "decision": "evidence_only",
        "rationale": "The description is source-consistent and remains preparation-only."
      }
    ],
    "arithmetic_and_scope": "Preserve the ordered 10 min soak, 121°C/15 min autoclave and cooling to 47°C. The blood is added afterward; this cycle does not sterilize the already blood-supplemented plates."
  },
  {
    "quantity_id": "q8",
    "ingredient_or_context": "Source pH range",
    "field_path": "ph_range",
    "local": null,
    "source_amount": {
      "central": 7.2,
      "tolerance": 0.2,
      "min": 7.0,
      "max": 7.4
    },
    "source_unit": "pH",
    "source_stage": "Source final preparation statement",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "dsmz1203",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf",
        "source_locator": "PDF page 1, final sentence",
        "exact_source_quote": "pH: 7.2 ± 0.2",
        "snapshot_sha256": "782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89",
        "parsed_text_sha256": "993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b"
      },
      {
        "source_key": "togoM2521original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521",
        "source_locator": "$.meta.ph",
        "exact_source_quote": "\"ph\": \"7.0 - 7.4\"",
        "snapshot_sha256": "2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_range",
        "stored": null,
        "decision": "add",
        "rationale": "Restore the exact source pH range retained in the owner."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.0,
          "max": 7.4
        },
        "decision": "evidence_only",
        "rationale": "7.2−0.2=7.0 and 7.2+0.2=7.4; the correct range lacks attached evidence."
      }
    ],
    "arithmetic_and_scope": "This arithmetic translates the stated tolerance only; it does not establish an adjustment reagent, incubation pH measurement or growth response."
  },
  {
    "quantity_id": "q9",
    "ingredient_or_context": "Measured final volume after blood",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": null,
    "source_unit": "not stated",
    "source_stage": "After blood addition",
    "decision": "not_quantified",
    "source_snippets": [
      {
        "source_key": "dsmz1203",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf",
        "source_locator": "PDF page 1, water-makeup row",
        "exact_source_quote": "add deionized water to 1000.0 ml",
        "snapshot_sha256": "782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89",
        "parsed_text_sha256": "993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b"
      },
      {
        "source_key": "togoM2521original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "Cool to 47°C then aseptically add 5-10% of sterile defibrinated horse blood, mix well and pour plates.",
        "snapshot_sha256": "2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "rationale": "Do not infer a final post-blood volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": "Aseptically add 5-10% sterile defibrinated horse blood, mix well, and pour plates.",
        "decision": "not_quantified",
        "rationale": "The existing description gives a percent range without a basis or measured final volume."
      }
    ],
    "arithmetic_and_scope": "The base is made up to 1000 mL before blood. Neither final volume nor an exact final product concentration is computed from the unqualified 5–10%."
  },
  {
    "quantity_id": "q10",
    "ingredient_or_context": "Owner numerical source summary",
    "field_path": "notes",
    "local": "TOGO M2521 lists the DSMZ Medium 1203 Fastidious Anaerobe Agar formulation: 45.7 g Acumedia Fastidious Anaerobe Agar brought to one liter with deionized water, soaked, autoclaved at 121 C, cooled to 47 C, and supplemented with 5-10% sterile defibrinated horse blood.",
    "source_amount": {
      "base_g": 45.7,
      "makeup_L": 1,
      "autoclave_C": 121,
      "cool_C": 47,
      "blood_percent": "5-10"
    },
    "source_unit": "mixed source quantities",
    "source_stage": "Base and later blood stages, separately",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1203",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf",
        "source_locator": "PDF page 1, product row",
        "exact_source_quote": "Fastidious Anaerobe Agar (acumedia) 45.7 g",
        "snapshot_sha256": "782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89",
        "parsed_text_sha256": "993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b"
      },
      {
        "source_key": "dsmz1203",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf",
        "source_locator": "PDF page 1, water-makeup row",
        "exact_source_quote": "add deionized water to 1000.0 ml",
        "snapshot_sha256": "782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89",
        "parsed_text_sha256": "993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b"
      },
      {
        "source_key": "togoM2521original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "Cool to 47°C then aseptically add 5-10% of sterile defibrinated horse blood, mix well and pour plates.",
        "snapshot_sha256": "2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886"
      },
      {
        "source_key": "togoM2521original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "sterilize by autoclaving at 121°C for 15 minutes.",
        "snapshot_sha256": "2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
        "field_path": "notes",
        "stored": "TOGO M2521 lists the DSMZ Medium 1203 Fastidious Anaerobe Agar formulation: 45.7 g Acumedia Fastidious Anaerobe Agar brought to one liter with deionized water, soaked, autoclaved at 121 C, cooled to 47 C, and supplemented with 5-10% sterile defibrinated horse blood.",
        "decision": "evidence_only",
        "rationale": "The current note correctly distinguishes base makeup, cooling and literal percent range; retain stage context while removing unsupported percent-basis typing from the separate concentration field."
      }
    ],
    "arithmetic_and_scope": "This summary is not a replacement for individual amount evidence. The historical copy in curation_history is preserved as provenance and is not silently edited."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:009091.

2 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 0/2 primary and 0/2 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 2: primary 0.00%; secondary 0.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009091.

8 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Source accession and spelling divergence

identity: supported. Targets: CultureMech:009091.

Exact TOGO M2521 meta.src_url resolves to DSMZ1203 Fastidious Anaerobe Agar. The provider itself says Astidious; retain that spelling as source provenance while distinguishing the primary name. One maintained owner and generated target have CultureMech:009091. Source identity does not establish equivalence with any other unreviewed recipe.

### Base makeup, percent basis and final volume

consistency: concern. Targets: CultureMech:009091.

All five local concentration instances are covered, together with quantitative preparation, pH and owner notes. The base is made up to 1 L before blood; 45.7 g/L is supported only at that stage. The source blood range has an unspecified basis and the post-blood final volume is not declared.

### Reconcile the generated layer with retained owner preparation

completeness: concern. Targets: CultureMech:009091.

The maintained owner already carries the 10 min soak, 121°C/15 min autoclave, 47°C cooling, aseptic blood addition, pouring plates and pH 7.0–7.4. These are absent from the generated target. Preserve the correct owner claims and add claim-level evidence; correct its percent basis before regenerating. Do not repeat an already completed owner repair as if those fields were missing there.

### Source product, water and blood qualifiers

grounding: supported. Targets: CultureMech:009091.

The owner water CHEBI15377 and generic blood UBERON0000178 labels are canonical and nonobsolete. UBERON blood does not encode horse species, sterility or defibrination; the source-qualified preferred term and preparation carry those restrictions. The Acumedia formulation remains a commercial mixture; no pure-compound identity or uninspected substitute-product composition is assigned. The generated target has no ontology links, while the owner has two primary links and one current CHEBI secondary link among three ingredients. These are coverage counts, not correctness scores.

### Solid complex medium without inferred growth conditions

scope: supported. Targets: CultureMech:009091.

Commercial agar and horse blood support SOLID_AGAR and COMPLEX/UNDEFINED. The anaerobe name describes the source medium; it does not by itself establish an exact gas composition, incubation temperature, strain-specific growth result or ontology taxonomy accession. There are no asserted stock references, KG matches, high-metal labels or papers requiring independent biological interpretation here.

### References and history do not authenticate every quantity

evidence: concern. Targets: CultureMech:009091.

The owner has source references, source tags and a historical repair note, but no attached amount snippets. Correct source-supported values therefore receive evidence_only decisions rather than verified. The generated layer lacks those references and repaired fields. Preserve historical events; add fresh narrowly scoped evidence without silently rewriting past claims.

### Local repair-history limit and regeneration ownership

provenance: supported. Targets: CultureMech:009091.

The normalized owner is the curation surface. The current merger single-owner branch would copy its fields; the existing generated target is demonstrably stale. The named historical repair script was not recovered within the documented prior-base and current ignored-inclusive filename scopes. All eight history timestamps are timezone-aware. The local supplement is pinned separately and is not fabricated as a native repository source input.

## Findings

### f1: Generated formulation omits the blood and retained preparation

major / open / confirmed; issue key: culturemech.009091.stale-source-reconciliation.

The generated target still has 1000 G_PER_L water and only two ingredients. Its maintained owner has corrected volume representation, required sterile defibrinated horse blood, ordered preparation and pH. The source confirms these additions, subject to the owner percent-basis limitation.

### f2: The owner assigns an unsupported volume-percent basis

major / open / confirmed; issue key: culturemech.009091.unspecified-blood-percent.

Both primary and provider say 5–10% sterile defibrinated horse blood without specifying w/v, w/w or v/v. The maintained concentration uses PERCENT_V_V. No measured final volume or unambiguous dose in mL follows from the printed range.

### f3: Retained base quantities need explicit stage evidence

minor / open / confirmed; issue key: culturemech.009091.makeup-and-evidence-scope.

The owner water note describes 1000 mL water, while the primary says add water to 1000 mL. Its 1 L marker and 45.7 g/L product are supportable for the base before blood, but root references alone are not attached quantity evidence. The final blood-containing volume remains unknown.

## Recommended Actions And Acceptance Checks

### a1

Reconcile the owner percent and makeup scope first; then regenerate the target from that maintained source, preserving the required blood, ordered preparation, pH and references. Do not patch the generated YAML or re-add already present owner preparation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the literal range and unresolved basis in native notes/evidence. Remove or withhold the unsupported basis-specific assertion until exact support is available; do not replace it with another guessed enum or computed mL dose.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Clarify makeup rather than an exact water aliquot, attach literal source evidence to each quantitative claim and retain the pre-blood versus post-blood distinction in explanations. Preserve the owner history and exact product qualifier.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch037/368/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch037/368/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml:1:id: CultureMech:009091<br>./data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml:1:id: CultureMech:009091<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch037/source-preflight-bound/368/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 7 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| dsmz1203 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf; PDF page 1, title, two-row base formulation and complete preparation paragraph; rendered page inspected | supports | Primary establishes the Acumedia base and water makeup before blood, the ordered soak/autoclave/cool/add/plate procedure and pH. It does not give a basis for the blood percentage or a measured post-blood final volume. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521; $.meta, $.components[0].items and $.comments[1].comment | supports | The exact original API links M2521 to DSMZ1203 and retains the same preparation. Its Astidious title is a provider spelling; pH 7.0–7.4 agrees with 7.2±0.2. |
| blood-source | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521; $.comments[1].comment | supports | Blood must be sterile, defibrinated and horse-derived; it is added aseptically after cooling. The exact 5–10% range has no w/v, w/w or v/v declaration. |
| dsmz-cycle | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf; PDF page 1, preparation paragraph | supports | Soak for 10 minutes, autoclave at 121°C for 15 minutes, cool to 47°C, then add blood. These are preparation conditions. |
| dsmz-ph | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf; PDF page 1, final preparation sentence | supports | The exact source pH is 7.2±0.2, equivalent to the owner range 7.0–7.4. No incubation conditions or growth outcomes are inferred. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch037/368/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| uberon0000178 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000178; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | UBERON:0000178 resolves to blood. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml; data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 4, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml", "events": 4, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer maps L separately, maps unqualified percent to PERCENT_W_V and reads explicit comments only in selected branches; those mechanics are not scientific support for any percent basis. Current single-owner merge copies the maintained record with merge metadata. This does not authenticate the absent historical repair writer or imply the stale generated bytes were produced by current code. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer maps L separately, maps unqualified percent to PERCENT_W_V and reads explicit comments only in selected branches; those mechanics are not scientific support for any percent basis. Current single-owner merge copies the maintained record with merge metadata. This does not authenticate the absent historical repair writer or imply the stale generated bytes were produced by current code. |
| writer-absence-provenance | /private/tmp/culturemech-review-source-preflight-batch037-tail/368/writer-absence-supplement/supplement.json; Complete frozen local supplement; bounded ignored-inclusive owned036 filename/content searches and recorded exact-base lookup | context_only | The named historical repair_togo_literal_products_score40.py was not recovered in the documented prior-base search. The owner history is retained; current public source support is assessed independently. This supplement is local provenance, not a nonexistent repository input. |
| current-writer-filename-search | /private/tmp/culturemech-review-work-batch037/368/writer-filename-search.json; Ignored-inclusive current owned037 filename search | context_only | No filename matching *literal*product* was found in the current owned checkout. Combined with the explicitly older supplemental provenance, this limits writer-history authentication; it does not negate the independently read current source. |
| mediadive1203api-attempt | https://mediadive.dsmz.de/rest/medium/1203; Preserved exact public retrieval result | context_only | The preserved mediadive1203api response is HTTP 503. The exact DSMZ1203 PDF and original TOGO M2521 API are available and independently support this bounded formulation assessment. |
| mediadive1203api_retry-attempt | https://mediadive.dsmz.de/rest/medium/1203; Preserved exact public retrieval result | context_only | The preserved mediadive1203api_retry response is HTTP 503. The exact DSMZ1203 PDF and original TOGO M2521 API are available and independently support this bounded formulation assessment. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The preserved mediadive1203api response is HTTP 503. The exact DSMZ1203 PDF and original TOGO M2521 API are available and independently support this bounded formulation assessment.
- The preserved mediadive1203api_retry response is HTTP 503. The exact DSMZ1203 PDF and original TOGO M2521 API are available and independently support this bounded formulation assessment.
- The TOGO landing page is a JavaScript shell; the exact original structured API and primary PDF supply the formulation.
- No universal absence claim is made about the historical repair script or its execution. Its missing code is a provenance limitation, not a reason to reject independently supported present owner fields.
- No final post-blood concentration, blood percent basis, manufacturer component expansion, growth condition or taxonomic assertion is invented.
- This scientific assessment preceded formal review validation and saving; their actual outcomes are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T201727Z-culturemech-009091-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: astidious_anaerobe_agar (CultureMech:009091)'
started_at: '2026-10-21T20:11:21Z'
finished_at: '2026-10-21T20:17:27Z'
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
summary: 'The exact DSMZ1203/TOGO M2521 formulation is Fastidious Anaerobe Agar: 45.7
  g product made up to 1 L before a later 5–10% sterile defibrinated horse-blood addition.
  The generated record is stale relative to the maintained owner and omits the blood,
  preparation and pH. The owner retains these claims but overtypes the unspecified
  blood percentage as volume/volume and needs claim-level evidence and water-makeup
  clarification.'
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
  - path: data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml
    sha256: 4dab9f7abc717bc3649236620fdcc779f91df545a93b8b3e9ee116463d101726
    role: target
  - path: data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml
    sha256: af2dfe52efa87ecd47992c5a589f2f52a100e3df83355bf1795581319932d08d
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
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 368; batch 037 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-six task batches
    contain 360 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 363 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009091
targets:
- target_id: CultureMech:009091
  path: data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml
  label: astidious_anaerobe_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch037/368/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch037/368/strict.tsv"
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009091
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
  - CultureMech:009091
- check_id: mediadive1203api-source-access
  name: 'Exact source content access: mediadive1203api'
  required: false
  status: unavailable
  summary: The preserved mediadive1203api response is HTTP 503. The exact DSMZ1203
    PDF and original TOGO M2521 API are available and independently support this bounded
    formulation assessment.
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - mediadive1203api-attempt
- check_id: mediadive1203api_retry-source-access
  name: 'Exact source content access: mediadive1203api_retry'
  required: false
  status: unavailable
  summary: The preserved mediadive1203api_retry response is HTTP 503. The exact DSMZ1203
    PDF and original TOGO M2521 API are available and independently support this bounded
    formulation assessment.
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - mediadive1203api_retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T20:17:25Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T20:17:25Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:16.152211Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch037/368/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:17.249783Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch037/368/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:18.796016Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:19.722509Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T20:17:25Z'
  support: supports
  summary: './data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml:1:id: CultureMech:009091

    ./data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml:1:id: CultureMech:009091

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/source-preflight-bound/368/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T20:17:25Z'
  support: supports
  summary: 7 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 61a46e767bbf6e19b2d606bf4ccc935c1fca453178e64996e8ef1687a7b49684
- evidence_id: dsmz1203
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf
  locator: PDF page 1, title, two-row base formulation and complete preparation paragraph;
    rendered page inspected
  accessed_at: '2026-10-21T19:52:51.210645Z'
  support: supports
  summary: Primary establishes the Acumedia base and water makeup before blood, the
    ordered soak/autoclave/cool/add/plate procedure and pH. It does not give a basis
    for the blood percentage or a measured post-blood final volume.
  quote: add deionized water to 1000.0 ml
  snapshot_sha256: 782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521
  locator: $.meta, $.components[0].items and $.comments[1].comment
  accessed_at: '2026-10-21T19:52:50.266552Z'
  support: supports
  summary: The exact original API links M2521 to DSMZ1203 and retains the same preparation.
    Its Astidious title is a provider spelling; pH 7.0–7.4 agrees with 7.2±0.2.
  quote: '"src_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf"'
  snapshot_sha256: 2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886
- evidence_id: blood-source
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521
  locator: $.comments[1].comment
  accessed_at: '2026-10-21T19:52:50.266552Z'
  support: supports
  summary: Blood must be sterile, defibrinated and horse-derived; it is added aseptically
    after cooling. The exact 5–10% range has no w/v, w/w or v/v declaration.
  quote: Cool to 47°C then aseptically add 5-10% of sterile defibrinated horse blood,
    mix well and pour plates.
  snapshot_sha256: 2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886
- evidence_id: dsmz-cycle
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf
  locator: PDF page 1, preparation paragraph
  accessed_at: '2026-10-21T19:52:51.210645Z'
  support: supports
  summary: Soak for 10 minutes, autoclave at 121°C for 15 minutes, cool to 47°C, then
    add blood. These are preparation conditions.
  quote: Allow to soak for 10 minutes, swirl to mix then sterilize by autoclaving
    at 121°C for 15
  snapshot_sha256: 782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89
- evidence_id: dsmz-ph
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf
  locator: PDF page 1, final preparation sentence
  accessed_at: '2026-10-21T19:52:51.210645Z'
  support: supports
  summary: The exact source pH is 7.2±0.2, equivalent to the owner range 7.0–7.4.
    No incubation conditions or growth outcomes are inferred.
  quote: 'pH: 7.2 ± 0.2'
  snapshot_sha256: 782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/368/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T20:17:25Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 72d486980db4f8fc9c38e76a8bc0bb72114f910d97cd1dbf0d264b8aa81a7cbd
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
- evidence_id: uberon0000178
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000178
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T19:52:52.109180Z'
  support: supports
  summary: UBERON:0000178 resolves to blood. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 1922fcc7dd50d09155ecaa4a2fcc417b4f069ebda526a493f4b5ef840b7076da
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T20:17:25Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml; data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T20:17:25Z'
  support: context_only
  summary: '[{"input": "target", "events": 4, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml",
    "events": 4, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:17:25Z'
  support: context_only
  summary: Current importer maps L separately, maps unqualified percent to PERCENT_W_V
    and reads explicit comments only in selected branches; those mechanics are not
    scientific support for any percent basis. Current single-owner merge copies the
    maintained record with merge metadata. This does not authenticate the absent historical
    repair writer or imply the stale generated bytes were produced by current code.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:17:25Z'
  support: context_only
  summary: Current importer maps L separately, maps unqualified percent to PERCENT_W_V
    and reads explicit comments only in selected branches; those mechanics are not
    scientific support for any percent basis. Current single-owner merge copies the
    maintained record with merge metadata. This does not authenticate the absent historical
    repair writer or imply the stale generated bytes were produced by current code.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-absence-provenance
  kind: record_content
  reference: /private/tmp/culturemech-review-source-preflight-batch037-tail/368/writer-absence-supplement/supplement.json
  locator: Complete frozen local supplement; bounded ignored-inclusive owned036 filename/content
    searches and recorded exact-base lookup
  accessed_at: '2026-10-21T20:17:25Z'
  support: context_only
  summary: The named historical repair_togo_literal_products_score40.py was not recovered
    in the documented prior-base search. The owner history is retained; current public
    source support is assessed independently. This supplement is local provenance,
    not a nonexistent repository input.
  snapshot_sha256: f7196c4594bd861f90c34ee82a0e2b0c49fb62dc5b0a20c54ef0f15c441b05f4
- evidence_id: current-writer-filename-search
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/368/writer-filename-search.json
  locator: Ignored-inclusive current owned037 filename search
  accessed_at: '2026-10-21T20:17:25Z'
  support: context_only
  summary: No filename matching *literal*product* was found in the current owned checkout.
    Combined with the explicitly older supplemental provenance, this limits writer-history
    authentication; it does not negate the independently read current source.
  snapshot_sha256: ef5783cea454d0a72274d3cfb3b657a80351f237e2223c0820f4985e5f91fb78
  search_scope: Current owned037 ignored-inclusive filename pattern only; no universal
    or other-revision absence claim.
- evidence_id: mediadive1203api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1203
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:52:49.029868Z'
  support: context_only
  summary: The preserved mediadive1203api response is HTTP 503. The exact DSMZ1203
    PDF and original TOGO M2521 API are available and independently support this bounded
    formulation assessment.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive1203api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1203
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:53:28.239718Z'
  support: context_only
  summary: The preserved mediadive1203api_retry response is HTTP 503. The exact DSMZ1203
    PDF and original TOGO M2521 API are available and independently support this bounded
    formulation assessment.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 10 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"ingredient_or_context\": \"\
    Base water makeup\",\n    \"field_path\": \"ingredients[0].concentration\",\n\
    \    \"local\": {\n      \"value\": \"1000\",\n      \"unit\": \"G_PER_L\"\n \
    \   },\n    \"source_amount\": 1000,\n    \"source_unit\": \"mL makeup\",\n  \
    \  \"source_stage\": \"Base before blood\",\n    \"decision\": \"correct\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1203\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1, water-makeup row\",\n        \"exact_source_quote\"\
    : \"add deionized water to 1000.0 ml\",\n        \"snapshot_sha256\": \"782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89\"\
    ,\n        \"parsed_text_sha256\": \"993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2521original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"add deionized water to\\\",\\n          \\\"volume\\\
    \": 1000,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\"\
    : \"2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886\"\n     \
    \ }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"1000 G_PER_L\
    \ is a mass-concentration error; restore makeup to 1 L before blood.\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\n        },\n  \
    \      \"decision\": \"evidence_only\",\n        \"rationale\": \"1.0 L is numerically\
    \ appropriate as the pre-blood base makeup marker, not a measured water dose or\
    \ final blood-containing volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"TOGO\
    \ M2521 lists 1000 ml deionized water.\",\n        \"decision\": \"correct\",\n\
    \        \"rationale\": \"Clarify add water to 1000 mL rather than an independently\
    \ measured 1000 mL water addition.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"1000 mL = 1 L by unit conversion. Preserve the to wording and pre-blood stage;\
    \ no water density or final-medium concentration is inferred.\"\n  },\n  {\n \
    \   \"quantity_id\": \"q2\",\n    \"ingredient_or_context\": \"Acumedia agar base\"\
    ,\n    \"field_path\": \"ingredients[1].concentration\",\n    \"local\": {\n \
    \     \"value\": \"45.7\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : 45.7,\n    \"source_unit\": \"g per 1 L base\",\n    \"source_stage\": \"Before\
    \ blood\",\n    \"decision\": \"evidence_only\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1203\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1, product row\",\n        \"exact_source_quote\"\
    : \"Fastidious Anaerobe Agar (acumedia) 45.7 g\",\n        \"snapshot_sha256\"\
    : \"782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89\",\n    \
    \    \"parsed_text_sha256\": \"993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1203\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf\",\n   \
    \     \"source_locator\": \"PDF page 1, water-makeup row\",\n        \"exact_source_quote\"\
    : \"add deionized water to 1000.0 ml\",\n        \"snapshot_sha256\": \"782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89\"\
    ,\n        \"parsed_text_sha256\": \"993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2521original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Fastidious Anaerobe Agar (acumedia)\\\",\\n  \
    \        \\\"volume\\\": 45.7,\\n          \\\"unit\\\": \\\"g\\\"\",\n      \
    \  \"snapshot_sha256\": \"2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[1].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"45.7\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"45.7 G_PER_L is supported for the base explicitly made up to 1 L; it has no\
    \ attached concentration evidence and does not establish the final post-blood\
    \ concentration.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"45.7\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"45.7\
    \ G_PER_L is supported for the base explicitly made up to 1 L; it has no attached\
    \ concentration evidence and does not establish the final post-blood concentration.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"TOGO\
    \ M2521 lists 45.7 g Fastidious Anaerobe Agar (Acumedia) per liter.\",\n     \
    \   \"decision\": \"evidence_only\",\n        \"rationale\": \"Retain the per-litre\
    \ product amount explicitly at the pre-blood stage.\"\n      }\n    ],\n    \"\
    arithmetic_and_scope\": \"The explicit base makeup supports 45.7 g / 1 L = 45.7\
    \ g/L before blood. Product composition is not decomposed or authenticated from\
    \ a different manufacturer recipe.\"\n  },\n  {\n    \"quantity_id\": \"q3\",\n\
    \    \"ingredient_or_context\": \"Sterile defibrinated horse blood\",\n    \"\
    field_path\": \"ingredients[2].concentration\",\n    \"local\": null,\n    \"\
    source_amount\": \"5-10\",\n    \"source_unit\": \"percent, basis unspecified\"\
    ,\n    \"source_stage\": \"Aseptic addition after cooling to 47°C\",\n    \"decision\"\
    : \"correct\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM2521original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521\"\
    ,\n        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"Cool to 47°C then aseptically add 5-10% of sterile defibrinated horse blood,\
    \ mix well and pour plates.\",\n        \"snapshot_sha256\": \"2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[2].concentration\",\n       \
    \ \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\": \"\
    The generated target lacks the required source blood addition; restore its literal\
    \ range and qualifications.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5-10\",\n          \"unit\": \"PERCENT_V_V\"\n   \
    \     },\n        \"decision\": \"correct\",\n        \"rationale\": \"The source\
    \ does not support PERCENT_V_V. Preserve the 5–10% text with an explicit unresolved\
    \ basis; do not select another percentage enum by inference.\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"TOGO\
    \ M2521 instructs adding 5-10% sterile defibrinated horse blood after autoclaving\
    \ and cooling to 47 C.\",\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"The note retains the literal unqualified range and addition stage;\
    \ it is not claim-level evidence.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\",\n        \"field_path\"\
    : \"preparation_steps[3].description\",\n        \"stored\": \"Aseptically add\
    \ 5-10% sterile defibrinated horse blood, mix well, and pour plates.\",\n    \
    \    \"decision\": \"evidence_only\",\n        \"rationale\": \"The source supports\
    \ this literal unqualified range, aseptic mixing and pouring plates.\"\n     \
    \ }\n    ],\n    \"arithmetic_and_scope\": \"No conversion to mL, mass or a measured\
    \ final concentration is justified. The native enum offers only basis-specific\
    \ percentage units; use source-qualified notes/evidence until the basis is established\
    \ rather than a false fixed enum.\"\n  },\n  {\n    \"quantity_id\": \"q4\",\n\
    \    \"ingredient_or_context\": \"Base soaking duration\",\n    \"field_path\"\
    : \"preparation_steps\",\n    \"local\": null,\n    \"source_amount\": 10,\n \
    \   \"source_unit\": \"minutes\",\n    \"source_stage\": \"Ordered base preparation\
    \ before blood\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"togoM2521original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521\",\n\
    \        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"Allow to soak for 10 minutes\",\n        \"snapshot_sha256\": \"2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"Restore the\
    \ source-supported preparation already present in the maintained owner after resolving\
    \ its blood basis.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].duration\",\n        \"stored\"\
    : \"10 minutes\",\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Exact source numerical preparation claim is retained correctly; attach scoped\
    \ evidence, not a new growth assertion.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\",\n        \"\
    field_path\": \"preparation_steps[0].description\",\n        \"stored\": \"Allow\
    \ the agar powder to soak for 10 min, then swirl to mix.\",\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The description is source-consistent\
    \ and remains preparation-only.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"Preserve the ordered 10 min soak, 121°C/15 min autoclave and cooling to 47°C.\
    \ The blood is added afterward; this cycle does not sterilize the already blood-supplemented\
    \ plates.\"\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"ingredient_or_context\"\
    : \"Base autoclave temperature\",\n    \"field_path\": \"preparation_steps\",\n\
    \    \"local\": null,\n    \"source_amount\": 121,\n    \"source_unit\": \"degrees\
    \ Celsius\",\n    \"source_stage\": \"Ordered base preparation before blood\"\
    ,\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"togoM2521original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521\"\
    ,\n        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"sterilize by autoclaving at 121°C for 15 minutes.\",\n        \"snapshot_sha256\"\
    : \"2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886\"\n     \
    \ }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Restore the source-supported\
    \ preparation already present in the maintained owner after resolving its blood\
    \ basis.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Autoclave the mixed medium at 121 C for 15 min.\",\n        \"decision\":\
    \ \"evidence_only\",\n        \"rationale\": \"Exact source numerical preparation\
    \ claim is retained correctly; attach scoped evidence, not a new growth assertion.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Preserve the ordered 10 min\
    \ soak, 121°C/15 min autoclave and cooling to 47°C. The blood is added afterward;\
    \ this cycle does not sterilize the already blood-supplemented plates.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q6\",\n    \"ingredient_or_context\": \"Base autoclave\
    \ duration\",\n    \"field_path\": \"preparation_steps\",\n    \"local\": null,\n\
    \    \"source_amount\": 15,\n    \"source_unit\": \"minutes\",\n    \"source_stage\"\
    : \"Ordered base preparation before blood\",\n    \"decision\": \"add\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2521original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521\"\
    ,\n        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"sterilize by autoclaving at 121°C for 15 minutes.\",\n        \"snapshot_sha256\"\
    : \"2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886\"\n     \
    \ }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Restore the source-supported\
    \ preparation already present in the maintained owner after resolving its blood\
    \ basis.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Autoclave the mixed medium at 121 C for 15 min.\",\n        \"decision\":\
    \ \"evidence_only\",\n        \"rationale\": \"Exact source numerical preparation\
    \ claim is retained correctly; attach scoped evidence, not a new growth assertion.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Preserve the ordered 10 min\
    \ soak, 121°C/15 min autoclave and cooling to 47°C. The blood is added afterward;\
    \ this cycle does not sterilize the already blood-supplemented plates.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q7\",\n    \"ingredient_or_context\": \"Cooling temperature\
    \ before blood\",\n    \"field_path\": \"preparation_steps\",\n    \"local\":\
    \ null,\n    \"source_amount\": 47,\n    \"source_unit\": \"degrees Celsius\"\
    ,\n    \"source_stage\": \"Ordered base preparation before blood\",\n    \"decision\"\
    : \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2521original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521\"\
    ,\n        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"Cool to 47°C then aseptically add\",\n        \"snapshot_sha256\": \"2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"Restore the\
    \ source-supported preparation already present in the maintained owner after resolving\
    \ its blood basis.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].temperature\",\n        \"stored\"\
    : {\n          \"value\": 47.0,\n          \"unit\": \"CELSIUS\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"Exact source\
    \ numerical preparation claim is retained correctly; attach scoped evidence, not\
    \ a new growth assertion.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"Cool the sterilized medium to 47 C.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The description is source-consistent and remains preparation-only.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Preserve the ordered 10 min\
    \ soak, 121°C/15 min autoclave and cooling to 47°C. The blood is added afterward;\
    \ this cycle does not sterilize the already blood-supplemented plates.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q8\",\n    \"ingredient_or_context\": \"Source pH\
    \ range\",\n    \"field_path\": \"ph_range\",\n    \"local\": null,\n    \"source_amount\"\
    : {\n      \"central\": 7.2,\n      \"tolerance\": 0.2,\n      \"min\": 7.0,\n\
    \      \"max\": 7.4\n    },\n    \"source_unit\": \"pH\",\n    \"source_stage\"\
    : \"Source final preparation statement\",\n    \"decision\": \"add\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz1203\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1, final sentence\",\n        \"exact_source_quote\"\
    : \"pH: 7.2 ± 0.2\",\n        \"snapshot_sha256\": \"782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89\"\
    ,\n        \"parsed_text_sha256\": \"993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2521original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521\"\
    ,\n        \"source_locator\": \"$.meta.ph\",\n        \"exact_source_quote\"\
    : \"\\\"ph\\\": \\\"7.0 - 7.4\\\"\",\n        \"snapshot_sha256\": \"2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ph_range\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Restore the exact source\
    \ pH range retained in the owner.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\",\n        \"field_path\"\
    : \"ph_range\",\n        \"stored\": {\n          \"min\": 7.0,\n          \"\
    max\": 7.4\n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"7.2−0.2=7.0 and 7.2+0.2=7.4; the correct range lacks attached evidence.\"\n\
    \      }\n    ],\n    \"arithmetic_and_scope\": \"This arithmetic translates the\
    \ stated tolerance only; it does not establish an adjustment reagent, incubation\
    \ pH measurement or growth response.\"\n  },\n  {\n    \"quantity_id\": \"q9\"\
    ,\n    \"ingredient_or_context\": \"Measured final volume after blood\",\n   \
    \ \"field_path\": \"preparation_steps\",\n    \"local\": null,\n    \"source_amount\"\
    : null,\n    \"source_unit\": \"not stated\",\n    \"source_stage\": \"After blood\
    \ addition\",\n    \"decision\": \"not_quantified\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1203\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf\",\n       \
    \ \"source_locator\": \"PDF page 1, water-makeup row\",\n        \"exact_source_quote\"\
    : \"add deionized water to 1000.0 ml\",\n        \"snapshot_sha256\": \"782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89\"\
    ,\n        \"parsed_text_sha256\": \"993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2521original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521\"\
    ,\n        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"Cool to 47°C then aseptically add 5-10% of sterile defibrinated horse blood,\
    \ mix well and pour plates.\",\n        \"snapshot_sha256\": \"2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    Do not infer a final post-blood volume.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\",\n        \"\
    field_path\": \"preparation_steps[3].description\",\n        \"stored\": \"Aseptically\
    \ add 5-10% sterile defibrinated horse blood, mix well, and pour plates.\",\n\
    \        \"decision\": \"not_quantified\",\n        \"rationale\": \"The existing\
    \ description gives a percent range without a basis or measured final volume.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"The base is made up to 1000\
    \ mL before blood. Neither final volume nor an exact final product concentration\
    \ is computed from the unqualified 5–10%.\"\n  },\n  {\n    \"quantity_id\": \"\
    q10\",\n    \"ingredient_or_context\": \"Owner numerical source summary\",\n \
    \   \"field_path\": \"notes\",\n    \"local\": \"TOGO M2521 lists the DSMZ Medium\
    \ 1203 Fastidious Anaerobe Agar formulation: 45.7 g Acumedia Fastidious Anaerobe\
    \ Agar brought to one liter with deionized water, soaked, autoclaved at 121 C,\
    \ cooled to 47 C, and supplemented with 5-10% sterile defibrinated horse blood.\"\
    ,\n    \"source_amount\": {\n      \"base_g\": 45.7,\n      \"makeup_L\": 1,\n\
    \      \"autoclave_C\": 121,\n      \"cool_C\": 47,\n      \"blood_percent\":\
    \ \"5-10\"\n    },\n    \"source_unit\": \"mixed source quantities\",\n    \"\
    source_stage\": \"Base and later blood stages, separately\",\n    \"decision\"\
    : \"evidence_only\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1203\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1, product row\",\n        \"exact_source_quote\"\
    : \"Fastidious Anaerobe Agar (acumedia) 45.7 g\",\n        \"snapshot_sha256\"\
    : \"782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89\",\n    \
    \    \"parsed_text_sha256\": \"993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1203\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf\",\n   \
    \     \"source_locator\": \"PDF page 1, water-makeup row\",\n        \"exact_source_quote\"\
    : \"add deionized water to 1000.0 ml\",\n        \"snapshot_sha256\": \"782f6502aa39c04fa4736add87e3e8f72530430a3b41c1f3bb8772cfa2a17f89\"\
    ,\n        \"parsed_text_sha256\": \"993fd93b6d7f0d6da1207663ac7d142d6ea9f43c8df02e89ec98a34245bd3d2b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2521original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521\"\
    ,\n        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"Cool to 47°C then aseptically add 5-10% of sterile defibrinated horse blood,\
    \ mix well and pour plates.\",\n        \"snapshot_sha256\": \"2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886\"\
    \n      },\n      {\n        \"source_key\": \"togoM2521original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2521\"\
    ,\n        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"sterilize by autoclaving at 121°C for 15 minutes.\",\n        \"snapshot_sha256\"\
    : \"2124c8d418f3a85e5961c04991a7c9c8d918627dd1b144bfca44773d159b1886\"\n     \
    \ }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"TOGO M2521 lists\
    \ the DSMZ Medium 1203 Fastidious Anaerobe Agar formulation: 45.7 g Acumedia Fastidious\
    \ Anaerobe Agar brought to one liter with deionized water, soaked, autoclaved\
    \ at 121 C, cooled to 47 C, and supplemented with 5-10% sterile defibrinated horse\
    \ blood.\",\n        \"decision\": \"evidence_only\",\n        \"rationale\":\
    \ \"The current note correctly distinguishes base makeup, cooling and literal\
    \ percent range; retain stage context while removing unsupported percent-basis\
    \ typing from the separate concentration field.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"This summary is not a replacement for individual amount evidence. The historical\
    \ copy in curation_history is preserved as provenance and is not silently edited.\"\
    \n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '2 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 0/2 primary
    and 0/2 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - uberon0000178
  details: 'Instance coverage on a 0–100 percent scale, denominator 2: primary 0.00%;
    secondary 0.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 8 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Source accession and spelling divergence
  outcome: supported
  summary: Exact TOGO M2521 meta.src_url resolves to DSMZ1203 Fastidious Anaerobe
    Agar. The provider itself says Astidious; retain that spelling as source provenance
    while distinguishing the primary name. One maintained owner and generated target
    have CultureMech:009091. Source identity does not establish equivalence with any
    other unreviewed recipe.
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - record
  - dsmz1203
  - togo
  - owner-0
- assessment_id: source-stage-consistency
  area: consistency
  topic: Base makeup, percent basis and final volume
  outcome: concern
  summary: All five local concentration instances are covered, together with quantitative
    preparation, pH and owner notes. The base is made up to 1 L before blood; 45.7
    g/L is supported only at that stage. The source blood range has an unspecified
    basis and the post-blood final volume is not declared.
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - quantity-inventory
  - dsmz1203
  - blood-source
  - owner-0
- assessment_id: preparation
  area: completeness
  topic: Reconcile the generated layer with retained owner preparation
  outcome: concern
  summary: The maintained owner already carries the 10 min soak, 121°C/15 min autoclave,
    47°C cooling, aseptic blood addition, pouring plates and pH 7.0–7.4. These are
    absent from the generated target. Preserve the correct owner claims and add claim-level
    evidence; correct its percent basis before regenerating. Do not repeat an already
    completed owner repair as if those fields were missing there.
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - record
  - dsmz-cycle
  - dsmz-ph
  - blood-source
  - owner-0
- assessment_id: chemical-forms
  area: grounding
  topic: Source product, water and blood qualifiers
  outcome: supported
  summary: The owner water CHEBI15377 and generic blood UBERON0000178 labels are canonical
    and nonobsolete. UBERON blood does not encode horse species, sterility or defibrination;
    the source-qualified preferred term and preparation carry those restrictions.
    The Acumedia formulation remains a commercial mixture; no pure-compound identity
    or uninspected substitute-product composition is assigned. The generated target
    has no ontology links, while the owner has two primary links and one current CHEBI
    secondary link among three ingredients. These are coverage counts, not correctness
    scores.
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - record
  - dsmz1203
  - blood-source
  - chebi15377
  - uberon0000178
  - mim
  - owner-0
- assessment_id: classification
  area: scope
  topic: Solid complex medium without inferred growth conditions
  outcome: supported
  summary: Commercial agar and horse blood support SOLID_AGAR and COMPLEX/UNDEFINED.
    The anaerobe name describes the source medium; it does not by itself establish
    an exact gas composition, incubation temperature, strain-specific growth result
    or ontology taxonomy accession. There are no asserted stock references, KG matches,
    high-metal labels or papers requiring independent biological interpretation here.
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - record
  - dsmz1203
  - togo
  - owner-0
- assessment_id: evidence-placement
  area: evidence
  topic: References and history do not authenticate every quantity
  outcome: concern
  summary: The owner has source references, source tags and a historical repair note,
    but no attached amount snippets. Correct source-supported values therefore receive
    evidence_only decisions rather than verified. The generated layer lacks those
    references and repaired fields. Preserve historical events; add fresh narrowly
    scoped evidence without silently rewriting past claims.
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - record
  - quantity-inventory
  - history-metadata
  - owner-0
- assessment_id: ownership
  area: provenance
  topic: Local repair-history limit and regeneration ownership
  outcome: supported
  summary: The normalized owner is the curation surface. The current merger single-owner
    branch would copy its fields; the existing generated target is demonstrably stale.
    The named historical repair script was not recovered within the documented prior-base
    and current ignored-inclusive filename scopes. All eight history timestamps are
    timezone-aware. The local supplement is pinned separately and is not fabricated
    as a native repository source input.
  target_ids:
  - CultureMech:009091
  evidence_ids:
  - writer-0
  - writer-1
  - writer-absence-provenance
  - current-writer-filename-search
  - history-metadata
  - owner-0
findings:
- finding_id: f1
  issue_key: culturemech.009091.stale-source-reconciliation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated formulation omits the blood and retained preparation
  description: The generated target still has 1000 G_PER_L water and only two ingredients.
    Its maintained owner has corrected volume representation, required sterile defibrinated
    horse blood, ordered preparation and pH. The source confirms these additions,
    subject to the owner percent-basis limitation.
  target_ids:
  - CultureMech:009091
  field_paths:
  - ingredients
  - preparation_steps
  - ph_range
  - sterilization
  - references
  evidence_ids:
  - record
  - dsmz1203
  - blood-source
  - dsmz-cycle
  - dsmz-ph
  - quantity-inventory
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml
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
  issue_key: culturemech.009091.unspecified-blood-percent
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: The owner assigns an unsupported volume-percent basis
  description: Both primary and provider say 5–10% sterile defibrinated horse blood
    without specifying w/v, w/w or v/v. The maintained concentration uses PERCENT_V_V.
    No measured final volume or unambiguous dose in mL follows from the printed range.
  target_ids:
  - CultureMech:009091
  field_paths:
  - ingredients[2].concentration
  evidence_ids:
  - blood-source
  - dsmz1203
  - quantity-inventory
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.009091.makeup-and-evidence-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Retained base quantities need explicit stage evidence
  description: The owner water note describes 1000 mL water, while the primary says
    add water to 1000 mL. Its 1 L marker and 45.7 g/L product are supportable for
    the base before blood, but root references alone are not attached quantity evidence.
    The final blood-containing volume remains unknown.
  target_ids:
  - CultureMech:009091
  field_paths:
  - ingredients[0].notes
  - ingredients
  - preparation_steps
  - references
  evidence_ids:
  - dsmz1203
  - togo
  - quantity-inventory
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Reconcile the owner percent and makeup scope first; then regenerate
    the target from that maintained source, preserving the required blood, ordered
    preparation, pH and references. Do not patch the generated YAML or re-add already
    present owner preparation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009091
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml
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
  description: Preserve the literal range and unresolved basis in native notes/evidence.
    Remove or withhold the unsupported basis-specific assertion until exact support
    is available; do not replace it with another guessed enum or computed mL dose.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009091
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml
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
  description: Clarify makeup rather than an exact water aliquot, attach literal source
    evidence to each quantitative claim and retain the pre-blood versus post-blood
    distinction in explanations. Preserve the owner history and exact product qualifier.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009091
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml
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
- The preserved mediadive1203api response is HTTP 503. The exact DSMZ1203 PDF and
  original TOGO M2521 API are available and independently support this bounded formulation
  assessment.
- The preserved mediadive1203api_retry response is HTTP 503. The exact DSMZ1203 PDF
  and original TOGO M2521 API are available and independently support this bounded
  formulation assessment.
- The TOGO landing page is a JavaScript shell; the exact original structured API and
  primary PDF supply the formulation.
- No universal absence claim is made about the historical repair script or its execution.
  Its missing code is a provenance limitation, not a reason to reject independently
  supported present owner fields.
- No final post-blood concentration, blood percent basis, manufacturer component expansion,
  growth condition or taxonomic assertion is invented.
- This scientific assessment preceded formal review validation and saving; their actual
  outcomes are recorded separately.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-037
- generated-medium
```
