# Source and formulation review: anoyxnatronum_medium (CultureMech:003907)

- Review: 20261021T162101Z-culturemech-003907-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T16:17:53Z
- Finished UTC: 2026-10-21T16:21:01Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

ANOYXNATRONUM MEDIUM flattens SL10 and vitamin stock constituents into undiluted medium concentrations and loses their 1 mL doses. The primary supports source batch masses and anaerobic preparation but does not establish a measured final-medium denominator. Reconstruct the stock hierarchy, reconcile the maintained owners, correct nickel hydration and regenerate the target.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 286; batch 029 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-eight task batches contain 280 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 283 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003907 | data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml | generated | anoyxnatronum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003907 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003907 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch029/286/strict.tsv |
| validate-terms | passed | True | CultureMech:003907 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003907 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003907 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive1187api | unavailable | False | CultureMech:003907 | mediadive1187api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodo1187detail | unavailable | False | CultureMech:003907 | komodo1187detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodo1187actual | unavailable | False | CultureMech:003907 | komodo1187actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: mediadive1187retry | unavailable | False | CultureMech:003907 | mediadive1187retry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003907.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:003907.

27 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 27/28 primary and 26/28 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 28: primary 96.43%; secondary 92.86%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003907.

25 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Two maintained contributors and source accession

identity: supported. Targets: CultureMech:003907.

The target CultureMech:003907 derives from KOMODO1187 and DSMZ1187 CultureMech:000629. Their complete ingredients match; only the DSMZ owner retains preparation. Reciprocal SOURCE_DUPLICATE paths and IDs resolve exactly, but ingredient fingerprints and matching quantities do not establish complete formulation equivalence.

### Main batch and separately prepared stocks

consistency: concern. Targets: CultureMech:003907.

All three layers have nine direct quantities plus nine SL10 and ten vitamin entries as flat g/L. SL10 acid25%/10 mL becomes 2.5 g/L without a stated percentage basis. Other trace/vitamin values are stock-strength numbers, not delivered amounts. The main nine g/L values equal the listed batch masses numerically, but 1000 mL water and later additions do not independently establish final volume.

### Anaerobic main sequence and SL10 make-up

completeness: concern. Targets: CultureMech:003907.

The DSMZ owner retains pH9.0 and the main anaerobic/autoclave/late sterile-addition sequence; it misplaces the SL10 make-up procedure among main steps. The target and KOMODO owner omit preparation. N2 has no percentage and late sterile-stock strengths are not quantified. Source-specific instructions can be restored without inventing a generic autoclave temperature or duration. The primary omits glucose from the initial exclusion list but later adds it from a sterile stock; preserve that internal sequence ambiguity and resolve it without double dosing.

### Hydrate and stereochemical scope

grounding: concern. Targets: CultureMech:003907.

SL10 explicitly uses nickel chloride hexahydrate, while both local CHEBI slots assert anhydrous CHEBI:34887. Other captured forms were compared to the source. Calcium D-(+)-pantothenate is consistent with the stereochemical calcium-salt term; nonstereospecific lipoic acid does not encode the printed racemate but is not evidence of a contrary enantiomer. Generic B12 is not narrowed.

### Classification and biological scope

scope: supported. Targets: CultureMech:003907.

COMPLEX with SEMI_DEFINED composition is compatible with defined salts and yeast extract; LIQUID matches the formulation. Bacterial filing and generic cultivation application are source/catalog scope, not strain growth evidence. No named organism, DOI, PMID, genome or optimum is asserted. The Aerobic: Yes note requires catalog attribution alongside the explicitly anaerobic source procedure.

### Current import and merge behavior

provenance: concern. Targets: CultureMech:003907.

The current MediaDive importer separates primary stock additions and direct compounds, while preparation parsing collects steps from all solutions. Current formulation merging requires scientific-field compatibility; a fingerprint cannot excuse lost preparation. These are current implementation facts, not proof of the exact historical code path. Correct each maintained source representation before regeneration.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003907.

37 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "Na2CO3 25.0 g",
    "field_path": "ingredients[0].concentration",
    "decision": "unsupported",
    "local": {
      "value": "25",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "PDF main table; named row",
        "exact_source_quote": "Na2CO3 25.0 g",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "The primary supports this source batch mass. Stored g/L uses a nominal 1 L basis that is not independently established as final volume; preserve the source mass and unresolved denominator without silently endorsing final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "NaHCO3 25.0 g",
    "field_path": "ingredients[1].concentration",
    "decision": "unsupported",
    "local": {
      "value": "25",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "PDF main table; named row",
        "exact_source_quote": "NaHCO3 25.0 g",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "The primary supports this source batch mass. Stored g/L uses a nominal 1 L basis that is not independently established as final volume; preserve the source mass and unresolved denominator without silently endorsing final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "KCl 0.2 g",
    "field_path": "ingredients[2].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "PDF main table; named row",
        "exact_source_quote": "KCl 0.2 g",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "The primary supports this source batch mass. Stored g/L uses a nominal 1 L basis that is not independently established as final volume; preserve the source mass and unresolved denominator without silently endorsing final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "MgCl2 x 6 H20 0.1 g",
    "field_path": "ingredients[3].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "PDF main table; named row",
        "exact_source_quote": "MgCl2 x 6 H20 0.1 g",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "The primary supports this source batch mass. Stored g/L uses a nominal 1 L basis that is not independently established as final volume; preserve the source mass and unresolved denominator without silently endorsing final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "NH4Cl 0.5 g",
    "field_path": "ingredients[4].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "PDF main table; named row",
        "exact_source_quote": "NH4Cl 0.5 g",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "The primary supports this source batch mass. Stored g/L uses a nominal 1 L basis that is not independently established as final volume; preserve the source mass and unresolved denominator without silently endorsing final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "K2HPO4 0.2 g",
    "field_path": "ingredients[5].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "PDF main table; named row",
        "exact_source_quote": "K2HPO4 0.2 g",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "The primary supports this source batch mass. Stored g/L uses a nominal 1 L basis that is not independently established as final volume; preserve the source mass and unresolved denominator without silently endorsing final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "Yeast extract 0.2 g",
    "field_path": "ingredients[6].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "PDF main table; named row",
        "exact_source_quote": "Yeast extract 0.2 g",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "The primary supports this source batch mass. Stored g/L uses a nominal 1 L basis that is not independently established as final volume; preserve the source mass and unresolved denominator without silently endorsing final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "Na2S x 9 H2O 0.7 g",
    "field_path": "ingredients[7].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.7",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "PDF main table; named row",
        "exact_source_quote": "Na2S x 9 H2O 0.7 g",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "The primary supports this source batch mass. Stored g/L uses a nominal 1 L basis that is not independently established as final volume; preserve the source mass and unresolved denominator without silently endorsing final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.7",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.7",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.7",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "Glucose 5.0 g",
    "field_path": "ingredients[8].concentration",
    "decision": "unsupported",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "PDF main table; named row",
        "exact_source_quote": "Glucose 5.0 g",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "The primary supports this source batch mass. Stored g/L uses a nominal 1 L basis that is not independently established as final volume; preserve the source mass and unresolved denominator without silently endorsing final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "SL10: HCl (25%) 10.00 ml",
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "local": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "PDF pages1–2 SL10 stock table; named row",
        "exact_source_quote": "HCl (25%) 10.00 ml",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The source states 10 mL of 25% HCl for the SL10 stock. Percentage basis and density are unknown; neither 2.5 g nor 2.5 g/L is established."
  },
  {
    "ingredient_or_context": "SL10: FeCl2 x 4 H2O 1.50 g",
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "local": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "PDF pages1–2 SL10 stock table; named row",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the explicit SL10 make-up to 1 L, stock 1.5 g/L × 0.001 L aliquot = 0.0015 g delivered per source batch; no final-medium g/L follows."
  },
  {
    "ingredient_or_context": "SL10: ZnCl2 70.00 mg",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "local": {
      "value": "0.07",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "PDF pages1–2 SL10 stock table; named row",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the explicit SL10 make-up to 1 L, stock 0.07 g/L × 0.001 L aliquot = 0.00007 g delivered per source batch; no final-medium g/L follows."
  },
  {
    "ingredient_or_context": "SL10: MnCl2 x 4 H2O 100.00 mg",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "PDF pages1–2 SL10 stock table; named row",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the explicit SL10 make-up to 1 L, stock 0.1 g/L × 0.001 L aliquot = 0.0001 g delivered per source batch; no final-medium g/L follows."
  },
  {
    "ingredient_or_context": "SL10: H3BO3 6.00 mg",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "local": {
      "value": "0.006",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "PDF pages1–2 SL10 stock table; named row",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the explicit SL10 make-up to 1 L, stock 0.006 g/L × 0.001 L aliquot = 0.000006 g delivered per source batch; no final-medium g/L follows."
  },
  {
    "ingredient_or_context": "SL10: CoCl2 x 6 H2O 190.00 mg",
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "local": {
      "value": "0.19",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "PDF pages1–2 SL10 stock table; named row",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the explicit SL10 make-up to 1 L, stock 0.19 g/L × 0.001 L aliquot = 0.00019 g delivered per source batch; no final-medium g/L follows."
  },
  {
    "ingredient_or_context": "SL10: CuCl2 x 2 H2O 2.00 mg",
    "field_path": "ingredients[15].concentration",
    "decision": "correct",
    "local": {
      "value": "0.002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "PDF pages1–2 SL10 stock table; named row",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the explicit SL10 make-up to 1 L, stock 0.002 g/L × 0.001 L aliquot = 0.000002 g delivered per source batch; no final-medium g/L follows."
  },
  {
    "ingredient_or_context": "SL10: NiCl2 x 6 H2O 24.00 mg",
    "field_path": "ingredients[16].concentration",
    "decision": "correct",
    "local": {
      "value": "0.024",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "PDF pages1–2 SL10 stock table; named row",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the explicit SL10 make-up to 1 L, stock 0.024 g/L × 0.001 L aliquot = 0.000024 g delivered per source batch; no final-medium g/L follows."
  },
  {
    "ingredient_or_context": "SL10: Na2MoO4 x 2 H2O 36.00 mg",
    "field_path": "ingredients[17].concentration",
    "decision": "correct",
    "local": {
      "value": "0.036",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "PDF pages1–2 SL10 stock table; named row",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the explicit SL10 make-up to 1 L, stock 0.036 g/L × 0.001 L aliquot = 0.000036 g delivered per source batch; no final-medium g/L follows."
  },
  {
    "ingredient_or_context": "Vitamin stock: Biotin 2.00 mg",
    "field_path": "ingredients[18].concentration",
    "decision": "correct",
    "local": {
      "value": "0.002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "PDF pages2–3 Wolin vitamin stock table; named row",
        "exact_source_quote": "Biotin 2.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The source gives the vitamin mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.002 g/L × 0.001 L would deliver 0.000002 g; measured stock/final-medium volume is not asserted."
  },
  {
    "ingredient_or_context": "Vitamin stock: Folic acid 2.00 mg",
    "field_path": "ingredients[19].concentration",
    "decision": "correct",
    "local": {
      "value": "0.002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "PDF pages2–3 Wolin vitamin stock table; named row",
        "exact_source_quote": "Folic acid 2.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The source gives the vitamin mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.002 g/L × 0.001 L would deliver 0.000002 g; measured stock/final-medium volume is not asserted."
  },
  {
    "ingredient_or_context": "Vitamin stock: Pyridoxine hydrochloride 10.00 mg",
    "field_path": "ingredients[20].concentration",
    "decision": "correct",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "PDF pages2–3 Wolin vitamin stock table; named row",
        "exact_source_quote": "Pyridoxine hydrochloride 10.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The source gives the vitamin mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.01 g/L × 0.001 L would deliver 0.00001 g; measured stock/final-medium volume is not asserted."
  },
  {
    "ingredient_or_context": "Vitamin stock: Thiamine HCl 5.00 mg",
    "field_path": "ingredients[21].concentration",
    "decision": "correct",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "PDF pages2–3 Wolin vitamin stock table; named row",
        "exact_source_quote": "Thiamine HCl 5.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The source gives the vitamin mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.005 g/L × 0.001 L would deliver 0.000005 g; measured stock/final-medium volume is not asserted."
  },
  {
    "ingredient_or_context": "Vitamin stock: Riboflavin 5.00 mg",
    "field_path": "ingredients[22].concentration",
    "decision": "correct",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "PDF pages2–3 Wolin vitamin stock table; named row",
        "exact_source_quote": "Riboflavin 5.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The source gives the vitamin mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.005 g/L × 0.001 L would deliver 0.000005 g; measured stock/final-medium volume is not asserted."
  },
  {
    "ingredient_or_context": "Vitamin stock: Nicotinic acid 5.00 mg",
    "field_path": "ingredients[23].concentration",
    "decision": "correct",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "PDF pages2–3 Wolin vitamin stock table; named row",
        "exact_source_quote": "Nicotinic acid 5.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The source gives the vitamin mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.005 g/L × 0.001 L would deliver 0.000005 g; measured stock/final-medium volume is not asserted."
  },
  {
    "ingredient_or_context": "Vitamin stock: Calcium D-(+)-pantothenate 5.00 mg",
    "field_path": "ingredients[24].concentration",
    "decision": "correct",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "PDF pages2–3 Wolin vitamin stock table; named row",
        "exact_source_quote": "Calcium D-(+)-pantothenate 5.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The source gives the vitamin mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.005 g/L × 0.001 L would deliver 0.000005 g; measured stock/final-medium volume is not asserted."
  },
  {
    "ingredient_or_context": "Vitamin stock: Vitamin B12 0.10 mg",
    "field_path": "ingredients[25].concentration",
    "decision": "correct",
    "local": {
      "value": "0.0001",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "PDF pages2–3 Wolin vitamin stock table; named row",
        "exact_source_quote": "Vitamin B12 0.10 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The source gives the vitamin mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.0001 g/L × 0.001 L would deliver 1E-7 g; measured stock/final-medium volume is not asserted."
  },
  {
    "ingredient_or_context": "Vitamin stock: p-Aminobenzoic acid 5.00 mg",
    "field_path": "ingredients[26].concentration",
    "decision": "correct",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "PDF pages2–3 Wolin vitamin stock table; named row",
        "exact_source_quote": "p-Aminobenzoic acid 5.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The source gives the vitamin mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.005 g/L × 0.001 L would deliver 0.000005 g; measured stock/final-medium volume is not asserted."
  },
  {
    "ingredient_or_context": "Vitamin stock: (DL)-alpha-Lipoic acid 5.00 mg",
    "field_path": "ingredients[27].concentration",
    "decision": "correct",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "PDF pages2–3 Wolin vitamin stock table; named row",
        "exact_source_quote": "(DL)-alpha-Lipoic acid 5.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Restore the original stock recipe and unit, with its separate 1 mL main-medium dose. The current field improperly states an undiluted direct-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The source gives the vitamin mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.005 g/L × 0.001 L would deliver 0.000005 g; measured stock/final-medium volume is not asserted."
  },
  {
    "ingredient_or_context": "SL10 aliquot",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "main table",
        "exact_source_quote": "Trace elements SL-10 (see medium 320) 1.0 ml",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "Represent this source-only quantity in its named stage, preserving volume units. An existing preparation container is not an assertion of this water or stock dose.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Vitamin aliquot",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "main table",
        "exact_source_quote": "Vitamin solution (see medium 141) 1.0 ml",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "Represent this source-only quantity in its named stage, preserving volume units. An existing preparation container is not an assertion of this water or stock dose.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main water",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "main table",
        "exact_source_quote": "Distilled water 1000.0 ml",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "Represent this source-only quantity in its named stage, preserving volume units. An existing preparation container is not an assertion of this water or stock dose.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "pH 9.0"
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Prepare the medium anaerobically without the vitamins, Na2S, yeast extract NaHCO3, and Na2CO3. Boil the medium, cool under N2, add the NaHCO3, and Na2CO3, dispense under N2 and autoclave the medium. Add the vitamin solution, yeast extract, Na2S and glucose from sterile stock solution prepared under N2 to the cooled, autoclaved medium."
          },
          {
            "step_number": 3,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "SL10 water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "SL10 table",
        "exact_source_quote": "Distilled water 990.00 ml",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6"
      }
    ],
    "rationale": "Represent this source-only quantity in its named stage, preserving volume units. An existing preparation container is not an assertion of this water or stock dose.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Vitamin water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Wolin vitamin table, page3",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Represent this source-only quantity in its named stage, preserving volume units. An existing preparation container is not an assertion of this water or stock dose.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main scalar pH",
    "field_path": "ph_value",
    "decision": "evidence_only",
    "local": 9.0,
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "main pH line",
        "exact_source_quote": "pH 9.0",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "The correct scalar is retained in all three layers without attached exact claim evidence.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 9.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "ph_value",
        "stored": 9.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "ph_value",
        "stored": 9.0,
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Main preparation pH",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "main pH line",
        "exact_source_quote": "pH 9.0",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "Retain the literal endpoint with evidence in its correct stage. The DSMZ stock make-up instruction belongs to SL10 rather than the main medium.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "pH 9.0",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "SL10 final make-up",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz320",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf",
        "source_locator": "SL10 make-up, page2",
        "exact_source_quote": "make up to 1000.00 ml.",
        "snapshot_sha256": "d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9",
        "parsed_text_sha256": "d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6"
      }
    ],
    "rationale": "Retain the literal endpoint with evidence in its correct stage. The DSMZ stock make-up instruction belongs to SL10 rather than the main medium.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Unquantified later-stock strengths and N2 fraction",
    "field_path": "preparation_steps",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1187",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf",
        "source_locator": "final main preparation sentence",
        "exact_source_quote": "glucose from sterile stock solution prepared under N2 to the cooled, autoclaved medium.",
        "snapshot_sha256": "b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c",
        "parsed_text_sha256": "05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949"
      }
    ],
    "rationale": "The primary names sterile late stocks and N2 but gives no strengths, extra aliquot volumes or nitrogen percentage; no values may be invented.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "pH 9.0"
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Prepare the medium anaerobically without the vitamins, Na2S, yeast extract NaHCO3, and Na2CO3. Boil the medium, cool under N2, add the NaHCO3, and Na2CO3, dispense under N2 and autoclave the medium. Add the vitamin solution, yeast extract, Na2S and glucose from sterile stock solution prepared under N2 to the cooled, autoclaved medium."
          },
          {
            "step_number": 3,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "not_quantified"
      }
    ]
  }
]

## Findings

### f1: Stock constituents replace the intended dilute additions

blocker / open / confirmed; issue key: anoyxnatronum-stock-flattening.

Nine SL10 and ten vitamin constituents are direct g/L in all three local layers, while both 1 mL stock doses are absent. The acid volume/percentage is additionally converted to unsupported mass. This changes the denoted formulation; the nine main g/L values retain an unresolved final-volume basis.

### f2: Source nickel hexahydrate is grounded to anhydrous salt

major / open / confirmed; issue key: anoyxnatronum-nickel-form.

SL10 uses NiCl2 x 6 H2O, 24 mg per stock preparation. CHEBI:34887 in both primary and secondary fields denotes Cl2Ni without six waters.

### f3: Anaerobic preparation is lost and stock make-up is misplaced

major / open / confirmed; issue key: anoyxnatronum-preparation-scope.

The target and KOMODO owner omit the main anaerobic/autoclave/late-addition procedure. The DSMZ owner retains it but presents the SL10 make-up to1000 mL as a main preparation step. Source-specific stage recovery is required; this is a representation defect, not evidence for an unprinted sterilization cycle.

### f4: Aerobic catalog metadata and historical timestamps need qualification

minor / open / confirmed; issue key: anoyxnatronum-catalog-history.

The target and KOMODO owner retain Aerobic: Yes while the primary prescribes anaerobic preparation. They also retain malformed .fZ and timezone-naive history values. These are metadata limits, not grounds to invent physiology or corrected dates.

## Recommended Actions And Acceptance Checks

### a1

Rebuild SL10 and the vitamin stock in the maintained owners with exact source units and separate 1 mL doses; preserve direct batch masses and unknown final denominator, then regenerate only compatible source records.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify a source-matching hydrate identifier for both asserted slots and retain the original stock mass and dose. Do not invent a replacement or convert to anhydrous mass.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the DSMZ main sequence with claim evidence, move the trace preparation under SL10 and reconcile the other owner before regeneration; keep N2 unquantified.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attribute the catalog flag and append bounded provenance clarifications during authorized curation; preserve historical events and avoid guessing missing timestamp content.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch029/286/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch029/286/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml:1:id: CultureMech:003907<br>./data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml:1:id: CultureMech:003907<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch029/source-preflight-bound/286/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 35 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch029/source-preflight-bound/286/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| dsmz1187 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf; Entire DSMZ1187 PDF; main table and preparation | supports | The complete primary and page image were read. Nine direct masses, two 1 mL stock additions, 1000 mL water and pH9.0 are distinct quantities; N2 is unquantified and no autoclave cycle is printed. |
| dsmz320 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf; PDF pages1–2, Trace element solution SL-10 only | supports | Only the nine-component SL10 stock and its make-up instruction transfer. Basal medium, sludge, rumen and organism-specific instructions are excluded. |
| dsmz141 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf; PDF pages2–3, Wolin vitamin solution only | supports | Only ten vitamin masses and 1000 mL stock water transfer; parent basal/mineral ingredients and gas/strain instructions are excluded. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact raw table header and accession1187 row | context_only | The row links DSMZ1187 and preserves pH9.0 and Is Aerobic=true as catalog metadata, not experimental growth or a cultivation instruction. |
| mediadive1187api-attempt | https://mediadive.dsmz.de/rest/medium/1187; Preserved exact public retrieval result | context_only | mediadive1187api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodo1187detail-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaInfo=1187; Preserved exact public retrieval result | context_only | komodo1187detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodo1187actual-attempt | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1187; Preserved exact public retrieval result | context_only | komodo1187actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| mediadive1187retry-attempt | https://mediadive.dsmz.de/rest/medium/1187; Preserved exact public retrieval result | context_only | mediadive1187retry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml; data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:58.346117"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:58.346117"}]}, {"input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml", "events": 7, "timestamp_issues": []}] |
| quantity-inventory | /private/tmp/culturemech-review-work-batch029/286/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch029/286/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- mediadive1187api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodo1187detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodo1187actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- mediadive1187retry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- Both exact main MediaDive attempts returned503. They are optional corroboration here: no existing attached historical amount claim is independently authenticated or asserted. Available collection primaries support the bounded assessment; final-volume uncertainty is explicitly assessed rather than hidden.
- Only named SL10 and vitamin subsections transfer from the parent PDFs; parent organisms, basal recipes and gas conditions are excluded.
- This scientific assessment preceded formal review validation and saving; their results are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T162101Z-culturemech-003907-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anoyxnatronum_medium (CultureMech:003907)'
started_at: '2026-10-21T16:17:53Z'
finished_at: '2026-10-21T16:21:01Z'
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
summary: ANOYXNATRONUM MEDIUM flattens SL10 and vitamin stock constituents into undiluted
  medium concentrations and loses their 1 mL doses. The primary supports source batch
  masses and anaerobic preparation but does not establish a measured final-medium
  denominator. Reconstruct the stock hierarchy, reconcile the maintained owners, correct
  nickel hydration and regenerate the target.
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
  - path: data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml
    sha256: 47259e5b09d7c5cc96dc2e706d9ddd00ee44928488f240883b4df360a80017d4
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml
    sha256: 6e302a78e204bedb52d43604d3d7599939b73a4b0b3acd8bd51298a69efe9f03
    role: context
  - path: data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml
    sha256: e268484d398e45b8092fd471af73e57971fce25aedd94e680926670b8359536b
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/anoyxnatronum_medium.yaml.md
    sha256: 5de70e63e33ca1b8fb1b9f1f9b5ed1f0311fd0ef5a1691ac8ae1eaa15c2ebcd1
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml.md
    sha256: 7940083fab4d647bec4bf8f1ee3b64c944359616e0bd950a4feea732c0c88303
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
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
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
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
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
  selection: Task review 286; batch 029 item 6 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-eight task batches
    contain 280 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 283 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003907
targets:
- target_id: CultureMech:003907
  path: data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml
  label: anoyxnatronum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch029/286/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch029/286/strict.tsv"
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003907
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
  - CultureMech:003907
- check_id: mediadive1187api-source-access
  name: 'Exact source content access: mediadive1187api'
  required: false
  status: unavailable
  summary: 'mediadive1187api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - mediadive1187api-attempt
- check_id: komodo1187detail-source-access
  name: 'Exact source content access: komodo1187detail'
  required: false
  status: unavailable
  summary: 'komodo1187detail: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - komodo1187detail-attempt
- check_id: komodo1187actual-source-access
  name: 'Exact source content access: komodo1187actual'
  required: false
  status: unavailable
  summary: 'komodo1187actual: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - komodo1187actual-attempt
- check_id: mediadive1187retry-source-access
  name: 'Exact source content access: mediadive1187retry'
  required: false
  status: unavailable
  summary: 'mediadive1187retry: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - mediadive1187retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T16:21:00Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:21:00Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:21:00Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:25.156693Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch029/286/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:26.404560Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch029/286/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:27.927182Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:28.859070Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T16:21:00Z'
  support: supports
  summary: './data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml:1:id: CultureMech:003907

    ./data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml:1:id: CultureMech:003907

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/source-preflight-bound/286/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T16:21:00Z'
  support: supports
  summary: 35 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 95724181535b0e6c3696b981a66590017f3bca4d24c5519dc61d24d81cde5cff
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/source-preflight-bound/286/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T16:21:00Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: d244b262fc82da438c0134f0df671bbef4c043a606848fb7d72000d9ba7b501b
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T16:21:00Z'
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
  accessed_at: '2026-10-21T16:21:00Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T16:21:00Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: dsmz1187
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf
  locator: Entire DSMZ1187 PDF; main table and preparation
  accessed_at: '2026-10-21T16:01:40.489490Z'
  support: supports
  summary: The complete primary and page image were read. Nine direct masses, two
    1 mL stock additions, 1000 mL water and pH9.0 are distinct quantities; N2 is unquantified
    and no autoclave cycle is printed.
  snapshot_sha256: b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c
- evidence_id: dsmz320
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf
  locator: PDF pages1–2, Trace element solution SL-10 only
  accessed_at: '2026-10-21T13:20:08.151265Z'
  support: supports
  summary: Only the nine-component SL10 stock and its make-up instruction transfer.
    Basal medium, sludge, rumen and organism-specific instructions are excluded.
  snapshot_sha256: d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9
- evidence_id: dsmz141
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf
  locator: PDF pages2–3, Wolin vitamin solution only
  accessed_at: '2026-10-21T10:13:12.306566Z'
  support: supports
  summary: Only ten vitamin masses and 1000 mL stock water transfer; parent basal/mineral
    ingredients and gas/strain instructions are excluded.
  snapshot_sha256: 8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact raw table header and accession1187 row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: context_only
  summary: The row links DSMZ1187 and preserves pH9.0 and Is Aerobic=true as catalog
    metadata, not experimental growth or a cultivation instruction.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1187'\
    \ >1187</a></TD>\n\t\t\t\t\t<TD>ANOYXNATRONUM medium</TD>\n\t\t\t\t\t<TD> 9.0</TD>\n\
    \t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n<TD><a\
    \ href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: mediadive1187api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1187
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:01:39.342518Z'
  support: context_only
  summary: 'mediadive1187api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo1187detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaInfo=1187
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:01:39.342148Z'
  support: context_only
  summary: 'komodo1187detail: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: b2fcfcf52457b76b523e4a3e2734249a36459209ac2dcf577618fc0f9117a30f
- evidence_id: komodo1187actual-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1187
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:01:39.341874Z'
  support: context_only
  summary: 'komodo1187actual: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 924f7735d109c256f751c0f84ea892533c1ca143072c2911621832b4ae28c2ff
- evidence_id: mediadive1187retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1187
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:03:01.044955Z'
  support: context_only
  summary: 'mediadive1187retry: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
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
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: CHEBI:15940 resolves to nicotinic acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: CHEBI:15956 resolves to biotin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
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
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17883
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:37:25.439020Z'
  support: supports
  summary: CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: CHEBI:27470 resolves to folic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
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
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
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
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
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
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to zinc dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
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
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
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
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T16:21:00Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid",
    "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier":
    "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic
    acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term":
    "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type":
    "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier":
    "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier":
    "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid",
    "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier":
    "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type":
    "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate
    solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961":
    [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier":
    "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label":
    "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term":
    "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label":
    "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term",
    "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id":
    "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976":
    [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976",
    "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate",
    "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249":
    [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249",
    "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term":
    "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml;
    data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T16:21:00Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:58.346117"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:58.346117"}]}, {"input": "data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/286/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T16:21:00Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 5016a4247311229189bd0a47729a267d9e2224513ac2b4ca48199eb66ec53db7
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/286/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T16:21:00Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: 5421ff724e7466dc135f6487b9bd1b4a3aee58499a50e0c9d782797f2e9d0a9d
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '27 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 27/28
    primary and 26/28 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131527
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi17234
  - chebi176843
  - chebi17883
  - chebi27470
  - chebi29377
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi32139
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi49105
  - chebi49976
  - chebi53503
  - chebi75213
  - chebi76209
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  details: 'Instance coverage on a 0–100 percent scale, denominator 28: primary 96.43%;
    secondary 92.86%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 25 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: identity
  area: identity
  topic: Two maintained contributors and source accession
  outcome: supported
  summary: The target CultureMech:003907 derives from KOMODO1187 and DSMZ1187 CultureMech:000629.
    Their complete ingredients match; only the DSMZ owner retains preparation. Reciprocal
    SOURCE_DUPLICATE paths and IDs resolve exactly, but ingredient fingerprints and
    matching quantities do not establish complete formulation equivalence.
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - id-search
  - catalog
  - dsmz1187
- assessment_id: source-stages
  area: consistency
  topic: Main batch and separately prepared stocks
  outcome: concern
  summary: All three layers have nine direct quantities plus nine SL10 and ten vitamin
    entries as flat g/L. SL10 acid25%/10 mL becomes 2.5 g/L without a stated percentage
    basis. Other trace/vitamin values are stock-strength numbers, not delivered amounts.
    The main nine g/L values equal the listed batch masses numerically, but 1000 mL
    water and later additions do not independently establish final volume.
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - record
  - dsmz1187
  - dsmz320
  - dsmz141
- assessment_id: preparation
  area: completeness
  topic: Anaerobic main sequence and SL10 make-up
  outcome: concern
  summary: The DSMZ owner retains pH9.0 and the main anaerobic/autoclave/late sterile-addition
    sequence; it misplaces the SL10 make-up procedure among main steps. The target
    and KOMODO owner omit preparation. N2 has no percentage and late sterile-stock
    strengths are not quantified. Source-specific instructions can be restored without
    inventing a generic autoclave temperature or duration. The primary omits glucose
    from the initial exclusion list but later adds it from a sterile stock; preserve
    that internal sequence ambiguity and resolve it without double dosing.
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1187
  - dsmz320
- assessment_id: forms
  area: grounding
  topic: Hydrate and stereochemical scope
  outcome: concern
  summary: SL10 explicitly uses nickel chloride hexahydrate, while both local CHEBI
    slots assert anhydrous CHEBI:34887. Other captured forms were compared to the
    source. Calcium D-(+)-pantothenate is consistent with the stereochemical calcium-salt
    term; nonstereospecific lipoic acid does not encode the printed racemate but is
    not evidence of a contrary enantiomer. Generic B12 is not narrowed.
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - record
  - dsmz320
  - dsmz141
  - chebi34887
  - chebi31345
  - chebi16494
  - chebi176843
- assessment_id: classification
  area: scope
  topic: Classification and biological scope
  outcome: supported
  summary: 'COMPLEX with SEMI_DEFINED composition is compatible with defined salts
    and yeast extract; LIQUID matches the formulation. Bacterial filing and generic
    cultivation application are source/catalog scope, not strain growth evidence.
    No named organism, DOI, PMID, genome or optimum is asserted. The Aerobic: Yes
    note requires catalog attribution alongside the explicitly anaerobic source procedure.'
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - record
  - catalog
  - dsmz1187
- assessment_id: writers
  area: provenance
  topic: Current import and merge behavior
  outcome: concern
  summary: The current MediaDive importer separates primary stock additions and direct
    compounds, while preparation parsing collects steps from all solutions. Current
    formulation merging requires scientific-field compatibility; a fingerprint cannot
    excuse lost preparation. These are current implementation facts, not proof of
    the exact historical code path. Correct each maintained source representation
    before regeneration.
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - record
  - writer-context-0
  - writer-context-1
  - writer-context-2
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 37 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003907
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"Na2CO3 25.0 g\",\n    \"field_path\"\
    : \"ingredients[0].concentration\",\n    \"decision\": \"unsupported\",\n    \"\
    local\": {\n      \"value\": \"25\",\n      \"unit\": \"G_PER_L\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1187\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"PDF main table; named row\",\n        \"exact_source_quote\"\
    : \"Na2CO3 25.0 g\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this source batch\
    \ mass. Stored g/L uses a nominal 1 L basis that is not independently established\
    \ as final volume; preserve the source mass and unresolved denominator without\
    \ silently endorsing final concentration.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[0].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"25\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\":\
    \ \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    NaHCO3 25.0 g\",\n    \"field_path\": \"ingredients[1].concentration\",\n    \"\
    decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"25\",\n   \
    \   \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz1187\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"PDF main table; named row\",\n        \"exact_source_quote\"\
    : \"NaHCO3 25.0 g\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this source batch\
    \ mass. Stored g/L uses a nominal 1 L basis that is not independently established\
    \ as final volume; preserve the source mass and unresolved denominator without\
    \ silently endorsing final concentration.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[1].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"25\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\":\
    \ \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    KCl 0.2 g\",\n    \"field_path\": \"ingredients[2].concentration\",\n    \"decision\"\
    : \"unsupported\",\n    \"local\": {\n      \"value\": \"0.2\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1187\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"PDF main table; named row\",\n        \"exact_source_quote\"\
    : \"KCl 0.2 g\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this source batch\
    \ mass. Stored g/L uses a nominal 1 L basis that is not independently established\
    \ as final volume; preserve the source mass and unresolved denominator without\
    \ silently endorsing final concentration.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[2].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    MgCl2 x 6 H20 0.1 g\",\n    \"field_path\": \"ingredients[3].concentration\",\n\
    \    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.1\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1187\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"PDF main table; named row\",\n        \"exact_source_quote\"\
    : \"MgCl2 x 6 H20 0.1 g\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this source batch\
    \ mass. Stored g/L uses a nominal 1 L basis that is not independently established\
    \ as final volume; preserve the source mass and unresolved denominator without\
    \ silently endorsing final concentration.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[3].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    NH4Cl 0.5 g\",\n    \"field_path\": \"ingredients[4].concentration\",\n    \"\
    decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.5\",\n  \
    \    \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz1187\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"PDF main table; named row\",\n        \"exact_source_quote\"\
    : \"NH4Cl 0.5 g\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this source batch\
    \ mass. Stored g/L uses a nominal 1 L basis that is not independently established\
    \ as final volume; preserve the source mass and unresolved denominator without\
    \ silently endorsing final concentration.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[4].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    K2HPO4 0.2 g\",\n    \"field_path\": \"ingredients[5].concentration\",\n    \"\
    decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.2\",\n  \
    \    \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz1187\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"PDF main table; named row\",\n        \"exact_source_quote\"\
    : \"K2HPO4 0.2 g\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this source batch\
    \ mass. Stored g/L uses a nominal 1 L basis that is not independently established\
    \ as final volume; preserve the source mass and unresolved denominator without\
    \ silently endorsing final concentration.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[5].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    Yeast extract 0.2 g\",\n    \"field_path\": \"ingredients[6].concentration\",\n\
    \    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.2\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1187\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"PDF main table; named row\",\n        \"exact_source_quote\"\
    : \"Yeast extract 0.2 g\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this source batch\
    \ mass. Stored g/L uses a nominal 1 L basis that is not independently established\
    \ as final volume; preserve the source mass and unresolved denominator without\
    \ silently endorsing final concentration.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[6].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    Na2S x 9 H2O 0.7 g\",\n    \"field_path\": \"ingredients[7].concentration\",\n\
    \    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.7\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1187\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"PDF main table; named row\",\n        \"exact_source_quote\"\
    : \"Na2S x 9 H2O 0.7 g\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this source batch\
    \ mass. Stored g/L uses a nominal 1 L basis that is not independently established\
    \ as final volume; preserve the source mass and unresolved denominator without\
    \ silently endorsing final concentration.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[7].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"0.7\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.7\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.7\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    Glucose 5.0 g\",\n    \"field_path\": \"ingredients[8].concentration\",\n    \"\
    decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"5\",\n    \
    \  \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz1187\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"PDF main table; named row\",\n        \"exact_source_quote\"\
    : \"Glucose 5.0 g\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this source batch\
    \ mass. Stored g/L uses a nominal 1 L basis that is not independently established\
    \ as final volume; preserve the source mass and unresolved denominator without\
    \ silently endorsing final concentration.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[8].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[8].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"SL10:\
    \ HCl (25%) 10.00 ml\",\n    \"field_path\": \"ingredients[9].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"2.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz320\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\"\
    ,\n        \"source_locator\": \"PDF pages1–2 SL10 stock table; named row\",\n\
    \        \"exact_source_quote\": \"HCl (25%) 10.00 ml\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[9].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2.5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The\
    \ source states 10 mL of 25% HCl for the SL10 stock. Percentage basis and density\
    \ are unknown; neither 2.5 g nor 2.5 g/L is established.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"SL10: FeCl2 x 4 H2O 1.50 g\",\n    \"field_path\":\
    \ \"ingredients[10].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"1.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz320\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\",\n        \"\
    source_locator\": \"PDF pages1–2 SL10 stock table; named row\",\n        \"exact_source_quote\"\
    : \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\": \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\"\
    ,\n        \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the explicit SL10 make-up to 1 L, stock 1.5 g/L × 0.001 L aliquot = 0.0015 g\
    \ delivered per source batch; no final-medium g/L follows.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"SL10: ZnCl2 70.00 mg\",\n    \"field_path\": \"ingredients[11].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.07\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz320\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\"\
    ,\n        \"source_locator\": \"PDF pages1–2 SL10 stock table; named row\",\n\
    \        \"exact_source_quote\": \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[11].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.07\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[11].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the explicit SL10 make-up\
    \ to 1 L, stock 0.07 g/L × 0.001 L aliquot = 0.00007 g delivered per source batch;\
    \ no final-medium g/L follows.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    SL10: MnCl2 x 4 H2O 100.00 mg\",\n    \"field_path\": \"ingredients[12].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.1\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz320\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\"\
    ,\n        \"source_locator\": \"PDF pages1–2 SL10 stock table; named row\",\n\
    \        \"exact_source_quote\": \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the explicit SL10 make-up to 1 L, stock 0.1 g/L × 0.001 L aliquot = 0.0001 g\
    \ delivered per source batch; no final-medium g/L follows.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"SL10: H3BO3 6.00 mg\",\n    \"field_path\": \"ingredients[13].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.006\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz320\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\"\
    ,\n        \"source_locator\": \"PDF pages1–2 SL10 stock table; named row\",\n\
    \        \"exact_source_quote\": \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[13].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.006\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[13].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the explicit SL10 make-up\
    \ to 1 L, stock 0.006 g/L × 0.001 L aliquot = 0.000006 g delivered per source\
    \ batch; no final-medium g/L follows.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"SL10: CoCl2 x 6 H2O 190.00 mg\",\n    \"field_path\": \"ingredients[14].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.19\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz320\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\"\
    ,\n        \"source_locator\": \"PDF pages1–2 SL10 stock table; named row\",\n\
    \        \"exact_source_quote\": \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[14].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.19\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[14].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the explicit SL10 make-up\
    \ to 1 L, stock 0.19 g/L × 0.001 L aliquot = 0.00019 g delivered per source batch;\
    \ no final-medium g/L follows.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    SL10: CuCl2 x 2 H2O 2.00 mg\",\n    \"field_path\": \"ingredients[15].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.002\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz320\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\"\
    ,\n        \"source_locator\": \"PDF pages1–2 SL10 stock table; named row\",\n\
    \        \"exact_source_quote\": \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[15].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.002\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the explicit SL10 make-up\
    \ to 1 L, stock 0.002 g/L × 0.001 L aliquot = 0.000002 g delivered per source\
    \ batch; no final-medium g/L follows.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"SL10: NiCl2 x 6 H2O 24.00 mg\",\n    \"field_path\": \"ingredients[16].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.024\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz320\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\"\
    ,\n        \"source_locator\": \"PDF pages1–2 SL10 stock table; named row\",\n\
    \        \"exact_source_quote\": \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[16].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.024\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[16].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the explicit SL10 make-up\
    \ to 1 L, stock 0.024 g/L × 0.001 L aliquot = 0.000024 g delivered per source\
    \ batch; no final-medium g/L follows.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"SL10: Na2MoO4 x 2 H2O 36.00 mg\",\n    \"field_path\": \"ingredients[17].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.036\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz320\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\"\
    ,\n        \"source_locator\": \"PDF pages1–2 SL10 stock table; named row\",\n\
    \        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\"\
    : \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\",\n    \
    \    \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[17].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.036\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[17].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the explicit SL10 make-up\
    \ to 1 L, stock 0.036 g/L × 0.001 L aliquot = 0.000036 g delivered per source\
    \ batch; no final-medium g/L follows.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Vitamin stock: Biotin 2.00 mg\",\n    \"field_path\": \"ingredients[18].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.002\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz141\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"PDF pages2–3 Wolin vitamin stock table; named\
    \ row\",\n        \"exact_source_quote\": \"Biotin 2.00 mg\",\n        \"snapshot_sha256\"\
    : \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\",\n    \
    \    \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[18].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.002\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[18].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The source gives the vitamin\
    \ mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.002\
    \ g/L × 0.001 L would deliver 0.000002 g; measured stock/final-medium volume is\
    \ not asserted.\"\n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock:\
    \ Folic acid 2.00 mg\",\n    \"field_path\": \"ingredients[19].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.002\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz141\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"PDF pages2–3 Wolin vitamin stock table; named\
    \ row\",\n        \"exact_source_quote\": \"Folic acid 2.00 mg\",\n        \"\
    snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[19].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.002\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[19].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The source gives the vitamin\
    \ mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.002\
    \ g/L × 0.001 L would deliver 0.000002 g; measured stock/final-medium volume is\
    \ not asserted.\"\n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock:\
    \ Pyridoxine hydrochloride 10.00 mg\",\n    \"field_path\": \"ingredients[20].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.01\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz141\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"PDF pages2–3 Wolin vitamin stock table; named\
    \ row\",\n        \"exact_source_quote\": \"Pyridoxine hydrochloride 10.00 mg\"\
    ,\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[20].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[20].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The source gives the vitamin\
    \ mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.01\
    \ g/L × 0.001 L would deliver 0.00001 g; measured stock/final-medium volume is\
    \ not asserted.\"\n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock:\
    \ Thiamine HCl 5.00 mg\",\n    \"field_path\": \"ingredients[21].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.005\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz141\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"PDF pages2–3 Wolin vitamin stock table; named\
    \ row\",\n        \"exact_source_quote\": \"Thiamine HCl 5.00 mg\",\n        \"\
    snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[21].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[21].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The source gives the vitamin\
    \ mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.005\
    \ g/L × 0.001 L would deliver 0.000005 g; measured stock/final-medium volume is\
    \ not asserted.\"\n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock:\
    \ Riboflavin 5.00 mg\",\n    \"field_path\": \"ingredients[22].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.005\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz141\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"PDF pages2–3 Wolin vitamin stock table; named\
    \ row\",\n        \"exact_source_quote\": \"Riboflavin 5.00 mg\",\n        \"\
    snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[22].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[22].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The source gives the vitamin\
    \ mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.005\
    \ g/L × 0.001 L would deliver 0.000005 g; measured stock/final-medium volume is\
    \ not asserted.\"\n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock:\
    \ Nicotinic acid 5.00 mg\",\n    \"field_path\": \"ingredients[23].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.005\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz141\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"PDF pages2–3 Wolin vitamin stock table; named\
    \ row\",\n        \"exact_source_quote\": \"Nicotinic acid 5.00 mg\",\n      \
    \  \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[23].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[23].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The source gives the vitamin\
    \ mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.005\
    \ g/L × 0.001 L would deliver 0.000005 g; measured stock/final-medium volume is\
    \ not asserted.\"\n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock:\
    \ Calcium D-(+)-pantothenate 5.00 mg\",\n    \"field_path\": \"ingredients[24].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.005\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz141\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"PDF pages2–3 Wolin vitamin stock table; named\
    \ row\",\n        \"exact_source_quote\": \"Calcium D-(+)-pantothenate 5.00 mg\"\
    ,\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[24].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[24].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The source gives the vitamin\
    \ mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.005\
    \ g/L × 0.001 L would deliver 0.000005 g; measured stock/final-medium volume is\
    \ not asserted.\"\n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock:\
    \ Vitamin B12 0.10 mg\",\n    \"field_path\": \"ingredients[25].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.0001\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz141\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"PDF pages2–3 Wolin vitamin stock table; named\
    \ row\",\n        \"exact_source_quote\": \"Vitamin B12 0.10 mg\",\n        \"\
    snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[25].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.0001\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[25].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The source gives the vitamin\
    \ mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.0001\
    \ g/L × 0.001 L would deliver 1E-7 g; measured stock/final-medium volume is not\
    \ asserted.\"\n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock: p-Aminobenzoic\
    \ acid 5.00 mg\",\n    \"field_path\": \"ingredients[26].concentration\",\n  \
    \  \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.005\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz141\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"PDF pages2–3 Wolin vitamin stock table; named\
    \ row\",\n        \"exact_source_quote\": \"p-Aminobenzoic acid 5.00 mg\",\n \
    \       \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[26].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[26].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The source gives the vitamin\
    \ mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.005\
    \ g/L × 0.001 L would deliver 0.000005 g; measured stock/final-medium volume is\
    \ not asserted.\"\n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock:\
    \ (DL)-alpha-Lipoic acid 5.00 mg\",\n    \"field_path\": \"ingredients[27].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.005\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz141\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"PDF pages2–3 Wolin vitamin stock table; named\
    \ row\",\n        \"exact_source_quote\": \"(DL)-alpha-Lipoic acid 5.00 mg\",\n\
    \        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the original stock recipe and\
    \ unit, with its separate 1 mL main-medium dose. The current field improperly\
    \ states an undiluted direct-medium concentration.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[27].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[27].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The source gives the vitamin\
    \ mass with 1000 mL water. Conditional only on a nominal 1 L stock basis, 0.005\
    \ g/L × 0.001 L would deliver 0.000005 g; measured stock/final-medium volume is\
    \ not asserted.\"\n  },\n  {\n    \"ingredient_or_context\": \"SL10 aliquot\"\
    ,\n    \"field_path\": \"solutions\",\n    \"decision\": \"add\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1187\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"main table\",\n        \"exact_source_quote\"\
    : \"Trace elements SL-10 (see medium 320) 1.0 ml\",\n        \"snapshot_sha256\"\
    : \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\",\n    \
    \    \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"Represent this source-only quantity in\
    \ its named stage, preserving volume units. An existing preparation container\
    \ is not an assertion of this water or stock dose.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"solutions\",\n        \"\
    stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Vitamin aliquot\",\n    \"field_path\": \"solutions\",\n    \"decision\":\
    \ \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz1187\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"main table\",\n        \"exact_source_quote\"\
    : \"Vitamin solution (see medium 141) 1.0 ml\",\n        \"snapshot_sha256\":\
    \ \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\",\n    \
    \    \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"Represent this source-only quantity in\
    \ its named stage, preserving volume units. An existing preparation container\
    \ is not an assertion of this water or stock dose.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"solutions\",\n        \"\
    stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main water\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz1187\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"main table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.0 ml\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"Represent this source-only quantity in\
    \ its named stage, preserving volume units. An existing preparation container\
    \ is not an assertion of this water or stock dose.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"preparation_steps\",\n \
    \       \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"pH 9.0\"\n          },\n          {\n        \
    \    \"step_number\": 2,\n            \"action\": \"AUTOCLAVE\",\n           \
    \ \"description\": \"Prepare the medium anaerobically without the vitamins, Na2S,\
    \ yeast extract NaHCO3, and Na2CO3. Boil the medium, cool under N2, add the NaHCO3,\
    \ and Na2CO3, dispense under N2 and autoclave the medium. Add the vitamin solution,\
    \ yeast extract, Na2S and glucose from sterile stock solution prepared under N2\
    \ to the cooled, autoclaved medium.\"\n          },\n          {\n           \
    \ \"step_number\": 3,\n            \"action\": \"DISSOLVE\",\n            \"description\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n   \
    \     \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"SL10 water\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"add\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz320\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\"\
    ,\n        \"source_locator\": \"SL10 table\",\n        \"exact_source_quote\"\
    : \"Distilled water 990.00 ml\",\n        \"snapshot_sha256\": \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\"\
    ,\n        \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    \n      }\n    ],\n    \"rationale\": \"Represent this source-only quantity in\
    \ its named stage, preserving volume units. An existing preparation container\
    \ is not an assertion of this water or stock dose.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"solutions\",\n        \"\
    stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Vitamin water\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"\
    add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz141\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Wolin vitamin table, page3\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Represent this source-only quantity in\
    \ its named stage, preserving volume units. An existing preparation container\
    \ is not an assertion of this water or stock dose.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"solutions\",\n        \"\
    stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main scalar pH\",\n    \"field_path\": \"ph_value\",\n    \"decision\": \"\
    evidence_only\",\n    \"local\": 9.0,\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz1187\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"main pH line\",\n        \"exact_source_quote\"\
    : \"pH 9.0\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"The correct scalar is retained in all\
    \ three layers without attached exact claim evidence.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ph_value\",\n      \
    \  \"stored\": 9.0,\n        \"decision\": \"evidence_only\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.0,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main preparation pH\",\n    \"field_path\": \"preparation_steps\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz1187\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\"\
    ,\n        \"source_locator\": \"main pH line\",\n        \"exact_source_quote\"\
    : \"pH 9.0\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the literal endpoint with evidence\
    \ in its correct stage. The DSMZ stock make-up instruction belongs to SL10 rather\
    \ than the main medium.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n      \
    \  \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"pH 9.0\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n  },\n\
    \  {\n    \"ingredient_or_context\": \"SL10 final make-up\",\n    \"field_path\"\
    : \"solutions\",\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz320\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf\",\n        \"\
    source_locator\": \"SL10 make-up, page2\",\n        \"exact_source_quote\": \"\
    make up to 1000.00 ml.\",\n        \"snapshot_sha256\": \"d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9\"\
    ,\n        \"parsed_text_sha256\": \"d554a6501afdfb01554cfd9b8b9dbeb3f5ade38605ab46b91b1fabc6b11179b6\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the literal endpoint with evidence\
    \ in its correct stage. The DSMZ stock make-up instruction belongs to SL10 rather\
    \ than the main medium.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Unquantified later-stock\
    \ strengths and N2 fraction\",\n    \"field_path\": \"preparation_steps\",\n \
    \   \"decision\": \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1187\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1187.pdf\",\n       \
    \ \"source_locator\": \"final main preparation sentence\",\n        \"exact_source_quote\"\
    : \"glucose from sterile stock solution prepared under N2 to the cooled, autoclaved\
    \ medium.\",\n        \"snapshot_sha256\": \"b806a3c363658796f93c3fd63604c34a18b0f49a4a33e3d4bd42539872f0865c\"\
    ,\n        \"parsed_text_sha256\": \"05fabfb14c078169b2d701f9802d4953f50ddd045bff3e3f40b5f2938ff2d949\"\
    \n      }\n    ],\n    \"rationale\": \"The primary names sterile late stocks\
    \ and N2 but gives no strengths, extra aliquot volumes or nitrogen percentage;\
    \ no values may be invented.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n \
    \       \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": [\n          {\n            \"step_number\"\
    : 1,\n            \"action\": \"MIX\",\n            \"description\": \"pH 9.0\"\
    \n          },\n          {\n            \"step_number\": 2,\n            \"action\"\
    : \"AUTOCLAVE\",\n            \"description\": \"Prepare the medium anaerobically\
    \ without the vitamins, Na2S, yeast extract NaHCO3, and Na2CO3. Boil the medium,\
    \ cool under N2, add the NaHCO3, and Na2CO3, dispense under N2 and autoclave the\
    \ medium. Add the vitamin solution, yeast extract, Na2S and glucose from sterile\
    \ stock solution prepared under N2 to the cooled, autoclaved medium.\"\n     \
    \     },\n          {\n            \"step_number\": 3,\n            \"action\"\
    : \"DISSOLVE\",\n            \"description\": \"First dissolve FeCl2 in the HCl,\
    \ then dilute in water, add and dissolve the other salts. Finally make up to 1000.00\
    \ ml.\"\n          }\n        ],\n        \"decision\": \"not_quantified\"\n \
    \     }\n    ]\n  }\n]"
findings:
- finding_id: f1
  issue_key: anoyxnatronum-stock-flattening
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock constituents replace the intended dilute additions
  description: Nine SL10 and ten vitamin constituents are direct g/L in all three
    local layers, while both 1 mL stock doses are absent. The acid volume/percentage
    is additionally converted to unsupported mass. This changes the denoted formulation;
    the nine main g/L values retain an unresolved final-volume basis.
  target_ids:
  - CultureMech:003907
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1187
  - dsmz320
  - dsmz141
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml
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
  issue_key: anoyxnatronum-nickel-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Source nickel hexahydrate is grounded to anhydrous salt
  description: SL10 uses NiCl2 x 6 H2O, 24 mg per stock preparation. CHEBI:34887 in
    both primary and secondary fields denotes Cl2Ni without six waters.
  target_ids:
  - CultureMech:003907
  field_paths:
  - ingredients[16].term
  - ingredients[16].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - dsmz320
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml
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
  issue_key: anoyxnatronum-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Anaerobic preparation is lost and stock make-up is misplaced
  description: The target and KOMODO owner omit the main anaerobic/autoclave/late-addition
    procedure. The DSMZ owner retains it but presents the SL10 make-up to1000 mL as
    a main preparation step. Source-specific stage recovery is required; this is a
    representation defect, not evidence for an unprinted sterilization cycle.
  target_ids:
  - CultureMech:003907
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1187
  - dsmz320
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml
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
  issue_key: anoyxnatronum-catalog-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Aerobic catalog metadata and historical timestamps need qualification
  description: 'The target and KOMODO owner retain Aerobic: Yes while the primary
    prescribes anaerobic preparation. They also retain malformed .fZ and timezone-naive
    history values. These are metadata limits, not grounds to invent physiology or
    corrected dates.'
  target_ids:
  - CultureMech:003907
  field_paths:
  - notes
  - curation_history
  evidence_ids:
  - record
  - catalog
  - history-metadata
  - dsmz1187
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml
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
  description: Rebuild SL10 and the vitamin stock in the maintained owners with exact
    source units and separate 1 mL doses; preserve direct batch masses and unknown
    final denominator, then regenerate only compatible source records.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003907
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml
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
  description: Verify a source-matching hydrate identifier for both asserted slots
    and retain the original stock mass and dose. Do not invent a replacement or convert
    to anhydrous mass.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003907
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml
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
  description: Preserve the DSMZ main sequence with claim evidence, move the trace
    preparation under SL10 and reconcile the other owner before regeneration; keep
    N2 unquantified.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003907
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml
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
  description: Attribute the catalog flag and append bounded provenance clarifications
    during authorized curation; preserve historical events and avoid guessing missing
    timestamp content.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003907
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml
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
- 'mediadive1187api: exact public request returned HTTP 503; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'komodo1187detail: exact public request returned HTTP 403; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'komodo1187actual: exact public request returned HTTP 403; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'mediadive1187retry: exact public request returned HTTP 503; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'Both exact main MediaDive attempts returned503. They are optional corroboration
  here: no existing attached historical amount claim is independently authenticated
  or asserted. Available collection primaries support the bounded assessment; final-volume
  uncertainty is explicitly assessed rather than hidden.'
- Only named SL10 and vitamin subsections transfer from the parent PDFs; parent organisms,
  basal recipes and gas conditions are excluded.
- This scientific assessment preceded formal review validation and saving; their results
  are recorded separately.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-029
- generated-medium
```
