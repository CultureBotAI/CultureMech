# Source and formulation review: artificial_seawater_base_with_thiosulfate_as_the_electron_donor (CultureMech:008841)

- Review: 20261021T202020Z-culturemech-008841-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T20:11:19Z
- Finished UTC: 2026-10-21T20:20:20Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M2252 is a three-entry shorthand, not a complete reconstruction of the cited MC-1 experiments. The primary paper separates 10 mM semisolid radiolabel cultures from a staged liquid bottle recipe. The generated target is stale, the maintained owner adds useful bounded citation and taxonomy context, and both retain an ester-class grounding for the inorganic thiosulfate donor. Full artificial-seawater, mineral-elixir and vitamin formulas remain unavailable. The owner’s 1000 mL/L base value may be a normalization marker; its stage and denominator require evidence rather than a presumption of numerical error.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 364; batch 037 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-six task batches contain 360 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 363 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008841 | data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml | generated | artificial_seawater_base_with_thiosulfate_as_the_electron_donor |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008841 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008841 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch037/364/strict.tsv |
| validate-terms | passed | True | CultureMech:008841 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008841 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008841 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: pmid15338111publisher | unavailable | True | CultureMech:008841 | The current publisher route supplies bibliographic/abstract material but no inspected complete artificial-seawater recipe. The requested PDF route returned the same access page, not a usable full-text formula. |
| Exact source content access: pmc1180996pdf | unavailable | True | CultureMech:008841 | The requested 1997 primary PDF returned a download interstitial; its available PMC page supplies abstract/bibliography but not the complete modified Wolfe or vitamin formulas. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008841.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:008841.

42 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "Artificial seawater base",
    "stage": "Generated secondary shorthand",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 1,
      "unit": "L",
      "basis": "Listed base input, not a measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "togoM2252original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2252",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Artificial seawater\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "1d34bc97fa49460f6db13a3405d5fa5bc0b369dbe850c8d7b68e882264e872b0"
      }
    ],
    "interpretation": "The provider supplies a liquid base volume; 1 G_PER_L is unsupported. The exact base composition remains unresolved."
  },
  {
    "decision_id": "q2",
    "name": "Artificial seawater base denominator",
    "stage": "Maintained secondary shorthand",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "value": 1000,
      "unit": "ML_PER_L",
      "basis": "Existing normalization marker; denominator/stage evidence unresolved"
    },
    "source_snippets": [
      {
        "source_key": "togoM2252original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2252",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Artificial seawater\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "1d34bc97fa49460f6db13a3405d5fa5bc0b369dbe850c8d7b68e882264e872b0"
      }
    ],
    "interpretation": "The owner’s 1000 mL/L may be a normalization marker for the unresolved artificial-seawater base. The provider supports a 1 L base input, but does not independently establish the owner’s normalization denominator or a measured final-medium ratio. Retain the numerical marker pending stage/basis evidence; it is not demonstrated numerically false."
  },
  {
    "decision_id": "q3",
    "name": "Thiosulfate",
    "stage": "Secondary three-entry shorthand",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "10",
          "unit": "MILLIMOLAR"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "10.0",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": 10,
      "unit": "MILLIMOLAR",
      "scope": "Exact TOGO shorthand; primary 10 mM independently belongs to semisolid variant"
    },
    "source_snippets": [
      {
        "source_key": "togoM2252original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2252",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"thiosulfate\",\n          \"volume\": 10,\n          \"unit\": \"mM\"",
        "snapshot_sha256": "1d34bc97fa49460f6db13a3405d5fa5bc0b369dbe850c8d7b68e882264e872b0"
      },
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Table 1 caption",
        "exact_source_quote": "Contribution of CO 2 to protein carbon in cells of the magnetotactic coccus strain MC-1 grown in semisolid, oxygen-gradient medium containing 10 mM thiosulfate as the electron source",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "The local value agrees with the provider, but neither layer has attached claim-level amount evidence. Do not merge the primary semisolid quantity with the separate liquid post-autoclave stock dose."
  },
  {
    "decision_id": "q4",
    "name": "Oxygen",
    "stage": "Secondary gas entry",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "dissolved_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "togoM2252original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2252",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"O2\"",
        "snapshot_sha256": "1d34bc97fa49460f6db13a3405d5fa5bc0b369dbe850c8d7b68e882264e872b0"
      }
    ],
    "interpretation": "A variable gas entry has no numerical concentration. Primary bottle-gas volumes and headspace percentages are separate observations, not dissolved oxygen concentrations."
  },
  {
    "decision_id": "q5",
    "name": "Incubation temperature",
    "stage": "Maintained liquid/provider scope",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "temperature_value",
        "stored": 25.0
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "TOGO M2252 reports a liquid artificial seawater base with 10 mM thiosulfate as the electron donor for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the cultivation context and state that cultures were incubated statically under an O2 gradient at 25 C in the dark."
      }
    ],
    "desired": {
      "value": 25,
      "unit": "DEG_C"
    },
    "source_snippets": [
      {
        "source_key": "togoM2252original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2252",
        "source_locator": "$.comments[1]",
        "exact_source_quote": "Cultures were incubated statically under an [O2] (O2 concentration) gradient at 25°C in the dark.",
        "snapshot_sha256": "1d34bc97fa49460f6db13a3405d5fa5bc0b369dbe850c8d7b68e882264e872b0",
        "parsed_text_sha256": "be035e46506ad7db91dda885f66a9c76a24965ac000816e0d42a3f3d8850c259"
      },
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Materials and Methods, liquid incubation sentence",
        "exact_source_quote": "at 25°C.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "The owner’s 25°C agrees with both the provider and liquid primary context but lacks attached amount evidence. Darkness is supported by the provider text only."
  },
  {
    "decision_id": "q6",
    "name": "Semisolid temperature",
    "stage": "Radiolabel variant",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "Source: https://togomedium.org/medium/M2252"
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "TOGO M2252 reports a liquid artificial seawater base with 10 mM thiosulfate as the electron donor for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the cultivation context and state that cultures were incubated statically under an O2 gradient at 25 C in the dark."
      }
    ],
    "desired": {
      "value": 28,
      "unit": "DEG_C",
      "physical_state": "SEMISOLID"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Radiolabel variant",
        "exact_source_quote": "cells of strain MC-1 were grown microaerobically in semisolid medium at 28°C",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Keep this as a separate source-specific experiment; do not replace the liquid owner’s temperature."
  },
  {
    "decision_id": "q7",
    "name": "Semisolid thiosulfate",
    "stage": "Radiolabel variant",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "Source: https://togomedium.org/medium/M2252"
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "TOGO M2252 reports a liquid artificial seawater base with 10 mM thiosulfate as the electron donor for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the cultivation context and state that cultures were incubated statically under an O2 gradient at 25 C in the dark."
      }
    ],
    "desired": {
      "value": 10,
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Radiolabel variant",
        "exact_source_quote": "Contribution of CO 2 to protein carbon in cells of the magnetotactic coccus strain MC-1 grown in semisolid, oxygen-gradient medium containing 10 mM thiosulfate as the electron source",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "This is an explicit Table 1 caption quantity, not a footnote or proof that the liquid recipe has the same concentration."
  },
  {
    "decision_id": "q8",
    "name": "Liquid culture volume",
    "stage": "Liquid enzyme/lipid/isotope culture",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 850,
      "unit": "ML",
      "basis": "Stated culture-medium volume in bottle"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid enzyme/lipid/isotope culture",
        "exact_source_quote": "Cells were grown in 850 ml of medium in 2-liter glass bottles.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Preserve the stated liquid-culture volume; it is not license to rebase every later bottle addition to one liter or infer a measured final volume."
  },
  {
    "decision_id": "q9",
    "name": "Bottle volume",
    "stage": "Liquid enzyme/lipid/isotope culture",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 2,
      "unit": "L"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid enzyme/lipid/isotope culture",
        "exact_source_quote": "Cells were grown in 850 ml of medium in 2-liter glass bottles.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Vessel capacity is distinct from liquid-medium volume and actual headspace after additions."
  },
  {
    "decision_id": "q10",
    "name": "Modified Wolfe mineral elixir dose",
    "stage": "Liquid medium before autoclaving",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Artificial seawater",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solvating media, Mineral source; Properties: Complex component, Defined component, Solution"
          },
          {
            "preferred_term": "thiosulfate",
            "concentration": {
              "value": "10",
              "unit": "MILLIMOLAR"
            },
            "notes": "Role: Growth factor; Properties: Defined component, Inorganic compound, Simple component",
            "term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            }
          },
          {
            "preferred_term": "O2",
            "notes": "Properties: Gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Artificial seawater",
            "concentration": {
              "value": "1000.0",
              "unit": "ML_PER_L"
            },
            "source": "TOGO M2252",
            "notes": "TOGO M2252 lists 1 L Artificial seawater as the base; this artificial seawater mixture is retained without a single-compound ontology grounding."
          },
          {
            "preferred_term": "thiosulfate",
            "concentration": {
              "value": "10.0",
              "unit": "MILLIMOLAR"
            },
            "source": "TOGO M2252",
            "notes": "TOGO M2252 lists 10 mM thiosulfate as the electron donor.",
            "term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            }
          },
          {
            "preferred_term": "Oxygen gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "source": "TOGO M2252",
            "notes": "TOGO M2252 lists O2 and states that cultures were incubated statically under an O2 gradient.",
            "term": {
              "id": "CHEBI:15379",
              "label": "dioxygen"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15379",
              "label": "dioxygen"
            }
          }
        ]
      }
    ],
    "desired": {
      "value": 5,
      "unit": "ML_PER_L",
      "basis": "Before autoclaving"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid medium before autoclaving",
        "exact_source_quote": "The medium consisted of an artificial seawater ( 6 ) base to which was added the following (per liter), in order, prior to autoclaving: 5 ml of modified Wolfe's mineral elixir ( 21 ), 0.25 g of NH 4 Cl, and 100 μl of 0.2% (wt/vol) aqueous resazurin.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "The per-liter clause applies explicitly to this pre-autoclave list. Stock dose and stock strength are separate; the modified Wolfe formula is not recovered."
  },
  {
    "decision_id": "q11",
    "name": "NH4Cl",
    "stage": "Liquid medium before autoclaving",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Artificial seawater",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solvating media, Mineral source; Properties: Complex component, Defined component, Solution"
          },
          {
            "preferred_term": "thiosulfate",
            "concentration": {
              "value": "10",
              "unit": "MILLIMOLAR"
            },
            "notes": "Role: Growth factor; Properties: Defined component, Inorganic compound, Simple component",
            "term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            }
          },
          {
            "preferred_term": "O2",
            "notes": "Properties: Gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Artificial seawater",
            "concentration": {
              "value": "1000.0",
              "unit": "ML_PER_L"
            },
            "source": "TOGO M2252",
            "notes": "TOGO M2252 lists 1 L Artificial seawater as the base; this artificial seawater mixture is retained without a single-compound ontology grounding."
          },
          {
            "preferred_term": "thiosulfate",
            "concentration": {
              "value": "10.0",
              "unit": "MILLIMOLAR"
            },
            "source": "TOGO M2252",
            "notes": "TOGO M2252 lists 10 mM thiosulfate as the electron donor.",
            "term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            }
          },
          {
            "preferred_term": "Oxygen gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "source": "TOGO M2252",
            "notes": "TOGO M2252 lists O2 and states that cultures were incubated statically under an O2 gradient.",
            "term": {
              "id": "CHEBI:15379",
              "label": "dioxygen"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15379",
              "label": "dioxygen"
            }
          }
        ]
      }
    ],
    "desired": {
      "value": 0.25,
      "unit": "G_PER_L",
      "basis": "Before autoclaving"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid medium before autoclaving",
        "exact_source_quote": "The medium consisted of an artificial seawater ( 6 ) base to which was added the following (per liter), in order, prior to autoclaving: 5 ml of modified Wolfe's mineral elixir ( 21 ), 0.25 g of NH 4 Cl, and 100 μl of 0.2% (wt/vol) aqueous resazurin.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "The per-liter clause applies explicitly to this pre-autoclave list. Stock dose and stock strength are separate; the modified Wolfe formula is not recovered."
  },
  {
    "decision_id": "q12",
    "name": "Resazurin stock dose",
    "stage": "Liquid medium before autoclaving",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Artificial seawater",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solvating media, Mineral source; Properties: Complex component, Defined component, Solution"
          },
          {
            "preferred_term": "thiosulfate",
            "concentration": {
              "value": "10",
              "unit": "MILLIMOLAR"
            },
            "notes": "Role: Growth factor; Properties: Defined component, Inorganic compound, Simple component",
            "term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            }
          },
          {
            "preferred_term": "O2",
            "notes": "Properties: Gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Artificial seawater",
            "concentration": {
              "value": "1000.0",
              "unit": "ML_PER_L"
            },
            "source": "TOGO M2252",
            "notes": "TOGO M2252 lists 1 L Artificial seawater as the base; this artificial seawater mixture is retained without a single-compound ontology grounding."
          },
          {
            "preferred_term": "thiosulfate",
            "concentration": {
              "value": "10.0",
              "unit": "MILLIMOLAR"
            },
            "source": "TOGO M2252",
            "notes": "TOGO M2252 lists 10 mM thiosulfate as the electron donor.",
            "term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            }
          },
          {
            "preferred_term": "Oxygen gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "source": "TOGO M2252",
            "notes": "TOGO M2252 lists O2 and states that cultures were incubated statically under an O2 gradient.",
            "term": {
              "id": "CHEBI:15379",
              "label": "dioxygen"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15379",
              "label": "dioxygen"
            }
          }
        ]
      }
    ],
    "desired": {
      "value": 100,
      "unit": "MICROLITER_PER_L",
      "basis": "Before autoclaving"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid medium before autoclaving",
        "exact_source_quote": "The medium consisted of an artificial seawater ( 6 ) base to which was added the following (per liter), in order, prior to autoclaving: 5 ml of modified Wolfe's mineral elixir ( 21 ), 0.25 g of NH 4 Cl, and 100 μl of 0.2% (wt/vol) aqueous resazurin.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "The per-liter clause applies explicitly to this pre-autoclave list. Stock dose and stock strength are separate; the modified Wolfe formula is not recovered."
  },
  {
    "decision_id": "q13",
    "name": "Resazurin stock strength",
    "stage": "Liquid medium before autoclaving",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Artificial seawater",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solvating media, Mineral source; Properties: Complex component, Defined component, Solution"
          },
          {
            "preferred_term": "thiosulfate",
            "concentration": {
              "value": "10",
              "unit": "MILLIMOLAR"
            },
            "notes": "Role: Growth factor; Properties: Defined component, Inorganic compound, Simple component",
            "term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            }
          },
          {
            "preferred_term": "O2",
            "notes": "Properties: Gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Artificial seawater",
            "concentration": {
              "value": "1000.0",
              "unit": "ML_PER_L"
            },
            "source": "TOGO M2252",
            "notes": "TOGO M2252 lists 1 L Artificial seawater as the base; this artificial seawater mixture is retained without a single-compound ontology grounding."
          },
          {
            "preferred_term": "thiosulfate",
            "concentration": {
              "value": "10.0",
              "unit": "MILLIMOLAR"
            },
            "source": "TOGO M2252",
            "notes": "TOGO M2252 lists 10 mM thiosulfate as the electron donor.",
            "term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26977",
              "label": "thiosulfate"
            }
          },
          {
            "preferred_term": "Oxygen gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "source": "TOGO M2252",
            "notes": "TOGO M2252 lists O2 and states that cultures were incubated statically under an O2 gradient.",
            "term": {
              "id": "CHEBI:15379",
              "label": "dioxygen"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15379",
              "label": "dioxygen"
            }
          }
        ]
      }
    ],
    "desired": {
      "value": 0.2,
      "unit": "PERCENT_W_V",
      "basis": "Stock strength, not final concentration"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid medium before autoclaving",
        "exact_source_quote": "The medium consisted of an artificial seawater ( 6 ) base to which was added the following (per liter), in order, prior to autoclaving: 5 ml of modified Wolfe's mineral elixir ( 21 ), 0.25 g of NH 4 Cl, and 100 μl of 0.2% (wt/vol) aqueous resazurin.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "The per-liter clause applies explicitly to this pre-autoclave list. Stock dose and stock strength are separate; the modified Wolfe formula is not recovered."
  },
  {
    "decision_id": "q14",
    "name": "Main pH",
    "stage": "Liquid medium before gas treatment",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 7.0,
      "unit": "PH"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid medium before gas treatment",
        "exact_source_quote": "The pH of the medium was adjusted to 7.0, 1.26 g of NaHCO 3 was added per liter, and the vessel was sealed.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Preserve the main pH and explicitly per-liter bicarbonate separately from later buffer pH."
  },
  {
    "decision_id": "q15",
    "name": "NaHCO3",
    "stage": "Liquid medium before gas treatment",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 1.26,
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid medium before gas treatment",
        "exact_source_quote": "The pH of the medium was adjusted to 7.0, 1.26 g of NaHCO 3 was added per liter, and the vessel was sealed.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Preserve the main pH and explicitly per-liter bicarbonate separately from later buffer pH."
  },
  {
    "decision_id": "q16",
    "name": "CO2 in N2",
    "stage": "Liquid pre-autoclave gas treatment",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 7.5,
      "unit": "PERCENT",
      "qualifier": "Gas composition; source does not label v/v"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid pre-autoclave gas treatment",
        "exact_source_quote": "The medium was then bubbled with 7.5% CO 2 gas in N 2 (flow rate about 100 ml min −1 ) passed over heated copper wire to remove O 2 for 45 min.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Do not invent a v/v qualifier, copper temperature or pressure reference. This treatment precedes sealing and autoclaving."
  },
  {
    "decision_id": "q17",
    "name": "Gas flow",
    "stage": "Liquid pre-autoclave gas treatment",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 100,
      "unit": "ML_PER_MIN",
      "qualifier": "About"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid pre-autoclave gas treatment",
        "exact_source_quote": "The medium was then bubbled with 7.5% CO 2 gas in N 2 (flow rate about 100 ml min −1 ) passed over heated copper wire to remove O 2 for 45 min.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Do not invent a v/v qualifier, copper temperature or pressure reference. This treatment precedes sealing and autoclaving."
  },
  {
    "decision_id": "q18",
    "name": "Gas treatment duration",
    "stage": "Liquid pre-autoclave gas treatment",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 45,
      "unit": "MIN",
      "qualifier": "Gas passed over heated copper wire"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid pre-autoclave gas treatment",
        "exact_source_quote": "The medium was then bubbled with 7.5% CO 2 gas in N 2 (flow rate about 100 ml min −1 ) passed over heated copper wire to remove O 2 for 45 min.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Do not invent a v/v qualifier, copper temperature or pressure reference. This treatment precedes sealing and autoclaving."
  },
  {
    "decision_id": "q19",
    "name": "Autoclave cycle",
    "stage": "Liquid sterilization",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "temperature": null,
      "duration": null
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid sterilization",
        "exact_source_quote": "The medium was sealed and autoclaved.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "The paper names autoclaving without a temperature or duration; no collection default applies to this journal method."
  },
  {
    "decision_id": "q20",
    "name": "Phosphate buffer dose",
    "stage": "Liquid additions after autoclaving and cooling",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "value": 1.28,
      "unit": "ML",
      "basis": "Per medium bottle"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid additions after autoclaving and cooling",
        "exact_source_quote": "After the autoclaving and cooling steps, the following solutions were injected into the medium bottles, in order, from anaerobic stocks (except for the cysteine, which was made fresh and filter sterilized directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "These are later medium-bottle additions. The earlier per-liter clause is not carried across paragraphs. Keep stock recipe, dose, pH and physical state separate; KHPO4 is the printed buffer notation, not an inferred specific phosphate salt."
  },
  {
    "decision_id": "q21",
    "name": "Phosphate buffer strength",
    "stage": "Liquid additions after autoclaving and cooling",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "value": 0.5,
      "unit": "MOLAR",
      "basis": "KHPO4 source notation"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid additions after autoclaving and cooling",
        "exact_source_quote": "After the autoclaving and cooling steps, the following solutions were injected into the medium bottles, in order, from anaerobic stocks (except for the cysteine, which was made fresh and filter sterilized directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "These are later medium-bottle additions. The earlier per-liter clause is not carried across paragraphs. Keep stock recipe, dose, pH and physical state separate; KHPO4 is the printed buffer notation, not an inferred specific phosphate salt."
  },
  {
    "decision_id": "q22",
    "name": "Phosphate buffer pH",
    "stage": "Liquid additions after autoclaving and cooling",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "value": 6.9,
      "unit": "PH",
      "basis": "Stock pH"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid additions after autoclaving and cooling",
        "exact_source_quote": "After the autoclaving and cooling steps, the following solutions were injected into the medium bottles, in order, from anaerobic stocks (except for the cysteine, which was made fresh and filter sterilized directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "These are later medium-bottle additions. The earlier per-liter clause is not carried across paragraphs. Keep stock recipe, dose, pH and physical state separate; KHPO4 is the printed buffer notation, not an inferred specific phosphate salt."
  },
  {
    "decision_id": "q23",
    "name": "Neutralized cysteine hydrochloride monohydrate dose",
    "stage": "Liquid additions after autoclaving and cooling",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "value": 0.85,
      "unit": "ML",
      "basis": "Per medium bottle"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid additions after autoclaving and cooling",
        "exact_source_quote": "After the autoclaving and cooling steps, the following solutions were injected into the medium bottles, in order, from anaerobic stocks (except for the cysteine, which was made fresh and filter sterilized directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "These are later medium-bottle additions. The earlier per-liter clause is not carried across paragraphs. Keep stock recipe, dose, pH and physical state separate; KHPO4 is the printed buffer notation, not an inferred specific phosphate salt."
  },
  {
    "decision_id": "q24",
    "name": "Cysteine stock strength",
    "stage": "Liquid additions after autoclaving and cooling",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "value": 0.23,
      "unit": "MOLAR",
      "basis": "Fresh stock, filter-sterilized directly into medium"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid additions after autoclaving and cooling",
        "exact_source_quote": "After the autoclaving and cooling steps, the following solutions were injected into the medium bottles, in order, from anaerobic stocks (except for the cysteine, which was made fresh and filter sterilized directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "These are later medium-bottle additions. The earlier per-liter clause is not carried across paragraphs. Keep stock recipe, dose, pH and physical state separate; KHPO4 is the printed buffer notation, not an inferred specific phosphate salt."
  },
  {
    "decision_id": "q25",
    "name": "Sodium thiosulfate pentahydrate stock dose",
    "stage": "Liquid additions after autoclaving and cooling",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "value": 8.5,
      "unit": "ML",
      "basis": "Per medium bottle"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid additions after autoclaving and cooling",
        "exact_source_quote": "After the autoclaving and cooling steps, the following solutions were injected into the medium bottles, in order, from anaerobic stocks (except for the cysteine, which was made fresh and filter sterilized directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "These are later medium-bottle additions. The earlier per-liter clause is not carried across paragraphs. Keep stock recipe, dose, pH and physical state separate; KHPO4 is the printed buffer notation, not an inferred specific phosphate salt."
  },
  {
    "decision_id": "q26",
    "name": "Thiosulfate stock strength",
    "stage": "Liquid additions after autoclaving and cooling",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "value": 25,
      "unit": "PERCENT_W_V",
      "basis": "Explicit wt/vol stock"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid additions after autoclaving and cooling",
        "exact_source_quote": "After the autoclaving and cooling steps, the following solutions were injected into the medium bottles, in order, from anaerobic stocks (except for the cysteine, which was made fresh and filter sterilized directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "These are later medium-bottle additions. The earlier per-liter clause is not carried across paragraphs. Keep stock recipe, dose, pH and physical state separate; KHPO4 is the printed buffer notation, not an inferred specific phosphate salt."
  },
  {
    "decision_id": "q27",
    "name": "Vitamin solution dose",
    "stage": "Liquid additions after autoclaving and cooling",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "value": 0.4,
      "unit": "ML",
      "basis": "Per medium bottle; formula unresolved"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid additions after autoclaving and cooling",
        "exact_source_quote": "After the autoclaving and cooling steps, the following solutions were injected into the medium bottles, in order, from anaerobic stocks (except for the cysteine, which was made fresh and filter sterilized directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "These are later medium-bottle additions. The earlier per-liter clause is not carried across paragraphs. Keep stock recipe, dose, pH and physical state separate; KHPO4 is the printed buffer notation, not an inferred specific phosphate salt."
  },
  {
    "decision_id": "q28",
    "name": "FeSO4 stock dose",
    "stage": "Liquid iron addition after reduction",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "value": 2.5,
      "unit": "ML",
      "basis": "Per medium bottle after reduction"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid iron addition after reduction",
        "exact_source_quote": "The medium was allowed to become reduced (colorless), after which 2.5 ml of 0.01 M FeSO 4 dissolved in 0.2 N HCl was injected.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Do not choose a hydrate or convert normality to an unstated final concentration. The dose belongs to the medium bottle."
  },
  {
    "decision_id": "q29",
    "name": "FeSO4 stock strength",
    "stage": "Liquid iron addition after reduction",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "value": 0.01,
      "unit": "MOLAR",
      "basis": "Hydration unspecified"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid iron addition after reduction",
        "exact_source_quote": "The medium was allowed to become reduced (colorless), after which 2.5 ml of 0.01 M FeSO 4 dissolved in 0.2 N HCl was injected.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Do not choose a hydrate or convert normality to an unstated final concentration. The dose belongs to the medium bottle."
  },
  {
    "decision_id": "q30",
    "name": "HCl carrier strength",
    "stage": "Liquid iron addition after reduction",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "value": 0.2,
      "unit": "NORMAL",
      "basis": "Carrier acid, not final acid concentration"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid iron addition after reduction",
        "exact_source_quote": "The medium was allowed to become reduced (colorless), after which 2.5 ml of 0.01 M FeSO 4 dissolved in 0.2 N HCl was injected.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Do not choose a hydrate or convert normality to an unstated final concentration. The dose belongs to the medium bottle."
  },
  {
    "decision_id": "q31",
    "name": "Sterile O2 dose",
    "stage": "Liquid post-inoculation oxygen",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 6,
      "unit": "ML",
      "basis": "After inoculation"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid post-inoculation oxygen",
        "exact_source_quote": "The medium was inoculated, after which 6 ml of sterile O 2 was injected (0.4% of the headspace) and the medium was carefully placed without shaking so as not to disturb the forming [O 2 ] gradient, at 25°C.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Preserve both source-stated values without recomputing an exact headspace or treating gas percentage as dissolved concentration."
  },
  {
    "decision_id": "q32",
    "name": "Initial O2 headspace fraction",
    "stage": "Liquid post-inoculation oxygen",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 0.4,
      "unit": "PERCENT",
      "basis": "Source-stated headspace percentage"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Liquid post-inoculation oxygen",
        "exact_source_quote": "The medium was inoculated, after which 6 ml of sterile O 2 was injected (0.4% of the headspace) and the medium was carefully placed without shaking so as not to disturb the forming [O 2 ] gradient, at 25°C.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Preserve both source-stated values without recomputing an exact headspace or treating gas percentage as dissolved concentration."
  },
  {
    "decision_id": "q33",
    "name": "Liquid incubation temperature",
    "stage": "Source liquid method",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "temperature_value",
        "stored": null
      }
    ],
    "desired": {
      "value": 25,
      "unit": "DEG_C"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Source liquid method",
        "exact_source_quote": "The medium was inoculated, after which 6 ml of sterile O 2 was injected (0.4% of the headspace) and the medium was carefully placed without shaking so as not to disturb the forming [O 2 ] gradient, at 25°C.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "The generated target omits the maintained owner’s supported liquid temperature. Keep semisolid 28°C separate."
  },
  {
    "decision_id": "q34",
    "name": "Initial inoculum",
    "stage": "Primary Results / Growth experiments",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "Source: https://togomedium.org/medium/M2252"
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "TOGO M2252 reports a liquid artificial seawater base with 10 mM thiosulfate as the electron donor for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the cultivation context and state that cultures were incubated statically under an O2 gradient at 25 C in the dark."
      }
    ],
    "desired": {
      "value": 1,
      "unit": "PERCENT",
      "qualifier": "Results context; percentage basis not specified"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Primary Results / Growth experiments",
        "exact_source_quote": "an initial inoculum of 1%",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Record as source-specific experimental context, not a required formulation ingredient, general optimum or proof that the local abbreviated recipe reproduces this experiment."
  },
  {
    "decision_id": "q35",
    "name": "Initial growth-supporting O2",
    "stage": "Primary Results / Growth experiments",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "Source: https://togomedium.org/medium/M2252"
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "TOGO M2252 reports a liquid artificial seawater base with 10 mM thiosulfate as the electron donor for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the cultivation context and state that cultures were incubated statically under an O2 gradient at 25 C in the dark."
      }
    ],
    "desired": {
      "value": 0.5,
      "unit": "PERCENT",
      "qualifier": "Approximate result, not a universal set point"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Primary Results / Growth experiments",
        "exact_source_quote": "was about 0.5% O 2 in the headspace.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Record as source-specific experimental context, not a required formulation ingredient, general optimum or proof that the local abbreviated recipe reproduces this experiment."
  },
  {
    "decision_id": "q36",
    "name": "Later oxygen range",
    "stage": "Primary Results / Growth experiments",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "Source: https://togomedium.org/medium/M2252"
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "TOGO M2252 reports a liquid artificial seawater base with 10 mM thiosulfate as the electron donor for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the cultivation context and state that cultures were incubated statically under an O2 gradient at 25 C in the dark."
      }
    ],
    "desired": {
      "value": "4 to 5",
      "unit": "PERCENT",
      "qualifier": "Later established culture only"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Primary Results / Growth experiments",
        "exact_source_quote": "volumes of O 2 up to 4 to 5% of the headspace could be introduced",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Record as source-specific experimental context, not a required formulation ingredient, general optimum or proof that the local abbreviated recipe reproduces this experiment."
  },
  {
    "decision_id": "q37",
    "name": "Initial gradient-maintenance interval",
    "stage": "Primary Results / Growth experiments",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "Source: https://togomedium.org/medium/M2252"
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "TOGO M2252 reports a liquid artificial seawater base with 10 mM thiosulfate as the electron donor for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the cultivation context and state that cultures were incubated statically under an O2 gradient at 25 C in the dark."
      }
    ],
    "desired": {
      "value": "6 to 7",
      "unit": "DAYS",
      "qualifier": "Source growth observation"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Primary Results / Growth experiments",
        "exact_source_quote": "during the first 6 to 7 days after inoculation",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Record as source-specific experimental context, not a required formulation ingredient, general optimum or proof that the local abbreviated recipe reproduces this experiment."
  },
  {
    "decision_id": "q38",
    "name": "Average doubling time",
    "stage": "Primary Results / Growth experiments",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "Source: https://togomedium.org/medium/M2252"
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "TOGO M2252 reports a liquid artificial seawater base with 10 mM thiosulfate as the electron donor for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the cultivation context and state that cultures were incubated statically under an O2 gradient at 25 C in the dark."
      }
    ],
    "desired": {
      "value": 30,
      "unit": "HOURS",
      "qualifier": "Estimate in these gradient cultures"
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Primary Results / Growth experiments",
        "exact_source_quote": "we estimate an average doubling time of ∼30 h",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Record as source-specific experimental context, not a required formulation ingredient, general optimum or proof that the local abbreviated recipe reproduces this experiment."
  },
  {
    "decision_id": "q39",
    "name": "Unspecified later oxygen addition",
    "stage": "Established liquid culture",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "additional_dose_schedule": null
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Established liquid culture",
        "exact_source_quote": "greater amounts of sterile O 2 could be injected and used by growing cells.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "No universal dose schedule is given; retain the separately described later 4–5% headspace observation."
  },
  {
    "decision_id": "q40",
    "name": "ASW, elixir and vitamin complete formulas",
    "stage": "Unresolved external source recipes",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "artificial_seawater_formula": null,
      "modified_Wolfe_formula": null,
      "vitamin_formula": null
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Pre-autoclave list citing references 6 and 21",
        "exact_source_quote": "The medium consisted of an artificial seawater ( 6 ) base to which was added the following (per liter), in order, prior to autoclaving: 5 ml of modified Wolfe's mineral elixir ( 21 ), 0.25 g of NH 4 Cl, and 100 μl of 0.2% (wt/vol) aqueous resazurin.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      },
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Post-autoclave vitamin addition citing reference 21",
        "exact_source_quote": "After the autoclaving and cooling steps, the following solutions were injected into the medium bottles, in order, from anaerobic stocks (except for the cysteine, which was made fresh and filter sterilized directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Named source dependencies are not complete formulas in the inspected material. Do not substitute a familiar seawater, Wolfe or vitamin recipe."
  },
  {
    "decision_id": "q41",
    "name": "Semisolid gelling agent and amount",
    "stage": "Radiolabel variant",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "Source: https://togomedium.org/medium/M2252"
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "notes",
        "stored": "TOGO M2252 reports a liquid artificial seawater base with 10 mM thiosulfate as the electron donor for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the cultivation context and state that cultures were incubated statically under an O2 gradient at 25 C in the dark."
      }
    ],
    "desired": {
      "gelling_agent": null,
      "gelling_amount": null
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Radiolabel variant",
        "exact_source_quote": "cells of strain MC-1 were grown microaerobically in semisolid medium at 28°C",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "No gelling formula is supplied in this inspected paragraph; do not assume agar or a concentration."
  },
  {
    "decision_id": "q42",
    "name": "Measured final volume",
    "stage": "Liquid assembly",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "measured_final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Initial liquid-culture sentence",
        "exact_source_quote": "Cells were grown in 850 ml of medium in 2-liter glass bottles.",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      },
      {
        "source_key": "pmc1392968",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/",
        "source_locator": "Later bottle additions",
        "exact_source_quote": "After the autoclaving and cooling steps, the following solutions were injected into the medium bottles, in order, from anaerobic stocks (except for the cysteine, which was made fresh and filter sterilized directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).",
        "snapshot_sha256": "7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403",
        "parsed_text_sha256": "c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd"
      }
    ],
    "interpretation": "Preserve 850 mL and the sequential addition amounts without treating their arithmetic sum as a measured final volume."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:008841.

2 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 1/3 primary and 1/3 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 3: primary 33.33%; secondary 33.33%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:008841.

20 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact source and maintained owner

identity: supported. Targets: CultureMech:008841.

The generated target and single maintained owner resolve to TOGO M2252 and CultureMech:008841. The maintained owner’s later citation, oxygen and temperature content is absent from the generated snapshot. Primary experiments, secondary shorthand and the current owner are distinguishable rather than assumed identical.

### Complete source recipe and variants

completeness: concern. Targets: CultureMech:008841.

The primary method names components and stages missing from the three-entry shorthand; some may be hidden by the unresolved artificial-seawater base. The 10 mM primary statement is in the Table 1 caption for semisolid radiolabel culture. The liquid method uses a separate sodium-thiosulfate stock dose. Resolve their relationship without asserting wholesale omissions or a proven exact variant.

### Medium-specific MC-1 evidence and comparators

evidence: supported. Targets: CultureMech:008841.

The primary documents MC-1 growth in its own staged liquid and semisolid oxygen-gradient cultures, including failure without thiosulfate. PMID22581902 and current NCBI identify MC-1 as Magnetococcus marinus MC-1. This supports the cited experiments, not exact equivalence of the abbreviated local recipe. C. tepidum, R. rubrum, MV-1/MV-2 and broader taxon mentions do not establish growth on this record.

### Bibliography and historical source access

provenance: concern. Targets: CultureMech:008841.

All five inspected PubMed identities and twelve named taxonomy nodes are reconciled with their bounded roles. The owner correctly retains unresolved formulas, parent-only taxa and historical placement. Its October 14 named archives remain unrecovered; current abstracts and methods are independent current evidence, not historical byte verification.

### Source-specific preparation and conditions

completeness: concern. Targets: CultureMech:008841.

Inventory retains pre-autoclave per-liter additions, post-autoclave bottle doses, pH 7 versus buffer pH 6.9, 25°C liquid versus 28°C semisolid conditions, oxygen-gradient handling and source uncertainty. No autoclave cycle, complete stock formula, headspace arithmetic or final-volume conversion is supplied by inference.

### Physical state and composition classification

scope: concern. Targets: CultureMech:008841.

The local LIQUID state corresponds to the secondary and liquid primary context but must not absorb the semisolid Table 1 variant. Owner SEMI_DEFINED and target UNDEFINED differ; neither classification substitutes for resolving the exact base and stock formulas. Artificial seawater is a mixture and should not be forced to a single-compound ID.

## Findings

### f1: Canonical thiosulfate label masks the wrong chemical class

major / open / confirmed; issue key: culturemech.008841.wrong-thiosulfate-class.

Both layers assign CHEBI:26977, defined as an ester of thiosulfuric acid. The provider calls the donor inorganic thiosulfate and the liquid primary specifies sodium thiosulfate pentahydrate; the ester-class term cannot represent either merely by label agreement.

### f2: Generated artificial-seawater liquid volume has a mass unit

major / open / confirmed; issue key: culturemech.008841.base-volume-denominator.

The generated target stores the source-listed 1 L artificial-seawater input as 1 G_PER_L, a confirmed liquid-to-mass unit error. The owner’s 1000 ML_PER_L may instead be a normalization marker; its denominator and stage require evidence, but this row alone does not establish a numerical error in that owner value.

### f3: Three-entry shorthand does not resolve the primary culture recipes

major / open / confirmed; issue key: culturemech.008841.variant-stage-collapse.

The local liquid shorthand omits the paper’s stage structure. Its 10 mM value is supported secondarily, while the primary’s explicit 10 mM appears in the semisolid Table 1 caption. Missing named base/stock formulas prevent deciding which components are hidden by shorthand versus genuine recipe differences.

### f4: Useful citations do not attach formulation and condition claims

major / open / confirmed; issue key: culturemech.008841.missing-claim-evidence.

The maintained owner has extensive bounded bibliography and taxonomy notes, but the local amounts, temperature and preparation lack claim-level supporting evidence. Existing current source access does not authenticate the absent historical archive bytes.

### f5: Generated target predates maintained source and condition context

minor / open / confirmed; issue key: culturemech.008841.generated-owner-drift.

The merged target lacks the maintained owner’s citations, oxygen grounding, 25°C/static-gradient metadata and explicit formulation limitations. These later owner fields still require the corrections and evidence described here before propagation.

## Recommended Actions And Acceptance Checks

### a1

Re-ground the donor only after separating anion shorthand from the explicitly supplied sodium salt/hydrate; verify primary and secondary identifiers independently.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Correct the generated target’s mass unit using the source-listed liquid input, and authenticate the maintained owner’s normalization denominator and stage without presuming its 1000 mL/L marker is numerically false.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Recover the cited base and stock recipes, represent each experiment with its own quantities and preparation, and resolve equivalence or variants without mixing stage denominators.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach narrow current source excerpts to supported claims, retain the historical limitations, and distinguish provider-only dark incubation from primary methods.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Curate the maintained owner first, then regenerate and compare exact scientific fields without treating successful generation as source verification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch037/364/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch037/364/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml:1:id: CultureMech:008841<br>./data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml:1:id: CultureMech:008841<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch037/source-preflight-bound/364/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 30 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2252; $.components[0]; $.comments[0:2] | supports | Three-row secondary shorthand with 1 L artificial seawater, 10 mM thiosulfate and unquantified oxygen; static 25°C dark incubation is provider wording. |
| primary-methods | https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/; Materials and Methods / Bacteria and growth conditions | supports | The liquid method distinguishes per-liter additions before autoclaving from subsequent additions to the medium bottles. |
| primary-table1 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/; Table 1 caption, not its footnotes | supports | The explicit primary 10 mM amount belongs to semisolid radiolabel cultures; it does not establish the concentration of the separate liquid bottle recipe. |
| primary-growth | https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/; Results / Growth experiments | supports | MC-1 growth, oxygen-gradient dependence and the negative no-thiosulfate control apply to the paper’s specified cultures. Comparator recipes and enzyme-assay mixtures are excluded. |
| thiosulfate-definition | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26977; Exact CHEBI:26977 definition | refutes | The canonical label resolves, but the term denotes an ester class rather than the inorganic thiosulfate anion or sodium thiosulfate pentahydrate reagent. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch037/364/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15379 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15379; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15379 resolves to dioxygen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26977 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26977; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26977 resolves to thiosulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15379": [{"label": "Dioxygen", "match_type": "preferred_term", "identifier": "CHEBI:15379", "preferred_term": "Dioxygen", "ontology_id": "CHEBI:15379", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26977": [{"label": "Thiosulfate", "match_type": "preferred_term", "identifier": "CHEBI:26977", "preferred_term": "Thiosulfate", "ontology_id": "CHEBI:26977", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml; data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml", "events": 11, "timestamp_issues": []}] |
| pubmed-16461683 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=16461683,22581902,15338111,9251816,22984137&amp;retmode=xml; PubmedArticle with PMID 16461683; bibliography and abstract | supports | Primary MC-1 formulation and growth experiments; semisolid versus liquid scopes differ. |
| pubmed-22581902 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=16461683,22581902,15338111,9251816,22984137&amp;retmode=xml; PubmedArticle with PMID 22581902; bibliography and abstract | supports | MC-1 species/type-strain identity, not exact formulation support. |
| pubmed-15338111 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=16461683,22581902,15338111,9251816,22984137&amp;retmode=xml; PubmedArticle with PMID 15338111; bibliography and abstract | supports | Cited artificial-seawater source; abstract-only MV-1/MV-2 evidence, no complete formula. |
| pubmed-9251816 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=16461683,22581902,15338111,9251816,22984137&amp;retmode=xml; PubmedArticle with PMID 9251816; bibliography and abstract | supports | Cited mineral/vitamin source; available abstract and bibliographic page do not supply full recipes. |
| pubmed-22984137 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=16461683,22581902,15338111,9251816,22984137&amp;retmode=xml; PubmedArticle with PMID 22984137; bibliography and abstract | supports | Supporting identity for MV-1 at species rank, not an additional MC-1 growth claim. |
| bibliography-taxonomy | /private/tmp/culturemech-review-work-batch037/364/bibliography-taxonomy-inventory.json; Five PubMed identities and all twelve exact NCBI Taxon records | supports | All named taxa resolve with current rank, synonyms/type material and source-specific role. The owner already preserves broad-rank and historical-placement limits; no extra growth edge is inferred. |
| taxonomy-source | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1085,1097,1124597,1191478,1191479,13134,156889,162171,188,2,28181,28211&amp;retmode=xml; Exact top-level Taxon records and their lineage/type material | supports | Current names and ranks are checked separately from paper-era placement. |
| pmid15338111publisher-attempt | https://link.springer.com/article/10.1007/s00203-004-0716-y; Preserved exact public retrieval result | context_only | The current publisher route supplies bibliographic/abstract material but no inspected complete artificial-seawater recipe. The requested PDF route returned the same access page, not a usable full-text formula. |
| pmc1180996pdf-attempt | https://pmc.ncbi.nlm.nih.gov/articles/PMC1180996/pdf/biophysj00033-0446.pdf; Preserved exact public retrieval result | context_only | The requested 1997 primary PDF returned a download interstitial; its available PMC page supplies abstract/bibliography but not the complete modified Wolfe or vitamin formulas. |
| historical-limit | /private/tmp/culturemech-review-work-batch037/364/history-inventory.json; Exact prior partial review and ignored-inclusive archive search | context_only | Historical source hashes and local receipt claims are retained as provenance. Current usable source content does not recreate absent historical archives. Prior formal failures belong to that historical review and are not this record’s original canonical results. |
| writer-0 | scripts/repair_togo_m2252_artificial_seawater_thiosulfate_score15.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code was read to explain representation boundaries; its programmed 1000 ML_PER_L and label-based grounding do not authenticate the source denominator, chemical identity or historical execution. |
| writer-1 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code was read to explain representation boundaries; its programmed 1000 ML_PER_L and label-based grounding do not authenticate the source denominator, chemical identity or historical execution. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code was read to explain representation boundaries; its programmed 1000 ML_PER_L and label-based grounding do not authenticate the source denominator, chemical identity or historical execution. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The current publisher route supplies bibliographic/abstract material but no inspected complete artificial-seawater recipe. The requested PDF route returned the same access page, not a usable full-text formula.
- The requested 1997 primary PDF returned a download interstitial; its available PMC page supplies abstract/bibliography but not the complete modified Wolfe or vitamin formulas.
- The Table 1 caption supplies 10 mM for semisolid culture; the frozen preparatory context’s earlier footnote wording is superseded by the exact source locator used here.
- The five PubMed records and twelve taxonomy nodes were reviewed for the named roles, not as exhaustive full-paper organism inventories or a complete correction/retraction search.
- Comparator culture media, extraction buffers, enzyme assays, radiolabel analytical concentrations and general taxon optima are excluded from recipe transfer.
- No native growth association, new experiment or complete recipe reconstruction is asserted.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T202020Z-culturemech-008841-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: artificial_seawater_base_with_thiosulfate_as_the_electron_donor
  (CultureMech:008841)'
started_at: '2026-10-21T20:11:19Z'
finished_at: '2026-10-21T20:20:20Z'
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
summary: TOGO M2252 is a three-entry shorthand, not a complete reconstruction of the
  cited MC-1 experiments. The primary paper separates 10 mM semisolid radiolabel cultures
  from a staged liquid bottle recipe. The generated target is stale, the maintained
  owner adds useful bounded citation and taxonomy context, and both retain an ester-class
  grounding for the inorganic thiosulfate donor. Full artificial-seawater, mineral-elixir
  and vitamin formulas remain unavailable. The owner’s 1000 mL/L base value may be
  a normalization marker; its stage and denominator require evidence rather than a
  presumption of numerical error.
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
  - path: data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    sha256: e3813e31d455605d7586239a044a477ba54b73ee89a1c5e5e8a3044a12317789
    role: target
  - path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    sha256: b2c6926654ec9187c8ce41170af10727a42de3916bfb493c31854ead501aa82c
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
  - path: reviews/structured/20261014T023122Z-hopwood-magnetotactic-citations/review.md
    sha256: 2eb03b9e281dcc2b1834ef5d2ee9bedb081a85a27731dbcb4ad3a32562b9d5bd
    role: context
  - path: reviews/structured/20261014T023122Z-hopwood-magnetotactic-citations/review.yaml
    sha256: 8c2e563ec586bc6c7b635d8b772f8630f947b0fcb0a414e703694b596a4f4bd9
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
  - path: scripts/repair_togo_m2252_artificial_seawater_thiosulfate_score15.py
    sha256: 93780c67e91e65bd2a6e5286c95884b29d899bdb8f80c9cff63fc835fefa5bd2
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
  selection: Task review 364; batch 037 item 4 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-six task batches
    contain 360 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 363 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008841
targets:
- target_id: CultureMech:008841
  path: data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  label: artificial_seawater_base_with_thiosulfate_as_the_electron_donor
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch037/364/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch037/364/strict.tsv"
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008841
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
  - CultureMech:008841
- check_id: pmid15338111publisher-source-access
  name: 'Exact source content access: pmid15338111publisher'
  required: true
  status: unavailable
  summary: The current publisher route supplies bibliographic/abstract material but
    no inspected complete artificial-seawater recipe. The requested PDF route returned
    the same access page, not a usable full-text formula.
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - pmid15338111publisher-attempt
- check_id: pmc1180996pdf-source-access
  name: 'Exact source content access: pmc1180996pdf'
  required: true
  status: unavailable
  summary: The requested 1997 primary PDF returned a download interstitial; its available
    PMC page supplies abstract/bibliography but not the complete modified Wolfe or
    vitamin formulas.
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - pmc1180996pdf-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T20:20:18Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T20:20:18Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:11:56.844537Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch037/364/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T20:11:58.945191Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch037/364/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:01.440358Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:02.834155Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T20:20:18Z'
  support: supports
  summary: './data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml:1:id:
    CultureMech:008841

    ./data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml:1:id:
    CultureMech:008841

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/source-preflight-bound/364/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T20:20:18Z'
  support: supports
  summary: 30 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 4f8d86d50af032ba4b0b9e23607c36b4a92399d0d21f7a8a0ca4ff32edb09beb
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2252
  locator: $.components[0]; $.comments[0:2]
  accessed_at: '2026-10-21T19:52:54.033180Z'
  support: supports
  summary: Three-row secondary shorthand with 1 L artificial seawater, 10 mM thiosulfate
    and unquantified oxygen; static 25°C dark incubation is provider wording.
  quote: Cultures were incubated statically under an [O2] (O2 concentration) gradient
    at 25°C in the dark.
  snapshot_sha256: 1d34bc97fa49460f6db13a3405d5fa5bc0b369dbe850c8d7b68e882264e872b0
- evidence_id: primary-methods
  kind: database
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/
  locator: Materials and Methods / Bacteria and growth conditions
  accessed_at: '2026-10-21T19:52:51.677274Z'
  support: supports
  summary: The liquid method distinguishes per-liter additions before autoclaving
    from subsequent additions to the medium bottles.
  quote: Cells were grown in 850 ml of medium in 2-liter glass bottles.
  snapshot_sha256: 7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403
- evidence_id: primary-table1
  kind: database
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/
  locator: Table 1 caption, not its footnotes
  accessed_at: '2026-10-21T19:52:51.677274Z'
  support: supports
  summary: The explicit primary 10 mM amount belongs to semisolid radiolabel cultures;
    it does not establish the concentration of the separate liquid bottle recipe.
  quote: Contribution of CO 2 to protein carbon in cells of the magnetotactic coccus
    strain MC-1 grown in semisolid, oxygen-gradient medium containing 10 mM thiosulfate
    as the electron source
  snapshot_sha256: 7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403
- evidence_id: primary-growth
  kind: database
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/
  locator: Results / Growth experiments
  accessed_at: '2026-10-21T19:52:51.677274Z'
  support: supports
  summary: MC-1 growth, oxygen-gradient dependence and the negative no-thiosulfate
    control apply to the paper’s specified cultures. Comparator recipes and enzyme-assay
    mixtures are excluded.
  quote: Cells of strain MC-1 did not grow, however, when S 2 O 3 2− was omitted.
  snapshot_sha256: 7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403
- evidence_id: thiosulfate-definition
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26977
  locator: Exact CHEBI:26977 definition
  accessed_at: '2026-10-21T14:17:00.336648Z'
  support: refutes
  summary: The canonical label resolves, but the term denotes an ester class rather
    than the inorganic thiosulfate anion or sodium thiosulfate pentahydrate reagent.
  quote: An ester of thiosulfuric acid.
  snapshot_sha256: a990ebf9eb6a4ce57b8fa38f22d27790338a651ec0dfa07ef5564cdd952019c8
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/364/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T20:20:18Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: efac9c06ce79a663caaed18617d37cc88756218b7bd29dd644f67a25f3239013
- evidence_id: chebi15379
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15379
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T19:52:55.763130Z'
  support: supports
  summary: CHEBI:15379 resolves to dioxygen. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 68c310530d30379f78e9f302f3394ca9b8dde1bd84e32c60b439df1b6e12741c
- evidence_id: chebi26977
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26977
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T14:17:00.336648Z'
  support: supports
  summary: CHEBI:26977 resolves to thiosulfate. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: a990ebf9eb6a4ce57b8fa38f22d27790338a651ec0dfa07ef5564cdd952019c8
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T20:20:18Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15379":
    [{"label": "Dioxygen", "match_type": "preferred_term", "identifier": "CHEBI:15379",
    "preferred_term": "Dioxygen", "ontology_id": "CHEBI:15379", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26977": [{"label": "Thiosulfate", "match_type":
    "preferred_term", "identifier": "CHEBI:26977", "preferred_term": "Thiosulfate",
    "ontology_id": "CHEBI:26977", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml;
    data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T20:20:18Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml",
    "events": 11, "timestamp_issues": []}]'
- evidence_id: pubmed-16461683
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=16461683,22581902,15338111,9251816,22984137&retmode=xml
  locator: PubmedArticle with PMID 16461683; bibliography and abstract
  accessed_at: '2026-10-21T19:55:27.759548Z'
  support: supports
  summary: Primary MC-1 formulation and growth experiments; semisolid versus liquid
    scopes differ.
  quote: Evidence for autotrophy via the reverse tricarboxylic acid cycle in the marine
    magnetotactic coccus strain MC-1.
  snapshot_sha256: 724c082b353c99ebba0c0b421a8807a8f8c3b1817610d9ad82aeb55c3943dc15
- evidence_id: pubmed-22581902
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=16461683,22581902,15338111,9251816,22984137&retmode=xml
  locator: PubmedArticle with PMID 22581902; bibliography and abstract
  accessed_at: '2026-10-21T19:55:27.759548Z'
  support: supports
  summary: MC-1 species/type-strain identity, not exact formulation support.
  quote: Magnetococcus marinus gen. nov., sp. nov., a marine, magnetotactic bacterium
    that represents a novel lineage (Magnetococcaceae fam. nov., Magnetococcales ord.
    nov.) at the base of the Alphaproteobacteria.
  snapshot_sha256: 724c082b353c99ebba0c0b421a8807a8f8c3b1817610d9ad82aeb55c3943dc15
- evidence_id: pubmed-15338111
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=16461683,22581902,15338111,9251816,22984137&retmode=xml
  locator: PubmedArticle with PMID 15338111; bibliography and abstract
  accessed_at: '2026-10-21T19:55:27.759548Z'
  support: supports
  summary: Cited artificial-seawater source; abstract-only MV-1/MV-2 evidence, no
    complete formula.
  quote: Chemolithoautotrophy in the marine, magnetotactic bacterial strains MV-1
    and MV-2.
  snapshot_sha256: 724c082b353c99ebba0c0b421a8807a8f8c3b1817610d9ad82aeb55c3943dc15
- evidence_id: pubmed-9251816
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=16461683,22581902,15338111,9251816,22984137&retmode=xml
  locator: PubmedArticle with PMID 9251816; bibliography and abstract
  accessed_at: '2026-10-21T19:55:27.759548Z'
  support: supports
  summary: Cited mineral/vitamin source; available abstract and bibliographic page
    do not supply full recipes.
  quote: Magneto-aerotaxis in marine coccoid bacteria.
  snapshot_sha256: 724c082b353c99ebba0c0b421a8807a8f8c3b1817610d9ad82aeb55c3943dc15
- evidence_id: pubmed-22984137
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=16461683,22581902,15338111,9251816,22984137&retmode=xml
  locator: PubmedArticle with PMID 22984137; bibliography and abstract
  accessed_at: '2026-10-21T19:55:27.759548Z'
  support: supports
  summary: Supporting identity for MV-1 at species rank, not an additional MC-1 growth
    claim.
  quote: 'Magnetovibrio blakemorei gen. nov., sp. nov., a magnetotactic bacterium
    (Alphaproteobacteria: Rhodospirillaceae) isolated from a salt marsh.'
  snapshot_sha256: 724c082b353c99ebba0c0b421a8807a8f8c3b1817610d9ad82aeb55c3943dc15
- evidence_id: bibliography-taxonomy
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/364/bibliography-taxonomy-inventory.json
  locator: Five PubMed identities and all twelve exact NCBI Taxon records
  accessed_at: '2026-10-21T20:20:18Z'
  support: supports
  summary: All named taxa resolve with current rank, synonyms/type material and source-specific
    role. The owner already preserves broad-rank and historical-placement limits;
    no extra growth edge is inferred.
  snapshot_sha256: 0e7c9ee952f2fa5dbc38752d840f6596f103f54037ee2a3ecdae1fe961f39152
- evidence_id: taxonomy-source
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1085,1097,1124597,1191478,1191479,13134,156889,162171,188,2,28181,28211&retmode=xml
  locator: Exact top-level Taxon records and their lineage/type material
  accessed_at: '2026-10-21T19:55:28.790773Z'
  support: supports
  summary: Current names and ranks are checked separately from paper-era placement.
  quote: <ScientificName>Magnetococcus marinus MC-1</ScientificName>
  snapshot_sha256: 29ef034cd5bf1bb494ccb8171fcec61db43501ddfb748637805e470ef3b09a8f
- evidence_id: pmid15338111publisher-attempt
  kind: database
  reference: https://link.springer.com/article/10.1007/s00203-004-0716-y
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:55:31.506277Z'
  support: context_only
  summary: The current publisher route supplies bibliographic/abstract material but
    no inspected complete artificial-seawater recipe. The requested PDF route returned
    the same access page, not a usable full-text formula.
  snapshot_sha256: c29f47fa4c571008b93cfda59f8797cab1b3565cf1e67c2e78d7166722d42bcb
- evidence_id: pmc1180996pdf-attempt
  kind: database
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1180996/pdf/biophysj00033-0446.pdf
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:55:30.729103Z'
  support: context_only
  summary: The requested 1997 primary PDF returned a download interstitial; its available
    PMC page supplies abstract/bibliography but not the complete modified Wolfe or
    vitamin formulas.
  snapshot_sha256: f39536d99e842dcc4f1fc840ddb01c8f8378326d82cd7ee408c29ff2047c5f35
- evidence_id: historical-limit
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/364/history-inventory.json
  locator: Exact prior partial review and ignored-inclusive archive search
  accessed_at: '2026-10-21T20:20:18Z'
  support: context_only
  summary: Historical source hashes and local receipt claims are retained as provenance.
    Current usable source content does not recreate absent historical archives. Prior
    formal failures belong to that historical review and are not this record’s original
    canonical results.
  snapshot_sha256: 3ba091bab6b29d6a664d9876987c43533c8697d12e6503054df757c5550ac132
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_togo_m2252_artificial_seawater_thiosulfate_score15.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:20:18Z'
  support: context_only
  summary: Current code was read to explain representation boundaries; its programmed
    1000 ML_PER_L and label-based grounding do not authenticate the source denominator,
    chemical identity or historical execution.
  snapshot_sha256: 93780c67e91e65bd2a6e5286c95884b29d899bdb8f80c9cff63fc835fefa5bd2
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:20:18Z'
  support: context_only
  summary: Current code was read to explain representation boundaries; its programmed
    1000 ML_PER_L and label-based grounding do not authenticate the source denominator,
    chemical identity or historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:20:18Z'
  support: context_only
  summary: Current code was read to explain representation boundaries; its programmed
    1000 ML_PER_L and label-based grounding do not authenticate the source denominator,
    chemical identity or historical execution.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 42 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Artificial seawater\
    \ base\",\n    \"stage\": \"Generated secondary shorthand\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 1,\n      \"unit\": \"\
    L\",\n      \"basis\": \"Listed base input, not a measured final volume\"\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2252original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2252\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Artificial seawater\\\",\\n          \\\"volume\\\
    \": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"\
    1d34bc97fa49460f6db13a3405d5fa5bc0b369dbe850c8d7b68e882264e872b0\"\n      }\n\
    \    ],\n    \"interpretation\": \"The provider supplies a liquid base volume;\
    \ 1 G_PER_L is unsupported. The exact base composition remains unresolved.\"\n\
    \  },\n  {\n    \"decision_id\": \"q2\",\n    \"name\": \"Artificial seawater\
    \ base denominator\",\n    \"stage\": \"Maintained secondary shorthand\",\n  \
    \  \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"ML_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"value\": 1000,\n      \"\
    unit\": \"ML_PER_L\",\n      \"basis\": \"Existing normalization marker; denominator/stage\
    \ evidence unresolved\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"togoM2252original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2252\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Artificial seawater\\\",\\n          \\\"volume\\\
    \": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"\
    1d34bc97fa49460f6db13a3405d5fa5bc0b369dbe850c8d7b68e882264e872b0\"\n      }\n\
    \    ],\n    \"interpretation\": \"The owner’s 1000 mL/L may be a normalization\
    \ marker for the unresolved artificial-seawater base. The provider supports a\
    \ 1 L base input, but does not independently establish the owner’s normalization\
    \ denominator or a measured final-medium ratio. Retain the numerical marker pending\
    \ stage/basis evidence; it is not demonstrated numerically false.\"\n  },\n  {\n\
    \    \"decision_id\": \"q3\",\n    \"name\": \"Thiosulfate\",\n    \"stage\":\
    \ \"Secondary three-entry shorthand\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"MILLIMOLAR\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"MILLIMOLAR\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"value\": 10,\n      \"unit\"\
    : \"MILLIMOLAR\",\n      \"scope\": \"Exact TOGO shorthand; primary 10 mM independently\
    \ belongs to semisolid variant\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2252original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2252\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"thiosulfate\\\",\\n          \\\"volume\\\": 10,\\\
    n          \\\"unit\\\": \\\"mM\\\"\",\n        \"snapshot_sha256\": \"1d34bc97fa49460f6db13a3405d5fa5bc0b369dbe850c8d7b68e882264e872b0\"\
    \n      },\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Table 1 caption\",\n        \"exact_source_quote\": \"Contribution of CO 2\
    \ to protein carbon in cells of the magnetotactic coccus strain MC-1 grown in\
    \ semisolid, oxygen-gradient medium containing 10 mM thiosulfate as the electron\
    \ source\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"The local value agrees with the provider,\
    \ but neither layer has attached claim-level amount evidence. Do not merge the\
    \ primary semisolid quantity with the separate liquid post-autoclave stock dose.\"\
    \n  },\n  {\n    \"decision_id\": \"q4\",\n    \"name\": \"Oxygen\",\n    \"stage\"\
    : \"Secondary gas entry\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"dissolved_concentration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM2252original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2252\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"O2\\\"\",\n        \"snapshot_sha256\": \"1d34bc97fa49460f6db13a3405d5fa5bc0b369dbe850c8d7b68e882264e872b0\"\
    \n      }\n    ],\n    \"interpretation\": \"A variable gas entry has no numerical\
    \ concentration. Primary bottle-gas volumes and headspace percentages are separate\
    \ observations, not dissolved oxygen concentrations.\"\n  },\n  {\n    \"decision_id\"\
    : \"q5\",\n    \"name\": \"Incubation temperature\",\n    \"stage\": \"Maintained\
    \ liquid/provider scope\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": 25.0\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"TOGO M2252 reports\
    \ a liquid artificial seawater base with 10 mM thiosulfate as the electron donor\
    \ for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the\
    \ cultivation context and state that cultures were incubated statically under\
    \ an O2 gradient at 25 C in the dark.\"\n      }\n    ],\n    \"desired\": {\n\
    \      \"value\": 25,\n      \"unit\": \"DEG_C\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM2252original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2252\",\n\
    \        \"source_locator\": \"$.comments[1]\",\n        \"exact_source_quote\"\
    : \"Cultures were incubated statically under an [O2] (O2 concentration) gradient\
    \ at 25°C in the dark.\",\n        \"snapshot_sha256\": \"1d34bc97fa49460f6db13a3405d5fa5bc0b369dbe850c8d7b68e882264e872b0\"\
    ,\n        \"parsed_text_sha256\": \"be035e46506ad7db91dda885f66a9c76a24965ac000816e0d42a3f3d8850c259\"\
    \n      },\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Materials and Methods, liquid incubation sentence\",\n        \"exact_source_quote\"\
    : \"at 25°C.\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner’s 25°C agrees with both\
    \ the provider and liquid primary context but lacks attached amount evidence.\
    \ Darkness is supported by the provider text only.\"\n  },\n  {\n    \"decision_id\"\
    : \"q6\",\n    \"name\": \"Semisolid temperature\",\n    \"stage\": \"Radiolabel\
    \ variant\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: https://togomedium.org/medium/M2252\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"TOGO M2252 reports\
    \ a liquid artificial seawater base with 10 mM thiosulfate as the electron donor\
    \ for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the\
    \ cultivation context and state that cultures were incubated statically under\
    \ an O2 gradient at 25 C in the dark.\"\n      }\n    ],\n    \"desired\": {\n\
    \      \"value\": 28,\n      \"unit\": \"DEG_C\",\n      \"physical_state\": \"\
    SEMISOLID\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"pmc1392968\",\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Radiolabel variant\",\n        \"exact_source_quote\"\
    : \"cells of strain MC-1 were grown microaerobically in semisolid medium at 28°C\"\
    ,\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Keep this as a separate source-specific\
    \ experiment; do not replace the liquid owner’s temperature.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q7\",\n    \"name\": \"Semisolid thiosulfate\",\n    \"\
    stage\": \"Radiolabel variant\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: https://togomedium.org/medium/M2252\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"TOGO M2252 reports\
    \ a liquid artificial seawater base with 10 mM thiosulfate as the electron donor\
    \ for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the\
    \ cultivation context and state that cultures were incubated statically under\
    \ an O2 gradient at 25 C in the dark.\"\n      }\n    ],\n    \"desired\": {\n\
    \      \"value\": 10,\n      \"unit\": \"MILLIMOLAR\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Radiolabel variant\",\n        \"exact_source_quote\": \"Contribution of CO\
    \ 2 to protein carbon in cells of the magnetotactic coccus strain MC-1 grown in\
    \ semisolid, oxygen-gradient medium containing 10 mM thiosulfate as the electron\
    \ source\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"This is an explicit Table 1 caption\
    \ quantity, not a footnote or proof that the liquid recipe has the same concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q8\",\n    \"name\": \"Liquid culture volume\"\
    ,\n    \"stage\": \"Liquid enzyme/lipid/isotope culture\",\n    \"decision\":\
    \ \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 850,\n      \"unit\": \"\
    ML\",\n      \"basis\": \"Stated culture-medium volume in bottle\"\n    },\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"pmc1392968\",\n\
    \        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid enzyme/lipid/isotope culture\",\n    \
    \    \"exact_source_quote\": \"Cells were grown in 850 ml of medium in 2-liter\
    \ glass bottles.\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the stated liquid-culture\
    \ volume; it is not license to rebase every later bottle addition to one liter\
    \ or infer a measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q9\"\
    ,\n    \"name\": \"Bottle volume\",\n    \"stage\": \"Liquid enzyme/lipid/isotope\
    \ culture\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 2,\n      \"unit\": \"\
    L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"pmc1392968\"\
    ,\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid enzyme/lipid/isotope culture\",\n    \
    \    \"exact_source_quote\": \"Cells were grown in 850 ml of medium in 2-liter\
    \ glass bottles.\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Vessel capacity is distinct from\
    \ liquid-medium volume and actual headspace after additions.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q10\",\n    \"name\": \"Modified Wolfe mineral elixir dose\"\
    ,\n    \"stage\": \"Liquid medium before autoclaving\",\n    \"decision\": \"\
    add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Artificial seawater\",\n            \"\
    concentration\": {\n              \"value\": \"1\",\n              \"unit\": \"\
    G_PER_L\"\n            },\n            \"notes\": \"Role: Solvating media, Mineral\
    \ source; Properties: Complex component, Defined component, Solution\"\n     \
    \     },\n          {\n            \"preferred_term\": \"thiosulfate\",\n    \
    \        \"concentration\": {\n              \"value\": \"10\",\n            \
    \  \"unit\": \"MILLIMOLAR\"\n            },\n            \"notes\": \"Role: Growth\
    \ factor; Properties: Defined component, Inorganic compound, Simple component\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:26977\",\n         \
    \     \"label\": \"thiosulfate\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:26977\",\n              \"label\": \"thiosulfate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    O2\",\n            \"notes\": \"Properties: Gas\",\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            }\n          }\n        ]\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Artificial seawater\",\n            \"\
    concentration\": {\n              \"value\": \"1000.0\",\n              \"unit\"\
    : \"ML_PER_L\"\n            },\n            \"source\": \"TOGO M2252\",\n    \
    \        \"notes\": \"TOGO M2252 lists 1 L Artificial seawater as the base; this\
    \ artificial seawater mixture is retained without a single-compound ontology grounding.\"\
    \n          },\n          {\n            \"preferred_term\": \"thiosulfate\",\n\
    \            \"concentration\": {\n              \"value\": \"10.0\",\n      \
    \        \"unit\": \"MILLIMOLAR\"\n            },\n            \"source\": \"\
    TOGO M2252\",\n            \"notes\": \"TOGO M2252 lists 10 mM thiosulfate as\
    \ the electron donor.\",\n            \"term\": {\n              \"id\": \"CHEBI:26977\"\
    ,\n              \"label\": \"thiosulfate\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:26977\",\n              \"label\": \"thiosulfate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Oxygen gas\",\n            \"concentration\": {\n              \"value\": \"variable\"\
    ,\n              \"unit\": \"VARIABLE\"\n            },\n            \"source\"\
    : \"TOGO M2252\",\n            \"notes\": \"TOGO M2252 lists O2 and states that\
    \ cultures were incubated statically under an O2 gradient.\",\n            \"\
    term\": {\n              \"id\": \"CHEBI:15379\",\n              \"label\": \"\
    dioxygen\"\n            },\n            \"mediaingredientmech_chebi_term\": {\n\
    \              \"id\": \"CHEBI:15379\",\n              \"label\": \"dioxygen\"\
    \n            }\n          }\n        ]\n      }\n    ],\n    \"desired\": {\n\
    \      \"value\": 5,\n      \"unit\": \"ML_PER_L\",\n      \"basis\": \"Before\
    \ autoclaving\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"pmc1392968\",\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid medium before autoclaving\",\n       \
    \ \"exact_source_quote\": \"The medium consisted of an artificial seawater ( 6\
    \ ) base to which was added the following (per liter), in order, prior to autoclaving:\
    \ 5 ml of modified Wolfe's mineral elixir ( 21 ), 0.25 g of NH 4 Cl, and 100 μl\
    \ of 0.2% (wt/vol) aqueous resazurin.\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"The per-liter clause applies explicitly\
    \ to this pre-autoclave list. Stock dose and stock strength are separate; the\
    \ modified Wolfe formula is not recovered.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q11\",\n    \"name\": \"NH4Cl\",\n    \"stage\": \"Liquid medium before autoclaving\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Artificial seawater\",\n            \"\
    concentration\": {\n              \"value\": \"1\",\n              \"unit\": \"\
    G_PER_L\"\n            },\n            \"notes\": \"Role: Solvating media, Mineral\
    \ source; Properties: Complex component, Defined component, Solution\"\n     \
    \     },\n          {\n            \"preferred_term\": \"thiosulfate\",\n    \
    \        \"concentration\": {\n              \"value\": \"10\",\n            \
    \  \"unit\": \"MILLIMOLAR\"\n            },\n            \"notes\": \"Role: Growth\
    \ factor; Properties: Defined component, Inorganic compound, Simple component\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:26977\",\n         \
    \     \"label\": \"thiosulfate\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:26977\",\n              \"label\": \"thiosulfate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    O2\",\n            \"notes\": \"Properties: Gas\",\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            }\n          }\n        ]\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Artificial seawater\",\n            \"\
    concentration\": {\n              \"value\": \"1000.0\",\n              \"unit\"\
    : \"ML_PER_L\"\n            },\n            \"source\": \"TOGO M2252\",\n    \
    \        \"notes\": \"TOGO M2252 lists 1 L Artificial seawater as the base; this\
    \ artificial seawater mixture is retained without a single-compound ontology grounding.\"\
    \n          },\n          {\n            \"preferred_term\": \"thiosulfate\",\n\
    \            \"concentration\": {\n              \"value\": \"10.0\",\n      \
    \        \"unit\": \"MILLIMOLAR\"\n            },\n            \"source\": \"\
    TOGO M2252\",\n            \"notes\": \"TOGO M2252 lists 10 mM thiosulfate as\
    \ the electron donor.\",\n            \"term\": {\n              \"id\": \"CHEBI:26977\"\
    ,\n              \"label\": \"thiosulfate\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:26977\",\n              \"label\": \"thiosulfate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Oxygen gas\",\n            \"concentration\": {\n              \"value\": \"variable\"\
    ,\n              \"unit\": \"VARIABLE\"\n            },\n            \"source\"\
    : \"TOGO M2252\",\n            \"notes\": \"TOGO M2252 lists O2 and states that\
    \ cultures were incubated statically under an O2 gradient.\",\n            \"\
    term\": {\n              \"id\": \"CHEBI:15379\",\n              \"label\": \"\
    dioxygen\"\n            },\n            \"mediaingredientmech_chebi_term\": {\n\
    \              \"id\": \"CHEBI:15379\",\n              \"label\": \"dioxygen\"\
    \n            }\n          }\n        ]\n      }\n    ],\n    \"desired\": {\n\
    \      \"value\": 0.25,\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Before\
    \ autoclaving\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"pmc1392968\",\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid medium before autoclaving\",\n       \
    \ \"exact_source_quote\": \"The medium consisted of an artificial seawater ( 6\
    \ ) base to which was added the following (per liter), in order, prior to autoclaving:\
    \ 5 ml of modified Wolfe's mineral elixir ( 21 ), 0.25 g of NH 4 Cl, and 100 μl\
    \ of 0.2% (wt/vol) aqueous resazurin.\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"The per-liter clause applies explicitly\
    \ to this pre-autoclave list. Stock dose and stock strength are separate; the\
    \ modified Wolfe formula is not recovered.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q12\",\n    \"name\": \"Resazurin stock dose\",\n    \"stage\": \"Liquid medium\
    \ before autoclaving\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Artificial seawater\",\n            \"\
    concentration\": {\n              \"value\": \"1\",\n              \"unit\": \"\
    G_PER_L\"\n            },\n            \"notes\": \"Role: Solvating media, Mineral\
    \ source; Properties: Complex component, Defined component, Solution\"\n     \
    \     },\n          {\n            \"preferred_term\": \"thiosulfate\",\n    \
    \        \"concentration\": {\n              \"value\": \"10\",\n            \
    \  \"unit\": \"MILLIMOLAR\"\n            },\n            \"notes\": \"Role: Growth\
    \ factor; Properties: Defined component, Inorganic compound, Simple component\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:26977\",\n         \
    \     \"label\": \"thiosulfate\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:26977\",\n              \"label\": \"thiosulfate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    O2\",\n            \"notes\": \"Properties: Gas\",\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            }\n          }\n        ]\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Artificial seawater\",\n            \"\
    concentration\": {\n              \"value\": \"1000.0\",\n              \"unit\"\
    : \"ML_PER_L\"\n            },\n            \"source\": \"TOGO M2252\",\n    \
    \        \"notes\": \"TOGO M2252 lists 1 L Artificial seawater as the base; this\
    \ artificial seawater mixture is retained without a single-compound ontology grounding.\"\
    \n          },\n          {\n            \"preferred_term\": \"thiosulfate\",\n\
    \            \"concentration\": {\n              \"value\": \"10.0\",\n      \
    \        \"unit\": \"MILLIMOLAR\"\n            },\n            \"source\": \"\
    TOGO M2252\",\n            \"notes\": \"TOGO M2252 lists 10 mM thiosulfate as\
    \ the electron donor.\",\n            \"term\": {\n              \"id\": \"CHEBI:26977\"\
    ,\n              \"label\": \"thiosulfate\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:26977\",\n              \"label\": \"thiosulfate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Oxygen gas\",\n            \"concentration\": {\n              \"value\": \"variable\"\
    ,\n              \"unit\": \"VARIABLE\"\n            },\n            \"source\"\
    : \"TOGO M2252\",\n            \"notes\": \"TOGO M2252 lists O2 and states that\
    \ cultures were incubated statically under an O2 gradient.\",\n            \"\
    term\": {\n              \"id\": \"CHEBI:15379\",\n              \"label\": \"\
    dioxygen\"\n            },\n            \"mediaingredientmech_chebi_term\": {\n\
    \              \"id\": \"CHEBI:15379\",\n              \"label\": \"dioxygen\"\
    \n            }\n          }\n        ]\n      }\n    ],\n    \"desired\": {\n\
    \      \"value\": 100,\n      \"unit\": \"MICROLITER_PER_L\",\n      \"basis\"\
    : \"Before autoclaving\"\n    },\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"pmc1392968\",\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid medium before autoclaving\",\n       \
    \ \"exact_source_quote\": \"The medium consisted of an artificial seawater ( 6\
    \ ) base to which was added the following (per liter), in order, prior to autoclaving:\
    \ 5 ml of modified Wolfe's mineral elixir ( 21 ), 0.25 g of NH 4 Cl, and 100 μl\
    \ of 0.2% (wt/vol) aqueous resazurin.\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"The per-liter clause applies explicitly\
    \ to this pre-autoclave list. Stock dose and stock strength are separate; the\
    \ modified Wolfe formula is not recovered.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q13\",\n    \"name\": \"Resazurin stock strength\",\n    \"stage\": \"Liquid\
    \ medium before autoclaving\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Artificial seawater\",\n            \"\
    concentration\": {\n              \"value\": \"1\",\n              \"unit\": \"\
    G_PER_L\"\n            },\n            \"notes\": \"Role: Solvating media, Mineral\
    \ source; Properties: Complex component, Defined component, Solution\"\n     \
    \     },\n          {\n            \"preferred_term\": \"thiosulfate\",\n    \
    \        \"concentration\": {\n              \"value\": \"10\",\n            \
    \  \"unit\": \"MILLIMOLAR\"\n            },\n            \"notes\": \"Role: Growth\
    \ factor; Properties: Defined component, Inorganic compound, Simple component\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:26977\",\n         \
    \     \"label\": \"thiosulfate\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:26977\",\n              \"label\": \"thiosulfate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    O2\",\n            \"notes\": \"Properties: Gas\",\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            }\n          }\n        ]\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Artificial seawater\",\n            \"\
    concentration\": {\n              \"value\": \"1000.0\",\n              \"unit\"\
    : \"ML_PER_L\"\n            },\n            \"source\": \"TOGO M2252\",\n    \
    \        \"notes\": \"TOGO M2252 lists 1 L Artificial seawater as the base; this\
    \ artificial seawater mixture is retained without a single-compound ontology grounding.\"\
    \n          },\n          {\n            \"preferred_term\": \"thiosulfate\",\n\
    \            \"concentration\": {\n              \"value\": \"10.0\",\n      \
    \        \"unit\": \"MILLIMOLAR\"\n            },\n            \"source\": \"\
    TOGO M2252\",\n            \"notes\": \"TOGO M2252 lists 10 mM thiosulfate as\
    \ the electron donor.\",\n            \"term\": {\n              \"id\": \"CHEBI:26977\"\
    ,\n              \"label\": \"thiosulfate\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:26977\",\n              \"label\": \"thiosulfate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Oxygen gas\",\n            \"concentration\": {\n              \"value\": \"variable\"\
    ,\n              \"unit\": \"VARIABLE\"\n            },\n            \"source\"\
    : \"TOGO M2252\",\n            \"notes\": \"TOGO M2252 lists O2 and states that\
    \ cultures were incubated statically under an O2 gradient.\",\n            \"\
    term\": {\n              \"id\": \"CHEBI:15379\",\n              \"label\": \"\
    dioxygen\"\n            },\n            \"mediaingredientmech_chebi_term\": {\n\
    \              \"id\": \"CHEBI:15379\",\n              \"label\": \"dioxygen\"\
    \n            }\n          }\n        ]\n      }\n    ],\n    \"desired\": {\n\
    \      \"value\": 0.2,\n      \"unit\": \"PERCENT_W_V\",\n      \"basis\": \"\
    Stock strength, not final concentration\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\": \"\
    https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Liquid medium before autoclaving\",\n        \"exact_source_quote\": \"The\
    \ medium consisted of an artificial seawater ( 6 ) base to which was added the\
    \ following (per liter), in order, prior to autoclaving: 5 ml of modified Wolfe's\
    \ mineral elixir ( 21 ), 0.25 g of NH 4 Cl, and 100 μl of 0.2% (wt/vol) aqueous\
    \ resazurin.\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"The per-liter clause applies explicitly\
    \ to this pre-autoclave list. Stock dose and stock strength are separate; the\
    \ modified Wolfe formula is not recovered.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q14\",\n    \"name\": \"Main pH\",\n    \"stage\": \"Liquid medium before\
    \ gas treatment\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 7.0,\n      \"unit\": \"\
    PH\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    pmc1392968\",\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid medium before gas treatment\",\n     \
    \   \"exact_source_quote\": \"The pH of the medium was adjusted to 7.0, 1.26 g\
    \ of NaHCO 3 was added per liter, and the vessel was sealed.\",\n        \"snapshot_sha256\"\
    : \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\",\n    \
    \    \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the main pH and explicitly\
    \ per-liter bicarbonate separately from later buffer pH.\"\n  },\n  {\n    \"\
    decision_id\": \"q15\",\n    \"name\": \"NaHCO3\",\n    \"stage\": \"Liquid medium\
    \ before gas treatment\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 1.26,\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"pmc1392968\",\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid medium before gas treatment\",\n     \
    \   \"exact_source_quote\": \"The pH of the medium was adjusted to 7.0, 1.26 g\
    \ of NaHCO 3 was added per liter, and the vessel was sealed.\",\n        \"snapshot_sha256\"\
    : \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\",\n    \
    \    \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the main pH and explicitly\
    \ per-liter bicarbonate separately from later buffer pH.\"\n  },\n  {\n    \"\
    decision_id\": \"q16\",\n    \"name\": \"CO2 in N2\",\n    \"stage\": \"Liquid\
    \ pre-autoclave gas treatment\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 7.5,\n      \"unit\": \"\
    PERCENT\",\n      \"qualifier\": \"Gas composition; source does not label v/v\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"pmc1392968\"\
    ,\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid pre-autoclave gas treatment\",\n     \
    \   \"exact_source_quote\": \"The medium was then bubbled with 7.5% CO 2 gas in\
    \ N 2 (flow rate about 100 ml min −1 ) passed over heated copper wire to remove\
    \ O 2 for 45 min.\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Do not invent a v/v qualifier, copper\
    \ temperature or pressure reference. This treatment precedes sealing and autoclaving.\"\
    \n  },\n  {\n    \"decision_id\": \"q17\",\n    \"name\": \"Gas flow\",\n    \"\
    stage\": \"Liquid pre-autoclave gas treatment\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 100,\n      \"unit\": \"\
    ML_PER_MIN\",\n      \"qualifier\": \"About\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Liquid pre-autoclave gas treatment\",\n        \"exact_source_quote\": \"\
    The medium was then bubbled with 7.5% CO 2 gas in N 2 (flow rate about 100 ml\
    \ min −1 ) passed over heated copper wire to remove O 2 for 45 min.\",\n     \
    \   \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Do not invent a v/v qualifier, copper\
    \ temperature or pressure reference. This treatment precedes sealing and autoclaving.\"\
    \n  },\n  {\n    \"decision_id\": \"q18\",\n    \"name\": \"Gas treatment duration\"\
    ,\n    \"stage\": \"Liquid pre-autoclave gas treatment\",\n    \"decision\": \"\
    add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 45,\n      \"unit\": \"\
    MIN\",\n      \"qualifier\": \"Gas passed over heated copper wire\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"pmc1392968\",\n\
    \        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid pre-autoclave gas treatment\",\n     \
    \   \"exact_source_quote\": \"The medium was then bubbled with 7.5% CO 2 gas in\
    \ N 2 (flow rate about 100 ml min −1 ) passed over heated copper wire to remove\
    \ O 2 for 45 min.\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Do not invent a v/v qualifier, copper\
    \ temperature or pressure reference. This treatment precedes sealing and autoclaving.\"\
    \n  },\n  {\n    \"decision_id\": \"q19\",\n    \"name\": \"Autoclave cycle\"\
    ,\n    \"stage\": \"Liquid sterilization\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"temperature\": null,\n      \"duration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    pmc1392968\",\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid sterilization\",\n        \"exact_source_quote\"\
    : \"The medium was sealed and autoclaved.\",\n        \"snapshot_sha256\": \"\
    7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\",\n        \"\
    parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"The paper names autoclaving without\
    \ a temperature or duration; no collection default applies to this journal method.\"\
    \n  },\n  {\n    \"decision_id\": \"q20\",\n    \"name\": \"Phosphate buffer dose\"\
    ,\n    \"stage\": \"Liquid additions after autoclaving and cooling\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": 1.28,\n      \"unit\": \"ML\",\n\
    \      \"basis\": \"Per medium bottle\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\": \"\
    https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Liquid additions after autoclaving and cooling\",\n        \"exact_source_quote\"\
    : \"After the autoclaving and cooling steps, the following solutions were injected\
    \ into the medium bottles, in order, from anaerobic stocks (except for the cysteine,\
    \ which was made fresh and filter sterilized directly into the medium): 1.28 ml\
    \ of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl\
    \ · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin\
    \ solution ( 21 ).\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"These are later medium-bottle additions.\
    \ The earlier per-liter clause is not carried across paragraphs. Keep stock recipe,\
    \ dose, pH and physical state separate; KHPO4 is the printed buffer notation,\
    \ not an inferred specific phosphate salt.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q21\",\n    \"name\": \"Phosphate buffer strength\",\n    \"stage\": \"Liquid\
    \ additions after autoclaving and cooling\",\n    \"decision\": \"add\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": 0.5,\n      \"unit\": \"MOLAR\"\
    ,\n      \"basis\": \"KHPO4 source notation\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Liquid additions after autoclaving and cooling\",\n        \"exact_source_quote\"\
    : \"After the autoclaving and cooling steps, the following solutions were injected\
    \ into the medium bottles, in order, from anaerobic stocks (except for the cysteine,\
    \ which was made fresh and filter sterilized directly into the medium): 1.28 ml\
    \ of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl\
    \ · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin\
    \ solution ( 21 ).\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"These are later medium-bottle additions.\
    \ The earlier per-liter clause is not carried across paragraphs. Keep stock recipe,\
    \ dose, pH and physical state separate; KHPO4 is the printed buffer notation,\
    \ not an inferred specific phosphate salt.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q22\",\n    \"name\": \"Phosphate buffer pH\",\n    \"stage\": \"Liquid additions\
    \ after autoclaving and cooling\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": 6.9,\n      \"unit\": \"PH\",\n\
    \      \"basis\": \"Stock pH\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"pmc1392968\",\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid additions after autoclaving and cooling\"\
    ,\n        \"exact_source_quote\": \"After the autoclaving and cooling steps,\
    \ the following solutions were injected into the medium bottles, in order, from\
    \ anaerobic stocks (except for the cysteine, which was made fresh and filter sterilized\
    \ directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of\
    \ 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O\
    \ 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).\",\n        \"snapshot_sha256\"\
    : \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\",\n    \
    \    \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"These are later medium-bottle additions.\
    \ The earlier per-liter clause is not carried across paragraphs. Keep stock recipe,\
    \ dose, pH and physical state separate; KHPO4 is the printed buffer notation,\
    \ not an inferred specific phosphate salt.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q23\",\n    \"name\": \"Neutralized cysteine hydrochloride monohydrate dose\"\
    ,\n    \"stage\": \"Liquid additions after autoclaving and cooling\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": 0.85,\n      \"unit\": \"ML\",\n\
    \      \"basis\": \"Per medium bottle\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\": \"\
    https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Liquid additions after autoclaving and cooling\",\n        \"exact_source_quote\"\
    : \"After the autoclaving and cooling steps, the following solutions were injected\
    \ into the medium bottles, in order, from anaerobic stocks (except for the cysteine,\
    \ which was made fresh and filter sterilized directly into the medium): 1.28 ml\
    \ of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl\
    \ · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin\
    \ solution ( 21 ).\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"These are later medium-bottle additions.\
    \ The earlier per-liter clause is not carried across paragraphs. Keep stock recipe,\
    \ dose, pH and physical state separate; KHPO4 is the printed buffer notation,\
    \ not an inferred specific phosphate salt.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q24\",\n    \"name\": \"Cysteine stock strength\",\n    \"stage\": \"Liquid\
    \ additions after autoclaving and cooling\",\n    \"decision\": \"add\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": 0.23,\n      \"unit\": \"MOLAR\"\
    ,\n      \"basis\": \"Fresh stock, filter-sterilized directly into medium\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"pmc1392968\"\
    ,\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid additions after autoclaving and cooling\"\
    ,\n        \"exact_source_quote\": \"After the autoclaving and cooling steps,\
    \ the following solutions were injected into the medium bottles, in order, from\
    \ anaerobic stocks (except for the cysteine, which was made fresh and filter sterilized\
    \ directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of\
    \ 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O\
    \ 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).\",\n        \"snapshot_sha256\"\
    : \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\",\n    \
    \    \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"These are later medium-bottle additions.\
    \ The earlier per-liter clause is not carried across paragraphs. Keep stock recipe,\
    \ dose, pH and physical state separate; KHPO4 is the printed buffer notation,\
    \ not an inferred specific phosphate salt.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q25\",\n    \"name\": \"Sodium thiosulfate pentahydrate stock dose\",\n  \
    \  \"stage\": \"Liquid additions after autoclaving and cooling\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": 8.5,\n      \"unit\": \"ML\",\n\
    \      \"basis\": \"Per medium bottle\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\": \"\
    https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Liquid additions after autoclaving and cooling\",\n        \"exact_source_quote\"\
    : \"After the autoclaving and cooling steps, the following solutions were injected\
    \ into the medium bottles, in order, from anaerobic stocks (except for the cysteine,\
    \ which was made fresh and filter sterilized directly into the medium): 1.28 ml\
    \ of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl\
    \ · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin\
    \ solution ( 21 ).\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"These are later medium-bottle additions.\
    \ The earlier per-liter clause is not carried across paragraphs. Keep stock recipe,\
    \ dose, pH and physical state separate; KHPO4 is the printed buffer notation,\
    \ not an inferred specific phosphate salt.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q26\",\n    \"name\": \"Thiosulfate stock strength\",\n    \"stage\": \"Liquid\
    \ additions after autoclaving and cooling\",\n    \"decision\": \"add\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": 25,\n      \"unit\": \"PERCENT_W_V\"\
    ,\n      \"basis\": \"Explicit wt/vol stock\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Liquid additions after autoclaving and cooling\",\n        \"exact_source_quote\"\
    : \"After the autoclaving and cooling steps, the following solutions were injected\
    \ into the medium bottles, in order, from anaerobic stocks (except for the cysteine,\
    \ which was made fresh and filter sterilized directly into the medium): 1.28 ml\
    \ of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl\
    \ · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin\
    \ solution ( 21 ).\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"These are later medium-bottle additions.\
    \ The earlier per-liter clause is not carried across paragraphs. Keep stock recipe,\
    \ dose, pH and physical state separate; KHPO4 is the printed buffer notation,\
    \ not an inferred specific phosphate salt.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q27\",\n    \"name\": \"Vitamin solution dose\",\n    \"stage\": \"Liquid\
    \ additions after autoclaving and cooling\",\n    \"decision\": \"add\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": 0.4,\n      \"unit\": \"ML\",\n\
    \      \"basis\": \"Per medium bottle; formula unresolved\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Liquid additions after autoclaving and cooling\",\n        \"exact_source_quote\"\
    : \"After the autoclaving and cooling steps, the following solutions were injected\
    \ into the medium bottles, in order, from anaerobic stocks (except for the cysteine,\
    \ which was made fresh and filter sterilized directly into the medium): 1.28 ml\
    \ of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl\
    \ · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin\
    \ solution ( 21 ).\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"These are later medium-bottle additions.\
    \ The earlier per-liter clause is not carried across paragraphs. Keep stock recipe,\
    \ dose, pH and physical state separate; KHPO4 is the printed buffer notation,\
    \ not an inferred specific phosphate salt.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q28\",\n    \"name\": \"FeSO4 stock dose\",\n    \"stage\": \"Liquid iron\
    \ addition after reduction\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": 2.5,\n      \"unit\": \"ML\",\n\
    \      \"basis\": \"Per medium bottle after reduction\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Liquid iron addition after reduction\",\n        \"exact_source_quote\": \"\
    The medium was allowed to become reduced (colorless), after which 2.5 ml of 0.01\
    \ M FeSO 4 dissolved in 0.2 N HCl was injected.\",\n        \"snapshot_sha256\"\
    : \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\",\n    \
    \    \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Do not choose a hydrate or convert\
    \ normality to an unstated final concentration. The dose belongs to the medium\
    \ bottle.\"\n  },\n  {\n    \"decision_id\": \"q29\",\n    \"name\": \"FeSO4 stock\
    \ strength\",\n    \"stage\": \"Liquid iron addition after reduction\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": 0.01,\n      \"unit\": \"MOLAR\"\
    ,\n      \"basis\": \"Hydration unspecified\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Liquid iron addition after reduction\",\n        \"exact_source_quote\": \"\
    The medium was allowed to become reduced (colorless), after which 2.5 ml of 0.01\
    \ M FeSO 4 dissolved in 0.2 N HCl was injected.\",\n        \"snapshot_sha256\"\
    : \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\",\n    \
    \    \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Do not choose a hydrate or convert\
    \ normality to an unstated final concentration. The dose belongs to the medium\
    \ bottle.\"\n  },\n  {\n    \"decision_id\": \"q30\",\n    \"name\": \"HCl carrier\
    \ strength\",\n    \"stage\": \"Liquid iron addition after reduction\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": 0.2,\n      \"unit\": \"NORMAL\"\
    ,\n      \"basis\": \"Carrier acid, not final acid concentration\"\n    },\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"pmc1392968\",\n\
    \        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid iron addition after reduction\",\n   \
    \     \"exact_source_quote\": \"The medium was allowed to become reduced (colorless),\
    \ after which 2.5 ml of 0.01 M FeSO 4 dissolved in 0.2 N HCl was injected.\",\n\
    \        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Do not choose a hydrate or convert\
    \ normality to an unstated final concentration. The dose belongs to the medium\
    \ bottle.\"\n  },\n  {\n    \"decision_id\": \"q31\",\n    \"name\": \"Sterile\
    \ O2 dose\",\n    \"stage\": \"Liquid post-inoculation oxygen\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 6,\n      \"unit\": \"\
    ML\",\n      \"basis\": \"After inoculation\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Liquid post-inoculation oxygen\",\n        \"exact_source_quote\": \"The medium\
    \ was inoculated, after which 6 ml of sterile O 2 was injected (0.4% of the headspace)\
    \ and the medium was carefully placed without shaking so as not to disturb the\
    \ forming [O 2 ] gradient, at 25°C.\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve both source-stated values\
    \ without recomputing an exact headspace or treating gas percentage as dissolved\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q32\",\n    \"name\": \"\
    Initial O2 headspace fraction\",\n    \"stage\": \"Liquid post-inoculation oxygen\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 0.4,\n      \"unit\": \"\
    PERCENT\",\n      \"basis\": \"Source-stated headspace percentage\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"pmc1392968\",\n\
    \        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Liquid post-inoculation oxygen\",\n        \"\
    exact_source_quote\": \"The medium was inoculated, after which 6 ml of sterile\
    \ O 2 was injected (0.4% of the headspace) and the medium was carefully placed\
    \ without shaking so as not to disturb the forming [O 2 ] gradient, at 25°C.\"\
    ,\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve both source-stated values\
    \ without recomputing an exact headspace or treating gas percentage as dissolved\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q33\",\n    \"name\": \"\
    Liquid incubation temperature\",\n    \"stage\": \"Source liquid method\",\n \
    \   \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 25,\n      \"unit\": \"\
    DEG_C\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"pmc1392968\",\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Source liquid method\",\n        \"exact_source_quote\"\
    : \"The medium was inoculated, after which 6 ml of sterile O 2 was injected (0.4%\
    \ of the headspace) and the medium was carefully placed without shaking so as\
    \ not to disturb the forming [O 2 ] gradient, at 25°C.\",\n        \"snapshot_sha256\"\
    : \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\",\n    \
    \    \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"The generated target omits the maintained\
    \ owner’s supported liquid temperature. Keep semisolid 28°C separate.\"\n  },\n\
    \  {\n    \"decision_id\": \"q34\",\n    \"name\": \"Initial inoculum\",\n   \
    \ \"stage\": \"Primary Results / Growth experiments\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: https://togomedium.org/medium/M2252\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"TOGO M2252 reports\
    \ a liquid artificial seawater base with 10 mM thiosulfate as the electron donor\
    \ for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the\
    \ cultivation context and state that cultures were incubated statically under\
    \ an O2 gradient at 25 C in the dark.\"\n      }\n    ],\n    \"desired\": {\n\
    \      \"value\": 1,\n      \"unit\": \"PERCENT\",\n      \"qualifier\": \"Results\
    \ context; percentage basis not specified\"\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Primary Results / Growth experiments\",\n        \"exact_source_quote\": \"\
    an initial inoculum of 1%\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Record as source-specific experimental\
    \ context, not a required formulation ingredient, general optimum or proof that\
    \ the local abbreviated recipe reproduces this experiment.\"\n  },\n  {\n    \"\
    decision_id\": \"q35\",\n    \"name\": \"Initial growth-supporting O2\",\n   \
    \ \"stage\": \"Primary Results / Growth experiments\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: https://togomedium.org/medium/M2252\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"TOGO M2252 reports\
    \ a liquid artificial seawater base with 10 mM thiosulfate as the electron donor\
    \ for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the\
    \ cultivation context and state that cultures were incubated statically under\
    \ an O2 gradient at 25 C in the dark.\"\n      }\n    ],\n    \"desired\": {\n\
    \      \"value\": 0.5,\n      \"unit\": \"PERCENT\",\n      \"qualifier\": \"\
    Approximate result, not a universal set point\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Primary Results / Growth experiments\",\n        \"exact_source_quote\": \"\
    was about 0.5% O 2 in the headspace.\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Record as source-specific experimental\
    \ context, not a required formulation ingredient, general optimum or proof that\
    \ the local abbreviated recipe reproduces this experiment.\"\n  },\n  {\n    \"\
    decision_id\": \"q36\",\n    \"name\": \"Later oxygen range\",\n    \"stage\"\
    : \"Primary Results / Growth experiments\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: https://togomedium.org/medium/M2252\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"TOGO M2252 reports\
    \ a liquid artificial seawater base with 10 mM thiosulfate as the electron donor\
    \ for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the\
    \ cultivation context and state that cultures were incubated statically under\
    \ an O2 gradient at 25 C in the dark.\"\n      }\n    ],\n    \"desired\": {\n\
    \      \"value\": \"4 to 5\",\n      \"unit\": \"PERCENT\",\n      \"qualifier\"\
    : \"Later established culture only\"\n    },\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Primary Results / Growth experiments\",\n   \
    \     \"exact_source_quote\": \"volumes of O 2 up to 4 to 5% of the headspace\
    \ could be introduced\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Record as source-specific experimental\
    \ context, not a required formulation ingredient, general optimum or proof that\
    \ the local abbreviated recipe reproduces this experiment.\"\n  },\n  {\n    \"\
    decision_id\": \"q37\",\n    \"name\": \"Initial gradient-maintenance interval\"\
    ,\n    \"stage\": \"Primary Results / Growth experiments\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: https://togomedium.org/medium/M2252\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"TOGO M2252 reports\
    \ a liquid artificial seawater base with 10 mM thiosulfate as the electron donor\
    \ for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the\
    \ cultivation context and state that cultures were incubated statically under\
    \ an O2 gradient at 25 C in the dark.\"\n      }\n    ],\n    \"desired\": {\n\
    \      \"value\": \"6 to 7\",\n      \"unit\": \"DAYS\",\n      \"qualifier\"\
    : \"Source growth observation\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"pmc1392968\",\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Primary Results / Growth experiments\",\n   \
    \     \"exact_source_quote\": \"during the first 6 to 7 days after inoculation\"\
    ,\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Record as source-specific experimental\
    \ context, not a required formulation ingredient, general optimum or proof that\
    \ the local abbreviated recipe reproduces this experiment.\"\n  },\n  {\n    \"\
    decision_id\": \"q38\",\n    \"name\": \"Average doubling time\",\n    \"stage\"\
    : \"Primary Results / Growth experiments\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: https://togomedium.org/medium/M2252\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"TOGO M2252 reports\
    \ a liquid artificial seawater base with 10 mM thiosulfate as the electron donor\
    \ for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the\
    \ cultivation context and state that cultures were incubated statically under\
    \ an O2 gradient at 25 C in the dark.\"\n      }\n    ],\n    \"desired\": {\n\
    \      \"value\": 30,\n      \"unit\": \"HOURS\",\n      \"qualifier\": \"Estimate\
    \ in these gradient cultures\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"pmc1392968\",\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Primary Results / Growth experiments\",\n   \
    \     \"exact_source_quote\": \"we estimate an average doubling time of ∼30 h\"\
    ,\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Record as source-specific experimental\
    \ context, not a required formulation ingredient, general optimum or proof that\
    \ the local abbreviated recipe reproduces this experiment.\"\n  },\n  {\n    \"\
    decision_id\": \"q39\",\n    \"name\": \"Unspecified later oxygen addition\",\n\
    \    \"stage\": \"Established liquid culture\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"additional_dose_schedule\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"pmc1392968\"\
    ,\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Established liquid culture\",\n        \"exact_source_quote\"\
    : \"greater amounts of sterile O 2 could be injected and used by growing cells.\"\
    ,\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"No universal dose schedule is given;\
    \ retain the separately described later 4–5% headspace observation.\"\n  },\n\
    \  {\n    \"decision_id\": \"q40\",\n    \"name\": \"ASW, elixir and vitamin complete\
    \ formulas\",\n    \"stage\": \"Unresolved external source recipes\",\n    \"\
    decision\": \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"artificial_seawater_formula\": null,\n  \
    \    \"modified_Wolfe_formula\": null,\n      \"vitamin_formula\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"pmc1392968\",\n\
    \        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Pre-autoclave list citing references 6 and 21\"\
    ,\n        \"exact_source_quote\": \"The medium consisted of an artificial seawater\
    \ ( 6 ) base to which was added the following (per liter), in order, prior to\
    \ autoclaving: 5 ml of modified Wolfe's mineral elixir ( 21 ), 0.25 g of NH 4\
    \ Cl, and 100 μl of 0.2% (wt/vol) aqueous resazurin.\",\n        \"snapshot_sha256\"\
    : \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\",\n    \
    \    \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      },\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Post-autoclave vitamin addition citing reference 21\",\n        \"exact_source_quote\"\
    : \"After the autoclaving and cooling steps, the following solutions were injected\
    \ into the medium bottles, in order, from anaerobic stocks (except for the cysteine,\
    \ which was made fresh and filter sterilized directly into the medium): 1.28 ml\
    \ of 0.5 M KHPO 4 buffer, pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl\
    \ · H 2 O, 8.5 ml of 25% (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin\
    \ solution ( 21 ).\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Named source dependencies are not\
    \ complete formulas in the inspected material. Do not substitute a familiar seawater,\
    \ Wolfe or vitamin recipe.\"\n  },\n  {\n    \"decision_id\": \"q41\",\n    \"\
    name\": \"Semisolid gelling agent and amount\",\n    \"stage\": \"Radiolabel variant\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: https://togomedium.org/medium/M2252\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"TOGO M2252 reports\
    \ a liquid artificial seawater base with 10 mM thiosulfate as the electron donor\
    \ for microaerobic strain MC-1 growth. Its comments cite PMID:16461683 for the\
    \ cultivation context and state that cultures were incubated statically under\
    \ an O2 gradient at 25 C in the dark.\"\n      }\n    ],\n    \"desired\": {\n\
    \      \"gelling_agent\": null,\n      \"gelling_amount\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"pmc1392968\",\n     \
    \   \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n \
    \       \"source_locator\": \"Radiolabel variant\",\n        \"exact_source_quote\"\
    : \"cells of strain MC-1 were grown microaerobically in semisolid medium at 28°C\"\
    ,\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"No gelling formula is supplied in\
    \ this inspected paragraph; do not assume agar or a concentration.\"\n  },\n \
    \ {\n    \"decision_id\": \"q42\",\n    \"name\": \"Measured final volume\",\n\
    \    \"stage\": \"Liquid assembly\",\n    \"decision\": \"not_quantified\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"measured_final_volume\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"pmc1392968\"\
    ,\n        \"source_url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\"\
    ,\n        \"source_locator\": \"Initial liquid-culture sentence\",\n        \"\
    exact_source_quote\": \"Cells were grown in 850 ml of medium in 2-liter glass\
    \ bottles.\",\n        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      },\n      {\n        \"source_key\": \"pmc1392968\",\n        \"source_url\"\
    : \"https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/\",\n        \"source_locator\"\
    : \"Later bottle additions\",\n        \"exact_source_quote\": \"After the autoclaving\
    \ and cooling steps, the following solutions were injected into the medium bottles,\
    \ in order, from anaerobic stocks (except for the cysteine, which was made fresh\
    \ and filter sterilized directly into the medium): 1.28 ml of 0.5 M KHPO 4 buffer,\
    \ pH 6.9, 0.85 ml of 0.23 M neutralized cysteine · HCl · H 2 O, 8.5 ml of 25%\
    \ (wt/vol) Na 2 S 2 O 3 · 5H 2 O, and 0.4 ml of vitamin solution ( 21 ).\",\n\
    \        \"snapshot_sha256\": \"7a29aad6b2f83dbdc8c26e95712695da968c6f2660575cee939144bd5df67403\"\
    ,\n        \"parsed_text_sha256\": \"c7910c71967e1c1fcaf5928511da90875dabc23e8316d2a4a7ad3abda9320bcd\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve 850 mL and the sequential\
    \ addition amounts without treating their arithmetic sum as a measured final volume.\"\
    \n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '2 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 1/3 primary
    and 1/3 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15379
  - chebi26977
  details: 'Instance coverage on a 0–100 percent scale, denominator 3: primary 33.33%;
    secondary 33.33%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 20 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact source and maintained owner
  outcome: supported
  summary: The generated target and single maintained owner resolve to TOGO M2252
    and CultureMech:008841. The maintained owner’s later citation, oxygen and temperature
    content is absent from the generated snapshot. Primary experiments, secondary
    shorthand and the current owner are distinguishable rather than assumed identical.
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - record
  - owner-0
  - provider
  - primary-methods
- assessment_id: formulation
  area: completeness
  topic: Complete source recipe and variants
  outcome: concern
  summary: The primary method names components and stages missing from the three-entry
    shorthand; some may be hidden by the unresolved artificial-seawater base. The
    10 mM primary statement is in the Table 1 caption for semisolid radiolabel culture.
    The liquid method uses a separate sodium-thiosulfate stock dose. Resolve their
    relationship without asserting wholesale omissions or a proven exact variant.
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - primary-methods
  - primary-table1
  - quantity-inventory
  - pmid15338111publisher-attempt
  - pmc1180996pdf-attempt
- assessment_id: growth
  area: evidence
  topic: Medium-specific MC-1 evidence and comparators
  outcome: supported
  summary: The primary documents MC-1 growth in its own staged liquid and semisolid
    oxygen-gradient cultures, including failure without thiosulfate. PMID22581902
    and current NCBI identify MC-1 as Magnetococcus marinus MC-1. This supports the
    cited experiments, not exact equivalence of the abbreviated local recipe. C. tepidum,
    R. rubrum, MV-1/MV-2 and broader taxon mentions do not establish growth on this
    record.
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - primary-methods
  - primary-growth
  - pubmed-22581902
  - bibliography-taxonomy
  - taxonomy-source
- assessment_id: citations
  area: provenance
  topic: Bibliography and historical source access
  outcome: concern
  summary: All five inspected PubMed identities and twelve named taxonomy nodes are
    reconciled with their bounded roles. The owner correctly retains unresolved formulas,
    parent-only taxa and historical placement. Its October 14 named archives remain
    unrecovered; current abstracts and methods are independent current evidence, not
    historical byte verification.
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - bibliography-taxonomy
  - historical-limit
  - owner-0
- assessment_id: preparation
  area: completeness
  topic: Source-specific preparation and conditions
  outcome: concern
  summary: Inventory retains pre-autoclave per-liter additions, post-autoclave bottle
    doses, pH 7 versus buffer pH 6.9, 25°C liquid versus 28°C semisolid conditions,
    oxygen-gradient handling and source uncertainty. No autoclave cycle, complete
    stock formula, headspace arithmetic or final-volume conversion is supplied by
    inference.
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - primary-methods
  - primary-table1
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Physical state and composition classification
  outcome: concern
  summary: The local LIQUID state corresponds to the secondary and liquid primary
    context but must not absorb the semisolid Table 1 variant. Owner SEMI_DEFINED
    and target UNDEFINED differ; neither classification substitutes for resolving
    the exact base and stock formulas. Artificial seawater is a mixture and should
    not be forced to a single-compound ID.
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - record
  - owner-0
  - provider
  - primary-methods
  - primary-table1
findings:
- finding_id: f1
  issue_key: culturemech.008841.wrong-thiosulfate-class
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Canonical thiosulfate label masks the wrong chemical class
  description: Both layers assign CHEBI:26977, defined as an ester of thiosulfuric
    acid. The provider calls the donor inorganic thiosulfate and the liquid primary
    specifies sodium thiosulfate pentahydrate; the ester-class term cannot represent
    either merely by label agreement.
  target_ids:
  - CultureMech:008841
  field_paths:
  - ingredients[1].term
  - ingredients[1].mediaingredientmech_chebi_term
  evidence_ids:
  - thiosulfate-definition
  - provider
  - primary-methods
  - chebi26977
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
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
  issue_key: culturemech.008841.base-volume-denominator
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Generated artificial-seawater liquid volume has a mass unit
  description: The generated target stores the source-listed 1 L artificial-seawater
    input as 1 G_PER_L, a confirmed liquid-to-mass unit error. The owner’s 1000 ML_PER_L
    may instead be a normalization marker; its denominator and stage require evidence,
    but this row alone does not establish a numerical error in that owner value.
  target_ids:
  - CultureMech:008841
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
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
  issue_key: culturemech.008841.variant-stage-collapse
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Three-entry shorthand does not resolve the primary culture recipes
  description: The local liquid shorthand omits the paper’s stage structure. Its 10
    mM value is supported secondarily, while the primary’s explicit 10 mM appears
    in the semisolid Table 1 caption. Missing named base/stock formulas prevent deciding
    which components are hidden by shorthand versus genuine recipe differences.
  target_ids:
  - CultureMech:008841
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  - physical_state
  evidence_ids:
  - primary-methods
  - primary-table1
  - quantity-inventory
  - pmid15338111publisher-attempt
  - pmc1180996pdf-attempt
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
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
  issue_key: culturemech.008841.missing-claim-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Useful citations do not attach formulation and condition claims
  description: The maintained owner has extensive bounded bibliography and taxonomy
    notes, but the local amounts, temperature and preparation lack claim-level supporting
    evidence. Existing current source access does not authenticate the absent historical
    archive bytes.
  target_ids:
  - CultureMech:008841
  field_paths:
  - references
  - ingredients
  - temperature_value
  - preparation_steps
  evidence_ids:
  - owner-0
  - bibliography-taxonomy
  - historical-limit
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
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
  issue_key: culturemech.008841.generated-owner-drift
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Generated target predates maintained source and condition context
  description: The merged target lacks the maintained owner’s citations, oxygen grounding,
    25°C/static-gradient metadata and explicit formulation limitations. These later
    owner fields still require the corrections and evidence described here before
    propagation.
  target_ids:
  - CultureMech:008841
  field_paths:
  - references
  - temperature_value
  - aeration
  - incubation_atmosphere
  - composition_type
  evidence_ids:
  - record
  - owner-0
  - historical-limit
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
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
  description: Re-ground the donor only after separating anion shorthand from the
    explicitly supplied sodium salt/hydrate; verify primary and secondary identifiers
    independently.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008841
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
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
  description: Correct the generated target’s mass unit using the source-listed liquid
    input, and authenticate the maintained owner’s normalization denominator and stage
    without presuming its 1000 mL/L marker is numerically false.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008841
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
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
  description: Recover the cited base and stock recipes, represent each experiment
    with its own quantities and preparation, and resolve equivalence or variants without
    mixing stage denominators.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008841
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
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
  description: Attach narrow current source excerpts to supported claims, retain the
    historical limitations, and distinguish provider-only dark incubation from primary
    methods.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008841
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
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
  description: Curate the maintained owner first, then regenerate and compare exact
    scientific fields without treating successful generation as source verification.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:008841
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
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
- The current publisher route supplies bibliographic/abstract material but no inspected
  complete artificial-seawater recipe. The requested PDF route returned the same access
  page, not a usable full-text formula.
- The requested 1997 primary PDF returned a download interstitial; its available PMC
  page supplies abstract/bibliography but not the complete modified Wolfe or vitamin
  formulas.
- The Table 1 caption supplies 10 mM for semisolid culture; the frozen preparatory
  context’s earlier footnote wording is superseded by the exact source locator used
  here.
- The five PubMed records and twelve taxonomy nodes were reviewed for the named roles,
  not as exhaustive full-paper organism inventories or a complete correction/retraction
  search.
- Comparator culture media, extraction buffers, enzyme assays, radiolabel analytical
  concentrations and general taxon optima are excluded from recipe transfer.
- No native growth association, new experiment or complete recipe reconstruction is
  asserted.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-037
- generated-medium
```
