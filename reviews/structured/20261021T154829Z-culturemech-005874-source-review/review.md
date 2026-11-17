# Source and formulation review: anaerocellum_medium (CultureMech:005874)

- Review: 20261021T154829Z-culturemech-005874-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T15:43:28Z
- Finished UTC: 2026-10-21T15:48:29Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The ANAEROCELLUM merge combines the base recipe with two explicitly different strain variants, while every local layer flattens SL10 and vitamin stocks. Reconcile the maintained variant formulations, restore stock doses and source-specific preparation, and correct nickel/resazurin forms before regeneration. Exact historical provider correspondence remains unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 272; batch 028 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-seven task batches contain 270 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 273 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:005874 | data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml | generated | anaerocellum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:005874 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:005874 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch028/272/strict.tsv |
| validate-terms | passed | True | CultureMech:005874 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:005874 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:005874 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive516api | unavailable | True | CultureMech:005874 | mediadive516api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodoMediaListCanonical | unavailable | False | CultureMech:005874 | komodoMediaListCanonical: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodo516detail | unavailable | False | CultureMech:005874 | komodo516detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodo516_1detail | unavailable | False | CultureMech:005874 | komodo516_1detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodo516_9003detail | unavailable | False | CultureMech:005874 | komodo516_9003detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: mediadive516apiRetry | unavailable | True | CultureMech:005874 | mediadive516apiRetry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodo516actual | unavailable | False | CultureMech:005874 | komodo516actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodo516_1actual | unavailable | False | CultureMech:005874 | komodo516_1actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodo516_9003actual | unavailable | False | CultureMech:005874 | komodo516_9003actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:005874.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:005874.

28 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 28/29 primary and 26/29 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 29: primary 96.55%; secondary 89.66%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:005874.

48 timestamp instances inspected; 8 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Base formulation and two strain-specific variants

identity: concern. Targets: CultureMech:005874.

Target CultureMech:005874 includes KOMODO 516, DSMZ 516 CultureMech:001648, DSM 6724 owner CultureMech:005872 and DSM 9003 owner CultureMech:005873. The latter two are explicit source variants, not synonyms of an unchanged formula. All five local layers nevertheless share 29 ingredient amounts. Current owners already have reciprocal STRAIN_SPECIFIC_VARIANT relationships, while the generated target retains stale SOURCE_DUPLICATE relationships and synonym collapse.

### Stock dilution and variant-specific amounts

consistency: concern. Targets: CultureMech:005874.

SL10 is added at 1 mL and the 10x vitamin stock at 1 mL; their 19 stock constituents appear undiluted in every local direct-ingredient list. The primary replaces cellobiose with 5 g/L soluble starch for DSM 6724, and specifies 1 g/L Trypticase plus 2 g/L yeast extract for DSM 9003. Neither change is represented in its owner. Base rounded g/L values are compatible with a 1.002 L denominator, but listed water plus three quantified liquid additions totals 1002.5 mL, before unspecified later-stock volumes. Neither sum is measured final volume.

### Anaerobic main procedure and separate stock instructions

completeness: concern. Targets: CultureMech:005874.

The DSMZ owner alone retains the main gas fractions, 30–45 min sparging, autoclaving, later additions and vitamin/cellobiose filtration. It places SL10 dissolution and final 1000 mL makeup among main steps. Other layers omit preparation. The DSM 6724 starch clause includes a sterile anoxic stock added after autoclaving and must remain variant-specific. No unprinted sterilization temperature/duration is added.

### Classifications and bounded organism scope

scope: supported. Targets: CultureMech:005874.

COMPLEX and SEMI_DEFINED describe a formulation with named salts/substrate plus yeast extract; LIQUID matches the source. Generic bacterial cultivation is not a growth-result assertion. DSM numbers in owner names and source variant clauses identify formulation scope; no unsupported species, taxonomy, genome, incubation optimum, DOI or PMID is inferred. KOMODO aerobic flags remain catalog metadata rather than validation of the anaerobic primary instructions.

### Nickel hydration and resazurin sodium salt

grounding: concern. Targets: CultureMech:005874.

The source specifies nickel chloride hexahydrate but CHEBI:34887 denotes Cl2Ni without water. Sodium resazurin is grounded to CHEBI:8806, whose formula C12H7NO4 contains no sodium. HCl 25% has no printed mass/volume basis and cannot by itself justify 2.5 g/L. Other explicit hydrate forms agree with their captured structures; calcium D-(+)-pantothenate and nonspecific DL-lipoic acid are not falsely flagged.

### Topology repair does not establish ingredient curation

provenance: concern. Targets: CultureMech:005874.

The September topology repair changed relationships/status while guarding unchanged concentrations. Current owner ingredients_curated flags therefore do not substantiate the missing source variant formulas. Current importer stock handling and lossless formulation merge guards support a maintained-owner correction route; they do not replay historical imports or validate the stale generated merge.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:005874.

46 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "NH4Cl 0.33 g",
    "field_path": "ingredients[0].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.329341",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 base table; exact named row",
        "exact_source_quote": "NH4Cl 0.33 g",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The base source batch amount is supported, but the historical normalized g/L basis is not independently verified. Variant-specific contrary amounts or substrate replacement are marked correct only in the affected owner layer.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 0.33 g / 1.002 L = 0.3293413173652694610778443114 g/L. The displayed local rounding is retained; 1.002 L is not an independently established final volume."
  },
  {
    "ingredient_or_context": "KH2PO4 0.33 g",
    "field_path": "ingredients[1].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.329341",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 base table; exact named row",
        "exact_source_quote": "KH2PO4 0.33 g",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The base source batch amount is supported, but the historical normalized g/L basis is not independently verified. Variant-specific contrary amounts or substrate replacement are marked correct only in the affected owner layer.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 0.33 g / 1.002 L = 0.3293413173652694610778443114 g/L. The displayed local rounding is retained; 1.002 L is not an independently established final volume."
  },
  {
    "ingredient_or_context": "KCl 0.33 g",
    "field_path": "ingredients[2].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.329341",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 base table; exact named row",
        "exact_source_quote": "KCl 0.33 g",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The base source batch amount is supported, but the historical normalized g/L basis is not independently verified. Variant-specific contrary amounts or substrate replacement are marked correct only in the affected owner layer.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 0.33 g / 1.002 L = 0.3293413173652694610778443114 g/L. The displayed local rounding is retained; 1.002 L is not an independently established final volume."
  },
  {
    "ingredient_or_context": "MgCl2 x 6 H2O 0.33 g",
    "field_path": "ingredients[3].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.329341",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 base table; exact named row",
        "exact_source_quote": "MgCl2 x 6 H2O 0.33 g",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The base source batch amount is supported, but the historical normalized g/L basis is not independently verified. Variant-specific contrary amounts or substrate replacement are marked correct only in the affected owner layer.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 0.33 g / 1.002 L = 0.3293413173652694610778443114 g/L. The displayed local rounding is retained; 1.002 L is not an independently established final volume."
  },
  {
    "ingredient_or_context": "CaCl2 x 2 H2O 0.33 g",
    "field_path": "ingredients[4].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.329341",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 base table; exact named row",
        "exact_source_quote": "CaCl2 x 2 H2O 0.33 g",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The base source batch amount is supported, but the historical normalized g/L basis is not independently verified. Variant-specific contrary amounts or substrate replacement are marked correct only in the affected owner layer.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 0.33 g / 1.002 L = 0.3293413173652694610778443114 g/L. The displayed local rounding is retained; 1.002 L is not an independently established final volume."
  },
  {
    "ingredient_or_context": "Yeast extract 0.50 g",
    "field_path": "ingredients[5].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.499002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 base table; exact named row",
        "exact_source_quote": "Yeast extract 0.50 g",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      },
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 DSM 9003 variant clause",
        "exact_source_quote": "For DSM 9003: Supplement medium with 1.00 g/l Trypticase peptone and increase amount\nof yeast extract to 2.00 g/l.",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The base source batch amount is supported, but the historical normalized g/L basis is not independently verified. Variant-specific contrary amounts or substrate replacement are marked correct only in the affected owner layer.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional comparison only: 0.5 g / 1.002 L = 0.4990019960079840319361277445 g/L. The displayed local rounding is retained; 1.002 L is not an independently established final volume."
  },
  {
    "ingredient_or_context": "Sodium resazurin (0.1% w/v) 0.50 ml",
    "field_path": "ingredients[6].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.000499002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 base table; exact named row",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The base source batch amount is supported, but the historical normalized g/L basis is not independently verified. Variant-specific contrary amounts or substrate replacement are marked correct only in the affected owner layer.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.000499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.000499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.000499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.000499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.000499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "0.1 g/100 mL × 0.50 mL = 0.0005 g sodium resazurin delivered. Dividing by a hypothetical 1.002 L gives 0.000499001996 g/L; the denominator is unresolved and the source stock strength/dose must remain explicit."
  },
  {
    "ingredient_or_context": "Na2CO3 1.50 g",
    "field_path": "ingredients[7].concentration",
    "decision": "unsupported",
    "local": {
      "value": "1.49701",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 base table; exact named row",
        "exact_source_quote": "Na2CO3 1.50 g",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The base source batch amount is supported, but the historical normalized g/L basis is not independently verified. Variant-specific contrary amounts or substrate replacement are marked correct only in the affected owner layer.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.49701",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.49701",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.49701",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.49701",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.49701",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 1.5 g / 1.002 L = 1.497005988023952095808383234 g/L. The displayed local rounding is retained; 1.002 L is not an independently established final volume."
  },
  {
    "ingredient_or_context": "Cellobiose 5.00 g",
    "field_path": "ingredients[8].concentration",
    "decision": "unsupported",
    "local": {
      "value": "4.99002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 base table; exact named row",
        "exact_source_quote": "Cellobiose 5.00 g",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      },
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 DSM 6724 variant clause",
        "exact_source_quote": "For DSM 6724: Replace cellobiose with 5.00 g/l soluble starch as substrate added to the\nautoclaved medium from a sterile anoxic stock solution.",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The base source batch amount is supported, but the historical normalized g/L basis is not independently verified. Variant-specific contrary amounts or substrate replacement are marked correct only in the affected owner layer.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "4.99002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "4.99002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "4.99002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "4.99002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "4.99002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 5 g / 1.002 L = 4.990019960079840319361277445 g/L. The displayed local rounding is retained; 1.002 L is not an independently established final volume."
  },
  {
    "ingredient_or_context": "Na2S x 9 H2O 0.50 g",
    "field_path": "ingredients[9].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.499002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 base table; exact named row",
        "exact_source_quote": "Na2S x 9 H2O 0.50 g",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The base source batch amount is supported, but the historical normalized g/L basis is not independently verified. Variant-specific contrary amounts or substrate replacement are marked correct only in the affected owner layer.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 0.5 g / 1.002 L = 0.4990019960079840319361277445 g/L. The displayed local rounding is retained; 1.002 L is not an independently established final volume."
  },
  {
    "ingredient_or_context": "SL10 stock: HCl (25%) 10.00 ml",
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "local": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 SL10 table",
        "exact_source_quote": "HCl (25%) 10.00 ml",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "HCl 25%, 10 mL is a stock reagent addition. The percentage basis is unspecified; no 2.5 g or final g/L conversion is endorsed."
  },
  {
    "ingredient_or_context": "SL10 stock: FeCl2 x 4 H2O 1.50 g",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "local": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 SL10 table",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 1.5 g/L × 0.001 L would deliver 0.0015 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "SL10 stock: ZnCl2 70.00 mg",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "local": {
      "value": "0.07",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 SL10 table",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.07 g/L × 0.001 L would deliver 0.00007 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "SL10 stock: MnCl2 x 4 H2O 100.00 mg",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 SL10 table",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.1 g/L × 0.001 L would deliver 0.0001 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "SL10 stock: H3BO3 6.00 mg",
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "local": {
      "value": "0.006",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 SL10 table",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.006 g/L × 0.001 L would deliver 0.000006 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "SL10 stock: CoCl2 x 6 H2O 190.00 mg",
    "field_path": "ingredients[15].concentration",
    "decision": "correct",
    "local": {
      "value": "0.19",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 SL10 table",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.19 g/L × 0.001 L would deliver 0.00019 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "SL10 stock: CuCl2 x 2 H2O 2.00 mg",
    "field_path": "ingredients[16].concentration",
    "decision": "correct",
    "local": {
      "value": "0.002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 SL10 table",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.002 g/L × 0.001 L would deliver 0.000002 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "SL10 stock: NiCl2 x 6 H2O 24.00 mg",
    "field_path": "ingredients[17].concentration",
    "decision": "correct",
    "local": {
      "value": "0.024",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 SL10 table",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.024 g/L × 0.001 L would deliver 0.000024 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "SL10 stock: Na2MoO4 x 2 H2O 36.00 mg",
    "field_path": "ingredients[18].concentration",
    "decision": "correct",
    "local": {
      "value": "0.036",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 SL10 table",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.036 g/L × 0.001 L would deliver 0.000036 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "Vitamin stock: Biotin 20.00 mg",
    "field_path": "ingredients[19].concentration",
    "decision": "correct",
    "local": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) table",
        "exact_source_quote": "Biotin 20.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.02 g/L × 0.001 L would deliver 0.00002 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "Vitamin stock: Folic acid 20.00 mg",
    "field_path": "ingredients[20].concentration",
    "decision": "correct",
    "local": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) table",
        "exact_source_quote": "Folic acid 20.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
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
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.02 g/L × 0.001 L would deliver 0.00002 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "Vitamin stock: Pyridoxine hydrochloride 100.00 mg",
    "field_path": "ingredients[21].concentration",
    "decision": "correct",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) table",
        "exact_source_quote": "Pyridoxine hydrochloride 100.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.1 g/L × 0.001 L would deliver 0.0001 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "Vitamin stock: Thiamine HCl 50.00 mg",
    "field_path": "ingredients[22].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) table",
        "exact_source_quote": "Thiamine HCl 50.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "Vitamin stock: Riboflavin 50.00 mg",
    "field_path": "ingredients[23].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) table",
        "exact_source_quote": "Riboflavin 50.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "Vitamin stock: Nicotinic acid 50.00 mg",
    "field_path": "ingredients[24].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) table",
        "exact_source_quote": "Nicotinic acid 50.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "Vitamin stock: Calcium D-(+)-pantothenate 50.00 mg",
    "field_path": "ingredients[25].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) table",
        "exact_source_quote": "Calcium D-(+)-pantothenate 50.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "Vitamin stock: Vitamin B12 1.00 mg",
    "field_path": "ingredients[26].concentration",
    "decision": "correct",
    "local": {
      "value": "0.001",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) table",
        "exact_source_quote": "Vitamin B12 1.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.001 g/L × 0.001 L would deliver 0.000001 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "Vitamin stock: p-Aminobenzoic acid 50.00 mg",
    "field_path": "ingredients[27].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) table",
        "exact_source_quote": "p-Aminobenzoic acid 50.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "Vitamin stock: (DL)-alpha-Lipoic acid 50.00 mg",
    "field_path": "ingredients[28].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) table",
        "exact_source_quote": "(DL)-alpha-Lipoic acid 50.00 mg",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Restore the source stock composition, original units and 1 mL receiving dose. These are not undiluted direct-medium concentrations.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per listed batch. The vitamin calculation is conditional on that declared stock basis; no final-medium g/L is inferred."
  },
  {
    "ingredient_or_context": "SL10 dose",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 main table",
        "exact_source_quote": "Trace element solution SL-10 1.00 ml",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Preserve the named stock aliquot/strength or solvent quantity at the correct stage. Existing container contents are recorded exactly and do not imply these absent quantitative claims.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Vitamin dose",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 main table",
        "exact_source_quote": "Wolin's vitamin solution (10x) 1.00 ml",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Preserve the named stock aliquot/strength or solvent quantity at the correct stage. Existing container contents are recorded exactly and do not imply these absent quantitative claims.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Resazurin stock strength and aliquot",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 main table",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Preserve the named stock aliquot/strength or solvent quantity at the correct stage. Existing container contents are recorded exactly and do not imply these absent quantitative claims.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
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
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 main table",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Preserve the named stock aliquot/strength or solvent quantity at the correct stage. Existing container contents are recorded exactly and do not imply these absent quantitative claims.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Dissolve ingredients (except vitamins, carbonate, cellobiose and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation add vitamins, cellobiose and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Stock solutions of vitamins and cellobiose should be sterilized by filtration. The pH of the complete medium should be at 7.1 - 7.3."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "SL10 initial water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 SL10 table",
        "exact_source_quote": "Distilled water 990.00 ml",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Preserve the named stock aliquot/strength or solvent quantity at the correct stage. Existing container contents are recorded exactly and do not imply these absent quantitative claims.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
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
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 2 vitamin table",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Preserve the named stock aliquot/strength or solvent quantity at the correct stage. Existing container contents are recorded exactly and do not imply these absent quantitative claims.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main pH range",
    "field_path": "ph_range",
    "decision": "evidence_only",
    "local": {
      "min": 7.1,
      "max": 7.3
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "7.1 - 7.3.",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The base range survives without attached evidence in target/base/6724; the 9003 owner lacks it. Its variant clause changes other components and does not print a different pH.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_range",
        "stored": {
          "min": 7.1,
          "max": 7.3
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.1,
          "max": 7.3
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.1,
          "max": 7.3
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.1,
          "max": 7.3
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ph_range",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main gas fractions",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "80% N2 and 20% CO2 gas mixture for 30 - 45 min",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "DSMZ alone retains the literal procedure. Attach main evidence and restore SL10 stock scope for makeup; reconcile the other source-specific layers without transferring variant-only instructions.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except vitamins, carbonate, cellobiose and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation add vitamins, cellobiose and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Stock solutions of vitamins and cellobiose should be sterilized by filtration. The pH of the complete medium should be at 7.1 - 7.3.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sparging duration",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "30 - 45 min",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "DSMZ alone retains the literal procedure. Attach main evidence and restore SL10 stock scope for makeup; reconcile the other source-specific layers without transferring variant-only instructions.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except vitamins, carbonate, cellobiose and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation add vitamins, cellobiose and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Stock solutions of vitamins and cellobiose should be sterilized by filtration. The pH of the complete medium should be at 7.1 - 7.3.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Later-stock nitrogen fraction",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "stock solutions prepared under 100% N2 gas",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "DSMZ alone retains the literal procedure. Attach main evidence and restore SL10 stock scope for makeup; reconcile the other source-specific layers without transferring variant-only instructions.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except vitamins, carbonate, cellobiose and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation add vitamins, cellobiose and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Stock solutions of vitamins and cellobiose should be sterilized by filtration. The pH of the complete medium should be at 7.1 - 7.3.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Carbonate-stock gas fractions",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "solution prepared under 80% N2 and 20% CO2 gas mixture.",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "DSMZ alone retains the literal procedure. Attach main evidence and restore SL10 stock scope for makeup; reconcile the other source-specific layers without transferring variant-only instructions.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except vitamins, carbonate, cellobiose and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation add vitamins, cellobiose and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Stock solutions of vitamins and cellobiose should be sterilized by filtration. The pH of the complete medium should be at 7.1 - 7.3.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main pH in preparation",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "7.1 - 7.3.",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "DSMZ alone retains the literal procedure. Attach main evidence and restore SL10 stock scope for makeup; reconcile the other source-specific layers without transferring variant-only instructions.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except vitamins, carbonate, cellobiose and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation add vitamins, cellobiose and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Stock solutions of vitamins and cellobiose should be sterilized by filtration. The pH of the complete medium should be at 7.1 - 7.3.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "SL10 final makeup",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 2 SL10 procedure",
        "exact_source_quote": "make up to 1000.00 ml.",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "DSMZ alone retains the literal procedure. Attach main evidence and restore SL10 stock scope for makeup; reconcile the other source-specific layers without transferring variant-only instructions.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "DSM 6724 starch replacement",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "local": {
      "value": "4.99002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 named variant clause",
        "exact_source_quote": "For DSM 6724: Replace cellobiose with 5.00 g/l soluble starch as substrate added to the\nautoclaved medium from a sterile anoxic stock solution.",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Replace the cellobiose ingredient/formulation branch with soluble starch 5.00 g/L only in the DSM 6724 owner; this is an explicit source concentration, not a batch-volume calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "4.99002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "DSM 9003 yeast extract",
    "field_path": "ingredients[5].concentration",
    "decision": "correct",
    "local": {
      "value": "0.499002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 named variant clause",
        "exact_source_quote": "For DSM 9003: Supplement medium with 1.00 g/l Trypticase peptone and increase amount\nof yeast extract to 2.00 g/l.",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The explicit source variant requires yeast extract 2.00 g/L, not the inherited base value.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "DSM 9003 Trypticase addition",
    "field_path": "ingredients",
    "decision": "add",
    "local": [
      {
        "preferred_term": "NH4Cl",
        "term": {
          "id": "CHEBI:31206",
          "label": "ammonium chloride"
        },
        "concentration": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:31206",
          "label": "ammonium chloride"
        }
      },
      {
        "preferred_term": "KH2PO4",
        "term": {
          "id": "CHEBI:63036",
          "label": "potassium dihydrogen phosphate"
        },
        "concentration": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:63036",
          "label": "potassium dihydrogen phosphate"
        }
      },
      {
        "preferred_term": "KCl",
        "term": {
          "id": "CHEBI:32588",
          "label": "potassium chloride"
        },
        "concentration": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:32588",
          "label": "potassium chloride"
        }
      },
      {
        "preferred_term": "MgCl2 x 6 H2O",
        "term": {
          "id": "CHEBI:86345",
          "label": "magnesium dichloride hexahydrate"
        },
        "concentration": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:86345",
          "label": "magnesium dichloride hexahydrate"
        }
      },
      {
        "preferred_term": "CaCl2 x 2 H2O",
        "term": {
          "id": "CHEBI:86158",
          "label": "calcium chloride dihydrate"
        },
        "concentration": {
          "value": "0.329341",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:86158",
          "label": "calcium chloride dihydrate"
        }
      },
      {
        "preferred_term": "Yeast extract",
        "concentration": {
          "value": "0.499002",
          "unit": "G_PER_L"
        }
      },
      {
        "preferred_term": "Sodium resazurin",
        "concentration": {
          "value": "0.000499002",
          "unit": "G_PER_L"
        },
        "term": {
          "id": "CHEBI:8806",
          "label": "Resazurin"
        }
      },
      {
        "preferred_term": "Na2CO3",
        "term": {
          "id": "CHEBI:29377",
          "label": "sodium carbonate"
        },
        "concentration": {
          "value": "1.49701",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:29377",
          "label": "sodium carbonate"
        }
      },
      {
        "preferred_term": "Cellobiose",
        "term": {
          "id": "CHEBI:17057",
          "label": "cellobiose"
        },
        "concentration": {
          "value": "4.99002",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:17057",
          "label": "cellobiose"
        }
      },
      {
        "preferred_term": "Na2S x 9 H2O",
        "term": {
          "id": "CHEBI:76209",
          "label": "sodium sulfide nonahydrate"
        },
        "concentration": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:76209",
          "label": "sodium sulfide nonahydrate"
        }
      },
      {
        "preferred_term": "HCl",
        "term": {
          "id": "CHEBI:17883",
          "label": "hydrogen chloride"
        },
        "concentration": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:17883",
          "label": "hydrogen chloride"
        }
      },
      {
        "preferred_term": "FeCl2 x 4 H2O",
        "term": {
          "id": "CHEBI:86249",
          "label": "iron dichloride tetrahydrate"
        },
        "concentration": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:86249",
          "label": "iron dichloride tetrahydrate"
        }
      },
      {
        "preferred_term": "ZnCl2",
        "term": {
          "id": "CHEBI:49976",
          "label": "zinc dichloride"
        },
        "concentration": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:49976",
          "label": "zinc dichloride"
        }
      },
      {
        "preferred_term": "MnCl2 x 4 H2O",
        "term": {
          "id": "CHEBI:86368",
          "label": "manganese(II) chloride tetrahydrate"
        },
        "concentration": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:86368",
          "label": "manganese(II) chloride tetrahydrate"
        }
      },
      {
        "preferred_term": "H3BO3",
        "term": {
          "id": "CHEBI:33118",
          "label": "boric acid"
        },
        "concentration": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:33118",
          "label": "boric acid"
        }
      },
      {
        "preferred_term": "CoCl2 x 6 H2O",
        "term": {
          "id": "CHEBI:53503",
          "label": "cobalt chloride hexahydrate"
        },
        "concentration": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:53503",
          "label": "cobalt chloride hexahydrate"
        }
      },
      {
        "preferred_term": "CuCl2 x 2 H2O",
        "term": {
          "id": "CHEBI:86318",
          "label": "copper(II) chloride dihydrate"
        },
        "concentration": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:86318",
          "label": "copper(II) chloride dihydrate"
        }
      },
      {
        "preferred_term": "NiCl2 x 6 H2O",
        "term": {
          "id": "CHEBI:34887",
          "label": "nickel dichloride"
        },
        "concentration": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:34887",
          "label": "nickel dichloride"
        }
      },
      {
        "preferred_term": "Na2MoO4 x 2 H2O",
        "term": {
          "id": "CHEBI:75213",
          "label": "sodium molybdate dihydrate"
        },
        "concentration": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:75213",
          "label": "sodium molybdate dihydrate"
        }
      },
      {
        "preferred_term": "Biotin",
        "term": {
          "id": "CHEBI:15956",
          "label": "biotin"
        },
        "concentration": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:15956",
          "label": "biotin"
        }
      },
      {
        "preferred_term": "Folic acid",
        "term": {
          "id": "CHEBI:27470",
          "label": "folic acid"
        },
        "concentration": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:27470",
          "label": "folic acid"
        }
      },
      {
        "preferred_term": "Pyridoxine hydrochloride",
        "term": {
          "id": "CHEBI:30961",
          "label": "pyridoxine hydrochloride"
        },
        "concentration": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:30961",
          "label": "pyridoxine hydrochloride"
        }
      },
      {
        "preferred_term": "Thiamine HCl",
        "term": {
          "id": "CHEBI:49105",
          "label": "thiamine hydrochloride"
        },
        "concentration": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:49105",
          "label": "thiamine hydrochloride"
        }
      },
      {
        "preferred_term": "Riboflavin",
        "term": {
          "id": "CHEBI:17015",
          "label": "riboflavin"
        },
        "concentration": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:17015",
          "label": "riboflavin"
        }
      },
      {
        "preferred_term": "Nicotinic acid",
        "term": {
          "id": "CHEBI:15940",
          "label": "nicotinic acid"
        },
        "concentration": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:15940",
          "label": "nicotinic acid"
        }
      },
      {
        "preferred_term": "Calcium D-(+)-pantothenate",
        "concentration": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "term": {
          "id": "CHEBI:31345",
          "label": "Calcium pantothenate"
        }
      },
      {
        "preferred_term": "Vitamin B12",
        "term": {
          "id": "CHEBI:176843",
          "label": "vitamin B12"
        },
        "concentration": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:176843",
          "label": "vitamin B12"
        }
      },
      {
        "preferred_term": "p-Aminobenzoic acid",
        "term": {
          "id": "CHEBI:30753",
          "label": "4-aminobenzoic acid"
        },
        "concentration": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:30753",
          "label": "4-aminobenzoic acid"
        }
      },
      {
        "preferred_term": "(DL)-alpha-Lipoic acid",
        "term": {
          "id": "CHEBI:16494",
          "label": "lipoic acid"
        },
        "concentration": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:16494",
          "label": "lipoic acid"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 named variant clause",
        "exact_source_quote": "For DSM 9003: Supplement medium with 1.00 g/l Trypticase peptone and increase amount\nof yeast extract to 2.00 g/l.",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "Add the explicit source-only Trypticase peptone 1.00 g/L in its variant owner. Do not add it to the base recipe.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "NH4Cl",
            "term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            },
            "concentration": {
              "value": "0.329341",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            }
          },
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "0.329341",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            }
          },
          {
            "preferred_term": "KCl",
            "term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            },
            "concentration": {
              "value": "0.329341",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            }
          },
          {
            "preferred_term": "MgCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            },
            "concentration": {
              "value": "0.329341",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            }
          },
          {
            "preferred_term": "CaCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "concentration": {
              "value": "0.329341",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "0.499002",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Sodium resazurin",
            "concentration": {
              "value": "0.000499002",
              "unit": "G_PER_L"
            },
            "term": {
              "id": "CHEBI:8806",
              "label": "Resazurin"
            }
          },
          {
            "preferred_term": "Na2CO3",
            "term": {
              "id": "CHEBI:29377",
              "label": "sodium carbonate"
            },
            "concentration": {
              "value": "1.49701",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:29377",
              "label": "sodium carbonate"
            }
          },
          {
            "preferred_term": "Cellobiose",
            "term": {
              "id": "CHEBI:17057",
              "label": "cellobiose"
            },
            "concentration": {
              "value": "4.99002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17057",
              "label": "cellobiose"
            }
          },
          {
            "preferred_term": "Na2S x 9 H2O",
            "term": {
              "id": "CHEBI:76209",
              "label": "sodium sulfide nonahydrate"
            },
            "concentration": {
              "value": "0.499002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:76209",
              "label": "sodium sulfide nonahydrate"
            }
          },
          {
            "preferred_term": "HCl",
            "term": {
              "id": "CHEBI:17883",
              "label": "hydrogen chloride"
            },
            "concentration": {
              "value": "2.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17883",
              "label": "hydrogen chloride"
            }
          },
          {
            "preferred_term": "FeCl2 x 4 H2O",
            "term": {
              "id": "CHEBI:86249",
              "label": "iron dichloride tetrahydrate"
            },
            "concentration": {
              "value": "1.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86249",
              "label": "iron dichloride tetrahydrate"
            }
          },
          {
            "preferred_term": "ZnCl2",
            "term": {
              "id": "CHEBI:49976",
              "label": "zinc dichloride"
            },
            "concentration": {
              "value": "0.07",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:49976",
              "label": "zinc dichloride"
            }
          },
          {
            "preferred_term": "MnCl2 x 4 H2O",
            "term": {
              "id": "CHEBI:86368",
              "label": "manganese(II) chloride tetrahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86368",
              "label": "manganese(II) chloride tetrahydrate"
            }
          },
          {
            "preferred_term": "H3BO3",
            "term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            },
            "concentration": {
              "value": "0.006",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            }
          },
          {
            "preferred_term": "CoCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:53503",
              "label": "cobalt chloride hexahydrate"
            },
            "concentration": {
              "value": "0.19",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:53503",
              "label": "cobalt chloride hexahydrate"
            }
          },
          {
            "preferred_term": "CuCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86318",
              "label": "copper(II) chloride dihydrate"
            },
            "concentration": {
              "value": "0.002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86318",
              "label": "copper(II) chloride dihydrate"
            }
          },
          {
            "preferred_term": "NiCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            },
            "concentration": {
              "value": "0.024",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            }
          },
          {
            "preferred_term": "Na2MoO4 x 2 H2O",
            "term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            },
            "concentration": {
              "value": "0.036",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            }
          },
          {
            "preferred_term": "Biotin",
            "term": {
              "id": "CHEBI:15956",
              "label": "biotin"
            },
            "concentration": {
              "value": "0.02",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15956",
              "label": "biotin"
            }
          },
          {
            "preferred_term": "Folic acid",
            "term": {
              "id": "CHEBI:27470",
              "label": "folic acid"
            },
            "concentration": {
              "value": "0.02",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:27470",
              "label": "folic acid"
            }
          },
          {
            "preferred_term": "Pyridoxine hydrochloride",
            "term": {
              "id": "CHEBI:30961",
              "label": "pyridoxine hydrochloride"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:30961",
              "label": "pyridoxine hydrochloride"
            }
          },
          {
            "preferred_term": "Thiamine HCl",
            "term": {
              "id": "CHEBI:49105",
              "label": "thiamine hydrochloride"
            },
            "concentration": {
              "value": "0.05",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:49105",
              "label": "thiamine hydrochloride"
            }
          },
          {
            "preferred_term": "Riboflavin",
            "term": {
              "id": "CHEBI:17015",
              "label": "riboflavin"
            },
            "concentration": {
              "value": "0.05",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17015",
              "label": "riboflavin"
            }
          },
          {
            "preferred_term": "Nicotinic acid",
            "term": {
              "id": "CHEBI:15940",
              "label": "nicotinic acid"
            },
            "concentration": {
              "value": "0.05",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15940",
              "label": "nicotinic acid"
            }
          },
          {
            "preferred_term": "Calcium D-(+)-pantothenate",
            "concentration": {
              "value": "0.05",
              "unit": "G_PER_L"
            },
            "term": {
              "id": "CHEBI:31345",
              "label": "Calcium pantothenate"
            }
          },
          {
            "preferred_term": "Vitamin B12",
            "term": {
              "id": "CHEBI:176843",
              "label": "vitamin B12"
            },
            "concentration": {
              "value": "0.001",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:176843",
              "label": "vitamin B12"
            }
          },
          {
            "preferred_term": "p-Aminobenzoic acid",
            "term": {
              "id": "CHEBI:30753",
              "label": "4-aminobenzoic acid"
            },
            "concentration": {
              "value": "0.05",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:30753",
              "label": "4-aminobenzoic acid"
            }
          },
          {
            "preferred_term": "(DL)-alpha-Lipoic acid",
            "term": {
              "id": "CHEBI:16494",
              "label": "lipoic acid"
            },
            "concentration": {
              "value": "0.05",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16494",
              "label": "lipoic acid"
            }
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Unspecified later-stock strengths/volumes",
    "field_path": "solutions",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz516",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock\nsolution prepared under 80% N2 and 20% CO2 gas mixture.",
        "snapshot_sha256": "5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801",
        "parsed_text_sha256": "8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831"
      }
    ],
    "rationale": "The source gives main masses and specific listed aliquots, but no separate cellobiose, carbonate or sulfide stock concentration/volume. Do not fabricate those or a complete final-volume denominator.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      }
    ]
  }
]

## Findings

### f1: Stock formulations and explicit strain variants are collapsed

blocker / open / confirmed; issue key: anaerocellum-stock-and-variant-conflation.

All five local layers flatten SL10 and vitamin stocks while retaining the same 29 concentrations. The DSM 6724 owner still has cellobiose instead of 5 g/L starch; the DSM 9003 owner lacks 1 g/L Trypticase and retains base yeast extract instead of 2 g/L. The generated target also collapses these variants as synonyms/source duplicates. The denoted formulations are materially wrong despite topology repairs and ingredients_curated flags.

### f2: Nickel hydrate and sodium resazurin identities are mismatched

major / open / confirmed; issue key: anaerocellum-salt-hydrate-forms.

NiCl2 x 6 H2O uses anhydrous CHEBI:34887 in both asserted slots. Sodium resazurin uses unsalted CHEBI:8806 in the primary slot. Correct canonical labels do not make these source forms equivalent.

### f3: Source preparation is omitted or flattened across stages

major / open / confirmed; issue key: anaerocellum-preparation-stock-scope.

Only the DSMZ owner preserves main anaerobic handling; its SL10 dissolution/makeup is misplaced as main preparation. Other layers omit source procedures, including the DSM 6724-specific sterile starch addition.

### f4: Catalog metadata and history need bounded qualification

minor / open / confirmed; issue key: anaerocellum-catalog-history-qualification.

KOMODO base and DSM 6724 flags say Aerobic: Yes while DSM 9003 says No; these are source catalog values, not experimental validation. Target and KOMODO-derived owners retain malformed and naive historical timestamps.

## Recommended Actions And Acceptance Checks

### a1

Reconcile the base and both explicit variants in maintained owners, preserving source stock architecture and concentrations. Reassess status flags and regenerate only compatible records; do not repeat topology-only repair as ingredient curation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve exact source-supported hydrate and sodium-salt identifiers without guessed replacements or mass conversions. Preserve 24 mg nickel salt per SL10 stock and the 0.1% w/v, 0.50 mL resazurin addition.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Keep main gas/pH/filtration instructions and SL10 1000 mL makeup in their separate stages, and preserve the strain-specific starch procedure. Use broad P2 for the combined representation defect; do not invent a sterilization cycle.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve exact catalog attribution and append any justified historical clarification without silently rewriting old timestamps or treating catalog flags as growth evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/anaerocellum_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/for_dsm_6724.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-3 | data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch028/272/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch028/272/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml:1:id: CultureMech:005874<br>./data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml:1:id: CultureMech:005874<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch028/source-preflight-bound/272/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 45 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch028/source-preflight-bound/272/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf; Complete PDF pages 1–2: base recipe, DSM 6724/9003 clauses, SL10 and vitamin sections | supports | Both page images and text were read. The source explicitly replaces cellobiose with starch for DSM 6724 and adds Trypticase/increases yeast extract for DSM 9003. |
| sl10-parent | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf; SL10 recipe and final 1000 mL makeup only | supports | The full parent was read, but unrelated basal ingredients, sludge/rumen fluid and organism scope are excluded. |
| vitamin-parent | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf; Wolin vitamin solution (10x) subsection only | supports | Only the named ten-vitamin stock transfers; other stocks, basal composition and organism instructions are excluded. |
| solution595 | https://mediadive.dsmz.de/rest/solution/595; $.data.id, name, volume, recipe and steps | supports | Exact SL10 stock endpoint declares volume 1000 and retains HCl 25%, 10 mL plus 990 mL water and explicit 1000 mL makeup. Its g_l value for HCl does not supply the missing percentage basis. |
| solution5980 | https://mediadive.dsmz.de/rest/solution/5980; $.data.id, name, volume, recipe and steps | supports | Exact vitamin stock endpoint declares nominal volume 1000. It does not establish the main-medium final volume or independently recover the historical main API. |
| catalog-0 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact href MediaInfo=516 and exact header | context_only | Exact catalog accession/name/pH/aerobic metadata only; a catalog row is not the unavailable variant formulation. |
| catalog-1 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact href MediaInfo=516.1 and exact header | context_only | Exact catalog accession/name/pH/aerobic metadata only; a catalog row is not the unavailable variant formulation. |
| catalog-2 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact href MediaInfo=516_9003 and exact header | context_only | Exact catalog accession/name/pH/aerobic metadata only; a catalog row is not the unavailable variant formulation. |
| mediadive516api-attempt | https://mediadive.dsmz.de/rest/medium/516; Preserved exact public retrieval result | context_only | mediadive516api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodoMediaListCanonical-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaList; Preserved exact public retrieval result | context_only | komodoMediaListCanonical: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodo516detail-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaInfo=516; Preserved exact public retrieval result | context_only | komodo516detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodo516_1detail-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaInfo=516.1; Preserved exact public retrieval result | context_only | komodo516_1detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodo516_9003detail-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaInfo=516_9003; Preserved exact public retrieval result | context_only | komodo516_9003detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| mediadive516apiRetry-attempt | https://mediadive.dsmz.de/rest/medium/516; Preserved exact public retrieval result | context_only | mediadive516apiRetry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodo516actual-attempt | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=516; Preserved exact public retrieval result | context_only | komodo516actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodo516_1actual-attempt | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=516.1; Preserved exact public retrieval result | context_only | komodo516_1actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodo516_9003actual-attempt | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=516_9003; Preserved exact public retrieval result | context_only | komodo516_9003actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| historical-report | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/anaerocellum_medium.yaml.md; Complete dated header and extracted source recipe/step rows | context_only | The unchanged-result hash matches the DSMZ owner. Historical g_l values and source hash/time are derivative report assertions, not independently recovered raw API bytes. |
| topology-writer | scripts/repair_komodo_516_anaerocellum_score10.py; Complete script, exact ingredient guards, repair_hub, repair_child and history/status writes | context_only | The current script preserves the 29-ingredient signature while changing reciprocal parent/variant relations and setting ingredients_curated. It does not implement the source starch, Trypticase or increased yeast-extract formulations. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17057 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17057 resolves to cellobiose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17057": [{"label": "Cellobiose", "match_type": "preferred_term", "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml; data/normalized_yaml/bacterial/anaerocellum_medium.yaml; data/normalized_yaml/bacterial/for_dsm_6724.yaml; data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:04.555633"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:04.555633"}]}, {"input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:15.387185"}]}, {"input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:04.093074"}]}] |
| quantity-inventory | /private/tmp/culturemech-review-work-batch028/272/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch028/272/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- mediadive516api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodoMediaListCanonical: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodo516detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodo516_1detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodo516_9003detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- mediadive516apiRetry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodo516actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodo516_1actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodo516_9003actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- Both exact main MediaDive 516 attempts returned HTTP 503; exact historical main-response correspondence and normalization remain unavailable. The dated report does not substitute for raw bytes. All KOMODO detail failures remain preserved; current primary explicitly supports the two stated variant changes.
- The listed 1002.5 mL liquid sum and the numerically implied 1002 mL historical denominator are distinct and neither is measured final volume. HCl 25% has no stated percent basis.
- Only named SL10/vitamin parent subsections transfer. No source strain mention is promoted to a taxonomic, assembly or growth claim.
- This scientific assessment preceded formal review validation and saving; their results are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T154829Z-culturemech-005874-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerocellum_medium (CultureMech:005874)'
started_at: '2026-10-21T15:43:28Z'
finished_at: '2026-10-21T15:48:29Z'
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
summary: The ANAEROCELLUM merge combines the base recipe with two explicitly different
  strain variants, while every local layer flattens SL10 and vitamin stocks. Reconcile
  the maintained variant formulations, restore stock doses and source-specific preparation,
  and correct nickel/resazurin forms before regeneration. Exact historical provider
  correspondence remains unavailable.
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
  - path: data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml
    sha256: 4c2a12e42130dcd7d923d0a68eeb6b4ec19ff30e93f42fe9e404df3ecdbda6f3
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml
    sha256: 1331b9febdc7246c5c2c975ada321bddb5784dea109242dd8139d51311231962
    role: context
  - path: data/normalized_yaml/bacterial/anaerocellum_medium.yaml
    sha256: 7666925954d51356346bfb4a09b97fdd3367ce5b91ed48cf9465b994ecc5c1e9
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_6724.yaml
    sha256: 3be4479c4031561dda1c93347908d4631bf0b5a1041bc37172417e49f440815f
    role: context
  - path: data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml
    sha256: 7257739b96c49c1c8afd06cb6e8e905e130429fad6f8f5c21a13efd41083db20
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/anaerocellum_medium.yaml.md
    sha256: 2e33e3922186992d791a58d355ab089f42d9a9343cca8e20348e2a4f87b50442
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
  - path: scripts/repair_komodo_516_anaerocellum_score10.py
    sha256: a8957cdaa22ff486ee1b7e409879c5422353f540d02784478db68a35c8102514
    role: context
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
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
  selection: Task review 272; batch 028 item 2 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-seven task batches
    contain 270 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 273 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:005874
targets:
- target_id: CultureMech:005874
  path: data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml
  label: anaerocellum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerocellum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_6724.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch028/272/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch028/272/strict.tsv"
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:005874
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
  - CultureMech:005874
- check_id: mediadive516api-source-access
  name: 'Exact source content access: mediadive516api'
  required: true
  status: unavailable
  summary: 'mediadive516api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - mediadive516api-attempt
- check_id: komodoMediaListCanonical-source-access
  name: 'Exact source content access: komodoMediaListCanonical'
  required: false
  status: unavailable
  summary: 'komodoMediaListCanonical: exact public request returned HTTP 403; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - komodoMediaListCanonical-attempt
- check_id: komodo516detail-source-access
  name: 'Exact source content access: komodo516detail'
  required: false
  status: unavailable
  summary: 'komodo516detail: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - komodo516detail-attempt
- check_id: komodo516_1detail-source-access
  name: 'Exact source content access: komodo516_1detail'
  required: false
  status: unavailable
  summary: 'komodo516_1detail: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - komodo516_1detail-attempt
- check_id: komodo516_9003detail-source-access
  name: 'Exact source content access: komodo516_9003detail'
  required: false
  status: unavailable
  summary: 'komodo516_9003detail: exact public request returned HTTP 403; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - komodo516_9003detail-attempt
- check_id: mediadive516apiRetry-source-access
  name: 'Exact source content access: mediadive516apiRetry'
  required: true
  status: unavailable
  summary: 'mediadive516apiRetry: exact public request returned HTTP 503; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - mediadive516apiRetry-attempt
- check_id: komodo516actual-source-access
  name: 'Exact source content access: komodo516actual'
  required: false
  status: unavailable
  summary: 'komodo516actual: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - komodo516actual-attempt
- check_id: komodo516_1actual-source-access
  name: 'Exact source content access: komodo516_1actual'
  required: false
  status: unavailable
  summary: 'komodo516_1actual: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - komodo516_1actual-attempt
- check_id: komodo516_9003actual-source-access
  name: 'Exact source content access: komodo516_9003actual'
  required: false
  status: unavailable
  summary: 'komodo516_9003actual: exact public request returned HTTP 403; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - komodo516_9003actual-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerocellum_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_6724.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:43:43.545336Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch028/272/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T15:43:45.724855Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch028/272/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:43:47.994387Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:43:49.186611Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T15:48:28Z'
  support: supports
  summary: './data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml:1:id: CultureMech:005874

    ./data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml:1:id: CultureMech:005874

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/source-preflight-bound/272/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T15:48:28Z'
  support: supports
  summary: 45 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 416c9a1c8345db2dc60918f0a78d69e63e7f644924b4f197c58a59ee4fee996a
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/source-preflight-bound/272/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: 2ae5a41e8fd5befb8117f6620f700c9f88092d42d5b4e4536df6a6fe97a5a68c
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T15:48:28Z'
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
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf
  locator: 'Complete PDF pages 1–2: base recipe, DSM 6724/9003 clauses, SL10 and vitamin
    sections'
  accessed_at: '2026-10-21T15:16:37.386140Z'
  support: supports
  summary: Both page images and text were read. The source explicitly replaces cellobiose
    with starch for DSM 6724 and adds Trypticase/increases yeast extract for DSM 9003.
  snapshot_sha256: 5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801
- evidence_id: sl10-parent
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf
  locator: SL10 recipe and final 1000 mL makeup only
  accessed_at: '2026-10-21T13:20:08.151265Z'
  support: supports
  summary: The full parent was read, but unrelated basal ingredients, sludge/rumen
    fluid and organism scope are excluded.
  snapshot_sha256: d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9
- evidence_id: vitamin-parent
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf
  locator: Wolin vitamin solution (10x) subsection only
  accessed_at: '2026-10-21T13:16:27.298931Z'
  support: supports
  summary: Only the named ten-vitamin stock transfers; other stocks, basal composition
    and organism instructions are excluded.
  snapshot_sha256: e1f85e4a546abc825218226bbb18d78bd9c054b7e11399aa7161ad259a3b663f
- evidence_id: solution595
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/595
  locator: $.data.id, name, volume, recipe and steps
  accessed_at: '2026-10-21T11:03:05.357684Z'
  support: supports
  summary: Exact SL10 stock endpoint declares volume 1000 and retains HCl 25%, 10
    mL plus 990 mL water and explicit 1000 mL makeup. Its g_l value for HCl does not
    supply the missing percentage basis.
  snapshot_sha256: 5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab
- evidence_id: solution5980
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5980
  locator: $.data.id, name, volume, recipe and steps
  accessed_at: '2026-10-21T11:03:05.362213Z'
  support: supports
  summary: Exact vitamin stock endpoint declares nominal volume 1000. It does not
    establish the main-medium final volume or independently recover the historical
    main API.
  snapshot_sha256: 2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c
- evidence_id: catalog-0
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact href MediaInfo=516 and exact header
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: context_only
  summary: Exact catalog accession/name/pH/aerobic metadata only; a catalog row is
    not the unavailable variant formulation.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=516'\
    \ >516</a></TD>\n\t\t\t\t\t<TD>ANAEROCELLUM medium</TD>\n\t\t\t\t\t<TD> 7.1 -\
    \ 7.3</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n\
    <TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf</a></TD>\n\t\
    \t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: catalog-1
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact href MediaInfo=516.1 and exact header
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: context_only
  summary: Exact catalog accession/name/pH/aerobic metadata only; a catalog row is
    not the unavailable variant formulation.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=516.1'\
    \ >516.1</a></TD>\n\t\t\t\t\t<TD> For DSM 6724</TD>\n\t\t\t\t\t<TD> 7.1 - 7.3</TD>\n\
    \t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n<TD><a\
    \ href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: catalog-2
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact href MediaInfo=516_9003 and exact header
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: context_only
  summary: Exact catalog accession/name/pH/aerobic metadata only; a catalog row is
    not the unavailable variant formulation.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=516_9003'\
    \ >516_9003</a></TD>\n\t\t\t\t\t<TD>MEDIUM 516 MODIFIED FOR DSM 9003</TD>\n\t\t\
    \t\t\t<TD>null</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\
    \t\t<TD>false</TD>\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf</a></TD>\n\t\
    \t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: mediadive516api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/516
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.752935Z'
  support: context_only
  summary: 'mediadive516api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodoMediaListCanonical-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaList
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.731434Z'
  support: context_only
  summary: 'komodoMediaListCanonical: exact public request returned HTTP 403; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  snapshot_sha256: de9e2f3074ac08195adc2554773d95a742ed9a6bb880fb2c361ab1916afcfbb3
- evidence_id: komodo516detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaInfo=516
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.405067Z'
  support: context_only
  summary: 'komodo516detail: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 8100c00ff73956a11f167682dee9c7214de5fcc6130a57baf03fe7e212bfd07f
- evidence_id: komodo516_1detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaInfo=516.1
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.430490Z'
  support: context_only
  summary: 'komodo516_1detail: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: cead9fba74a5b57ce35f0ef548f00279450603a924baf451d650c83a59dfb4cc
- evidence_id: komodo516_9003detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaInfo=516_9003
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.431618Z'
  support: context_only
  summary: 'komodo516_9003detail: exact public request returned HTTP 403; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  snapshot_sha256: fd2a0c1baa392672249fb9bfa6c08daac0bbe7d12bed045298c7e5bad304490b
- evidence_id: mediadive516apiRetry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/516
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:19:00.532613Z'
  support: context_only
  summary: 'mediadive516apiRetry: exact public request returned HTTP 503; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo516actual-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=516
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:19:00.144731Z'
  support: context_only
  summary: 'komodo516actual: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: a02bed2ce6ff0422a8b617bb0fdd168b75a5ba0efdb7252157ebaaad9ccc0d93
- evidence_id: komodo516_1actual-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=516.1
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:19:00.176138Z'
  support: context_only
  summary: 'komodo516_1actual: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 1b82b176b6f286d4d091525e5f8113d23b54fdf111a6efa8e4c5a745eeb5e5ff
- evidence_id: komodo516_9003actual-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=516_9003
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:19:00.180797Z'
  support: context_only
  summary: 'komodo516_9003actual: exact public request returned HTTP 403; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  snapshot_sha256: 4977bec8a4f7fca9d8921d8f5da6343b578cb40d13a0a84c3a0bc5122364dc04
- evidence_id: historical-report
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/anaerocellum_medium.yaml.md
  locator: Complete dated header and extracted source recipe/step rows
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: The unchanged-result hash matches the DSMZ owner. Historical g_l values
    and source hash/time are derivative report assertions, not independently recovered
    raw API bytes.
  snapshot_sha256: 2e33e3922186992d791a58d355ab089f42d9a9343cca8e20348e2a4f87b50442
- evidence_id: topology-writer
  kind: record_content
  reference: scripts/repair_komodo_516_anaerocellum_score10.py
  locator: Complete script, exact ingredient guards, repair_hub, repair_child and
    history/status writes
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: The current script preserves the 29-ingredient signature while changing
    reciprocal parent/variant relations and setting ingredients_curated. It does not
    implement the source starch, Trypticase or increased yeast-extract formulations.
  snapshot_sha256: a8957cdaa22ff486ee1b7e409879c5422353f540d02784478db68a35c8102514
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
- evidence_id: chebi17057
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:39.796651Z'
  support: supports
  summary: CHEBI:17057 resolves to cellobiose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 3548f79d3274a33683125152944998cffa00bd4fce774c8d872db9003222ed06
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
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T15:48:28Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15940":
    [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940",
    "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type":
    "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id":
    "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494":
    [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label":
    "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term":
    "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:17057": [{"label": "Cellobiose", "match_type": "preferred_term",
    "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label":
    "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term",
    "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label":
    "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate
    solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic
    acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type":
    "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride",
    "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier":
    "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type":
    "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id":
    "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118":
    [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label":
    "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term":
    "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label":
    "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209":
    [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id":
    "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318":
    [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368":
    [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml;
    data/normalized_yaml/bacterial/anaerocellum_medium.yaml; data/normalized_yaml/bacterial/for_dsm_6724.yaml;
    data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:04.555633"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml",
    "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:04.555633"}]}, {"input": "data/normalized_yaml/bacterial/anaerocellum_medium.yaml",
    "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/for_dsm_6724.yaml",
    "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:15.387185"}]}, {"input": "data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml",
    "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:04.093074"}]}]'
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/272/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: f23e2e311c51cd2925231485ffa5cfdf044d86e3e85e8fa7ef959da7c324c161
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/272/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T15:48:28Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: aa2ff25d8775fb850de98b6116cc63337478a74db1b08675afaebd3164c38146
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '28 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 28/29
    primary and 26/29 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - owner-2
  - owner-3
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi17057
  - chebi176843
  - chebi17883
  - chebi27470
  - chebi29377
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi49105
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi75213
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 29: primary 96.55%;
    secondary 89.66%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 48 timestamp instances inspected; 8 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
  - owner-3
- assessment_id: identity
  area: identity
  topic: Base formulation and two strain-specific variants
  outcome: concern
  summary: Target CultureMech:005874 includes KOMODO 516, DSMZ 516 CultureMech:001648,
    DSM 6724 owner CultureMech:005872 and DSM 9003 owner CultureMech:005873. The latter
    two are explicit source variants, not synonyms of an unchanged formula. All five
    local layers nevertheless share 29 ingredient amounts. Current owners already
    have reciprocal STRAIN_SPECIFIC_VARIANT relationships, while the generated target
    retains stale SOURCE_DUPLICATE relationships and synonym collapse.
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - owner-3
  - primary
  - catalog-0
  - catalog-1
  - catalog-2
  - topology-writer
  - id-search
- assessment_id: formulation
  area: consistency
  topic: Stock dilution and variant-specific amounts
  outcome: concern
  summary: SL10 is added at 1 mL and the 10x vitamin stock at 1 mL; their 19 stock
    constituents appear undiluted in every local direct-ingredient list. The primary
    replaces cellobiose with 5 g/L soluble starch for DSM 6724, and specifies 1 g/L
    Trypticase plus 2 g/L yeast extract for DSM 9003. Neither change is represented
    in its owner. Base rounded g/L values are compatible with a 1.002 L denominator,
    but listed water plus three quantified liquid additions totals 1002.5 mL, before
    unspecified later-stock volumes. Neither sum is measured final volume.
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - record
  - primary
  - solution595
  - solution5980
  - historical-report
- assessment_id: preparation
  area: completeness
  topic: Anaerobic main procedure and separate stock instructions
  outcome: concern
  summary: The DSMZ owner alone retains the main gas fractions, 30–45 min sparging,
    autoclaving, later additions and vitamin/cellobiose filtration. It places SL10
    dissolution and final 1000 mL makeup among main steps. Other layers omit preparation.
    The DSM 6724 starch clause includes a sterile anoxic stock added after autoclaving
    and must remain variant-specific. No unprinted sterilization temperature/duration
    is added.
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - record
  - owner-1
  - primary
  - sl10-parent
- assessment_id: classification
  area: scope
  topic: Classifications and bounded organism scope
  outcome: supported
  summary: COMPLEX and SEMI_DEFINED describe a formulation with named salts/substrate
    plus yeast extract; LIQUID matches the source. Generic bacterial cultivation is
    not a growth-result assertion. DSM numbers in owner names and source variant clauses
    identify formulation scope; no unsupported species, taxonomy, genome, incubation
    optimum, DOI or PMID is inferred. KOMODO aerobic flags remain catalog metadata
    rather than validation of the anaerobic primary instructions.
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - record
  - primary
  - catalog-0
  - catalog-1
  - catalog-2
- assessment_id: forms
  area: grounding
  topic: Nickel hydration and resazurin sodium salt
  outcome: concern
  summary: The source specifies nickel chloride hexahydrate but CHEBI:34887 denotes
    Cl2Ni without water. Sodium resazurin is grounded to CHEBI:8806, whose formula
    C12H7NO4 contains no sodium. HCl 25% has no printed mass/volume basis and cannot
    by itself justify 2.5 g/L. Other explicit hydrate forms agree with their captured
    structures; calcium D-(+)-pantothenate and nonspecific DL-lipoic acid are not
    falsely flagged.
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - record
  - primary
  - chebi34887
  - chebi8806
  - chebi31345
  - chebi16494
- assessment_id: writer-scope
  area: provenance
  topic: Topology repair does not establish ingredient curation
  outcome: concern
  summary: The September topology repair changed relationships/status while guarding
    unchanged concentrations. Current owner ingredients_curated flags therefore do
    not substantiate the missing source variant formulas. Current importer stock handling
    and lossless formulation merge guards support a maintained-owner correction route;
    they do not replay historical imports or validate the stale generated merge.
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - record
  - topology-writer
  - historical-report
  - writer-context-0
  - writer-context-1
  - writer-context-2
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 46 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:005874
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"NH4Cl 0.33 g\",\n    \"field_path\"\
    : \"ingredients[0].concentration\",\n    \"decision\": \"unsupported\",\n    \"\
    local\": {\n      \"value\": \"0.329341\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz516\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 base table; exact named row\",\n \
    \       \"exact_source_quote\": \"NH4Cl 0.33 g\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The base source batch amount is supported,\
    \ but the historical normalized g/L basis is not independently verified. Variant-specific\
    \ contrary amounts or substrate replacement are marked correct only in the affected\
    \ owner layer.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[0].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.329341\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 0.33 g / 1.002 L = 0.3293413173652694610778443114\
    \ g/L. The displayed local rounding is retained; 1.002 L is not an independently\
    \ established final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"KH2PO4\
    \ 0.33 g\",\n    \"field_path\": \"ingredients[1].concentration\",\n    \"decision\"\
    : \"unsupported\",\n    \"local\": {\n      \"value\": \"0.329341\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 base table; exact named row\",\n \
    \       \"exact_source_quote\": \"KH2PO4 0.33 g\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The base source batch amount is supported,\
    \ but the historical normalized g/L basis is not independently verified. Variant-specific\
    \ contrary amounts or substrate replacement are marked correct only in the affected\
    \ owner layer.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[1].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.329341\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 0.33 g / 1.002 L = 0.3293413173652694610778443114\
    \ g/L. The displayed local rounding is retained; 1.002 L is not an independently\
    \ established final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"KCl\
    \ 0.33 g\",\n    \"field_path\": \"ingredients[2].concentration\",\n    \"decision\"\
    : \"unsupported\",\n    \"local\": {\n      \"value\": \"0.329341\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 base table; exact named row\",\n \
    \       \"exact_source_quote\": \"KCl 0.33 g\",\n        \"snapshot_sha256\":\
    \ \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The base source batch amount is supported,\
    \ but the historical normalized g/L basis is not independently verified. Variant-specific\
    \ contrary amounts or substrate replacement are marked correct only in the affected\
    \ owner layer.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[2].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.329341\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 0.33 g / 1.002 L = 0.3293413173652694610778443114\
    \ g/L. The displayed local rounding is retained; 1.002 L is not an independently\
    \ established final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"MgCl2\
    \ x 6 H2O 0.33 g\",\n    \"field_path\": \"ingredients[3].concentration\",\n \
    \   \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.329341\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 base table; exact named row\",\n \
    \       \"exact_source_quote\": \"MgCl2 x 6 H2O 0.33 g\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The base source batch amount is supported,\
    \ but the historical normalized g/L basis is not independently verified. Variant-specific\
    \ contrary amounts or substrate replacement are marked correct only in the affected\
    \ owner layer.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[3].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.329341\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 0.33 g / 1.002 L = 0.3293413173652694610778443114\
    \ g/L. The displayed local rounding is retained; 1.002 L is not an independently\
    \ established final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"CaCl2\
    \ x 2 H2O 0.33 g\",\n    \"field_path\": \"ingredients[4].concentration\",\n \
    \   \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.329341\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 base table; exact named row\",\n \
    \       \"exact_source_quote\": \"CaCl2 x 2 H2O 0.33 g\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The base source batch amount is supported,\
    \ but the historical normalized g/L basis is not independently verified. Variant-specific\
    \ contrary amounts or substrate replacement are marked correct only in the affected\
    \ owner layer.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[4].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.329341\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 0.33 g / 1.002 L = 0.3293413173652694610778443114\
    \ g/L. The displayed local rounding is retained; 1.002 L is not an independently\
    \ established final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"Yeast\
    \ extract 0.50 g\",\n    \"field_path\": \"ingredients[5].concentration\",\n \
    \   \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.499002\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 base table; exact named row\",\n \
    \       \"exact_source_quote\": \"Yeast extract 0.50 g\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      },\n      {\n        \"source_key\": \"dsmz516\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\",\n    \
    \    \"source_locator\": \"PDF page 1 DSM 9003 variant clause\",\n        \"exact_source_quote\"\
    : \"For DSM 9003: Supplement medium with 1.00 g/l Trypticase peptone and increase\
    \ amount\\nof yeast extract to 2.00 g/l.\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The base source batch amount is supported,\
    \ but the historical normalized g/L basis is not independently verified. Variant-specific\
    \ contrary amounts or substrate replacement are marked correct only in the affected\
    \ owner layer.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[5].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.499002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 0.5 g / 1.002 L = 0.4990019960079840319361277445\
    \ g/L. The displayed local rounding is retained; 1.002 L is not an independently\
    \ established final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"Sodium\
    \ resazurin (0.1% w/v) 0.50 ml\",\n    \"field_path\": \"ingredients[6].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.000499002\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 base table; exact named row\",\n \
    \       \"exact_source_quote\": \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n   \
    \     \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The base source batch amount is supported,\
    \ but the historical normalized g/L basis is not independently verified. Variant-specific\
    \ contrary amounts or substrate replacement are marked correct only in the affected\
    \ owner layer.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.000499002\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[6].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.000499002\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"unsupported\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000499002\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"unsupported\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"\
    field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.000499002\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000499002\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"0.1 g/100 mL × 0.50 mL = 0.0005 g sodium resazurin delivered. Dividing by\
    \ a hypothetical 1.002 L gives 0.000499001996 g/L; the denominator is unresolved\
    \ and the source stock strength/dose must remain explicit.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"Na2CO3 1.50 g\",\n    \"field_path\": \"ingredients[7].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"1.49701\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 base table; exact named row\",\n \
    \       \"exact_source_quote\": \"Na2CO3 1.50 g\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The base source batch amount is supported,\
    \ but the historical normalized g/L basis is not independently verified. Variant-specific\
    \ contrary amounts or substrate replacement are marked correct only in the affected\
    \ owner layer.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"1.49701\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[7].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1.49701\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.49701\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1.49701\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.49701\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 1.5 g / 1.002 L = 1.497005988023952095808383234\
    \ g/L. The displayed local rounding is retained; 1.002 L is not an independently\
    \ established final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"Cellobiose\
    \ 5.00 g\",\n    \"field_path\": \"ingredients[8].concentration\",\n    \"decision\"\
    : \"unsupported\",\n    \"local\": {\n      \"value\": \"4.99002\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 base table; exact named row\",\n \
    \       \"exact_source_quote\": \"Cellobiose 5.00 g\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      },\n      {\n        \"source_key\": \"dsmz516\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\",\n    \
    \    \"source_locator\": \"PDF page 1 DSM 6724 variant clause\",\n        \"exact_source_quote\"\
    : \"For DSM 6724: Replace cellobiose with 5.00 g/l soluble starch as substrate\
    \ added to the\\nautoclaved medium from a sterile anoxic stock solution.\",\n\
    \        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The base source batch amount is supported,\
    \ but the historical normalized g/L basis is not independently verified. Variant-specific\
    \ contrary amounts or substrate replacement are marked correct only in the affected\
    \ owner layer.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"4.99002\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[8].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"4.99002\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"4.99002\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"ingredients[8].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"4.99002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.99002\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 5 g / 1.002 L = 4.990019960079840319361277445\
    \ g/L. The displayed local rounding is retained; 1.002 L is not an independently\
    \ established final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"Na2S\
    \ x 9 H2O 0.50 g\",\n    \"field_path\": \"ingredients[9].concentration\",\n \
    \   \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.499002\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 base table; exact named row\",\n \
    \       \"exact_source_quote\": \"Na2S x 9 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The base source batch amount is supported,\
    \ but the historical normalized g/L basis is not independently verified. Variant-specific\
    \ contrary amounts or substrate replacement are marked correct only in the affected\
    \ owner layer.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[9].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[9].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[9].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"ingredients[9].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.499002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 0.5 g / 1.002 L = 0.4990019960079840319361277445\
    \ g/L. The displayed local rounding is retained; 1.002 L is not an independently\
    \ established final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"SL10\
    \ stock: HCl (25%) 10.00 ml\",\n    \"field_path\": \"ingredients[10].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"2.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 SL10 table\",\n        \"exact_source_quote\"\
    : \"HCl (25%) 10.00 ml\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[10].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"HCl\
    \ 25%, 10 mL is a stock reagent addition. The percentage basis is unspecified;\
    \ no 2.5 g or final g/L conversion is endorsed.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"SL10 stock: FeCl2 x 4 H2O 1.50 g\",\n    \"field_path\": \"ingredients[11].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 SL10 table\",\n        \"exact_source_quote\"\
    : \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[11].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 1.5\
    \ g/L × 0.001 L would deliver 0.0015 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"SL10 stock: ZnCl2 70.00 mg\",\n\
    \    \"field_path\": \"ingredients[12].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": {\n      \"value\": \"0.07\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz516\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 SL10 table\",\n        \"exact_source_quote\"\
    : \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[12].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[12].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.07 g/L × 0.001 L would deliver 0.00007 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"SL10 stock: MnCl2 x 4 H2O 100.00\
    \ mg\",\n    \"field_path\": \"ingredients[13].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.1\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 SL10 table\",\n        \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[13].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.1\
    \ g/L × 0.001 L would deliver 0.0001 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"SL10 stock: H3BO3 6.00 mg\",\n \
    \   \"field_path\": \"ingredients[14].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"local\": {\n      \"value\": \"0.006\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz516\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 SL10 table\",\n        \"exact_source_quote\"\
    : \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[14].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[14].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.006 g/L × 0.001 L would deliver 0.000006 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"SL10 stock: CoCl2 x 6 H2O 190.00\
    \ mg\",\n    \"field_path\": \"ingredients[15].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.19\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 SL10 table\",\n        \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[15].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.19 g/L × 0.001 L would deliver 0.00019 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"SL10 stock: CuCl2 x 2 H2O 2.00 mg\"\
    ,\n    \"field_path\": \"ingredients[16].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": {\n      \"value\": \"0.002\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 SL10 table\",\n        \"exact_source_quote\"\
    : \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[16].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[16].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.002 g/L × 0.001 L would deliver 0.000002 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"SL10 stock: NiCl2 x 6 H2O 24.00\
    \ mg\",\n    \"field_path\": \"ingredients[17].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.024\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 SL10 table\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[17].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[17].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.024 g/L × 0.001 L would deliver 0.000024 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"SL10 stock: Na2MoO4 x 2 H2O 36.00\
    \ mg\",\n    \"field_path\": \"ingredients[18].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.036\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 SL10 table\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[18].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[18].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.036 g/L × 0.001 L would deliver 0.000036 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock: Biotin 20.00 mg\"\
    ,\n    \"field_path\": \"ingredients[19].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": {\n      \"value\": \"0.02\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz516\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) table\",\n   \
    \     \"exact_source_quote\": \"Biotin 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[19].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[19].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.02 g/L × 0.001 L would deliver 0.00002 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock: Folic acid 20.00\
    \ mg\",\n    \"field_path\": \"ingredients[20].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.02\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) table\",\n   \
    \     \"exact_source_quote\": \"Folic acid 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[20].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[20].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.02 g/L × 0.001 L would deliver 0.00002 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock: Pyridoxine hydrochloride\
    \ 100.00 mg\",\n    \"field_path\": \"ingredients[21].concentration\",\n    \"\
    decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.1\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) table\",\n   \
    \     \"exact_source_quote\": \"Pyridoxine hydrochloride 100.00 mg\",\n      \
    \  \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[21].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration, 0.1\
    \ g/L × 0.001 L would deliver 0.0001 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock: Thiamine HCl 50.00\
    \ mg\",\n    \"field_path\": \"ingredients[22].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.05\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) table\",\n   \
    \     \"exact_source_quote\": \"Thiamine HCl 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[22].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[22].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.05 g/L × 0.001 L would deliver 0.00005 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock: Riboflavin 50.00\
    \ mg\",\n    \"field_path\": \"ingredients[23].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.05\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) table\",\n   \
    \     \"exact_source_quote\": \"Riboflavin 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[23].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[23].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.05 g/L × 0.001 L would deliver 0.00005 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock: Nicotinic acid 50.00\
    \ mg\",\n    \"field_path\": \"ingredients[24].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.05\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) table\",\n   \
    \     \"exact_source_quote\": \"Nicotinic acid 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[24].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[24].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.05 g/L × 0.001 L would deliver 0.00005 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock: Calcium D-(+)-pantothenate\
    \ 50.00 mg\",\n    \"field_path\": \"ingredients[25].concentration\",\n    \"\
    decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.05\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) table\",\n   \
    \     \"exact_source_quote\": \"Calcium D-(+)-pantothenate 50.00 mg\",\n     \
    \   \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[25].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[25].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.05 g/L × 0.001 L would deliver 0.00005 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock: Vitamin B12 1.00\
    \ mg\",\n    \"field_path\": \"ingredients[26].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.001\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) table\",\n   \
    \     \"exact_source_quote\": \"Vitamin B12 1.00 mg\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[26].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[26].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.001 g/L × 0.001 L would deliver 0.000001 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock: p-Aminobenzoic acid\
    \ 50.00 mg\",\n    \"field_path\": \"ingredients[27].concentration\",\n    \"\
    decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.05\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) table\",\n   \
    \     \"exact_source_quote\": \"p-Aminobenzoic acid 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[27].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[27].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.05 g/L × 0.001 L would deliver 0.00005 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Vitamin stock: (DL)-alpha-Lipoic\
    \ acid 50.00 mg\",\n    \"field_path\": \"ingredients[28].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.05\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) table\",\n   \
    \     \"exact_source_quote\": \"(DL)-alpha-Lipoic acid 50.00 mg\",\n        \"\
    snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source stock composition,\
    \ original units and 1 mL receiving dose. These are not undiluted direct-medium\
    \ concentrations.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[28].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[28].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\",\n\
    \        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the SL10 explicit 1 L makeup or vitamin provider nominal 1 L declaration,\
    \ 0.05 g/L × 0.001 L would deliver 0.00005 g per listed batch. The vitamin calculation\
    \ is conditional on that declared stock basis; no final-medium g/L is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"SL10 dose\",\n    \"field_path\"\
    : \"solutions\",\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz516\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\",\n        \"\
    source_locator\": \"PDF page 1 main table\",\n        \"exact_source_quote\":\
    \ \"Trace element solution SL-10 1.00 ml\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the named stock aliquot/strength\
    \ or solvent quantity at the correct stage. Existing container contents are recorded\
    \ exactly and do not imply these absent quantitative claims.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Vitamin dose\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"\
    add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main table\",\n        \"exact_source_quote\"\
    : \"Wolin's vitamin solution (10x) 1.00 ml\",\n        \"snapshot_sha256\": \"\
    5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n        \"\
    parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the named stock aliquot/strength\
    \ or solvent quantity at the correct stage. Existing container contents are recorded\
    \ exactly and do not imply these absent quantitative claims.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Resazurin stock strength and aliquot\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz516\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\",\n        \"\
    source_locator\": \"PDF page 1 main table\",\n        \"exact_source_quote\":\
    \ \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the named stock aliquot/strength\
    \ or solvent quantity at the correct stage. Existing container contents are recorded\
    \ exactly and do not imply these absent quantitative claims.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main water\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the named stock aliquot/strength\
    \ or solvent quantity at the correct stage. Existing container contents are recorded\
    \ exactly and do not imply these absent quantitative claims.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Dissolve ingredients (except vitamins, carbonate,\
    \ cellobiose and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture\
    \ for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere\
    \ into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation\
    \ add vitamins, cellobiose and sulfide from sterile anoxic stock solutions prepared\
    \ under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared\
    \ under 80% N2 and 20% CO2 gas mixture. Stock solutions of vitamins and cellobiose\
    \ should be sterilized by filtration. The pH of the complete medium should be\
    \ at 7.1 - 7.3.\"\n          },\n          {\n            \"step_number\": 2,\n\
    \            \"action\": \"DISSOLVE\",\n            \"description\": \"First dissolve\
    \ FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\"\n          }\n        ],\n        \"decision\": \"\
    add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"SL10 initial water\",\n    \"field_path\": \"solutions\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 SL10 table\",\n        \"exact_source_quote\"\
    : \"Distilled water 990.00 ml\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the named stock aliquot/strength\
    \ or solvent quantity at the correct stage. Existing container contents are recorded\
    \ exactly and do not imply these absent quantitative claims.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Vitamin water\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"\
    add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 vitamin table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the named stock aliquot/strength\
    \ or solvent quantity at the correct stage. Existing container contents are recorded\
    \ exactly and do not imply these absent quantitative claims.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main pH range\",\n    \"field_path\": \"ph_range\",\n    \"decision\": \"\
    evidence_only\",\n    \"local\": {\n      \"min\": 7.1,\n      \"max\": 7.3\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz516\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"7.1 - 7.3.\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The base range survives without attached\
    \ evidence in target/base/6724; the 9003 owner lacks it. Its variant clause changes\
    \ other components and does not print a different pH.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ph_range\",\n      \
    \  \"stored\": {\n          \"min\": 7.1,\n          \"max\": 7.3\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\",\n  \
    \      \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"min\"\
    : 7.1,\n          \"max\": 7.3\n        },\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.1,\n          \"max\": 7.3\n        },\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.1,\n          \"max\": 7.3\n        },\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main gas fractions\",\n    \"field_path\": \"preparation_steps\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"80% N2 and 20% CO2 gas mixture for 30 - 45 min\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains the literal procedure.\
    \ Attach main evidence and restore SL10 stock scope for makeup; reconcile the\
    \ other source-specific layers without transferring variant-only instructions.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except vitamins, carbonate, cellobiose and sulfide),\
    \ then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make\
    \ it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Prior to inoculation add vitamins, cellobiose\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and\
    \ carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20%\
    \ CO2 gas mixture. Stock solutions of vitamins and cellobiose should be sterilized\
    \ by filtration. The pH of the complete medium should be at 7.1 - 7.3.\",\n  \
    \      \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null,\n        \"decision\": \"\
    add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sparging duration\",\n    \"field_path\": \"preparation_steps\",\n  \
    \  \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"30 - 45 min\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains the literal procedure.\
    \ Attach main evidence and restore SL10 stock scope for makeup; reconcile the\
    \ other source-specific layers without transferring variant-only instructions.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except vitamins, carbonate, cellobiose and sulfide),\
    \ then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make\
    \ it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Prior to inoculation add vitamins, cellobiose\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and\
    \ carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20%\
    \ CO2 gas mixture. Stock solutions of vitamins and cellobiose should be sterilized\
    \ by filtration. The pH of the complete medium should be at 7.1 - 7.3.\",\n  \
    \      \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null,\n        \"decision\": \"\
    add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Later-stock nitrogen fraction\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz516\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\",\n        \"\
    source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"stock solutions prepared under 100% N2 gas\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains the literal procedure.\
    \ Attach main evidence and restore SL10 stock scope for makeup; reconcile the\
    \ other source-specific layers without transferring variant-only instructions.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except vitamins, carbonate, cellobiose and sulfide),\
    \ then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make\
    \ it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Prior to inoculation add vitamins, cellobiose\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and\
    \ carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20%\
    \ CO2 gas mixture. Stock solutions of vitamins and cellobiose should be sterilized\
    \ by filtration. The pH of the complete medium should be at 7.1 - 7.3.\",\n  \
    \      \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null,\n        \"decision\": \"\
    add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Carbonate-stock gas fractions\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz516\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\",\n        \"\
    source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"solution prepared under 80% N2 and 20% CO2 gas mixture.\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains the literal procedure.\
    \ Attach main evidence and restore SL10 stock scope for makeup; reconcile the\
    \ other source-specific layers without transferring variant-only instructions.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except vitamins, carbonate, cellobiose and sulfide),\
    \ then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make\
    \ it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Prior to inoculation add vitamins, cellobiose\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and\
    \ carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20%\
    \ CO2 gas mixture. Stock solutions of vitamins and cellobiose should be sterilized\
    \ by filtration. The pH of the complete medium should be at 7.1 - 7.3.\",\n  \
    \      \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null,\n        \"decision\": \"\
    add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main pH in preparation\",\n    \"field_path\": \"preparation_steps\",\n  \
    \  \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"7.1 - 7.3.\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains the literal procedure.\
    \ Attach main evidence and restore SL10 stock scope for makeup; reconcile the\
    \ other source-specific layers without transferring variant-only instructions.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except vitamins, carbonate, cellobiose and sulfide),\
    \ then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make\
    \ it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Prior to inoculation add vitamins, cellobiose\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and\
    \ carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20%\
    \ CO2 gas mixture. Stock solutions of vitamins and cellobiose should be sterilized\
    \ by filtration. The pH of the complete medium should be at 7.1 - 7.3.\",\n  \
    \      \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null,\n        \"decision\": \"\
    add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"SL10 final makeup\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 SL10 procedure\",\n        \"exact_source_quote\"\
    : \"make up to 1000.00 ml.\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains the literal procedure.\
    \ Attach main evidence and restore SL10 stock scope for makeup; reconcile the\
    \ other source-specific layers without transferring variant-only instructions.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSM 6724 starch replacement\",\n    \"field_path\": \"ingredients[8].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"4.99002\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 named variant clause\",\n        \"\
    exact_source_quote\": \"For DSM 6724: Replace cellobiose with 5.00 g/l soluble\
    \ starch as substrate added to the\\nautoclaved medium from a sterile anoxic stock\
    \ solution.\",\n        \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Replace the cellobiose ingredient/formulation\
    \ branch with soluble starch 5.00 g/L only in the DSM 6724 owner; this is an explicit\
    \ source concentration, not a batch-volume calculation.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\",\n   \
    \     \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"4.99002\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSM 9003 yeast extract\",\n    \"field_path\": \"ingredients[5].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.499002\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 named variant clause\",\n        \"\
    exact_source_quote\": \"For DSM 9003: Supplement medium with 1.00 g/l Trypticase\
    \ peptone and increase amount\\nof yeast extract to 2.00 g/l.\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The explicit source variant requires yeast\
    \ extract 2.00 g/L, not the inherited base value.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"\
    ingredient_or_context\": \"DSM 9003 Trypticase addition\",\n    \"field_path\"\
    : \"ingredients\",\n    \"decision\": \"add\",\n    \"local\": [\n      {\n  \
    \      \"preferred_term\": \"NH4Cl\",\n        \"term\": {\n          \"id\":\
    \ \"CHEBI:31206\",\n          \"label\": \"ammonium chloride\"\n        },\n \
    \       \"concentration\": {\n          \"value\": \"0.329341\",\n          \"\
    unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\": {\n\
    \          \"id\": \"CHEBI:31206\",\n          \"label\": \"ammonium chloride\"\
    \n        }\n      },\n      {\n        \"preferred_term\": \"KH2PO4\",\n    \
    \    \"term\": {\n          \"id\": \"CHEBI:63036\",\n          \"label\": \"\
    potassium dihydrogen phosphate\"\n        },\n        \"concentration\": {\n \
    \         \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:63036\"\
    ,\n          \"label\": \"potassium dihydrogen phosphate\"\n        }\n      },\n\
    \      {\n        \"preferred_term\": \"KCl\",\n        \"term\": {\n        \
    \  \"id\": \"CHEBI:32588\",\n          \"label\": \"potassium chloride\"\n   \
    \     },\n        \"concentration\": {\n          \"value\": \"0.329341\",\n \
    \         \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:32588\",\n          \"label\": \"potassium chloride\"\
    \n        }\n      },\n      {\n        \"preferred_term\": \"MgCl2 x 6 H2O\"\
    ,\n        \"term\": {\n          \"id\": \"CHEBI:86345\",\n          \"label\"\
    : \"magnesium dichloride hexahydrate\"\n        },\n        \"concentration\"\
    : {\n          \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"mediaingredientmech_chebi_term\": {\n          \"id\": \"\
    CHEBI:86345\",\n          \"label\": \"magnesium dichloride hexahydrate\"\n  \
    \      }\n      },\n      {\n        \"preferred_term\": \"CaCl2 x 2 H2O\",\n\
    \        \"term\": {\n          \"id\": \"CHEBI:86158\",\n          \"label\"\
    : \"calcium chloride dihydrate\"\n        },\n        \"concentration\": {\n \
    \         \"value\": \"0.329341\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:86158\"\
    ,\n          \"label\": \"calcium chloride dihydrate\"\n        }\n      },\n\
    \      {\n        \"preferred_term\": \"Yeast extract\",\n        \"concentration\"\
    : {\n          \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"preferred_term\": \"Sodium resazurin\",\n\
    \        \"concentration\": {\n          \"value\": \"0.000499002\",\n       \
    \   \"unit\": \"G_PER_L\"\n        },\n        \"term\": {\n          \"id\":\
    \ \"CHEBI:8806\",\n          \"label\": \"Resazurin\"\n        }\n      },\n \
    \     {\n        \"preferred_term\": \"Na2CO3\",\n        \"term\": {\n      \
    \    \"id\": \"CHEBI:29377\",\n          \"label\": \"sodium carbonate\"\n   \
    \     },\n        \"concentration\": {\n          \"value\": \"1.49701\",\n  \
    \        \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:29377\",\n          \"label\": \"sodium carbonate\"\
    \n        }\n      },\n      {\n        \"preferred_term\": \"Cellobiose\",\n\
    \        \"term\": {\n          \"id\": \"CHEBI:17057\",\n          \"label\"\
    : \"cellobiose\"\n        },\n        \"concentration\": {\n          \"value\"\
    : \"4.99002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:17057\",\n          \"label\": \"cellobiose\"\n\
    \        }\n      },\n      {\n        \"preferred_term\": \"Na2S x 9 H2O\",\n\
    \        \"term\": {\n          \"id\": \"CHEBI:76209\",\n          \"label\"\
    : \"sodium sulfide nonahydrate\"\n        },\n        \"concentration\": {\n \
    \         \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:76209\"\
    ,\n          \"label\": \"sodium sulfide nonahydrate\"\n        }\n      },\n\
    \      {\n        \"preferred_term\": \"HCl\",\n        \"term\": {\n        \
    \  \"id\": \"CHEBI:17883\",\n          \"label\": \"hydrogen chloride\"\n    \
    \    },\n        \"concentration\": {\n          \"value\": \"2.5\",\n       \
    \   \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:17883\",\n          \"label\": \"hydrogen chloride\"\
    \n        }\n      },\n      {\n        \"preferred_term\": \"FeCl2 x 4 H2O\"\
    ,\n        \"term\": {\n          \"id\": \"CHEBI:86249\",\n          \"label\"\
    : \"iron dichloride tetrahydrate\"\n        },\n        \"concentration\": {\n\
    \          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:86249\"\
    ,\n          \"label\": \"iron dichloride tetrahydrate\"\n        }\n      },\n\
    \      {\n        \"preferred_term\": \"ZnCl2\",\n        \"term\": {\n      \
    \    \"id\": \"CHEBI:49976\",\n          \"label\": \"zinc dichloride\"\n    \
    \    },\n        \"concentration\": {\n          \"value\": \"0.07\",\n      \
    \    \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:49976\",\n          \"label\": \"zinc dichloride\"\
    \n        }\n      },\n      {\n        \"preferred_term\": \"MnCl2 x 4 H2O\"\
    ,\n        \"term\": {\n          \"id\": \"CHEBI:86368\",\n          \"label\"\
    : \"manganese(II) chloride tetrahydrate\"\n        },\n        \"concentration\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:86368\"\
    ,\n          \"label\": \"manganese(II) chloride tetrahydrate\"\n        }\n \
    \     },\n      {\n        \"preferred_term\": \"H3BO3\",\n        \"term\": {\n\
    \          \"id\": \"CHEBI:33118\",\n          \"label\": \"boric acid\"\n   \
    \     },\n        \"concentration\": {\n          \"value\": \"0.006\",\n    \
    \      \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:33118\",\n          \"label\": \"boric acid\"\n\
    \        }\n      },\n      {\n        \"preferred_term\": \"CoCl2 x 6 H2O\",\n\
    \        \"term\": {\n          \"id\": \"CHEBI:53503\",\n          \"label\"\
    : \"cobalt chloride hexahydrate\"\n        },\n        \"concentration\": {\n\
    \          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:53503\"\
    ,\n          \"label\": \"cobalt chloride hexahydrate\"\n        }\n      },\n\
    \      {\n        \"preferred_term\": \"CuCl2 x 2 H2O\",\n        \"term\": {\n\
    \          \"id\": \"CHEBI:86318\",\n          \"label\": \"copper(II) chloride\
    \ dihydrate\"\n        },\n        \"concentration\": {\n          \"value\":\
    \ \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:86318\",\n          \"label\": \"copper(II) chloride\
    \ dihydrate\"\n        }\n      },\n      {\n        \"preferred_term\": \"NiCl2\
    \ x 6 H2O\",\n        \"term\": {\n          \"id\": \"CHEBI:34887\",\n      \
    \    \"label\": \"nickel dichloride\"\n        },\n        \"concentration\":\
    \ {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:34887\"\
    ,\n          \"label\": \"nickel dichloride\"\n        }\n      },\n      {\n\
    \        \"preferred_term\": \"Na2MoO4 x 2 H2O\",\n        \"term\": {\n     \
    \     \"id\": \"CHEBI:75213\",\n          \"label\": \"sodium molybdate dihydrate\"\
    \n        },\n        \"concentration\": {\n          \"value\": \"0.036\",\n\
    \          \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:75213\",\n          \"label\": \"sodium molybdate\
    \ dihydrate\"\n        }\n      },\n      {\n        \"preferred_term\": \"Biotin\"\
    ,\n        \"term\": {\n          \"id\": \"CHEBI:15956\",\n          \"label\"\
    : \"biotin\"\n        },\n        \"concentration\": {\n          \"value\": \"\
    0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:15956\",\n          \"label\": \"biotin\"\n   \
    \     }\n      },\n      {\n        \"preferred_term\": \"Folic acid\",\n    \
    \    \"term\": {\n          \"id\": \"CHEBI:27470\",\n          \"label\": \"\
    folic acid\"\n        },\n        \"concentration\": {\n          \"value\": \"\
    0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:27470\",\n          \"label\": \"folic acid\"\n\
    \        }\n      },\n      {\n        \"preferred_term\": \"Pyridoxine hydrochloride\"\
    ,\n        \"term\": {\n          \"id\": \"CHEBI:30961\",\n          \"label\"\
    : \"pyridoxine hydrochloride\"\n        },\n        \"concentration\": {\n   \
    \       \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:30961\"\
    ,\n          \"label\": \"pyridoxine hydrochloride\"\n        }\n      },\n  \
    \    {\n        \"preferred_term\": \"Thiamine HCl\",\n        \"term\": {\n \
    \         \"id\": \"CHEBI:49105\",\n          \"label\": \"thiamine hydrochloride\"\
    \n        },\n        \"concentration\": {\n          \"value\": \"0.05\",\n \
    \         \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:49105\",\n          \"label\": \"thiamine hydrochloride\"\
    \n        }\n      },\n      {\n        \"preferred_term\": \"Riboflavin\",\n\
    \        \"term\": {\n          \"id\": \"CHEBI:17015\",\n          \"label\"\
    : \"riboflavin\"\n        },\n        \"concentration\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:17015\",\n          \"label\": \"riboflavin\"\n\
    \        }\n      },\n      {\n        \"preferred_term\": \"Nicotinic acid\"\
    ,\n        \"term\": {\n          \"id\": \"CHEBI:15940\",\n          \"label\"\
    : \"nicotinic acid\"\n        },\n        \"concentration\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:15940\",\n          \"label\": \"nicotinic acid\"\
    \n        }\n      },\n      {\n        \"preferred_term\": \"Calcium D-(+)-pantothenate\"\
    ,\n        \"concentration\": {\n          \"value\": \"0.05\",\n          \"\
    unit\": \"G_PER_L\"\n        },\n        \"term\": {\n          \"id\": \"CHEBI:31345\"\
    ,\n          \"label\": \"Calcium pantothenate\"\n        }\n      },\n      {\n\
    \        \"preferred_term\": \"Vitamin B12\",\n        \"term\": {\n         \
    \ \"id\": \"CHEBI:176843\",\n          \"label\": \"vitamin B12\"\n        },\n\
    \        \"concentration\": {\n          \"value\": \"0.001\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\": {\n   \
    \       \"id\": \"CHEBI:176843\",\n          \"label\": \"vitamin B12\"\n    \
    \    }\n      },\n      {\n        \"preferred_term\": \"p-Aminobenzoic acid\"\
    ,\n        \"term\": {\n          \"id\": \"CHEBI:30753\",\n          \"label\"\
    : \"4-aminobenzoic acid\"\n        },\n        \"concentration\": {\n        \
    \  \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n       \
    \ \"mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:30753\",\n\
    \          \"label\": \"4-aminobenzoic acid\"\n        }\n      },\n      {\n\
    \        \"preferred_term\": \"(DL)-alpha-Lipoic acid\",\n        \"term\": {\n\
    \          \"id\": \"CHEBI:16494\",\n          \"label\": \"lipoic acid\"\n  \
    \      },\n        \"concentration\": {\n          \"value\": \"0.05\",\n    \
    \      \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:16494\",\n          \"label\": \"lipoic acid\"\n\
    \        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 named variant clause\",\n        \"\
    exact_source_quote\": \"For DSM 9003: Supplement medium with 1.00 g/l Trypticase\
    \ peptone and increase amount\\nof yeast extract to 2.00 g/l.\",\n        \"snapshot_sha256\"\
    : \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\",\n    \
    \    \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"Add the explicit source-only Trypticase\
    \ peptone 1.00 g/L in its variant owner. Do not add it to the base recipe.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"NH4Cl\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:31206\",\n              \"label\": \"ammonium chloride\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.329341\",\n              \"unit\": \"G_PER_L\"\n            },\n           \
    \ \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:31206\"\
    ,\n              \"label\": \"ammonium chloride\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"KH2PO4\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            },\n            \"concentration\": {\n \
    \             \"value\": \"0.329341\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium dihydrogen\
    \ phosphate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"KCl\",\n            \"term\": {\n              \"id\": \"CHEBI:32588\",\n\
    \              \"label\": \"potassium chloride\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"0.329341\",\n             \
    \ \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32588\",\n              \"label\": \"potassium\
    \ chloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"MgCl2 x 6 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86345\"\
    ,\n              \"label\": \"magnesium dichloride hexahydrate\"\n           \
    \ },\n            \"concentration\": {\n              \"value\": \"0.329341\"\
    ,\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86345\",\n              \"label\": \"magnesium\
    \ dichloride hexahydrate\"\n            }\n          },\n          {\n       \
    \     \"preferred_term\": \"CaCl2 x 2 H2O\",\n            \"term\": {\n      \
    \        \"id\": \"CHEBI:86158\",\n              \"label\": \"calcium chloride\
    \ dihydrate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.329341\",\n              \"unit\": \"G_PER_L\"\n           \
    \ },\n            \"mediaingredientmech_chebi_term\": {\n              \"id\"\
    : \"CHEBI:86158\",\n              \"label\": \"calcium chloride dihydrate\"\n\
    \            }\n          },\n          {\n            \"preferred_term\": \"\
    Yeast extract\",\n            \"concentration\": {\n              \"value\": \"\
    0.499002\",\n              \"unit\": \"G_PER_L\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"Sodium resazurin\",\n        \
    \    \"concentration\": {\n              \"value\": \"0.000499002\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"term\": {\n     \
    \         \"id\": \"CHEBI:8806\",\n              \"label\": \"Resazurin\"\n  \
    \          }\n          },\n          {\n            \"preferred_term\": \"Na2CO3\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:29377\",\n         \
    \     \"label\": \"sodium carbonate\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"1.49701\",\n              \"unit\": \"G_PER_L\"\
    \n            },\n            \"mediaingredientmech_chebi_term\": {\n        \
    \      \"id\": \"CHEBI:29377\",\n              \"label\": \"sodium carbonate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Cellobiose\",\n            \"term\": {\n              \"id\": \"CHEBI:17057\"\
    ,\n              \"label\": \"cellobiose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"4.99002\",\n              \"unit\": \"G_PER_L\"\
    \n            },\n            \"mediaingredientmech_chebi_term\": {\n        \
    \      \"id\": \"CHEBI:17057\",\n              \"label\": \"cellobiose\"\n   \
    \         }\n          },\n          {\n            \"preferred_term\": \"Na2S\
    \ x 9 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:76209\",\n\
    \              \"label\": \"sodium sulfide nonahydrate\"\n            },\n   \
    \         \"concentration\": {\n              \"value\": \"0.499002\",\n     \
    \         \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:76209\",\n              \"label\": \"sodium\
    \ sulfide nonahydrate\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"HCl\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:17883\",\n              \"label\": \"hydrogen chloride\"\n         \
    \   },\n            \"concentration\": {\n              \"value\": \"2.5\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:17883\",\n              \"label\": \"hydrogen\
    \ chloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"FeCl2 x 4 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86249\"\
    ,\n              \"label\": \"iron dichloride tetrahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"1.5\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86249\",\n              \"label\": \"iron dichloride\
    \ tetrahydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"ZnCl2\",\n            \"term\": {\n              \"id\": \"CHEBI:49976\",\n\
    \              \"label\": \"zinc dichloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"0.07\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:49976\",\n              \"label\": \"zinc dichloride\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    MnCl2 x 4 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86368\"\
    ,\n              \"label\": \"manganese(II) chloride tetrahydrate\"\n        \
    \    },\n            \"concentration\": {\n              \"value\": \"0.1\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86368\",\n              \"label\": \"manganese(II)\
    \ chloride tetrahydrate\"\n            }\n          },\n          {\n        \
    \    \"preferred_term\": \"H3BO3\",\n            \"term\": {\n              \"\
    id\": \"CHEBI:33118\",\n              \"label\": \"boric acid\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.006\",\n     \
    \         \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:33118\",\n              \"label\": \"boric\
    \ acid\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:53503\"\
    ,\n              \"label\": \"cobalt chloride hexahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.19\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:53503\",\n              \"label\": \"cobalt\
    \ chloride hexahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"CuCl2 x 2 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:86318\",\n              \"label\": \"copper(II) chloride\
    \ dihydrate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.002\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:86318\"\
    ,\n              \"label\": \"copper(II) chloride dihydrate\"\n            }\n\
    \          },\n          {\n            \"preferred_term\": \"NiCl2 x 6 H2O\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:34887\",\n         \
    \     \"label\": \"nickel dichloride\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.024\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:34887\",\n              \"label\": \"nickel dichloride\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Na2MoO4 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75213\"\
    ,\n              \"label\": \"sodium molybdate dihydrate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"0.036\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75213\",\n              \"label\": \"sodium\
    \ molybdate dihydrate\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"Biotin\",\n            \"term\": {\n              \"\
    id\": \"CHEBI:15956\",\n              \"label\": \"biotin\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.02\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:15956\",\n              \"label\": \"biotin\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Folic acid\",\n            \"term\": {\n              \"id\": \"CHEBI:27470\"\
    ,\n              \"label\": \"folic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.02\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:27470\",\n              \"label\": \"folic acid\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Pyridoxine\
    \ hydrochloride\",\n            \"term\": {\n              \"id\": \"CHEBI:30961\"\
    ,\n              \"label\": \"pyridoxine hydrochloride\"\n            },\n   \
    \         \"concentration\": {\n              \"value\": \"0.1\",\n          \
    \    \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:30961\",\n              \"label\": \"pyridoxine\
    \ hydrochloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Thiamine HCl\",\n            \"term\": {\n              \"id\": \"CHEBI:49105\"\
    ,\n              \"label\": \"thiamine hydrochloride\"\n            },\n     \
    \       \"concentration\": {\n              \"value\": \"0.05\",\n           \
    \   \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:49105\",\n              \"label\": \"thiamine\
    \ hydrochloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Riboflavin\",\n            \"term\": {\n              \"id\": \"CHEBI:17015\"\
    ,\n              \"label\": \"riboflavin\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.05\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:17015\",\n              \"label\": \"riboflavin\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Nicotinic\
    \ acid\",\n            \"term\": {\n              \"id\": \"CHEBI:15940\",\n \
    \             \"label\": \"nicotinic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.05\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15940\",\n              \"label\": \"nicotinic acid\"\n\
    \            }\n          },\n          {\n            \"preferred_term\": \"\
    Calcium D-(+)-pantothenate\",\n            \"concentration\": {\n            \
    \  \"value\": \"0.05\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"term\": {\n              \"id\": \"CHEBI:31345\",\n           \
    \   \"label\": \"Calcium pantothenate\"\n            }\n          },\n       \
    \   {\n            \"preferred_term\": \"Vitamin B12\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:176843\",\n              \"label\": \"vitamin\
    \ B12\"\n            },\n            \"concentration\": {\n              \"value\"\
    : \"0.001\",\n              \"unit\": \"G_PER_L\"\n            },\n          \
    \  \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:176843\"\
    ,\n              \"label\": \"vitamin B12\"\n            }\n          },\n   \
    \       {\n            \"preferred_term\": \"p-Aminobenzoic acid\",\n        \
    \    \"term\": {\n              \"id\": \"CHEBI:30753\",\n              \"label\"\
    : \"4-aminobenzoic acid\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.05\",\n              \"unit\": \"G_PER_L\"\n   \
    \         },\n            \"mediaingredientmech_chebi_term\": {\n            \
    \  \"id\": \"CHEBI:30753\",\n              \"label\": \"4-aminobenzoic acid\"\n\
    \            }\n          },\n          {\n            \"preferred_term\": \"\
    (DL)-alpha-Lipoic acid\",\n            \"term\": {\n              \"id\": \"CHEBI:16494\"\
    ,\n              \"label\": \"lipoic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.05\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:16494\",\n              \"label\": \"lipoic acid\"\n   \
    \         }\n          }\n        ],\n        \"decision\": \"add\"\n      }\n\
    \    ]\n  },\n  {\n    \"ingredient_or_context\": \"Unspecified later-stock strengths/volumes\"\
    ,\n    \"field_path\": \"solutions\",\n    \"decision\": \"not_quantified\",\n\
    \    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz516\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium516.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic\
    \ stock\\nsolution prepared under 80% N2 and 20% CO2 gas mixture.\",\n       \
    \ \"snapshot_sha256\": \"5664f7bb278786086f93a82cf7922033a200ab587552b13f0cfc61b07b8c4801\"\
    ,\n        \"parsed_text_sha256\": \"8c5a8a0b0ddb84845650924f43deda7d9ca153be4e5070c9773730d7c8f77831\"\
    \n      }\n    ],\n    \"rationale\": \"The source gives main masses and specific\
    \ listed aliquots, but no separate cellobiose, carbonate or sulfide stock concentration/volume.\
    \ Do not fabricate those or a complete final-volume denominator.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"not_quantified\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerocellum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_6724.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"not_quantified\"\n      }\n    ]\n  }\n]"
findings:
- finding_id: f1
  issue_key: anaerocellum-stock-and-variant-conflation
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock formulations and explicit strain variants are collapsed
  description: All five local layers flatten SL10 and vitamin stocks while retaining
    the same 29 concentrations. The DSM 6724 owner still has cellobiose instead of
    5 g/L starch; the DSM 9003 owner lacks 1 g/L Trypticase and retains base yeast
    extract instead of 2 g/L. The generated target also collapses these variants as
    synonyms/source duplicates. The denoted formulations are materially wrong despite
    topology repairs and ingredients_curated flags.
  target_ids:
  - CultureMech:005874
  field_paths:
  - ingredients
  - solutions
  - derived_media
  - synonyms
  - merged_from
  - data_quality_flags
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - owner-3
  - primary
  - topology-writer
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerocellum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_6724.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml
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
  issue_key: anaerocellum-salt-hydrate-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and sodium resazurin identities are mismatched
  description: NiCl2 x 6 H2O uses anhydrous CHEBI:34887 in both asserted slots. Sodium
    resazurin uses unsalted CHEBI:8806 in the primary slot. Correct canonical labels
    do not make these source forms equivalent.
  target_ids:
  - CultureMech:005874
  field_paths:
  - ingredients[17].term
  - ingredients[17].mediaingredientmech_chebi_term
  - ingredients[6].term
  evidence_ids:
  - record
  - primary
  - chebi34887
  - chebi8806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerocellum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_6724.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml
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
  issue_key: anaerocellum-preparation-stock-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation is omitted or flattened across stages
  description: Only the DSMZ owner preserves main anaerobic handling; its SL10 dissolution/makeup
    is misplaced as main preparation. Other layers omit source procedures, including
    the DSM 6724-specific sterile starch addition.
  target_ids:
  - CultureMech:005874
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - owner-1
  - primary
  - sl10-parent
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerocellum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_6724.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml
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
  issue_key: anaerocellum-catalog-history-qualification
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Catalog metadata and history need bounded qualification
  description: 'KOMODO base and DSM 6724 flags say Aerobic: Yes while DSM 9003 says
    No; these are source catalog values, not experimental validation. Target and KOMODO-derived
    owners retain malformed and naive historical timestamps.'
  target_ids:
  - CultureMech:005874
  field_paths:
  - notes
  - curation_history
  evidence_ids:
  - record
  - catalog-0
  - catalog-1
  - catalog-2
  - history-metadata
  - primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerocellum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_6724.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml
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
  description: Reconcile the base and both explicit variants in maintained owners,
    preserving source stock architecture and concentrations. Reassess status flags
    and regenerate only compatible records; do not repeat topology-only repair as
    ingredient curation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:005874
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerocellum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_6724.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml
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
  description: Resolve exact source-supported hydrate and sodium-salt identifiers
    without guessed replacements or mass conversions. Preserve 24 mg nickel salt per
    SL10 stock and the 0.1% w/v, 0.50 mL resazurin addition.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:005874
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerocellum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_6724.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml
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
  description: Keep main gas/pH/filtration instructions and SL10 1000 mL makeup in
    their separate stages, and preserve the strain-specific starch procedure. Use
    broad P2 for the combined representation defect; do not invent a sterilization
    cycle.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:005874
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerocellum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_6724.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml
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
  description: Preserve exact catalog attribution and append any justified historical
    clarification without silently rewriting old timestamps or treating catalog flags
    as growth evidence.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:005874
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerocellum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_6724.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml
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
- 'mediadive516api: exact public request returned HTTP 503; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'komodoMediaListCanonical: exact public request returned HTTP 403; original access
  time, response bytes and any separately recorded retry are retained. Error bytes
  do not establish formulation or historical absence.'
- 'komodo516detail: exact public request returned HTTP 403; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'komodo516_1detail: exact public request returned HTTP 403; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'komodo516_9003detail: exact public request returned HTTP 403; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'mediadive516apiRetry: exact public request returned HTTP 503; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'komodo516actual: exact public request returned HTTP 403; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'komodo516_1actual: exact public request returned HTTP 403; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'komodo516_9003actual: exact public request returned HTTP 403; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- Both exact main MediaDive 516 attempts returned HTTP 503; exact historical main-response
  correspondence and normalization remain unavailable. The dated report does not substitute
  for raw bytes. All KOMODO detail failures remain preserved; current primary explicitly
  supports the two stated variant changes.
- The listed 1002.5 mL liquid sum and the numerically implied 1002 mL historical denominator
  are distinct and neither is measured final volume. HCl 25% has no stated percent
  basis.
- Only named SL10/vitamin parent subsections transfer. No source strain mention is
  promoted to a taxonomic, assembly or growth claim.
- This scientific assessment preceded formal review validation and saving; their results
  are recorded separately.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-028
- generated-medium
```
