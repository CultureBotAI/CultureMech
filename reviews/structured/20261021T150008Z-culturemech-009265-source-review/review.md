# Source and formulation review: ammonifex_degensii_medium (CultureMech:009265)

- Review: 20261021T150008Z-culturemech-009265-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T14:47:42Z
- Finished UTC: 2026-10-21T15:00:08Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The TOGO M2714 record flattens a mineral stock into the medium, misstates liquid and milligram amounts, and points to a different trace-stock recipe. The linked DSMZ 716 source disagrees with TOGO on reductant and pressure; preserve both source representations while reconciling preparation, chemical forms and the stale generated layer.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 252; batch 026 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-five task batches contain 250 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 253 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009265 | data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml | generated | ammonifex_degensii_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009265 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009265 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch026/252/strict.tsv |
| validate-terms | passed | True | CultureMech:009265 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009265 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009265 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact current pinned legacy identifier lookup | passed | True | CultureMech:009265 | The complete pinned catalog/tree exact lookup completed; no legacy000170 correspondence was recovered. |
| Required historical correspondence for asserted legacy000170 | unavailable | True | CultureMech:009265 | The record asserts a historical identifier whose exact correspondence is not established by the available captured resources. A completed current negative lookup does not resolve that historical claim. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009265.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:009265.

25 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 24/24 primary and 21/24 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 24: primary 100.00%; secondary 87.50%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009265.

30 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Immediate source, linked primary and maintained input

identity: concern. Targets: CultureMech:009265.

The target is the generated copy of TOGO M2714, which explicitly points to DSMZ 716. Both captured sources are available, but TOGO specifies sulfide and 2 bar after inoculation while DSMZ/MediaDive specify DL-dithiothreitol and 0.5 bar after growth starts. These are separate current source representations; no evidence dates the change or supports calling one version newer. The target also predates its owner’s identical-duplicate collapse of water and NaCl; that repair did not restore stock scope.

### Asserted trace-stock reference

identity: concern. Targets: CultureMech:009265.

The solution6187 link resolves to an EDTA/chloride formulation, not the locally defined M2714 NTA/sulfate formulation corroborated by modified Wolin stock241. Its six existing concentration attachments correctly support their own provider-declared solution values, but cannot validate the receiver’s link. The dependency’s 1000 PERCENT_V_V water, placeholder ingredient and zinc-hydrate/generic-ID mismatch must not be inherited as a repair.

### Main amounts, stock quantities and generated divergence

consistency: concern. Targets: CultureMech:009265.

The target sums water to 2000 g/L and NaCl to 2 g/L; its owner collapses these to 1000 and 1 but still mixes main and trace-stock stages. Both retain MgSO4·7H2O 3.09 and CaCl2·2H2O 0.16 g/L as sums of main and undiluted stock amounts. Source 0.3 mg selenite and 0.4 mg tungstate become 0.3 and 0.4 g/L locally, a 1000-fold mass-unit error even before stock dilution. Four liquid stock doses are mislabeled G_PER_L. Other source grams are batch amounts; 1000 mL water and provider volume 1003 do not independently establish a final denominator.

### Missing anaerobic sequence and source-specific pressures

completeness: concern. Targets: CultureMech:009265.

Neither medium layer contains the source preparation or pH 7.2. Common supported details include 80% H2/20% CO2 for 30–45 minutes, the example 10 mL in 25 mL vessels, nitrate under 100% N2, carbonate under 80% N2/20% CO2, and stock pH 6.5 then 7.0 with unquantified KOH. Retain the TOGO sulfide/2-bar sequence separately from DSMZ’s filter-sterilized DTT/0.5-bar sequence. No autoclave cycle, fixed gas amount, KOH dose or later-stock strength is inferred.

### Hydrates, secondary specificity and legacy identifier

grounding: concern. Targets: CultureMech:009265.

Nickel hexahydrate uses anhydrous CHEBI:34887. MgSO4 heptahydrate has correct primary CHEBI:31795 but generic/anhydrous secondary CHEBI:32599. Source K2HPO4 trihydrate uses CHEBI:131527, whose formula HO4P.2K and mass 174.174 omit hydrate waters even though a trihydrate synonym is present; preserve that internal term ambiguity rather than claiming the synonym proves the form or inventing a replacement. Selenite CHEBI:131361 explicitly has the pentahydrate formula and is not a form error. Legacy nitrate 000170 remains historically unresolved after a completed bounded lookup, separately from its supported primary CHEBI:63043.

### Defined chemical formulation versus complex category

scope: concern. Targets: CultureMech:009265.

The source lists named chemical components and identified stock compositions; MediaDive explicitly marks the medium noncomplex. COMPLEX/UNDEFINED is unsupported by these inspected formulations and should be reassessed with the selected source version. LIQUID is supported by the absence of a solidifying ingredient. No organism growth or exact strain identification is inferred solely from the medium name or generic application.

### Current source separation and repair limits

provenance: concern. Targets: CultureMech:009265.

Current TOGO parsing separates main sections and local stock compositions, preserves ml/mg units, and extracts preparation comments. The cleanup code no longer sums differing duplicates, while source-stage reconciliation is still necessary here. These are current implementation observations, not proof of the historical execution path. Correct the maintained source representation, preserve the existing repair history and regenerate the stale target after review.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009265.

52 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "Main: Na-resazurin solution (0.1% w/v)",
    "field_path": "solutions[0].concentration",
    "decision": "correct",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Na-resazurin solution (0.1% w/v)\",\n          \"volume\": 0.5,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"(w/v)\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The stated 0.1% w/v strength is 0.1 g/100 mL = 1 mg/mL. Thus the stated source dose delivers 0.5 mg sodium resazurin per batch, not the local numeric dose in g/L."
  },
  {
    "ingredient_or_context": "Main: NiCl2 x 6 H2O solution (0.1% w/v)",
    "field_path": "solutions[1].concentration",
    "decision": "correct",
    "local": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"NiCl2 x 6 H2O solution (0.1% w/v)\",\n          \"volume\": 0.2,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"(w/v)\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.2,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000199402,\n                        \"mmol_l\": 0.00153861,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The stated 0.1% w/v strength is 0.1 g/100 mL = 1 mg/mL. Thus the stated source dose delivers 0.2 mg nickel chloride hexahydrate per batch, not the local numeric dose in g/L."
  },
  {
    "ingredient_or_context": "Main: Distilled water",
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "local": {
      "value": "2000.0",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2000.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Main: MgSO4 x 7 H2O",
    "field_path": "ingredients[1].concentration",
    "decision": "correct",
    "local": {
      "value": "3.09",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"MgSO4 x 7 H2O\",\n          \"volume\": 0.09,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.09,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0897308,\n                        \"mmol_l\": 0.364055,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.09",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.09",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Main: NaCl",
    "field_path": "ingredients[2].concentration",
    "decision": "correct",
    "local": {
      "value": "2.0",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 17.0604,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Main: CaCl2 x 2 H2O",
    "field_path": "ingredients[3].concentration",
    "decision": "correct",
    "local": {
      "value": "0.16",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"CaCl2 x 2 H2O\",\n          \"volume\": 0.06,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.06,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0598205,\n                        \"mmol_l\": 0.406901,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.16",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.16",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Main: KH2PO4",
    "field_path": "ingredients[4].concentration",
    "decision": "correct",
    "local": {
      "value": "0.22",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.22,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.22,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.219342,\n                        \"mmol_l\": 1.6118,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.22",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.22",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Main: Na2S x 9 H2O",
    "field_path": "ingredients[5].concentration",
    "decision": "conflict",
    "local": {
      "value": "0.3",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"Na2S x 9 H2O\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"DL-Dithiothreitol\",\n                        \"compound_id\": 151,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\": 1.93845,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "TOGO specifies 0.3 g sodium sulfide nonahydrate, whereas DSMZ/MediaDive specifies 0.3 g DL-dithiothreitol. Preserve the source disagreement; matching numbers do not establish chemical equivalence.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      }
    ]
  },
  {
    "ingredient_or_context": "Main: (NH4)2SO4",
    "field_path": "ingredients[6].concentration",
    "decision": "correct",
    "local": {
      "value": "0.22",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"(NH4)2SO4\",\n          \"volume\": 0.22,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.22,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.219342,\n                        \"mmol_l\": 1.65992,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.22",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.22",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Main: Na2CO3",
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "local": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Na2CO3\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\": 14.1102,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Main: KNO3",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"KNO3\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 9.86132,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Main: K2HPO4 x 3 H2O",
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "local": {
      "value": "0.3",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[11]",
        "exact_source_quote": "\"component_name\": \"K2HPO4 x 3 H2O\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4 x 3 H2O\",\n                        \"compound_id\": 244,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\": 1.71724,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Main: FeSO4 x 7 H2O solution (0.1% w/v in 0.1 N H2SO4)",
    "field_path": "solutions[2].concentration",
    "decision": "correct",
    "local": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[12]",
        "exact_source_quote": "\"component_name\": \"FeSO4 x 7 H2O solution (0.1% w/v in 0.1 N H2SO4)\",\n          \"volume\": 2,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"attribute\": \"0.1% w/v in 0.1 N H2SO4\",\n                        \"amount\": 2,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00199402,\n                        \"mmol_l\": 0.00717234,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The stated 0.1% w/v strength is 0.1 g/100 mL = 1 mg/mL. Thus the stated source dose delivers 2 mg iron sulfate heptahydrate per batch, not the local numeric dose in g/L. Retain the iron stock’s 0.1 N H2SO4 qualifier without converting normality to molarity."
  },
  {
    "ingredient_or_context": "Main: Trace element solution",
    "field_path": "solutions[3].concentration",
    "decision": "correct",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[13]",
        "exact_source_quote": "\"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Main: Carbon dioxide gas",
    "field_path": "ingredients[10].concentration",
    "decision": "not_quantified",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[14]",
        "exact_source_quote": "\"component_name\": \"Carbon dioxide gas\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      }
    ],
    "rationale": "The gas identity is present as VARIABLE; neither source supplies a fixed gas mass or volumetric dose. The specified atmosphere fractions, duration and pressure belong to preparation, not g/L.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "Main: Hydrogen gas",
    "field_path": "ingredients[11].concentration",
    "decision": "not_quantified",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[0].items[15]",
        "exact_source_quote": "\"component_name\": \"Hydrogen gas\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      }
    ],
    "rationale": "The gas identity is present as VARIABLE; neither source supplies a fixed gas mass or volumetric dose. The specified atmosphere fractions, duration and pressure belong to preparation, not g/L.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "M2714 trace stock: Distilled water",
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "local": {
      "value": "2000.0",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[15]",
        "exact_source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2000.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "M2714 trace stock: MgSO4 x 7 H2O",
    "field_path": "ingredients[1].concentration",
    "decision": "correct",
    "local": {
      "value": "3.09",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4 x 7 H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.09",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.09",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: NaCl",
    "field_path": "ingredients[2].concentration",
    "decision": "correct",
    "local": {
      "value": "2.0",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: CaCl2 x 2 H2O",
    "field_path": "ingredients[3].concentration",
    "decision": "correct",
    "local": {
      "value": "0.16",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"CaCl2 x 2 H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.16",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.16",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: Na2MoO4 x 2 H2O",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4 x 2 H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: H3BO3",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: FeSO4 x 7 H2O",
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"FeSO4 x 7 H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: NiCl2 x 6 H2O",
    "field_path": "ingredients[15].concentration",
    "decision": "correct",
    "local": {
      "value": "0.03",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"NiCl2 x 6 H2O\",\n          \"volume\": 0.03,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: ZnSO4 x 7 H2O",
    "field_path": "ingredients[16].concentration",
    "decision": "correct",
    "local": {
      "value": "0.18",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"ZnSO4 x 7 H2O\",\n          \"volume\": 0.18,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: CuSO4 x 5 H2O",
    "field_path": "ingredients[17].concentration",
    "decision": "correct",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"CuSO4 x 5 H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: Na2SeO3 x 5 H2O",
    "field_path": "ingredients[18].concentration",
    "decision": "correct",
    "local": {
      "value": "0.3",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[10]",
        "exact_source_quote": "\"component_name\": \"Na2SeO3 x 5 H2O\",\n          \"volume\": 0.3,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "0.3 mg × 0.001 g/mg = 0.0003 g per stock batch. The local same numeric value in g/L is 1000 times the stock mass on a nominal 1 L basis, and still omits the 1 mL receiving dose."
  },
  {
    "ingredient_or_context": "M2714 trace stock: CoSO4 x 7 H2O",
    "field_path": "ingredients[19].concentration",
    "decision": "correct",
    "local": {
      "value": "0.18",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[11]",
        "exact_source_quote": "\"component_name\": \"CoSO4 x 7 H2O\",\n          \"volume\": 0.18,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: KAl(SO4)2 x 12 H2O",
    "field_path": "ingredients[20].concentration",
    "decision": "correct",
    "local": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[12]",
        "exact_source_quote": "\"component_name\": \"KAl(SO4)2 x 12 H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: Nitrilotriacetic acid",
    "field_path": "ingredients[21].concentration",
    "decision": "correct",
    "local": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[13]",
        "exact_source_quote": "\"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: Na2WO4 x 2 H2O",
    "field_path": "ingredients[22].concentration",
    "decision": "correct",
    "local": {
      "value": "0.4",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[14]",
        "exact_source_quote": "\"component_name\": \"Na2WO4 x 2 H2O\",\n          \"volume\": 0.4,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\": 0.00121267,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "0.4 mg × 0.001 g/mg = 0.0004 g per stock batch. The local same numeric value in g/L is 1000 times the stock mass on a nominal 1 L basis, and still omits the 1 mL receiving dose."
  },
  {
    "ingredient_or_context": "M2714 trace stock: MnSO4 x H2O",
    "field_path": "ingredients[23].concentration",
    "decision": "correct",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[15]",
        "exact_source_quote": "\"component_name\": \"MnSO4 x H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Restore the exact source batch amount, original unit and main-versus-stock stage; no measured final concentration is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes source stock grams ×1/1000 grams per main batch. Final main g/L additionally requires an established final volume; the stock’s water quantity alone is not such a declaration."
  },
  {
    "ingredient_or_context": "M2714 trace stock: KOH solution",
    "field_path": "solutions[4].concentration",
    "decision": "correct",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.components[1].items[16]",
        "exact_source_quote": "\"component_name\": \"KOH solution\"",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      }
    ],
    "rationale": "KOH is an unquantified titrant for the trace-stock pH 6.5 then 7.0, not a main-medium stock dose. Retain the absence of a fixed amount while restoring stock scope.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Main atmosphere 80% H2/20% CO2 and 30–45 min",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Dissolve ingredients (except nitrate, carbonate and sulfide), then sparge medium with 80% H2 and 20% CO2 gas mixture for 30 – 45 min to make it anoxic.",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      }
    ],
    "rationale": "Add this source-specific preparation context with claim evidence; it is not an ingredient concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Example 10 mL in 25 mL vessels; autoclaving",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "Dispense medium under same gas atmosphere into anoxic serum vials (e.g., 10 ml medium in 25 ml Balchtype tubes) and autoclave.",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      }
    ],
    "rationale": "Preserve the source example as an example, not a mandatory batch size; no autoclave temperature/duration is specified.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Nitrate 100% N2 and carbonate 80% N2/20% CO2 stocks",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.comments[2].comment",
        "exact_source_quote": "Prior to use add nitrate from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture.",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      }
    ],
    "rationale": "Add this source-specific preparation context with claim evidence; it is not an ingredient concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main pH 7.2",
    "field_path": "ph_value",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.comments[3].comment",
        "exact_source_quote": "adjust pH of the medium to 7.2.",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      }
    ],
    "rationale": "Add this source-specific preparation context with claim evidence; it is not an ingredient concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "ph_value",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "TOGO sulfide 100% N2 before inoculation",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.comments[3].comment",
        "exact_source_quote": "Before inoculation add sulfide from a sterile anoxic stock solution prepared under 100% N2 gas and adjust pH of the medium to 7.2.",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      }
    ],
    "rationale": "Add this source-specific preparation context with claim evidence; it is not an ingredient concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Pressure and timing conflict",
    "field_path": "preparation_steps",
    "decision": "conflict",
    "local": null,
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.comments[3].comment",
        "exact_source_quote": "After inoculation pressurize vials to 2 bar overpressure with sterile 80% H2 and 20% CO2 gas mixture.",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      },
      {
        "source_key": "dsmz716",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium716.pdf",
        "source_locator": "PDF page1 preparation paragraph2",
        "exact_source_quote": "After growth has started pressurize vials to 0.5 bar overpressure with a sterile 80% H2\nand 20% CO2 gas mixture.",
        "snapshot_sha256": "a25c391fab84a47a454da6c5ad9aa95eb2d973c519fbb1aae1fdccec6506f66c",
        "parsed_text_sha256": "b5d3edff32b291b3781935bd644110717bf51edd0753966a30c7ba435a712b6f"
      }
    ],
    "rationale": "Preserve both source pressure/timing claims and resolve which source formulation is intended. No supported chronology chooses one.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Trace-stock initial pH 6.5 and final pH 7.0/KOH",
    "field_path": "solutions[3].preparation_notes",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.comments[5].comment",
        "exact_source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      }
    ],
    "rationale": "These endpoints belong to the correct locally defined mineral stock, not the wrongly linked 6187 or the main medium. KOH strength and dose are not supplied.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[3].preparation_notes",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "solutions[3].preparation_notes",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Unquantified KOH stock titrant",
    "field_path": "solutions[4].concentration",
    "decision": "not_quantified",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_snippets": [
      {
        "source_key": "togoM2714",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714",
        "source_locator": "$.comments[5].comment",
        "exact_source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "snapshot_sha256": "99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc"
      }
    ],
    "rationale": "No fixed KOH amount or stock strength is supplied. Scope correction is separately required; do not invent a dose.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "Main nominal volume discrepancy",
    "field_path": "preparation_steps",
    "decision": "conflict",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1003",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"attribute\": \"0.1% w/v in 0.1 N H2SO4\",\n                        \"amount\": 2,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00199402,\n                        \"mmol_l\": 0.00717234,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.2,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000199402,\n                        \"mmol_l\": 0.00153861,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "Listed liquid additions total 1003.7 mL, whereas the provider declares 1003 mL; neither establishes a measured final volume after separately prepared nitrate/carbonate/reductant additions.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "arithmetic": "1000 +2 +0.2 +1 +0.5 =1003.7 mL; no final g/L denominator is selected."
  },
  {
    "ingredient_or_context": "DSMZ-only DTT preparation alternative",
    "field_path": "preparation_steps",
    "decision": "conflict",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz716",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium716.pdf",
        "source_locator": "PDF page1 preparation paragraph1",
        "exact_source_quote": "from an anoxic stock solution sterilized by filtration under 100% N2 gas and adjust the pH\nof the medium to 7.2.",
        "snapshot_sha256": "a25c391fab84a47a454da6c5ad9aa95eb2d973c519fbb1aae1fdccec6506f66c",
        "parsed_text_sha256": "b5d3edff32b291b3781935bd644110717bf51edd0753966a30c7ba435a712b6f"
      },
      {
        "source_key": "mediadive716api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/716",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"DL-Dithiothreitol\",\n                        \"compound_id\": 151,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\": 1.93845,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c"
      }
    ],
    "rationale": "The DTT 0.3 g/100% N2 filter-sterilized addition belongs to the captured DSMZ formulation; do not silently insert it into the TOGO sulfide version.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Context-only6187: Na2-EDTA",
    "field_path": "composition[0].concentration",
    "decision": "verified",
    "local": {
      "value": "0.75",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\": 34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.75,\n                \"unit\": \"g\",\n                \"g_l\": 0.75,\n                \"mmol_l\": 2.23078,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "rationale": "Existing attached literal snippet, source hash and provider g_l agree within solution6187 only. This does not validate the receiver’s stock identity, measured final volume or chemical form.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.75",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context-only6187: Distilled water",
    "field_path": "composition[1].concentration",
    "decision": "correct",
    "local": {
      "value": "1000",
      "unit": "PERCENT_V_V"
    },
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "rationale": "The water row has no attached amount evidence and its PERCENT_V_V conversion is unsupported. Preserve the source’s actual 1000 mL water addition without inferring a measured final volume or receiver quantity.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "1000",
          "unit": "PERCENT_V_V"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Context-only6187: FeCl3 x 6 H2O",
    "field_path": "composition[2].concentration",
    "decision": "verified",
    "local": {
      "value": "0.097",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"FeCl3 x 6 H2O\",\n                \"compound_id\": 82,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 97,\n                \"unit\": \"mg\",\n                \"g_l\": 0.097,\n                \"mmol_l\": 0.358866,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "rationale": "Existing attached literal snippet, source hash and provider g_l agree within solution6187 only. This does not validate the receiver’s stock identity, measured final volume or chemical form.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.097",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context-only6187: MnCl2 x 4 H2O",
    "field_path": "composition[3].concentration",
    "decision": "verified",
    "local": {
      "value": "0.041",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 41,\n                \"unit\": \"mg\",\n                \"g_l\": 0.041,\n                \"mmol_l\": 0.20717,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "rationale": "Existing attached literal snippet, source hash and provider g_l agree within solution6187 only. This does not validate the receiver’s stock identity, measured final volume or chemical form.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "0.041",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context-only6187: ZnCl2 x 6 H2O",
    "field_path": "composition[4].concentration",
    "decision": "verified",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[4]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"ZnCl2 x 6 H2O\",\n                \"compound_id\": 2351,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.005,\n                \"mmol_l\": 0.0204583,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "rationale": "Existing attached literal snippet, source hash and provider g_l agree within solution6187 only. This does not validate the receiver’s stock identity, measured final volume or chemical form.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[4].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context-only6187: CoCl2 x 6 H2O",
    "field_path": "composition[5].concentration",
    "decision": "verified",
    "local": {
      "value": "0.002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0154037,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "rationale": "Existing attached literal snippet, source hash and provider g_l agree within solution6187 only. This does not validate the receiver’s stock identity, measured final volume or chemical form.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[5].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context-only6187: Na2MoO4 x 2 H2O",
    "field_path": "composition[6].concentration",
    "decision": "verified",
    "local": {
      "value": "0.004",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[6]",
        "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0165323,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "rationale": "Existing attached literal snippet, source hash and provider g_l agree within solution6187 only. This does not validate the receiver’s stock identity, measured final volume or chemical form.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[6].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "6187 placeholder ingredient",
    "field_path": "ingredients[0].concentration",
    "decision": "unsupported",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.name",
        "exact_source_quote": "\"name\": \"Trace element solution\"",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "rationale": "The placeholder is not a source compound or quantified addition; retain it as an existing context defect, not receiver evidence.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "6187 preparation water/EDTA quantities",
    "field_path": "preparation_notes",
    "decision": "evidence_only",
    "local": "Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \r\nfollowing sequence:",
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.steps[0].step",
        "exact_source_quote": "Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "rationale": "The preparation text agrees for this dependency; concentration evidence is attached to composition rows rather than this preparation claim. Do not convert the water addition into a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "preparation_notes",
        "stored": "Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \r\nfollowing sequence:",
        "decision": "evidence_only"
      }
    ]
  }
]

## Findings

### f1: Flattened stocks and wrong units change the medium formulation

blocker / open / confirmed; issue key: ammonifex-degensii-stock-unit-flattening.

Main and mineral-stock quantities have been summed, collapsed or represented together without the 1 mL dilution. Water is labeled as mass, four liquid stock doses as g/L, and selenite/tungstate mg as g/L. The owner’s later water/NaCl collapse means the target is additionally stale, but copying that owner alone would preserve the main stock defect.

### f2: The trace-stock reference denotes a different formulation

blocker / open / confirmed; issue key: ammonifex-degensii-wrong-trace-stock.

The asserted solution6187 is an EDTA/chloride stock, whereas M2714 defines an NTA/sulfate stock corroborated by DSMZ716/stock241. Six valid attached quantity claims in 6187 do not establish identity equivalence or support this link.

### f3: Missing preparation hides a material source disagreement

major / open / confirmed; issue key: ammonifex-degensii-source-preparation-conflict.

Both medium layers omit the anaerobic sequence and pH. TOGO sulfide/2 bar after inoculation conflicts with DSMZ DTT/0.5 bar after growth starts. The shared source accession does not justify silently substituting one procedure.

### f4: Source hydrate specificity is not consistently represented

major / open / confirmed; issue key: ammonifex-degensii-hydrate-correspondence.

Nickel hexahydrate is mapped to anhydrous 34887; magnesium heptahydrate’s correct primary 31795 has generic/anhydrous secondary 32599. Phosphate 131527 has an anhydrous formula alongside a trihydrate synonym, leaving the source-form correspondence internally ambiguous. Do not use these terms to recalculate hydrate masses or molarity.

### f5: Complex and undefined categories lack source support

major / open / confirmed; issue key: ammonifex-degensii-composition-category.

Both captured recipes provide named chemical formulations and the provider marks the medium noncomplex. The local COMPLEX/UNDEFINED assertions do not follow from the inspected source.

### f6: Historical nitrate linkage remains unresolved

minor / open / confirmed; issue key: ammonifex-degensii-legacy-nitrate-link.

The asserted legacy MediaIngredientMech:000170 could not be resolved in the complete pinned public catalog/tree. This completed negative lookup does not invalidate the separately supported potassium-nitrate primary ID or establish a new equivalence.

## Recommended Actions And Acceptance Checks

### a1

Reconcile the maintained owner against the selected source version, separate main batches and local mineral stock, restore literal mg/ml units and supported preparation. Preserve the existing repair history; regenerate after source-stage correction. Resolve the volume discrepancy before any final-medium normalization.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve and represent the exact M2714 mineral stock, replacing or withdrawing the unsupported 6187 link through maintained-input curation. Keep 6187’s own evidence unchanged unless separately authorized for review.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Document the intended source representation and its exact preparation, preserving the alternative as an unresolved version conflict with no unsupported chronology. Keep gas fractions, pressure timing, sterilization methods and stock pH in their correct stages.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Reconcile exact supplied forms independently in each asserted slot, preserving original source masses and ambiguity where no supported replacement identifier is established.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Reassess classification against the reconciled exact source formulation and attach source support; do not derive classification from unresolved legacy stock placeholders.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Preserve the historical assertion and annotate its unresolved correspondence; use an exact supported migration only if independently established.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch026/252/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch026/252/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml:1:id: CultureMech:009265<br>./data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml:1:id: CultureMech:009265<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch026/source-preflight-bound/252/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 39 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch026/source-preflight-bound/252/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-3 | src/culturemech/import/togo_importer.py; _ingredient_from_item lines 273–339; _solution_from_item lines 533–585; _extract_primary_components lines 587–641; _extract_preparation_steps lines 644–668; _parse_unit lines 713–746 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-4 | scripts/repair_jcm_stock_preparations.py; leaf lines 161–237; stock lines 239–278; stages lines 335–364; procedures lines 366–461 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714; $.meta; $.components[0:2]; $.comments[0:6] | supports | Full exact M2714 structured source read. This is the immediate source version: sulfide 0.3 g and 2 bar after inoculation, with a locally defined NTA/sulfate mineral stock. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium716.pdf; DSMZ 716 PDF pages 1–2, complete main table/preparation and modified Wolin stock | supports | Both PDF pages read and visually inspected. This source uses DL-dithiothreitol 0.3 g and 0.5 bar after growth starts; it does not establish the chronology of the TOGO disagreement. |
| provider | https://mediadive.dsmz.de/rest/medium/716; $.data.medium and $.data.solutions[0:2] | supports | Exact MediaDive 716 main/stock rows and preparation agree with the captured DSMZ version. Its 1003 mL main declaration is distinct from the 1003.7 mL sum of listed liquid additions. |
| stock241 | https://mediadive.dsmz.de/rest/solution/241; $.data.id, recipe, volume and steps | supports | Exact modified Wolin NTA/sulfate stock. Only this stock is transferred for comparison; no receiving-medium identity follows from sharing it. |
| stock141-primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf; PDF page 2: Modified Wolin mineral solution only | supports | The explicitly referenced stock corroborates DSMZ 716. Other medium-141 ingredients, vitamins, organisms and conditions are outside the transferred scope. |
| dependency6187 | data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml; Entire scoped stock dependency including composition, all six evidence objects and nine history events | context_only | Exact internal reference resolves, but the EDTA/chloride formulation is different from M2714’s NTA/sulfate stock. Existing evidence is evaluated only for this dependency, not transferred to the receiving medium. |
| stock6187 | https://mediadive.dsmz.de/rest/solution/6187; $.data: exact referenced solution identity, seven recipe rows and preparation | supports | The referenced stock contains Na2-EDTA and chloride salts rather than the NTA/sulfate mineral recipe required by M2714/DSMZ 716. The generic shared name does not establish equivalence. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi18276 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18276; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:18276 resolves to dihydrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32599 resolves to magnesium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63043 resolves to potassium nitrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32599": [{"label": "Magnesium sulfate", "match_type": "preferred_term", "identifier": "CHEBI:32599", "preferred_term": "Magnesium sulfate", "ontology_id": "CHEBI:32599", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 15, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml", "events": 15, "timestamp_issues": []}] |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Complete pinned public catalog/tree; exact legacy identifier and filename search | supports | Completed bounded historical identifier search. No exact legacy 000170 identity was recovered; current CHEBI nitrate mapping is a separate assertion. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Complete pinned public catalog/tree; exact legacy identifier and filename search | supports | Completed bounded historical identifier search. No exact legacy 000170 identity was recovered; current CHEBI nitrate mapping is a separate assertion. |
| legacy-search | Pinned public MIM catalog and complete tree; Exact MediaIngredientMech:000170 string and 000170 filename check | context_only | No exact legacy identity found in the two complete captured resources; this does not prove the historical ID never existed. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch026/252/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch026/252/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |
| dependency-history | data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml; All nine history events and six full evidence explanations | context_only | All nine dependency events were read; two timestamps lack timezone information. Six exact current source snippets/hashes match their attached historical claims, but their historical access time is not independently authenticated. Preserve these events rather than rewriting them. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No source revision chronology is established between TOGO M2714 and DSMZ716. A provisional context sentence calling the linked primary newer is not adopted in this assessment.
- The linked 6187 dependency was read in full for identity and evidence scope; its own broader curation verdict is outside this single-medium review. Its attached quantities do not transfer across the incorrect reference.
- All exact primary/provider comparisons and the required current pinned lookup completed. Required historical correspondence for the asserted legacy MediaIngredientMech:000170 remains unavailable; this unresolved claim makes completion partial. The completed negative current lookup is not itself failed or unavailable.
- This scientific assessment preceded formal review validation and saving; their results are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T150008Z-culturemech-009265-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: ammonifex_degensii_medium (CultureMech:009265)'
started_at: '2026-10-21T14:47:42Z'
finished_at: '2026-10-21T15:00:08Z'
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
summary: The TOGO M2714 record flattens a mineral stock into the medium, misstates
  liquid and milligram amounts, and points to a different trace-stock recipe. The
  linked DSMZ 716 source disagrees with TOGO on reductant and pressure; preserve both
  source representations while reconciling preparation, chemical forms and the stale
  generated layer.
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
  - path: data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml
    sha256: 17342357da96fe8b103903563a9769a5946f1a33e6d154fc7e7abe84f7c8a5af
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
    sha256: e4ecc665b651e9f3141dfd551be91da578f97c58721518d4f5a1bd99e5617e29
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    sha256: 955006bc9e48d5032fd4cd252d70fb954591eb54cd393da5bb89b3b763702987
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
  - path: scripts/fetch_medium_concentration_sources.py
    sha256: 746c2828863e6ee409d88409a540ea0a8d01ffad3e38be4a4a47f47bec5bbeb5
    role: context
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
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
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
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
  - path: src/culturemech/convert/togo_raw_yaml.py
    sha256: ce5e73545c9ecde54724259d2fd475676c0f3cb44dcfd283950e89fd49c10993
    role: context
  - path: src/culturemech/curate/curation_event.py
    sha256: e8aa053ba6dd06485b29ca5da640f91ef96513feff18492a72adc12f40130024
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
    sha256: 64a778108fd3197a8cc08082f80c1de3ec33eda58350cee5df612ab61d23cea1
    role: context
  - path: src/culturemech/validation/recipe_references.py
    sha256: 5d49d3db2f043a82b253e5a0bed03239004043922e1daab43c399a84d64fc237
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 252; batch 026 item 2 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-five task batches
    contain 250 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 253 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009265
targets:
- target_id: CultureMech:009265
  path: data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml
  label: ammonifex_degensii_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch026/252/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch026/252/strict.tsv"
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009265
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
  - CultureMech:009265
- check_id: legacy-current-exact-lookup
  name: Exact current pinned legacy identifier lookup
  required: true
  status: passed
  summary: The complete pinned catalog/tree exact lookup completed; no legacy000170
    correspondence was recovered.
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - legacy-search
  - mimPinnedCatalog
  - mimPinnedTree
- check_id: legacy-historical-correspondence
  name: Required historical correspondence for asserted legacy000170
  required: true
  status: unavailable
  summary: The record asserts a historical identifier whose exact correspondence is
    not established by the available captured resources. A completed current negative
    lookup does not resolve that historical claim.
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - legacy-search
  - record
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:49:35.197710Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch026/252/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T14:49:36.674211Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch026/252/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:49:38.370438Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:49:39.498552Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T15:00:07Z'
  support: supports
  summary: './data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml:1:id: CultureMech:009265

    ./data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml:1:id:
    CultureMech:009265

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/source-preflight-bound/252/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T15:00:07Z'
  support: supports
  summary: 39 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: d1bdeb566adfe6aca5700dc1914108473af6f6d0e1b01ee9c21dcf08fc21a1ef
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/source-preflight-bound/252/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: dc6d10702af9a8ca2e514a2d81698b6522d47b8b4ed7da88441e66ec625ecd2a
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-context-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570;
    _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps
    lines 653–721
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-context-3
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item lines 273–339; _solution_from_item lines 533–585;
    _extract_primary_components lines 587–641; _extract_preparation_steps lines 644–668;
    _parse_unit lines 713–746
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-context-4
  kind: record_content
  reference: scripts/repair_jcm_stock_preparations.py
  locator: leaf lines 161–237; stock lines 239–278; stages lines 335–364; procedures
    lines 366–461
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714
  locator: $.meta; $.components[0:2]; $.comments[0:6]
  accessed_at: '2026-10-21T14:16:59.242703Z'
  support: supports
  summary: 'Full exact M2714 structured source read. This is the immediate source
    version: sulfide 0.3 g and 2 bar after inoculation, with a locally defined NTA/sulfate
    mineral stock.'
  snapshot_sha256: 99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium716.pdf
  locator: DSMZ 716 PDF pages 1–2, complete main table/preparation and modified Wolin
    stock
  accessed_at: '2026-10-21T14:17:00.126640Z'
  support: supports
  summary: Both PDF pages read and visually inspected. This source uses DL-dithiothreitol
    0.3 g and 0.5 bar after growth starts; it does not establish the chronology of
    the TOGO disagreement.
  snapshot_sha256: a25c391fab84a47a454da6c5ad9aa95eb2d973c519fbb1aae1fdccec6506f66c
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/716
  locator: $.data.medium and $.data.solutions[0:2]
  accessed_at: '2026-10-21T14:16:58.882943Z'
  support: supports
  summary: Exact MediaDive 716 main/stock rows and preparation agree with the captured
    DSMZ version. Its 1003 mL main declaration is distinct from the 1003.7 mL sum
    of listed liquid additions.
  snapshot_sha256: e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c
- evidence_id: stock241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/241
  locator: $.data.id, recipe, volume and steps
  accessed_at: '2026-10-21T10:37:16.846684Z'
  support: supports
  summary: Exact modified Wolin NTA/sulfate stock. Only this stock is transferred
    for comparison; no receiving-medium identity follows from sharing it.
  snapshot_sha256: 50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d
- evidence_id: stock141-primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf
  locator: 'PDF page 2: Modified Wolin mineral solution only'
  accessed_at: '2026-10-21T10:13:12.306566Z'
  support: supports
  summary: The explicitly referenced stock corroborates DSMZ 716. Other medium-141
    ingredients, vitamins, organisms and conditions are outside the transferred scope.
  snapshot_sha256: 8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8
- evidence_id: dependency6187
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
  locator: Entire scoped stock dependency including composition, all six evidence
    objects and nine history events
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: Exact internal reference resolves, but the EDTA/chloride formulation is
    different from M2714’s NTA/sulfate stock. Existing evidence is evaluated only
    for this dependency, not transferred to the receiving medium.
  snapshot_sha256: 955006bc9e48d5032fd4cd252d70fb954591eb54cd393da5bb89b3b763702987
- evidence_id: stock6187
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6187
  locator: '$.data: exact referenced solution identity, seven recipe rows and preparation'
  accessed_at: '2026-10-21T14:16:58.890288Z'
  support: supports
  summary: The referenced stock contains Na2-EDTA and chloride salts rather than the
    NTA/sulfate mineral recipe required by M2714/DSMZ 716. The generic shared name
    does not establish equivalence.
  snapshot_sha256: d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
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
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: CHEBI:16526 resolves to carbon dioxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi18276
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18276
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:27.615173Z'
  support: supports
  summary: CHEBI:18276 resolves to dihydrogen. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 47a32d9cfe41e3759385a0e4e002e9fa208fe1511d84e3d0d1f9f1ca9ce6e86d
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
- evidence_id: chebi29377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:31:16.500548Z'
  support: supports
  summary: CHEBI:29377 resolves to sodium carbonate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
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
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to nickel dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
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
- evidence_id: chebi63043
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:40.679699Z'
  support: supports
  summary: CHEBI:63043 resolves to potassium nitrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: c324450e6330a169c708c32a7908b6df0276f4dc76da413e473b563928f61c13
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
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
- evidence_id: chebi91244
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:07.079384Z'
  support: supports
  summary: CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T15:00:07Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377":
    [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377",
    "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440":
    [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32599": [{"label": "Magnesium sulfate", "match_type": "preferred_term",
    "identifier": "CHEBI:32599", "preferred_term": "Magnesium sulfate", "ontology_id":
    "CHEBI:32599", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118":
    [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label":
    "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557",
    "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4",
    "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836":
    [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O",
    "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label":
    "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id":
    "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244":
    [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244",
    "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AMMONIFEX_DEGENSII_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: '[{"input": "target", "events": 15, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml", "events":
    15, "timestamp_issues": []}]'
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Complete pinned public catalog/tree; exact legacy identifier and filename
    search
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: Completed bounded historical identifier search. No exact legacy 000170
    identity was recovered; current CHEBI nitrate mapping is a separate assertion.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Complete pinned public catalog/tree; exact legacy identifier and filename
    search
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: supports
  summary: Completed bounded historical identifier search. No exact legacy 000170
    identity was recovered; current CHEBI nitrate mapping is a separate assertion.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: legacy-search
  kind: search
  reference: Pinned public MIM catalog and complete tree
  locator: Exact MediaIngredientMech:000170 string and 000170 filename check
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: No exact legacy identity found in the two complete captured resources;
    this does not prove the historical ID never existed.
  search_scope: All 2953 records in the captured pinned MIM catalog and all 7384 entries
    in the complete captured tree; exact identifier/filename only, no sibling lookup
    or invented equivalence.
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/252/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: a4142f02d78c1316bb50825c61469850bae41d6991431d12c578404a943ef929
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/252/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: cc723e31baca6c0a0c144f043b657418d30ae303572127ccd9714a30afcd7b49
- evidence_id: dependency-history
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
  locator: All nine history events and six full evidence explanations
  accessed_at: '2026-10-21T15:00:07Z'
  support: context_only
  summary: All nine dependency events were read; two timestamps lack timezone information.
    Six exact current source snippets/hashes match their attached historical claims,
    but their historical access time is not independently authenticated. Preserve
    these events rather than rewriting them.
  snapshot_sha256: 955006bc9e48d5032fd4cd252d70fb954591eb54cd393da5bb89b3b763702987
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '25 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 24/24
    primary and 21/24 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131361
  - chebi131527
  - chebi15377
  - chebi16526
  - chebi18276
  - chebi26710
  - chebi29377
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi32599
  - chebi33118
  - chebi34887
  - chebi44557
  - chebi62946
  - chebi63036
  - chebi63043
  - chebi63939
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi86158
  - chebi86364
  - chebi86465
  - chebi91244
  details: 'Instance coverage on a 0–100 percent scale, denominator 24: primary 100.00%;
    secondary 87.50%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 30 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Immediate source, linked primary and maintained input
  outcome: concern
  summary: The target is the generated copy of TOGO M2714, which explicitly points
    to DSMZ 716. Both captured sources are available, but TOGO specifies sulfide and
    2 bar after inoculation while DSMZ/MediaDive specify DL-dithiothreitol and 0.5
    bar after growth starts. These are separate current source representations; no
    evidence dates the change or supports calling one version newer. The target also
    predates its owner’s identical-duplicate collapse of water and NaCl; that repair
    did not restore stock scope.
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - record
  - owner-0
  - togo
  - primary
  - provider
- assessment_id: stock-identity
  area: identity
  topic: Asserted trace-stock reference
  outcome: concern
  summary: The solution6187 link resolves to an EDTA/chloride formulation, not the
    locally defined M2714 NTA/sulfate formulation corroborated by modified Wolin stock241.
    Its six existing concentration attachments correctly support their own provider-declared
    solution values, but cannot validate the receiver’s link. The dependency’s 1000
    PERCENT_V_V water, placeholder ingredient and zinc-hydrate/generic-ID mismatch
    must not be inherited as a repair.
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - record
  - owner-0
  - dependency6187
  - stock6187
  - stock241
  - stock141-primary
  - togo
- assessment_id: formulation
  area: consistency
  topic: Main amounts, stock quantities and generated divergence
  outcome: concern
  summary: The target sums water to 2000 g/L and NaCl to 2 g/L; its owner collapses
    these to 1000 and 1 but still mixes main and trace-stock stages. Both retain MgSO4·7H2O
    3.09 and CaCl2·2H2O 0.16 g/L as sums of main and undiluted stock amounts. Source
    0.3 mg selenite and 0.4 mg tungstate become 0.3 and 0.4 g/L locally, a 1000-fold
    mass-unit error even before stock dilution. Four liquid stock doses are mislabeled
    G_PER_L. Other source grams are batch amounts; 1000 mL water and provider volume
    1003 do not independently establish a final denominator.
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - record
  - owner-0
  - togo
  - primary
  - provider
- assessment_id: preparation
  area: completeness
  topic: Missing anaerobic sequence and source-specific pressures
  outcome: concern
  summary: Neither medium layer contains the source preparation or pH 7.2. Common
    supported details include 80% H2/20% CO2 for 30–45 minutes, the example 10 mL
    in 25 mL vessels, nitrate under 100% N2, carbonate under 80% N2/20% CO2, and stock
    pH 6.5 then 7.0 with unquantified KOH. Retain the TOGO sulfide/2-bar sequence
    separately from DSMZ’s filter-sterilized DTT/0.5-bar sequence. No autoclave cycle,
    fixed gas amount, KOH dose or later-stock strength is inferred.
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - record
  - owner-0
  - togo
  - primary
- assessment_id: forms
  area: grounding
  topic: Hydrates, secondary specificity and legacy identifier
  outcome: concern
  summary: Nickel hexahydrate uses anhydrous CHEBI:34887. MgSO4 heptahydrate has correct
    primary CHEBI:31795 but generic/anhydrous secondary CHEBI:32599. Source K2HPO4
    trihydrate uses CHEBI:131527, whose formula HO4P.2K and mass 174.174 omit hydrate
    waters even though a trihydrate synonym is present; preserve that internal term
    ambiguity rather than claiming the synonym proves the form or inventing a replacement.
    Selenite CHEBI:131361 explicitly has the pentahydrate formula and is not a form
    error. Legacy nitrate 000170 remains historically unresolved after a completed
    bounded lookup, separately from its supported primary CHEBI:63043.
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - record
  - togo
  - primary
  - chebi34887
  - chebi31795
  - chebi32599
  - chebi131527
  - chebi131361
  - chebi63043
  - legacy-search
- assessment_id: classification
  area: scope
  topic: Defined chemical formulation versus complex category
  outcome: concern
  summary: The source lists named chemical components and identified stock compositions;
    MediaDive explicitly marks the medium noncomplex. COMPLEX/UNDEFINED is unsupported
    by these inspected formulations and should be reassessed with the selected source
    version. LIQUID is supported by the absence of a solidifying ingredient. No organism
    growth or exact strain identification is inferred solely from the medium name
    or generic application.
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - record
  - togo
  - primary
  - provider
- assessment_id: writers
  area: provenance
  topic: Current source separation and repair limits
  outcome: concern
  summary: Current TOGO parsing separates main sections and local stock compositions,
    preserves ml/mg units, and extracts preparation comments. The cleanup code no
    longer sums differing duplicates, while source-stage reconciliation is still necessary
    here. These are current implementation observations, not proof of the historical
    execution path. Correct the maintained source representation, preserve the existing
    repair history and regenerate the stale target after review.
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - record
  - owner-0
  - writer-context-0
  - writer-context-1
  - writer-context-2
  - writer-context-3
  - writer-context-4
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 52 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009265
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"Main: Na-resazurin solution (0.1%\
    \ w/v)\",\n    \"field_path\": \"solutions[0].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.5\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na-resazurin solution (0.1% w/v)\\\",\\n     \
    \     \\\"volume\\\": 0.5,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\
    \"conc_value\\\": 0.1,\\n          \\\"conc_unit\\\": \\\"(w/v)\\\"\",\n     \
    \   \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\
    \": 1852,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n  \
    \                      \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.000498504,\\n       \
    \                 \\\"mmol_l\\\": 0.00198473,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact source batch amount,\
    \ original unit and main-versus-stock stage; no measured final concentration is\
    \ established.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"solutions[0].concentration\",\n        \"stored\": {\n   \
    \       \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The\
    \ stated 0.1% w/v strength is 0.1 g/100 mL = 1 mg/mL. Thus the stated source dose\
    \ delivers 0.5 mg sodium resazurin per batch, not the local numeric dose in g/L.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Main: NiCl2 x 6 H2O solution (0.1%\
    \ w/v)\",\n    \"field_path\": \"solutions[1].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.2\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2 x 6 H2O solution (0.1% w/v)\\\",\\n    \
    \      \\\"volume\\\": 0.2,\\n          \\\"unit\\\": \\\"ml\\\",\\n         \
    \ \\\"conc_value\\\": 0.1,\\n          \\\"conc_unit\\\": \\\"(w/v)\\\"\",\n \
    \       \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n    \
    \                    \\\"amount\\\": 0.2,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.000199402,\\n       \
    \                 \\\"mmol_l\\\": 0.00153861,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact source batch amount,\
    \ original unit and main-versus-stock stage; no measured final concentration is\
    \ established.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"solutions[1].concentration\",\n        \"stored\": {\n   \
    \       \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The\
    \ stated 0.1% w/v strength is 0.1 g/100 mL = 1 mg/mL. Thus the stated source dose\
    \ delivers 0.2 mg nickel chloride hexahydrate per batch, not the local numeric\
    \ dose in g/L.\"\n  },\n  {\n    \"ingredient_or_context\": \"Main: Distilled\
    \ water\",\n    \"field_path\": \"ingredients[0].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"2000.0\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1000,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact source batch amount,\
    \ original unit and main-versus-stock stage; no measured final concentration is\
    \ established.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"2000.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main: MgSO4 x 7 H2O\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"3.09\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 0.09,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.09,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0897308,\\\
    n                        \\\"mmol_l\\\": 0.364055,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"3.09\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.09\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main: NaCl\",\n    \"field_path\": \"ingredients[2].concentration\",\n   \
    \ \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"2.0\",\n  \
    \    \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 1,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.997009,\\n           \
    \             \\\"mmol_l\\\": 17.0604,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact source batch amount,\
    \ original unit and main-versus-stock stage; no measured final concentration is\
    \ established.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main: CaCl2 x 2 H2O\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.16\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2 x 2 H2O\\\",\\n          \\\"volume\\\"\
    : 0.06,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.06,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0598205,\\\
    n                        \\\"mmol_l\\\": 0.406901,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.16\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.16\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main: KH2PO4\",\n    \"field_path\": \"ingredients[4].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.22\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.22,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.22,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.219342,\\n     \
    \                   \\\"mmol_l\\\": 1.6118,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact source batch amount,\
    \ original unit and main-versus-stock stage; no measured final concentration is\
    \ established.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.22\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.22\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main: Na2S x 9 H2O\",\n    \"field_path\": \"ingredients[5].concentration\"\
    ,\n    \"decision\": \"conflict\",\n    \"local\": {\n      \"value\": \"0.3\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2S x 9 H2O\\\",\\n          \\\"volume\\\":\
    \ 0.3,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"DL-Dithiothreitol\\\",\\n                        \\\"compound_id\\\
    \": 151,\\n                        \\\"amount\\\": 0.3,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.299103,\\\
    n                        \\\"mmol_l\\\": 1.93845,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"TOGO specifies 0.3 g sodium sulfide nonahydrate,\
    \ whereas DSMZ/MediaDive specifies 0.3 g DL-dithiothreitol. Preserve the source\
    \ disagreement; matching numbers do not establish chemical equivalence.\",\n \
    \   \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.3\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"conflict\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"conflict\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main: (NH4)2SO4\",\n    \"field_path\": \"ingredients[6].concentration\",\n\
    \    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.22\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"(NH4)2SO4\\\",\\n          \\\"volume\\\": 0.22,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 0.22,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.219342,\\\
    n                        \\\"mmol_l\\\": 1.65992,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.22\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.22\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main: Na2CO3\",\n    \"field_path\": \"ingredients[7].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1.5\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2CO3\\\",\\n          \\\"volume\\\": 1.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"Na2CO3\\\",\\n                        \\\"compound_id\\\"\
    : 32,\\n                        \\\"amount\\\": 1.5,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.49551,\\\
    n                        \\\"mmol_l\\\": 14.1102,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main: KNO3\",\n    \"field_path\": \"ingredients[8].concentration\",\n   \
    \ \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1\",\n    \
    \  \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KNO3\\\",\\n          \\\"volume\\\": 1,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"KNO3\\\",\\n                        \\\"compound_id\\\": 191,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.997009,\\n           \
    \             \\\"mmol_l\\\": 9.86132,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact source batch amount,\
    \ original unit and main-versus-stock stage; no measured final concentration is\
    \ established.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main: K2HPO4 x 3 H2O\",\n    \"field_path\": \"ingredients[9].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.3\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4 x 3 H2O\\\",\\n          \\\"volume\\\"\
    : 0.3,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"K2HPO4 x 3 H2O\\\",\\n                        \\\"compound_id\\\
    \": 244,\\n                        \\\"amount\\\": 0.3,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.299103,\\\
    n                        \\\"mmol_l\\\": 1.71724,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[9].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.3\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main: FeSO4 x 7 H2O solution (0.1% w/v in 0.1 N H2SO4)\",\n    \"field_path\"\
    : \"solutions[2].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"2\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM2714\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\",\n\
    \        \"source_locator\": \"$.components[0].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4 x 7 H2O solution (0.1% w/v in 0.1 N H2SO4)\\\
    \",\\n          \\\"volume\\\": 2,\\n          \\\"unit\\\": \\\"ml\\\"\",\n \
    \       \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"attribute\\\": \\\"0.1% w/v in 0.1 N H2SO4\\\
    \",\\n                        \\\"amount\\\": 2,\\n                        \\\"\
    unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.00199402,\\n  \
    \                      \\\"mmol_l\\\": 0.00717234,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The\
    \ stated 0.1% w/v strength is 0.1 g/100 mL = 1 mg/mL. Thus the stated source dose\
    \ delivers 2 mg iron sulfate heptahydrate per batch, not the local numeric dose\
    \ in g/L. Retain the iron stock’s 0.1 N H2SO4 qualifier without converting normality\
    \ to molarity.\"\n  },\n  {\n    \"ingredient_or_context\": \"Main: Trace element\
    \ solution\",\n    \"field_path\": \"solutions[3].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"1\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution\\\",\\n          \\\"volume\\\
    \": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main: Carbon dioxide gas\",\n    \"field_path\": \"ingredients[10].concentration\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local\": {\n      \"value\": \"\
    variable\",\n      \"unit\": \"VARIABLE\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[14]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Carbon dioxide gas\\\"\",\n        \"snapshot_sha256\"\
    : \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n     \
    \ }\n    ],\n    \"rationale\": \"The gas identity is present as VARIABLE; neither\
    \ source supplies a fixed gas mass or volumetric dose. The specified atmosphere\
    \ fractions, duration and pressure belong to preparation, not g/L.\",\n    \"\
    action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\":\
    \ [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"variable\",\n          \"unit\"\
    : \"VARIABLE\"\n        },\n        \"decision\": \"not_quantified\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Main: Hydrogen gas\",\n    \"field_path\": \"\
    ingredients[11].concentration\",\n    \"decision\": \"not_quantified\",\n    \"\
    local\": {\n      \"value\": \"variable\",\n      \"unit\": \"VARIABLE\"\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2714\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[0].items[15]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Hydrogen gas\\\"\",\n        \"snapshot_sha256\"\
    : \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n     \
    \ }\n    ],\n    \"rationale\": \"The gas identity is present as VARIABLE; neither\
    \ source supplies a fixed gas mass or volumetric dose. The specified atmosphere\
    \ fractions, duration and pressure belong to preparation, not g/L.\",\n    \"\
    action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\":\
    \ [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[11].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"variable\",\n          \"unit\"\
    : \"VARIABLE\"\n        },\n        \"decision\": \"not_quantified\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"M2714 trace stock: Distilled water\",\n    \"\
    field_path\": \"ingredients[0].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"local\": {\n      \"value\": \"2000.0\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2714\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1000,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[15]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 16,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact source batch amount,\
    \ original unit and main-versus-stock stage; no measured final concentration is\
    \ established.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"2000.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"M2714 trace stock: MgSO4 x 7 H2O\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"3.09\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 3,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 3,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n      \
    \                  \\\"mmol_l\\\": 12.1716,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact source batch amount,\
    \ original unit and main-versus-stock stage; no measured final concentration is\
    \ established.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"3.09\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.09\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose\
    \ contributes source stock grams ×1/1000 grams per main batch. Final main g/L\
    \ additionally requires an established final volume; the stock’s water quantity\
    \ alone is not such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"M2714 trace stock: NaCl\",\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"2.0\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 1,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n                  \
    \      \\\"mmol_l\\\": 17.1116,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact source batch amount,\
    \ original unit and main-versus-stock stage; no measured final concentration is\
    \ established.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"If\
    \ the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes\
    \ source stock grams ×1/1000 grams per main batch. Final main g/L additionally\
    \ requires an established final volume; the stock’s water quantity alone is not\
    \ such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\": \"M2714 trace\
    \ stock: CaCl2 x 2 H2O\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.16\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2 x 2 H2O\\\",\\n          \\\"volume\\\"\
    : 0.1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.680203,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact source batch amount,\
    \ original unit and main-versus-stock stage; no measured final concentration is\
    \ established.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.16\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.16\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose\
    \ contributes source stock grams ×1/1000 grams per main batch. Final main g/L\
    \ additionally requires an established final volume; the stock’s water quantity\
    \ alone is not such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"M2714 trace stock: Na2MoO4 x 2 H2O\",\n    \"field_path\": \"ingredients[12].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.01\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n          \\\"volume\\\"\
    : 0.01,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 0.01,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\n\
    \                        \\\"mmol_l\\\": 0.0413309,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose\
    \ contributes source stock grams ×1/1000 grams per main batch. Final main g/L\
    \ additionally requires an established final volume; the stock’s water quantity\
    \ alone is not such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"M2714 trace stock: H3BO3\",\n    \"field_path\": \"ingredients[13].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.01\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\":\
    \ 37,\\n                        \\\"amount\\\": 0.01,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\n \
    \                       \\\"mmol_l\\\": 0.161708,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[13].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose\
    \ contributes source stock grams ×1/1000 grams per main batch. Final main g/L\
    \ additionally requires an established final volume; the stock’s water quantity\
    \ alone is not such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"M2714 trace stock: FeSO4 x 7 H2O\",\n    \"field_path\": \"ingredients[14].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.1\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 0.1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"mmol_l\\\": 0.359693,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[14].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"If\
    \ the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes\
    \ source stock grams ×1/1000 grams per main batch. Final main g/L additionally\
    \ requires an established final volume; the stock’s water quantity alone is not\
    \ such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\": \"M2714 trace\
    \ stock: NiCl2 x 6 H2O\",\n    \"field_path\": \"ingredients[15].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.03\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2 x 6 H2O\\\",\\n          \\\"volume\\\"\
    : 0.03,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 0.03,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.03,\\\
    n                        \\\"mmol_l\\\": 0.231483,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[15].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.03\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose\
    \ contributes source stock grams ×1/1000 grams per main batch. Final main g/L\
    \ additionally requires an established final volume; the stock’s water quantity\
    \ alone is not such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"M2714 trace stock: ZnSO4 x 7 H2O\",\n    \"field_path\": \"ingredients[16].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.18\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 0.18,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 0.18,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.18,\\\
    n                        \\\"mmol_l\\\": 0.625954,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[16].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.18\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose\
    \ contributes source stock grams ×1/1000 grams per main batch. Final main g/L\
    \ additionally requires an established final volume; the stock’s water quantity\
    \ alone is not such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"M2714 trace stock: CuSO4 x 5 H2O\",\n    \"field_path\": \"ingredients[17].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.01\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuSO4 x 5 H2O\\\",\\n          \\\"volume\\\"\
    : 0.01,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 121,\\n                        \\\"amount\\\": 0.01,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\\
    n                        \\\"mmol_l\\\": 0.0400503,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[17].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose\
    \ contributes source stock grams ×1/1000 grams per main batch. Final main g/L\
    \ additionally requires an established final volume; the stock’s water quantity\
    \ alone is not such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"M2714 trace stock: Na2SeO3 x 5 H2O\",\n    \"field_path\": \"ingredients[18].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.3\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SeO3 x 5 H2O\\\",\\n          \\\"volume\\\"\
    : 0.3,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Na2SeO3 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 107,\\n                        \\\"amount\\\": 0.3,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0003,\\\
    n                        \\\"mmol_l\\\": 0.00114062,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[18].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.3\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"0.3\
    \ mg × 0.001 g/mg = 0.0003 g per stock batch. The local same numeric value in\
    \ g/L is 1000 times the stock mass on a nominal 1 L basis, and still omits the\
    \ 1 mL receiving dose.\"\n  },\n  {\n    \"ingredient_or_context\": \"M2714 trace\
    \ stock: CoSO4 x 7 H2O\",\n    \"field_path\": \"ingredients[19].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.18\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 0.18,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CoSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 198,\\n                        \\\"amount\\\": 0.18,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.18,\\\
    n                        \\\"mmol_l\\\": 1.16132,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[19].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.18\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose\
    \ contributes source stock grams ×1/1000 grams per main batch. Final main g/L\
    \ additionally requires an established final volume; the stock’s water quantity\
    \ alone is not such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"M2714 trace stock: KAl(SO4)2 x 12 H2O\",\n    \"field_path\": \"ingredients[20].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.02\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KAl(SO4)2 x 12 H2O\\\",\\n          \\\"volume\\\
    \": 0.02,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"AlK(SO4)2 x 12 H2O\\\",\\n                        \\\"compound_id\\\
    \": 908,\\n                        \\\"amount\\\": 0.02,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\\
    n                        \\\"mmol_l\\\": 0.0421596,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[20].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.02\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"If the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose\
    \ contributes source stock grams ×1/1000 grams per main batch. Final main g/L\
    \ additionally requires an established final volume; the stock’s water quantity\
    \ alone is not such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"M2714 trace stock: Nitrilotriacetic acid\",\n    \"field_path\": \"ingredients[21].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrilotriacetic acid\\\",\\n          \\\"volume\\\
    \": 1.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Nitrilotriacetic acid\\\",\\n                        \\\"compound_id\\\
    \": 189,\\n                        \\\"amount\\\": 1.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n\
    \                        \\\"mmol_l\\\": 7.84765,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[21].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"If\
    \ the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes\
    \ source stock grams ×1/1000 grams per main batch. Final main g/L additionally\
    \ requires an established final volume; the stock’s water quantity alone is not\
    \ such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\": \"M2714 trace\
    \ stock: Na2WO4 x 2 H2O\",\n    \"field_path\": \"ingredients[22].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.4\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[14]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2WO4 x 2 H2O\\\",\\n          \\\"volume\\\"\
    : 0.4,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[14]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 15,\\n                        \\\
    \"compound\\\": \\\"Na2WO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 249,\\n                        \\\"amount\\\": 0.4,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0004,\\\
    n                        \\\"mmol_l\\\": 0.00121267,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Restore the exact source batch amount, original\
    \ unit and main-versus-stock stage; no measured final concentration is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[22].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.4\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"0.4\
    \ mg × 0.001 g/mg = 0.0004 g per stock batch. The local same numeric value in\
    \ g/L is 1000 times the stock mass on a nominal 1 L basis, and still omits the\
    \ 1 mL receiving dose.\"\n  },\n  {\n    \"ingredient_or_context\": \"M2714 trace\
    \ stock: MnSO4 x H2O\",\n    \"field_path\": \"ingredients[23].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[15]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnSO4 x H2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n \
    \                       \\\"mmol_l\\\": 2.9583,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact source batch amount,\
    \ original unit and main-versus-stock stage; no measured final concentration is\
    \ established.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[23].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"If\
    \ the mineral stock has the provider-declared 1000 mL basis, a 1 mL dose contributes\
    \ source stock grams ×1/1000 grams per main batch. Final main g/L additionally\
    \ requires an established final volume; the stock’s water quantity alone is not\
    \ such a declaration.\"\n  },\n  {\n    \"ingredient_or_context\": \"M2714 trace\
    \ stock: KOH solution\",\n    \"field_path\": \"solutions[4].concentration\",\n\
    \    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"variable\"\
    ,\n      \"unit\": \"VARIABLE\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.components[1].items[16]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KOH solution\\\"\",\n        \"snapshot_sha256\"\
    : \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n     \
    \ }\n    ],\n    \"rationale\": \"KOH is an unquantified titrant for the trace-stock\
    \ pH 6.5 then 7.0, not a main-medium stock dose. Retain the absence of a fixed\
    \ amount while restoring stock scope.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"solutions[4].concentration\",\n     \
    \   \"stored\": {\n          \"value\": \"variable\",\n          \"unit\": \"\
    VARIABLE\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"\
    ingredient_or_context\": \"Main atmosphere 80% H2/20% CO2 and 30–45 min\",\n \
    \   \"field_path\": \"preparation_steps\",\n    \"decision\": \"add\",\n    \"\
    local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Dissolve ingredients (except nitrate, carbonate and sulfide), then sparge\
    \ medium with 80% H2 and 20% CO2 gas mixture for 30 – 45 min to make it anoxic.\"\
    ,\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      }\n    ],\n    \"rationale\": \"Add this source-specific preparation context\
    \ with claim evidence; it is not an ingredient concentration.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Example 10 mL in 25 mL vessels; autoclaving\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM2714\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\",\n\
    \        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"Dispense medium under same gas atmosphere into anoxic serum vials (e.g., 10\
    \ ml medium in 25 ml Balchtype tubes) and autoclave.\",\n        \"snapshot_sha256\"\
    : \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n     \
    \ }\n    ],\n    \"rationale\": \"Preserve the source example as an example, not\
    \ a mandatory batch size; no autoclave temperature/duration is specified.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Nitrate 100% N2 and carbonate 80% N2/20% CO2 stocks\",\n    \"field_path\"\
    : \"preparation_steps\",\n    \"decision\": \"add\",\n    \"local\": null,\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2714\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.comments[2].comment\",\n        \"exact_source_quote\"\
    : \"Prior to use add nitrate from a sterile anoxic stock solution prepared under\
    \ 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under\
    \ 80% N2 and 20% CO2 gas mixture.\",\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      }\n    ],\n    \"rationale\": \"Add this source-specific preparation context\
    \ with claim evidence; it is not an ingredient concentration.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main pH 7.2\",\n    \"field_path\": \"ph_value\",\n    \"decision\": \"add\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.comments[3].comment\",\n        \"exact_source_quote\"\
    : \"adjust pH of the medium to 7.2.\",\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      }\n    ],\n    \"rationale\": \"Add this source-specific preparation context\
    \ with claim evidence; it is not an ingredient concentration.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ph_value\",\n      \
    \  \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"TOGO sulfide 100% N2 before inoculation\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM2714\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\",\n\
    \        \"source_locator\": \"$.comments[3].comment\",\n        \"exact_source_quote\"\
    : \"Before inoculation add sulfide from a sterile anoxic stock solution prepared\
    \ under 100% N2 gas and adjust pH of the medium to 7.2.\",\n        \"snapshot_sha256\"\
    : \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n     \
    \ }\n    ],\n    \"rationale\": \"Add this source-specific preparation context\
    \ with claim evidence; it is not an ingredient concentration.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Pressure and timing conflict\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"decision\": \"conflict\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM2714\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\",\n\
    \        \"source_locator\": \"$.comments[3].comment\",\n        \"exact_source_quote\"\
    : \"After inoculation pressurize vials to 2 bar overpressure with sterile 80%\
    \ H2 and 20% CO2 gas mixture.\",\n        \"snapshot_sha256\": \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\
    \n      },\n      {\n        \"source_key\": \"dsmz716\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium716.pdf\",\n    \
    \    \"source_locator\": \"PDF page1 preparation paragraph2\",\n        \"exact_source_quote\"\
    : \"After growth has started pressurize vials to 0.5 bar overpressure with a sterile\
    \ 80% H2\\nand 20% CO2 gas mixture.\",\n        \"snapshot_sha256\": \"a25c391fab84a47a454da6c5ad9aa95eb2d973c519fbb1aae1fdccec6506f66c\"\
    ,\n        \"parsed_text_sha256\": \"b5d3edff32b291b3781935bd644110717bf51edd0753966a30c7ba435a712b6f\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve both source pressure/timing claims\
    \ and resolve which source formulation is intended. No supported chronology chooses\
    \ one.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace-stock initial pH 6.5 and final pH 7.0/KOH\",\n    \"field_path\": \"\
    solutions[3].preparation_notes\",\n    \"decision\": \"add\",\n    \"local\":\
    \ null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2714\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.comments[5].comment\",\n        \"exact_source_quote\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\":\
    \ \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n     \
    \ }\n    ],\n    \"rationale\": \"These endpoints belong to the correct locally\
    \ defined mineral stock, not the wrongly linked 6187 or the main medium. KOH strength\
    \ and dose are not supplied.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"solutions[3].preparation_notes\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].preparation_notes\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Unquantified KOH stock titrant\",\n    \"field_path\": \"solutions[4].concentration\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local\": {\n      \"value\": \"\
    variable\",\n      \"unit\": \"VARIABLE\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"togoM2714\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2714\"\
    ,\n        \"source_locator\": \"$.comments[5].comment\",\n        \"exact_source_quote\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\":\
    \ \"99bc192311bdf1a723e2a18ac18df047942fd2bfaf3e7607863c96b4fe2b79dc\"\n     \
    \ }\n    ],\n    \"rationale\": \"No fixed KOH amount or stock strength is supplied.\
    \ Scope correction is separately required; do not invent a dose.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"variable\",\n          \"unit\"\
    : \"VARIABLE\"\n        },\n        \"decision\": \"not_quantified\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Main nominal volume discrepancy\",\n    \"field_path\"\
    : \"preparation_steps\",\n    \"decision\": \"conflict\",\n    \"local\": null,\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive716api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1003\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"attribute\\\": \\\"0.1% w/v in 0.1 N H2SO4\\\
    \",\\n                        \\\"amount\\\": 2,\\n                        \\\"\
    unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.00199402,\\n  \
    \                      \\\"mmol_l\\\": 0.00717234,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n    \
    \                    \\\"amount\\\": 0.2,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.000199402,\\n       \
    \                 \\\"mmol_l\\\": 0.00153861,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive716api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\
    \": 1852,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n  \
    \                      \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.000498504,\\n       \
    \                 \\\"mmol_l\\\": 0.00198473,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\
    \n      }\n    ],\n    \"rationale\": \"Listed liquid additions total 1003.7 mL,\
    \ whereas the provider declares 1003 mL; neither establishes a measured final\
    \ volume after separately prepared nitrate/carbonate/reductant additions.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"1000 +2\
    \ +0.2 +1 +0.5 =1003.7 mL; no final g/L denominator is selected.\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"DSMZ-only DTT preparation alternative\",\n \
    \   \"field_path\": \"preparation_steps\",\n    \"decision\": \"conflict\",\n\
    \    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz716\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium716.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 preparation paragraph1\",\n       \
    \ \"exact_source_quote\": \"from an anoxic stock solution sterilized by filtration\
    \ under 100% N2 gas and adjust the pH\\nof the medium to 7.2.\",\n        \"snapshot_sha256\"\
    : \"a25c391fab84a47a454da6c5ad9aa95eb2d973c519fbb1aae1fdccec6506f66c\",\n    \
    \    \"parsed_text_sha256\": \"b5d3edff32b291b3781935bd644110717bf51edd0753966a30c7ba435a712b6f\"\
    \n      },\n      {\n        \"source_key\": \"mediadive716api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/716\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"DL-Dithiothreitol\\\",\\n                        \\\"compound_id\\\
    \": 151,\\n                        \\\"amount\\\": 0.3,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.299103,\\\
    n                        \\\"mmol_l\\\": 1.93845,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e2a695aa3c998e8e55163f885368bc13e841ee8ebf3bb6116316775c205d300c\"\n      }\n\
    \    ],\n    \"rationale\": \"The DTT 0.3 g/100% N2 filter-sterilized addition\
    \ belongs to the captured DSMZ formulation; do not silently insert it into the\
    \ TOGO sulfide version.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n      \
    \  \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context-only6187: Na2-EDTA\",\n    \"field_path\": \"composition[0].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": {\n      \"value\": \"0.75\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 1,\\n                \\\"compound\\\
    \": \\\"Na2-EDTA\\\",\\n                \\\"compound_id\\\": 34,\\n          \
    \      \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.75,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.75,\\n                \\\"mmol_l\\\
    \": 2.23078,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"rationale\": \"Existing attached literal snippet, source\
    \ hash and provider g_l agree within solution6187 only. This does not validate\
    \ the receiver’s stock identity, measured final volume or chemical form.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.75\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context-only6187: Distilled water\",\n    \"field_path\": \"composition[1].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1000\"\
    ,\n      \"unit\": \"PERCENT_V_V\"\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 2,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 1000,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"rationale\": \"The water row has no attached amount evidence\
    \ and its PERCENT_V_V conversion is unsupported. Preserve the source’s actual\
    \ 1000 mL water addition without inferring a measured final volume or receiver\
    \ quantity.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000\",\n          \"unit\": \"PERCENT_V_V\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"\
    ingredient_or_context\": \"Context-only6187: FeCl3 x 6 H2O\",\n    \"field_path\"\
    : \"composition[2].concentration\",\n    \"decision\": \"verified\",\n    \"local\"\
    : {\n      \"value\": \"0.097\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"solution6187\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\",\n    \
    \    \"source_locator\": \"$.data.recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 4,\\n                \\\"compound\\\
    \": \\\"FeCl3 x 6 H2O\\\",\\n                \\\"compound_id\\\": 82,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 97,\\n                \\\"unit\\\":\
    \ \\\"mg\\\",\\n                \\\"g_l\\\": 0.097,\\n                \\\"mmol_l\\\
    \": 0.358866,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"rationale\": \"Existing attached literal snippet, source\
    \ hash and provider g_l agree within solution6187 only. This does not validate\
    \ the receiver’s stock identity, measured final volume or chemical form.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.097\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context-only6187: MnCl2 x 4 H2O\",\n    \"field_path\": \"composition[3].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": {\n      \"value\": \"0.041\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 5,\\n                \\\"compound\\\
    \": \\\"MnCl2 x 4 H2O\\\",\\n                \\\"compound_id\\\": 36,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 41,\\n                \\\"unit\\\":\
    \ \\\"mg\\\",\\n                \\\"g_l\\\": 0.041,\\n                \\\"mmol_l\\\
    \": 0.20717,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"rationale\": \"Existing attached literal snippet, source\
    \ hash and provider g_l agree within solution6187 only. This does not validate\
    \ the receiver’s stock identity, measured final volume or chemical form.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.041\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context-only6187: ZnCl2 x 6 H2O\",\n    \"field_path\": \"composition[4].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": {\n      \"value\": \"0.005\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 6,\\n                \\\"compound\\\
    \": \\\"ZnCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 2351,\\n   \
    \             \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 5,\\n                \\\"unit\\\": \\\
    \"mg\\\",\\n                \\\"g_l\\\": 0.005,\\n                \\\"mmol_l\\\
    \": 0.0204583,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"rationale\": \"Existing attached literal snippet, source\
    \ hash and provider g_l agree within solution6187 only. This does not validate\
    \ the receiver’s stock identity, measured final volume or chemical form.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context-only6187: CoCl2 x 6 H2O\",\n    \"field_path\": \"composition[5].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": {\n      \"value\": \"0.002\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 7,\\n                \\\"compound\\\
    \": \\\"CoCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 38,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 2,\\n                \\\"unit\\\": \\\
    \"mg\\\",\\n                \\\"g_l\\\": 0.002,\\n                \\\"mmol_l\\\
    \": 0.0154037,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"rationale\": \"Existing attached literal snippet, source\
    \ hash and provider g_l agree within solution6187 only. This does not validate\
    \ the receiver’s stock identity, measured final volume or chemical form.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context-only6187: Na2MoO4 x 2 H2O\",\n    \"field_path\": \"composition[6].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": {\n      \"value\": \"0.004\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 8,\\n                \\\"compound\\\
    \": \\\"Na2MoO4 x 2 H2O\\\",\\n                \\\"compound_id\\\": 9,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 4,\\n                \\\"unit\\\": \\\
    \"mg\\\",\\n                \\\"g_l\\\": 0.004,\\n                \\\"mmol_l\\\
    \": 0.0165323,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"rationale\": \"Existing attached literal snippet, source\
    \ hash and provider g_l agree within solution6187 only. This does not validate\
    \ the receiver’s stock identity, measured final volume or chemical form.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"6187 placeholder ingredient\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"variable\"\
    ,\n      \"unit\": \"VARIABLE\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.name\",\n        \"exact_source_quote\"\
    : \"\\\"name\\\": \\\"Trace element solution\\\"\",\n        \"snapshot_sha256\"\
    : \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\n     \
    \ }\n    ],\n    \"rationale\": \"The placeholder is not a source compound or\
    \ quantified addition; retain it as an existing context defect, not receiver evidence.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"6187 preparation water/EDTA quantities\",\n\
    \    \"field_path\": \"preparation_notes\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals\
    \ in exactly the \\r\\nfollowing sequence:\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"solution6187\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/solution/6187\",\n        \"source_locator\": \"\
    $.data.steps[0].step\",\n        \"exact_source_quote\": \"Add to 1000 ml of distilled\
    \ water 0.75 g Na2EDTA and the minerals\",\n        \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"rationale\": \"The preparation text agrees for this dependency;\
    \ concentration evidence is attached to composition rows rather than this preparation\
    \ claim. Do not convert the water addition into a measured final volume.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"preparation_notes\",\n        \"stored\": \"Add to\
    \ 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \\\
    r\\nfollowing sequence:\",\n        \"decision\": \"evidence_only\"\n      }\n\
    \    ]\n  }\n]"
findings:
- finding_id: f1
  issue_key: ammonifex-degensii-stock-unit-flattening
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Flattened stocks and wrong units change the medium formulation
  description: Main and mineral-stock quantities have been summed, collapsed or represented
    together without the 1 mL dilution. Water is labeled as mass, four liquid stock
    doses as g/L, and selenite/tungstate mg as g/L. The owner’s later water/NaCl collapse
    means the target is additionally stale, but copying that owner alone would preserve
    the main stock defect.
  target_ids:
  - CultureMech:009265
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - togo
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
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
  issue_key: ammonifex-degensii-wrong-trace-stock
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The trace-stock reference denotes a different formulation
  description: The asserted solution6187 is an EDTA/chloride stock, whereas M2714
    defines an NTA/sulfate stock corroborated by DSMZ716/stock241. Six valid attached
    quantity claims in 6187 do not establish identity equivalence or support this
    link.
  target_ids:
  - CultureMech:009265
  field_paths:
  - solutions[3].term
  - solutions[3].notes
  - solutions[3].composition
  evidence_ids:
  - record
  - owner-0
  - togo
  - primary
  - stock241
  - dependency6187
  - stock6187
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: ammonifex-degensii-source-preparation-conflict
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Missing preparation hides a material source disagreement
  description: Both medium layers omit the anaerobic sequence and pH. TOGO sulfide/2
    bar after inoculation conflicts with DSMZ DTT/0.5 bar after growth starts. The
    shared source accession does not justify silently substituting one procedure.
  target_ids:
  - CultureMech:009265
  field_paths:
  - preparation_steps
  - ph_value
  - ingredients[5]
  evidence_ids:
  - record
  - owner-0
  - togo
  - primary
  - provider
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3.5
  normalization_reason: P3.5 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: ammonifex-degensii-hydrate-correspondence
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Source hydrate specificity is not consistently represented
  description: Nickel hexahydrate is mapped to anhydrous 34887; magnesium heptahydrate’s
    correct primary 31795 has generic/anhydrous secondary 32599. Phosphate 131527
    has an anhydrous formula alongside a trihydrate synonym, leaving the source-form
    correspondence internally ambiguous. Do not use these terms to recalculate hydrate
    masses or molarity.
  target_ids:
  - CultureMech:009265
  field_paths:
  - ingredients[1].mediaingredientmech_chebi_term
  - ingredients[9].term
  - ingredients[9].mediaingredientmech_chebi_term
  - ingredients[15].term
  - ingredients[15].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - primary
  - chebi31795
  - chebi32599
  - chebi131527
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: ammonifex-degensii-composition-category
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Complex and undefined categories lack source support
  description: Both captured recipes provide named chemical formulations and the provider
    marks the medium noncomplex. The local COMPLEX/UNDEFINED assertions do not follow
    from the inspected source.
  target_ids:
  - CultureMech:009265
  field_paths:
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - togo
  - primary
  - provider
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: ammonifex-degensii-legacy-nitrate-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical nitrate linkage remains unresolved
  description: The asserted legacy MediaIngredientMech:000170 could not be resolved
    in the complete pinned public catalog/tree. This completed negative lookup does
    not invalidate the separately supported potassium-nitrate primary ID or establish
    a new equivalence.
  target_ids:
  - CultureMech:009265
  field_paths:
  - ingredients[8].mediaingredientmech_term
  evidence_ids:
  - record
  - legacy-search
  - mimPinnedCatalog
  - mimPinnedTree
  - chebi63043
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Reconcile the maintained owner against the selected source version,
    separate main batches and local mineral stock, restore literal mg/ml units and
    supported preparation. Preserve the existing repair history; regenerate after
    source-stage correction. Resolve the volume discrepancy before any final-medium
    normalization.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
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
  description: Resolve and represent the exact M2714 mineral stock, replacing or withdrawing
    the unsupported 6187 link through maintained-input curation. Keep 6187’s own evidence
    unchanged unless separately authorized for review.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
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
  description: Document the intended source representation and its exact preparation,
    preserving the alternative as an unresolved version conflict with no unsupported
    chronology. Keep gas fractions, pressure timing, sterilization methods and stock
    pH in their correct stages.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
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
  description: Reconcile exact supplied forms independently in each asserted slot,
    preserving original source masses and ambiguity where no supported replacement
    identifier is established.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
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
- action_id: a5
  description: Reassess classification against the reconciled exact source formulation
    and attach source support; do not derive classification from unresolved legacy
    stock placeholders.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
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
- action_id: a6
  description: Preserve the historical assertion and annotate its unresolved correspondence;
    use an exact supported migration only if independently established.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:009265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml
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
- No source revision chronology is established between TOGO M2714 and DSMZ716. A provisional
  context sentence calling the linked primary newer is not adopted in this assessment.
- The linked 6187 dependency was read in full for identity and evidence scope; its
  own broader curation verdict is outside this single-medium review. Its attached
  quantities do not transfer across the incorrect reference.
- All exact primary/provider comparisons and the required current pinned lookup completed.
  Required historical correspondence for the asserted legacy MediaIngredientMech:000170
  remains unavailable; this unresolved claim makes completion partial. The completed
  negative current lookup is not itself failed or unavailable.
- This scientific assessment preceded formal review validation and saving; their results
  are recorded separately.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-026
- generated-medium
```
