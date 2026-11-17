# Source and formulation review: aspergillus_complete_medium (CultureMech:007742)

- Review: 20261021T201526Z-culturemech-007742-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T20:11:20Z
- Finished UTC: 2026-10-21T20:15:26Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact JCM 1134 and TOGO M1214 identify one Aspergillus Complete Medium. Both local layers turn its 1 L water input into 1 g/L, and omit the collection-wide sterilization instruction. Four dry numerals match the source batch amounts, but the source does not establish a measured final-litre denominator. Source-specific products and generic chemical identities are preserved without inventing organism growth claims.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 367; batch 037 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-six task batches contain 360 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 363 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007742 | data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml | generated | aspergillus_complete_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007742 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007742 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch037/367/strict.tsv |
| validate-terms | passed | True | CultureMech:007742 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007742 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007742 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadiveJ1134api | unavailable | False | CultureMech:007742 | The preserved mediadiveJ1134api response is HTTP 503. Exact JCM1134 and structured TOGO M1214 remain available, so this optional corroborating failure does not prevent the bounded assessment. |
| Exact source content access: mediadiveJ1134api_retry | unavailable | False | CultureMech:007742 | The preserved mediadiveJ1134api_retry response is HTTP 503. Exact JCM1134 and structured TOGO M1214 remain available, so this optional corroborating failure does not prevent the bounded assessment. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007742.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:007742.

8 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "ingredient_or_context": "Distilled water",
    "field_path": "ingredients[0].concentration",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_amount": 1,
    "source_unit": "L",
    "source_stage": "JCM1134 complete recipe batch with 1 L water input",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm1134",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134",
        "source_locator": "Main composition table",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27",
        "parsed_text_sha256": "1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b"
      },
      {
        "source_key": "togoM1214original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1214",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "8edb02b051f7b4573e722b942ba51ca56350d4059708a1bf221a75dd6762a5e6"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore the literal 1 L water input. The stored 1 G_PER_L is dimensionally wrong; no density conversion is justified."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore the literal 1 L water input. The stored 1 G_PER_L is dimensionally wrong; no density conversion is justified."
      }
    ],
    "arithmetic_and_scope": "Restore the literal 1 L water input. The stored 1 G_PER_L is dimensionally wrong; no density conversion is justified."
  },
  {
    "quantity_id": "q2",
    "ingredient_or_context": "Malt extract (BD-Difco)",
    "field_path": "ingredients[1].concentration",
    "local": {
      "value": "20",
      "unit": "G_PER_L"
    },
    "source_amount": 20,
    "source_unit": "g",
    "source_stage": "JCM1134 complete recipe batch with 1 L water input",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "jcm1134",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134",
        "source_locator": "Main composition table",
        "exact_source_quote": "Malt extract (BD-Difco) 20.0 g",
        "snapshot_sha256": "f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27",
        "parsed_text_sha256": "1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b"
      },
      {
        "source_key": "togoM1214original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1214",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Malt extract (BD--Difco)\",\n          \"volume\": 20,\n          \"unit\": \"g\"",
        "snapshot_sha256": "8edb02b051f7b4573e722b942ba51ca56350d4059708a1bf221a75dd6762a5e6"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral equals the dry batch amount, but 1 L water is not an explicit measured final volume. Preserve the batch mass with its context and evidence; do not assert a final g/L denominator from that input alone."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral equals the dry batch amount, but 1 L water is not an explicit measured final volume. Preserve the batch mass with its context and evidence; do not assert a final g/L denominator from that input alone."
      }
    ],
    "arithmetic_and_scope": "The stored numeral equals the dry batch amount, but 1 L water is not an explicit measured final volume. Preserve the batch mass with its context and evidence; do not assert a final g/L denominator from that input alone."
  },
  {
    "quantity_id": "q3",
    "ingredient_or_context": "Glucose",
    "field_path": "ingredients[2].concentration",
    "local": {
      "value": "20",
      "unit": "G_PER_L"
    },
    "source_amount": 20,
    "source_unit": "g",
    "source_stage": "JCM1134 complete recipe batch with 1 L water input",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "jcm1134",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134",
        "source_locator": "Main composition table",
        "exact_source_quote": "Glucose 20.0 g",
        "snapshot_sha256": "f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27",
        "parsed_text_sha256": "1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b"
      },
      {
        "source_key": "togoM1214original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1214",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Glucose\",\n          \"volume\": 20,\n          \"unit\": \"g\"",
        "snapshot_sha256": "8edb02b051f7b4573e722b942ba51ca56350d4059708a1bf221a75dd6762a5e6"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral equals the dry batch amount, but 1 L water is not an explicit measured final volume. Preserve the batch mass with its context and evidence; do not assert a final g/L denominator from that input alone."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral equals the dry batch amount, but 1 L water is not an explicit measured final volume. Preserve the batch mass with its context and evidence; do not assert a final g/L denominator from that input alone."
      }
    ],
    "arithmetic_and_scope": "The stored numeral equals the dry batch amount, but 1 L water is not an explicit measured final volume. Preserve the batch mass with its context and evidence; do not assert a final g/L denominator from that input alone."
  },
  {
    "quantity_id": "q4",
    "ingredient_or_context": "Agar",
    "field_path": "ingredients[3].concentration",
    "local": {
      "value": "20",
      "unit": "G_PER_L"
    },
    "source_amount": 20,
    "source_unit": "g",
    "source_stage": "JCM1134 complete recipe batch with 1 L water input",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "jcm1134",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134",
        "source_locator": "Main composition table",
        "exact_source_quote": "Agar 20.0 g",
        "snapshot_sha256": "f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27",
        "parsed_text_sha256": "1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b"
      },
      {
        "source_key": "togoM1214original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1214",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"Agar\",\n          \"volume\": 20,\n          \"unit\": \"g\"",
        "snapshot_sha256": "8edb02b051f7b4573e722b942ba51ca56350d4059708a1bf221a75dd6762a5e6"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral equals the dry batch amount, but 1 L water is not an explicit measured final volume. Preserve the batch mass with its context and evidence; do not assert a final g/L denominator from that input alone."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral equals the dry batch amount, but 1 L water is not an explicit measured final volume. Preserve the batch mass with its context and evidence; do not assert a final g/L denominator from that input alone."
      }
    ],
    "arithmetic_and_scope": "The stored numeral equals the dry batch amount, but 1 L water is not an explicit measured final volume. Preserve the batch mass with its context and evidence; do not assert a final g/L denominator from that input alone."
  },
  {
    "quantity_id": "q5",
    "ingredient_or_context": "Peptone (BD-Difco)",
    "field_path": "ingredients[4].concentration",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_amount": 10,
    "source_unit": "g",
    "source_stage": "JCM1134 complete recipe batch with 1 L water input",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "jcm1134",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134",
        "source_locator": "Main composition table",
        "exact_source_quote": "Peptone (BD-Difco) 10.0 g",
        "snapshot_sha256": "f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27",
        "parsed_text_sha256": "1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b"
      },
      {
        "source_key": "togoM1214original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1214",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"Peptone (BD--Difco)\",\n          \"volume\": 10,\n          \"unit\": \"g\"",
        "snapshot_sha256": "8edb02b051f7b4573e722b942ba51ca56350d4059708a1bf221a75dd6762a5e6"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral equals the dry batch amount, but 1 L water is not an explicit measured final volume. Preserve the batch mass with its context and evidence; do not assert a final g/L denominator from that input alone."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral equals the dry batch amount, but 1 L water is not an explicit measured final volume. Preserve the batch mass with its context and evidence; do not assert a final g/L denominator from that input alone."
      }
    ],
    "arithmetic_and_scope": "The stored numeral equals the dry batch amount, but 1 L water is not an explicit measured final volume. Preserve the batch mass with its context and evidence; do not assert a final g/L denominator from that input alone."
  },
  {
    "quantity_id": "q6",
    "ingredient_or_context": "Sterilization temperature",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": 121,
    "source_unit": "degrees Celsius",
    "source_stage": "JCM page-wide default sterilization",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm1134",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134",
        "source_locator": "Page-wide default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27",
        "parsed_text_sha256": "1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Add only the source collection default autoclave condition, preserving its unless-otherwise-stated qualifier. It is a preparation parameter, not a growth condition."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Add only the source collection default autoclave condition, preserving its unless-otherwise-stated qualifier. It is a preparation parameter, not a growth condition."
      }
    ],
    "arithmetic_and_scope": "Add only the source collection default autoclave condition, preserving its unless-otherwise-stated qualifier. It is a preparation parameter, not a growth condition."
  },
  {
    "quantity_id": "q7",
    "ingredient_or_context": "Sterilization duration",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": 15,
    "source_unit": "minutes",
    "source_stage": "JCM page-wide default sterilization",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm1134",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134",
        "source_locator": "Page-wide default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27",
        "parsed_text_sha256": "1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Add only the source collection default autoclave condition, preserving its unless-otherwise-stated qualifier. It is a preparation parameter, not a growth condition."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Add only the source collection default autoclave condition, preserving its unless-otherwise-stated qualifier. It is a preparation parameter, not a growth condition."
      }
    ],
    "arithmetic_and_scope": "Add only the source collection default autoclave condition, preserving its unless-otherwise-stated qualifier. It is a preparation parameter, not a growth condition."
  },
  {
    "quantity_id": "q8",
    "ingredient_or_context": "Measured final volume after dry additions",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": null,
    "source_unit": "not declared",
    "source_stage": "Final prepared medium",
    "decision": "not_quantified",
    "source_snippets": [
      {
        "source_key": "jcm1134",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134",
        "source_locator": "Main composition table",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27",
        "parsed_text_sha256": "1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "rationale": "No measured final-volume instruction is printed. Retain the source batch rather than inventing a dilution denominator."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "rationale": "No measured final-volume instruction is printed. Retain the source batch rather than inventing a dilution denominator."
      }
    ],
    "arithmetic_and_scope": "No mass-to-final-concentration conversion is performed."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:007742.

3 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 3/5 primary and 3/5 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 5: primary 60.00%; secondary 60.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:007742.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact accession and maintained input

identity: supported. Targets: CultureMech:007742.

The complete TOGO meta identifies JCM_M1134 and the exact JCM primary URL. Both full local files carry CultureMech:007742 and the same five ingredients; the generated layer adds merge metadata/history. No stock, variant or namesake is substituted.

### Every source amount and denominator

consistency: concern. Targets: CultureMech:007742.

All ten local concentration occurrences are covered individually by layer. Water is a volume, while the four dry numerals are batch masses with an unresolved measured final-volume basis. All five source components are present; there are no nested stocks or stock doses to infer.

### Generic chemicals and branded complex products

grounding: supported. Targets: CultureMech:007742.

Water, generic glucose and agar have matching nonobsolete canonical labels and current MIM preferred rows. No particular glucose anomer is claimed. Malt extract and peptone remain BD-Difco-qualified mixtures, not guessed pure chemicals or verified manufacturer compositions. Generic agar denotes a polysaccharide mixture.

### Missing collection sterilization default

completeness: concern. Targets: CultureMech:007742.

Both layers omit preparation and sterilization. JCM supplies its page-wide 121°C for 15 min default and prints no exception here. Preserve that exact scope; no pressure, cooling step, pH, culture temperature, gas mixture or vessel size is supplied.

### Physical state, mixtures and growth restraint

scope: concern. Targets: CultureMech:007742.

Agar supports SOLID_AGAR; malt extract and peptone support COMPLEX/UNDEFINED. Bacterial filing is an inherited classification, not an organism-level claim established by the Aspergillus title. Current importer category heuristics are not a taxonomy authority. No target organism, growth outcome, KG match, DOI/PMID, high-metal label or specific incubation parameter is asserted or invented in this assessment.

### Amount-level evidence is missing

evidence: concern. Targets: CultureMech:007742.

Both local layers lack attached amount evidence and structured source references. URLs in notes and provider roles/properties establish provenance leads, not independently verified ingredient functions or growth. The new review evidence does not silently become recipe evidence.

### Current writer, owner and history boundaries

provenance: supported. Targets: CultureMech:007742.

Future corrections belong to the exact normalized TOGO owner and any demonstrated importer defect, followed by separately authorized regeneration. All 13 history timestamps are timezone-aware. Historical ID/grounding/MIM migrations are preserved; no legacy MIM ID is currently asserted. No scientific-status promotion follows from passing schema checks.

## Findings

### f1: Water volume is encoded as mass concentration

major / open / confirmed; issue key: culturemech.007742.quantity-basis.

Both local layers encode the source 1 L water input as 1 G_PER_L. The other four numerals match dry batch masses, but the source does not state a measured final litre. Their present G_PER_L interpretation therefore also needs explicit source-basis reconciliation.

### f2: The collection sterilization instruction is absent

minor / open / confirmed; issue key: culturemech.007742.collection-sterilization.

The exact JCM page states its default autoclave cycle, 121°C for 15 min, and no exception is printed for medium 1134. Neither local layer retains preparation or sterilization.

### f3: Source amounts lack attached claim-level evidence

minor / open / confirmed; issue key: culturemech.007742.amount-evidence.

The five source rows are recoverable, but neither local layer has claim-linked amount snippets or a structured reference list. The reference validator examined zero evidence references.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained water field to a volume representation; retain all four dry batch masses and the unresolved final-volume basis in scoped explanations. Attach exact amount evidence and regenerate only after owner correction.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add the collection default with its qualifier and source locator to the maintained preparation, without turning sterilization values into incubation conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach exact amount and preparation evidence in the native claim locations, retaining product qualifiers and source batch scope. Do not fill missing organism or culture-condition fields by inference.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch037/367/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch037/367/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml:1:id: CultureMech:007742<br>./data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml:1:id: CultureMech:007742<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch037/source-preflight-bound/367/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 8 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| jcm1134 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134; Exact medium 1134 title and complete five-row formulation table | supports | The collection lists malt extract 20 g, peptone 10 g, glucose 20 g, agar 20 g and distilled water 1 L. The water is an input volume; no measured final volume, pH or organism-specific outcome is printed. |
| jcm-default | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134; Page-wide default before the medium title; no medium-specific exception printed | supports | The collection default supplies an autoclave cycle, not an incubation temperature or growth result. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1214; $.meta, $.components[0].items and empty $.comments | supports | M1214 explicitly resolves to JCM_M1134 and retains all five source quantities and product qualifiers. The provider has no preparation comment; its empty comments do not erase the JCM page-wide default. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch037/367/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml", "events": 6, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO _ingredient_from_item/_parse_unit recognizes L distinctly from G_PER_L, while its simple g mapping does not establish a final-volume basis. Current preparation extraction reads explicit comments; empty M1214 comments do not contain the JCM page-wide default. The current one-owner merge copies maintained content with merge metadata. These reads identify follow-up ownership; they do not authenticate a historical execution. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO _ingredient_from_item/_parse_unit recognizes L distinctly from G_PER_L, while its simple g mapping does not establish a final-volume basis. Current preparation extraction reads explicit comments; empty M1214 comments do not contain the JCM page-wide default. The current one-owner merge copies maintained content with merge metadata. These reads identify follow-up ownership; they do not authenticate a historical execution. |
| mediadiveJ1134api-attempt | https://mediadive.dsmz.de/rest/medium/J1134; Preserved exact public retrieval result | context_only | The preserved mediadiveJ1134api response is HTTP 503. Exact JCM1134 and structured TOGO M1214 remain available, so this optional corroborating failure does not prevent the bounded assessment. |
| mediadiveJ1134api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J1134; Preserved exact public retrieval result | context_only | The preserved mediadiveJ1134api_retry response is HTTP 503. Exact JCM1134 and structured TOGO M1214 remain available, so this optional corroborating failure does not prevent the bounded assessment. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The preserved mediadiveJ1134api response is HTTP 503. Exact JCM1134 and structured TOGO M1214 remain available, so this optional corroborating failure does not prevent the bounded assessment.
- The preserved mediadiveJ1134api_retry response is HTTP 503. Exact JCM1134 and structured TOGO M1214 remain available, so this optional corroborating failure does not prevent the bounded assessment.
- The TOGO page capture is only a JavaScript shell; formulation evidence comes from its exact structured API and JCM1134.
- Completion describes assessment of the exact current claims and available sources; it does not resolve unsupported denominators or certify a growth protocol.
- This scientific assessment preceded formal review validation and saving; their actual outcomes are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T201526Z-culturemech-007742-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: aspergillus_complete_medium (CultureMech:007742)'
started_at: '2026-10-21T20:11:20Z'
finished_at: '2026-10-21T20:15:26Z'
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
summary: Exact JCM 1134 and TOGO M1214 identify one Aspergillus Complete Medium. Both
  local layers turn its 1 L water input into 1 g/L, and omit the collection-wide sterilization
  instruction. Four dry numerals match the source batch amounts, but the source does
  not establish a measured final-litre denominator. Source-specific products and generic
  chemical identities are preserved without inventing organism growth claims.
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
  - path: data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml
    sha256: 23a99462b052f49e9cf7444c420a451c8832933f15f2b248b7bbad635d56232f
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml
    sha256: c5b75c11c35faa04c650dad05c9358907d3ab36960d8517b4ff917add5240a08
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
  selection: Task review 367; batch 037 item 7 of 10, selected in Python lexicographic
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
  - CultureMech:007742
targets:
- target_id: CultureMech:007742
  path: data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml
  label: aspergillus_complete_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch037/367/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch037/367/strict.tsv"
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007742
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
  - CultureMech:007742
- check_id: mediadiveJ1134api-source-access
  name: 'Exact source content access: mediadiveJ1134api'
  required: false
  status: unavailable
  summary: The preserved mediadiveJ1134api response is HTTP 503. Exact JCM1134 and
    structured TOGO M1214 remain available, so this optional corroborating failure
    does not prevent the bounded assessment.
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - mediadiveJ1134api-attempt
- check_id: mediadiveJ1134api_retry-source-access
  name: 'Exact source content access: mediadiveJ1134api_retry'
  required: false
  status: unavailable
  summary: The preserved mediadiveJ1134api_retry response is HTTP 503. Exact JCM1134
    and structured TOGO M1214 remain available, so this optional corroborating failure
    does not prevent the bounded assessment.
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - mediadiveJ1134api_retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T20:15:23Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T20:15:23Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:12.411118Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch037/367/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:13.475822Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch037/367/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:14.673534Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:15.417924Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T20:15:23Z'
  support: supports
  summary: './data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml:1:id: CultureMech:007742

    ./data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml:1:id:
    CultureMech:007742

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/source-preflight-bound/367/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T20:15:23Z'
  support: supports
  summary: 8 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: beac3f5493d9e1622b96d8805a2ecd1c256c83c931ce9dd93c7f096c3cb1bf91
- evidence_id: jcm1134
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134
  locator: Exact medium 1134 title and complete five-row formulation table
  accessed_at: '2026-10-21T19:52:52.132436Z'
  support: supports
  summary: The collection lists malt extract 20 g, peptone 10 g, glucose 20 g, agar
    20 g and distilled water 1 L. The water is an input volume; no measured final
    volume, pH or organism-specific outcome is printed.
  quote: Malt extract (BD-Difco) 20.0 g Peptone (BD-Difco) 10.0 g Glucose 20.0 g Agar
    20.0 g Distilled water 1.0 L
  snapshot_sha256: f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27
- evidence_id: jcm-default
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134
  locator: Page-wide default before the medium title; no medium-specific exception
    printed
  accessed_at: '2026-10-21T19:52:52.132436Z'
  support: supports
  summary: The collection default supplies an autoclave cycle, not an incubation temperature
    or growth result.
  quote: Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.
  snapshot_sha256: f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1214
  locator: $.meta, $.components[0].items and empty $.comments
  accessed_at: '2026-10-21T19:52:50.266376Z'
  support: supports
  summary: M1214 explicitly resolves to JCM_M1134 and retains all five source quantities
    and product qualifiers. The provider has no preparation comment; its empty comments
    do not erase the JCM page-wide default.
  quote: '"original_media_id": "JCM_M1134"'
  snapshot_sha256: 8edb02b051f7b4573e722b942ba51ca56350d4059708a1bf221a75dd6762a5e6
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/367/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T20:15:23Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 4552b9f0c773f1318ccc433aaaaea2e162bb0942146d83c055f6ebd5f59f088b
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T20:15:23Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type":
    "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id":
    "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509":
    [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T20:15:23Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:15:23Z'
  support: context_only
  summary: Current TOGO _ingredient_from_item/_parse_unit recognizes L distinctly
    from G_PER_L, while its simple g mapping does not establish a final-volume basis.
    Current preparation extraction reads explicit comments; empty M1214 comments do
    not contain the JCM page-wide default. The current one-owner merge copies maintained
    content with merge metadata. These reads identify follow-up ownership; they do
    not authenticate a historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:15:23Z'
  support: context_only
  summary: Current TOGO _ingredient_from_item/_parse_unit recognizes L distinctly
    from G_PER_L, while its simple g mapping does not establish a final-volume basis.
    Current preparation extraction reads explicit comments; empty M1214 comments do
    not contain the JCM page-wide default. The current one-owner merge copies maintained
    content with merge metadata. These reads identify follow-up ownership; they do
    not authenticate a historical execution.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: mediadiveJ1134api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1134
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:52:49.159379Z'
  support: context_only
  summary: The preserved mediadiveJ1134api response is HTTP 503. Exact JCM1134 and
    structured TOGO M1214 remain available, so this optional corroborating failure
    does not prevent the bounded assessment.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ1134api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1134
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:53:28.239622Z'
  support: context_only
  summary: The preserved mediadiveJ1134api_retry response is HTTP 503. Exact JCM1134
    and structured TOGO M1214 remain available, so this optional corroborating failure
    does not prevent the bounded assessment.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 8 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"ingredient_or_context\": \"\
    Distilled water\",\n    \"field_path\": \"ingredients[0].concentration\",\n  \
    \  \"local\": {\n      \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_amount\": 1,\n    \"source_unit\": \"L\",\n    \"source_stage\"\
    : \"JCM1134 complete recipe batch with 1 L water input\",\n    \"decision\": \"\
    correct\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1134\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134\"\
    ,\n        \"source_locator\": \"Main composition table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27\"\
    ,\n        \"parsed_text_sha256\": \"1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b\"\
    \n      },\n      {\n        \"source_key\": \"togoM1214original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1214\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"8edb02b051f7b4573e722b942ba51ca56350d4059708a1bf221a75dd6762a5e6\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[0].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Restore\
    \ the literal 1 L water input. The stored 1 G_PER_L is dimensionally wrong; no\
    \ density conversion is justified.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Restore the literal\
    \ 1 L water input. The stored 1 G_PER_L is dimensionally wrong; no density conversion\
    \ is justified.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"Restore the\
    \ literal 1 L water input. The stored 1 G_PER_L is dimensionally wrong; no density\
    \ conversion is justified.\"\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"\
    ingredient_or_context\": \"Malt extract (BD-Difco)\",\n    \"field_path\": \"\
    ingredients[1].concentration\",\n    \"local\": {\n      \"value\": \"20\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 20,\n    \"source_unit\"\
    : \"g\",\n    \"source_stage\": \"JCM1134 complete recipe batch with 1 L water\
    \ input\",\n    \"decision\": \"unsupported\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"jcm1134\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134\"\
    ,\n        \"source_locator\": \"Main composition table\",\n        \"exact_source_quote\"\
    : \"Malt extract (BD-Difco) 20.0 g\",\n        \"snapshot_sha256\": \"f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27\"\
    ,\n        \"parsed_text_sha256\": \"1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b\"\
    \n      },\n      {\n        \"source_key\": \"togoM1214original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1214\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Malt extract (BD--Difco)\\\",\\n          \\\"\
    volume\\\": 20,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"8edb02b051f7b4573e722b942ba51ca56350d4059708a1bf221a75dd6762a5e6\"\n     \
    \ }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The stored numeral\
    \ equals the dry batch amount, but 1 L water is not an explicit measured final\
    \ volume. Preserve the batch mass with its context and evidence; do not assert\
    \ a final g/L denominator from that input alone.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The stored numeral\
    \ equals the dry batch amount, but 1 L water is not an explicit measured final\
    \ volume. Preserve the batch mass with its context and evidence; do not assert\
    \ a final g/L denominator from that input alone.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"The stored numeral equals the dry batch amount, but 1 L water is not an explicit\
    \ measured final volume. Preserve the batch mass with its context and evidence;\
    \ do not assert a final g/L denominator from that input alone.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q3\",\n    \"ingredient_or_context\": \"Glucose\",\n \
    \   \"field_path\": \"ingredients[2].concentration\",\n    \"local\": {\n    \
    \  \"value\": \"20\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : 20,\n    \"source_unit\": \"g\",\n    \"source_stage\": \"JCM1134 complete recipe\
    \ batch with 1 L water input\",\n    \"decision\": \"unsupported\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1134\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134\",\n        \"source_locator\"\
    : \"Main composition table\",\n        \"exact_source_quote\": \"Glucose 20.0\
    \ g\",\n        \"snapshot_sha256\": \"f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27\"\
    ,\n        \"parsed_text_sha256\": \"1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b\"\
    \n      },\n      {\n        \"source_key\": \"togoM1214original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1214\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Glucose\\\",\\n          \\\"volume\\\": 20,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"8edb02b051f7b4573e722b942ba51ca56350d4059708a1bf221a75dd6762a5e6\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[2].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"\
    The stored numeral equals the dry batch amount, but 1 L water is not an explicit\
    \ measured final volume. Preserve the batch mass with its context and evidence;\
    \ do not assert a final g/L denominator from that input alone.\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The stored numeral\
    \ equals the dry batch amount, but 1 L water is not an explicit measured final\
    \ volume. Preserve the batch mass with its context and evidence; do not assert\
    \ a final g/L denominator from that input alone.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"The stored numeral equals the dry batch amount, but 1 L water is not an explicit\
    \ measured final volume. Preserve the batch mass with its context and evidence;\
    \ do not assert a final g/L denominator from that input alone.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q4\",\n    \"ingredient_or_context\": \"Agar\",\n    \"\
    field_path\": \"ingredients[3].concentration\",\n    \"local\": {\n      \"value\"\
    : \"20\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 20,\n \
    \   \"source_unit\": \"g\",\n    \"source_stage\": \"JCM1134 complete recipe batch\
    \ with 1 L water input\",\n    \"decision\": \"unsupported\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1134\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134\",\n        \"source_locator\"\
    : \"Main composition table\",\n        \"exact_source_quote\": \"Agar 20.0 g\"\
    ,\n        \"snapshot_sha256\": \"f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27\"\
    ,\n        \"parsed_text_sha256\": \"1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b\"\
    \n      },\n      {\n        \"source_key\": \"togoM1214original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1214\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Agar\\\",\\n          \\\"volume\\\": 20,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"8edb02b051f7b4573e722b942ba51ca56350d4059708a1bf221a75dd6762a5e6\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[3].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"\
    The stored numeral equals the dry batch amount, but 1 L water is not an explicit\
    \ measured final volume. Preserve the batch mass with its context and evidence;\
    \ do not assert a final g/L denominator from that input alone.\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The stored numeral\
    \ equals the dry batch amount, but 1 L water is not an explicit measured final\
    \ volume. Preserve the batch mass with its context and evidence; do not assert\
    \ a final g/L denominator from that input alone.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"The stored numeral equals the dry batch amount, but 1 L water is not an explicit\
    \ measured final volume. Preserve the batch mass with its context and evidence;\
    \ do not assert a final g/L denominator from that input alone.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q5\",\n    \"ingredient_or_context\": \"Peptone (BD-Difco)\"\
    ,\n    \"field_path\": \"ingredients[4].concentration\",\n    \"local\": {\n \
    \     \"value\": \"10\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : 10,\n    \"source_unit\": \"g\",\n    \"source_stage\": \"JCM1134 complete recipe\
    \ batch with 1 L water input\",\n    \"decision\": \"unsupported\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1134\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134\",\n        \"source_locator\"\
    : \"Main composition table\",\n        \"exact_source_quote\": \"Peptone (BD-Difco)\
    \ 10.0 g\",\n        \"snapshot_sha256\": \"f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27\"\
    ,\n        \"parsed_text_sha256\": \"1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b\"\
    \n      },\n      {\n        \"source_key\": \"togoM1214original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1214\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Peptone (BD--Difco)\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    8edb02b051f7b4573e722b942ba51ca56350d4059708a1bf221a75dd6762a5e6\"\n      }\n\
    \    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n\
    \        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The stored numeral\
    \ equals the dry batch amount, but 1 L water is not an explicit measured final\
    \ volume. Preserve the batch mass with its context and evidence; do not assert\
    \ a final g/L denominator from that input alone.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The stored numeral\
    \ equals the dry batch amount, but 1 L water is not an explicit measured final\
    \ volume. Preserve the batch mass with its context and evidence; do not assert\
    \ a final g/L denominator from that input alone.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"The stored numeral equals the dry batch amount, but 1 L water is not an explicit\
    \ measured final volume. Preserve the batch mass with its context and evidence;\
    \ do not assert a final g/L denominator from that input alone.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q6\",\n    \"ingredient_or_context\": \"Sterilization\
    \ temperature\",\n    \"field_path\": \"preparation_steps\",\n    \"local\": null,\n\
    \    \"source_amount\": 121,\n    \"source_unit\": \"degrees Celsius\",\n    \"\
    source_stage\": \"JCM page-wide default sterilization\",\n    \"decision\": \"\
    add\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1134\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134\"\
    ,\n        \"source_locator\": \"Page-wide default\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27\"\
    ,\n        \"parsed_text_sha256\": \"1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"Add only the\
    \ source collection default autoclave condition, preserving its unless-otherwise-stated\
    \ qualifier. It is a preparation parameter, not a growth condition.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Add only the source\
    \ collection default autoclave condition, preserving its unless-otherwise-stated\
    \ qualifier. It is a preparation parameter, not a growth condition.\"\n      }\n\
    \    ],\n    \"arithmetic_and_scope\": \"Add only the source collection default\
    \ autoclave condition, preserving its unless-otherwise-stated qualifier. It is\
    \ a preparation parameter, not a growth condition.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q7\",\n    \"ingredient_or_context\": \"Sterilization duration\",\n    \"\
    field_path\": \"preparation_steps\",\n    \"local\": null,\n    \"source_amount\"\
    : 15,\n    \"source_unit\": \"minutes\",\n    \"source_stage\": \"JCM page-wide\
    \ default sterilization\",\n    \"decision\": \"add\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1134\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134\",\n        \"source_locator\"\
    : \"Page-wide default\",\n        \"exact_source_quote\": \"Unless otherwise stated,\
    \ sterilize media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\"\
    : \"f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27\",\n    \
    \    \"parsed_text_sha256\": \"1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"Add only the\
    \ source collection default autoclave condition, preserving its unless-otherwise-stated\
    \ qualifier. It is a preparation parameter, not a growth condition.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Add only the source\
    \ collection default autoclave condition, preserving its unless-otherwise-stated\
    \ qualifier. It is a preparation parameter, not a growth condition.\"\n      }\n\
    \    ],\n    \"arithmetic_and_scope\": \"Add only the source collection default\
    \ autoclave condition, preserving its unless-otherwise-stated qualifier. It is\
    \ a preparation parameter, not a growth condition.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q8\",\n    \"ingredient_or_context\": \"Measured final volume after dry additions\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"local\": null,\n    \"source_amount\"\
    : null,\n    \"source_unit\": \"not declared\",\n    \"source_stage\": \"Final\
    \ prepared medium\",\n    \"decision\": \"not_quantified\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1134\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1134\",\n        \"source_locator\"\
    : \"Main composition table\",\n        \"exact_source_quote\": \"Distilled water\
    \ 1.0 L\",\n        \"snapshot_sha256\": \"f6dfdd46acb6d92c2d7e41d5ade304ef4baa34771c058c4d0ee5e1ecd6e5cb27\"\
    ,\n        \"parsed_text_sha256\": \"1e632419f9ae32a6319c8a82f6abfa146b7adb0b8a2f82c09f7d19df957de89b\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    No measured final-volume instruction is printed. Retain the source batch rather\
    \ than inventing a dilution denominator.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"not_quantified\",\n        \"rationale\": \"No measured\
    \ final-volume instruction is printed. Retain the source batch rather than inventing\
    \ a dilution denominator.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"\
    No mass-to-final-concentration conversion is performed.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '3 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 3/5 primary
    and 3/5 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi17234
  - chebi2509
  details: 'Instance coverage on a 0–100 percent scale, denominator 5: primary 60.00%;
    secondary 60.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact accession and maintained input
  outcome: supported
  summary: The complete TOGO meta identifies JCM_M1134 and the exact JCM primary URL.
    Both full local files carry CultureMech:007742 and the same five ingredients;
    the generated layer adds merge metadata/history. No stock, variant or namesake
    is substituted.
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - record
  - togo
  - jcm1134
  - owner-0
- assessment_id: source-stage-consistency
  area: consistency
  topic: Every source amount and denominator
  outcome: concern
  summary: All ten local concentration occurrences are covered individually by layer.
    Water is a volume, while the four dry numerals are batch masses with an unresolved
    measured final-volume basis. All five source components are present; there are
    no nested stocks or stock doses to infer.
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - quantity-inventory
  - jcm1134
  - togo
  - owner-0
- assessment_id: forms
  area: grounding
  topic: Generic chemicals and branded complex products
  outcome: supported
  summary: Water, generic glucose and agar have matching nonobsolete canonical labels
    and current MIM preferred rows. No particular glucose anomer is claimed. Malt
    extract and peptone remain BD-Difco-qualified mixtures, not guessed pure chemicals
    or verified manufacturer compositions. Generic agar denotes a polysaccharide mixture.
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - record
  - jcm1134
  - togo
  - chebi15377
  - chebi17234
  - chebi2509
  - mim
- assessment_id: preparation
  area: completeness
  topic: Missing collection sterilization default
  outcome: concern
  summary: Both layers omit preparation and sterilization. JCM supplies its page-wide
    121°C for 15 min default and prints no exception here. Preserve that exact scope;
    no pressure, cooling step, pH, culture temperature, gas mixture or vessel size
    is supplied.
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - record
  - jcm-default
  - owner-0
- assessment_id: classification
  area: scope
  topic: Physical state, mixtures and growth restraint
  outcome: concern
  summary: Agar supports SOLID_AGAR; malt extract and peptone support COMPLEX/UNDEFINED.
    Bacterial filing is an inherited classification, not an organism-level claim established
    by the Aspergillus title. Current importer category heuristics are not a taxonomy
    authority. No target organism, growth outcome, KG match, DOI/PMID, high-metal
    label or specific incubation parameter is asserted or invented in this assessment.
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - record
  - jcm1134
  - togo
  - writer-0
- assessment_id: evidence-placement
  area: evidence
  topic: Amount-level evidence is missing
  outcome: concern
  summary: Both local layers lack attached amount evidence and structured source references.
    URLs in notes and provider roles/properties establish provenance leads, not independently
    verified ingredient functions or growth. The new review evidence does not silently
    become recipe evidence.
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - record
  - quantity-inventory
  - jcm1134
  - togo
  - owner-0
- assessment_id: ownership
  area: provenance
  topic: Current writer, owner and history boundaries
  outcome: supported
  summary: Future corrections belong to the exact normalized TOGO owner and any demonstrated
    importer defect, followed by separately authorized regeneration. All 13 history
    timestamps are timezone-aware. Historical ID/grounding/MIM migrations are preserved;
    no legacy MIM ID is currently asserted. No scientific-status promotion follows
    from passing schema checks.
  target_ids:
  - CultureMech:007742
  evidence_ids:
  - history-metadata
  - writer-0
  - writer-1
  - owner-0
findings:
- finding_id: f1
  issue_key: culturemech.007742.quantity-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water volume is encoded as mass concentration
  description: Both local layers encode the source 1 L water input as 1 G_PER_L. The
    other four numerals match dry batch masses, but the source does not state a measured
    final litre. Their present G_PER_L interpretation therefore also needs explicit
    source-basis reconciliation.
  target_ids:
  - CultureMech:007742
  field_paths:
  - ingredients
  evidence_ids:
  - jcm1134
  - togo
  - quantity-inventory
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: culturemech.007742.collection-sterilization
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: The collection sterilization instruction is absent
  description: The exact JCM page states its default autoclave cycle, 121°C for 15
    min, and no exception is printed for medium 1134. Neither local layer retains
    preparation or sterilization.
  target_ids:
  - CultureMech:007742
  field_paths:
  - preparation_steps
  - sterilization
  evidence_ids:
  - jcm-default
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.007742.amount-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source amounts lack attached claim-level evidence
  description: The five source rows are recoverable, but neither local layer has claim-linked
    amount snippets or a structured reference list. The reference validator examined
    zero evidence references.
  target_ids:
  - CultureMech:007742
  field_paths:
  - ingredients
  - references
  evidence_ids:
  - jcm1134
  - togo
  - quantity-inventory
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml
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
  description: Correct the maintained water field to a volume representation; retain
    all four dry batch masses and the unresolved final-volume basis in scoped explanations.
    Attach exact amount evidence and regenerate only after owner correction.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007742
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml
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
  description: Add the collection default with its qualifier and source locator to
    the maintained preparation, without turning sterilization values into incubation
    conditions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007742
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml
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
  description: Attach exact amount and preparation evidence in the native claim locations,
    retaining product qualifiers and source batch scope. Do not fill missing organism
    or culture-condition fields by inference.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007742
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml
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
- The preserved mediadiveJ1134api response is HTTP 503. Exact JCM1134 and structured
  TOGO M1214 remain available, so this optional corroborating failure does not prevent
  the bounded assessment.
- The preserved mediadiveJ1134api_retry response is HTTP 503. Exact JCM1134 and structured
  TOGO M1214 remain available, so this optional corroborating failure does not prevent
  the bounded assessment.
- The TOGO page capture is only a JavaScript shell; formulation evidence comes from
  its exact structured API and JCM1134.
- Completion describes assessment of the exact current claims and available sources;
  it does not resolve unsupported denominators or certify a growth protocol.
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
