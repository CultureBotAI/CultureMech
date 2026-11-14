# Source and formulation review: anaerobranca_medium (CultureMech:006290)

- Review: 20261021T154611Z-culturemech-006290-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T15:43:28Z
- Finished UTC: 2026-10-21T15:46:11Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

ANAEROBRANCA MEDIUM preserves seven normalized main additions but misrepresents 25 mineral/vitamin stock constituents as undiluted direct-medium concentrations. Restore the two stock recipes and their 5 mL/1 mL doses, reconcile source-specific preparation and nickel hydration, then regenerate from the maintained owners. Exact historical main-provider correspondence remains unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 271; batch 028 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-seven task batches contain 270 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 273 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006290 | data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml | generated | anaerobranca_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006290 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006290 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch028/271/strict.tsv |
| validate-terms | passed | True | CultureMech:006290 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006290 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006290 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive685api | unavailable | True | CultureMech:006290 | mediadive685api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodoMediaListCanonical | unavailable | False | CultureMech:006290 | komodoMediaListCanonical: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodo685detail | unavailable | False | CultureMech:006290 | komodo685detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: mediadive685apiRetry | unavailable | True | CultureMech:006290 | mediadive685apiRetry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodo685actual | unavailable | False | CultureMech:006290 | komodo685actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006290.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:006290.

31 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 31/32 primary and 30/32 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 32: primary 96.88%; secondary 93.75%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006290.

25 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Generated target and two maintained source contributors

identity: supported. Targets: CultureMech:006290.

CultureMech:006290 derives from KOMODO 685 and DSMZ 685 CultureMech:001822. The exact catalog link and primary title support the shared source identity. All three local layers have the same 32 ingredient amounts; DSMZ alone retains the main and mineral preparation. Reciprocal SOURCE_DUPLICATE owner links are internally coherent but do not certify the flattened formula.

### Main masses and two separate stock recipes

consistency: concern. Targets: CultureMech:006290.

The source lists seven direct masses, 5 mL mineral stock, 1 mL vitamin stock and 1000 mL water. All 15 mineral and 10 vitamin constituents instead appear at their stock-strength g/L in every local layer. Main stored values are numerically compatible, within their displayed rounding, with dividing the source masses by 1.006 L; the 1006 mL sum of named liquid inputs is not measured final volume and excludes unspecified later-stock volumes. The unavailable main API prevents exact independent confirmation of that historical normalization.

### Main anaerobic procedure and stock-specific pH

completeness: concern. Targets: CultureMech:006290.

The DSMZ owner retains main pH 8.5, 100% N2, 30–45 min sparging, autoclaving and the sterile later additions. It also retains the mineral stock pH 6.5 then 7.0 with KOH, but incorrectly places that procedure among main-medium steps. The generated target and KOMODO owner omit both procedures. Preserve fumarate/vitamin filtration, source-specific stock handling and stock pH; the primary gives no autoclave temperature or duration to invent.

### Medium class, physical state and biological claims

scope: supported. Targets: CultureMech:006290.

COMPLEX/UNDEFINED is consistent with yeast extract and LIQUID with the collection formulation. Bacterial filing and generic microbial-cultivation application are catalog scope, not experimental growth evidence. No named organism/strain, incubation optimum, DOI or PMID is asserted. The KOMODO Aerobic: Yes note conflicts with the primary anaerobic procedure when read as a cultivation instruction and requires attribution.

### Source-specific hydrate and vitamin forms

grounding: concern. Targets: CultureMech:006290.

The mineral recipe explicitly specifies NiCl2 x 6 H2O, while both asserted CHEBI slots use CHEBI:34887 with formula Cl2Ni. Other explicit source hydrate forms were compared to their captured structures. Calcium D-(+)-pantothenate is consistent with CHEBI:31345 stereochemistry; the DL-lipoic source is not contradicted by the nonstereospecific CHEBI:16494 structure. Generic vitamin B12 remains generic. No replacement CURIE or unsupported stereochemical conversion is proposed.

### Current transform behavior and historical attribution

provenance: concern. Targets: CultureMech:006290.

Current MediaDive parsing separates primary stock additions from direct compounds, although preparation parsing still concatenates steps from all solutions. Current formulation merging requires scientific-field compatibility; ingredient-set equality alone is insufficient. The inspected DSMZ resolver copies ingredient/solution composition without copying preparation and emits naive timestamps. These are current implementation observations, not proof of the precise historical execution. Correct maintained owners and preserve source distinctions before regeneration.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006290.

47 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "KH2PO4 0.50 g",
    "field_path": "ingredients[0].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.497018",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main table; exact named row",
        "exact_source_quote": "KH2PO4 0.50 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "The primary verifies the source batch mass, but not the final-volume denominator of the stored g/L. Preserve the source amount and preparation stage; do not silently endorse or renormalize the historical rounded value.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.497018",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.497018",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.497018",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 0.5 g / 1.006 L = 0.4970178926441351888667992048 g/L; stored 0.497018 g/L. Displayed rounding is retained. The 1006 mL sum is not a measured final volume."
  },
  {
    "ingredient_or_context": "Na2HPO4 x 2 H2O 3.90 g",
    "field_path": "ingredients[1].concentration",
    "decision": "unsupported",
    "local": {
      "value": "3.87674",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main table; exact named row",
        "exact_source_quote": "Na2HPO4 x 2 H2O 3.90 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "The primary verifies the source batch mass, but not the final-volume denominator of the stored g/L. Preserve the source amount and preparation stage; do not silently endorse or renormalize the historical rounded value.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.87674",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.87674",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.87674",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 3.9 g / 1.006 L = 3.876739562624254473161033797 g/L; stored 3.87674 g/L. Displayed rounding is retained. The 1006 mL sum is not a measured final volume."
  },
  {
    "ingredient_or_context": "KCl 0.50 g",
    "field_path": "ingredients[2].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.497018",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main table; exact named row",
        "exact_source_quote": "KCl 0.50 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "The primary verifies the source batch mass, but not the final-volume denominator of the stored g/L. Preserve the source amount and preparation stage; do not silently endorse or renormalize the historical rounded value.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.497018",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.497018",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.497018",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 0.5 g / 1.006 L = 0.4970178926441351888667992048 g/L; stored 0.497018 g/L. Displayed rounding is retained. The 1006 mL sum is not a measured final volume."
  },
  {
    "ingredient_or_context": "Yeast extract 5.00 g",
    "field_path": "ingredients[3].concentration",
    "decision": "unsupported",
    "local": {
      "value": "4.97018",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main table; exact named row",
        "exact_source_quote": "Yeast extract 5.00 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "The primary verifies the source batch mass, but not the final-volume denominator of the stored g/L. Preserve the source amount and preparation stage; do not silently endorse or renormalize the historical rounded value.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "4.97018",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "4.97018",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "4.97018",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 5 g / 1.006 L = 4.970178926441351888667992048 g/L; stored 4.97018 g/L. Displayed rounding is retained. The 1006 mL sum is not a measured final volume."
  },
  {
    "ingredient_or_context": "Na2-fumarate 1.50 g",
    "field_path": "ingredients[4].concentration",
    "decision": "unsupported",
    "local": {
      "value": "1.49105",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main table; exact named row",
        "exact_source_quote": "Na2-fumarate 1.50 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "The primary verifies the source batch mass, but not the final-volume denominator of the stored g/L. Preserve the source amount and preparation stage; do not silently endorse or renormalize the historical rounded value.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.49105",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.49105",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.49105",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 1.5 g / 1.006 L = 1.491053677932405566600397614 g/L; stored 1.49105 g/L. Displayed rounding is retained. The 1006 mL sum is not a measured final volume."
  },
  {
    "ingredient_or_context": "L-Cysteine HCl x H2O 0.15 g",
    "field_path": "ingredients[5].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.149105",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main table; exact named row",
        "exact_source_quote": "L-Cysteine HCl x H2O 0.15 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "The primary verifies the source batch mass, but not the final-volume denominator of the stored g/L. Preserve the source amount and preparation stage; do not silently endorse or renormalize the historical rounded value.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.149105",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.149105",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.149105",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 0.15 g / 1.006 L = 0.1491053677932405566600397614 g/L; stored 0.149105 g/L. Displayed rounding is retained. The 1006 mL sum is not a measured final volume."
  },
  {
    "ingredient_or_context": "Na2S x 9 H2O 0.15 g",
    "field_path": "ingredients[6].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.149105",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main table; exact named row",
        "exact_source_quote": "Na2S x 9 H2O 0.15 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "The primary verifies the source batch mass, but not the final-volume denominator of the stored g/L. Preserve the source amount and preparation stage; do not silently endorse or renormalize the historical rounded value.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.149105",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.149105",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.149105",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "Conditional comparison only: 0.15 g / 1.006 L = 0.1491053677932405566600397614 g/L; stored 0.149105 g/L. Displayed rounding is retained. The 1006 mL sum is not a measured final volume."
  },
  {
    "ingredient_or_context": "mineral stock: Nitrilotriacetic acid 1.50 g",
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "local": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "Nitrilotriacetic acid 1.50 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
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
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 1.5 g/L × 0.005 L would deliver 0.0075 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: MgSO4 x 7 H2O 3.00 g",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "local": {
      "value": "3",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "MgSO4 x 7 H2O 3.00 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 3 g/L × 0.005 L would deliver 0.015 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: MnSO4 x H2O 0.50 g",
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "MnSO4 x H2O 0.50 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.5 g/L × 0.005 L would deliver 0.0025 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: NaCl 1.00 g",
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "NaCl 1.00 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 1 g/L × 0.005 L would deliver 0.005 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: FeSO4 x 7 H2O 0.10 g",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "FeSO4 x 7 H2O 0.10 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.1 g/L × 0.005 L would deliver 0.0005 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: CoSO4 x 7 H2O 0.18 g",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "local": {
      "value": "0.18",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "CoSO4 x 7 H2O 0.18 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.18 g/L × 0.005 L would deliver 0.00090 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: CaCl2 x 2 H2O 0.10 g",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "CaCl2 x 2 H2O 0.10 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
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
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.1 g/L × 0.005 L would deliver 0.0005 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: ZnSO4 x 7 H2O 0.18 g",
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "local": {
      "value": "0.18",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "ZnSO4 x 7 H2O 0.18 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.18 g/L × 0.005 L would deliver 0.00090 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: CuSO4 x 5 H2O 0.01 g",
    "field_path": "ingredients[15].concentration",
    "decision": "correct",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "CuSO4 x 5 H2O 0.01 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.01 g/L × 0.005 L would deliver 0.00005 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: AlK(SO4)2 x 12 H2O 0.02 g",
    "field_path": "ingredients[16].concentration",
    "decision": "correct",
    "local": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "AlK(SO4)2 x 12 H2O 0.02 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.02 g/L × 0.005 L would deliver 0.00010 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: H3BO3 0.01 g",
    "field_path": "ingredients[17].concentration",
    "decision": "correct",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "H3BO3 0.01 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
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
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.01 g/L × 0.005 L would deliver 0.00005 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: Na2MoO4 x 2 H2O 0.01 g",
    "field_path": "ingredients[18].concentration",
    "decision": "correct",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.01 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.01 g/L × 0.005 L would deliver 0.00005 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: NiCl2 x 6 H2O 0.03 g",
    "field_path": "ingredients[19].concentration",
    "decision": "correct",
    "local": {
      "value": "0.03",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "NiCl2 x 6 H2O 0.03 g",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.03 g/L × 0.005 L would deliver 0.00015 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: Na2SeO3 x 5 H2O 0.30 mg",
    "field_path": "ingredients[20].concentration",
    "decision": "correct",
    "local": {
      "value": "0.0003",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "Na2SeO3 x 5 H2O 0.30 mg",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.0003 g/L × 0.005 L would deliver 0.0000015 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "mineral stock: Na2WO4 x 2 H2O 0.40 mg",
    "field_path": "ingredients[21].concentration",
    "decision": "correct",
    "local": {
      "value": "0.0004",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table; exact named row",
        "exact_source_quote": "Na2WO4 x 2 H2O 0.40 mg",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.0004 g/L × 0.005 L would deliver 0.0000020 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "vitamin stock: Biotin 20.00 mg",
    "field_path": "ingredients[22].concentration",
    "decision": "correct",
    "local": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) stock table; exact named row",
        "exact_source_quote": "Biotin 20.00 mg",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.02 g/L × 0.001 L would deliver 0.00002 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "vitamin stock: Folic acid 20.00 mg",
    "field_path": "ingredients[23].concentration",
    "decision": "correct",
    "local": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) stock table; exact named row",
        "exact_source_quote": "Folic acid 20.00 mg",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.02 g/L × 0.001 L would deliver 0.00002 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "vitamin stock: Pyridoxine hydrochloride 100.00 mg",
    "field_path": "ingredients[24].concentration",
    "decision": "correct",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) stock table; exact named row",
        "exact_source_quote": "Pyridoxine hydrochloride 100.00 mg",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.1 g/L × 0.001 L would deliver 0.0001 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "vitamin stock: Thiamine HCl 50.00 mg",
    "field_path": "ingredients[25].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) stock table; exact named row",
        "exact_source_quote": "Thiamine HCl 50.00 mg",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
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
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "vitamin stock: Riboflavin 50.00 mg",
    "field_path": "ingredients[26].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) stock table; exact named row",
        "exact_source_quote": "Riboflavin 50.00 mg",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "vitamin stock: Nicotinic acid 50.00 mg",
    "field_path": "ingredients[27].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) stock table; exact named row",
        "exact_source_quote": "Nicotinic acid 50.00 mg",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
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
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "vitamin stock: Calcium D-(+)-pantothenate 50.00 mg",
    "field_path": "ingredients[28].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) stock table; exact named row",
        "exact_source_quote": "Calcium D-(+)-pantothenate 50.00 mg",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
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
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "vitamin stock: Vitamin B12 1.00 mg",
    "field_path": "ingredients[29].concentration",
    "decision": "correct",
    "local": {
      "value": "0.001",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) stock table; exact named row",
        "exact_source_quote": "Vitamin B12 1.00 mg",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.001 g/L × 0.001 L would deliver 0.000001 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "vitamin stock: p-Aminobenzoic acid 50.00 mg",
    "field_path": "ingredients[30].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) stock table; exact named row",
        "exact_source_quote": "p-Aminobenzoic acid 50.00 mg",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "vitamin stock: (DL)-alpha-Lipoic acid 50.00 mg",
    "field_path": "ingredients[31].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 2 Wolin vitamin (10x) stock table; exact named row",
        "exact_source_quote": "(DL)-alpha-Lipoic acid 50.00 mg",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "This amount belongs to the separate stock recipe, not an undiluted direct-medium concentration. Restore the stock composition, original unit and receiving-medium aliquot. No final-medium g/L is established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the exact stock endpoint’s nominal 1 L volume declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per listed medium batch. This is conditional stock arithmetic, not a measured final-medium concentration."
  },
  {
    "ingredient_or_context": "Mineral stock dose",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main table",
        "exact_source_quote": "Modified Wolin's mineral solution 5.00 ml",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "Represent this explicit source-only dose or solvent quantity in its own stage. Existing preparation container values are retained as inspected; their presence is not a water or aliquot claim. A listed water amount does not establish measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Vitamin stock dose",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main table",
        "exact_source_quote": "Wolin's vitamin solution (10x) 1.00 ml",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "Represent this explicit source-only dose or solvent quantity in its own stage. Existing preparation container values are retained as inspected; their presence is not a water or aliquot claim. A listed water amount does not establish measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
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
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main table",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "Represent this explicit source-only dose or solvent quantity in its own stage. Existing preparation container values are retained as inspected; their presence is not a water or aliquot claim. A listed water amount does not establish measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust pH of complete medium to 8.5, if necessary."
          },
          {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Mineral stock water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 Modified Wolin mineral stock table",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "Represent this explicit source-only dose or solvent quantity in its own stage. Existing preparation container values are retained as inspected; their presence is not a water or aliquot claim. A listed water amount does not establish measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Vitamin stock water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 2 Wolin vitamin stock table",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "Represent this explicit source-only dose or solvent quantity in its own stage. Existing preparation container values are retained as inspected; their presence is not a water or aliquot claim. A listed water amount does not establish measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main recorded pH",
    "field_path": "ph_value",
    "decision": "evidence_only",
    "local": 8.5,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "adjust pH to 8.5",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "All three layers retain pH 8.5 without matching attached claim evidence.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 8.5,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "ph_value",
        "stored": 8.5,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "ph_value",
        "stored": 8.5,
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Main initial pH",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "adjust pH to 8.5",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "DSMZ alone retains this literal numeric context. Attach evidence to the main procedure; restore stock scope for mineral endpoints. The target and KOMODO require the source-specific procedure.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust pH of complete medium to 8.5, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Main N2 fraction",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "100% N2 gas for 30 - 45 min",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "DSMZ alone retains this literal numeric context. Attach evidence to the main procedure; restore stock scope for mineral endpoints. The target and KOMODO require the source-specific procedure.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust pH of complete medium to 8.5, if necessary.",
        "decision": "evidence_only"
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
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "30 - 45 min",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "DSMZ alone retains this literal numeric context. Attach evidence to the main procedure; restore stock scope for mineral endpoints. The target and KOMODO require the source-specific procedure.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust pH of complete medium to 8.5, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Later-stock N2 fraction",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "solutions prepared under 100% N2 gas.",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "DSMZ alone retains this literal numeric context. Attach evidence to the main procedure; restore stock scope for mineral endpoints. The target and KOMODO require the source-specific procedure.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust pH of complete medium to 8.5, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Main final pH",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 main preparation",
        "exact_source_quote": "Adjust pH of complete medium to 8.5",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "DSMZ alone retains this literal numeric context. Attach evidence to the main procedure; restore stock scope for mineral endpoints. The target and KOMODO require the source-specific procedure.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust pH of complete medium to 8.5, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Mineral initial pH",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 mineral stock procedure",
        "exact_source_quote": "adjust pH to 6.5 with KOH",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "DSMZ alone retains this literal numeric context. Attach evidence to the main procedure; restore stock scope for mineral endpoints. The target and KOMODO require the source-specific procedure.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Mineral final pH",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 mineral stock procedure",
        "exact_source_quote": "final to pH 7.0 with KOH.",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "DSMZ alone retains this literal numeric context. Attach evidence to the main procedure; restore stock scope for mineral endpoints. The target and KOMODO require the source-specific procedure.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Unquantified mineral KOH titrant",
    "field_path": "solutions",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 mineral titration",
        "exact_source_quote": "final to pH 7.0 with KOH.",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "KOH has no stated dose. Fumarate, cysteine and sulfide have stated main masses but no stock strength or aliquot volume; the vitamin aliquot is separately specified in the main table. Preserve these limits without inventing a concentration, dose or final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Unspecified later-stock strengths and aliquot volumes",
    "field_path": "solutions",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz685",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf",
        "source_locator": "PDF page 1 later additions",
        "exact_source_quote": "After sterilization add fumarate, vitamins, cysteine and sulfide from sterile anoxic stock\nsolutions prepared under 100% N2 gas.",
        "snapshot_sha256": "711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32",
        "parsed_text_sha256": "e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d"
      }
    ],
    "rationale": "KOH has no stated dose. Fumarate, cysteine and sulfide have stated main masses but no stock strength or aliquot volume; the vitamin aliquot is separately specified in the main table. Preserve these limits without inventing a concentration, dose or final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust pH of complete medium to 8.5, if necessary.",
        "decision": "not_quantified"
      }
    ]
  }
]

## Findings

### f1: Stock-strength constituents replace the intended aliquots

blocker / open / confirmed; issue key: anaerobranca-stock-formulation-flattening.

All three layers list the 15 mineral and 10 vitamin constituents as direct g/L at stock strength, while omitting the 5 mL mineral and 1 mL vitamin additions. This materially changes the denoted medium. The seven historical main g/L values also lack an independently established final-volume basis; source batch masses remain available and must be preserved.

### f2: Nickel hexahydrate is grounded to anhydrous nickel dichloride

major / open / confirmed; issue key: anaerobranca-nickel-hydrate.

The source mineral stock specifies NiCl2 x 6 H2O, 0.03 g, but every local layer asserts CHEBI:34887, whose formula is Cl2Ni. The secondary CHEBI key repeats the same form mismatch.

### f3: Anaerobic preparation is missing or assigned to the wrong stage

major / open / confirmed; issue key: anaerobranca-preparation-stage-loss.

The target and KOMODO owner omit the source anaerobic and sterilization sequence. The DSMZ owner retains that sequence but stores the mineral pH 6.5 to 7.0 titration as main preparation. Mis-scoping this stock titration can contradict main pH 8.5. This is a combined preparation representation defect; no unprinted sterilization cycle is inferred.

### f4: Catalog aerobic flag and historical timestamp limitations need qualification

minor / open / confirmed; issue key: anaerobranca-catalog-history-qualification.

The target and KOMODO owner retain Aerobic: Yes from the catalog, while the primary specifies anoxic preparation. Both also retain one malformed timestamp and one timezone-naive timestamp. Catalog attribution and append-only clarification are needed; neither a physiological growth claim nor a fabricated timestamp is warranted.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the two named stocks and source doses in each maintained owner, retain the seven original main masses and unresolved final-volume basis, then regenerate compatible source-specific records. Do not convert nominal stock delivery into an asserted final-medium concentration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve a verified nickel hexahydrate identity for both asserted slots, retaining the 0.03 g source stock mass and separate 5 mL stock dose. Do not invent a replacement identifier or infer an anhydrous mass conversion.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the existing DSMZ main instructions with attached evidence, move mineral titration into the stock procedure, and reconcile the other owner before regeneration. Keep 100% N2, 30–45 min, main pH 8.5 and source filtration qualifiers distinct.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Qualify the catalog flag as source metadata and append a bounded provenance clarification. Preserve old history and do not guess timezone or malformed timestamp digits.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/anaerobranca_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch028/271/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch028/271/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml:1:id: CultureMech:006290<br>./data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml:1:id: CultureMech:006290<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch028/source-preflight-bound/271/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 44 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch028/source-preflight-bound/271/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| dsmz685 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf; Complete DSMZ 685 PDF pages 1–2; main table, preparation, mineral and vitamin tables | supports | Both PDF pages and extracted text were read. Seven direct masses, two stock aliquots and 1000 mL main water are distinct from the two stock compositions; no measured final-medium volume is stated. |
| mineral-parent | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf; Modified Wolin mineral solution subsection only | supports | The complete parent was read, but only the named mineral recipe and its pH procedure transfer. Parent basal medium, other stocks, gas pressure and organism instructions do not transfer. |
| vitamin-parent | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf; Wolin vitamin solution (10x) subsection only | supports | Only the named ten-vitamin stock transfers. Parent basal medium, SL10, iron stock and organism-specific instructions are excluded. |
| solution241 | https://mediadive.dsmz.de/rest/solution/241; $.data.id, name, volume, recipe and steps | supports | Exact named stock endpoint was read in full. It declares volume 1000 and preserves the stock recipe. This supports a nominal 1 L stock basis; it does not establish the main-medium final volume or the inaccessible historical main API bytes. |
| solution5980 | https://mediadive.dsmz.de/rest/solution/5980; $.data.id, name, volume, recipe and steps | supports | Exact named stock endpoint was read in full. It declares volume 1000 and preserves the stock recipe. This supports a nominal 1 L stock basis; it does not establish the main-medium final volume or the inaccessible historical main API bytes. |
| komodo-catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact href MediaInfo=685; exact raw table header | context_only | KOMODO 685 identifies the medium, links DSMZ 685, lists pH 8.5 and marks Is Aerobic true. This is attributed catalog metadata, not proof of aerobic cultivation. |
| mediadive685api-attempt | https://mediadive.dsmz.de/rest/medium/685; Preserved exact public retrieval result | context_only | mediadive685api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodoMediaListCanonical-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaList; Preserved exact public retrieval result | context_only | komodoMediaListCanonical: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodo685detail-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaInfo=685; Preserved exact public retrieval result | context_only | komodo685detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| mediadive685apiRetry-attempt | https://mediadive.dsmz.de/rest/medium/685; Preserved exact public retrieval result | context_only | mediadive685apiRetry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodo685actual-attempt | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=685; Preserved exact public retrieval result | context_only | komodo685actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| historical-report | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/anaerobranca_medium.yaml.md; Dated report header and every source recipe/step excerpt | context_only | The October 7 derivative report retains historical source hash/time and rounded g_l values. Its unchanged-result hash matches the current DSMZ owner. The report is not an independently recovered raw API response; no fresh access time or exact historical-byte validation is inferred. |
| chebi115156 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_115156; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:115156 resolves to disodium fumarate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91258 resolves to disodium hydrogenphosphate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:115156": [{"label": "Na2-fumarate", "match_type": "preferred_term", "identifier": "CHEBI:115156", "preferred_term": "Na2-fumarate", "ontology_id": "CHEBI:115156", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91258": [{"label": "Na2HPO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml; data/normalized_yaml/bacterial/anaerobranca_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.867025"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.867025"}]}, {"input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml", "events": 7, "timestamp_issues": []}] |
| resolver | src/culturemech/enrich/dsmz_resolver.py; _build_dsmz_index, merge_composition and _add_enrichment_metadata | context_only | Current resolver methods read: composition copying excludes preparation; enrichment uses datetime.now().isoformat(). No resolver execution or reconstruction of a historical run. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch028/271/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch028/271/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- mediadive685api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodoMediaListCanonical: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodo685detail: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- mediadive685apiRetry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodo685actual: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- Exact main MediaDive 685 access failed twice with HTTP 503. Independent historical main-response correspondence and its normalization basis remain unavailable; the dated local report is derivative context only. Available DSMZ primary and named stock endpoints support the scoped findings.
- The parent DSMZ 141 and 120 sources are used only for the explicitly referenced stocks. Their other media, organisms and gas/pressure conditions do not transfer.
- The primary lists stock water and titration; conditional delivered masses use the provider’s declared nominal 1 L stock bases. No measured final stock or medium volume is asserted.
- This scientific assessment preceded formal review validation and saving; their results are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T154611Z-culturemech-006290-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerobranca_medium (CultureMech:006290)'
started_at: '2026-10-21T15:43:28Z'
finished_at: '2026-10-21T15:46:11Z'
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
summary: ANAEROBRANCA MEDIUM preserves seven normalized main additions but misrepresents
  25 mineral/vitamin stock constituents as undiluted direct-medium concentrations.
  Restore the two stock recipes and their 5 mL/1 mL doses, reconcile source-specific
  preparation and nickel hydration, then regenerate from the maintained owners. Exact
  historical main-provider correspondence remains unavailable.
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
  - path: data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml
    sha256: daf8599e8f233f6bfdba954c31b7e606bb9a2e90aeefa37dacc87b9a1a93060d
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml
    sha256: 17b320ded470737fdd93425a8c27cff829537f35452e34988cc7079624df4e98
    role: context
  - path: data/normalized_yaml/bacterial/anaerobranca_medium.yaml
    sha256: 63eb9661b8f533494fdc50f0ab6a2328db1bad70042358177217adebf0b4a673
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/anaerobranca_medium.yaml.md
    sha256: 461bfe61f9ff09bd1e5041d80f184f791be552f9f6110bc1aaa643276a2540a2
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
  selection: Task review 271; batch 028 item 1 of 10, selected in Python lexicographic
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
  - CultureMech:006290
targets:
- target_id: CultureMech:006290
  path: data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml
  label: anaerobranca_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobranca_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch028/271/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch028/271/strict.tsv"
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006290
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
  - CultureMech:006290
- check_id: mediadive685api-source-access
  name: 'Exact source content access: mediadive685api'
  required: true
  status: unavailable
  summary: 'mediadive685api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - mediadive685api-attempt
- check_id: komodoMediaListCanonical-source-access
  name: 'Exact source content access: komodoMediaListCanonical'
  required: false
  status: unavailable
  summary: 'komodoMediaListCanonical: exact public request returned HTTP 403; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - komodoMediaListCanonical-attempt
- check_id: komodo685detail-source-access
  name: 'Exact source content access: komodo685detail'
  required: false
  status: unavailable
  summary: 'komodo685detail: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - komodo685detail-attempt
- check_id: mediadive685apiRetry-source-access
  name: 'Exact source content access: mediadive685apiRetry'
  required: true
  status: unavailable
  summary: 'mediadive685apiRetry: exact public request returned HTTP 503; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - mediadive685apiRetry-attempt
- check_id: komodo685actual-source-access
  name: 'Exact source content access: komodo685actual'
  required: false
  status: unavailable
  summary: 'komodo685actual: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - komodo685actual-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T15:46:09Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:46:09Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerobranca_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:46:09Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:43:37.647864Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch028/271/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T15:43:38.912722Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch028/271/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:43:40.955594Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:43:42.123981Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T15:46:09Z'
  support: supports
  summary: './data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml:1:id: CultureMech:006290

    ./data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml:1:id: CultureMech:006290

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/source-preflight-bound/271/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T15:46:09Z'
  support: supports
  summary: 44 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 3e0a6f18bdf35c6d39d010b51dee9c1bcb6a29b815969bfe34ed6c80f0d8ad4d
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/source-preflight-bound/271/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T15:46:09Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: 1393833db2920346a16aa8e517363272b03ceb730fa47a77436fd7021b7388b7
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T15:46:09Z'
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
  accessed_at: '2026-10-21T15:46:09Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T15:46:09Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: dsmz685
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf
  locator: Complete DSMZ 685 PDF pages 1–2; main table, preparation, mineral and vitamin
    tables
  accessed_at: '2026-10-21T15:16:37.495024Z'
  support: supports
  summary: Both PDF pages and extracted text were read. Seven direct masses, two stock
    aliquots and 1000 mL main water are distinct from the two stock compositions;
    no measured final-medium volume is stated.
  snapshot_sha256: 711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32
- evidence_id: mineral-parent
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf
  locator: Modified Wolin mineral solution subsection only
  accessed_at: '2026-10-21T10:13:12.306566Z'
  support: supports
  summary: The complete parent was read, but only the named mineral recipe and its
    pH procedure transfer. Parent basal medium, other stocks, gas pressure and organism
    instructions do not transfer.
  snapshot_sha256: 8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8
- evidence_id: vitamin-parent
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf
  locator: Wolin vitamin solution (10x) subsection only
  accessed_at: '2026-10-21T13:16:27.298931Z'
  support: supports
  summary: Only the named ten-vitamin stock transfers. Parent basal medium, SL10,
    iron stock and organism-specific instructions are excluded.
  snapshot_sha256: e1f85e4a546abc825218226bbb18d78bd9c054b7e11399aa7161ad259a3b663f
- evidence_id: solution241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/241
  locator: $.data.id, name, volume, recipe and steps
  accessed_at: '2026-10-21T10:37:16.846684Z'
  support: supports
  summary: Exact named stock endpoint was read in full. It declares volume 1000 and
    preserves the stock recipe. This supports a nominal 1 L stock basis; it does not
    establish the main-medium final volume or the inaccessible historical main API
    bytes.
  snapshot_sha256: 50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d
- evidence_id: solution5980
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5980
  locator: $.data.id, name, volume, recipe and steps
  accessed_at: '2026-10-21T11:03:05.362213Z'
  support: supports
  summary: Exact named stock endpoint was read in full. It declares volume 1000 and
    preserves the stock recipe. This supports a nominal 1 L stock basis; it does not
    establish the main-medium final volume or the inaccessible historical main API
    bytes.
  snapshot_sha256: 2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c
- evidence_id: komodo-catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact href MediaInfo=685; exact raw table header
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: context_only
  summary: KOMODO 685 identifies the medium, links DSMZ 685, lists pH 8.5 and marks
    Is Aerobic true. This is attributed catalog metadata, not proof of aerobic cultivation.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=685'\
    \ >685</a></TD>\n\t\t\t\t\t<TD>ANAEROBRANCA medium</TD>\n\t\t\t\t\t<TD> 8.5</TD>\n\
    \t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n<TD><a\
    \ href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: mediadive685api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/685
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.853337Z'
  support: context_only
  summary: 'mediadive685api: exact public request returned HTTP 503; original access
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
- evidence_id: komodo685detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaInfo=685
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.468234Z'
  support: context_only
  summary: 'komodo685detail: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 275e3fb178557113f89bece0ad2fb501df2f45e435470ec0601b0bf9b2a7543b
- evidence_id: mediadive685apiRetry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/685
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:19:00.568085Z'
  support: context_only
  summary: 'mediadive685apiRetry: exact public request returned HTTP 503; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo685actual-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=685
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:19:00.220656Z'
  support: context_only
  summary: 'komodo685actual: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 34045c9eb52bc92fb7b332d39f7806011e76300238404586991367834dd994dc
- evidence_id: historical-report
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/anaerobranca_medium.yaml.md
  locator: Dated report header and every source recipe/step excerpt
  accessed_at: '2026-10-21T15:46:09Z'
  support: context_only
  summary: The October 7 derivative report retains historical source hash/time and
    rounded g_l values. Its unchanged-result hash matches the current DSMZ owner.
    The report is not an independently recovered raw API response; no fresh access
    time or exact historical-byte validation is inferred.
  snapshot_sha256: 461bfe61f9ff09bd1e5041d80f184f791be552f9f6110bc1aaa643276a2540a2
- evidence_id: chebi115156
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_115156
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T15:16:38.281331Z'
  support: supports
  summary: CHEBI:115156 resolves to disodium fumarate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 5ff8efa80c6b0a7a4a764e6c2b95eaf39e97073440e33b02d6dd2b3affd79452
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
- evidence_id: chebi91248
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:32.136441Z'
  support: supports
  summary: CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: chebi91258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:28:27.054091Z'
  support: supports
  summary: CHEBI:91258 resolves to disodium hydrogenphosphate dihydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: f6c74e6e0b876aadf2fe47494521d320abb79244773bf4c44da7b288b1e27319
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T15:46:09Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:115156":
    [{"label": "Na2-fumarate", "match_type": "preferred_term", "identifier": "CHEBI:115156",
    "preferred_term": "Na2-fumarate", "ontology_id": "CHEBI:115156", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term":
    "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED",
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
    "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier":
    "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label":
    "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label":
    "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753",
    "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride",
    "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term":
    "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O",
    "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label":
    "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id":
    "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105":
    [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939":
    [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209":
    [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label":
    "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465",
    "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term":
    "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id":
    "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91258":
    [{"label": "Na2HPO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91258",
    "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml;
    data/normalized_yaml/bacterial/anaerobranca_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T15:46:09Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:59.867025"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:59.867025"}]}, {"input": "data/normalized_yaml/bacterial/anaerobranca_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: _build_dsmz_index, merge_composition and _add_enrichment_metadata
  accessed_at: '2026-10-21T15:46:09Z'
  support: context_only
  summary: 'Current resolver methods read: composition copying excludes preparation;
    enrichment uses datetime.now().isoformat(). No resolver execution or reconstruction
    of a historical run.'
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/271/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T15:46:09Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 4b2cb7741fea78bffa788cdafe2a73ed6d47c8e3c3c5cce28cffdc318685d8dd
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/271/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T15:46:09Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: 21fd89fe2d521982a421d956a0f61d484d7d8749e756f611e5628c99760c3fea
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '31 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 31/32
    primary and 30/32 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi115156
  - chebi131361
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi176843
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31345
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi44557
  - chebi49105
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi86158
  - chebi86364
  - chebi86465
  - chebi91244
  - chebi91248
  - chebi91258
  details: 'Instance coverage on a 0–100 percent scale, denominator 32: primary 96.88%;
    secondary 93.75%. These are linkage metrics, not correctness scores. Missing optional
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
  - CultureMech:006290
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: identity
  area: identity
  topic: Generated target and two maintained source contributors
  outcome: supported
  summary: CultureMech:006290 derives from KOMODO 685 and DSMZ 685 CultureMech:001822.
    The exact catalog link and primary title support the shared source identity. All
    three local layers have the same 32 ingredient amounts; DSMZ alone retains the
    main and mineral preparation. Reciprocal SOURCE_DUPLICATE owner links are internally
    coherent but do not certify the flattened formula.
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - id-search
  - komodo-catalog
  - dsmz685
- assessment_id: formulation
  area: consistency
  topic: Main masses and two separate stock recipes
  outcome: concern
  summary: The source lists seven direct masses, 5 mL mineral stock, 1 mL vitamin
    stock and 1000 mL water. All 15 mineral and 10 vitamin constituents instead appear
    at their stock-strength g/L in every local layer. Main stored values are numerically
    compatible, within their displayed rounding, with dividing the source masses by
    1.006 L; the 1006 mL sum of named liquid inputs is not measured final volume and
    excludes unspecified later-stock volumes. The unavailable main API prevents exact
    independent confirmation of that historical normalization.
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - record
  - dsmz685
  - solution241
  - solution5980
  - historical-report
- assessment_id: preparation
  area: completeness
  topic: Main anaerobic procedure and stock-specific pH
  outcome: concern
  summary: The DSMZ owner retains main pH 8.5, 100% N2, 30–45 min sparging, autoclaving
    and the sterile later additions. It also retains the mineral stock pH 6.5 then
    7.0 with KOH, but incorrectly places that procedure among main-medium steps. The
    generated target and KOMODO owner omit both procedures. Preserve fumarate/vitamin
    filtration, source-specific stock handling and stock pH; the primary gives no
    autoclave temperature or duration to invent.
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz685
  - mineral-parent
- assessment_id: classification
  area: scope
  topic: Medium class, physical state and biological claims
  outcome: supported
  summary: 'COMPLEX/UNDEFINED is consistent with yeast extract and LIQUID with the
    collection formulation. Bacterial filing and generic microbial-cultivation application
    are catalog scope, not experimental growth evidence. No named organism/strain,
    incubation optimum, DOI or PMID is asserted. The KOMODO Aerobic: Yes note conflicts
    with the primary anaerobic procedure when read as a cultivation instruction and
    requires attribution.'
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - record
  - dsmz685
  - komodo-catalog
- assessment_id: forms
  area: grounding
  topic: Source-specific hydrate and vitamin forms
  outcome: concern
  summary: The mineral recipe explicitly specifies NiCl2 x 6 H2O, while both asserted
    CHEBI slots use CHEBI:34887 with formula Cl2Ni. Other explicit source hydrate
    forms were compared to their captured structures. Calcium D-(+)-pantothenate is
    consistent with CHEBI:31345 stereochemistry; the DL-lipoic source is not contradicted
    by the nonstereospecific CHEBI:16494 structure. Generic vitamin B12 remains generic.
    No replacement CURIE or unsupported stereochemical conversion is proposed.
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - record
  - dsmz685
  - chebi34887
  - chebi31345
  - chebi16494
  - chebi176843
- assessment_id: writer-scope
  area: provenance
  topic: Current transform behavior and historical attribution
  outcome: concern
  summary: Current MediaDive parsing separates primary stock additions from direct
    compounds, although preparation parsing still concatenates steps from all solutions.
    Current formulation merging requires scientific-field compatibility; ingredient-set
    equality alone is insufficient. The inspected DSMZ resolver copies ingredient/solution
    composition without copying preparation and emits naive timestamps. These are
    current implementation observations, not proof of the precise historical execution.
    Correct maintained owners and preserve source distinctions before regeneration.
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - record
  - historical-report
  - writer-context-0
  - writer-context-1
  - writer-context-2
  - resolver
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 47 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006290
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"KH2PO4 0.50 g\",\n    \"field_path\"\
    : \"ingredients[0].concentration\",\n    \"decision\": \"unsupported\",\n    \"\
    local\": {\n      \"value\": \"0.497018\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz685\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main table; exact named row\",\n \
    \       \"exact_source_quote\": \"KH2PO4 0.50 g\",\n        \"snapshot_sha256\"\
    : \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n    \
    \    \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"The primary verifies the source batch\
    \ mass, but not the final-volume denominator of the stored g/L. Preserve the source\
    \ amount and preparation stage; do not silently endorse or renormalize the historical\
    \ rounded value.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.497018\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[0].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.497018\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.497018\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 0.5 g / 1.006 L = 0.4970178926441351888667992048\
    \ g/L; stored 0.497018 g/L. Displayed rounding is retained. The 1006 mL sum is\
    \ not a measured final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    Na2HPO4 x 2 H2O 3.90 g\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"3.87674\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main table; exact named row\",\n \
    \       \"exact_source_quote\": \"Na2HPO4 x 2 H2O 3.90 g\",\n        \"snapshot_sha256\"\
    : \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n    \
    \    \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"The primary verifies the source batch\
    \ mass, but not the final-volume denominator of the stored g/L. Preserve the source\
    \ amount and preparation stage; do not silently endorse or renormalize the historical\
    \ rounded value.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"3.87674\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[1].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"3.87674\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"3.87674\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\": \"\
    Conditional comparison only: 3.9 g / 1.006 L = 3.876739562624254473161033797 g/L;\
    \ stored 3.87674 g/L. Displayed rounding is retained. The 1006 mL sum is not a\
    \ measured final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"KCl 0.50\
    \ g\",\n    \"field_path\": \"ingredients[2].concentration\",\n    \"decision\"\
    : \"unsupported\",\n    \"local\": {\n      \"value\": \"0.497018\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main table; exact named row\",\n \
    \       \"exact_source_quote\": \"KCl 0.50 g\",\n        \"snapshot_sha256\":\
    \ \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n    \
    \    \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"The primary verifies the source batch\
    \ mass, but not the final-volume denominator of the stored g/L. Preserve the source\
    \ amount and preparation stage; do not silently endorse or renormalize the historical\
    \ rounded value.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.497018\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[2].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.497018\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.497018\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 0.5 g / 1.006 L = 0.4970178926441351888667992048\
    \ g/L; stored 0.497018 g/L. Displayed rounding is retained. The 1006 mL sum is\
    \ not a measured final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    Yeast extract 5.00 g\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"4.97018\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main table; exact named row\",\n \
    \       \"exact_source_quote\": \"Yeast extract 5.00 g\",\n        \"snapshot_sha256\"\
    : \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n    \
    \    \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"The primary verifies the source batch\
    \ mass, but not the final-volume denominator of the stored g/L. Preserve the source\
    \ amount and preparation stage; do not silently endorse or renormalize the historical\
    \ rounded value.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"4.97018\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[3].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"4.97018\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"4.97018\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\": \"\
    Conditional comparison only: 5 g / 1.006 L = 4.970178926441351888667992048 g/L;\
    \ stored 4.97018 g/L. Displayed rounding is retained. The 1006 mL sum is not a\
    \ measured final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"Na2-fumarate\
    \ 1.50 g\",\n    \"field_path\": \"ingredients[4].concentration\",\n    \"decision\"\
    : \"unsupported\",\n    \"local\": {\n      \"value\": \"1.49105\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main table; exact named row\",\n \
    \       \"exact_source_quote\": \"Na2-fumarate 1.50 g\",\n        \"snapshot_sha256\"\
    : \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n    \
    \    \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"The primary verifies the source batch\
    \ mass, but not the final-volume denominator of the stored g/L. Preserve the source\
    \ amount and preparation stage; do not silently endorse or renormalize the historical\
    \ rounded value.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.49105\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[4].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1.49105\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.49105\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\": \"\
    Conditional comparison only: 1.5 g / 1.006 L = 1.491053677932405566600397614 g/L;\
    \ stored 1.49105 g/L. Displayed rounding is retained. The 1006 mL sum is not a\
    \ measured final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"L-Cysteine\
    \ HCl x H2O 0.15 g\",\n    \"field_path\": \"ingredients[5].concentration\",\n\
    \    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.149105\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main table; exact named row\",\n \
    \       \"exact_source_quote\": \"L-Cysteine HCl x H2O 0.15 g\",\n        \"snapshot_sha256\"\
    : \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n    \
    \    \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"The primary verifies the source batch\
    \ mass, but not the final-volume denominator of the stored g/L. Preserve the source\
    \ amount and preparation stage; do not silently endorse or renormalize the historical\
    \ rounded value.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.149105\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[5].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.149105\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.149105\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 0.15 g / 1.006 L = 0.1491053677932405566600397614\
    \ g/L; stored 0.149105 g/L. Displayed rounding is retained. The 1006 mL sum is\
    \ not a measured final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    Na2S x 9 H2O 0.15 g\",\n    \"field_path\": \"ingredients[6].concentration\",\n\
    \    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.149105\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main table; exact named row\",\n \
    \       \"exact_source_quote\": \"Na2S x 9 H2O 0.15 g\",\n        \"snapshot_sha256\"\
    : \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n    \
    \    \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"The primary verifies the source batch\
    \ mass, but not the final-volume denominator of the stored g/L. Preserve the source\
    \ amount and preparation stage; do not silently endorse or renormalize the historical\
    \ rounded value.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.149105\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[6].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.149105\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.149105\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional comparison only: 0.15 g / 1.006 L = 0.1491053677932405566600397614\
    \ g/L; stored 0.149105 g/L. Displayed rounding is retained. The 1006 mL sum is\
    \ not a measured final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    mineral stock: Nitrilotriacetic acid 1.50 g\",\n    \"field_path\": \"ingredients[7].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"Nitrilotriacetic acid\
    \ 1.50 g\",\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the exact stock endpoint’s nominal 1 L volume declaration, 1.5 g/L × 0.005 L\
    \ would deliver 0.0075 g per listed medium batch. This is conditional stock arithmetic,\
    \ not a measured final-medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"mineral stock: MgSO4 x 7 H2O 3.00 g\",\n    \"field_path\": \"ingredients[8].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"3\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 3.00 g\"\
    ,\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[8].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"3\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the exact stock endpoint’s nominal 1 L volume declaration, 3 g/L × 0.005 L would\
    \ deliver 0.015 g per listed medium batch. This is conditional stock arithmetic,\
    \ not a measured final-medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"mineral stock: MnSO4 x H2O 0.50 g\",\n    \"field_path\": \"ingredients[9].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"MnSO4 x H2O 0.50 g\",\n\
    \        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[9].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the exact stock endpoint’s nominal 1 L volume declaration, 0.5 g/L × 0.005 L\
    \ would deliver 0.0025 g per listed medium batch. This is conditional stock arithmetic,\
    \ not a measured final-medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"mineral stock: NaCl 1.00 g\",\n    \"field_path\": \"ingredients[10].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"NaCl 1.00 g\",\n     \
    \   \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the exact stock endpoint’s nominal 1 L volume declaration, 1 g/L × 0.005 L would\
    \ deliver 0.005 g per listed medium batch. This is conditional stock arithmetic,\
    \ not a measured final-medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"mineral stock: FeSO4 x 7 H2O 0.10 g\",\n    \"field_path\": \"ingredients[11].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.1\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"FeSO4 x 7 H2O 0.10 g\"\
    ,\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[11].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the exact stock endpoint’s nominal 1 L volume declaration, 0.1 g/L × 0.005 L\
    \ would deliver 0.0005 g per listed medium batch. This is conditional stock arithmetic,\
    \ not a measured final-medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"mineral stock: CoSO4 x 7 H2O 0.18 g\",\n    \"field_path\": \"ingredients[12].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.18\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"CoSO4 x 7 H2O 0.18 g\"\
    ,\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.18\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[12].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.18\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.18 g/L × 0.005 L would deliver 0.00090 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"mineral stock:\
    \ CaCl2 x 2 H2O 0.10 g\",\n    \"field_path\": \"ingredients[13].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.1\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 0.10 g\"\
    ,\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[13].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the exact stock endpoint’s nominal 1 L volume declaration, 0.1 g/L × 0.005 L\
    \ would deliver 0.0005 g per listed medium batch. This is conditional stock arithmetic,\
    \ not a measured final-medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"mineral stock: ZnSO4 x 7 H2O 0.18 g\",\n    \"field_path\": \"ingredients[14].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.18\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 0.18 g\"\
    ,\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[14].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.18\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[14].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.18\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.18 g/L × 0.005 L would deliver 0.00090 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"mineral stock:\
    \ CuSO4 x 5 H2O 0.01 g\",\n    \"field_path\": \"ingredients[15].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.01\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"CuSO4 x 5 H2O 0.01 g\"\
    ,\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[15].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.01 g/L × 0.005 L would deliver 0.00005 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"mineral stock:\
    \ AlK(SO4)2 x 12 H2O 0.02 g\",\n    \"field_path\": \"ingredients[16].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.02\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"AlK(SO4)2 x 12 H2O 0.02\
    \ g\",\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[16].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.02\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[16].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.02 g/L × 0.005 L would deliver 0.00010 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"mineral stock:\
    \ H3BO3 0.01 g\",\n    \"field_path\": \"ingredients[17].concentration\",\n  \
    \  \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.01\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"H3BO3 0.01 g\",\n    \
    \    \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[17].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[17].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.01 g/L × 0.005 L would deliver 0.00005 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"mineral stock:\
    \ Na2MoO4 x 2 H2O 0.01 g\",\n    \"field_path\": \"ingredients[18].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.01\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 0.01 g\"\
    ,\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[18].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[18].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.01 g/L × 0.005 L would deliver 0.00005 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"mineral stock:\
    \ NiCl2 x 6 H2O 0.03 g\",\n    \"field_path\": \"ingredients[19].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.03\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"NiCl2 x 6 H2O 0.03 g\"\
    ,\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[19].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.03\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[19].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.03\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.03 g/L × 0.005 L would deliver 0.00015 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"mineral stock:\
    \ Na2SeO3 x 5 H2O 0.30 mg\",\n    \"field_path\": \"ingredients[20].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.0003\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"Na2SeO3 x 5 H2O 0.30 mg\"\
    ,\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[20].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.0003\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[20].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0003\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.0003 g/L × 0.005 L would deliver 0.0000015\
    \ g per listed medium batch. This is conditional stock arithmetic, not a measured\
    \ final-medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    mineral stock: Na2WO4 x 2 H2O 0.40 mg\",\n    \"field_path\": \"ingredients[21].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.0004\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table;\
    \ exact named row\",\n        \"exact_source_quote\": \"Na2WO4 x 2 H2O 0.40 mg\"\
    ,\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[21].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.0004\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[21].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0004\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.0004 g/L × 0.005 L would deliver 0.0000020\
    \ g per listed medium batch. This is conditional stock arithmetic, not a measured\
    \ final-medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    vitamin stock: Biotin 20.00 mg\",\n    \"field_path\": \"ingredients[22].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.02\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) stock table; exact\
    \ named row\",\n        \"exact_source_quote\": \"Biotin 20.00 mg\",\n       \
    \ \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[22].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.02\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[22].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.02 g/L × 0.001 L would deliver 0.00002 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"vitamin stock:\
    \ Folic acid 20.00 mg\",\n    \"field_path\": \"ingredients[23].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.02\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) stock table; exact\
    \ named row\",\n        \"exact_source_quote\": \"Folic acid 20.00 mg\",\n   \
    \     \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[23].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.02\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[23].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.02 g/L × 0.001 L would deliver 0.00002 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"vitamin stock:\
    \ Pyridoxine hydrochloride 100.00 mg\",\n    \"field_path\": \"ingredients[24].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.1\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) stock table; exact\
    \ named row\",\n        \"exact_source_quote\": \"Pyridoxine hydrochloride 100.00\
    \ mg\",\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[24].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the exact stock endpoint’s nominal 1 L volume declaration, 0.1 g/L × 0.001 L\
    \ would deliver 0.0001 g per listed medium batch. This is conditional stock arithmetic,\
    \ not a measured final-medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"vitamin stock: Thiamine HCl 50.00 mg\",\n    \"field_path\": \"ingredients[25].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.05\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) stock table; exact\
    \ named row\",\n        \"exact_source_quote\": \"Thiamine HCl 50.00 mg\",\n \
    \       \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[25].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[25].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"vitamin stock:\
    \ Riboflavin 50.00 mg\",\n    \"field_path\": \"ingredients[26].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.05\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) stock table; exact\
    \ named row\",\n        \"exact_source_quote\": \"Riboflavin 50.00 mg\",\n   \
    \     \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[26].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[26].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"vitamin stock:\
    \ Nicotinic acid 50.00 mg\",\n    \"field_path\": \"ingredients[27].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.05\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) stock table; exact\
    \ named row\",\n        \"exact_source_quote\": \"Nicotinic acid 50.00 mg\",\n\
    \        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[27].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[27].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"vitamin stock:\
    \ Calcium D-(+)-pantothenate 50.00 mg\",\n    \"field_path\": \"ingredients[28].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.05\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) stock table; exact\
    \ named row\",\n        \"exact_source_quote\": \"Calcium D-(+)-pantothenate 50.00\
    \ mg\",\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[28].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[28].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"vitamin stock:\
    \ Vitamin B12 1.00 mg\",\n    \"field_path\": \"ingredients[29].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.001\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) stock table; exact\
    \ named row\",\n        \"exact_source_quote\": \"Vitamin B12 1.00 mg\",\n   \
    \     \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[29].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.001\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[29].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.001 g/L × 0.001 L would deliver 0.000001 g\
    \ per listed medium batch. This is conditional stock arithmetic, not a measured\
    \ final-medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    vitamin stock: p-Aminobenzoic acid 50.00 mg\",\n    \"field_path\": \"ingredients[30].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.05\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) stock table; exact\
    \ named row\",\n        \"exact_source_quote\": \"p-Aminobenzoic acid 50.00 mg\"\
    ,\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[30].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[30].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"vitamin stock:\
    \ (DL)-alpha-Lipoic acid 50.00 mg\",\n    \"field_path\": \"ingredients[31].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.05\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin (10x) stock table; exact\
    \ named row\",\n        \"exact_source_quote\": \"(DL)-alpha-Lipoic acid 50.00\
    \ mg\",\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"This amount belongs to the separate stock\
    \ recipe, not an undiluted direct-medium concentration. Restore the stock composition,\
    \ original unit and receiving-medium aliquot. No final-medium g/L is established.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[31].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[31].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On the exact stock endpoint’s\
    \ nominal 1 L volume declaration, 0.05 g/L × 0.001 L would deliver 0.00005 g per\
    \ listed medium batch. This is conditional stock arithmetic, not a measured final-medium\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"Mineral stock\
    \ dose\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"add\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main table\",\n        \"exact_source_quote\"\
    : \"Modified Wolin's mineral solution 5.00 ml\",\n        \"snapshot_sha256\"\
    : \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n    \
    \    \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"Represent this explicit source-only dose\
    \ or solvent quantity in its own stage. Existing preparation container values\
    \ are retained as inspected; their presence is not a water or aliquot claim. A\
    \ listed water amount does not establish measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Vitamin stock dose\",\n    \"field_path\": \"solutions\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main table\",\n        \"exact_source_quote\"\
    : \"Wolin's vitamin solution (10x) 1.00 ml\",\n        \"snapshot_sha256\": \"\
    711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n        \"\
    parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"Represent this explicit source-only dose\
    \ or solvent quantity in its own stage. Existing preparation container values\
    \ are retained as inspected; their presence is not a water or aliquot claim. A\
    \ listed water amount does not establish measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main water\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"Represent this explicit source-only dose\
    \ or solvent quantity in its own stage. Existing preparation container values\
    \ are retained as inspected; their presence is not a water or aliquot claim. A\
    \ listed water amount does not establish measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Dissolve ingredients (except fumarate, vitamins,\
    \ cysteine and sulfide), adjust pH to 8.5 and sparge medium with 100% N2 gas for\
    \ 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. After sterilization\
    \ add fumarate, vitamins, cysteine and sulfide from sterile anoxic stock solutions\
    \ prepared under 100% N2 gas. Stock solutions of fumarate and vitamins are sterilized\
    \ by filtration. Adjust pH of complete medium to 8.5, if necessary.\"\n      \
    \    },\n          {\n            \"step_number\": 2,\n            \"action\"\
    : \"ADJUST_PH\",\n            \"description\": \"First dissolve nitrilotriacetic\
    \ acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0\
    \ with KOH.\"\n          }\n        ],\n        \"decision\": \"add\"\n      }\n\
    \    ]\n  },\n  {\n    \"ingredient_or_context\": \"Mineral stock water\",\n \
    \   \"field_path\": \"solutions\",\n    \"decision\": \"add\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz685\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 Modified Wolin mineral stock table\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"\
    snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"Represent this explicit source-only dose\
    \ or solvent quantity in its own stage. Existing preparation container values\
    \ are retained as inspected; their presence is not a water or aliquot claim. A\
    \ listed water amount does not establish measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Vitamin stock water\",\n    \"field_path\": \"solutions\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 Wolin vitamin stock table\",\n   \
    \     \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\"\
    : \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n    \
    \    \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"Represent this explicit source-only dose\
    \ or solvent quantity in its own stage. Existing preparation container values\
    \ are retained as inspected; their presence is not a water or aliquot claim. A\
    \ listed water amount does not establish measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main recorded pH\",\n    \"field_path\": \"ph_value\",\n    \"decision\":\
    \ \"evidence_only\",\n    \"local\": 8.5,\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"adjust pH to 8.5\",\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"All three layers retain pH 8.5 without\
    \ matching attached claim evidence.\",\n    \"action_taken\": \"Review only; no\
    \ recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ph_value\",\n        \"stored\": 8.5,\n \
    \       \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\",\n  \
    \      \"field_path\": \"ph_value\",\n        \"stored\": 8.5,\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 8.5,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main initial pH\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"adjust pH to 8.5\",\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains this literal numeric\
    \ context. Attach evidence to the main procedure; restore stock scope for mineral\
    \ endpoints. The target and KOMODO require the source-specific procedure.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust\
    \ pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic.\
    \ Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or\
    \ serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas.\
    \ Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust\
    \ pH of complete medium to 8.5, if necessary.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Main N2 fraction\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"decision\": \"add\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"100% N2 gas for 30 - 45 min\",\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains this literal numeric\
    \ context. Attach evidence to the main procedure; restore stock scope for mineral\
    \ endpoints. The target and KOMODO require the source-specific procedure.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust\
    \ pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic.\
    \ Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or\
    \ serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas.\
    \ Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust\
    \ pH of complete medium to 8.5, if necessary.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Main sparging duration\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"decision\": \"add\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"30 - 45 min\",\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains this literal numeric\
    \ context. Attach evidence to the main procedure; restore stock scope for mineral\
    \ endpoints. The target and KOMODO require the source-specific procedure.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust\
    \ pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic.\
    \ Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or\
    \ serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas.\
    \ Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust\
    \ pH of complete medium to 8.5, if necessary.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Later-stock N2 fraction\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"decision\": \"add\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"solutions prepared under 100% N2 gas.\",\n        \"snapshot_sha256\": \"\
    711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n        \"\
    parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains this literal numeric\
    \ context. Attach evidence to the main procedure; restore stock scope for mineral\
    \ endpoints. The target and KOMODO require the source-specific procedure.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust\
    \ pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic.\
    \ Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or\
    \ serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas.\
    \ Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust\
    \ pH of complete medium to 8.5, if necessary.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Main final pH\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"decision\": \"add\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"Adjust pH of complete medium to 8.5\",\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains this literal numeric\
    \ context. Attach evidence to the main procedure; restore stock scope for mineral\
    \ endpoints. The target and KOMODO require the source-specific procedure.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust\
    \ pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic.\
    \ Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or\
    \ serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas.\
    \ Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust\
    \ pH of complete medium to 8.5, if necessary.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Mineral initial\
    \ pH\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\": \"add\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 mineral stock procedure\",\n     \
    \   \"exact_source_quote\": \"adjust pH to 6.5 with KOH\",\n        \"snapshot_sha256\"\
    : \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n    \
    \    \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains this literal numeric\
    \ context. Attach evidence to the main procedure; restore stock scope for mineral\
    \ endpoints. The target and KOMODO require the source-specific procedure.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Mineral final pH\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"decision\": \"add\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 mineral stock procedure\",\n     \
    \   \"exact_source_quote\": \"final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\"\
    : \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n    \
    \    \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ alone retains this literal numeric\
    \ context. Attach evidence to the main procedure; restore stock scope for mineral\
    \ endpoints. The target and KOMODO require the source-specific procedure.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Unquantified mineral\
    \ KOH titrant\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz685\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 mineral titration\",\n        \"exact_source_quote\"\
    : \"final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\": \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\"\
    ,\n        \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"KOH has no stated dose. Fumarate, cysteine\
    \ and sulfide have stated main masses but no stock strength or aliquot volume;\
    \ the vitamin aliquot is separately specified in the main table. Preserve these\
    \ limits without inventing a concentration, dose or final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"not_quantified\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Unspecified later-stock\
    \ strengths and aliquot volumes\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz685\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium685.pdf\",\n        \"\
    source_locator\": \"PDF page 1 later additions\",\n        \"exact_source_quote\"\
    : \"After sterilization add fumarate, vitamins, cysteine and sulfide from sterile\
    \ anoxic stock\\nsolutions prepared under 100% N2 gas.\",\n        \"snapshot_sha256\"\
    : \"711721020a688062f4b77280fc71f8bee8e24cb7468da0acd75855fb7ec50c32\",\n    \
    \    \"parsed_text_sha256\": \"e2872e850e90ddaa13e01de667d8d49b339139e25a38f163634a26b60e56eb1d\"\
    \n      }\n    ],\n    \"rationale\": \"KOH has no stated dose. Fumarate, cysteine\
    \ and sulfide have stated main masses but no stock strength or aliquot volume;\
    \ the vitamin aliquot is separately specified in the main table. Preserve these\
    \ limits without inventing a concentration, dose or final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"not_quantified\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobranca_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except fumarate, vitamins, cysteine and sulfide), adjust\
    \ pH to 8.5 and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic.\
    \ Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or\
    \ serum vials and autoclave. After sterilization add fumarate, vitamins, cysteine\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas.\
    \ Stock solutions of fumarate and vitamins are sterilized by filtration. Adjust\
    \ pH of complete medium to 8.5, if necessary.\",\n        \"decision\": \"not_quantified\"\
    \n      }\n    ]\n  }\n]"
findings:
- finding_id: f1
  issue_key: anaerobranca-stock-formulation-flattening
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock-strength constituents replace the intended aliquots
  description: All three layers list the 15 mineral and 10 vitamin constituents as
    direct g/L at stock strength, while omitting the 5 mL mineral and 1 mL vitamin
    additions. This materially changes the denoted medium. The seven historical main
    g/L values also lack an independently established final-volume basis; source batch
    masses remain available and must be preserved.
  target_ids:
  - CultureMech:006290
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz685
  - solution241
  - solution5980
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobranca_medium.yaml
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
  issue_key: anaerobranca-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is grounded to anhydrous nickel dichloride
  description: The source mineral stock specifies NiCl2 x 6 H2O, 0.03 g, but every
    local layer asserts CHEBI:34887, whose formula is Cl2Ni. The secondary CHEBI key
    repeats the same form mismatch.
  target_ids:
  - CultureMech:006290
  field_paths:
  - ingredients[19].term
  - ingredients[19].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz685
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobranca_medium.yaml
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
  issue_key: anaerobranca-preparation-stage-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Anaerobic preparation is missing or assigned to the wrong stage
  description: The target and KOMODO owner omit the source anaerobic and sterilization
    sequence. The DSMZ owner retains that sequence but stores the mineral pH 6.5 to
    7.0 titration as main preparation. Mis-scoping this stock titration can contradict
    main pH 8.5. This is a combined preparation representation defect; no unprinted
    sterilization cycle is inferred.
  target_ids:
  - CultureMech:006290
  field_paths:
  - preparation_steps
  - solutions
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz685
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobranca_medium.yaml
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
  issue_key: anaerobranca-catalog-history-qualification
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Catalog aerobic flag and historical timestamp limitations need qualification
  description: 'The target and KOMODO owner retain Aerobic: Yes from the catalog,
    while the primary specifies anoxic preparation. Both also retain one malformed
    timestamp and one timezone-naive timestamp. Catalog attribution and append-only
    clarification are needed; neither a physiological growth claim nor a fabricated
    timestamp is warranted.'
  target_ids:
  - CultureMech:006290
  field_paths:
  - notes
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - komodo-catalog
  - dsmz685
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobranca_medium.yaml
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
  description: Reconstruct the two named stocks and source doses in each maintained
    owner, retain the seven original main masses and unresolved final-volume basis,
    then regenerate compatible source-specific records. Do not convert nominal stock
    delivery into an asserted final-medium concentration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006290
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobranca_medium.yaml
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
  description: Resolve a verified nickel hexahydrate identity for both asserted slots,
    retaining the 0.03 g source stock mass and separate 5 mL stock dose. Do not invent
    a replacement identifier or infer an anhydrous mass conversion.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006290
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobranca_medium.yaml
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
  description: Preserve the existing DSMZ main instructions with attached evidence,
    move mineral titration into the stock procedure, and reconcile the other owner
    before regeneration. Keep 100% N2, 30–45 min, main pH 8.5 and source filtration
    qualifiers distinct.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006290
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobranca_medium.yaml
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
  description: Qualify the catalog flag as source metadata and append a bounded provenance
    clarification. Preserve old history and do not guess timezone or malformed timestamp
    digits.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006290
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobranca_medium.yaml
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
- 'mediadive685api: exact public request returned HTTP 503; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'komodoMediaListCanonical: exact public request returned HTTP 403; original access
  time, response bytes and any separately recorded retry are retained. Error bytes
  do not establish formulation or historical absence.'
- 'komodo685detail: exact public request returned HTTP 403; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'mediadive685apiRetry: exact public request returned HTTP 503; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'komodo685actual: exact public request returned HTTP 403; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- Exact main MediaDive 685 access failed twice with HTTP 503. Independent historical
  main-response correspondence and its normalization basis remain unavailable; the
  dated local report is derivative context only. Available DSMZ primary and named
  stock endpoints support the scoped findings.
- The parent DSMZ 141 and 120 sources are used only for the explicitly referenced
  stocks. Their other media, organisms and gas/pressure conditions do not transfer.
- The primary lists stock water and titration; conditional delivered masses use the
  provider’s declared nominal 1 L stock bases. No measured final stock or medium volume
  is asserted.
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
