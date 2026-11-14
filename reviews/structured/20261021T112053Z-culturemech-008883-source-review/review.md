# Source and formulation review: acidithiobacillus_ferrooxidans_medium (CultureMech:008883)

- Review: 20261021T112053Z-culturemech-008883-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T11:17:50Z
- Finished UTC: 2026-10-21T11:20:53Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

ATCC 2039 / TOGO M2297 identity is resolved, but the represented formulation combines solution and stock batches, assigns unrelated A/B references and loses source preparation scope. Source-stage reconstruction is needed before this record is usable as the named medium.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 175; batch 018 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seventeen task batches contain 170 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 172 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008883 | data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml | generated | acidithiobacillus_ferrooxidans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008883 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008883 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch018/175/strict.tsv |
| validate-terms | passed | True | CultureMech:008883 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008883 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008883 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008883.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:008883.

16 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 15/16 primary and 15/16 secondary instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 16: primary 93.75%; secondary 93.75%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:008883.

29 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact source and stock identity

identity: concern. Targets: CultureMech:008883.

TOGO M2297 and the original ATCC 2039 title agree. Both reviewed layers contain the same 16 direct rows and four solution descriptors. ATCC Solution A is ammonium sulfate, magnesium sulfate, phosphate, water and a Wolfe aliquot; Solution B is ferrous sulfate and water. MediaDive 5342 instead contains yeast extract, casamino acids and 100 g NaCl among eight rows; 5343 contains 80 g carbonate and 100 g NaCl. Their local stock IDs resolve to CultureMech:014254/014255, but they are scientifically wrong associations. No replacement stock ID is invented.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:008883.

28 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "field_path": "solutions[0].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "TOGO complete-medium A/B aliquot declarations",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Solution A\",\n          \"volume\": 800,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "TOGO declares 800 ml of this local A/B solution, not g/L. ATCC prints the associated water batch and instructs combining the prepared solutions; retain that source distinction and do not substitute the unrelated MediaDive stock.",
    "source_name": "Solution A",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 800,
    "source_original_unit": "ml"
  },
  {
    "field_path": "solutions[1].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "TOGO complete-medium A/B aliquot declarations",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Solution B\",\n          \"volume\": 200,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "TOGO declares 200 ml of this local A/B solution, not g/L. ATCC prints the associated water batch and instructs combining the prepared solutions; retain that source distinction and do not substitute the unrelated MediaDive stock.",
    "source_name": "Solution B",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 200,
    "source_original_unit": "ml"
  },
  {
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Solution A",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"MgSO4 x 7 H2O\",\n          \"volume\": 2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "Restore this exact source batch amount and stage; the current per-liter/direct-medium placement is not established by this source row. No final working concentration is inferred.",
    "source_name": "MgSO4 x 7 H2O",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 2,
    "source_original_unit": "g",
    "arithmetic": "The recorded 5.0 is the unscaled sum 2.0 + 3.0 from Solution A and the Wolfe stock. These are different stages; adding them does not calculate the final medium concentration."
  },
  {
    "field_path": "ingredients[1].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Solution A",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "Restore this exact source batch amount and stage; the current per-liter/direct-medium placement is not established by this source row. No final working concentration is inferred.",
    "source_name": "K2HPO4",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 0.4,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[2].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Solution A",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"(NH4)2SO4\",\n          \"volume\": 0.8,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "Restore this exact source batch amount and stage; the current per-liter/direct-medium placement is not established by this source row. No final working concentration is inferred.",
    "source_name": "(NH4)2SO4",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 0.8,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[3].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Solution A",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"DI Water\",\n          \"volume\": 800,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This is a literal liquid volume in the named stage, not a mass concentration. Keep source water and stock aliquots separate; water volumes alone do not establish final volume.",
    "source_name": "DI Water",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 800,
    "source_original_unit": "ml",
    "arithmetic": "The recorded 2000 is 800 + 200 + 1000 ml across A, B and a separately prepared stock. Neither that sum nor a density assumption supports 2000 g/L."
  },
  {
    "field_path": "solutions[2].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Solution A",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"*Wolfe's Mineral Solution (see below)\",\n          \"volume\": 5,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This is a literal liquid volume in the named stage, not a mass concentration. Keep source water and stock aliquots separate; water volumes alone do not establish final volume.",
    "source_name": "*Wolfe's Mineral Solution (see below)",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 5,
    "source_original_unit": "ml"
  },
  {
    "field_path": "ingredients[4].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Solution A",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"H2SO4\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "The source specifies an adjustment reagent with a pH endpoint but no fixed dose or stock strength. Retain the nonnumeric amount with the correct solution/stock scope and endpoint; do not manufacture a concentration.",
    "source_name": "H2SO4",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": null,
    "source_original_unit": null
  },
  {
    "field_path": "ingredients[5].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Solution B",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"FeSO4 x 7 H2O\",\n          \"volume\": 20,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "Restore this exact source batch amount and stage; the current per-liter/direct-medium placement is not established by this source row. No final working concentration is inferred.",
    "source_name": "FeSO4 x 7 H2O",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 20,
    "source_original_unit": "g",
    "arithmetic": "The recorded 20.1 is the unscaled sum 20.0 + 0.1 from Solution B and the Wolfe stock. This is not a valid stock dilution."
  },
  {
    "field_path": "ingredients[3].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Solution B",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"DI Water\",\n          \"volume\": 200,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This is a literal liquid volume in the named stage, not a mass concentration. Keep source water and stock aliquots separate; water volumes alone do not establish final volume.",
    "source_name": "DI Water",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 200,
    "source_original_unit": "ml",
    "arithmetic": "The recorded 2000 is 800 + 200 + 1000 ml across A, B and a separately prepared stock. Neither that sum nor a density assumption supports 2000 g/L."
  },
  {
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"MgSO4 x 7 H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This amount belongs to the separately prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition and dose hierarchy rather than retaining an undiluted final-medium row.",
    "source_name": "MgSO4 x 7 H2O",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 3,
    "source_original_unit": "g",
    "arithmetic": "The recorded 5.0 is the unscaled sum 2.0 + 3.0 from Solution A and the Wolfe stock. These are different stages; adding them does not calculate the final medium concentration."
  },
  {
    "field_path": "ingredients[6].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This amount belongs to the separately prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition and dose hierarchy rather than retaining an undiluted final-medium row.",
    "source_name": "NaCl",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 1,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4 x 2 H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This amount belongs to the separately prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition and dose hierarchy rather than retaining an undiluted final-medium row.",
    "source_name": "Na2MoO4 x 2 H2O",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 0.01,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This amount belongs to the separately prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition and dose hierarchy rather than retaining an undiluted final-medium row.",
    "source_name": "H3BO3",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 0.01,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[5].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[4]",
        "exact_source_quote": "\"component_name\": \"FeSO4 x 7 H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This amount belongs to the separately prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition and dose hierarchy rather than retaining an undiluted final-medium row.",
    "source_name": "FeSO4 x 7 H2O",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 0.1,
    "source_original_unit": "g",
    "arithmetic": "The recorded 20.1 is the unscaled sum 20.0 + 0.1 from Solution B and the Wolfe stock. This is not a valid stock dilution."
  },
  {
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[5]",
        "exact_source_quote": "\"component_name\": \"CoCl2 x 6 H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This amount belongs to the separately prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition and dose hierarchy rather than retaining an undiluted final-medium row.",
    "source_name": "CoCl2 x 6 H2O",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 0.1,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[6]",
        "exact_source_quote": "\"component_name\": \"ZnSO4 x 7 H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This amount belongs to the separately prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition and dose hierarchy rather than retaining an undiluted final-medium row.",
    "source_name": "ZnSO4 x 7 H2O",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 0.1,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[7]",
        "exact_source_quote": "\"component_name\": \"CuSO4 x 5 H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This amount belongs to the separately prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition and dose hierarchy rather than retaining an undiluted final-medium row.",
    "source_name": "CuSO4 x 5 H2O",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 0.01,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[8]",
        "exact_source_quote": "\"component_name\": \"AlK(SO4)2 x 12H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This amount belongs to the separately prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition and dose hierarchy rather than retaining an undiluted final-medium row.",
    "source_name": "AlK(SO4)2 x 12H2O",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 0.01,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[9]",
        "exact_source_quote": "\"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This amount belongs to the separately prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition and dose hierarchy rather than retaining an undiluted final-medium row.",
    "source_name": "Nitrilotriacetic acid",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 1.5,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[10]",
        "exact_source_quote": "\"component_name\": \"CaCl2\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This amount belongs to the separately prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition and dose hierarchy rather than retaining an undiluted final-medium row.",
    "source_name": "CaCl2",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 0.1,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[15].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[11]",
        "exact_source_quote": "\"component_name\": \"MnSO4 x H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This amount belongs to the separately prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition and dose hierarchy rather than retaining an undiluted final-medium row.",
    "source_name": "MnSO4 x H2O",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 0.5,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[3].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[12]",
        "exact_source_quote": "\"component_name\": \"DI Water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "This is a literal liquid volume in the named stage, not a mass concentration. Keep source water and stock aliquots separate; water volumes alone do not establish final volume.",
    "source_name": "DI Water",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": 1000,
    "source_original_unit": "ml",
    "arithmetic": "The recorded 2000 is 800 + 200 + 1000 ml across A, B and a separately prepared stock. Neither that sum nor a density assumption supports 2000 g/L."
  },
  {
    "field_path": "solutions[3].concentration",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "correct"
    },
    "source_stage": "Wolfe's Mineral Solution",
    "source_snippets": [
      {
        "source_key": "togoM2297",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297",
        "source_locator": "$.components[3].items[13]",
        "exact_source_quote": "\"component_name\": \"Potassium hydroxide solution\"",
        "snapshot_sha256": "97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f"
      }
    ],
    "explanation": "The source specifies an adjustment reagent with a pH endpoint but no fixed dose or stock strength. Retain the nonnumeric amount with the correct solution/stock scope and endpoint; do not manufacture a concentration.",
    "source_name": "Potassium hydroxide solution",
    "primary_source_evidence_id": "atcc2039",
    "source_original_amount": null,
    "source_original_unit": null
  },
  {
    "field_path": "solutions[0].preparation.pH",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "add"
    },
    "source_stage": "Solution A",
    "source_snippets": [
      {
        "source_key": "atccOriginal",
        "source_url": "https://www.atcc.org/~/media/4C29EA2E2A0749BB9354D8AC64AA715B.ashx",
        "source_locator": "ATCC 2039 PDF, corresponding A or Wolfe preparation paragraph",
        "exact_source_quote": "Adjust Solution A to pH 2.3 with H2SO4 and filter-sterilize.",
        "snapshot_sha256": "dfbbe0099b70c8a5dc13ab2861c29f7a76477a6ab087bf1c65fa3fb3abe51ead",
        "parsed_text_sha256": "b05f12680a7368101f2cb413a108866e6a8918f788c50585f312c11d1bc5e73b"
      }
    ],
    "explanation": "Add the source-specific pH 2.3 endpoint and acid/filter preparation; it is not a reported final complete-medium pH.",
    "primary_source_evidence_id": "atcc2039"
  },
  {
    "field_path": "solutions[2].preparation.initial_water",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "add"
    },
    "source_stage": "Wolfe stock initial dissolution",
    "source_snippets": [
      {
        "source_key": "atccOriginal",
        "source_url": "https://www.atcc.org/~/media/4C29EA2E2A0749BB9354D8AC64AA715B.ashx",
        "source_locator": "ATCC 2039 PDF, corresponding A or Wolfe preparation paragraph",
        "exact_source_quote": "approximately 500 ml of water",
        "snapshot_sha256": "dfbbe0099b70c8a5dc13ab2861c29f7a76477a6ab087bf1c65fa3fb3abe51ead",
        "parsed_text_sha256": "b05f12680a7368101f2cb413a108866e6a8918f788c50585f312c11d1bc5e73b"
      }
    ],
    "explanation": "Preserve approximate 500 ml for initial NTA dissolution, not a second water addition on top of the stock batch.",
    "primary_source_evidence_id": "atcc2039"
  },
  {
    "field_path": "solutions[2].preparation.pH",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "add"
    },
    "source_stage": "Wolfe stock NTA dissolution",
    "source_snippets": [
      {
        "source_key": "atccOriginal",
        "source_url": "https://www.atcc.org/~/media/4C29EA2E2A0749BB9354D8AC64AA715B.ashx",
        "source_locator": "ATCC 2039 PDF, corresponding A or Wolfe preparation paragraph",
        "exact_source_quote": "adjust to pH 6.5",
        "snapshot_sha256": "dfbbe0099b70c8a5dc13ab2861c29f7a76477a6ab087bf1c65fa3fb3abe51ead",
        "parsed_text_sha256": "b05f12680a7368101f2cb413a108866e6a8918f788c50585f312c11d1bc5e73b"
      }
    ],
    "explanation": "Add stock-specific pH 6.5 with KOH; no fixed KOH amount or strength is supplied.",
    "primary_source_evidence_id": "atcc2039"
  },
  {
    "field_path": "solutions[2].preparation.water_makeup",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml": "add"
    },
    "source_stage": "Wolfe stock after NTA dissolution, before other compounds",
    "source_snippets": [
      {
        "source_key": "atccOriginal",
        "source_url": "https://www.atcc.org/~/media/4C29EA2E2A0749BB9354D8AC64AA715B.ashx",
        "source_locator": "ATCC 2039 PDF, corresponding A or Wolfe preparation paragraph",
        "exact_source_quote": "Bring volume to 1000 ml with remaining",
        "snapshot_sha256": "dfbbe0099b70c8a5dc13ab2861c29f7a76477a6ab087bf1c65fa3fb3abe51ead",
        "parsed_text_sha256": "b05f12680a7368101f2cb413a108866e6a8918f788c50585f312c11d1bc5e73b"
      }
    ],
    "explanation": "Preserve the source order: bring volume to 1000 ml, then add remaining compounds one at a time. Do not silently rewrite this as measured final volume after all solutes.",
    "primary_source_evidence_id": "atcc2039"
  }
]

### A/B filtration, stock dissolution and pH scope

completeness: concern. Targets: CultureMech:008883.

Neither local layer retains the source instructions. ATCC requires A pH 2.3 with sulfuric acid and filtration, rapid dissolution/filtration of B, aseptic combination and dispensing, and a separate NTA/KOH pH 6.5 dissolution/makeup sequence for Wolfe stock. The yellow precipitate/iron-oxidation note is source context. No generic autoclave cycle is substituted. ATCC permits MD-TMS as an alternative, but no product composition or formulation equivalence beyond that explicit option is asserted.

### All named salts, hydrates and adjustment reagents

grounding: concern. Targets: CultureMech:008883.

The primary terms preserve the explicitly supplied sulfate/chloride hydrates, including CoCl2 hexahydrate and potassium aluminium sulfate dodecahydrate. Calcium chloride has no hydrate specified; no hydrate or molar conversion is invented. MgSO4 heptahydrate is correctly primary-grounded to CHEBI:31795, but its secondary key remains generic CHEBI:32599 despite the later primary correction. Sulfuric acid identity does not establish an unspecified solution strength.

### Medium classification and physical state

scope: concern. Targets: CultureMech:008883.

Bacterial placement and liquid state agree with the named source. COMPLEX/UNDEFINED is not supported for this explicit formulation of named chemicals and a specified mineral stock. An optional commercial substitute is not evidence that the current stated recipe uses an undefined mixture. Classification must follow the reconstructed source branch, with reagent-strength uncertainty kept separate from compositional classification.

### Owner correspondence and current writer context

provenance: supported. Targets: CultureMech:008883.

The maintained owner and generated copy have matching formulation fields; the generated merge history adds provenance, not scientific evidence. The old cleanup notes explicitly retain cross-stage sums, while current cleanup avoids this summing behavior. Correct the normalized owner and source-specific references before separately authorized regeneration. No runtime or historical replay is claimed.

### Biological identifiers, cultivation claims and literature scope

scope: supported. Targets: CultureMech:008883.

The medium title, generic cultivation application and source-specific strain instructions do not establish an experimental growth result or a taxon/strain equivalence. No target-organism CURIE, genome assembly, DOI or PMID is asserted in the reviewed target or maintained owners. No organism identifier, incubation optimum or unreported growth claim is added.

## Findings

### f1: The represented formulation does not preserve ATCC 2039 solution identity

blocker / open / confirmed; issue key: cm008883-formulation-stage-and-stock-identity.

A/B/Wolfe stages are flattened into 16 direct rows, including unscaled Mg and Fe sums and 2000 g/L water; 800/200/5 ml additions are encoded as g/L. Two resolvable stock IDs denote unrelated high-salt formulations. These combined defects make the encoded recipe materially different from the named ATCC medium.

### f2: Source-specific filtration and stock preparation are missing

major / open / confirmed; issue key: cm008883-source-preparation-missing.

The omitted filtration, aseptic mixing and distinct pH 2.3/6.5 operations determine how the staged recipe is prepared; their absence materially limits reproducibility.

### f3: Secondary magnesium linkage loses the source heptahydrate form

major / open / confirmed; issue key: cm008883-secondary-magnesium-form.

Both layers retain generic magnesium sulfate CHEBI:32599 as secondary identity although the source and corrected primary term specify magnesium sulfate heptahydrate CHEBI:31795. Exact existence in the pinned MIM index does not validate this broader correspondence.

### f4: Complex and undefined classification lacks source support

major / open / confirmed; issue key: cm008883-classification-source-support.

The exact stated source recipe specifies named chemical components and a defined mineral-stock recipe; no undefined nutrient mixture is identified for the selected branch.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the exact A/B/Wolfe hierarchy in the normalized owner, remove or replace the unsupported 5342/5343 associations only after source-specific identity resolution, preserve literal batch units and attach scoped evidence. Do not compute a final concentration from unspecified final volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore exact source preparation in the correct A/B/Wolfe scopes, preserving nonnumeric acid/base doses, order and optional substitution boundary; do not invent autoclave conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Reconcile the secondary key with the explicit heptahydrate using the pinned resolver/index and source evidence; preserve the actual supplied hydrate and the independently corrected stock quantities.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Reassess composition and medium type from the restored source formulation; preserve the commercial-substitute option as a separate qualified branch rather than using it to justify the base classification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch018/175/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch018/175/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml:1:id: CultureMech:008883<br>./data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml:1:id: CultureMech:008883<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch018/source-preflight-bound/175/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 25 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| atcc2039 | https://www.atcc.org/~/media/4C29EA2E2A0749BB9354D8AC64AA715B.ashx; Complete ATCC Medium 2039 PDF: Solution A, Solution B, Complete Medium and Wolfe mineral sections | supports | The exact original collection URL resolves to ATCC 2039. Its A/B preparation and Wolfe stock are separate stages; all amounts and preparation passages were read. |
| togoM2297 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297; meta; all four components sections; all comments | supports | Exact TOGO M2297 points to the same ATCC document and preserves local section identity, original g/ml amounts and preparation comments. |
| solution5342 | https://mediadive.dsmz.de/rest/solution/5342; $.data.id, name, complete recipe and steps | refutes | This asserted MediaDive stock resolves, but its composition belongs to a different formulation; generic A/B names do not establish correspondence. |
| solution5343 | https://mediadive.dsmz.de/rest/solution/5343; $.data.id, name, complete recipe and steps | refutes | This asserted MediaDive stock resolves, but its composition belongs to a different formulation; generic A/B names do not establish correspondence. |
| dependency-context | data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml; data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml; Complete pinned contextual YAML files | context_only | [{"path": "data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml", "sha256": "fbc65564968b86b312f7795ff5c4527f199c51d04dc2764452d46bb5ba339566", "id": "CultureMech:014254", "term": {"id": "mediadive.solution:5342", "label": "Solution A"}, "scope": "Complete contextual record read for this target association; not a separate record review."}, {"path": "data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml", "sha256": "84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5", "id": "CultureMech:014255", "term": {"id": "mediadive.solution:5343", "label": "Solution B"}, "scope": "Complete contextual record read for this target association; not a separate record review."}] |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32599 resolves to magnesium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:3312 resolves to calcium dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32599": [{"label": "Magnesium sulfate", "match_type": "preferred_term", "identifier": "CHEBI:32599", "preferred_term": "Magnesium sulfate", "ontology_id": "CHEBI:32599", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3312": [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 15, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml", "events": 14, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Read the current TOGO primary/local-section, unit and comment methods; solution migrator name index and resolver; cleanup duplicate reducer; merge compatibility/evidence preservation and exporter quantity edges. Current TOGO code separates local stock sections and preserves comments, but bare g/ml to per-liter mapping still requires a justified basis. The migrator can resolve generic names without source identity. Current cleanup no longer sums conflicting duplicates, and current merge requires formulation compatibility. These current writers are follow-up owners/context, not an authenticated replay of the older import/cleanup. The exporter emits encoded stock/ingredient quantities and cannot recover missing preparation or correct their source scope. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Read the current TOGO primary/local-section, unit and comment methods; solution migrator name index and resolver; cleanup duplicate reducer; merge compatibility/evidence preservation and exporter quantity edges. Current TOGO code separates local stock sections and preserves comments, but bare g/ml to per-liter mapping still requires a justified basis. The migrator can resolve generic names without source identity. Current cleanup no longer sums conflicting duplicates, and current merge requires formulation compatibility. These current writers are follow-up owners/context, not an authenticated replay of the older import/cleanup. The exporter emits encoded stock/ingredient quantities and cannot recover missing preparation or correct their source scope. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Read the current TOGO primary/local-section, unit and comment methods; solution migrator name index and resolver; cleanup duplicate reducer; merge compatibility/evidence preservation and exporter quantity edges. Current TOGO code separates local stock sections and preserves comments, but bare g/ml to per-liter mapping still requires a justified basis. The migrator can resolve generic names without source identity. Current cleanup no longer sums conflicting duplicates, and current merge requires formulation compatibility. These current writers are follow-up owners/context, not an authenticated replay of the older import/cleanup. The exporter emits encoded stock/ingredient quantities and cannot recover missing preparation or correct their source scope. |
| writer-3 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Read the current TOGO primary/local-section, unit and comment methods; solution migrator name index and resolver; cleanup duplicate reducer; merge compatibility/evidence preservation and exporter quantity edges. Current TOGO code separates local stock sections and preserves comments, but bare g/ml to per-liter mapping still requires a justified basis. The migrator can resolve generic names without source identity. Current cleanup no longer sums conflicting duplicates, and current merge requires formulation compatibility. These current writers are follow-up owners/context, not an authenticated replay of the older import/cleanup. The exporter emits encoded stock/ingredient quantities and cannot recover missing preparation or correct their source scope. |
| writer-4 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Read the current TOGO primary/local-section, unit and comment methods; solution migrator name index and resolver; cleanup duplicate reducer; merge compatibility/evidence preservation and exporter quantity edges. Current TOGO code separates local stock sections and preserves comments, but bare g/ml to per-liter mapping still requires a justified basis. The migrator can resolve generic names without source identity. Current cleanup no longer sums conflicting duplicates, and current merge requires formulation compatibility. These current writers are follow-up owners/context, not an authenticated replay of the older import/cleanup. The exporter emits encoded stock/ingredient quantities and cannot recover missing preparation or correct their source scope. |
| writer-5 | src/culturemech/export/kgx_export.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Read the current TOGO primary/local-section, unit and comment methods; solution migrator name index and resolver; cleanup duplicate reducer; merge compatibility/evidence preservation and exporter quantity edges. Current TOGO code separates local stock sections and preserves comments, but bare g/ml to per-liter mapping still requires a justified basis. The migrator can resolve generic names without source identity. Current cleanup no longer sums conflicting duplicates, and current merge requires formulation compatibility. These current writers are follow-up owners/context, not an authenticated replay of the older import/cleanup. The exporter emits encoded stock/ingredient quantities and cannot recover missing preparation or correct their source scope. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch018/175/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No explicit final volume for the completed ATCC A/B mixture is supplied in the inspected text. TOGO 800/200 ml solution references are retained as source declarations, not treated as measured final-volume evidence.
- The contextual 5342/5343 records were inspected to reject these target associations; their independent formulation, grounding and history defects are not separately reviewed.
- No fixed acid/base stock strength or dose is supplied. The current OLS and MIM snapshots do not establish supplier grade, purity, hydration not printed in the source, or historical import methodology.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T112053Z-culturemech-008883-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidithiobacillus_ferrooxidans_medium (CultureMech:008883)'
started_at: '2026-10-21T11:17:50Z'
finished_at: '2026-10-21T11:20:53Z'
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
summary: ATCC 2039 / TOGO M2297 identity is resolved, but the represented formulation
  combines solution and stock batches, assigns unrelated A/B references and loses
  source preparation scope. Source-stage reconstruction is needed before this record
  is usable as the named medium.
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
  - path: data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml
    sha256: 3783b1cfaabbf1b8d8a577f29565a3bac814f2f37cad7ffccb0235afa4d72a48
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml
    sha256: bce908b57c7d8d88d8fd8e122f77efc993d9b3fbfe4f30b8eca282b13e75586e
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml
    sha256: fbc65564968b86b312f7795ff5c4527f199c51d04dc2764452d46bb5ba339566
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml
    sha256: 84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5
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
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 175; batch 018 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding seventeen task batches
    contain 170 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 172 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008883
targets:
- target_id: CultureMech:008883
  path: data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml
  label: acidithiobacillus_ferrooxidans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch018/175/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch018/175/strict.tsv"
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008883
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
  - CultureMech:008883
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:20:51Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:20:51Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:19:01.738645Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch018/175/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T11:19:03.452127Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch018/175/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:19:06.214400Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:19:07.610151Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:20:51Z'
  support: supports
  summary: './data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml:1:id:
    CultureMech:008883

    ./data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml:1:id:
    CultureMech:008883

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch018/source-preflight-bound/175/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:20:51Z'
  support: supports
  summary: 25 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: c9ba4c4189f90ab79ea46fbb92f333ac41a643a7659bc08aa982a5ba51e918b2
- evidence_id: atcc2039
  kind: primary_source
  reference: https://www.atcc.org/~/media/4C29EA2E2A0749BB9354D8AC64AA715B.ashx
  locator: 'Complete ATCC Medium 2039 PDF: Solution A, Solution B, Complete Medium
    and Wolfe mineral sections'
  accessed_at: '2026-10-21T11:02:38.067609Z'
  support: supports
  summary: The exact original collection URL resolves to ATCC 2039. Its A/B preparation
    and Wolfe stock are separate stages; all amounts and preparation passages were
    read.
  snapshot_sha256: dfbbe0099b70c8a5dc13ab2861c29f7a76477a6ab087bf1c65fa3fb3abe51ead
- evidence_id: togoM2297
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297
  locator: meta; all four components sections; all comments
  accessed_at: '2026-10-21T11:02:38.064248Z'
  support: supports
  summary: Exact TOGO M2297 points to the same ATCC document and preserves local section
    identity, original g/ml amounts and preparation comments.
  snapshot_sha256: 97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f
- evidence_id: solution5342
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5342
  locator: $.data.id, name, complete recipe and steps
  accessed_at: '2026-10-21T07:31:13.269119Z'
  support: refutes
  summary: This asserted MediaDive stock resolves, but its composition belongs to
    a different formulation; generic A/B names do not establish correspondence.
  quote: '"id": 5342'
  snapshot_sha256: 4bf262e02d0a83f9d1a24a52d2a14383aa8c6f27384e446d7da6274a05319240
- evidence_id: solution5343
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5343
  locator: $.data.id, name, complete recipe and steps
  accessed_at: '2026-10-21T07:31:13.547266Z'
  support: refutes
  summary: This asserted MediaDive stock resolves, but its composition belongs to
    a different formulation; generic A/B names do not establish correspondence.
  quote: '"id": 5343'
  snapshot_sha256: 28c315b1d9cf9a5c19f4d79c639298f5818c06ea87462c84336f66297d20f4c0
- evidence_id: dependency-context
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml; data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml
  locator: Complete pinned contextual YAML files
  accessed_at: '2026-10-21T11:20:51Z'
  support: context_only
  summary: '[{"path": "data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml",
    "sha256": "fbc65564968b86b312f7795ff5c4527f199c51d04dc2764452d46bb5ba339566",
    "id": "CultureMech:014254", "term": {"id": "mediadive.solution:5342", "label":
    "Solution A"}, "scope": "Complete contextual record read for this target association;
    not a separate record review."}, {"path": "data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml",
    "sha256": "84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5",
    "id": "CultureMech:014255", "term": {"id": "mediadive.solution:5343", "label":
    "Solution B"}, "scope": "Complete contextual record read for this target association;
    not a separate record review."}]'
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
- evidence_id: chebi26836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:29:13.222926Z'
  support: supports
  summary: CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
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
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi32599
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.640268Z'
  support: supports
  summary: CHEBI:32599 resolves to magnesium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
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
- evidence_id: chebi3312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:16:24.822837Z'
  support: supports
  summary: CHEBI:3312 resolves to calcium dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 34ed49d95375c80dcb07576c67d04fa77337bfecf406accb283e8c32253b754b
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
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
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
- evidence_id: chebi86364
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:35.036768Z'
  support: supports
  summary: CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi86465
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:08.054799Z'
  support: supports
  summary: CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T11:20:51Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label":
    "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term":
    "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312":
    [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32599": [{"label": "Magnesium sulfate",
    "match_type": "preferred_term", "identifier": "CHEBI:32599", "preferred_term":
    "Magnesium sulfate", "ontology_id": "CHEBI:32599", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3312": [{"label":
    "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term":
    "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id":
    "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503":
    [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier":
    "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id":
    "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946":
    [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946",
    "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364":
    [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364",
    "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDITHIOBACILLUS_FERROOXIDANS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:20:51Z'
  support: context_only
  summary: '[{"input": "target", "events": 15, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml",
    "events": 14, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:20:51Z'
  support: context_only
  summary: Read the current TOGO primary/local-section, unit and comment methods;
    solution migrator name index and resolver; cleanup duplicate reducer; merge compatibility/evidence
    preservation and exporter quantity edges. Current TOGO code separates local stock
    sections and preserves comments, but bare g/ml to per-liter mapping still requires
    a justified basis. The migrator can resolve generic names without source identity.
    Current cleanup no longer sums conflicting duplicates, and current merge requires
    formulation compatibility. These current writers are follow-up owners/context,
    not an authenticated replay of the older import/cleanup. The exporter emits encoded
    stock/ingredient quantities and cannot recover missing preparation or correct
    their source scope.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:20:51Z'
  support: context_only
  summary: Read the current TOGO primary/local-section, unit and comment methods;
    solution migrator name index and resolver; cleanup duplicate reducer; merge compatibility/evidence
    preservation and exporter quantity edges. Current TOGO code separates local stock
    sections and preserves comments, but bare g/ml to per-liter mapping still requires
    a justified basis. The migrator can resolve generic names without source identity.
    Current cleanup no longer sums conflicting duplicates, and current merge requires
    formulation compatibility. These current writers are follow-up owners/context,
    not an authenticated replay of the older import/cleanup. The exporter emits encoded
    stock/ingredient quantities and cannot recover missing preparation or correct
    their source scope.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:20:51Z'
  support: context_only
  summary: Read the current TOGO primary/local-section, unit and comment methods;
    solution migrator name index and resolver; cleanup duplicate reducer; merge compatibility/evidence
    preservation and exporter quantity edges. Current TOGO code separates local stock
    sections and preserves comments, but bare g/ml to per-liter mapping still requires
    a justified basis. The migrator can resolve generic names without source identity.
    Current cleanup no longer sums conflicting duplicates, and current merge requires
    formulation compatibility. These current writers are follow-up owners/context,
    not an authenticated replay of the older import/cleanup. The exporter emits encoded
    stock/ingredient quantities and cannot recover missing preparation or correct
    their source scope.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:20:51Z'
  support: context_only
  summary: Read the current TOGO primary/local-section, unit and comment methods;
    solution migrator name index and resolver; cleanup duplicate reducer; merge compatibility/evidence
    preservation and exporter quantity edges. Current TOGO code separates local stock
    sections and preserves comments, but bare g/ml to per-liter mapping still requires
    a justified basis. The migrator can resolve generic names without source identity.
    Current cleanup no longer sums conflicting duplicates, and current merge requires
    formulation compatibility. These current writers are follow-up owners/context,
    not an authenticated replay of the older import/cleanup. The exporter emits encoded
    stock/ingredient quantities and cannot recover missing preparation or correct
    their source scope.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-4
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:20:51Z'
  support: context_only
  summary: Read the current TOGO primary/local-section, unit and comment methods;
    solution migrator name index and resolver; cleanup duplicate reducer; merge compatibility/evidence
    preservation and exporter quantity edges. Current TOGO code separates local stock
    sections and preserves comments, but bare g/ml to per-liter mapping still requires
    a justified basis. The migrator can resolve generic names without source identity.
    Current cleanup no longer sums conflicting duplicates, and current merge requires
    formulation compatibility. These current writers are follow-up owners/context,
    not an authenticated replay of the older import/cleanup. The exporter emits encoded
    stock/ingredient quantities and cannot recover missing preparation or correct
    their source scope.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-5
  kind: record_content
  reference: src/culturemech/export/kgx_export.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:20:51Z'
  support: context_only
  summary: Read the current TOGO primary/local-section, unit and comment methods;
    solution migrator name index and resolver; cleanup duplicate reducer; merge compatibility/evidence
    preservation and exporter quantity edges. Current TOGO code separates local stock
    sections and preserves comments, but bare g/ml to per-liter mapping still requires
    a justified basis. The migrator can resolve generic names without source identity.
    Current cleanup no longer sums conflicting duplicates, and current merge requires
    formulation compatibility. These current writers are follow-up owners/context,
    not an authenticated replay of the older import/cleanup. The exporter emits encoded
    stock/ingredient quantities and cannot recover missing preparation or correct
    their source scope.
  snapshot_sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch018/175/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:20:51Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: cfbc557736863fea86a63c3e76ee6ccca97bf8b31109cb68d7fc4faf9b8bb2fa
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '16 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 15/16 primary and 15/16 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form
    mismatch is addressed separately; valid IDs and labels do not establish correct
    source grounding.'
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi26710
  - chebi26836
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi32599
  - chebi33118
  - chebi3312
  - chebi44557
  - chebi53503
  - chebi62946
  - chebi75213
  - chebi75836
  - chebi86364
  - chebi86465
  details: 'Instance coverage on a 0–100 percent scale, denominator 16: primary 93.75%;
    secondary 93.75%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 29 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact source and stock identity
  outcome: concern
  summary: TOGO M2297 and the original ATCC 2039 title agree. Both reviewed layers
    contain the same 16 direct rows and four solution descriptors. ATCC Solution A
    is ammonium sulfate, magnesium sulfate, phosphate, water and a Wolfe aliquot;
    Solution B is ferrous sulfate and water. MediaDive 5342 instead contains yeast
    extract, casamino acids and 100 g NaCl among eight rows; 5343 contains 80 g carbonate
    and 100 g NaCl. Their local stock IDs resolve to CultureMech:014254/014255, but
    they are scientifically wrong associations. No replacement stock ID is invented.
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - record
  - owner-0
  - atcc2039
  - togoM2297
  - solution5342
  - solution5343
  - dependency-context
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 28 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"field_path\": \"solutions[0].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"layer_decisions\": {\n      \"target\": \"correct\",\n \
    \     \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"TOGO complete-medium A/B aliquot\
    \ declarations\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM2297\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution A\\\",\\n          \\\"volume\\\": 800,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"TOGO declares 800 ml of this local A/B\
    \ solution, not g/L. ATCC prints the associated water batch and instructs combining\
    \ the prepared solutions; retain that source distinction and do not substitute\
    \ the unrelated MediaDive stock.\",\n    \"source_name\": \"Solution A\",\n  \
    \  \"primary_source_evidence_id\": \"atcc2039\",\n    \"source_original_amount\"\
    : 800,\n    \"source_original_unit\": \"ml\"\n  },\n  {\n    \"field_path\": \"\
    solutions[1].concentration\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"TOGO complete-medium A/B aliquot\
    \ declarations\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM2297\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution B\\\",\\n          \\\"volume\\\": 200,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"TOGO declares 200 ml of this local A/B\
    \ solution, not g/L. ATCC prints the associated water batch and instructs combining\
    \ the prepared solutions; retain that source distinction and do not substitute\
    \ the unrelated MediaDive stock.\",\n    \"source_name\": \"Solution B\",\n  \
    \  \"primary_source_evidence_id\": \"atcc2039\",\n    \"source_original_amount\"\
    : 200,\n    \"source_original_unit\": \"ml\"\n  },\n  {\n    \"field_path\": \"\
    ingredients[0].concentration\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Solution A\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM2297\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\",\n\
    \        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 2,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"Restore this exact source batch amount\
    \ and stage; the current per-liter/direct-medium placement is not established\
    \ by this source row. No final working concentration is inferred.\",\n    \"source_name\"\
    : \"MgSO4 x 7 H2O\",\n    \"primary_source_evidence_id\": \"atcc2039\",\n    \"\
    source_original_amount\": 2,\n    \"source_original_unit\": \"g\",\n    \"arithmetic\"\
    : \"The recorded 5.0 is the unscaled sum 2.0 + 3.0 from Solution A and the Wolfe\
    \ stock. These are different stages; adding them does not calculate the final\
    \ medium concentration.\"\n  },\n  {\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\"\
    : \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Solution A\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM2297\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\",\n\
    \        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 0.4,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"Restore this exact source batch amount\
    \ and stage; the current per-liter/direct-medium placement is not established\
    \ by this source row. No final working concentration is inferred.\",\n    \"source_name\"\
    : \"K2HPO4\",\n    \"primary_source_evidence_id\": \"atcc2039\",\n    \"source_original_amount\"\
    : 0.4,\n    \"source_original_unit\": \"g\"\n  },\n  {\n    \"field_path\": \"\
    ingredients[2].concentration\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Solution A\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM2297\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\",\n\
    \        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"(NH4)2SO4\\\",\\n          \\\"volume\\\": 0.8,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"Restore this exact source batch amount\
    \ and stage; the current per-liter/direct-medium placement is not established\
    \ by this source row. No final working concentration is inferred.\",\n    \"source_name\"\
    : \"(NH4)2SO4\",\n    \"primary_source_evidence_id\": \"atcc2039\",\n    \"source_original_amount\"\
    : 0.8,\n    \"source_original_unit\": \"g\"\n  },\n  {\n    \"field_path\": \"\
    ingredients[3].concentration\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Solution A\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM2297\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\",\n\
    \        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"DI Water\\\",\\n          \\\"volume\\\": 800,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"This is a literal liquid volume in the\
    \ named stage, not a mass concentration. Keep source water and stock aliquots\
    \ separate; water volumes alone do not establish final volume.\",\n    \"source_name\"\
    : \"DI Water\",\n    \"primary_source_evidence_id\": \"atcc2039\",\n    \"source_original_amount\"\
    : 800,\n    \"source_original_unit\": \"ml\",\n    \"arithmetic\": \"The recorded\
    \ 2000 is 800 + 200 + 1000 ml across A, B and a separately prepared stock. Neither\
    \ that sum nor a density assumption supports 2000 g/L.\"\n  },\n  {\n    \"field_path\"\
    : \"solutions[2].concentration\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Solution A\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM2297\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\",\n\
    \        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"*Wolfe's Mineral Solution (see below)\\\",\\n\
    \          \\\"volume\\\": 5,\\n          \\\"unit\\\": \\\"ml\\\"\",\n      \
    \  \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"This is a literal liquid volume in the\
    \ named stage, not a mass concentration. Keep source water and stock aliquots\
    \ separate; water volumes alone do not establish final volume.\",\n    \"source_name\"\
    : \"*Wolfe's Mineral Solution (see below)\",\n    \"primary_source_evidence_id\"\
    : \"atcc2039\",\n    \"source_original_amount\": 5,\n    \"source_original_unit\"\
    : \"ml\"\n  },\n  {\n    \"field_path\": \"ingredients[4].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\":\
    \ \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Solution A\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM2297\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\",\n\
    \        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H2SO4\\\"\",\n        \"snapshot_sha256\": \"\
    97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\n      }\n\
    \    ],\n    \"explanation\": \"The source specifies an adjustment reagent with\
    \ a pH endpoint but no fixed dose or stock strength. Retain the nonnumeric amount\
    \ with the correct solution/stock scope and endpoint; do not manufacture a concentration.\"\
    ,\n    \"source_name\": \"H2SO4\",\n    \"primary_source_evidence_id\": \"atcc2039\"\
    ,\n    \"source_original_amount\": null,\n    \"source_original_unit\": null\n\
    \  },\n  {\n    \"field_path\": \"ingredients[5].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"layer_decisions\": {\n      \"target\": \"correct\",\n \
    \     \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Solution B\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM2297\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\",\n\
    \        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 20,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\n      }\n\
    \    ],\n    \"explanation\": \"Restore this exact source batch amount and stage;\
    \ the current per-liter/direct-medium placement is not established by this source\
    \ row. No final working concentration is inferred.\",\n    \"source_name\": \"\
    FeSO4 x 7 H2O\",\n    \"primary_source_evidence_id\": \"atcc2039\",\n    \"source_original_amount\"\
    : 20,\n    \"source_original_unit\": \"g\",\n    \"arithmetic\": \"The recorded\
    \ 20.1 is the unscaled sum 20.0 + 0.1 from Solution B and the Wolfe stock. This\
    \ is not a valid stock dilution.\"\n  },\n  {\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\"\
    : \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Solution B\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM2297\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\",\n\
    \        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"DI Water\\\",\\n          \\\"volume\\\": 200,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"This is a literal liquid volume in the\
    \ named stage, not a mass concentration. Keep source water and stock aliquots\
    \ separate; water volumes alone do not establish final volume.\",\n    \"source_name\"\
    : \"DI Water\",\n    \"primary_source_evidence_id\": \"atcc2039\",\n    \"source_original_amount\"\
    : 200,\n    \"source_original_unit\": \"ml\",\n    \"arithmetic\": \"The recorded\
    \ 2000 is 800 + 200 + 1000 ml across A, B and a separately prepared stock. Neither\
    \ that sum nor a density assumption supports 2000 g/L.\"\n  },\n  {\n    \"field_path\"\
    : \"ingredients[0].concentration\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 3,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"This amount belongs to the separately\
    \ prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore\
    \ stock composition and dose hierarchy rather than retaining an undiluted final-medium\
    \ row.\",\n    \"source_name\": \"MgSO4 x 7 H2O\",\n    \"primary_source_evidence_id\"\
    : \"atcc2039\",\n    \"source_original_amount\": 3,\n    \"source_original_unit\"\
    : \"g\",\n    \"arithmetic\": \"The recorded 5.0 is the unscaled sum 2.0 + 3.0\
    \ from Solution A and the Wolfe stock. These are different stages; adding them\
    \ does not calculate the final medium concentration.\"\n  },\n  {\n    \"field_path\"\
    : \"ingredients[6].concentration\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 1,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"This amount belongs to the separately\
    \ prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore\
    \ stock composition and dose hierarchy rather than retaining an undiluted final-medium\
    \ row.\",\n    \"source_name\": \"NaCl\",\n    \"primary_source_evidence_id\"\
    : \"atcc2039\",\n    \"source_original_amount\": 1,\n    \"source_original_unit\"\
    : \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[7].concentration\",\n  \
    \  \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\": \"\
    correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n          \\\"volume\\\"\
    : 0.01,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\n      }\n\
    \    ],\n    \"explanation\": \"This amount belongs to the separately prepared\
    \ Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition\
    \ and dose hierarchy rather than retaining an undiluted final-medium row.\",\n\
    \    \"source_name\": \"Na2MoO4 x 2 H2O\",\n    \"primary_source_evidence_id\"\
    : \"atcc2039\",\n    \"source_original_amount\": 0.01,\n    \"source_original_unit\"\
    : \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[8].concentration\",\n  \
    \  \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\": \"\
    correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"This amount belongs to the separately\
    \ prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore\
    \ stock composition and dose hierarchy rather than retaining an undiluted final-medium\
    \ row.\",\n    \"source_name\": \"H3BO3\",\n    \"primary_source_evidence_id\"\
    : \"atcc2039\",\n    \"source_original_amount\": 0.01,\n    \"source_original_unit\"\
    : \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[5].concentration\",\n  \
    \  \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\": \"\
    correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 0.1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\n      }\n\
    \    ],\n    \"explanation\": \"This amount belongs to the separately prepared\
    \ Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition\
    \ and dose hierarchy rather than retaining an undiluted final-medium row.\",\n\
    \    \"source_name\": \"FeSO4 x 7 H2O\",\n    \"primary_source_evidence_id\":\
    \ \"atcc2039\",\n    \"source_original_amount\": 0.1,\n    \"source_original_unit\"\
    : \"g\",\n    \"arithmetic\": \"The recorded 20.1 is the unscaled sum 20.0 + 0.1\
    \ from Solution B and the Wolfe stock. This is not a valid stock dilution.\"\n\
    \  },\n  {\n    \"field_path\": \"ingredients[9].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"layer_decisions\": {\n      \"target\": \"correct\",\n \
    \     \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2 x 6 H2O\\\",\\n          \\\"volume\\\"\
    : 0.1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\n      }\n\
    \    ],\n    \"explanation\": \"This amount belongs to the separately prepared\
    \ Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition\
    \ and dose hierarchy rather than retaining an undiluted final-medium row.\",\n\
    \    \"source_name\": \"CoCl2 x 6 H2O\",\n    \"primary_source_evidence_id\":\
    \ \"atcc2039\",\n    \"source_original_amount\": 0.1,\n    \"source_original_unit\"\
    : \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[10].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\":\
    \ \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 0.1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\n      }\n\
    \    ],\n    \"explanation\": \"This amount belongs to the separately prepared\
    \ Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition\
    \ and dose hierarchy rather than retaining an undiluted final-medium row.\",\n\
    \    \"source_name\": \"ZnSO4 x 7 H2O\",\n    \"primary_source_evidence_id\":\
    \ \"atcc2039\",\n    \"source_original_amount\": 0.1,\n    \"source_original_unit\"\
    : \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[11].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\":\
    \ \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuSO4 x 5 H2O\\\",\\n          \\\"volume\\\"\
    : 0.01,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\n      }\n\
    \    ],\n    \"explanation\": \"This amount belongs to the separately prepared\
    \ Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition\
    \ and dose hierarchy rather than retaining an undiluted final-medium row.\",\n\
    \    \"source_name\": \"CuSO4 x 5 H2O\",\n    \"primary_source_evidence_id\":\
    \ \"atcc2039\",\n    \"source_original_amount\": 0.01,\n    \"source_original_unit\"\
    : \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[12].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\":\
    \ \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"AlK(SO4)2 x 12H2O\\\",\\n          \\\"volume\\\
    \": 0.01,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\n     \
    \ }\n    ],\n    \"explanation\": \"This amount belongs to the separately prepared\
    \ Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition\
    \ and dose hierarchy rather than retaining an undiluted final-medium row.\",\n\
    \    \"source_name\": \"AlK(SO4)2 x 12H2O\",\n    \"primary_source_evidence_id\"\
    : \"atcc2039\",\n    \"source_original_amount\": 0.01,\n    \"source_original_unit\"\
    : \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[13].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\":\
    \ \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrilotriacetic acid\\\",\\n          \\\"volume\\\
    \": 1.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\n     \
    \ }\n    ],\n    \"explanation\": \"This amount belongs to the separately prepared\
    \ Wolfe stock; only 5 ml of that stock is added to Solution A. Restore stock composition\
    \ and dose hierarchy rather than retaining an undiluted final-medium row.\",\n\
    \    \"source_name\": \"Nitrilotriacetic acid\",\n    \"primary_source_evidence_id\"\
    : \"atcc2039\",\n    \"source_original_amount\": 1.5,\n    \"source_original_unit\"\
    : \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[14].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\":\
    \ \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"This amount belongs to the separately\
    \ prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore\
    \ stock composition and dose hierarchy rather than retaining an undiluted final-medium\
    \ row.\",\n    \"source_name\": \"CaCl2\",\n    \"primary_source_evidence_id\"\
    : \"atcc2039\",\n    \"source_original_amount\": 0.1,\n    \"source_original_unit\"\
    : \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[15].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\":\
    \ \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnSO4 x H2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"This amount belongs to the separately\
    \ prepared Wolfe stock; only 5 ml of that stock is added to Solution A. Restore\
    \ stock composition and dose hierarchy rather than retaining an undiluted final-medium\
    \ row.\",\n    \"source_name\": \"MnSO4 x H2O\",\n    \"primary_source_evidence_id\"\
    : \"atcc2039\",\n    \"source_original_amount\": 0.5,\n    \"source_original_unit\"\
    : \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[3].concentration\",\n  \
    \  \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\": \"\
    correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"DI Water\\\",\\n          \\\"volume\\\": 1000,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"This is a literal liquid volume in the\
    \ named stage, not a mass concentration. Keep source water and stock aliquots\
    \ separate; water volumes alone do not establish final volume.\",\n    \"source_name\"\
    : \"DI Water\",\n    \"primary_source_evidence_id\": \"atcc2039\",\n    \"source_original_amount\"\
    : 1000,\n    \"source_original_unit\": \"ml\",\n    \"arithmetic\": \"The recorded\
    \ 2000 is 800 + 200 + 1000 ml across A, B and a separately prepared stock. Neither\
    \ that sum nor a density assumption supports 2000 g/L.\"\n  },\n  {\n    \"field_path\"\
    : \"solutions[3].concentration\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"Wolfe's Mineral Solution\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2297\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2297\"\
    ,\n        \"source_locator\": \"$.components[3].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Potassium hydroxide solution\\\"\",\n        \"\
    snapshot_sha256\": \"97abefb92c4eb859c7cc5c5140731aa72360b38ebc31166365c761aded8ad37f\"\
    \n      }\n    ],\n    \"explanation\": \"The source specifies an adjustment reagent\
    \ with a pH endpoint but no fixed dose or stock strength. Retain the nonnumeric\
    \ amount with the correct solution/stock scope and endpoint; do not manufacture\
    \ a concentration.\",\n    \"source_name\": \"Potassium hydroxide solution\",\n\
    \    \"primary_source_evidence_id\": \"atcc2039\",\n    \"source_original_amount\"\
    : null,\n    \"source_original_unit\": null\n  },\n  {\n    \"field_path\": \"\
    solutions[0].preparation.pH\",\n    \"decision\": \"add\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"Solution A\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"atccOriginal\",\n        \"source_url\"\
    : \"https://www.atcc.org/~/media/4C29EA2E2A0749BB9354D8AC64AA715B.ashx\",\n  \
    \      \"source_locator\": \"ATCC 2039 PDF, corresponding A or Wolfe preparation\
    \ paragraph\",\n        \"exact_source_quote\": \"Adjust Solution A to pH 2.3\
    \ with H2SO4 and filter-sterilize.\",\n        \"snapshot_sha256\": \"dfbbe0099b70c8a5dc13ab2861c29f7a76477a6ab087bf1c65fa3fb3abe51ead\"\
    ,\n        \"parsed_text_sha256\": \"b05f12680a7368101f2cb413a108866e6a8918f788c50585f312c11d1bc5e73b\"\
    \n      }\n    ],\n    \"explanation\": \"Add the source-specific pH 2.3 endpoint\
    \ and acid/filter preparation; it is not a reported final complete-medium pH.\"\
    ,\n    \"primary_source_evidence_id\": \"atcc2039\"\n  },\n  {\n    \"field_path\"\
    : \"solutions[2].preparation.initial_water\",\n    \"decision\": \"add\",\n  \
    \  \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"Wolfe stock initial dissolution\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"atccOriginal\"\
    ,\n        \"source_url\": \"https://www.atcc.org/~/media/4C29EA2E2A0749BB9354D8AC64AA715B.ashx\"\
    ,\n        \"source_locator\": \"ATCC 2039 PDF, corresponding A or Wolfe preparation\
    \ paragraph\",\n        \"exact_source_quote\": \"approximately 500 ml of water\"\
    ,\n        \"snapshot_sha256\": \"dfbbe0099b70c8a5dc13ab2861c29f7a76477a6ab087bf1c65fa3fb3abe51ead\"\
    ,\n        \"parsed_text_sha256\": \"b05f12680a7368101f2cb413a108866e6a8918f788c50585f312c11d1bc5e73b\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve approximate 500 ml for initial\
    \ NTA dissolution, not a second water addition on top of the stock batch.\",\n\
    \    \"primary_source_evidence_id\": \"atcc2039\"\n  },\n  {\n    \"field_path\"\
    : \"solutions[2].preparation.pH\",\n    \"decision\": \"add\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"Wolfe stock NTA dissolution\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"atccOriginal\",\n\
    \        \"source_url\": \"https://www.atcc.org/~/media/4C29EA2E2A0749BB9354D8AC64AA715B.ashx\"\
    ,\n        \"source_locator\": \"ATCC 2039 PDF, corresponding A or Wolfe preparation\
    \ paragraph\",\n        \"exact_source_quote\": \"adjust to pH 6.5\",\n      \
    \  \"snapshot_sha256\": \"dfbbe0099b70c8a5dc13ab2861c29f7a76477a6ab087bf1c65fa3fb3abe51ead\"\
    ,\n        \"parsed_text_sha256\": \"b05f12680a7368101f2cb413a108866e6a8918f788c50585f312c11d1bc5e73b\"\
    \n      }\n    ],\n    \"explanation\": \"Add stock-specific pH 6.5 with KOH;\
    \ no fixed KOH amount or strength is supplied.\",\n    \"primary_source_evidence_id\"\
    : \"atcc2039\"\n  },\n  {\n    \"field_path\": \"solutions[2].preparation.water_makeup\"\
    ,\n    \"decision\": \"add\",\n    \"layer_decisions\": {\n      \"target\": \"\
    add\",\n      \"data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"Wolfe stock after NTA dissolution,\
    \ before other compounds\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"atccOriginal\",\n        \"source_url\": \"https://www.atcc.org/~/media/4C29EA2E2A0749BB9354D8AC64AA715B.ashx\"\
    ,\n        \"source_locator\": \"ATCC 2039 PDF, corresponding A or Wolfe preparation\
    \ paragraph\",\n        \"exact_source_quote\": \"Bring volume to 1000 ml with\
    \ remaining\",\n        \"snapshot_sha256\": \"dfbbe0099b70c8a5dc13ab2861c29f7a76477a6ab087bf1c65fa3fb3abe51ead\"\
    ,\n        \"parsed_text_sha256\": \"b05f12680a7368101f2cb413a108866e6a8918f788c50585f312c11d1bc5e73b\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve the source order: bring volume\
    \ to 1000 ml, then add remaining compounds one at a time. Do not silently rewrite\
    \ this as measured final volume after all solutes.\",\n    \"primary_source_evidence_id\"\
    : \"atcc2039\"\n  }\n]"
- assessment_id: preparation
  area: completeness
  topic: A/B filtration, stock dissolution and pH scope
  outcome: concern
  summary: Neither local layer retains the source instructions. ATCC requires A pH
    2.3 with sulfuric acid and filtration, rapid dissolution/filtration of B, aseptic
    combination and dispensing, and a separate NTA/KOH pH 6.5 dissolution/makeup sequence
    for Wolfe stock. The yellow precipitate/iron-oxidation note is source context.
    No generic autoclave cycle is substituted. ATCC permits MD-TMS as an alternative,
    but no product composition or formulation equivalence beyond that explicit option
    is asserted.
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - record
  - owner-0
  - atcc2039
  - togoM2297
  - quantity-inventory
- assessment_id: forms
  area: grounding
  topic: All named salts, hydrates and adjustment reagents
  outcome: concern
  summary: The primary terms preserve the explicitly supplied sulfate/chloride hydrates,
    including CoCl2 hexahydrate and potassium aluminium sulfate dodecahydrate. Calcium
    chloride has no hydrate specified; no hydrate or molar conversion is invented.
    MgSO4 heptahydrate is correctly primary-grounded to CHEBI:31795, but its secondary
    key remains generic CHEBI:32599 despite the later primary correction. Sulfuric
    acid identity does not establish an unspecified solution strength.
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - record
  - owner-0
  - atcc2039
  - chebi31795
  - chebi32599
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Medium classification and physical state
  outcome: concern
  summary: Bacterial placement and liquid state agree with the named source. COMPLEX/UNDEFINED
    is not supported for this explicit formulation of named chemicals and a specified
    mineral stock. An optional commercial substitute is not evidence that the current
    stated recipe uses an undefined mixture. Classification must follow the reconstructed
    source branch, with reagent-strength uncertainty kept separate from compositional
    classification.
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - record
  - owner-0
  - atcc2039
- assessment_id: provenance
  area: provenance
  topic: Owner correspondence and current writer context
  outcome: supported
  summary: The maintained owner and generated copy have matching formulation fields;
    the generated merge history adds provenance, not scientific evidence. The old
    cleanup notes explicitly retain cross-stage sums, while current cleanup avoids
    this summing behavior. Correct the normalized owner and source-specific references
    before separately authorized regeneration. No runtime or historical replay is
    claimed.
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  - writer-0
  - writer-1
  - writer-2
  - writer-3
  - writer-4
  - writer-5
- assessment_id: biology
  area: scope
  topic: Biological identifiers, cultivation claims and literature scope
  outcome: supported
  summary: The medium title, generic cultivation application and source-specific strain
    instructions do not establish an experimental growth result or a taxon/strain
    equivalence. No target-organism CURIE, genome assembly, DOI or PMID is asserted
    in the reviewed target or maintained owners. No organism identifier, incubation
    optimum or unreported growth claim is added.
  target_ids:
  - CultureMech:008883
  evidence_ids:
  - record
  - owner-0
findings:
- finding_id: f1
  issue_key: cm008883-formulation-stage-and-stock-identity
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The represented formulation does not preserve ATCC 2039 solution identity
  description: A/B/Wolfe stages are flattened into 16 direct rows, including unscaled
    Mg and Fe sums and 2000 g/L water; 800/200/5 ml additions are encoded as g/L.
    Two resolvable stock IDs denote unrelated high-salt formulations. These combined
    defects make the encoded recipe materially different from the named ATCC medium.
  target_ids:
  - CultureMech:008883
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - atcc2039
  - togoM2297
  - solution5342
  - solution5343
  - dependency-context
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml
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
  issue_key: cm008883-source-preparation-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source-specific filtration and stock preparation are missing
  description: The omitted filtration, aseptic mixing and distinct pH 2.3/6.5 operations
    determine how the staged recipe is prepared; their absence materially limits reproducibility.
  target_ids:
  - CultureMech:008883
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - owner-0
  - atcc2039
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3.5 is normalized to major because the exact source requires
    separate filtration and staged pH/dissolution operations; a generic or omitted
    preparation would not reproduce this iron-containing medium. P3.4 and P3.6 are
    related missing-detail observations covered by this finding.
- finding_id: f3
  issue_key: cm008883-secondary-magnesium-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Secondary magnesium linkage loses the source heptahydrate form
  description: Both layers retain generic magnesium sulfate CHEBI:32599 as secondary
    identity although the source and corrected primary term specify magnesium sulfate
    heptahydrate CHEBI:31795. Exact existence in the pinned MIM index does not validate
    this broader correspondence.
  target_ids:
  - CultureMech:008883
  field_paths:
  - ingredients[0].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - atcc2039
  - chebi31795
  - chebi32599
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml
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
  issue_key: cm008883-classification-source-support
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Complex and undefined classification lacks source support
  description: The exact stated source recipe specifies named chemical components
    and a defined mineral-stock recipe; no undefined nutrient mixture is identified
    for the selected branch.
  target_ids:
  - CultureMech:008883
  field_paths:
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - owner-0
  - atcc2039
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml
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
  description: Reconstruct the exact A/B/Wolfe hierarchy in the normalized owner,
    remove or replace the unsupported 5342/5343 associations only after source-specific
    identity resolution, preserve literal batch units and attach scoped evidence.
    Do not compute a final concentration from unspecified final volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008883
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml
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
  description: Restore exact source preparation in the correct A/B/Wolfe scopes, preserving
    nonnumeric acid/base doses, order and optional substitution boundary; do not invent
    autoclave conditions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008883
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml
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
  description: Reconcile the secondary key with the explicit heptahydrate using the
    pinned resolver/index and source evidence; preserve the actual supplied hydrate
    and the independently corrected stock quantities.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008883
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml
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
  description: Reassess composition and medium type from the restored source formulation;
    preserve the commercial-substitute option as a separate qualified branch rather
    than using it to justify the base classification.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008883
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2297_Acidithiobacillus_ferrooxidans_Medium.yaml
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
- No explicit final volume for the completed ATCC A/B mixture is supplied in the inspected
  text. TOGO 800/200 ml solution references are retained as source declarations, not
  treated as measured final-volume evidence.
- The contextual 5342/5343 records were inspected to reject these target associations;
  their independent formulation, grounding and history defects are not separately
  reviewed.
- No fixed acid/base stock strength or dose is supplied. The current OLS and MIM snapshots
  do not establish supplier grade, purity, hydration not printed in the source, or
  historical import methodology.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-018
- generated-medium
```
