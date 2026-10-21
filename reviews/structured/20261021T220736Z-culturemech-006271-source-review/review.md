# Source and formulation review: bacillus_thermantarcticus_medium (CultureMech:006271)

- Review: 20261021T220736Z-culturemech-006271-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T21:51:51Z
- Finished UTC: 2026-10-21T22:07:36Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 675 uses 500 mL soil extract and 500 mL water, not 500 g/L soil extract. Both maintained owners and the generated target retain the wrong soil unit; the DSMZ owner already preserves the delegated soil-extraction procedure. Its two attached amount claims are authenticated by recovered historical raw. Exact KG-Microbe medium 74 correspondence remains unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 384; batch 039 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-eight task batches contain 380 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 383 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006271 | data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml | generated | bacillus_thermantarcticus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006271 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006271 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch039/384/strict.tsv |
| validate-terms | passed | True | CultureMech:006271 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006271 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006271 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive675api | unavailable | False | CultureMech:006271 | Optional current access failure mediadive675api preserved separately; exact primary and recovered receiving raw remain available. |
| Exact source content access: mediadive675api_retry | unavailable | False | CultureMech:006271 | Optional current access failure mediadive675api_retry preserved separately; exact primary and recovered receiving raw remain available. |
| Exact source content access: mediadive80api | unavailable | False | CultureMech:006271 | Optional current access failure mediadive80api preserved separately; exact primary and recovered receiving raw remain available. |
| Exact source content access: komodo675detail | unavailable | False | CultureMech:006271 | Optional current access failure komodo675detail preserved separately; exact primary and recovered receiving raw remain available. |
| Required exact KG-Microbe medium 74 correspondence | unavailable | True | CultureMech:006271 | Bound source/input inventory contains no exact graph node/edge snapshot establishing the stored mediadive.medium:74 match. Source accession, ingredient names and code inspection cannot substitute for graph correspondence. No universal external graph absence is claimed. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006271.

The four documented recipes completed; interpret the scope of each separately.

### Exact DSMZ/KOMODO recipient and soil dependency

identity: supported. Targets: CultureMech:006271.

CultureMech:006271 is the KOMODO/generated target, CultureMech:001815 the maintained DSMZ 675 source. Source-duplicate links resolve to these exact owners. DSMZ 80 is only the named soil-extract preparation dependency, not an alternative full recipe. The medium title does not establish a strain growth assertion.

### Liquid extract and main water recovery

quantity: concern. Targets: CultureMech:006271.

All three layers store soil extract as 500 G_PER_L despite exact current primary and authenticated historical source specifying 500 mL. All omit the separate 500 mL main water. Two mass rates have authentic attached evidence only on the DSMZ owner. Listed liquids sum to 1000 mL and provider declares 1000 mL; those are distinct evidence bases from a measured final volume.

### Preserved owner procedure and excluded parent conditions

completeness: concern. Targets: CultureMech:006271.

The DSMZ owner already retains soil extraction: 400 g sieved air-dried soil with 960 mL water, 121 °C for one hour, cool/settle/decant/filter, then autoclave 200 mL aliquots and store at room temperature until clear. Target/KOMODO omit this procedure. Quantified extraction conditions must remain in the extract stage. DSMZ 80 main peptone, beef extract, glycerol, agar, 150 mL extract dose and pH 7 are excluded, as are its four historical amount claims.

### Current label and secondary correspondence

grounding: concern. Targets: CultureMech:006271.

Target primary-term coverage is 1/3 ingredients, while both owners have 3/3 primary terms; target CHEBI-based secondary coverage is 1/3. These fractions describe slots, not correctness or a requirement to assign pure-compound CHEBI IDs to mixtures. Exact current NaCl secondary key is supported. Owners’ Yeast extract and Soil extract labels differ by case from pinned FOODON/MICRO canonical labels; target lacks those later assertions. Parent-only label discrepancies do not transfer.

### Recovered exact historical receiving source

evidence: supported. Targets: CultureMech:006271.

Two DSMZ-owner amount claims match exact recovered raw 731589616c… and original October 7 access metadata. The embedded parent source_raw locator and extraction provenance are pinned in the bound catalog. Present-day 503 responses are separate attempts and do not negate the authenticated historical claim. The parent’s four main-formula objects are outside scope; their derivative status is retained without importing them.

### KG-Microbe identity remains unconfirmed

graph: unknown. Targets: CultureMech:006271.

All three layers assert mediadive.medium:74. The source identity is DSMZ 675, but differing identifiers alone do not prove a graph error. The relevant exact graph node/edges are not available in the bound evidence. Current matching code uses CHEBI/FOODON ingredient sets and ignores concentration; it also omits MICRO terms, so a code read or source formulation cannot authenticate the stored graph match.

### Undefined liquid mixture and catalog oxygen

scope: supported. Targets: CultureMech:006271.

COMPLEX/UNDEFINED/LIQUID accords with yeast extract and soil-water extract without agar in DSMZ 675. Catalog Aerobic: No is retained as provenance only; it does not supply a demonstrated gas regime. No generic temperature, target organism or parent growth condition is added.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006271.

25 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006271.

13 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Yeast extract",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "rationale": "Existing exact snippet and cited raw hash authenticated."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz675",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Yeast extract 6.0 g",
        "snapshot_sha256": "d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e",
        "parsed_text_sha256": "e3c099476e3bdca66a5f769de65059e326598eeb3cc850c5a0830359d7a27412",
        "accessed_at": "2026-10-21T20:56:16.901317Z"
      },
      {
        "source_key": "mediadive675Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/675",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "731589616c8a992664a6290b18db5dfb4bde2c843df1b7a0cf8bef7065f7632e",
        "accessed_at": "2026-10-07T12:17:23.420492+00:00"
      }
    ],
    "proposed_source_representation": {
      "printed_mass_g": 6,
      "historical_provider_g_L": 6,
      "provider_volume_mL": 1000,
      "stage": "main recipe"
    },
    "rationale": "Primary batch masses and authenticated provider rates agree. Verified applies only to the DSMZ owner with attached matching evidence; the other layers require claim-level support. Provider declared volume is not a measured-volume assertion."
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Sodium chloride",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "rationale": "Existing exact snippet and cited raw hash authenticated."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz675",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NaCl 3.0 g",
        "snapshot_sha256": "d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e",
        "parsed_text_sha256": "e3c099476e3bdca66a5f769de65059e326598eeb3cc850c5a0830359d7a27412",
        "accessed_at": "2026-10-21T20:56:16.901317Z"
      },
      {
        "source_key": "mediadive675Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/675",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 51.3347,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "731589616c8a992664a6290b18db5dfb4bde2c843df1b7a0cf8bef7065f7632e",
        "accessed_at": "2026-10-07T12:17:23.420492+00:00"
      }
    ],
    "proposed_source_representation": {
      "printed_mass_g": 3,
      "historical_provider_g_L": 3,
      "provider_volume_mL": 1000,
      "stage": "main recipe"
    },
    "rationale": "Primary batch masses and authenticated provider rates agree. Verified applies only to the DSMZ owner with attached matching evidence; the other layers require claim-level support. Provider declared volume is not a measured-volume assertion."
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Soil-extract receiving aliquot",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "500",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "500",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "500",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz675",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf",
        "source_locator": "Page 1 soil row",
        "exact_source_quote": "Soil extract (see medium 80) 500.0 ml",
        "snapshot_sha256": "d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e",
        "parsed_text_sha256": "e3c099476e3bdca66a5f769de65059e326598eeb3cc850c5a0830359d7a27412",
        "accessed_at": "2026-10-21T20:56:16.901317Z"
      },
      {
        "source_key": "mediadive675Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/675",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Soil extract\",\n                        \"compound_id\": 180,\n                        \"attribute\": \"\",\n                        \"amount\": 500,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "731589616c8a992664a6290b18db5dfb4bde2c843df1b7a0cf8bef7065f7632e",
        "accessed_at": "2026-10-07T12:17:23.420492+00:00"
      }
    ],
    "proposed_source_representation": {
      "amount_mL": 500,
      "amount_L": 0.5,
      "stage": "prepared liquid soil extract added to main batch"
    },
    "rationale": "500 G_PER_L is a mass/volume substitution in every local layer. Represent the literal liquid dose and delegated preparation without treating extract as 500 g of soil or a chemically defined solute."
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Main water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz675",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf",
        "source_locator": "Page 1 water row",
        "exact_source_quote": "Distilled water 500.0 ml",
        "snapshot_sha256": "d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e",
        "parsed_text_sha256": "e3c099476e3bdca66a5f769de65059e326598eeb3cc850c5a0830359d7a27412",
        "accessed_at": "2026-10-21T20:56:16.901317Z"
      },
      {
        "source_key": "mediadive675Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/675",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 500,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "731589616c8a992664a6290b18db5dfb4bde2c843df1b7a0cf8bef7065f7632e",
        "accessed_at": "2026-10-07T12:17:23.420492+00:00"
      }
    ],
    "proposed_source_representation": {
      "amount_mL": 500,
      "stage": "main batch water"
    },
    "rationale": "The fourth ingredient is absent in all three layers. This water is separate from the extraction water used to prepare soil extract."
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Main volume basis",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "Basis clarification, not another dose."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "Basis clarification, not another dose."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "Basis clarification, not another dose."
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive675Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/675",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "731589616c8a992664a6290b18db5dfb4bde2c843df1b7a0cf8bef7065f7632e",
        "accessed_at": "2026-10-07T12:17:23.420492+00:00"
      }
    ],
    "proposed_source_representation": {
      "provider_declared_mL": 1000,
      "sum_listed_liquid_inputs_mL": 1000,
      "independently_measured_final_volume": null
    },
    "rationale": "Keep the authenticated provider denominator separate from the arithmetic sum of 500 mL soil extract plus 500 mL water. Do not infer an independent measured final volume."
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Receiving pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 5.6,
          "max": 5.8
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 5.6,
          "max": 5.8
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 5.6,
          "max": 5.8
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH between 5.6 - 5.8.",
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz675",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf",
        "source_locator": "Page 1 final line",
        "exact_source_quote": "Adjust pH between 5.6 - 5.8.",
        "snapshot_sha256": "d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e",
        "parsed_text_sha256": "e3c099476e3bdca66a5f769de65059e326598eeb3cc850c5a0830359d7a27412",
        "accessed_at": "2026-10-21T20:56:16.901317Z"
      }
    ],
    "proposed_source_representation": {
      "range": [
        5.6,
        5.8
      ],
      "stage": "receiving medium"
    },
    "rationale": "The range is correct and the DSMZ owner retains the adjustment instruction. Do not transfer parent DSMZ 80 pH 7."
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Air-dried garden-soil input",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Soil extract is prepared by sieving air dried garden soil through a coarse sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one hour. After the mixture is cool and settled, the supernatant is carefully decanted, filtered through paper, autoclaved in 200 ml quantities, and stored at room temperature until cleared by sedimentation.",
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/glycerol_soil_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.0. Soil extract is prepared by sieving air dried garden soil through a coarse sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one hour. After the mixture is cool and settled, the supernatant is carefully decanted, filtered through paper, autoclaved in 200 ml quantities, and stored at room temperature until cleared by sedimentation.",
        "decision": "evidence_only",
        "rationale": "Only the soil-extraction sentences transfer; initial parent pH clause excluded."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz80",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf",
        "source_locator": "Page 1 soil-extraction paragraph",
        "exact_source_quote": "autoclaving 400 g",
        "snapshot_sha256": "908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5",
        "parsed_text_sha256": "84d1313331e12b5a3c6e3a21ba2d5493b85fa6120cd844a933c1c2bc4ccf78ce",
        "accessed_at": "2026-10-21T20:57:44.228195Z"
      }
    ],
    "proposed_source_representation": {
      "soil_input_g": 400,
      "soil_condition": "air-dried, coarse sieved",
      "stage": "soil-extract preparation"
    },
    "rationale": "Preserve the DSMZ owner’s existing exact procedure, attach stage-specific evidence and restore missing procedure in target/KOMODO. Soil input loading is not dissolved nutrient concentration or a measured stock final volume; decant/filter after cooling and settling before aliquot autoclaving."
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Extraction water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Soil extract is prepared by sieving air dried garden soil through a coarse sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one hour. After the mixture is cool and settled, the supernatant is carefully decanted, filtered through paper, autoclaved in 200 ml quantities, and stored at room temperature until cleared by sedimentation.",
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/glycerol_soil_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.0. Soil extract is prepared by sieving air dried garden soil through a coarse sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one hour. After the mixture is cool and settled, the supernatant is carefully decanted, filtered through paper, autoclaved in 200 ml quantities, and stored at room temperature until cleared by sedimentation.",
        "decision": "evidence_only",
        "rationale": "Only the soil-extraction sentences transfer; initial parent pH clause excluded."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz80",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf",
        "source_locator": "Page 1 soil-extraction paragraph",
        "exact_source_quote": "960 ml of distilled water",
        "snapshot_sha256": "908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5",
        "parsed_text_sha256": "84d1313331e12b5a3c6e3a21ba2d5493b85fa6120cd844a933c1c2bc4ccf78ce",
        "accessed_at": "2026-10-21T20:57:44.228195Z"
      }
    ],
    "proposed_source_representation": {
      "water_input_mL": 960,
      "stage": "soil-extract preparation"
    },
    "rationale": "Preserve the DSMZ owner’s existing exact procedure, attach stage-specific evidence and restore missing procedure in target/KOMODO. Soil input loading is not dissolved nutrient concentration or a measured stock final volume; decant/filter after cooling and settling before aliquot autoclaving."
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Extraction autoclave temperature",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Soil extract is prepared by sieving air dried garden soil through a coarse sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one hour. After the mixture is cool and settled, the supernatant is carefully decanted, filtered through paper, autoclaved in 200 ml quantities, and stored at room temperature until cleared by sedimentation.",
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/glycerol_soil_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.0. Soil extract is prepared by sieving air dried garden soil through a coarse sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one hour. After the mixture is cool and settled, the supernatant is carefully decanted, filtered through paper, autoclaved in 200 ml quantities, and stored at room temperature until cleared by sedimentation.",
        "decision": "evidence_only",
        "rationale": "Only the soil-extraction sentences transfer; initial parent pH clause excluded."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz80",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf",
        "source_locator": "Page 1 soil-extraction paragraph",
        "exact_source_quote": "at 121 C",
        "snapshot_sha256": "908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5",
        "parsed_text_sha256": "84d1313331e12b5a3c6e3a21ba2d5493b85fa6120cd844a933c1c2bc4ccf78ce",
        "accessed_at": "2026-10-21T20:57:44.228195Z"
      }
    ],
    "proposed_source_representation": {
      "temperature_C": 121,
      "stage": "soil-extract preparation"
    },
    "rationale": "Preserve the DSMZ owner’s existing exact procedure, attach stage-specific evidence and restore missing procedure in target/KOMODO. Soil input loading is not dissolved nutrient concentration or a measured stock final volume; decant/filter after cooling and settling before aliquot autoclaving."
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Extraction autoclave duration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Soil extract is prepared by sieving air dried garden soil through a coarse sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one hour. After the mixture is cool and settled, the supernatant is carefully decanted, filtered through paper, autoclaved in 200 ml quantities, and stored at room temperature until cleared by sedimentation.",
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/glycerol_soil_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.0. Soil extract is prepared by sieving air dried garden soil through a coarse sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one hour. After the mixture is cool and settled, the supernatant is carefully decanted, filtered through paper, autoclaved in 200 ml quantities, and stored at room temperature until cleared by sedimentation.",
        "decision": "evidence_only",
        "rationale": "Only the soil-extraction sentences transfer; initial parent pH clause excluded."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz80",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf",
        "source_locator": "Page 1 soil-extraction paragraph",
        "exact_source_quote": "for one hour.",
        "snapshot_sha256": "908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5",
        "parsed_text_sha256": "84d1313331e12b5a3c6e3a21ba2d5493b85fa6120cd844a933c1c2bc4ccf78ce",
        "accessed_at": "2026-10-21T20:57:44.228195Z"
      }
    ],
    "proposed_source_representation": {
      "duration_h": 1,
      "stage": "soil-extract preparation"
    },
    "rationale": "Preserve the DSMZ owner’s existing exact procedure, attach stage-specific evidence and restore missing procedure in target/KOMODO. Soil input loading is not dissolved nutrient concentration or a measured stock final volume; decant/filter after cooling and settling before aliquot autoclaving."
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Separated-extract autoclave aliquots",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Soil extract is prepared by sieving air dried garden soil through a coarse sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one hour. After the mixture is cool and settled, the supernatant is carefully decanted, filtered through paper, autoclaved in 200 ml quantities, and stored at room temperature until cleared by sedimentation.",
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/glycerol_soil_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.0. Soil extract is prepared by sieving air dried garden soil through a coarse sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one hour. After the mixture is cool and settled, the supernatant is carefully decanted, filtered through paper, autoclaved in 200 ml quantities, and stored at room temperature until cleared by sedimentation.",
        "decision": "evidence_only",
        "rationale": "Only the soil-extraction sentences transfer; initial parent pH clause excluded."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz80",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf",
        "source_locator": "Page 1 soil-extraction paragraph",
        "exact_source_quote": "autoclaved in 200 ml quantities",
        "snapshot_sha256": "908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5",
        "parsed_text_sha256": "84d1313331e12b5a3c6e3a21ba2d5493b85fa6120cd844a933c1c2bc4ccf78ce",
        "accessed_at": "2026-10-21T20:57:44.228195Z"
      }
    ],
    "proposed_source_representation": {
      "aliquot_mL": 200,
      "stage": "soil-extract preparation"
    },
    "rationale": "Preserve the DSMZ owner’s existing exact procedure, attach stage-specific evidence and restore missing procedure in target/KOMODO. Soil input loading is not dissolved nutrient concentration or a measured stock final volume; decant/filter after cooling and settling before aliquot autoclaving."
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Room-temperature storage and second autoclave cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Soil extract is prepared by sieving air dried garden soil through a coarse sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one hour. After the mixture is cool and settled, the supernatant is carefully decanted, filtered through paper, autoclaved in 200 ml quantities, and stored at room temperature until cleared by sedimentation.",
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/glycerol_soil_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.0. Soil extract is prepared by sieving air dried garden soil through a coarse sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one hour. After the mixture is cool and settled, the supernatant is carefully decanted, filtered through paper, autoclaved in 200 ml quantities, and stored at room temperature until cleared by sedimentation.",
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz80",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf",
        "source_locator": "Page 1 end of soil paragraph",
        "exact_source_quote": "stored at room temperature until",
        "snapshot_sha256": "908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5",
        "parsed_text_sha256": "84d1313331e12b5a3c6e3a21ba2d5493b85fa6120cd844a933c1c2bc4ccf78ce",
        "accessed_at": "2026-10-21T20:57:44.228195Z"
      }
    ],
    "proposed_source_representation": {
      "storage": "room temperature until cleared by sedimentation",
      "storage_numeric_C": null,
      "second_autoclave_duration_min": null,
      "second_autoclave_temperature_C": null
    },
    "rationale": "Do not turn room temperature into an invented numeric value or silently reuse the first extraction cycle for the second autoclaving step."
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Receiving-medium sterilization cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
        "field_path": "sterilization",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
        "field_path": "sterilization",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz675",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf",
        "source_locator": "Entire page ends with receiving pH; no receiving cycle",
        "exact_source_quote": "Adjust pH between 5.6 - 5.8.",
        "snapshot_sha256": "d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e",
        "parsed_text_sha256": "e3c099476e3bdca66a5f769de65059e326598eeb3cc850c5a0830359d7a27412",
        "accessed_at": "2026-10-21T20:56:16.901317Z"
      }
    ],
    "proposed_source_representation": {
      "receiving_cycle": null
    },
    "rationale": "The explicitly quantified 121 °C/one-hour operation belongs to soil extraction, not a generic final-medium cycle. Missing receiving cycle remains a preparation gap; no default cycle is invented."
  }
]

## Findings

### f1: Soil-extract volume is stored as mass concentration and main water is absent

blocker / open / confirmed; issue key: culturemech.006271.soil-dose-water.

Every target/owner soil field is 500 G_PER_L; source requires 500 mL liquid extract plus 500 mL distilled water. This changes both unit meaning and complete recipe representation.

### f2: Generated and KOMODO layers omit the delegated soil procedure

major / open / confirmed; issue key: culturemech.006271.soil-stage-preparation.

The maintained DSMZ owner retains the soil-extraction paragraph, while generated/KOMODO layers lack it. Extraction heat/duration and aliquot stages must not be mistaken for final-medium sterilization.

### f3: Stored graph match lacks exact supporting graph evidence

major / open / confirmed; issue key: culturemech.006271.graph-correspondence.

mediadive.medium:74 is present in all layers, but its exact graph identity/ingredient edges cannot be verified from the bound evidence. It is not confirmed incorrect solely because the primary accession is 675.

### f4: Generated terms and current canonical-label metadata need reconciliation

minor / open / confirmed; issue key: culturemech.006271.grounding-history.

Owner yeast/soil IDs are present but labels differ only in case; generated target lacks those later terms. Malformed and timezone-absent historical timestamps remain explicit. These observations do not justify changing mixture identity or inventing old times.

## Recommended Actions And Acceptance Checks

### a1

Correct both maintained owners to the exact liquid soil dose and add main water with source-stage evidence, preserving yeast/NaCl amounts and extraction provenance before separately authorized regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve existing DSMZ procedure, model the delegated extract stage and attach exact evidence in missing layers. Keep parent main recipe and pH excluded; retain unquantified final-medium sterilization rather than inventing a cycle.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retrieve the exact graph release/node/edges and matching provenance in separately authorized follow-up; retain uncertainty until then without substituting a guessed graph ID.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Canonicalize demonstrated owner labels, retain exact supported identities and reconcile stale generated fields after authorized owner fixes. Append honest provenance clarification without rewriting historical timestamps.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch039/384/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch039/384/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml:1:id: CultureMech:006271<br>./data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml:1:id: CultureMech:006271<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch039/source-preflight-bound/384/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 15 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| soil-parent | data/normalized_yaml/bacterial/glycerol_soil_medium.yaml; Entire DSMZ 80 owner read; only soil-preparation paragraph transferred | context_only | Parent main ingredients, pH 7, 150 mL soil dose and four attached main-amount claims are excluded. The indexed preparation field is retained solely to locate the shared soil procedure. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf; Entire one-page formula and pH | supports | Four printed inputs, exact liquid soil dose and receiving pH. |
| soil-primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf; Soil extract is prepared paragraph only | supports | Source-only soil loading, extraction water, heat stage, separation and final aliquots. Parent receiving formula and pH do not transfer. |
| historical-api | https://mediadive.dsmz.de/rest/medium/675; $.data.medium and $.data.solutions[0]; embedded parent $[40].source_raw | supports | Exact original October 7 response bytes recovered from a pinned repository report; original access time and hash retained, independent of present-day failed requests. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact accession 675 row | supports | KOMODO source identity and catalog metadata only. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch039/384/grounding-inventory.json; Exact local term/history slots and bound source authentication ledger | context_only | Complete exact-field inventory; current metadata, historical evidence and source forms remain distinct. |
| history-inventory | /private/tmp/culturemech-review-work-batch039/384/history-inventory.json; Exact local term/history slots and bound source authentication ledger | context_only | Complete exact-field inventory; current metadata, historical evidence and source forms remain distinct. |
| chebi17754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17754; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| foodon03302088 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03302088; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| micro0000178 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| micro0000457 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000457; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact pinned current CHEBI preferred-key rows; metadata source commit/hash | context_only | {"CHEBI:17754": [{"label": "Glycerol", "match_type": "preferred_term", "identifier": "CHEBI:17754", "preferred_term": "Glycerol", "ontology_id": "CHEBI:17754", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| writer-0 | scripts/repair_bacterial_score10_exact_terms_batch2.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Exact-ID/signature guarded term repair writes the owner FOODON/MICRO labels but preserves amounts. Current graph matching considers CHEBI/FOODON sets without concentrations and is not an exact graph snapshot verification. Current formulation-aware merger guards incompatible content; generated missing September term additions are a stale-layer observation, not an unconditional attribution to today’s merger. |
| writer-1 | scripts/repair_komodo_score10_exact_terms_batch2.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Exact-ID/signature guarded term repair writes the owner FOODON/MICRO labels but preserves amounts. Current graph matching considers CHEBI/FOODON sets without concentrations and is not an exact graph snapshot verification. Current formulation-aware merger guards incompatible content; generated missing September term additions are a stale-layer observation, not an unconditional attribution to today’s merger. |
| writer-2 | scripts/repair_bacterial_score10_exact_terms_batch3.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Exact-ID/signature guarded term repair writes the owner FOODON/MICRO labels but preserves amounts. Current graph matching considers CHEBI/FOODON sets without concentrations and is not an exact graph snapshot verification. Current formulation-aware merger guards incompatible content; generated missing September term additions are a stale-layer observation, not an unconditional attribution to today’s merger. |
| writer-3 | scripts/enrich_with_kg_microbe_matches.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Exact-ID/signature guarded term repair writes the owner FOODON/MICRO labels but preserves amounts. Current graph matching considers CHEBI/FOODON sets without concentrations and is not an exact graph snapshot verification. Current formulation-aware merger guards incompatible content; generated missing September term additions are a stale-layer observation, not an unconditional attribution to today’s merger. |
| writer-4 | src/culturemech/match/kg_media_matcher.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Exact-ID/signature guarded term repair writes the owner FOODON/MICRO labels but preserves amounts. Current graph matching considers CHEBI/FOODON sets without concentrations and is not an exact graph snapshot verification. Current formulation-aware merger guards incompatible content; generated missing September term additions are a stale-layer observation, not an unconditional attribution to today’s merger. |
| writer-5 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Exact-ID/signature guarded term repair writes the owner FOODON/MICRO labels but preserves amounts. Current graph matching considers CHEBI/FOODON sets without concentrations and is not an exact graph snapshot verification. Current formulation-aware merger guards incompatible content; generated missing September term additions are a stale-layer observation, not an unconditional attribution to today’s merger. |
| history-metadata | data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml; data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:56.209878"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:56.209878"}]}, {"input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml", "events": 8, "timestamp_issues": []}] |
| mediadive675api-attempt | https://mediadive.dsmz.de/rest/medium/675; Preserved exact public retrieval result | context_only | Optional current access failure mediadive675api preserved separately; exact primary and recovered receiving raw remain available. |
| mediadive675api_retry-attempt | https://mediadive.dsmz.de/rest/medium/675; Preserved exact public retrieval result | context_only | Optional current access failure mediadive675api_retry preserved separately; exact primary and recovered receiving raw remain available. |
| mediadive80api-attempt | https://mediadive.dsmz.de/rest/medium/80; Preserved exact public retrieval result | context_only | Optional current access failure mediadive80api preserved separately; exact primary and recovered receiving raw remain available. |
| komodo675detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=675; Preserved exact public retrieval result | context_only | Optional current access failure komodo675detail preserved separately; exact primary and recovered receiving raw remain available. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch039/384/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Optional current access failure mediadive675api preserved separately; exact primary and recovered receiving raw remain available.
- Optional current access failure mediadive675api_retry preserved separately; exact primary and recovered receiving raw remain available.
- Optional current access failure mediadive80api preserved separately; exact primary and recovered receiving raw remain available.
- Optional current access failure komodo675detail preserved separately; exact primary and recovered receiving raw remain available.
- Partial coverage is limited by the required exact KG-Microbe correspondence check, not optional provider failures or historical receiving raw authentication, which succeeded. No graph or source network call was made during drafting.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T220736Z-culturemech-006271-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bacillus_thermantarcticus_medium (CultureMech:006271)'
started_at: '2026-10-21T21:51:51Z'
finished_at: '2026-10-21T22:07:36Z'
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
summary: DSMZ 675 uses 500 mL soil extract and 500 mL water, not 500 g/L soil extract.
  Both maintained owners and the generated target retain the wrong soil unit; the
  DSMZ owner already preserves the delegated soil-extraction procedure. Its two attached
  amount claims are authenticated by recovered historical raw. Exact KG-Microbe medium
  74 correspondence remains unavailable.
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
  - path: data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml
    sha256: e90aee23573594893e409e227afc3e6258e39ddda216460d16c292cda879e2ce
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml
    sha256: 7dca8eccec3b725a1b5f8ca13e1df16246c3d1a26b6cb9151522f00d48040349
    role: context
  - path: data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml
    sha256: cce8ce725f156beb56aa2f3b97c6091ef65a47c29e341319cc7a6f97920eafa1
    role: context
  - path: data/normalized_yaml/bacterial/glycerol_soil_medium.yaml
    sha256: ea2fa6066028bff7a4b1c655560308d9c6fcba95b01c020368fdc84840bae029
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json
    sha256: 65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
    sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml.md
    sha256: 213c8c2e077a2d1d58689937e8e0ea3cad04b12040b4b6c36c14d494cb1a1f70
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/bacillus_thermantarcticus_medium.yaml.md
    sha256: 124331ec024892dbdee4a1bddb70f406cffc090c1ee45bf201b6631368d7a721
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
  - path: scripts/repair_bacterial_score10_exact_terms_batch2.py
    sha256: b598b051c7cbec73cb52d49e116d8d1c33c052e3d9cf74877041ce1e58a16a44
    role: context
  - path: scripts/repair_bacterial_score10_exact_terms_batch3.py
    sha256: 66332e39cabad33e5188b914fe048057f0106028e9e953ac1e80ed5a084c04f6
    role: context
  - path: scripts/repair_komodo_score10_exact_terms_batch2.py
    sha256: 4e078f461180d01acfc85326a136ba3b984453918b0492d796b763e15ac677e5
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
  - path: src/culturemech/match/kg_media_matcher.py
    sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
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
  selection: Task review 384; batch 039 item 4 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-eight task batches
    contain 380 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 383 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006271
targets:
- target_id: CultureMech:006271
  path: data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml
  label: bacillus_thermantarcticus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch039/384/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch039/384/strict.tsv"
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006271
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
  - CultureMech:006271
- check_id: mediadive675api-source-access
  name: 'Exact source content access: mediadive675api'
  required: false
  status: unavailable
  summary: Optional current access failure mediadive675api preserved separately; exact
    primary and recovered receiving raw remain available.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - mediadive675api-attempt
- check_id: mediadive675api_retry-source-access
  name: 'Exact source content access: mediadive675api_retry'
  required: false
  status: unavailable
  summary: Optional current access failure mediadive675api_retry preserved separately;
    exact primary and recovered receiving raw remain available.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - mediadive675api_retry-attempt
- check_id: mediadive80api-source-access
  name: 'Exact source content access: mediadive80api'
  required: false
  status: unavailable
  summary: Optional current access failure mediadive80api preserved separately; exact
    primary and recovered receiving raw remain available.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - mediadive80api-attempt
- check_id: komodo675detail-source-access
  name: 'Exact source content access: komodo675detail'
  required: false
  status: unavailable
  summary: Optional current access failure komodo675detail preserved separately; exact
    primary and recovered receiving raw remain available.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - komodo675detail-attempt
- check_id: exact-graph74
  name: Required exact KG-Microbe medium 74 correspondence
  required: true
  status: unavailable
  summary: Bound source/input inventory contains no exact graph node/edge snapshot
    establishing the stored mediadive.medium:74 match. Source accession, ingredient
    names and code inspection cannot substitute for graph correspondence. No universal
    external graph absence is claimed.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - grounding-inventory
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:20.787708Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch039/384/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:21.848543Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch039/384/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:23.024129Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:23.767948Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T22:03:02Z'
  support: supports
  summary: './data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml:1:id: CultureMech:006271

    ./data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml:1:id:
    CultureMech:006271

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/source-preflight-bound/384/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T22:03:02Z'
  support: supports
  summary: 15 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: f56c04b830886327437b87f0448dcdb3032a6b48de296dfe65335ec945d1339c
- evidence_id: soil-parent
  kind: record_content
  reference: data/normalized_yaml/bacterial/glycerol_soil_medium.yaml
  locator: Entire DSMZ 80 owner read; only soil-preparation paragraph transferred
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Parent main ingredients, pH 7, 150 mL soil dose and four attached main-amount
    claims are excluded. The indexed preparation field is retained solely to locate
    the shared soil procedure.
  snapshot_sha256: ea2fa6066028bff7a4b1c655560308d9c6fcba95b01c020368fdc84840bae029
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf
  locator: Entire one-page formula and pH
  accessed_at: '2026-10-21T20:56:16.901317Z'
  support: supports
  summary: Four printed inputs, exact liquid soil dose and receiving pH.
  quote: Soil extract (see medium 80) 500.0 ml
  snapshot_sha256: d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e
- evidence_id: soil-primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf
  locator: Soil extract is prepared paragraph only
  accessed_at: '2026-10-21T20:57:44.228195Z'
  support: supports
  summary: Source-only soil loading, extraction water, heat stage, separation and
    final aliquots. Parent receiving formula and pH do not transfer.
  quote: coarse sieve and autoclaving 400 g with 960 ml of distilled water
  snapshot_sha256: 908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5
- evidence_id: historical-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/675
  locator: $.data.medium and $.data.solutions[0]; embedded parent $[40].source_raw
  accessed_at: '2026-10-07T12:17:23.420492Z'
  support: supports
  summary: Exact original October 7 response bytes recovered from a pinned repository
    report; original access time and hash retained, independent of present-day failed
    requests.
  snapshot_sha256: 731589616c8a992664a6290b18db5dfb4bde2c843df1b7a0cf8bef7065f7632e
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact accession 675 row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: KOMODO source identity and catalog metadata only.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=675'\
    \ >675</a></TD>\n\t\t\t\t\t<TD>BACILLUS THERMANTARCTICUS medium</TD>\n\t\t\t\t\
    \t<TD> 5.6 - 5.8</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\
    \t\t\t<TD>false</TD>\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf</a></TD>\n\t\
    \t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/384/grounding-inventory.json
  locator: Exact local term/history slots and bound source authentication ledger
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Complete exact-field inventory; current metadata, historical evidence and
    source forms remain distinct.
  snapshot_sha256: 16f65fda5940a1a84add52adc012bc84ada9ca4cc65cfd49b58066923302d78d
- evidence_id: history-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/384/history-inventory.json
  locator: Exact local term/history slots and bound source authentication ledger
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Complete exact-field inventory; current metadata, historical evidence and
    source forms remain distinct.
  snapshot_sha256: 2382a63f7e2ffca0de38573a8892b51a919e2dc4ed5905acdee1e847f1efd340
- evidence_id: chebi17754
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17754
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:42:35.442871Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 0231975176416cbaad3ad04c9efeedbe9bef0b826645e592a4a2f511e8d1db95
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: foodon03302088
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03302088
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:00:49.378816Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: ee2e9f57bae58d8170d339f9a0575ea59cda36ff7c8a09fcf457358dcc894f22
- evidence_id: foodon03315426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:00:49.388263Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: micro0000178
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:00:49.423450Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: ef45aa186438f91d015280171fde8ccb25740a50cc6f2c6e848de6aad3339b31
- evidence_id: micro0000457
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000457
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T20:56:17.417821Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: d143920489595a6739ea637d7d46fa0323c7dda535e73dc4d31684ec39469859
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact pinned current CHEBI preferred-key rows; metadata source commit/hash
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: '{"CHEBI:17754": [{"label": "Glycerol", "match_type": "preferred_term",
    "identifier": "CHEBI:17754", "preferred_term": "Glycerol", "ontology_id": "CHEBI:17754",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label":
    "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term":
    "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_bacterial_score10_exact_terms_batch2.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Exact-ID/signature guarded term repair writes the owner FOODON/MICRO labels
    but preserves amounts. Current graph matching considers CHEBI/FOODON sets without
    concentrations and is not an exact graph snapshot verification. Current formulation-aware
    merger guards incompatible content; generated missing September term additions
    are a stale-layer observation, not an unconditional attribution to today’s merger.
  snapshot_sha256: b598b051c7cbec73cb52d49e116d8d1c33c052e3d9cf74877041ce1e58a16a44
- evidence_id: writer-1
  kind: record_content
  reference: scripts/repair_komodo_score10_exact_terms_batch2.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Exact-ID/signature guarded term repair writes the owner FOODON/MICRO labels
    but preserves amounts. Current graph matching considers CHEBI/FOODON sets without
    concentrations and is not an exact graph snapshot verification. Current formulation-aware
    merger guards incompatible content; generated missing September term additions
    are a stale-layer observation, not an unconditional attribution to today’s merger.
  snapshot_sha256: 4e078f461180d01acfc85326a136ba3b984453918b0492d796b763e15ac677e5
- evidence_id: writer-2
  kind: record_content
  reference: scripts/repair_bacterial_score10_exact_terms_batch3.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Exact-ID/signature guarded term repair writes the owner FOODON/MICRO labels
    but preserves amounts. Current graph matching considers CHEBI/FOODON sets without
    concentrations and is not an exact graph snapshot verification. Current formulation-aware
    merger guards incompatible content; generated missing September term additions
    are a stale-layer observation, not an unconditional attribution to today’s merger.
  snapshot_sha256: 66332e39cabad33e5188b914fe048057f0106028e9e953ac1e80ed5a084c04f6
- evidence_id: writer-3
  kind: record_content
  reference: scripts/enrich_with_kg_microbe_matches.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Exact-ID/signature guarded term repair writes the owner FOODON/MICRO labels
    but preserves amounts. Current graph matching considers CHEBI/FOODON sets without
    concentrations and is not an exact graph snapshot verification. Current formulation-aware
    merger guards incompatible content; generated missing September term additions
    are a stale-layer observation, not an unconditional attribution to today’s merger.
  snapshot_sha256: 61351f99ef2cb0cef03e74ad92d21dcf3b38df77a06602bdac814974e7728eeb
- evidence_id: writer-4
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Exact-ID/signature guarded term repair writes the owner FOODON/MICRO labels
    but preserves amounts. Current graph matching considers CHEBI/FOODON sets without
    concentrations and is not an exact graph snapshot verification. Current formulation-aware
    merger guards incompatible content; generated missing September term additions
    are a stale-layer observation, not an unconditional attribution to today’s merger.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
- evidence_id: writer-5
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Exact-ID/signature guarded term repair writes the owner FOODON/MICRO labels
    but preserves amounts. Current graph matching considers CHEBI/FOODON sets without
    concentrations and is not an exact graph snapshot verification. Current formulation-aware
    merger guards incompatible content; generated missing September term additions
    are a stale-layer observation, not an unconditional attribution to today’s merger.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml;
    data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:56.209878"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:56.209878"}]}, {"input": "data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml",
    "events": 8, "timestamp_issues": []}]'
- evidence_id: mediadive675api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/675
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:56:15.648819Z'
  support: context_only
  summary: Optional current access failure mediadive675api preserved separately; exact
    primary and recovered receiving raw remain available.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive675api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/675
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:57:45.210421Z'
  support: context_only
  summary: Optional current access failure mediadive675api_retry preserved separately;
    exact primary and recovered receiving raw remain available.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive80api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/80
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:57:44.228518Z'
  support: context_only
  summary: Optional current access failure mediadive80api preserved separately; exact
    primary and recovered receiving raw remain available.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo675detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=675
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:56:14.547409Z'
  support: context_only
  summary: Optional current access failure komodo675detail preserved separately; exact
    primary and recovered receiving raw remain available.
  snapshot_sha256: 85a11f38fa18fcf7bd34d848c7f2f11992ebdc017cedc29128468a936c395132
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/384/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T22:03:02Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 91c60fe826c897187888a99d22e9f58a000f632a369f9eb3b4daa71fa6c9d56b
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact DSMZ/KOMODO recipient and soil dependency
  outcome: supported
  summary: CultureMech:006271 is the KOMODO/generated target, CultureMech:001815 the
    maintained DSMZ 675 source. Source-duplicate links resolve to these exact owners.
    DSMZ 80 is only the named soil-extract preparation dependency, not an alternative
    full recipe. The medium title does not establish a strain growth assertion.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - id-search
  - primary
  - historical-api
  - catalog
  - soil-parent
  - soil-primary
- assessment_id: formulation
  area: quantity
  topic: Liquid extract and main water recovery
  outcome: concern
  summary: All three layers store soil extract as 500 G_PER_L despite exact current
    primary and authenticated historical source specifying 500 mL. All omit the separate
    500 mL main water. Two mass rates have authentic attached evidence only on the
    DSMZ owner. Listed liquids sum to 1000 mL and provider declares 1000 mL; those
    are distinct evidence bases from a measured final volume.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - primary
  - historical-api
  - quantity-inventory
- assessment_id: preparation
  area: completeness
  topic: Preserved owner procedure and excluded parent conditions
  outcome: concern
  summary: 'The DSMZ owner already retains soil extraction: 400 g sieved air-dried
    soil with 960 mL water, 121 °C for one hour, cool/settle/decant/filter, then autoclave
    200 mL aliquots and store at room temperature until clear. Target/KOMODO omit
    this procedure. Quantified extraction conditions must remain in the extract stage.
    DSMZ 80 main peptone, beef extract, glycerol, agar, 150 mL extract dose and pH
    7 are excluded, as are its four historical amount claims.'
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - owner-1
  - soil-primary
  - soil-parent
  - quantity-inventory
- assessment_id: grounding
  area: grounding
  topic: Current label and secondary correspondence
  outcome: concern
  summary: Target primary-term coverage is 1/3 ingredients, while both owners have
    3/3 primary terms; target CHEBI-based secondary coverage is 1/3. These fractions
    describe slots, not correctness or a requirement to assign pure-compound CHEBI
    IDs to mixtures. Exact current NaCl secondary key is supported. Owners’ Yeast
    extract and Soil extract labels differ by case from pinned FOODON/MICRO canonical
    labels; target lacks those later assertions. Parent-only label discrepancies do
    not transfer.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - grounding-inventory
  - mim
  - foodon03315426
  - micro0000457
  - chebi26710
- assessment_id: history-authentication
  area: evidence
  topic: Recovered exact historical receiving source
  outcome: supported
  summary: Two DSMZ-owner amount claims match exact recovered raw 731589616c… and
    original October 7 access metadata. The embedded parent source_raw locator and
    extraction provenance are pinned in the bound catalog. Present-day 503 responses
    are separate attempts and do not negate the authenticated historical claim. The
    parent’s four main-formula objects are outside scope; their derivative status
    is retained without importing them.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - history-inventory
  - historical-api
  - primary
  - soil-primary
- assessment_id: graph
  area: graph
  topic: KG-Microbe identity remains unconfirmed
  outcome: unknown
  summary: All three layers assert mediadive.medium:74. The source identity is DSMZ
    675, but differing identifiers alone do not prove a graph error. The relevant
    exact graph node/edges are not available in the bound evidence. Current matching
    code uses CHEBI/FOODON ingredient sets and ignores concentration; it also omits
    MICRO terms, so a code read or source formulation cannot authenticate the stored
    graph match.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - grounding-inventory
- assessment_id: classification-growth
  area: scope
  topic: Undefined liquid mixture and catalog oxygen
  outcome: supported
  summary: 'COMPLEX/UNDEFINED/LIQUID accords with yeast extract and soil-water extract
    without agar in DSMZ 675. Catalog Aerobic: No is retained as provenance only;
    it does not supply a demonstrated gas regime. No generic temperature, target organism
    or parent growth condition is added.'
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - primary
  - catalog
  - foodon03315426
  - micro0000457
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 25 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 13 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006271
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Yeast extract\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"rationale\": \"Existing exact\
    \ snippet and cited raw hash authenticated.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz675\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf\",\n        \"\
    source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\": \"Yeast\
    \ extract 6.0 g\",\n        \"snapshot_sha256\": \"d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e\"\
    ,\n        \"parsed_text_sha256\": \"e3c099476e3bdca66a5f769de65059e326598eeb3cc850c5a0830359d7a27412\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.901317Z\"\n      },\n      {\n\
    \        \"source_key\": \"mediadive675Historical\",\n        \"source_url\":\
    \ \"https://mediadive.dsmz.de/rest/medium/675\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 6,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 6,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"731589616c8a992664a6290b18db5dfb4bde2c843df1b7a0cf8bef7065f7632e\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:23.420492+00:00\"\n      }\n  \
    \  ],\n    \"proposed_source_representation\": {\n      \"printed_mass_g\": 6,\n\
    \      \"historical_provider_g_L\": 6,\n      \"provider_volume_mL\": 1000,\n\
    \      \"stage\": \"main recipe\"\n    },\n    \"rationale\": \"Primary batch\
    \ masses and authenticated provider rates agree. Verified applies only to the\
    \ DSMZ owner with attached matching evidence; the other layers require claim-level\
    \ support. Provider declared volume is not a measured-volume assertion.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\": \"Sodium chloride\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"rationale\": \"Existing exact\
    \ snippet and cited raw hash authenticated.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz675\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf\",\n        \"\
    source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\": \"NaCl\
    \ 3.0 g\",\n        \"snapshot_sha256\": \"d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e\"\
    ,\n        \"parsed_text_sha256\": \"e3c099476e3bdca66a5f769de65059e326598eeb3cc850c5a0830359d7a27412\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.901317Z\"\n      },\n      {\n\
    \        \"source_key\": \"mediadive675Historical\",\n        \"source_url\":\
    \ \"https://mediadive.dsmz.de/rest/medium/675\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 3,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n                  \
    \      \\\"mmol_l\\\": 51.3347,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"731589616c8a992664a6290b18db5dfb4bde2c843df1b7a0cf8bef7065f7632e\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:23.420492+00:00\"\n      }\n  \
    \  ],\n    \"proposed_source_representation\": {\n      \"printed_mass_g\": 3,\n\
    \      \"historical_provider_g_L\": 3,\n      \"provider_volume_mL\": 1000,\n\
    \      \"stage\": \"main recipe\"\n    },\n    \"rationale\": \"Primary batch\
    \ masses and authenticated provider rates agree. Verified applies only to the\
    \ DSMZ owner with attached matching evidence; the other layers require claim-level\
    \ support. Provider declared volume is not a measured-volume assertion.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\": \"Soil-extract\
    \ receiving aliquot\",\n    \"decision\": \"correct\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"500\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"500\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"500\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz675\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf\"\
    ,\n        \"source_locator\": \"Page 1 soil row\",\n        \"exact_source_quote\"\
    : \"Soil extract (see medium 80) 500.0 ml\",\n        \"snapshot_sha256\": \"\
    d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e\",\n        \"\
    parsed_text_sha256\": \"e3c099476e3bdca66a5f769de65059e326598eeb3cc850c5a0830359d7a27412\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.901317Z\"\n      },\n      {\n\
    \        \"source_key\": \"mediadive675Historical\",\n        \"source_url\":\
    \ \"https://mediadive.dsmz.de/rest/medium/675\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Soil extract\\\",\\n                        \\\"compound_id\\\
    \": 180,\\n                        \\\"attribute\\\": \\\"\\\",\\n           \
    \             \\\"amount\\\": 500,\\n                        \\\"unit\\\": \\\"\
    ml\\\",\\n                        \\\"optional\\\": 0\\n                    }\"\
    ,\n        \"snapshot_sha256\": \"731589616c8a992664a6290b18db5dfb4bde2c843df1b7a0cf8bef7065f7632e\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:23.420492+00:00\"\n      }\n  \
    \  ],\n    \"proposed_source_representation\": {\n      \"amount_mL\": 500,\n\
    \      \"amount_L\": 0.5,\n      \"stage\": \"prepared liquid soil extract added\
    \ to main batch\"\n    },\n    \"rationale\": \"500 G_PER_L is a mass/volume substitution\
    \ in every local layer. Represent the literal liquid dose and delegated preparation\
    \ without treating extract as 500 g of soil or a chemically defined solute.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\": \"Main\
    \ water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz675\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf\"\
    ,\n        \"source_locator\": \"Page 1 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 500.0 ml\",\n        \"snapshot_sha256\": \"d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e\"\
    ,\n        \"parsed_text_sha256\": \"e3c099476e3bdca66a5f769de65059e326598eeb3cc850c5a0830359d7a27412\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.901317Z\"\n      },\n      {\n\
    \        \"source_key\": \"mediadive675Historical\",\n        \"source_url\":\
    \ \"https://mediadive.dsmz.de/rest/medium/675\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 500,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"731589616c8a992664a6290b18db5dfb4bde2c843df1b7a0cf8bef7065f7632e\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:23.420492+00:00\"\n      }\n  \
    \  ],\n    \"proposed_source_representation\": {\n      \"amount_mL\": 500,\n\
    \      \"stage\": \"main batch water\"\n    },\n    \"rationale\": \"The fourth\
    \ ingredient is absent in all three layers. This water is separate from the extraction\
    \ water used to prepare soil extract.\"\n  },\n  {\n    \"quantity_id\": \"q5\"\
    ,\n    \"component_or_context\": \"Main volume basis\",\n    \"decision\": \"\
    evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"Basis clarification,\
    \ not another dose.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"Basis clarification,\
    \ not another dose.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"Basis clarification,\
    \ not another dose.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive675Historical\",\n        \"source_url\":\
    \ \"https://mediadive.dsmz.de/rest/medium/675\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 1000\",\n        \"snapshot_sha256\": \"731589616c8a992664a6290b18db5dfb4bde2c843df1b7a0cf8bef7065f7632e\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:23.420492+00:00\"\n      }\n  \
    \  ],\n    \"proposed_source_representation\": {\n      \"provider_declared_mL\"\
    : 1000,\n      \"sum_listed_liquid_inputs_mL\": 1000,\n      \"independently_measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"Keep the authenticated provider denominator\
    \ separate from the arithmetic sum of 500 mL soil extract plus 500 mL water. Do\
    \ not infer an independent measured final volume.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q6\",\n    \"component_or_context\": \"Receiving pH\",\n    \"decision\":\
    \ \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ph_range\",\n        \"stored\": {\n          \"min\": 5.6,\n          \"\
    max\": 5.8\n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 5.6,\n          \"max\": 5.8\n        },\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 5.6,\n          \"max\": 5.8\n        },\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH between 5.6 - 5.8.\",\n        \"decision\": \"evidence_only\",\n\
    \        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz675\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf\"\
    ,\n        \"source_locator\": \"Page 1 final line\",\n        \"exact_source_quote\"\
    : \"Adjust pH between 5.6 - 5.8.\",\n        \"snapshot_sha256\": \"d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e\"\
    ,\n        \"parsed_text_sha256\": \"e3c099476e3bdca66a5f769de65059e326598eeb3cc850c5a0830359d7a27412\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.901317Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"range\": [\n        5.6,\n\
    \        5.8\n      ],\n      \"stage\": \"receiving medium\"\n    },\n    \"\
    rationale\": \"The range is correct and the DSMZ owner retains the adjustment\
    \ instruction. Do not transfer parent DSMZ 80 pH 7.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q7\",\n    \"component_or_context\": \"Air-dried garden-soil input\",\n  \
    \  \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"preparation_steps\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Soil extract is prepared by sieving air dried garden soil through a coarse\
    \ sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one\
    \ hour. After the mixture is cool and settled, the supernatant is carefully decanted,\
    \ filtered through paper, autoclaved in 200 ml quantities, and stored at room\
    \ temperature until cleared by sedimentation.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/glycerol_soil_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.0. Soil extract is prepared by sieving air dried garden soil\
    \ through a coarse sieve and autoclaving 400 g with 960 ml of distilled water\
    \ at 121°C for one hour. After the mixture is cool and settled, the supernatant\
    \ is carefully decanted, filtered through paper, autoclaved in 200 ml quantities,\
    \ and stored at room temperature until cleared by sedimentation.\",\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Only the soil-extraction\
    \ sentences transfer; initial parent pH clause excluded.\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz80\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf\"\
    ,\n        \"source_locator\": \"Page 1 soil-extraction paragraph\",\n       \
    \ \"exact_source_quote\": \"autoclaving 400 g\",\n        \"snapshot_sha256\"\
    : \"908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5\",\n    \
    \    \"parsed_text_sha256\": \"84d1313331e12b5a3c6e3a21ba2d5493b85fa6120cd844a933c1c2bc4ccf78ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:57:44.228195Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"soil_input_g\": 400,\n   \
    \   \"soil_condition\": \"air-dried, coarse sieved\",\n      \"stage\": \"soil-extract\
    \ preparation\"\n    },\n    \"rationale\": \"Preserve the DSMZ owner’s existing\
    \ exact procedure, attach stage-specific evidence and restore missing procedure\
    \ in target/KOMODO. Soil input loading is not dissolved nutrient concentration\
    \ or a measured stock final volume; decant/filter after cooling and settling before\
    \ aliquot autoclaving.\"\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Extraction water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Soil extract is prepared by sieving air dried garden soil through a coarse\
    \ sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one\
    \ hour. After the mixture is cool and settled, the supernatant is carefully decanted,\
    \ filtered through paper, autoclaved in 200 ml quantities, and stored at room\
    \ temperature until cleared by sedimentation.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/glycerol_soil_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.0. Soil extract is prepared by sieving air dried garden soil\
    \ through a coarse sieve and autoclaving 400 g with 960 ml of distilled water\
    \ at 121°C for one hour. After the mixture is cool and settled, the supernatant\
    \ is carefully decanted, filtered through paper, autoclaved in 200 ml quantities,\
    \ and stored at room temperature until cleared by sedimentation.\",\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Only the soil-extraction\
    \ sentences transfer; initial parent pH clause excluded.\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz80\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf\"\
    ,\n        \"source_locator\": \"Page 1 soil-extraction paragraph\",\n       \
    \ \"exact_source_quote\": \"960 ml of distilled water\",\n        \"snapshot_sha256\"\
    : \"908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5\",\n    \
    \    \"parsed_text_sha256\": \"84d1313331e12b5a3c6e3a21ba2d5493b85fa6120cd844a933c1c2bc4ccf78ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:57:44.228195Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"water_input_mL\": 960,\n \
    \     \"stage\": \"soil-extract preparation\"\n    },\n    \"rationale\": \"Preserve\
    \ the DSMZ owner’s existing exact procedure, attach stage-specific evidence and\
    \ restore missing procedure in target/KOMODO. Soil input loading is not dissolved\
    \ nutrient concentration or a measured stock final volume; decant/filter after\
    \ cooling and settling before aliquot autoclaving.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q9\",\n    \"component_or_context\": \"Extraction autoclave temperature\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"preparation_steps\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Soil extract is prepared by sieving air dried garden soil through a coarse\
    \ sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one\
    \ hour. After the mixture is cool and settled, the supernatant is carefully decanted,\
    \ filtered through paper, autoclaved in 200 ml quantities, and stored at room\
    \ temperature until cleared by sedimentation.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/glycerol_soil_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.0. Soil extract is prepared by sieving air dried garden soil\
    \ through a coarse sieve and autoclaving 400 g with 960 ml of distilled water\
    \ at 121°C for one hour. After the mixture is cool and settled, the supernatant\
    \ is carefully decanted, filtered through paper, autoclaved in 200 ml quantities,\
    \ and stored at room temperature until cleared by sedimentation.\",\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Only the soil-extraction\
    \ sentences transfer; initial parent pH clause excluded.\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz80\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf\"\
    ,\n        \"source_locator\": \"Page 1 soil-extraction paragraph\",\n       \
    \ \"exact_source_quote\": \"at 121 C\",\n        \"snapshot_sha256\": \"908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5\"\
    ,\n        \"parsed_text_sha256\": \"84d1313331e12b5a3c6e3a21ba2d5493b85fa6120cd844a933c1c2bc4ccf78ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:57:44.228195Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"temperature_C\": 121,\n  \
    \    \"stage\": \"soil-extract preparation\"\n    },\n    \"rationale\": \"Preserve\
    \ the DSMZ owner’s existing exact procedure, attach stage-specific evidence and\
    \ restore missing procedure in target/KOMODO. Soil input loading is not dissolved\
    \ nutrient concentration or a measured stock final volume; decant/filter after\
    \ cooling and settling before aliquot autoclaving.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q10\",\n    \"component_or_context\": \"Extraction autoclave duration\",\n\
    \    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"preparation_steps\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Soil extract is prepared by sieving air dried garden soil through a coarse\
    \ sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one\
    \ hour. After the mixture is cool and settled, the supernatant is carefully decanted,\
    \ filtered through paper, autoclaved in 200 ml quantities, and stored at room\
    \ temperature until cleared by sedimentation.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/glycerol_soil_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.0. Soil extract is prepared by sieving air dried garden soil\
    \ through a coarse sieve and autoclaving 400 g with 960 ml of distilled water\
    \ at 121°C for one hour. After the mixture is cool and settled, the supernatant\
    \ is carefully decanted, filtered through paper, autoclaved in 200 ml quantities,\
    \ and stored at room temperature until cleared by sedimentation.\",\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Only the soil-extraction\
    \ sentences transfer; initial parent pH clause excluded.\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz80\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf\"\
    ,\n        \"source_locator\": \"Page 1 soil-extraction paragraph\",\n       \
    \ \"exact_source_quote\": \"for one hour.\",\n        \"snapshot_sha256\": \"\
    908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5\",\n        \"\
    parsed_text_sha256\": \"84d1313331e12b5a3c6e3a21ba2d5493b85fa6120cd844a933c1c2bc4ccf78ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:57:44.228195Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"duration_h\": 1,\n      \"\
    stage\": \"soil-extract preparation\"\n    },\n    \"rationale\": \"Preserve the\
    \ DSMZ owner’s existing exact procedure, attach stage-specific evidence and restore\
    \ missing procedure in target/KOMODO. Soil input loading is not dissolved nutrient\
    \ concentration or a measured stock final volume; decant/filter after cooling\
    \ and settling before aliquot autoclaving.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q11\",\n    \"component_or_context\": \"Separated-extract autoclave aliquots\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"preparation_steps\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Soil extract is prepared by sieving air dried garden soil through a coarse\
    \ sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one\
    \ hour. After the mixture is cool and settled, the supernatant is carefully decanted,\
    \ filtered through paper, autoclaved in 200 ml quantities, and stored at room\
    \ temperature until cleared by sedimentation.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/glycerol_soil_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.0. Soil extract is prepared by sieving air dried garden soil\
    \ through a coarse sieve and autoclaving 400 g with 960 ml of distilled water\
    \ at 121°C for one hour. After the mixture is cool and settled, the supernatant\
    \ is carefully decanted, filtered through paper, autoclaved in 200 ml quantities,\
    \ and stored at room temperature until cleared by sedimentation.\",\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Only the soil-extraction\
    \ sentences transfer; initial parent pH clause excluded.\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz80\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf\"\
    ,\n        \"source_locator\": \"Page 1 soil-extraction paragraph\",\n       \
    \ \"exact_source_quote\": \"autoclaved in 200 ml quantities\",\n        \"snapshot_sha256\"\
    : \"908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5\",\n    \
    \    \"parsed_text_sha256\": \"84d1313331e12b5a3c6e3a21ba2d5493b85fa6120cd844a933c1c2bc4ccf78ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:57:44.228195Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"aliquot_mL\": 200,\n     \
    \ \"stage\": \"soil-extract preparation\"\n    },\n    \"rationale\": \"Preserve\
    \ the DSMZ owner’s existing exact procedure, attach stage-specific evidence and\
    \ restore missing procedure in target/KOMODO. Soil input loading is not dissolved\
    \ nutrient concentration or a measured stock final volume; decant/filter after\
    \ cooling and settling before aliquot autoclaving.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q12\",\n    \"component_or_context\": \"Room-temperature storage and second\
    \ autoclave cycle\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Soil extract is prepared by sieving air dried garden soil through a coarse\
    \ sieve and autoclaving 400 g with 960 ml of distilled water at 121°C for one\
    \ hour. After the mixture is cool and settled, the supernatant is carefully decanted,\
    \ filtered through paper, autoclaved in 200 ml quantities, and stored at room\
    \ temperature until cleared by sedimentation.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/glycerol_soil_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.0. Soil extract is prepared by sieving air dried garden soil\
    \ through a coarse sieve and autoclaving 400 g with 960 ml of distilled water\
    \ at 121°C for one hour. After the mixture is cool and settled, the supernatant\
    \ is carefully decanted, filtered through paper, autoclaved in 200 ml quantities,\
    \ and stored at room temperature until cleared by sedimentation.\",\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz80\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium80.pdf\"\
    ,\n        \"source_locator\": \"Page 1 end of soil paragraph\",\n        \"exact_source_quote\"\
    : \"stored at room temperature until\",\n        \"snapshot_sha256\": \"908d0286b7f9db0e96cb539da10e185f1487360b266b95915cd4ab6f5767bdf5\"\
    ,\n        \"parsed_text_sha256\": \"84d1313331e12b5a3c6e3a21ba2d5493b85fa6120cd844a933c1c2bc4ccf78ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:57:44.228195Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"storage\": \"room temperature\
    \ until cleared by sedimentation\",\n      \"storage_numeric_C\": null,\n    \
    \  \"second_autoclave_duration_min\": null,\n      \"second_autoclave_temperature_C\"\
    : null\n    },\n    \"rationale\": \"Do not turn room temperature into an invented\
    \ numeric value or silently reuse the first extraction cycle for the second autoclaving\
    \ step.\"\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"Receiving-medium sterilization cycle\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null,\n   \
    \     \"decision\": \"not_quantified\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null,\n   \
    \     \"decision\": \"not_quantified\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null,\n   \
    \     \"decision\": \"not_quantified\",\n        \"rationale\": \"\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz675\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium675.pdf\"\
    ,\n        \"source_locator\": \"Entire page ends with receiving pH; no receiving\
    \ cycle\",\n        \"exact_source_quote\": \"Adjust pH between 5.6 - 5.8.\",\n\
    \        \"snapshot_sha256\": \"d4777c226e976d6490bbd03febbec875ed0fc8f4b3cfaa7607a01cd95b893e2e\"\
    ,\n        \"parsed_text_sha256\": \"e3c099476e3bdca66a5f769de65059e326598eeb3cc850c5a0830359d7a27412\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.901317Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"receiving_cycle\": null\n\
    \    },\n    \"rationale\": \"The explicitly quantified 121 °C/one-hour operation\
    \ belongs to soil extraction, not a generic final-medium cycle. Missing receiving\
    \ cycle remains a preparation gap; no default cycle is invented.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.006271.soil-dose-water
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Soil-extract volume is stored as mass concentration and main water is absent
  description: Every target/owner soil field is 500 G_PER_L; source requires 500 mL
    liquid extract plus 500 mL distilled water. This changes both unit meaning and
    complete recipe representation.
  target_ids:
  - CultureMech:006271
  field_paths:
  - ingredients[2].concentration
  - ingredients[3].concentration
  evidence_ids:
  - primary
  - historical-api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml
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
  issue_key: culturemech.006271.soil-stage-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated and KOMODO layers omit the delegated soil procedure
  description: The maintained DSMZ owner retains the soil-extraction paragraph, while
    generated/KOMODO layers lack it. Extraction heat/duration and aliquot stages must
    not be mistaken for final-medium sterilization.
  target_ids:
  - CultureMech:006271
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - soil-primary
  - owner-1
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml
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
  issue_key: culturemech.006271.graph-correspondence
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Stored graph match lacks exact supporting graph evidence
  description: mediadive.medium:74 is present in all layers, but its exact graph identity/ingredient
    edges cannot be verified from the bound evidence. It is not confirmed incorrect
    solely because the primary accession is 675.
  target_ids:
  - CultureMech:006271
  field_paths:
  - kg_microbe_match
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - grounding-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml
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
  issue_key: culturemech.006271.grounding-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated terms and current canonical-label metadata need reconciliation
  description: Owner yeast/soil IDs are present but labels differ only in case; generated
    target lacks those later terms. Malformed and timezone-absent historical timestamps
    remain explicit. These observations do not justify changing mixture identity or
    inventing old times.
  target_ids:
  - CultureMech:006271
  field_paths:
  - ingredients[0].term
  - ingredients[2].term
  - curation_history
  evidence_ids:
  - grounding-inventory
  - history-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml
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
  description: Correct both maintained owners to the exact liquid soil dose and add
    main water with source-stage evidence, preserving yeast/NaCl amounts and extraction
    provenance before separately authorized regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006271
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml
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
  description: Preserve existing DSMZ procedure, model the delegated extract stage
    and attach exact evidence in missing layers. Keep parent main recipe and pH excluded;
    retain unquantified final-medium sterilization rather than inventing a cycle.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006271
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml
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
  description: Retrieve the exact graph release/node/edges and matching provenance
    in separately authorized follow-up; retain uncertainty until then without substituting
    a guessed graph ID.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006271
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml
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
  description: Canonicalize demonstrated owner labels, retain exact supported identities
    and reconcile stale generated fields after authorized owner fixes. Append honest
    provenance clarification without rewriting historical timestamps.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006271
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml
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
- Optional current access failure mediadive675api preserved separately; exact primary
  and recovered receiving raw remain available.
- Optional current access failure mediadive675api_retry preserved separately; exact
  primary and recovered receiving raw remain available.
- Optional current access failure mediadive80api preserved separately; exact primary
  and recovered receiving raw remain available.
- Optional current access failure komodo675detail preserved separately; exact primary
  and recovered receiving raw remain available.
- Partial coverage is limited by the required exact KG-Microbe correspondence check,
  not optional provider failures or historical receiving raw authentication, which
  succeeded. No graph or source network call was made during drafting.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-039
- generated-medium
```
