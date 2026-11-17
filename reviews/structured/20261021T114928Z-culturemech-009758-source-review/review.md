# Source and formulation review: agc2_medium (CultureMech:009758)

- Review: 20261021T114928Z-culturemech-009758-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T11:43:30Z
- Finished UTC: 2026-10-21T11:49:28Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M377 and MediaDive J382 preserve AGC2-specific overrides and separate preparation stages, but both local layers flatten solution additions and stock ingredients, merge two water aliquots as mass, and convert a calcium-nitrate mg amount and acid ml dose to g/L. Final iron and yeast concentrations are explicitly supported by provider prose and must not be diluted again. Exact JCM 382 is unavailable; accessible JCM 92 is bounded parent context, so this review remains partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 190; batch 019 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eighteen task batches contain 180 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 182 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009758 | data/merge_yaml/merged/AGC2_Medium.yaml | generated | agc2_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009758 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009758 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch019/190/strict.tsv |
| validate-terms | passed | True | CultureMech:009758 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009758 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009758 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: jcm382 | unavailable | True | CultureMech:009758 | The exact JCM GRMD=382 response returned HTTP 200 with Nothing found and no formulation. Required upstream AGC2 verification remains unavailable. Accessible JCM 92 and agreement between TOGO/MediaDive do not replace the exact unavailable primary. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009758.

The four documented recipes completed; interpret the scope of each separately.

### AGC2 identity and bounded parent dependency

identity: supported. Targets: CultureMech:009758.

CultureMech:009758 and TOGO M377 resolve to original JCM_M382/MediaDive J382. The provider explicitly points to parent JCM 92 with overrides; the self-M377 references label local Sol. 1/Sol. 2 sections, not a different external stock or a request to add the complete medium twice. Parent CultureMech:003277 is context only.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009758.

16 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence. All 22 ingredient and stock-dose concentration instances across the target and maintained owners are explicitly covered; additional rows retain preparation quantities and source-only components.

[
  {
    "quantity_id": "q1",
    "ingredient_or_context": "Yeast extract final concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_scope": "Retain 0.5 G_PER_L in the receiving medium, supported explicitly by the AGC2 provider statement.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"yeast extract\",\n          \"volume\": 0.5,\n          \"unit\": \"g/L\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      },
      {
        "source_key": "mediadiveJ382api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J382",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "0.5 g/L yeast extract",
        "snapshot_sha256": "f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50"
      }
    ],
    "rationale": "The number and final-medium basis are explicit and agree with both layers, but no attached local concentration evidence exists. The separate 10% stock label does not license inventing its dose or percent basis."
  },
  {
    "quantity_id": "q2",
    "ingredient_or_context": "Solution 1 assembly aliquot",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "700",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "700",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_scope": "Preserve the source 700 ml local solution aliquot and exact matching section, with composition and preparation separate from receiving-medium ingredients.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Sol. 1\",\n          \"volume\": 700,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      }
    ],
    "rationale": "A named solution aliquot is not a pure ingredient or this number of grams per litre. The nominal aliquots do not settle final volume after acid, solutes and the unspecified yeast-stock addition. Do not infer a replacement external solution identifier."
  },
  {
    "quantity_id": "q3",
    "ingredient_or_context": "Solution 2 assembly aliquot",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "300",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "300",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_scope": "Preserve the source 300 ml local solution aliquot and exact matching section, with composition and preparation separate from receiving-medium ingredients.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Sol. 2\",\n          \"volume\": 300,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      }
    ],
    "rationale": "A named solution aliquot is not a pure ingredient or this number of grams per litre. The nominal aliquots do not settle final volume after acid, solutes and the unspecified yeast-stock addition. Do not infer a replacement external solution identifier."
  },
  {
    "quantity_id": "q4",
    "ingredient_or_context": "Two water preparation aliquots",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_scope": "Preserve 700 ml in Sol. 1 and separately 300 ml in Sol. 2; remove the false merged mass-concentration interpretation.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 700,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      },
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 300,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      }
    ],
    "rationale": "The two source water rows occur in different preparation stages. Their arithmetic sum is 1000 ml of listed water, not 1000 G_PER_L or a verified final medium volume. They must not be double-counted in restored solutions and direct ingredients."
  },
  {
    "quantity_id": "q5",
    "ingredient_or_context": "MgSO4・7H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_scope": "0.5 g in the source Sol. 1 batch, with its original water aliquot and receiving assembly scope.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      }
    ],
    "rationale": "The provider states this mass in Sol. 1 prepared with 700 ml water, not an independently supported concentration per final litre. Preserve the raw batch mass and stage; do not use the parent J92 normalization or the water amount alone as a final-volume denominator."
  },
  {
    "quantity_id": "q6",
    "ingredient_or_context": "K2HPO4",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_scope": "0.5 g in the source Sol. 1 batch, with its original water aliquot and receiving assembly scope.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      }
    ],
    "rationale": "The provider states this mass in Sol. 1 prepared with 700 ml water, not an independently supported concentration per final litre. Preserve the raw batch mass and stage; do not use the parent J92 normalization or the water amount alone as a final-volume denominator."
  },
  {
    "quantity_id": "q7",
    "ingredient_or_context": "KCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_scope": "0.1 g in the source Sol. 1 batch, with its original water aliquot and receiving assembly scope.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      }
    ],
    "rationale": "The provider states this mass in Sol. 1 prepared with 700 ml water, not an independently supported concentration per final litre. Preserve the raw batch mass and stage; do not use the parent J92 normalization or the water amount alone as a final-volume denominator."
  },
  {
    "quantity_id": "q8",
    "ingredient_or_context": "(NH4)2SO4",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_scope": "3 g in the source Sol. 1 batch, with its original water aliquot and receiving assembly scope.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"(NH4)2SO4\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      }
    ],
    "rationale": "The provider states this mass in Sol. 1 prepared with 700 ml water, not an independently supported concentration per final litre. Preserve the raw batch mass and stage; do not use the parent J92 normalization or the water amount alone as a final-volume denominator."
  },
  {
    "quantity_id": "q9",
    "ingredient_or_context": "Ca(NO3)2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_scope": "10 mg in the source Sol. 1 batch, with its original water aliquot and receiving assembly scope.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Ca(NO3)2\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      }
    ],
    "rationale": "The provider states this mass in Sol. 1 prepared with 700 ml water, not an independently supported concentration per final litre. Preserve the raw batch mass and stage; do not use the parent J92 normalization or the water amount alone as a final-volume denominator. The literal source is 10 mg, whereas both layers assert 10 G_PER_L. This is a mass-unit error as well as a stage/denominator error; the generic calcium-nitrate source does not settle hydrate identity."
  },
  {
    "quantity_id": "q10",
    "ingredient_or_context": "Sulfuric acid stock dose and strength",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_scope": "5 ml of the source 10 N sulfuric-acid solution in Sol. 2; retain normality as stock-strength context, not g/L or a guessed molarity.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"10 N H2SO4\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"N\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      },
      {
        "source_key": "mediadiveJ382api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J382",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "5 ml 10 N H2SO4",
        "snapshot_sha256": "f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50"
      }
    ],
    "rationale": "The ingredient name retains 10 N, but its 5 G_PER_L concentration is dimensionally wrong. No acid density, purity or unqualified equivalence-to-molarity conversion is supplied."
  },
  {
    "quantity_id": "q11",
    "ingredient_or_context": "Iron sulfate heptahydrate final concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "44.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "44.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_scope": "Retain 44.2 G_PER_L as the explicitly stated final-medium iron-salt concentration; retain its separately treated Sol. 2 preparation role.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 44.2,\n          \"unit\": \"g/L\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      },
      {
        "source_key": "mediadiveJ382api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J382",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "44.2 g/L (final) FeSO4 x 7H2O",
        "snapshot_sha256": "f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50"
      }
    ],
    "rationale": "The explicit final qualifier controls over the row being nested in the Sol. 2 section. Do not turn 44.2 g/L into 44.2 g per 300 ml, apply a second 0.3 dilution, or replace it with the parent iron amount. Neither local layer has attached evidence."
  },
  {
    "quantity_id": "q12",
    "ingredient_or_context": "Yeast-stock working dose and unspecified percentage basis",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "proposed_source_scope": "Retain the literal 10% stock description and separate sterile addition; working volume and w/v, w/w or v/v basis are unresolved.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"yeast extract\",\n          \"volume\": 0.5,\n          \"unit\": \"g/L\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      },
      {
        "source_key": "mediadiveJ382api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J382",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "sterile stock solution (10%)",
        "snapshot_sha256": "f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50"
      }
    ],
    "rationale": "This decision concerns the unquantified working dose and unsupported percentage basis, not absence of the printed number 10. The final yeast amount is separately supported; no working volume follows without verified stock strength on a defined basis."
  },
  {
    "quantity_id": "q13",
    "ingredient_or_context": "Final pH range",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "ph_range",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "ph_range",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_scope": "Preserve final pH 1.5–2.0 from both provider preparation statements, with final-stage scope.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.meta.ph",
        "exact_source_quote": "\"ph\": \"1.5-2.0\"",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      },
      {
        "source_key": "mediadiveJ382api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J382",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Check the final pH to be 1.5 - 2.0.",
        "snapshot_sha256": "f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50"
      }
    ],
    "rationale": "No pH field or preparation exists in either layer. Do not replace the supported range by a midpoint or treat a provider scalar as the range itself."
  },
  {
    "quantity_id": "q14",
    "ingredient_or_context": "Conflicting pH metadata and inherited adjustment sentence",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "conflict"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "conflict"
      }
    ],
    "proposed_source_scope": "Keep TOGO’s separate pH 3.0 sentence and MediaDive scalar 1.8 as conflicting/contextual provider metadata pending exact-primary resolution; do not silently synthesize a sequential adjustment protocol.",
    "source_snippets": [
      {
        "source_key": "togoM377",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Adjust pH to 3.0.",
        "snapshot_sha256": "f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496"
      },
      {
        "source_key": "mediadiveJ382api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J382",
        "source_locator": "$.data.medium.min_pH",
        "exact_source_quote": "\"min_pH\": 1.8",
        "snapshot_sha256": "f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50"
      },
      {
        "source_key": "mediadiveJ382api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J382",
        "source_locator": "$.data.medium.max_pH",
        "exact_source_quote": "\"max_pH\": 1.8",
        "snapshot_sha256": "f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50"
      }
    ],
    "rationale": "The parent has pH 3.0, but inheritance does not establish the role of that extra sentence in the final AGC2 recipe. The final-range prose is explicit; its exact relationship to the scalar and separate sentence remains unresolved."
  },
  {
    "quantity_id": "q15",
    "ingredient_or_context": "Separate Sol. 2 sterilization cycle",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_scope": "Retain the source 110°C for 30 min only for the separate iron/acid solution, followed by cooling and combination.",
    "source_snippets": [
      {
        "source_key": "mediadiveJ382api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J382",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "autoclave at 110C for 30 min.",
        "snapshot_sha256": "f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50"
      }
    ],
    "rationale": "Both layers omit the cycle and the source stage. Do not apply it universally to all ingredients or treat it as an incubation condition."
  },
  {
    "quantity_id": "q16",
    "ingredient_or_context": "Sol. 1 sterilization temperature and duration",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AGC2_Medium.yaml",
        "field_path": "sterilization",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
        "field_path": "sterilization",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "proposed_source_scope": "Provider specifies autoclaving Sol. 1 without its own explicit cycle; retain that limit while the exact JCM 382 primary is unavailable.",
    "source_snippets": [
      {
        "source_key": "mediadiveJ382api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J382",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "in 700 ml distilled water and autoclave.",
        "snapshot_sha256": "f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50"
      }
    ],
    "rationale": "The accessible parent collection-page default is not independently verified on the unavailable AGC2 primary. No cycle is inserted from an unrelated page or assigned to the entire recipe."
  }
]

### Source-specific forms and current CHEBI-based secondary correspondence

grounding: concern. Targets: CultureMech:009758.

7 distinct asserted chemical IDs resolve as nonobsolete. 0 local label instances differ from canonical labels. 5 of 5 distinct current CHEBI-based secondary keys have exact mapped preferred-term rows in the pinned index; unresolved keys: []. This does not validate historical legacy MIM IDs, supplied hydrates, stereochemistry or catalog products. Source magnesium/iron sulfate heptahydrates match the asserted hydrate terms. Generic calcium nitrate has an asserted anhydrous formula/synonym; the exact supplied hydration remains unspecified. Named solution additions and the 10 N acid stock are not pure-compound identities. Current secondary correspondence is not a validation of historical enrichment actions.

{"metrics": [{"input": "data/merge_yaml/merged/AGC2_Medium.yaml", "ingredient_instances": 11, "primary": 7, "current_secondary": 5, "primary_percent": 63.63636363636363, "current_secondary_percent": 45.45454545454545}, {"input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml", "ingredient_instances": 11, "primary": 7, "current_secondary": 5, "primary_percent": 63.63636363636363, "current_secondary_percent": 45.45454545454545}], "definition": "Ingredient-instance linkage percentages on a 0–100 scale, using each stated layer denominator; these are not scientific correctness scores.", "label_drift": []}

### Source-scoped preparation, conditions and physical-state branches

completeness: concern. Targets: CultureMech:009758.

Both layers omit the separately prepared Sol. 1 and iron/acid Sol. 2, the scoped Sol. 2 cycle, cooling/combination and later sterile yeast-stock addition. The final pH range is supported by both providers, while TOGO pH 3.0 and MediaDive scalar 1.8 must remain distinguished. Source volumes do not establish measured final volume, and the yeast-stock percent basis remains unqualified.

### Medium classification, applications and organism claim scope

scope: supported. Targets: CultureMech:009758.

COMPLEX/UNDEFINED is supported by the yeast-extract supplement despite the inorganic parent, and LIQUID matches the provider formulation without agar. The bacterial filing and generic cultivation application make no verified taxon, strain, habitat or growth claim. Parent source_environment annotations are explicitly excluded.

### Exact supplied chemical forms and mixture identity

grounding: concern. Targets: CultureMech:009758.

The source names calcium nitrate without a hydrate qualifier, while CHEBI:64205 has the anhydrous formula Ca.2NO3 and an anhydrous synonym. This is an unresolved source-form specificity, not proof of a wrong identifier or permission to select another hydrate. Preserve the source mass and obtain form evidence before any molar conversion.

### Claim-level formulation evidence and current annotations

evidence: concern. Targets: CultureMech:009758.

Target and owner source URLs and role notes do not supply claim-level amounts or preparation evidence. The three inspected parent J92 evidence objects support only parent quantities. Attach AGC2-specific excerpts and identify source stages; do not reuse parent environmental provenance or concentration normalization as AGC2 evidence.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009758.

21 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Source-stage repair in maintained owner and applicable writers

ownership: concern. Targets: CultureMech:009758.

Fix the exact TOGO owner using the AGC2 stage/amount inventory. Both water entries represent deliberate different stages; preserve the historical cleanup event and append a clarification. Recheck any future importer use against final-medium qualifiers and mixed-liquid stock basis before separately authorized regeneration.

## Findings

### f1: Solution stages, liquid volumes and calcium mass units are misrepresented

blocker / open / confirmed; issue key: cm009758-flattened-stages-and-unit-loss.

Both layers treat the 700/300 ml solution aliquots as 700/300 G_PER_L, merge distinct water aliquots into 1000 G_PER_L, write the 10 mg calcium-nitrate batch amount as 10 G_PER_L, and represent 5 ml of 10 N acid as 5 G_PER_L. Other Sol. 1 batch masses are flattened without an established final-volume denominator. The final iron and yeast values are explicitly supported and must be preserved without a second stock dilution.

### f2: Separate preparation, qualified stock addition and pH conflict are missing

major / open / confirmed; issue key: cm009758-preparation-ph-source-scope.

Neither local layer contains preparation, the separate iron/acid cycle, post-cooling assembly, sterile yeast-stock addition or final pH range. The unqualified 10% yeast-stock basis and provider pH disagreement prevent a fully specified replacement protocol. The accessible parent does not resolve the unavailable exact AGC2 source.

### f3: Calcium-nitrate hydration remains unverified

minor / open / confirmed; issue key: cm009758-calcium-form-specificity.

The source calcium-nitrate name is unqualified, while the valid CHEBI:64205 identity supplies an anhydrous formula and synonym. Matching canonical labels and current pinned secondary rows do not resolve the supplied hydration state.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the exact local preparation stages in the normalized owner, correct source unit and scope errors, and retain the provider-explicit final iron/yeast concentrations. Avoid double counting direct and stock constituents, density assumptions, invented stock identities or unsupported final-volume arithmetic. Attach exact quantity evidence before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Recover only the explicit AGC2 provider stages and range with exact excerpts, retain the unresolved pH/stock-basis limits, and seek the exact primary for closure. Do not copy parent environmental claims, substitute parent concentrations or impose its page default as confirmed AGC2 procedure.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the stated calcium-nitrate mass and explicitly qualify the unresolved source form. Obtain exact supplier/source form evidence before changing the identity or performing a molecular-weight conversion; do not invent a hydrate replacement.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AGC2_Medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AGC2_Medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AGC2_Medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch019/190/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch019/190/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AGC2_Medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AGC2_Medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AGC2_Medium.yaml:1:id: CultureMech:009758<br>./data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml:1:id: CultureMech:009758<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch019/source-preflight-bound/190/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 14 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| togoM377 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377; $.meta; all three $.components sections; $.comments[0] and [4] | supports | M377 identifies AGC2 Medium and original JCM_M382. Its main/solution sections preserve separate aliquots and the comment explicitly states final iron and yeast concentrations, AGC2-specific acid addition, separate treatment and final pH range. |
| mediadiveJ382api | https://mediadive.dsmz.de/rest/medium/J382; $.data.medium and $.data.solutions[0].steps[0] | supports | J382 is a step-only provider record. Its prose agrees with the AGC2 overrides and final pH range, while metadata gives a scalar pH 1.8. It supplies no numerical main-solution volume or ingredient recipe array. |
| jcm92 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=92; Complete parent 9K table, pH sentence and collection default | supports | The exact parent JCM 92 recipe is accessible and confirms the inherited salt identities and batch amounts. Its iron/acid values and preparation default belong to the parent and do not override AGC2-specific provider statements or authenticate unavailable JCM 382. |
| mediadiveJ92api | https://mediadive.dsmz.de/rest/medium/J92; Parent $.data.medium; $.data.solutions[0] | supports | The parent provider has its own declared volume, normalization and pH. These values cannot be transplanted into AGC2; parent identity and three existing parent concentration-evidence excerpts were checked separately. |
| jcm382-attempt | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=382; Preserved exact public retrieval result | context_only | The exact JCM GRMD=382 response returned HTTP 200 with Nothing found and no formulation. Required upstream AGC2 verification remains unavailable. Accessible JCM 92 and agreement between TOGO/MediaDive do not replace the exact unavailable primary. |
| parent-record | data/normalized_yaml/bacterial/9k_medium.yaml; Entire dependency record; three existing evidence objects; source_environment explicitly excluded | context_only | The exact parent ID/source and all fields were read. Three attached quantity snippets and response hashes match the bound J92 response, but support the parent only. Its CommunityMech environment notes, environmental quantities and ENVO linkage are not AGC2 growth, habitat, formulation or preparation evidence. No parent record review or correction is proposed. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch019/190/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | CHEBI:131527: dipotassium hydrogen phosphate. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | CHEBI:15377: water. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | CHEBI:31795: magnesium sulfate heptahydrate. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | CHEBI:32588: potassium chloride. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | CHEBI:62946: ammonium sulfate. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| chebi64205 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64205; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | CHEBI:64205: calcium nitrate. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | CHEBI:75836: iron(2+) sulfate heptahydrate. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| chemical-context | /private/tmp/culturemech-review-work-batch019/190/chemical-grounding-context.json; Every primary and current CHEBI-based secondary ingredient term in the target and maintained owners | context_only | Full OLS annotations, local instance locators, label differences, pinned exact-key MIM rows and layer-specific linkage metrics. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact identifier rows and pinned metadata source commit; no fuzzy replacements | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "current_secondary_rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:64205": [{"label": "Ca(NO3)2", "match_type": "preferred_term", "identifier": "CHEBI:64205", "preferred_term": "Ca(NO3)2", "ontology_id": "CHEBI:64205", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing": []} |
| history-metadata | data/merge_yaml/merged/AGC2_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml", "events": 10, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code handles named local sections, ml/mg units and preparation comments; it is not the old unconditional flattening path. Its local stock basis can still accept a reference equal to a water aliquot even when other liquid is present, and g/L rows in local sections retain their scalar without understanding a final-medium prose qualifier. These paths require source-aware review before reuse, not a claim of executed output. Current duplicate cleanup no longer sums disagreeing values; the older stored water sum and history remain. No historical process was replayed. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code handles named local sections, ml/mg units and preparation comments; it is not the old unconditional flattening path. Its local stock basis can still accept a reference equal to a water aliquot even when other liquid is present, and g/L rows in local sections retain their scalar without understanding a final-medium prose qualifier. These paths require source-aware review before reuse, not a claim of executed output. Current duplicate cleanup no longer sums disagreeing values; the older stored water sum and history remain. No historical process was replayed. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code handles named local sections, ml/mg units and preparation comments; it is not the old unconditional flattening path. Its local stock basis can still accept a reference equal to a water aliquot even when other liquid is present, and g/L rows in local sections retain their scalar without understanding a final-medium prose qualifier. These paths require source-aware review before reuse, not a claim of executed output. Current duplicate cleanup no longer sums disagreeing values; the older stored water sum and history remain. No historical process was replayed. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact JCM GRMD=382 response returned HTTP 200 with Nothing found and no formulation. Required upstream AGC2 verification remains unavailable. Accessible JCM 92 and agreement between TOGO/MediaDive do not replace the exact unavailable primary.
- Required JCM 382 formulation verification is unavailable; the accessible JCM 92 parent is not a substitute. Both current provider statements are used with their exact accession and stage limitations.
- The named 700/300 ml assembly, two water aliquots, additional acid and unspecified yeast-stock dose do not establish measured final volume. Final iron/yeast concentrations remain explicit source statements rather than quantities recalculated from those aliquots.
- Parent source_environment assertions and its existing evidence are excluded from AGC2 growth, habitat, taxonomy, amount normalization and preparation claims. No organism-specific optimization or new cultivation experiment is proposed.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T114928Z-culturemech-009758-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: agc2_medium (CultureMech:009758)'
started_at: '2026-10-21T11:43:30Z'
finished_at: '2026-10-21T11:49:28Z'
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
summary: TOGO M377 and MediaDive J382 preserve AGC2-specific overrides and separate
  preparation stages, but both local layers flatten solution additions and stock ingredients,
  merge two water aliquots as mass, and convert a calcium-nitrate mg amount and acid
  ml dose to g/L. Final iron and yeast concentrations are explicitly supported by
  provider prose and must not be diluted again. Exact JCM 382 is unavailable; accessible
  JCM 92 is bounded parent context, so this review remains partial.
source:
  git_revision: 24a1d277eb7f0437af53af0d178a30f9bfa6374c
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
  - path: data/merge_yaml/merged/AGC2_Medium.yaml
    sha256: 1c3c5f386007b0229cca00e11b205c6aadc4152d527f0883cc67f820902367bc
    role: target
  - path: data/normalized_yaml/bacterial/9k_medium.yaml
    sha256: 7c3855da19dcca522cb62809ce5c4f18c5cda3ea2de39b65e082aa38f13a867c
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml
    sha256: f37c8673aa5ff88a76168cf48c5332987a6050c89b3fe2a5e26243cb23d976b1
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
    sha256: 3576f5ce2adee0179be4f2d3fd134841249eb9a54a7eed8b388c3b345883a5fe
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
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
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
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/fetch/togo_fetcher.py
    sha256: 7aac40fe1d47e30810ae0be02f6e369ddb9bf657d630072595c62f46fb0bf339
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
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 190; batch 019 item 10 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding eighteen task batches
    contain 180 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 182 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009758
targets:
- target_id: CultureMech:009758
  path: data/merge_yaml/merged/AGC2_Medium.yaml
  label: agc2_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AGC2_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AGC2_Medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch019/190/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch019/190/strict.tsv"
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AGC2_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AGC2_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009758
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
  - CultureMech:009758
- check_id: jcm382-source-access
  name: 'Exact source content access: jcm382'
  required: true
  status: unavailable
  summary: The exact JCM GRMD=382 response returned HTTP 200 with Nothing found and
    no formulation. Required upstream AGC2 verification remains unavailable. Accessible
    JCM 92 and agreement between TOGO/MediaDive do not replace the exact unavailable
    primary.
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - jcm382-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AGC2_Medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:49:26Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:49:26Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AGC2_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:44.469362Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AGC2_Medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch019/190/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:45.946673Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch019/190/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AGC2_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:47.746314Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AGC2_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:48.735027Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:49:26Z'
  support: supports
  summary: './data/merge_yaml/merged/AGC2_Medium.yaml:1:id: CultureMech:009758

    ./data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml:1:id: CultureMech:009758

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/source-preflight-bound/190/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:49:26Z'
  support: supports
  summary: 14 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 98c52776f4c9097aca241a9d0e3ce8d1d14fad1f18f701e356b7d4a10f575ac9
- evidence_id: togoM377
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377
  locator: $.meta; all three $.components sections; $.comments[0] and [4]
  accessed_at: '2026-10-21T11:30:39.093369Z'
  support: supports
  summary: M377 identifies AGC2 Medium and original JCM_M382. Its main/solution sections
    preserve separate aliquots and the comment explicitly states final iron and yeast
    concentrations, AGC2-specific acid addition, separate treatment and final pH range.
  snapshot_sha256: f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496
- evidence_id: mediadiveJ382api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J382
  locator: $.data.medium and $.data.solutions[0].steps[0]
  accessed_at: '2026-10-21T11:30:38.449744Z'
  support: supports
  summary: J382 is a step-only provider record. Its prose agrees with the AGC2 overrides
    and final pH range, while metadata gives a scalar pH 1.8. It supplies no numerical
    main-solution volume or ingredient recipe array.
  snapshot_sha256: f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50
- evidence_id: jcm92
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=92
  locator: Complete parent 9K table, pH sentence and collection default
  accessed_at: '2026-10-21T09:00:12.131955Z'
  support: supports
  summary: The exact parent JCM 92 recipe is accessible and confirms the inherited
    salt identities and batch amounts. Its iron/acid values and preparation default
    belong to the parent and do not override AGC2-specific provider statements or
    authenticate unavailable JCM 382.
  snapshot_sha256: 3d608a40d0c3ac9e54aef695416957a54497252d2da61c1b12a481b88455bc2d
- evidence_id: mediadiveJ92api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J92
  locator: Parent $.data.medium; $.data.solutions[0]
  accessed_at: '2026-10-21T09:00:12.130263Z'
  support: supports
  summary: The parent provider has its own declared volume, normalization and pH.
    These values cannot be transplanted into AGC2; parent identity and three existing
    parent concentration-evidence excerpts were checked separately.
  snapshot_sha256: 867a8f1c9396fbdf0895d7573ba81dfb0d6723740e4a21498a4c1ba3f334e16a
- evidence_id: jcm382-attempt
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=382
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T11:30:40.261551Z'
  support: context_only
  summary: The exact JCM GRMD=382 response returned HTTP 200 with Nothing found and
    no formulation. Required upstream AGC2 verification remains unavailable. Accessible
    JCM 92 and agreement between TOGO/MediaDive do not replace the exact unavailable
    primary.
  snapshot_sha256: 5d30054c99b1ba979e6cbc6b6f3a0a7f14d633f5952dc3db948c20b33f5183e7
- evidence_id: parent-record
  kind: record_content
  reference: data/normalized_yaml/bacterial/9k_medium.yaml
  locator: Entire dependency record; three existing evidence objects; source_environment
    explicitly excluded
  accessed_at: '2026-10-21T11:49:26Z'
  support: context_only
  summary: The exact parent ID/source and all fields were read. Three attached quantity
    snippets and response hashes match the bound J92 response, but support the parent
    only. Its CommunityMech environment notes, environmental quantities and ENVO linkage
    are not AGC2 growth, habitat, formulation or preparation evidence. No parent record
    review or correction is proposed.
  snapshot_sha256: 7c3855da19dcca522cb62809ce5c4f18c5cda3ea2de39b65e082aa38f13a867c
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/190/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:49:26Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: ab02509e0b6e5cf7b106415cdbe626a7e4236472c0d78f88f5ee28fb96e84e47
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: 'CHEBI:131527: dipotassium hydrogen phosphate. Source-specific forms are
    assessed separately; valid ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: 'CHEBI:15377: water. Source-specific forms are assessed separately; valid
    ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: 'CHEBI:31795: magnesium sulfate heptahydrate. Source-specific forms are
    assessed separately; valid ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: 'CHEBI:32588: potassium chloride. Source-specific forms are assessed separately;
    valid ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: 'CHEBI:62946: ammonium sulfate. Source-specific forms are assessed separately;
    valid ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi64205
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64205
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-21T09:00:12.945373Z'
  support: supports
  summary: 'CHEBI:64205: calcium nitrate. Source-specific forms are assessed separately;
    valid ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: cf808711c3d8005562d7cb492a9da7abcb7a9ae6334934a1f4c5bafd1bd86062
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: 'CHEBI:75836: iron(2+) sulfate heptahydrate. Source-specific forms are
    assessed separately; valid ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chemical-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/190/chemical-grounding-context.json
  locator: Every primary and current CHEBI-based secondary ingredient term in the
    target and maintained owners
  accessed_at: '2026-10-21T11:49:26Z'
  support: context_only
  summary: Full OLS annotations, local instance locators, label differences, pinned
    exact-key MIM rows and layer-specific linkage metrics.
  snapshot_sha256: d22a213068999ded283f6acd246b071a5b4a314de80236fdd36e223306f9458c
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact identifier rows and pinned metadata source commit; no fuzzy replacements
  accessed_at: '2026-10-21T11:49:26Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "current_secondary_rows":
    {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier":
    "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water",
    "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4",
    "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:64205": [{"label": "Ca(NO3)2", "match_type": "preferred_term", "identifier":
    "CHEBI:64205", "preferred_term": "Ca(NO3)2", "ontology_id": "CHEBI:64205", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, "missing": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AGC2_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:49:26Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml", "events": 10, "timestamp_issues":
    []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:49:26Z'
  support: context_only
  summary: Current TOGO code handles named local sections, ml/mg units and preparation
    comments; it is not the old unconditional flattening path. Its local stock basis
    can still accept a reference equal to a water aliquot even when other liquid is
    present, and g/L rows in local sections retain their scalar without understanding
    a final-medium prose qualifier. These paths require source-aware review before
    reuse, not a claim of executed output. Current duplicate cleanup no longer sums
    disagreeing values; the older stored water sum and history remain. No historical
    process was replayed.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:49:26Z'
  support: context_only
  summary: Current TOGO code handles named local sections, ml/mg units and preparation
    comments; it is not the old unconditional flattening path. Its local stock basis
    can still accept a reference equal to a water aliquot even when other liquid is
    present, and g/L rows in local sections retain their scalar without understanding
    a final-medium prose qualifier. These paths require source-aware review before
    reuse, not a claim of executed output. Current duplicate cleanup no longer sums
    disagreeing values; the older stored water sum and history remain. No historical
    process was replayed.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:49:26Z'
  support: context_only
  summary: Current TOGO code handles named local sections, ml/mg units and preparation
    comments; it is not the old unconditional flattening path. Its local stock basis
    can still accept a reference equal to a water aliquot even when other liquid is
    present, and g/L rows in local sections retain their scalar without understanding
    a final-medium prose qualifier. These paths require source-aware review before
    reuse, not a claim of executed output. Current duplicate cleanup no longer sums
    disagreeing values; the older stored water sum and history remain. No historical
    process was replayed.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: AGC2 identity and bounded parent dependency
  outcome: supported
  summary: CultureMech:009758 and TOGO M377 resolve to original JCM_M382/MediaDive
    J382. The provider explicitly points to parent JCM 92 with overrides; the self-M377
    references label local Sol. 1/Sol. 2 sections, not a different external stock
    or a request to add the complete medium twice. Parent CultureMech:003277 is context
    only.
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togoM377
  - mediadiveJ382api
  - jcm92
  - mediadiveJ92api
  - parent-record
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 16 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence. All 22 ingredient and stock-dose concentration instances across
    the target and maintained owners are explicitly covered; additional rows retain
    preparation quantities and source-only components.
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"ingredient_or_context\": \"\
    Yeast extract final concentration\",\n    \"decision\": \"evidence_only\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_scope\": \"Retain\
    \ 0.5 G_PER_L in the receiving medium, supported explicitly by the AGC2 provider\
    \ statement.\",\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"togoM377\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"yeast extract\\\",\\n          \\\"volume\\\"\
    : 0.5,\\n          \\\"unit\\\": \\\"g/L\\\",\\n          \\\"conc_value\\\":\
    \ 10,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ382api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J382\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"0.5\
    \ g/L yeast extract\",\n        \"snapshot_sha256\": \"f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50\"\
    \n      }\n    ],\n    \"rationale\": \"The number and final-medium basis are\
    \ explicit and agree with both layers, but no attached local concentration evidence\
    \ exists. The separate 10% stock label does not license inventing its dose or\
    \ percent basis.\"\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"ingredient_or_context\"\
    : \"Solution 1 assembly aliquot\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"700\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"700\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"Preserve the source 700 ml local solution aliquot and exact matching section,\
    \ with composition and preparation separate from receiving-medium ingredients.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM377\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sol. 1\\\",\\n          \\\"volume\\\": 700,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\
    \n      }\n    ],\n    \"rationale\": \"A named solution aliquot is not a pure\
    \ ingredient or this number of grams per litre. The nominal aliquots do not settle\
    \ final volume after acid, solutes and the unspecified yeast-stock addition. Do\
    \ not infer a replacement external solution identifier.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q3\",\n    \"ingredient_or_context\": \"Solution 2 assembly aliquot\",\n \
    \   \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AGC2_Medium.yaml\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"300\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"300\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"Preserve the source 300 ml local solution aliquot and exact matching section,\
    \ with composition and preparation separate from receiving-medium ingredients.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM377\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sol. 2\\\",\\n          \\\"volume\\\": 300,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\
    \n      }\n    ],\n    \"rationale\": \"A named solution aliquot is not a pure\
    \ ingredient or this number of grams per litre. The nominal aliquots do not settle\
    \ final volume after acid, solutes and the unspecified yeast-stock addition. Do\
    \ not infer a replacement external solution identifier.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q4\",\n    \"ingredient_or_context\": \"Two water preparation aliquots\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1000.0\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"Preserve 700 ml in Sol. 1 and separately 300 ml in Sol. 2; remove the false\
    \ merged mass-concentration interpretation.\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"togoM377\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 700,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\n      },\n\
    \      {\n        \"source_key\": \"togoM377\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 300,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\n      }\n\
    \    ],\n    \"rationale\": \"The two source water rows occur in different preparation\
    \ stages. Their arithmetic sum is 1000 ml of listed water, not 1000 G_PER_L or\
    \ a verified final medium volume. They must not be double-counted in restored\
    \ solutions and direct ingredients.\"\n  },\n  {\n    \"quantity_id\": \"q5\"\
    ,\n    \"ingredient_or_context\": \"MgSO4・7H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"0.5 g in the source Sol. 1 batch, with its original water aliquot and receiving\
    \ assembly scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM377\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4・7H2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\
    \n      }\n    ],\n    \"rationale\": \"The provider states this mass in Sol.\
    \ 1 prepared with 700 ml water, not an independently supported concentration per\
    \ final litre. Preserve the raw batch mass and stage; do not use the parent J92\
    \ normalization or the water amount alone as a final-volume denominator.\"\n \
    \ },\n  {\n    \"quantity_id\": \"q6\",\n    \"ingredient_or_context\": \"K2HPO4\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"0.5 g in the source Sol. 1 batch, with its original water aliquot and receiving\
    \ assembly scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM377\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\
    \n      }\n    ],\n    \"rationale\": \"The provider states this mass in Sol.\
    \ 1 prepared with 700 ml water, not an independently supported concentration per\
    \ final litre. Preserve the raw batch mass and stage; do not use the parent J92\
    \ normalization or the water amount alone as a final-volume denominator.\"\n \
    \ },\n  {\n    \"quantity_id\": \"q7\",\n    \"ingredient_or_context\": \"KCl\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"0.1 g in the source Sol. 1 batch, with its original water aliquot and receiving\
    \ assembly scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM377\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.1,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\
    \n      }\n    ],\n    \"rationale\": \"The provider states this mass in Sol.\
    \ 1 prepared with 700 ml water, not an independently supported concentration per\
    \ final litre. Preserve the raw batch mass and stage; do not use the parent J92\
    \ normalization or the water amount alone as a final-volume denominator.\"\n \
    \ },\n  {\n    \"quantity_id\": \"q8\",\n    \"ingredient_or_context\": \"(NH4)2SO4\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"3 g in the source Sol. 1 batch, with its original water aliquot and receiving\
    \ assembly scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM377\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"(NH4)2SO4\\\",\\n          \\\"volume\\\": 3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\
    \n      }\n    ],\n    \"rationale\": \"The provider states this mass in Sol.\
    \ 1 prepared with 700 ml water, not an independently supported concentration per\
    \ final litre. Preserve the raw batch mass and stage; do not use the parent J92\
    \ normalization or the water amount alone as a final-volume denominator.\"\n \
    \ },\n  {\n    \"quantity_id\": \"q9\",\n    \"ingredient_or_context\": \"Ca(NO3)2\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[8].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\":\
    \ \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"10 mg in the source Sol. 1 batch, with its original water aliquot and receiving\
    \ assembly scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM377\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Ca(NO3)2\\\",\\n          \\\"volume\\\": 10,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\
    \n      }\n    ],\n    \"rationale\": \"The provider states this mass in Sol.\
    \ 1 prepared with 700 ml water, not an independently supported concentration per\
    \ final litre. Preserve the raw batch mass and stage; do not use the parent J92\
    \ normalization or the water amount alone as a final-volume denominator. The literal\
    \ source is 10 mg, whereas both layers assert 10 G_PER_L. This is a mass-unit\
    \ error as well as a stage/denominator error; the generic calcium-nitrate source\
    \ does not settle hydrate identity.\"\n  },\n  {\n    \"quantity_id\": \"q10\"\
    ,\n    \"ingredient_or_context\": \"Sulfuric acid stock dose and strength\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[9].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"5 ml of the source 10 N sulfuric-acid solution in Sol. 2; retain normality\
    \ as stock-strength context, not g/L or a guessed molarity.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM377\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\",\n     \
    \   \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10 N H2SO4\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 10,\\n  \
    \        \\\"conc_unit\\\": \\\"N\\\"\",\n        \"snapshot_sha256\": \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ382api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J382\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"5\
    \ ml 10 N H2SO4\",\n        \"snapshot_sha256\": \"f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50\"\
    \n      }\n    ],\n    \"rationale\": \"The ingredient name retains 10 N, but\
    \ its 5 G_PER_L concentration is dimensionally wrong. No acid density, purity\
    \ or unqualified equivalence-to-molarity conversion is supplied.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q11\",\n    \"ingredient_or_context\": \"Iron sulfate\
    \ heptahydrate final concentration\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"44.2\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[10].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"44.2\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_scope\": \"Retain\
    \ 44.2 G_PER_L as the explicitly stated final-medium iron-salt concentration;\
    \ retain its separately treated Sol. 2 preparation role.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM377\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\",\n     \
    \   \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4・7H2O\\\",\\n          \\\"volume\\\": 44.2,\\\
    n          \\\"unit\\\": \\\"g/L\\\"\",\n        \"snapshot_sha256\": \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ382api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J382\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"44.2\
    \ g/L (final) FeSO4 x 7H2O\",\n        \"snapshot_sha256\": \"f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50\"\
    \n      }\n    ],\n    \"rationale\": \"The explicit final qualifier controls\
    \ over the row being nested in the Sol. 2 section. Do not turn 44.2 g/L into 44.2\
    \ g per 300 ml, apply a second 0.3 dilution, or replace it with the parent iron\
    \ amount. Neither local layer has attached evidence.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q12\",\n    \"ingredient_or_context\": \"Yeast-stock working dose and unspecified\
    \ percentage basis\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"not_quantified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"not_quantified\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"Retain the literal 10% stock description and separate sterile addition; working\
    \ volume and w/v, w/w or v/v basis are unresolved.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM377\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\",\n     \
    \   \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"yeast extract\\\",\\n          \\\"volume\\\"\
    : 0.5,\\n          \\\"unit\\\": \\\"g/L\\\",\\n          \\\"conc_value\\\":\
    \ 10,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ382api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J382\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"sterile\
    \ stock solution (10%)\",\n        \"snapshot_sha256\": \"f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50\"\
    \n      }\n    ],\n    \"rationale\": \"This decision concerns the unquantified\
    \ working dose and unsupported percentage basis, not absence of the printed number\
    \ 10. The final yeast amount is separately supported; no working volume follows\
    \ without verified stock strength on a defined basis.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q13\",\n    \"ingredient_or_context\": \"Final pH range\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_scope\": \"Preserve\
    \ final pH 1.5–2.0 from both provider preparation statements, with final-stage\
    \ scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM377\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\"\
    ,\n        \"source_locator\": \"$.meta.ph\",\n        \"exact_source_quote\"\
    : \"\\\"ph\\\": \\\"1.5-2.0\\\"\",\n        \"snapshot_sha256\": \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ382api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J382\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Check\
    \ the final pH to be 1.5 - 2.0.\",\n        \"snapshot_sha256\": \"f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50\"\
    \n      }\n    ],\n    \"rationale\": \"No pH field or preparation exists in either\
    \ layer. Do not replace the supported range by a midpoint or treat a provider\
    \ scalar as the range itself.\"\n  },\n  {\n    \"quantity_id\": \"q14\",\n  \
    \  \"ingredient_or_context\": \"Conflicting pH metadata and inherited adjustment\
    \ sentence\",\n    \"decision\": \"conflict\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\",\n      \
    \  \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n       \
    \ \"decision\": \"conflict\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"conflict\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"Keep TOGO’s separate pH 3.0 sentence and MediaDive scalar 1.8 as conflicting/contextual\
    \ provider metadata pending exact-primary resolution; do not silently synthesize\
    \ a sequential adjustment protocol.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM377\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M377\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 3.0.\",\n        \"snapshot_sha256\": \"f471930488026ecd74c4157f6db8f1e4d8e99802c98daf391c55b78ae9cba496\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ382api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J382\",\n        \"source_locator\"\
    : \"$.data.medium.min_pH\",\n        \"exact_source_quote\": \"\\\"min_pH\\\"\
    : 1.8\",\n        \"snapshot_sha256\": \"f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ382api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J382\",\n        \"source_locator\"\
    : \"$.data.medium.max_pH\",\n        \"exact_source_quote\": \"\\\"max_pH\\\"\
    : 1.8\",\n        \"snapshot_sha256\": \"f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50\"\
    \n      }\n    ],\n    \"rationale\": \"The parent has pH 3.0, but inheritance\
    \ does not establish the role of that extra sentence in the final AGC2 recipe.\
    \ The final-range prose is explicit; its exact relationship to the scalar and\
    \ separate sentence remains unresolved.\"\n  },\n  {\n    \"quantity_id\": \"\
    q15\",\n    \"ingredient_or_context\": \"Separate Sol. 2 sterilization cycle\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AGC2_Medium.yaml\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"Retain the source 110°C for 30 min only for the separate iron/acid solution,\
    \ followed by cooling and combination.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadiveJ382api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/J382\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n      \
    \  \"exact_source_quote\": \"autoclave at 110C for 30 min.\",\n        \"snapshot_sha256\"\
    : \"f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50\"\n     \
    \ }\n    ],\n    \"rationale\": \"Both layers omit the cycle and the source stage.\
    \ Do not apply it universally to all ingredients or treat it as an incubation\
    \ condition.\"\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"ingredient_or_context\"\
    : \"Sol. 1 sterilization temperature and duration\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AGC2_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null,\n   \
    \     \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml\",\n        \"field_path\"\
    : \"sterilization\",\n        \"stored\": null,\n        \"decision\": \"not_quantified\"\
    \n      }\n    ],\n    \"proposed_source_scope\": \"Provider specifies autoclaving\
    \ Sol. 1 without its own explicit cycle; retain that limit while the exact JCM\
    \ 382 primary is unavailable.\",\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadiveJ382api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/J382\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n      \
    \  \"exact_source_quote\": \"in 700 ml distilled water and autoclave.\",\n   \
    \     \"snapshot_sha256\": \"f793dafcb91e88732e3400bc4be505cb8a3bef250030ee8d8eefffb0350e9f50\"\
    \n      }\n    ],\n    \"rationale\": \"The accessible parent collection-page\
    \ default is not independently verified on the unavailable AGC2 primary. No cycle\
    \ is inserted from an unrelated page or assigned to the entire recipe.\"\n  }\n\
    ]"
- assessment_id: grounding
  area: grounding
  topic: Source-specific forms and current CHEBI-based secondary correspondence
  outcome: concern
  summary: '7 distinct asserted chemical IDs resolve as nonobsolete. 0 local label
    instances differ from canonical labels. 5 of 5 distinct current CHEBI-based secondary
    keys have exact mapped preferred-term rows in the pinned index; unresolved keys:
    []. This does not validate historical legacy MIM IDs, supplied hydrates, stereochemistry
    or catalog products. Source magnesium/iron sulfate heptahydrates match the asserted
    hydrate terms. Generic calcium nitrate has an asserted anhydrous formula/synonym;
    the exact supplied hydration remains unspecified. Named solution additions and
    the 10 N acid stock are not pure-compound identities. Current secondary correspondence
    is not a validation of historical enrichment actions.'
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - record
  - chemical-context
  - mim
  - owner-0
  - chebi131527
  - chebi15377
  - chebi31795
  - chebi32588
  - chebi62946
  - chebi64205
  - chebi75836
  details: '{"metrics": [{"input": "data/merge_yaml/merged/AGC2_Medium.yaml", "ingredient_instances":
    11, "primary": 7, "current_secondary": 5, "primary_percent": 63.63636363636363,
    "current_secondary_percent": 45.45454545454545}, {"input": "data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml",
    "ingredient_instances": 11, "primary": 7, "current_secondary": 5, "primary_percent":
    63.63636363636363, "current_secondary_percent": 45.45454545454545}], "definition":
    "Ingredient-instance linkage percentages on a 0–100 scale, using each stated layer
    denominator; these are not scientific correctness scores.", "label_drift": []}'
- assessment_id: preparation
  area: completeness
  topic: Source-scoped preparation, conditions and physical-state branches
  outcome: concern
  summary: Both layers omit the separately prepared Sol. 1 and iron/acid Sol. 2, the
    scoped Sol. 2 cycle, cooling/combination and later sterile yeast-stock addition.
    The final pH range is supported by both providers, while TOGO pH 3.0 and MediaDive
    scalar 1.8 must remain distinguished. Source volumes do not establish measured
    final volume, and the yeast-stock percent basis remains unqualified.
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - record
  - owner-0
  - togoM377
  - mediadiveJ382api
  - jcm92
  - mediadiveJ92api
  - parent-record
- assessment_id: classification
  area: scope
  topic: Medium classification, applications and organism claim scope
  outcome: supported
  summary: COMPLEX/UNDEFINED is supported by the yeast-extract supplement despite
    the inorganic parent, and LIQUID matches the provider formulation without agar.
    The bacterial filing and generic cultivation application make no verified taxon,
    strain, habitat or growth claim. Parent source_environment annotations are explicitly
    excluded.
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - record
  - owner-0
  - togoM377
  - mediadiveJ382api
  - jcm92
  - mediadiveJ92api
  - parent-record
- assessment_id: forms
  area: grounding
  topic: Exact supplied chemical forms and mixture identity
  outcome: concern
  summary: The source names calcium nitrate without a hydrate qualifier, while CHEBI:64205
    has the anhydrous formula Ca.2NO3 and an anhydrous synonym. This is an unresolved
    source-form specificity, not proof of a wrong identifier or permission to select
    another hydrate. Preserve the source mass and obtain form evidence before any
    molar conversion.
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - record
  - chemical-context
  - owner-0
  - togoM377
  - mediadiveJ382api
  - jcm92
  - mediadiveJ92api
  - parent-record
- assessment_id: evidence-placement
  area: evidence
  topic: Claim-level formulation evidence and current annotations
  outcome: concern
  summary: Target and owner source URLs and role notes do not supply claim-level amounts
    or preparation evidence. The three inspected parent J92 evidence objects support
    only parent quantities. Attach AGC2-specific excerpts and identify source stages;
    do not reuse parent environmental provenance or concentration normalization as
    AGC2 evidence.
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - record
  - quantity-inventory
  - owner-0
  - togoM377
  - mediadiveJ382api
  - jcm92
  - mediadiveJ92api
  - parent-record
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 21 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: ownership
  area: ownership
  topic: Source-stage repair in maintained owner and applicable writers
  outcome: concern
  summary: Fix the exact TOGO owner using the AGC2 stage/amount inventory. Both water
    entries represent deliberate different stages; preserve the historical cleanup
    event and append a clarification. Recheck any future importer use against final-medium
    qualifiers and mixed-liquid stock basis before separately authorized regeneration.
  target_ids:
  - CultureMech:009758
  evidence_ids:
  - record
  - owner-0
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: cm009758-flattened-stages-and-unit-loss
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Solution stages, liquid volumes and calcium mass units are misrepresented
  description: Both layers treat the 700/300 ml solution aliquots as 700/300 G_PER_L,
    merge distinct water aliquots into 1000 G_PER_L, write the 10 mg calcium-nitrate
    batch amount as 10 G_PER_L, and represent 5 ml of 10 N acid as 5 G_PER_L. Other
    Sol. 1 batch masses are flattened without an established final-volume denominator.
    The final iron and yeast values are explicitly supported and must be preserved
    without a second stock dilution.
  target_ids:
  - CultureMech:009758
  field_paths:
  - ingredients[1:10].concentration
  - ingredients[3].notes
  - solutions
  evidence_ids:
  - record
  - owner-0
  - quantity-inventory
  - togoM377
  - mediadiveJ382api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml
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
  issue_key: cm009758-preparation-ph-source-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Separate preparation, qualified stock addition and pH conflict are missing
  description: Neither local layer contains preparation, the separate iron/acid cycle,
    post-cooling assembly, sterile yeast-stock addition or final pH range. The unqualified
    10% yeast-stock basis and provider pH disagreement prevent a fully specified replacement
    protocol. The accessible parent does not resolve the unavailable exact AGC2 source.
  target_ids:
  - CultureMech:009758
  field_paths:
  - preparation_steps
  - sterilization
  - ph_range
  - references
  - ingredients[*].evidence
  evidence_ids:
  - record
  - owner-0
  - quantity-inventory
  - togoM377
  - mediadiveJ382api
  - jcm382-attempt
  - parent-record
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: cm009758-calcium-form-specificity
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Calcium-nitrate hydration remains unverified
  description: The source calcium-nitrate name is unqualified, while the valid CHEBI:64205
    identity supplies an anhydrous formula and synonym. Matching canonical labels
    and current pinned secondary rows do not resolve the supplied hydration state.
  target_ids:
  - CultureMech:009758
  field_paths:
  - ingredients[8].term
  - ingredients[8].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - chebi64205
  - chemical-context
  - togoM377
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml
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
  description: Reconstruct the exact local preparation stages in the normalized owner,
    correct source unit and scope errors, and retain the provider-explicit final iron/yeast
    concentrations. Avoid double counting direct and stock constituents, density assumptions,
    invented stock identities or unsupported final-volume arithmetic. Attach exact
    quantity evidence before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009758
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml
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
  description: Recover only the explicit AGC2 provider stages and range with exact
    excerpts, retain the unresolved pH/stock-basis limits, and seek the exact primary
    for closure. Do not copy parent environmental claims, substitute parent concentrations
    or impose its page default as confirmed AGC2 procedure.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009758
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml
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
  description: Preserve the stated calcium-nitrate mass and explicitly qualify the
    unresolved source form. Obtain exact supplier/source form evidence before changing
    the identity or performing a molecular-weight conversion; do not invent a hydrate
    replacement.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009758
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M377_AGC2_Medium.yaml
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
- The exact JCM GRMD=382 response returned HTTP 200 with Nothing found and no formulation.
  Required upstream AGC2 verification remains unavailable. Accessible JCM 92 and agreement
  between TOGO/MediaDive do not replace the exact unavailable primary.
- Required JCM 382 formulation verification is unavailable; the accessible JCM 92
  parent is not a substitute. Both current provider statements are used with their
  exact accession and stage limitations.
- The named 700/300 ml assembly, two water aliquots, additional acid and unspecified
  yeast-stock dose do not establish measured final volume. Final iron/yeast concentrations
  remain explicit source statements rather than quantities recalculated from those
  aliquots.
- Parent source_environment assertions and its existing evidence are excluded from
  AGC2 growth, habitat, taxonomy, amount normalization and preparation claims. No
  organism-specific optimization or new cultivation experiment is proposed.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-019
- generated-medium
```
