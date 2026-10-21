# Source and formulation review: alkaliphilus_namsaraevii_medium (CultureMech:001144)

- Review: 20261021T133656Z-culturemech-001144-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:27:13Z
- Finished UTC: 2026-10-21T13:36:56Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ1661 specifies three 1 mL stock additions, but the target and owner expose their undiluted constituents as direct medium concentrations. HCl 25% volume becomes 2.5 g/L, nickel hexahydrate retains an anhydrous identifier, and the ferric-citrate 19% Fe qualifier is lost. Main preparation is largely preserved, while the SL-10 make-up instruction is misplaced as a main step. Current repaired stock dependencies and their historical evidence are assessed separately from the unchanged flat medium.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 226; batch 023 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-two task batches contain 220 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 223 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001144 | data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml | generated | alkaliphilus_namsaraevii_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001144 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001144 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch023/226/strict.tsv |
| validate-terms | passed | True | CultureMech:001144 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001144 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001144 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001144.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:001144.

28 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 28/29 primary and 27/29 secondary instances; all asserted mediaingredientmech_chebi_term keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 29: primary 96.55%; secondary 93.10%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001144.

73 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "Main sol. 1661 / KH2PO4",
    "field_path": "ingredients[0].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 3.66318,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Main sol. 1661 subsection row 1",
        "exact_source_quote": "KH2PO4 0.50 g",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "The local value matches the provider’s rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence. Preserve original source mass and nominal basis; later ferric/Mg stock additions and titration do not establish measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.498504",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.498504",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "0.5 g / 1.003 L = 0.4985044865403788634097706879 g/L conditionally; stored/provider value 0.498504 is rounded, not exact."
  },
  {
    "ingredient_or_context": "Main sol. 1661 / NaCl",
    "field_path": "ingredients[1].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 25,\n                        \"unit\": \"g\",\n                        \"g_l\": 24.9252,\n                        \"mmol_l\": 426.51,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Main sol. 1661 subsection row 2",
        "exact_source_quote": "NaCl 25.00 g",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "The local value matches the provider’s rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence. Preserve original source mass and nominal basis; later ferric/Mg stock additions and titration do not establish measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "24.9252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "24.9252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "25 g / 1.003 L = 24.92522432701894317048853440 g/L conditionally; stored/provider value 24.9252 is rounded, not exact."
  },
  {
    "ingredient_or_context": "Main sol. 1661 / Yeast extract",
    "field_path": "ingredients[2].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.49252,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Main sol. 1661 subsection row 3",
        "exact_source_quote": "Yeast extract 2.50 g",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "The local value matches the provider’s rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence. Preserve original source mass and nominal basis; later ferric/Mg stock additions and titration do not establish measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2.49252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2.49252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "2.5 g / 1.003 L = 2.492522432701894317048853440 g/L conditionally; stored/provider value 2.49252 is rounded, not exact."
  },
  {
    "ingredient_or_context": "Main sol. 1661 / NaHCO3",
    "field_path": "ingredients[3].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 1.85,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.84447,\n                        \"mmol_l\": 21.9561,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Main sol. 1661 subsection row 4",
        "exact_source_quote": "NaHCO3 1.85 g",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "The local value matches the provider’s rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence. Preserve original source mass and nominal basis; later ferric/Mg stock additions and titration do not establish measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.84447",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.84447",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "1.85 g / 1.003 L = 1.844466600199401794616151545 g/L conditionally; stored/provider value 1.84447 is rounded, not exact."
  },
  {
    "ingredient_or_context": "Main sol. 1661 / Na2CO3",
    "field_path": "ingredients[4].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.19641,\n                        \"mmol_l\": 11.2882,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Main sol. 1661 subsection row 5",
        "exact_source_quote": "Na2CO3 1.20 g",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "The local value matches the provider’s rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence. Preserve original source mass and nominal basis; later ferric/Mg stock additions and titration do not establish measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.19641",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.19641",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "1.2 g / 1.003 L = 1.196410767696909272183449651 g/L conditionally; stored/provider value 1.19641 is rounded, not exact."
  },
  {
    "ingredient_or_context": "Main sol. 1661 / Trace element solution SL-10",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Main sol. 1661 subsection row 6",
        "exact_source_quote": "Trace element solution SL-10 1.00 ml",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Restore this exact stock-addition or solvent quantity at its source stage. The three named stocks each have a 1 mL receiving dose; stock water remains separate from main water.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 1661 / Selenite-tungstate solution",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Main sol. 1661 subsection row 7",
        "exact_source_quote": "Selenite-tungstate solution 1.00 ml",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Restore this exact stock-addition or solvent quantity at its source stage. The three named stocks each have a 1 mL receiving dose; stock water remains separate from main water.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 1661 / Fe(III) citrate",
    "field_path": "ingredients[5].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Fe(III) citrate\",\n                        \"compound_id\": 45,\n                        \"attribute\": \"19% Fe\",\n                        \"amount\": 7.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 7.27817,\n                        \"mmol_l\": 29.7136,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Main sol. 1661 subsection row 8",
        "exact_source_quote": "Fe(III) citrate (19% Fe) 7.30 g",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "The local value matches the provider’s rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence. Preserve original source mass and nominal basis; later ferric/Mg stock additions and titration do not establish measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "7.27817",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "7.27817",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "7.3 g / 1.003 L = 7.278165503489531405782652044 g/L conditionally; stored/provider value 7.27817 is rounded, not exact."
  },
  {
    "ingredient_or_context": "Main sol. 1661 / MgCl2 x 6 H2O",
    "field_path": "ingredients[6].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199402,\n                        \"mmol_l\": 0.980811,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Main sol. 1661 subsection row 9",
        "exact_source_quote": "MgCl2 x 6 H2O 0.20 g",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "The local value matches the provider’s rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence. Preserve original source mass and nominal basis; later ferric/Mg stock additions and titration do not establish measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.199402",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.199402",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "0.2 g / 1.003 L = 0.1994017946161515453639082752 g/L conditionally; stored/provider value 0.199402 is rounded, not exact."
  },
  {
    "ingredient_or_context": "Main sol. 1661 / Wolin's vitamin solution (10x)",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Main sol. 1661 subsection row 10",
        "exact_source_quote": "Wolin's vitamin solution (10x) 1.00 ml",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Restore this exact stock-addition or solvent quantity at its source stage. The three named stocks each have a 1 mL receiving dose; stock water remains separate from main water.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 1661 / Distilled water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Main sol. 1661 subsection row 11",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Restore this exact stock-addition or solvent quantity at its source stage. The three named stocks each have a 1 mL receiving dose; stock water remains separate from main water.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Trace element solution SL-10 / HCl",
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Trace element solution SL-10 subsection row 1",
        "exact_source_quote": "HCl (25%) 10.00 ml",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "The source specifies 10 mL HCl 25% within SL-10; neither percent basis nor density is supplied. Provider g_l2.5 cannot validate a neat-solute conversion, and undiluted stock is not final medium.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Restore 10 mL liquid input (=0.010 L) and literal 25%; no pure-HCl grams or molarity inferred."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10 / FeCl2 x 4 H2O",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Trace element solution SL-10 subsection row 2",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 1.5 g/L × 0.001 L would deliver 0.0015 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10 / ZnCl2",
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Trace element solution SL-10 subsection row 3",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.07 g/L × 0.001 L would deliver 0.00007 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10 / MnCl2 x 4 H2O",
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Trace element solution SL-10 subsection row 4",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.1 g/L × 0.001 L would deliver 0.0001 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10 / H3BO3",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Trace element solution SL-10 subsection row 5",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.006 g/L × 0.001 L would deliver 0.000006 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10 / CoCl2 x 6 H2O",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Trace element solution SL-10 subsection row 6",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.19 g/L × 0.001 L would deliver 0.00019 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10 / CuCl2 x 2 H2O",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Trace element solution SL-10 subsection row 7",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.002 g/L × 0.001 L would deliver 0.000002 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10 / NiCl2 x 6 H2O",
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Trace element solution SL-10 subsection row 8",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.024 g/L × 0.001 L would deliver 0.000024 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10 / Na2MoO4 x 2 H2O",
    "field_path": "ingredients[15].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Trace element solution SL-10 subsection row 9",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.036 g/L × 0.001 L would deliver 0.000036 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10 / Distilled water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Trace element solution SL-10 subsection row 10",
        "exact_source_quote": "Distilled water 990.00 ml",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Restore this exact stock-addition or solvent quantity at its source stage. The three named stocks each have a 1 mL receiving dose; stock water remains separate from main water.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Selenite-tungstate solution / NaOH",
    "field_path": "ingredients[16].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[2].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Selenite-tungstate solution subsection row 1",
        "exact_source_quote": "NaOH 0.50 g",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.5 g/L × 0.001 L would deliver 0.0005 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Selenite-tungstate solution / Na2SeO3 x 5 H2O",
    "field_path": "ingredients[17].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[2].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Selenite-tungstate solution subsection row 2",
        "exact_source_quote": "Na2SeO3 x 5 H2O 3.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.003 g/L × 0.001 L would deliver 0.000003 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Selenite-tungstate solution / Na2WO4 x 2 H2O",
    "field_path": "ingredients[18].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[2].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Selenite-tungstate solution subsection row 3",
        "exact_source_quote": "Na2WO4 x 2 H2O 4.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.004 g/L × 0.001 L would deliver 0.000004 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Selenite-tungstate solution / Distilled water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[2].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Selenite-tungstate solution subsection row 4",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Restore this exact stock-addition or solvent quantity at its source stage. The three named stocks each have a 1 mL receiving dose; stock water remains separate from main water.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Biotin",
    "field_path": "ingredients[19].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection row 1",
        "exact_source_quote": "Biotin 20.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
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
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.02 g/L × 0.001 L would deliver 0.00002 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Folic acid",
    "field_path": "ingredients[20].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[3].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection row 2",
        "exact_source_quote": "Folic acid 20.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
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
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.02 g/L × 0.001 L would deliver 0.00002 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Pyridoxine hydrochloride",
    "field_path": "ingredients[21].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[3].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection row 3",
        "exact_source_quote": "Pyridoxine hydrochloride 100.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
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
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.1 g/L × 0.001 L would deliver 0.0001 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Thiamine HCl",
    "field_path": "ingredients[22].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[3].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection row 4",
        "exact_source_quote": "Thiamine HCl 50.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
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
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.05 g/L × 0.001 L would deliver 0.00005 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Riboflavin",
    "field_path": "ingredients[23].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[3].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection row 5",
        "exact_source_quote": "Riboflavin 50.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
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
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.05 g/L × 0.001 L would deliver 0.00005 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Nicotinic acid",
    "field_path": "ingredients[24].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[3].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection row 6",
        "exact_source_quote": "Nicotinic acid 50.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
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
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.05 g/L × 0.001 L would deliver 0.00005 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Calcium D-(+)-pantothenate",
    "field_path": "ingredients[25].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[3].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection row 7",
        "exact_source_quote": "Calcium D-(+)-pantothenate 50.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
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
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.05 g/L × 0.001 L would deliver 0.00005 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Vitamin B12",
    "field_path": "ingredients[26].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[3].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection row 8",
        "exact_source_quote": "Vitamin B12 1.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
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
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.001 g/L × 0.001 L would deliver 0.000001 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / p-Aminobenzoic acid",
    "field_path": "ingredients[27].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[3].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection row 9",
        "exact_source_quote": "p-Aminobenzoic acid 50.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
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
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.05 g/L × 0.001 L would deliver 0.00005 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / (DL)-alpha-Lipoic acid",
    "field_path": "ingredients[28].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[3].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection row 10",
        "exact_source_quote": "(DL)-alpha-Lipoic acid 50.00 mg",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "A concentration within an undiluted stock is stored as a direct medium concentration. Restore stock composition and its separate 1 mL receiving dose; exact measured receiving-medium volume remains unknown.",
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
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider-declared 1 L stock basis, 0.05 g/L × 0.001 L would deliver 0.00005 g; this conditional mass is not final medium g/L."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Distilled water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1661api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1661",
        "source_locator": "$.data.solutions[3].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273"
      },
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection row 11",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Restore this exact stock-addition or solvent quantity at its source stage. The three named stocks each have a 1 mL receiving dose; stock water remains separate from main water.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 595: HCl",
    "field_path": "composition[0].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution595",
        "source_url": "https://mediadive.dsmz.de/rest/solution/595",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"HCl\",\n                \"compound_id\": 68,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"25%\",\n                \"amount\": 10,\n                \"unit\": \"ml\",\n                \"g_l\": 2.5,\n                \"mmol_l\": 68.5683,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab"
      }
    ],
    "rationale": "10 mL HCl 25% input equals 0.01 L; unknown percentage basis and density are explicitly retained. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.01",
          "unit": "L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 595: FeCl2 x 4 H2O",
    "field_path": "composition[1].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution595",
        "source_url": "https://mediadive.dsmz.de/rest/solution/595",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\": \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 595: ZnCl2",
    "field_path": "composition[2].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution595",
        "source_url": "https://mediadive.dsmz.de/rest/solution/595",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\": \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 595: MnCl2 x 4 H2O",
    "field_path": "composition[3].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution595",
        "source_url": "https://mediadive.dsmz.de/rest/solution/595",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.505293,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 595: H3BO3",
    "field_path": "composition[4].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution595",
        "source_url": "https://mediadive.dsmz.de/rest/solution/595",
        "source_locator": "$.data.recipe[4]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\": \"mg\",\n                \"g_l\": 0.006,\n                \"mmol_l\": 0.0970246,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[4].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 595: CoCl2 x 6 H2O",
    "field_path": "composition[5].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution595",
        "source_url": "https://mediadive.dsmz.de/rest/solution/595",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\": \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[5].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 595: CuCl2 x 2 H2O",
    "field_path": "composition[6].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution595",
        "source_url": "https://mediadive.dsmz.de/rest/solution/595",
        "source_locator": "$.data.recipe[6]",
        "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[6].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 595: NiCl2 x 6 H2O",
    "field_path": "composition[7].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution595",
        "source_url": "https://mediadive.dsmz.de/rest/solution/595",
        "source_locator": "$.data.recipe[7]",
        "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\": \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[7].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 595: Na2MoO4 x 2 H2O",
    "field_path": "composition[8].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution595",
        "source_url": "https://mediadive.dsmz.de/rest/solution/595",
        "source_locator": "$.data.recipe[8]",
        "exact_source_quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\": \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[8].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 595: Distilled water",
    "field_path": "composition[9].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution595",
        "source_url": "https://mediadive.dsmz.de/rest/solution/595",
        "source_locator": "$.data.recipe[9]",
        "exact_source_quote": "{\n                \"recipe_order\": 10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 990,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab"
      }
    ],
    "rationale": "Explicit SL-10 final make-up to 1000 mL, separate from the 990 mL listed water. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[9].concentration",
        "stored": {
          "value": "to 1 L final volume",
          "unit": "VARIABLE"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 777: NaOH",
    "field_path": "composition[0].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution777",
        "source_url": "https://mediadive.dsmz.de/rest/solution/777",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"NaOH\",\n                \"compound_id\": 256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\": \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 12.5009,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 777: Na2SeO3 x 5 H2O",
    "field_path": "composition[1].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution777",
        "source_url": "https://mediadive.dsmz.de/rest/solution/777",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Na2SeO3 x 5 H2O\",\n                \"compound_id\": 107,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\": \"mg\",\n                \"g_l\": 0.003,\n                \"mmol_l\": 0.0114062,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 777: Na2WO4 x 2 H2O",
    "field_path": "composition[2].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution777",
        "source_url": "https://mediadive.dsmz.de/rest/solution/777",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\": 249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0121267,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 777: Distilled water",
    "field_path": "composition[3].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution777",
        "source_url": "https://mediadive.dsmz.de/rest/solution/777",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2"
      }
    ],
    "rationale": "Source 1000 mL water addition equals 1 L, not measured final stock volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 5980: Biotin",
    "field_path": "composition[0].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution5980",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5980",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0818632,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 5980: Folic acid",
    "field_path": "composition[1].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution5980",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5980",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Folic acid\",\n                \"compound_id\": 138,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0453104,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 5980: Pyridoxine hydrochloride",
    "field_path": "composition[2].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution5980",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5980",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\": 519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.486287,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 5980: Thiamine HCl",
    "field_path": "composition[3].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution5980",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5980",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.148236,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 5980: Riboflavin",
    "field_path": "composition[4].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution5980",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5980",
        "source_locator": "$.data.recipe[4]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"Riboflavin\",\n                \"compound_id\": 136,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.132837,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
        "field_path": "composition[4].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 5980: Nicotinic acid",
    "field_path": "composition[5].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution5980",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5980",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\": 139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.406141,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
        "field_path": "composition[5].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 5980: Calcium D-(+)-pantothenate",
    "field_path": "composition[6].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution5980",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5980",
        "source_locator": "$.data.recipe[6]",
        "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"Calcium D-(+)-pantothenate\",\n                \"compound_id\": 1512,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.209846,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
        "field_path": "composition[6].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 5980: Vitamin B12",
    "field_path": "composition[7].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution5980",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5980",
        "source_locator": "$.data.recipe[7]",
        "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\": 18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1,\n                \"unit\": \"mg\",\n                \"g_l\": 0.001,\n                \"mmol_l\": 0.00073779,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
        "field_path": "composition[7].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 5980: p-Aminobenzoic acid",
    "field_path": "composition[8].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution5980",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5980",
        "source_locator": "$.data.recipe[8]",
        "exact_source_quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\": 47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
        "field_path": "composition[8].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 5980: (DL)-alpha-Lipoic acid",
    "field_path": "composition[9].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution5980",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5980",
        "source_locator": "$.data.recipe[9]",
        "exact_source_quote": "{\n                \"recipe_order\": 10,\n                \"compound\": \"(DL)-alpha-Lipoic acid\",\n                \"compound_id\": 252,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.24233,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c"
      }
    ],
    "rationale": "Provider-declared nominal stock basis; not independently measured final volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
        "field_path": "composition[9].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Context stock 5980: Distilled water",
    "field_path": "composition[10].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "solution5980",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5980",
        "source_locator": "$.data.recipe[10]",
        "exact_source_quote": "{\n                \"recipe_order\": 11,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c"
      }
    ],
    "rationale": "Source 1000 mL water addition equals 1 L, not measured final stock volume. Existing attached same-layer evidence matches the exact captured row/hash; this does not certify all chemical mappings or receiving-medium dilution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
        "field_path": "composition[10].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sparging gas",
    "field_path": "preparation.Main_sparging_gas",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "100% N2 gas",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Preserved pure-N2 atmosphere has no fixed absolute volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sparging duration",
    "field_path": "preparation.Main_sparging_duration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "30 - 45 min",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Preserved duration is sparging time, not sterilization duration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Initial main pH",
    "field_path": "preparation.Initial_main_pH",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "then adjust pH to 9.5",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Preserve initial pH endpoint after carbonate additions.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Final main pH",
    "field_path": "preparation.Final_main_pH",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "Adjust pH of the complete medium to 9.5",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Preserve the final endpoint independently of ferric-stock pH.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 9.5,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ph_value",
        "stored": 9.5,
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Ferric stock strength",
    "field_path": "preparation.Ferric_stock_strength",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "10% w/v stock solution",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "This explicit w/v stock strength is retained in prose but lacks attached evidence and a structured stock.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Ferric stock pH",
    "field_path": "preparation.Ferric_stock_pH",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "adjust pH to 7.5-8.0",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "This preserved endpoint belongs to the ferric stock, not the final medium.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Stock preparation atmosphere",
    "field_path": "preparation.Stock_preparation_atmosphere",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "stock solutions prepared under 100% N2 gas",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Preserve the stated atmosphere and filtered vitamin stage.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "SL-10 make-up",
    "field_path": "preparation.SL-10_make-up",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "make up to 1000.00 ml.",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "The literal final make-up belongs to SL-10, not the complete medium. Move this instruction into the restored stock scope.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Ferric product iron qualifier",
    "field_path": "preparation.Ferric_product_iron_qualifier",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "Fe(III) citrate (19% Fe) 7.30 g",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Restore source 19% Fe product qualification; generic stoichiometric ferric citrate does not establish this product specification.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].preferred_term",
        "stored": "Fe(III) citrate",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "ingredients[5].preferred_term",
        "stored": "Fe(III) citrate",
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Trace acid stock strength",
    "field_path": "preparation.Trace_acid_stock_strength",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "HCl (25%) 10.00 ml",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Preserve literal 25% within SL-10 with unknown percentage basis and density; the source volume is not a neat-solute mass.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Vitamin stock factor",
    "field_path": "preparation.Vitamin_stock_factor",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "Wolin's vitamin solution (10x)",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "Preserve the explicitly tenfold vitamin stock and its 1 mL addition as different quantities.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Titrant quantity",
    "field_path": "preparation.titration_dose",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1661",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf",
        "source_locator": "Final adjustment condition",
        "exact_source_quote": "if necessary.",
        "snapshot_sha256": "2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36",
        "parsed_text_sha256": "1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512"
      }
    ],
    "rationale": "No fixed titrant identity, normality or dose is supplied for the main/ferric endpoints; do not fill from adjacent media.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if necessary.",
        "decision": "not_quantified"
      }
    ]
  }
]

### Exact medium and three scoped stock identities

identity: supported. Targets: CultureMech:001144.

CM001144 resolves to exact DSMZ1661 and the unique maintained owner. Stock 595 SL-10,777 selenite-tungstate and5980 tenfold vitamins correspond to the current primary’s320/385/120 subsections and have separately inspected local IDs CM014713/CM015156/CM014721. MediaDive161 contributes only existing evidence for5980; no parent-medium or organism claim is inherited.

### Main nominal amounts versus undiluted stock strengths

consistency: concern. Targets: CultureMech:001144.

All 58 medium concentration instances and 25 stock-context concentrations are assessed. Seven main local numbers agree with rounded provider g/L on the nominal 1003 mL declaration, without evidence. All 22 stock-derived medium entries are misplaced undiluted stock values, including unjustified HCl 2.5 g/L. The three 1 mL doses and source water are absent from the structured medium. Later ferric/Mg stock volume and pH adjustment prevent treating the table’s 1003 mL liquid sum as measured final medium volume.

### Nickel hydrate and ferric product specificity

grounding: concern. Targets: CultureMech:001144.

The source explicitly uses nickel dichloride hexahydrate, while medium primary/secondary CHEBI:34887 has formula 2Cl.Ni. The maintained 595 stock already withdrew this assertion; it is still present in the medium. Ferric citrate is explicitly 19% Fe and 7.3 g product, whereas generic CHEBI:144421 does not establish that product specification. Calcium D-(+)-pantothenate is compatible with the inspected stereospecific term; DL lipoic acid is not narrowed by the unspecified structural term. Other explicit stock hydrates match the inspected term structures.

### Preserved main instructions and misplaced stock instruction

completeness: concern. Targets: CultureMech:001144.

Main N2 sparging 30–45 min, pH 9.5, ferric 10% w/v stock with pH 7.5–8.0 and filtered vitamins are preserved but lack attached evidence. The SL-10 make-up to 1000 mL instruction is placed as a main step without a stock object. Restore the hierarchy and claim linkage; the exact source supplies no numeric autoclave cycle.

### Existing stock curation is distinct from medium state

provenance: supported. Targets: CultureMech:001144.

The complete three stock YAMLs contain 25 composition rows and 26 evidence objects. Current snippets and capture hashes match exact endpoints, with one additional 5980 recipe snapshot scoped within 161. Historical placeholder removals, HCl/water repairs and nickel withdrawal are preserved in appended changes; they do not certify the unchanged medium. All 27 stock timestamp instances were read, including six timezone-naive historical values; no old event is rewritten.

### Complex liquid and absent biological assertions

scope: supported. Targets: CultureMech:001144.

COMPLEX/UNDEFINED and LIQUID fit the yeast-extract liquid source. There is no specific strain/taxon/assembly or DOI/PMID growth claim to transfer from a dependency. Source accession and stock identity do not establish experimentally observed growth for an organism inferred from the medium name.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001144.

15 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Current importer and stale flattened representation

provenance: concern. Targets: CultureMech:001144.

The generated target matches the maintained flat owner; later stock-specific repairs did not alter it. Current composition parsing separates the first primary solution from later stock definitions; its preparation extraction still iterates solution steps. Exact source/context hashes identify maintenance responsibilities without claiming a historical replay.

## Findings

### f1: Undiluted stock compositions are represented as the medium

blocker / open / confirmed; issue key: culturemech.001144.stock-flattening.

Three 1 mL stock additions are replaced by 22 direct ingredient strengths from SL-10, selenium/tungsten and tenfold vitamins. HCl 25% 10 mL becomes 2.5 g/L without an explicit percentage basis or density. These combined stage/unit errors materially alter the named formulation.

### f2: Nickel hydrate and ferric product qualification are not preserved

major / open / confirmed; issue key: culturemech.001144.supplied-forms.

Nickel hexahydrate is grounded to a no-water term in both medium linkage fields, although the inspected 595 stock already removed that assertion. The ferric ingredient omits the exact 19% Fe product qualification; a generic stoichiometric iron(III)citrate identifier does not validate that supplied material.

### f3: SL-10 make-up is misplaced as a main preparation step

major / open / confirmed; issue key: culturemech.001144.preparation-scope.

The second step’s 1000 mL final make-up belongs to SL-10; treating it as a main instruction conflicts with distinct source stages. Main preparation is largely retained but the stock definitions and claim evidence needed to interpret it are missing.

## Recommended Actions And Acceptance Checks

### a1

Restore three separate stocks, their 1 mL additions, source water and exact supplied forms. Retain HCl volume/percentage as stated, and distinguish nominal provider concentrations from measured final volume. Attach source evidence to the maintained owner before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore source-specific hydrate/product scope and verify any replacement identifier independently. Preserve source masses and ferric-stock strength; do not apply anhydrous molecular weights or silently replace the 19% Fe product.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Move the retained SL-10 instruction into the correct stock and preserve main pH 9.5 versus ferric-stock pH 7.5–8.0, gas, order and filtered vitamins with evidence. Do not invent an autoclave cycle or final medium denominator.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch023/226/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch023/226/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml:1:id: CultureMech:001144<br>./data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml:1:id: CultureMech:001144<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch023/source-preflight-bound/226/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 38 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch023/source-preflight-bound/226/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| dsmz1661 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf; Entire exact main recipe, three stocks and full preparation; both primary PDF pages visually inspected | supports | All source amounts, supplied forms, stages and preparation compared, keeping the provider 1003 mL declaration separate from measured final volume. |
| mediadive1661api | https://mediadive.dsmz.de/rest/medium/1661; Entire exact main recipe, three stocks and full preparation; both primary PDF pages visually inspected | supports | All source amounts, supplied forms, stages and preparation compared, keeping the provider 1003 mL declaration separate from measured final volume. |
| dsmz320 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf; SL-10 stock only | supports | Exact stock context; parent medium formulations and organism claims are not transferred. |
| dsmz385 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf; Selenite-tungstate stock only | supports | Exact stock context; parent medium formulations and organism claims are not transferred. |
| dsmz120 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf; Wolin vitamin solution (10x) only | supports | Exact stock context; parent medium formulations and organism claims are not transferred. |
| solution595 | https://mediadive.dsmz.de/rest/solution/595; Entire SL-10 endpoint | supports | Exact stock context; parent medium formulations and organism claims are not transferred. |
| solution777 | https://mediadive.dsmz.de/rest/solution/777; Entire selenite-tungstate endpoint | supports | Exact stock context; parent medium formulations and organism claims are not transferred. |
| solution5980 | https://mediadive.dsmz.de/rest/solution/5980; Entire vitamin endpoint | supports | Exact stock context; parent medium formulations and organism claims are not transferred. |
| mediadive161api | https://mediadive.dsmz.de/rest/medium/161; Only solution5980 at data.solutions[4], referenced by existing vitamin evidence | supports | Exact stock context; parent medium formulations and organism claims are not transferred. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi144421 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_144421; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:144421 resolves to iron(III) citrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:144421": [{"label": "Fe(III) citrate", "match_type": "preferred_term", "identifier": "CHEBI:144421", "preferred_term": "Fe(III) citrate", "ontology_id": "CHEBI:144421", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| stock-evidence-recheck | /private/tmp/culturemech-review-work-batch023/226/stock-evidence-recheck.json; All 25 current composition amounts,26 attached evidence objects, complete histories and historical snapshots | supports | Stock 595 already retains HCl as 0.01 L, explicit water make-up and withdrawal of generic nickel CHEBI. Stocks 777/5980 retain 1 L water additions and nominal provider concentrations. These repairs and attached claims do not propagate into the reviewed flat medium. All original explanations/history were read; timestamps with absent timezone remain contextual historical issues. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch023/226/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch023/226/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| history-metadata | data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml; data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml", "events": 7, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Main 1003 mL and stock 777/5980 nominal 1 L declarations are provider bases, not measured volumes after dissolution/titration. SL-10 alone explicitly specifies final make-up to 1000 mL.
- HCl 25% percentage basis and density remain unknown. Ferric-citrate19% Fe is a supplied-product qualifier. No exact molarity or replacement chemical identifier is inferred.
- Stock historical retrieval-time claims are preserved as history; current literal/hash agreement is checked independently and does not authenticate the original retrieval event.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T133656Z-culturemech-001144-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaliphilus_namsaraevii_medium (CultureMech:001144)'
started_at: '2026-10-21T13:27:13Z'
finished_at: '2026-10-21T13:36:56Z'
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
summary: DSMZ1661 specifies three 1 mL stock additions, but the target and owner expose
  their undiluted constituents as direct medium concentrations. HCl 25% volume becomes
  2.5 g/L, nickel hexahydrate retains an anhydrous identifier, and the ferric-citrate
  19% Fe qualifier is lost. Main preparation is largely preserved, while the SL-10
  make-up instruction is misplaced as a main step. Current repaired stock dependencies
  and their historical evidence are assessed separately from the unchanged flat medium.
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
  - path: data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml
    sha256: ab99f892546e889c810ed459399bf9ff0adb97ebd8154d2c4444abbac2e4ea8d
    role: target
  - path: data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml
    sha256: 446e88f317a138c094ea118e6539928836a28dbb39c69907e1ef9007d2134038
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml
    sha256: 6d335bc921a8e8a99bae829fda6e81ae023de16a5c19a71b881fb54a9c14e082
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml
    sha256: b8b5efd085ffa7d0f4e3da6ccf82c0de49b364082867d531beefa757fa3c5950
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml
    sha256: 9153ff2e0d3d0c3a28989b2de6264998a0b09c845f531d6e6b366353e215ebba
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
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
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
  selection: Task review 226; batch 023 item 6 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-two task batches
    contain 220 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 223 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001144
targets:
- target_id: CultureMech:001144
  path: data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml
  label: alkaliphilus_namsaraevii_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch023/226/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch023/226/strict.tsv"
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001144
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
  - CultureMech:001144
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:36:55Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:36:55Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:54.273895Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch023/226/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:55.829015Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch023/226/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:57.501518Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:58.625075Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:36:55Z'
  support: supports
  summary: './data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml:1:id: CultureMech:001144

    ./data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml:1:id: CultureMech:001144

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/source-preflight-bound/226/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:36:55Z'
  support: supports
  summary: 38 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 89e06260afb2348bdd2132d790b539350cd33ef5215018532935c1d5f66c1295
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/source-preflight-bound/226/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T13:36:55Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: ac56325f157a8dc9a4057a76df4fd4b1c6b91c297acfb29e501fd11e993bbe3a
- evidence_id: dsmz1661
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf
  locator: Entire exact main recipe, three stocks and full preparation; both primary
    PDF pages visually inspected
  accessed_at: '2026-10-21T13:16:21.898768Z'
  support: supports
  summary: All source amounts, supplied forms, stages and preparation compared, keeping
    the provider 1003 mL declaration separate from measured final volume.
  snapshot_sha256: 2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36
- evidence_id: mediadive1661api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1661
  locator: Entire exact main recipe, three stocks and full preparation; both primary
    PDF pages visually inspected
  accessed_at: '2026-10-21T13:16:20.978040Z'
  support: supports
  summary: All source amounts, supplied forms, stages and preparation compared, keeping
    the provider 1003 mL declaration separate from measured final volume.
  snapshot_sha256: 4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273
- evidence_id: dsmz320
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf
  locator: SL-10 stock only
  accessed_at: '2026-10-21T13:20:08.151265Z'
  support: supports
  summary: Exact stock context; parent medium formulations and organism claims are
    not transferred.
  snapshot_sha256: d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9
- evidence_id: dsmz385
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf
  locator: Selenite-tungstate stock only
  accessed_at: '2026-10-21T13:20:08.153235Z'
  support: supports
  summary: Exact stock context; parent medium formulations and organism claims are
    not transferred.
  snapshot_sha256: d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22
- evidence_id: dsmz120
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf
  locator: Wolin vitamin solution (10x) only
  accessed_at: '2026-10-21T13:16:27.298931Z'
  support: supports
  summary: Exact stock context; parent medium formulations and organism claims are
    not transferred.
  snapshot_sha256: e1f85e4a546abc825218226bbb18d78bd9c054b7e11399aa7161ad259a3b663f
- evidence_id: solution595
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/595
  locator: Entire SL-10 endpoint
  accessed_at: '2026-10-21T11:03:05.357684Z'
  support: supports
  summary: Exact stock context; parent medium formulations and organism claims are
    not transferred.
  snapshot_sha256: 5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab
- evidence_id: solution777
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/777
  locator: Entire selenite-tungstate endpoint
  accessed_at: '2026-10-21T13:20:07.510517Z'
  support: supports
  summary: Exact stock context; parent medium formulations and organism claims are
    not transferred.
  snapshot_sha256: 3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2
- evidence_id: solution5980
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5980
  locator: Entire vitamin endpoint
  accessed_at: '2026-10-21T11:03:05.362213Z'
  support: supports
  summary: Exact stock context; parent medium formulations and organism claims are
    not transferred.
  snapshot_sha256: 2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c
- evidence_id: mediadive161api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/161
  locator: Only solution5980 at data.solutions[4], referenced by existing vitamin
    evidence
  accessed_at: '2026-10-21T11:09:26.550249Z'
  support: supports
  summary: Exact stock context; parent medium formulations and organism claims are
    not transferred.
  snapshot_sha256: 53d710b65b9a45b9d21c2fddd18a86b41de41d18c0a4c2cbd7de44b0a2ef8666
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
- evidence_id: chebi144421
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_144421
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T13:16:22.419325Z'
  support: supports
  summary: CHEBI:144421 resolves to iron(III) citrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 283ce05a4ff7d7b60c46f1b8447bc5f217ea1d84543f59ad566eb9f893b768a1
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
- evidence_id: chebi32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:28.263004Z'
  support: supports
  summary: CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
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
  accessed_at: '2026-10-21T13:36:55Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:144421": [{"label": "Fe(III) citrate",
    "match_type": "preferred_term", "identifier": "CHEBI:144421", "preferred_term":
    "Fe(III) citrate", "ontology_id": "CHEBI:144421", "mapping_status": "MAPPED",
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
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label":
    "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term":
    "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
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
    "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier":
    "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type":
    "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id":
    "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118":
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
    "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213":
    [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term":
    "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345":
    [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier":
    "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: stock-evidence-recheck
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/226/stock-evidence-recheck.json
  locator: All 25 current composition amounts,26 attached evidence objects, complete
    histories and historical snapshots
  accessed_at: '2026-10-21T13:36:55Z'
  support: supports
  summary: Stock 595 already retains HCl as 0.01 L, explicit water make-up and withdrawal
    of generic nickel CHEBI. Stocks 777/5980 retain 1 L water additions and nominal
    provider concentrations. These repairs and attached claims do not propagate into
    the reviewed flat medium. All original explanations/history were read; timestamps
    with absent timezone remain contextual historical issues.
  snapshot_sha256: de627829aae645c0c14b9abe8d7aa4cf1e516e8af766e062f4cc19f94b3f08de
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/226/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:36:55Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 56bf0b5e4425675cd88f276e7d2b2fbdff79e8a3a71fe3eb0326dcce37b5e4fb
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/226/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T13:36:55Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: e18131fa6fd166bd822341c3e0058bf28885e675fc21678e22ab944572de1d4b
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T13:36:55Z'
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
  accessed_at: '2026-10-21T13:36:55Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T13:36:55Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILUS_NAMSARAEVII_MEDIUM.yaml; data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:36:55Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '28 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 28/29 primary and 27/29 secondary
    instances; all asserted mediaingredientmech_chebi_term keys have exact pinned
    MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and
    labels do not establish correct source grounding.'
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131361
  - chebi144421
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi176843
  - chebi17883
  - chebi26710
  - chebi27470
  - chebi29377
  - chebi30753
  - chebi30961
  - chebi31345
  - chebi32139
  - chebi32145
  - chebi33118
  - chebi34887
  - chebi49105
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  details: 'Instance coverage on a 0–100 percent scale, denominator 29: primary 96.55%;
    secondary 93.10%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 73 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"Main sol. 1661 / KH2PO4\",\n\
    \    \"field_path\": \"ingredients[0].concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"KH2PO4\\\",\\n                \
    \        \\\"compound_id\\\": 11,\\n                        \\\"amount\\\": 0.5,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.498504,\\n                        \\\"mmol_l\\\": 3.66318,\\n   \
    \                     \\\"optional\\\": 0\\n                    }\",\n       \
    \ \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1661 subsection row 1\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.50 g\",\n        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"The local value matches the provider’s\
    \ rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence.\
    \ Preserve original source mass and nominal basis; later ferric/Mg stock additions\
    \ and titration do not establish measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.498504\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.498504\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"0.5 g / 1.003 L = 0.4985044865403788634097706879 g/L conditionally; stored/provider\
    \ value 0.498504 is rounded, not exact.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1661 / NaCl\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 25,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 24.9252,\\n            \
    \            \\\"mmol_l\\\": 426.51,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1661 subsection row 2\",\n        \"exact_source_quote\"\
    : \"NaCl 25.00 g\",\n        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"The local value matches the provider’s\
    \ rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence.\
    \ Preserve original source mass and nominal basis; later ferric/Mg stock additions\
    \ and titration do not establish measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"24.9252\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"24.9252\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"25 g / 1.003 L = 24.92522432701894317048853440 g/L conditionally; stored/provider\
    \ value 24.9252 is rounded, not exact.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1661 / Yeast extract\",\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 2.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.49252,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1661 subsection row 3\",\n        \"exact_source_quote\"\
    : \"Yeast extract 2.50 g\",\n        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"The local value matches the provider’s\
    \ rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence.\
    \ Preserve original source mass and nominal basis; later ferric/Mg stock additions\
    \ and titration do not establish measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2.49252\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.49252\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"2.5 g / 1.003 L = 2.492522432701894317048853440 g/L conditionally; stored/provider\
    \ value 2.49252 is rounded, not exact.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1661 / NaHCO3\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"NaHCO3\\\",\\n                        \\\"compound_id\\\": 55,\\\
    n                        \\\"amount\\\": 1.85,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.84447,\\n      \
    \                  \\\"mmol_l\\\": 21.9561,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1661 subsection row 4\",\n        \"exact_source_quote\"\
    : \"NaHCO3 1.85 g\",\n        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"The local value matches the provider’s\
    \ rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence.\
    \ Preserve original source mass and nominal basis; later ferric/Mg stock additions\
    \ and titration do not establish measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.84447\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.84447\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"1.85 g / 1.003 L = 1.844466600199401794616151545 g/L conditionally; stored/provider\
    \ value 1.84447 is rounded, not exact.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1661 / Na2CO3\",\n    \"field_path\": \"ingredients[4].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Na2CO3\\\",\\n                        \\\"compound_id\\\": 32,\\\
    n                        \\\"amount\\\": 1.2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.19641,\\n            \
    \            \\\"mmol_l\\\": 11.2882,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1661 subsection row 5\",\n        \"exact_source_quote\"\
    : \"Na2CO3 1.20 g\",\n        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"The local value matches the provider’s\
    \ rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence.\
    \ Preserve original source mass and nominal basis; later ferric/Mg stock additions\
    \ and titration do not establish measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.19641\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.19641\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"1.2 g / 1.003 L = 1.196410767696909272183449651 g/L conditionally; stored/provider\
    \ value 1.19641 is rounded, not exact.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1661 / Trace element solution SL-10\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution SL-10\\\",\\n                       \
    \ \\\"solution_id\\\": 595,\\n                        \\\"amount\\\": 1,\\n  \
    \                      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1661 subsection row 6\",\n        \"exact_source_quote\"\
    : \"Trace element solution SL-10 1.00 ml\",\n        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Restore this exact stock-addition or solvent\
    \ quantity at its source stage. The three named stocks each have a 1 mL receiving\
    \ dose; stock water remains separate from main water.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1661 / Selenite-tungstate solution\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Selenite-tungstate solution\\\",\\n                        \\\
    \"solution_id\\\": 777,\\n                        \\\"amount\\\": 1,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1661 subsection row 7\",\n        \"exact_source_quote\"\
    : \"Selenite-tungstate solution 1.00 ml\",\n        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Restore this exact stock-addition or solvent\
    \ quantity at its source stage. The three named stocks each have a 1 mL receiving\
    \ dose; stock water remains separate from main water.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1661 / Fe(III) citrate\",\n    \"field_path\": \"ingredients[5].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Fe(III) citrate\\\",\\n                        \\\"compound_id\\\
    \": 45,\\n                        \\\"attribute\\\": \\\"19% Fe\\\",\\n      \
    \                  \\\"amount\\\": 7.3,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 7.27817,\\n              \
    \          \\\"mmol_l\\\": 29.7136,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1661 subsection row 8\",\n        \"exact_source_quote\"\
    : \"Fe(III) citrate (19% Fe) 7.30 g\",\n        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"The local value matches the provider’s\
    \ rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence.\
    \ Preserve original source mass and nominal basis; later ferric/Mg stock additions\
    \ and titration do not establish measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"7.27817\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7.27817\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"7.3 g / 1.003 L = 7.278165503489531405782652044 g/L conditionally; stored/provider\
    \ value 7.27817 is rounded, not exact.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1661 / MgCl2 x 6 H2O\",\n    \"field_path\": \"ingredients[6].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 79,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.199402,\\\
    n                        \\\"mmol_l\\\": 0.980811,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\"\
    ,\n        \"source_locator\": \"Main sol. 1661 subsection row 9\",\n        \"\
    exact_source_quote\": \"MgCl2 x 6 H2O 0.20 g\",\n        \"snapshot_sha256\":\
    \ \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"The local value matches the provider’s\
    \ rounded nominal g/L on its declared 1003 mL basis but lacks attached evidence.\
    \ Preserve original source mass and nominal basis; later ferric/Mg stock additions\
    \ and titration do not establish measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.199402\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.199402\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"0.2 g / 1.003 L = 0.1994017946161515453639082752 g/L conditionally; stored/provider\
    \ value 0.199402 is rounded, not exact.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1661 / Wolin's vitamin solution (10x)\",\n    \"field_path\": \"\
    solutions\",\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                   \
    \     \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\"\
    ,\n        \"source_locator\": \"Main sol. 1661 subsection row 10\",\n       \
    \ \"exact_source_quote\": \"Wolin's vitamin solution (10x) 1.00 ml\",\n      \
    \  \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Restore this exact stock-addition or solvent\
    \ quantity at its source stage. The three named stocks each have a 1 mL receiving\
    \ dose; stock water remains separate from main water.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1661 / Distilled water\",\n    \"field_path\": \"solutions\",\n\
    \    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1661 subsection row 11\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Restore this exact stock-addition or solvent\
    \ quantity at its source stage. The three named stocks each have a 1 mL receiving\
    \ dose; stock water remains separate from main water.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace element solution SL-10 / HCl\",\n    \"field_path\": \"ingredients[7].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"HCl\\\",\\n                        \\\"compound_id\\\": 68,\\\
    n                        \\\"attribute\\\": \\\"25%\\\",\\n                  \
    \      \\\"amount\\\": 10,\\n                        \\\"unit\\\": \\\"ml\\\"\
    ,\\n                        \\\"g_l\\\": 2.5,\\n                        \\\"mmol_l\\\
    \": 68.5683,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Trace element solution SL-10 subsection row 1\",\n\
    \        \"exact_source_quote\": \"HCl (25%) 10.00 ml\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"The source specifies 10 mL HCl 25% within\
    \ SL-10; neither percent basis nor density is supplied. Provider g_l2.5 cannot\
    \ validate a neat-solute conversion, and undiluted stock is not final medium.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2.5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Restore\
    \ 10 mL liquid input (=0.010 L) and literal 25%; no pure-HCl grams or molarity\
    \ inferred.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace element solution\
    \ SL-10 / FeCl2 x 4 H2O\",\n    \"field_path\": \"ingredients[8].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"FeCl2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 260,\\n                        \\\"amount\\\": 1.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n\
    \                        \\\"mmol_l\\\": 7.54482,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\"\
    ,\n        \"source_locator\": \"Trace element solution SL-10 subsection row 2\"\
    ,\n        \"exact_source_quote\": \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n     \
    \   \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the provider-declared 1 L stock basis, 1.5 g/L × 0.001 L would deliver 0.0015\
    \ g; this conditional mass is not final medium g/L.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace element solution SL-10 / ZnCl2\",\n    \"field_path\": \"ingredients[9].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"ZnCl2\\\",\\n                        \\\"compound_id\\\": 64,\\\
    n                        \\\"amount\\\": 70,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.07,\\n              \
    \          \\\"mmol_l\\\": 0.513573,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Trace element solution SL-10 subsection row 3\",\n\
    \        \"exact_source_quote\": \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[9].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider-declared 1 L stock basis, 0.07 g/L × 0.001 L would deliver\
    \ 0.00007 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n   \
    \ \"ingredient_or_context\": \"Trace element solution SL-10 / MnCl2 x 4 H2O\"\
    ,\n    \"field_path\": \"ingredients[10].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[3]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 4,\\\
    n                        \\\"compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 36,\\n                        \\\"amount\\\
    \": 100,\\n                        \\\"unit\\\": \\\"mg\\\",\\n              \
    \          \\\"g_l\\\": 0.1,\\n                        \\\"mmol_l\\\": 0.505293,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Trace element solution SL-10 subsection row 4\",\n\
    \        \"exact_source_quote\": \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[10].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the provider-declared 1 L stock basis, 0.1 g/L × 0.001 L would deliver 0.0001\
    \ g; this conditional mass is not final medium g/L.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace element solution SL-10 / H3BO3\",\n    \"field_path\": \"ingredients[11].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\": 37,\\\
    n                        \\\"amount\\\": 6,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.006,\\n             \
    \           \\\"mmol_l\\\": 0.0970246,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Trace element solution SL-10 subsection row 5\",\n\
    \        \"exact_source_quote\": \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[11].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the provider-declared 1 L stock basis, 0.006 g/L × 0.001 L would deliver\
    \ 0.000006 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n  \
    \  \"ingredient_or_context\": \"Trace element solution SL-10 / CoCl2 x 6 H2O\"\
    ,\n    \"field_path\": \"ingredients[12].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 38,\\n                        \\\"amount\\\
    \": 190,\\n                        \\\"unit\\\": \\\"mg\\\",\\n              \
    \          \\\"g_l\\\": 0.19,\\n                        \\\"mmol_l\\\": 1.46335,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Trace element solution SL-10 subsection row 6\",\n\
    \        \"exact_source_quote\": \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[12].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider-declared 1 L stock basis, 0.19 g/L × 0.001 L would deliver\
    \ 0.00019 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n   \
    \ \"ingredient_or_context\": \"Trace element solution SL-10 / CuCl2 x 2 H2O\"\
    ,\n    \"field_path\": \"ingredients[13].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[6]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 7,\\\
    n                        \\\"compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 39,\\n                        \\\"amount\\\
    \": 2,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                \
    \        \\\"g_l\\\": 0.002,\\n                        \\\"mmol_l\\\": 0.0117314,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Trace element solution SL-10 subsection row 7\",\n\
    \        \"exact_source_quote\": \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[13].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the provider-declared 1 L stock basis, 0.002 g/L × 0.001 L would deliver\
    \ 0.000002 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n  \
    \  \"ingredient_or_context\": \"Trace element solution SL-10 / NiCl2 x 6 H2O\"\
    ,\n    \"field_path\": \"ingredients[14].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[7]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 8,\\\
    n                        \\\"compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 40,\\n                        \\\"amount\\\
    \": 24,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.024,\\n                        \\\"mmol_l\\\": 0.185187,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Trace element solution SL-10 subsection row 8\",\n\
    \        \"exact_source_quote\": \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[14].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the provider-declared 1 L stock basis, 0.024 g/L × 0.001 L would deliver\
    \ 0.000024 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n  \
    \  \"ingredient_or_context\": \"Trace element solution SL-10 / Na2MoO4 x 2 H2O\"\
    ,\n    \"field_path\": \"ingredients[15].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n       \
    \                 \\\"compound_id\\\": 9,\\n                        \\\"amount\\\
    \": 36,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.036,\\n                        \\\"mmol_l\\\": 0.148791,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Trace element solution SL-10 subsection row 9\",\n\
    \        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[15].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the provider-declared 1 L stock basis, 0.036 g/L × 0.001 L would deliver\
    \ 0.000036 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n  \
    \  \"ingredient_or_context\": \"Trace element solution SL-10 / Distilled water\"\
    ,\n    \"field_path\": \"solutions\",\n    \"decision\": \"add\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1661api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\",\n \
    \       \"source_locator\": \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 10,\\n                 \
    \       \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 990,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Trace element solution SL-10 subsection row 10\",\n\
    \        \"exact_source_quote\": \"Distilled water 990.00 ml\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Restore this exact stock-addition or solvent\
    \ quantity at its source stage. The three named stocks each have a 1 mL receiving\
    \ dose; stock water remains separate from main water.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Selenite-tungstate solution / NaOH\",\n    \"field_path\": \"ingredients[16].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"NaOH\\\",\\n                        \\\"compound_id\\\": 256,\\\
    n                        \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n                \
    \        \\\"mmol_l\\\": 12.5009,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Selenite-tungstate solution subsection row 1\",\n\
    \        \"exact_source_quote\": \"NaOH 0.50 g\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[16].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the provider-declared 1 L stock basis, 0.5 g/L × 0.001 L would deliver 0.0005\
    \ g; this conditional mass is not final medium g/L.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Selenite-tungstate solution / Na2SeO3 x 5 H2O\",\n    \"field_path\": \"ingredients[17].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Na2SeO3 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 107,\\n                        \\\"amount\\\": 3,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.003,\\\
    n                        \\\"mmol_l\\\": 0.0114062,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Selenite-tungstate solution subsection row 2\",\n\
    \        \"exact_source_quote\": \"Na2SeO3 x 5 H2O 3.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[17].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the provider-declared 1 L stock basis, 0.003 g/L × 0.001 L would deliver\
    \ 0.000003 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n  \
    \  \"ingredient_or_context\": \"Selenite-tungstate solution / Na2WO4 x 2 H2O\"\
    ,\n    \"field_path\": \"ingredients[18].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[2].recipe[2]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 3,\\\
    n                        \\\"compound\\\": \\\"Na2WO4 x 2 H2O\\\",\\n        \
    \                \\\"compound_id\\\": 249,\\n                        \\\"amount\\\
    \": 4,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                \
    \        \\\"g_l\\\": 0.004,\\n                        \\\"mmol_l\\\": 0.0121267,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Selenite-tungstate solution subsection row 3\",\n\
    \        \"exact_source_quote\": \"Na2WO4 x 2 H2O 4.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[18].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the provider-declared 1 L stock basis, 0.004 g/L × 0.001 L would deliver\
    \ 0.000004 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n  \
    \  \"ingredient_or_context\": \"Selenite-tungstate solution / Distilled water\"\
    ,\n    \"field_path\": \"solutions\",\n    \"decision\": \"add\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1661api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\",\n \
    \       \"source_locator\": \"$.data.solutions[2].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 1000,\\n     \
    \                   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Selenite-tungstate solution subsection row 4\",\n\
    \        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Restore this exact stock-addition or solvent\
    \ quantity at its source stage. The three named stocks each have a 1 mL receiving\
    \ dose; stock water remains separate from main water.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x) / Biotin\",\n    \"field_path\": \"ingredients[19].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Biotin\\\",\\n                        \\\"compound_id\\\": 46,\\\
    n                        \\\"amount\\\": 20,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.02,\\n              \
    \          \\\"mmol_l\\\": 0.0818632,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection row 1\"\
    ,\n        \"exact_source_quote\": \"Biotin 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[19].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider-declared 1 L stock basis, 0.02 g/L × 0.001 L would deliver\
    \ 0.00002 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n   \
    \ \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Folic acid\",\n\
    \    \"field_path\": \"ingredients[20].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[3].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Folic acid\\\",\\n            \
    \            \\\"compound_id\\\": 138,\\n                        \\\"amount\\\"\
    : 20,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                 \
    \       \\\"g_l\\\": 0.02,\\n                        \\\"mmol_l\\\": 0.0453104,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection row 2\"\
    ,\n        \"exact_source_quote\": \"Folic acid 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[20].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider-declared 1 L stock basis, 0.02 g/L × 0.001 L would deliver\
    \ 0.00002 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n   \
    \ \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Pyridoxine hydrochloride\"\
    ,\n    \"field_path\": \"ingredients[21].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[3].recipe[2]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 3,\\\
    n                        \\\"compound\\\": \\\"Pyridoxine hydrochloride\\\",\\\
    n                        \\\"compound_id\\\": 519,\\n                        \\\
    \"amount\\\": 100,\\n                        \\\"unit\\\": \\\"mg\\\",\\n    \
    \                    \\\"g_l\\\": 0.1,\\n                        \\\"mmol_l\\\"\
    : 0.486287,\\n                        \\\"optional\\\": 0\\n                 \
    \   }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection row 3\"\
    ,\n        \"exact_source_quote\": \"Pyridoxine hydrochloride 100.00 mg\",\n \
    \       \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[21].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the provider-declared 1 L stock basis, 0.1 g/L × 0.001 L would deliver 0.0001\
    \ g; this conditional mass is not final medium g/L.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x) / Thiamine HCl\",\n    \"field_path\": \"ingredients[22].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1661api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1661\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Thiamine HCl\\\",\\n                        \\\"compound_id\\\
    \": 1207,\\n                        \\\"amount\\\": 50,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.05,\\\
    n                        \\\"mmol_l\\\": 0.148236,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\"\
    ,\n        \"source_locator\": \"Wolin's vitamin solution (10x) subsection row\
    \ 4\",\n        \"exact_source_quote\": \"Thiamine HCl 50.00 mg\",\n        \"\
    snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[22].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider-declared 1 L stock basis, 0.05 g/L × 0.001 L would deliver\
    \ 0.00005 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n   \
    \ \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Riboflavin\",\n\
    \    \"field_path\": \"ingredients[23].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[3].recipe[4]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 5,\\\
    n                        \\\"compound\\\": \\\"Riboflavin\\\",\\n            \
    \            \\\"compound_id\\\": 136,\\n                        \\\"amount\\\"\
    : 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                 \
    \       \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.132837,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection row 5\"\
    ,\n        \"exact_source_quote\": \"Riboflavin 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[23].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider-declared 1 L stock basis, 0.05 g/L × 0.001 L would deliver\
    \ 0.00005 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n   \
    \ \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Nicotinic acid\"\
    ,\n    \"field_path\": \"ingredients[24].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[3].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"Nicotinic acid\\\",\\n        \
    \                \\\"compound_id\\\": 139,\\n                        \\\"amount\\\
    \": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.406141,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection row 6\"\
    ,\n        \"exact_source_quote\": \"Nicotinic acid 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[24].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider-declared 1 L stock basis, 0.05 g/L × 0.001 L would deliver\
    \ 0.00005 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n   \
    \ \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Calcium D-(+)-pantothenate\"\
    ,\n    \"field_path\": \"ingredients[25].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[3].recipe[6]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 7,\\\
    n                        \\\"compound\\\": \\\"Calcium D-(+)-pantothenate\\\"\
    ,\\n                        \\\"compound_id\\\": 1512,\\n                    \
    \    \\\"amount\\\": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\\
    n                        \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\
    \": 0.209846,\\n                        \\\"optional\\\": 0\\n               \
    \     }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection row 7\"\
    ,\n        \"exact_source_quote\": \"Calcium D-(+)-pantothenate 50.00 mg\",\n\
    \        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[25].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider-declared 1 L stock basis, 0.05 g/L × 0.001 L would deliver\
    \ 0.00005 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n   \
    \ \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Vitamin B12\"\
    ,\n    \"field_path\": \"ingredients[26].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[3].recipe[7]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 8,\\\
    n                        \\\"compound\\\": \\\"Vitamin B12\\\",\\n           \
    \             \\\"compound_id\\\": 18,\\n                        \\\"amount\\\"\
    : 1,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                  \
    \      \\\"g_l\\\": 0.001,\\n                        \\\"mmol_l\\\": 0.00073779,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection row 8\"\
    ,\n        \"exact_source_quote\": \"Vitamin B12 1.00 mg\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[26].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the provider-declared 1 L stock basis, 0.001 g/L × 0.001 L would deliver\
    \ 0.000001 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n  \
    \  \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / p-Aminobenzoic\
    \ acid\",\n    \"field_path\": \"ingredients[27].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[3].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"compound\\\": \\\"p-Aminobenzoic acid\\\",\\n   \
    \                     \\\"compound_id\\\": 47,\\n                        \\\"\
    amount\\\": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n       \
    \                 \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\"\
    : 0.364591,\\n                        \\\"optional\\\": 0\\n                 \
    \   }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection row 9\"\
    ,\n        \"exact_source_quote\": \"p-Aminobenzoic acid 50.00 mg\",\n       \
    \ \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[27].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider-declared 1 L stock basis, 0.05 g/L × 0.001 L would deliver\
    \ 0.00005 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n   \
    \ \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / (DL)-alpha-Lipoic\
    \ acid\",\n    \"field_path\": \"ingredients[28].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1661api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\"\
    ,\n        \"source_locator\": \"$.data.solutions[3].recipe[9]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 10,\\\
    n                        \\\"compound\\\": \\\"(DL)-alpha-Lipoic acid\\\",\\n\
    \                        \\\"compound_id\\\": 252,\\n                        \\\
    \"amount\\\": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n     \
    \                   \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\"\
    : 0.24233,\\n                        \\\"optional\\\": 0\\n                  \
    \  }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection row 10\"\
    ,\n        \"exact_source_quote\": \"(DL)-alpha-Lipoic acid 50.00 mg\",\n    \
    \    \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"A concentration within an undiluted stock\
    \ is stored as a direct medium concentration. Restore stock composition and its\
    \ separate 1 mL receiving dose; exact measured receiving-medium volume remains\
    \ unknown.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[28].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider-declared 1 L stock basis, 0.05 g/L × 0.001 L would deliver\
    \ 0.00005 g; this conditional mass is not final medium g/L.\"\n  },\n  {\n   \
    \ \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Distilled water\"\
    ,\n    \"field_path\": \"solutions\",\n    \"decision\": \"add\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1661api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1661\",\n \
    \       \"source_locator\": \"$.data.solutions[3].recipe[10]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 11,\\n                 \
    \       \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 1000,\\n     \
    \                   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"4e1cdb685fbad33d972886aef830396b573616cf751c92664a1e552ee6120273\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection row 11\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"\
    snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Restore this exact stock-addition or solvent\
    \ quantity at its source stage. The three named stocks each have a 1 mL receiving\
    \ dose; stock water remains separate from main water.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 595: HCl\",\n    \"field_path\": \"composition[0].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution595\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/595\",\n        \"source_locator\"\
    : \"$.data.recipe[0]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 1,\\n                \\\"compound\\\": \\\"HCl\\\",\\\
    n                \\\"compound_id\\\": 68,\\n                \\\"solution\\\":\
    \ null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": \\\"25%\\\",\\n               \
    \ \\\"amount\\\": 10,\\n                \\\"unit\\\": \\\"ml\\\",\\n         \
    \       \\\"g_l\\\": 2.5,\\n                \\\"mmol_l\\\": 68.5683,\\n      \
    \          \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab\"\n     \
    \ }\n    ],\n    \"rationale\": \"10 mL HCl 25% input equals 0.01 L; unknown percentage\
    \ basis and density are explicitly retained. Existing attached same-layer evidence\
    \ matches the exact captured row/hash; this does not certify all chemical mappings\
    \ or receiving-medium dilution.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"L\"\n        },\n \
    \       \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 595: FeCl2 x 4 H2O\",\n    \"field_path\": \"composition[1].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution595\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/595\",\n        \"source_locator\"\
    : \"$.data.recipe[1]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 2,\\n                \\\"compound\\\": \\\"FeCl2 x 4\
    \ H2O\\\",\\n                \\\"compound_id\\\": 260,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 1.5,\\n                \\\"unit\\\": \\\"g\\\"\
    ,\\n                \\\"g_l\\\": 1.5,\\n                \\\"mmol_l\\\": 7.54482,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 595: ZnCl2\",\n    \"field_path\": \"composition[2].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution595\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/595\",\n        \"source_locator\"\
    : \"$.data.recipe[2]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 3,\\n                \\\"compound\\\": \\\"ZnCl2\\\"\
    ,\\n                \\\"compound_id\\\": 64,\\n                \\\"solution\\\"\
    : null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 70,\\n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\
    \": 0.07,\\n                \\\"mmol_l\\\": 0.513573,\\n                \\\"optional\\\
    \": 0\\n            }\",\n        \"snapshot_sha256\": \"5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab\"\
    \n      }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis;\
    \ not independently measured final volume. Existing attached same-layer evidence\
    \ matches the exact captured row/hash; this does not certify all chemical mappings\
    \ or receiving-medium dilution.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 595: MnCl2 x 4 H2O\",\n    \"field_path\": \"composition[3].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution595\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/595\",\n        \"source_locator\"\
    : \"$.data.recipe[3]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 4,\\n                \\\"compound\\\": \\\"MnCl2 x 4\
    \ H2O\\\",\\n                \\\"compound_id\\\": 36,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 100,\\n                \\\"unit\\\": \\\"mg\\\",\\n    \
    \            \\\"g_l\\\": 0.1,\\n                \\\"mmol_l\\\": 0.505293,\\n\
    \                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 595: H3BO3\",\n    \"field_path\": \"composition[4].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution595\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/595\",\n        \"source_locator\"\
    : \"$.data.recipe[4]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 5,\\n                \\\"compound\\\": \\\"H3BO3\\\"\
    ,\\n                \\\"compound_id\\\": 37,\\n                \\\"solution\\\"\
    : null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 6,\\n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\
    \": 0.006,\\n                \\\"mmol_l\\\": 0.0970246,\\n                \\\"\
    optional\\\": 0\\n            }\",\n        \"snapshot_sha256\": \"5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab\"\
    \n      }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis;\
    \ not independently measured final volume. Existing attached same-layer evidence\
    \ matches the exact captured row/hash; this does not certify all chemical mappings\
    \ or receiving-medium dilution.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 595: CoCl2 x 6 H2O\",\n    \"field_path\": \"composition[5].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution595\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/595\",\n        \"source_locator\"\
    : \"$.data.recipe[5]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 6,\\n                \\\"compound\\\": \\\"CoCl2 x 6\
    \ H2O\\\",\\n                \\\"compound_id\\\": 38,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 190,\\n                \\\"unit\\\": \\\"mg\\\",\\n    \
    \            \\\"g_l\\\": 0.19,\\n                \\\"mmol_l\\\": 1.46335,\\n\
    \                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 595: CuCl2 x 2 H2O\",\n    \"field_path\": \"composition[6].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution595\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/595\",\n        \"source_locator\"\
    : \"$.data.recipe[6]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 7,\\n                \\\"compound\\\": \\\"CuCl2 x 2\
    \ H2O\\\",\\n                \\\"compound_id\\\": 39,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 2,\\n                \\\"unit\\\": \\\"mg\\\",\\n      \
    \          \\\"g_l\\\": 0.002,\\n                \\\"mmol_l\\\": 0.0117314,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 595: NiCl2 x 6 H2O\",\n    \"field_path\": \"composition[7].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution595\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/595\",\n        \"source_locator\"\
    : \"$.data.recipe[7]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 8,\\n                \\\"compound\\\": \\\"NiCl2 x 6\
    \ H2O\\\",\\n                \\\"compound_id\\\": 40,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 24,\\n                \\\"unit\\\": \\\"mg\\\",\\n     \
    \           \\\"g_l\\\": 0.024,\\n                \\\"mmol_l\\\": 0.185187,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 595: Na2MoO4 x 2 H2O\",\n    \"field_path\": \"composition[8].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution595\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/595\",\n        \"source_locator\"\
    : \"$.data.recipe[8]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 9,\\n                \\\"compound\\\": \\\"Na2MoO4 x\
    \ 2 H2O\\\",\\n                \\\"compound_id\\\": 9,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 36,\\n                \\\"unit\\\": \\\"mg\\\"\
    ,\\n                \\\"g_l\\\": 0.036,\\n                \\\"mmol_l\\\": 0.148791,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 595: Distilled water\",\n    \"field_path\": \"composition[9].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution595\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/595\",\n        \"source_locator\"\
    : \"$.data.recipe[9]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 10,\\n                \\\"compound\\\": \\\"Distilled\
    \ water\\\",\\n                \\\"compound_id\\\": 4,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 990,\\n                \\\"unit\\\": \\\"ml\\\
    \",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\": null,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab\"\n     \
    \ }\n    ],\n    \"rationale\": \"Explicit SL-10 final make-up to 1000 mL, separate\
    \ from the 990 mL listed water. Existing attached same-layer evidence matches\
    \ the exact captured row/hash; this does not certify all chemical mappings or\
    \ receiving-medium dilution.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"to 1 L final volume\",\n          \"unit\": \"VARIABLE\"\
    \n        },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Context stock 777: NaOH\",\n    \"field_path\"\
    : \"composition[0].concentration\",\n    \"decision\": \"verified\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"solution777\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/777\",\n\
    \        \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 1,\\n                \\\"compound\\\
    \": \\\"NaOH\\\",\\n                \\\"compound_id\\\": 256,\\n             \
    \   \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n  \
    \              \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\\
    n                \\\"amount\\\": 0.5,\\n                \\\"unit\\\": \\\"g\\\"\
    ,\\n                \\\"g_l\\\": 0.5,\\n                \\\"mmol_l\\\": 12.5009,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 777: Na2SeO3 x 5 H2O\",\n    \"field_path\": \"composition[1].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution777\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/777\",\n        \"source_locator\"\
    : \"$.data.recipe[1]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 2,\\n                \\\"compound\\\": \\\"Na2SeO3 x\
    \ 5 H2O\\\",\\n                \\\"compound_id\\\": 107,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 3,\\n                \\\"unit\\\": \\\"mg\\\"\
    ,\\n                \\\"g_l\\\": 0.003,\\n                \\\"mmol_l\\\": 0.0114062,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 777: Na2WO4 x 2 H2O\",\n    \"field_path\": \"composition[2].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution777\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/777\",\n        \"source_locator\"\
    : \"$.data.recipe[2]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 3,\\n                \\\"compound\\\": \\\"Na2WO4 x 2\
    \ H2O\\\",\\n                \\\"compound_id\\\": 249,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 4,\\n                \\\"unit\\\": \\\"mg\\\"\
    ,\\n                \\\"g_l\\\": 0.004,\\n                \\\"mmol_l\\\": 0.0121267,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 777: Distilled water\",\n    \"field_path\": \"composition[3].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution777\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/777\",\n        \"source_locator\"\
    : \"$.data.recipe[3]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 4,\\n                \\\"compound\\\": \\\"Distilled\
    \ water\\\",\\n                \\\"compound_id\\\": 4,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 1000,\\n                \\\"unit\\\": \\\"ml\\\
    \",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\": null,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2\"\n     \
    \ }\n    ],\n    \"rationale\": \"Source 1000 mL water addition equals 1 L, not\
    \ measured final stock volume. Existing attached same-layer evidence matches the\
    \ exact captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        },\n    \
    \    \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 5980: Biotin\",\n    \"field_path\": \"composition[0].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5980\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5980\",\n        \"source_locator\"\
    : \"$.data.recipe[0]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 1,\\n                \\\"compound\\\": \\\"Biotin\\\"\
    ,\\n                \\\"compound_id\\\": 46,\\n                \\\"solution\\\"\
    : null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 20,\\n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\
    \": 0.02,\\n                \\\"mmol_l\\\": 0.0818632,\\n                \\\"\
    optional\\\": 0\\n            }\",\n        \"snapshot_sha256\": \"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c\"\
    \n      }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis;\
    \ not independently measured final volume. Existing attached same-layer evidence\
    \ matches the exact captured row/hash; this does not certify all chemical mappings\
    \ or receiving-medium dilution.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 5980: Folic acid\",\n    \"field_path\": \"composition[1].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5980\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5980\",\n        \"source_locator\"\
    : \"$.data.recipe[1]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 2,\\n                \\\"compound\\\": \\\"Folic acid\\\
    \",\\n                \\\"compound_id\\\": 138,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 20,\\n                \\\"unit\\\": \\\"mg\\\",\\n     \
    \           \\\"g_l\\\": 0.02,\\n                \\\"mmol_l\\\": 0.0453104,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 5980: Pyridoxine hydrochloride\",\n    \"field_path\": \"composition[2].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5980\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5980\",\n        \"source_locator\"\
    : \"$.data.recipe[2]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 3,\\n                \\\"compound\\\": \\\"Pyridoxine\
    \ hydrochloride\\\",\\n                \\\"compound_id\\\": 519,\\n          \
    \      \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 100,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.1,\\n                \\\"mmol_l\\\
    \": 0.486287,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c\"\
    \n      }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis;\
    \ not independently measured final volume. Existing attached same-layer evidence\
    \ matches the exact captured row/hash; this does not certify all chemical mappings\
    \ or receiving-medium dilution.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 5980: Thiamine HCl\",\n    \"field_path\": \"composition[3].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5980\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5980\",\n        \"source_locator\"\
    : \"$.data.recipe[3]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 4,\\n                \\\"compound\\\": \\\"Thiamine HCl\\\
    \",\\n                \\\"compound_id\\\": 1207,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 50,\\n                \\\"unit\\\": \\\"mg\\\",\\n     \
    \           \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\": 0.148236,\\n\
    \                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 5980: Riboflavin\",\n    \"field_path\": \"composition[4].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5980\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5980\",\n        \"source_locator\"\
    : \"$.data.recipe[4]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 5,\\n                \\\"compound\\\": \\\"Riboflavin\\\
    \",\\n                \\\"compound_id\\\": 136,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 50,\\n                \\\"unit\\\": \\\"mg\\\",\\n     \
    \           \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\": 0.132837,\\n\
    \                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml\"\
    ,\n        \"field_path\": \"composition[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 5980: Nicotinic acid\",\n    \"field_path\": \"composition[5].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5980\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5980\",\n        \"source_locator\"\
    : \"$.data.recipe[5]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 6,\\n                \\\"compound\\\": \\\"Nicotinic\
    \ acid\\\",\\n                \\\"compound_id\\\": 139,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 50,\\n                \\\"unit\\\": \\\"mg\\\"\
    ,\\n                \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\": 0.406141,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 5980: Calcium D-(+)-pantothenate\",\n    \"field_path\": \"\
    composition[6].concentration\",\n    \"decision\": \"verified\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"solution5980\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5980\",\n\
    \        \"source_locator\": \"$.data.recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 7,\\n                \\\"compound\\\
    \": \\\"Calcium D-(+)-pantothenate\\\",\\n                \\\"compound_id\\\"\
    : 1512,\\n                \\\"solution\\\": null,\\n                \\\"solution_id\\\
    \": null,\\n                \\\"condition\\\": null,\\n                \\\"attribute\\\
    \": null,\\n                \\\"amount\\\": 50,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\
    \": 0.209846,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c\"\
    \n      }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis;\
    \ not independently measured final volume. Existing attached same-layer evidence\
    \ matches the exact captured row/hash; this does not certify all chemical mappings\
    \ or receiving-medium dilution.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml\"\
    ,\n        \"field_path\": \"composition[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 5980: Vitamin B12\",\n    \"field_path\": \"composition[7].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5980\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5980\",\n        \"source_locator\"\
    : \"$.data.recipe[7]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 8,\\n                \\\"compound\\\": \\\"Vitamin B12\\\
    \",\\n                \\\"compound_id\\\": 18,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 1,\\n                \\\"unit\\\": \\\"mg\\\",\\n      \
    \          \\\"g_l\\\": 0.001,\\n                \\\"mmol_l\\\": 0.00073779,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml\"\
    ,\n        \"field_path\": \"composition[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 5980: p-Aminobenzoic acid\",\n    \"field_path\": \"composition[8].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5980\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5980\",\n        \"source_locator\"\
    : \"$.data.recipe[8]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 9,\\n                \\\"compound\\\": \\\"p-Aminobenzoic\
    \ acid\\\",\\n                \\\"compound_id\\\": 47,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 50,\\n                \\\"unit\\\": \\\"mg\\\"\
    ,\\n                \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\": 0.364591,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml\"\
    ,\n        \"field_path\": \"composition[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 5980: (DL)-alpha-Lipoic acid\",\n    \"field_path\": \"composition[9].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5980\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5980\",\n        \"source_locator\"\
    : \"$.data.recipe[9]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 10,\\n                \\\"compound\\\": \\\"(DL)-alpha-Lipoic\
    \ acid\\\",\\n                \\\"compound_id\\\": 252,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 50,\\n                \\\"unit\\\": \\\"mg\\\"\
    ,\\n                \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\": 0.24233,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider-declared nominal stock basis; not independently\
    \ measured final volume. Existing attached same-layer evidence matches the exact\
    \ captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml\"\
    ,\n        \"field_path\": \"composition[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Context stock 5980: Distilled water\",\n    \"field_path\": \"composition[10].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5980\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5980\",\n        \"source_locator\"\
    : \"$.data.recipe[10]\",\n        \"exact_source_quote\": \"{\\n             \
    \   \\\"recipe_order\\\": 11,\\n                \\\"compound\\\": \\\"Distilled\
    \ water\\\",\\n                \\\"compound_id\\\": 4,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 1000,\\n                \\\"unit\\\": \\\"ml\\\
    \",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\": null,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c\"\n     \
    \ }\n    ],\n    \"rationale\": \"Source 1000 mL water addition equals 1 L, not\
    \ measured final stock volume. Existing attached same-layer evidence matches the\
    \ exact captured row/hash; this does not certify all chemical mappings or receiving-medium\
    \ dilution.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml\"\
    ,\n        \"field_path\": \"composition[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        },\n    \
    \    \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sparging gas\",\n    \"field_path\": \"preparation.Main_sparging_gas\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation or named stock subsection\",\n\
    \        \"exact_source_quote\": \"100% N2 gas\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Preserved pure-N2 atmosphere has no fixed\
    \ absolute volume.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric\
    \ citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas\
    \ for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate,\
    \ then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10%\
    \ w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements,\
    \ selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration.\
    \ Adjust pH of the complete medium to 9.5, if necessary.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric\
    \ citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas\
    \ for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate,\
    \ then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10%\
    \ w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements,\
    \ selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration.\
    \ Adjust pH of the complete medium to 9.5, if necessary.\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sparging duration\",\n    \"field_path\": \"preparation.Main_sparging_duration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation or named stock subsection\",\n\
    \        \"exact_source_quote\": \"30 - 45 min\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Preserved duration is sparging time, not\
    \ sterilization duration.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric\
    \ citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas\
    \ for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate,\
    \ then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10%\
    \ w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements,\
    \ selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration.\
    \ Adjust pH of the complete medium to 9.5, if necessary.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric\
    \ citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas\
    \ for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate,\
    \ then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10%\
    \ w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements,\
    \ selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration.\
    \ Adjust pH of the complete medium to 9.5, if necessary.\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Initial main pH\",\n    \"field_path\": \"preparation.Initial_main_pH\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation or named stock subsection\",\n\
    \        \"exact_source_quote\": \"then adjust pH to 9.5\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve initial pH endpoint after carbonate\
    \ additions.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n \
    \   \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve\
    \ ingredients (except bicarbonate, carbonate, trace elements, ferric citrate,\
    \ magnesium chloride and vitamins) and sparge medium with 100% N2 gas for 30 -\
    \ 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate, then adjust\
    \ pH to 9.5 and dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Add ferric citrate (10% w/v stock solution;\
    \ dissolve by boiling and adjust pH to 7.5-8.0), trace elements, selenite-tungstate\
    \ solution, magnesium chloride and vitamins from sterile anoxic stock solutions\
    \ prepared under 100% N2 gas. Sterilize vitamins by filtration. Adjust pH of the\
    \ complete medium to 9.5, if necessary.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric\
    \ citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas\
    \ for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate,\
    \ then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10%\
    \ w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements,\
    \ selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration.\
    \ Adjust pH of the complete medium to 9.5, if necessary.\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Final main pH\",\n    \"field_path\": \"preparation.Final_main_pH\",\n   \
    \ \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation or named stock subsection\",\n\
    \        \"exact_source_quote\": \"Adjust pH of the complete medium to 9.5\",\n\
    \        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the final endpoint independently\
    \ of ferric-stock pH.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ph_value\",\n        \"stored\": 9.5,\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.5,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Ferric stock strength\",\n    \"field_path\": \"preparation.Ferric_stock_strength\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation or named stock subsection\",\n\
    \        \"exact_source_quote\": \"10% w/v stock solution\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"This explicit w/v stock strength is retained\
    \ in prose but lacks attached evidence and a structured stock.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Dissolve ingredients (except bicarbonate, carbonate,\
    \ trace elements, ferric citrate, magnesium chloride and vitamins) and sparge\
    \ medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100%\
    \ N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\
    \ Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH\
    \ to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride\
    \ and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas.\
    \ Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if\
    \ necessary.\",\n        \"decision\": \"evidence_only\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric\
    \ citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas\
    \ for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate,\
    \ then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10%\
    \ w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements,\
    \ selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration.\
    \ Adjust pH of the complete medium to 9.5, if necessary.\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Ferric stock pH\",\n    \"field_path\": \"preparation.Ferric_stock_pH\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation or named stock subsection\",\n\
    \        \"exact_source_quote\": \"adjust pH to 7.5-8.0\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"This preserved endpoint belongs to the\
    \ ferric stock, not the final medium.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"preparation_steps[0].description\",\n\
    \        \"stored\": \"Dissolve ingredients (except bicarbonate, carbonate, trace\
    \ elements, ferric citrate, magnesium chloride and vitamins) and sparge medium\
    \ with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate\
    \ and carbonate, then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere\
    \ into anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate\
    \ (10% w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace\
    \ elements, selenite-tungstate solution, magnesium chloride and vitamins from\
    \ sterile anoxic stock solutions prepared under 100% N2 gas. Sterilize vitamins\
    \ by filtration. Adjust pH of the complete medium to 9.5, if necessary.\",\n \
    \       \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\",\n \
    \       \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric\
    \ citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas\
    \ for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate,\
    \ then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10%\
    \ w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements,\
    \ selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration.\
    \ Adjust pH of the complete medium to 9.5, if necessary.\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Stock preparation atmosphere\",\n    \"field_path\": \"preparation.Stock_preparation_atmosphere\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation or named stock subsection\",\n\
    \        \"exact_source_quote\": \"stock solutions prepared under 100% N2 gas\"\
    ,\n        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the stated atmosphere and filtered\
    \ vitamin stage.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric\
    \ citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas\
    \ for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate,\
    \ then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10%\
    \ w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements,\
    \ selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration.\
    \ Adjust pH of the complete medium to 9.5, if necessary.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric\
    \ citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas\
    \ for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate,\
    \ then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10%\
    \ w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements,\
    \ selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration.\
    \ Adjust pH of the complete medium to 9.5, if necessary.\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"SL-10 make-up\",\n    \"field_path\": \"preparation.SL-10_make-up\",\n   \
    \ \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation or named stock subsection\"\
    ,\n        \"exact_source_quote\": \"make up to 1000.00 ml.\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"The literal final make-up belongs to SL-10,\
    \ not the complete medium. Move this instruction into the restored stock scope.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"First dissolve FeCl2 in the HCl, then dilute in water,\
    \ add and dissolve the other salts. Finally make up to 1000.00 ml.\",\n      \
    \  \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Ferric product iron\
    \ qualifier\",\n    \"field_path\": \"preparation.Ferric_product_iron_qualifier\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation or named stock subsection\",\n\
    \        \"exact_source_quote\": \"Fe(III) citrate (19% Fe) 7.30 g\",\n      \
    \  \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Restore source 19% Fe product qualification;\
    \ generic stoichiometric ferric citrate does not establish this product specification.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[5].preferred_term\"\
    ,\n        \"stored\": \"Fe(III) citrate\",\n        \"decision\": \"correct\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].preferred_term\",\n        \"stored\"\
    : \"Fe(III) citrate\",\n        \"decision\": \"correct\"\n      }\n    ]\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Trace acid stock strength\",\n    \"field_path\"\
    : \"preparation.Trace_acid_stock_strength\",\n    \"decision\": \"add\",\n   \
    \ \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1661\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation or named stock subsection\"\
    ,\n        \"exact_source_quote\": \"HCl (25%) 10.00 ml\",\n        \"snapshot_sha256\"\
    : \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\",\n    \
    \    \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve literal 25% within SL-10 with\
    \ unknown percentage basis and density; the source volume is not a neat-solute\
    \ mass.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null,\n        \"decision\": \"add\"\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Vitamin stock factor\",\n    \"field_path\": \"preparation.Vitamin_stock_factor\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation or named stock subsection\",\n\
    \        \"exact_source_quote\": \"Wolin's vitamin solution (10x)\",\n       \
    \ \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the explicitly tenfold vitamin\
    \ stock and its 1 mL addition as different quantities.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Titrant quantity\",\n    \"field_path\": \"preparation.titration_dose\",\n\
    \    \"decision\": \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1661\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1661.pdf\",\n       \
    \ \"source_locator\": \"Final adjustment condition\",\n        \"exact_source_quote\"\
    : \"if necessary.\",\n        \"snapshot_sha256\": \"2c38dcab365a4ded2243135278091471dd24ce0084f30b9da9ade4212e57bb36\"\
    ,\n        \"parsed_text_sha256\": \"1d448da17c80c63e194bac2eff1f40a0f44e445bbf31213a6b3795cf8dbce512\"\
    \n      }\n    ],\n    \"rationale\": \"No fixed titrant identity, normality or\
    \ dose is supplied for the main/ferric endpoints; do not fill from adjacent media.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Dissolve ingredients (except bicarbonate, carbonate,\
    \ trace elements, ferric citrate, magnesium chloride and vitamins) and sparge\
    \ medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ bicarbonate and carbonate, then adjust pH to 9.5 and dispense medium under 100%\
    \ N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\
    \ Add ferric citrate (10% w/v stock solution; dissolve by boiling and adjust pH\
    \ to 7.5-8.0), trace elements, selenite-tungstate solution, magnesium chloride\
    \ and vitamins from sterile anoxic stock solutions prepared under 100% N2 gas.\
    \ Sterilize vitamins by filtration. Adjust pH of the complete medium to 9.5, if\
    \ necessary.\",\n        \"decision\": \"not_quantified\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, carbonate, trace elements, ferric\
    \ citrate, magnesium chloride and vitamins) and sparge medium with 100% N2 gas\
    \ for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate and carbonate,\
    \ then adjust pH to 9.5 and dispense medium under 100% N2 gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. Add ferric citrate (10%\
    \ w/v stock solution; dissolve by boiling and adjust pH to 7.5-8.0), trace elements,\
    \ selenite-tungstate solution, magnesium chloride and vitamins from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Sterilize vitamins by filtration.\
    \ Adjust pH of the complete medium to 9.5, if necessary.\",\n        \"decision\"\
    : \"not_quantified\"\n      }\n    ]\n  }\n]"
- assessment_id: identity
  area: identity
  topic: Exact medium and three scoped stock identities
  outcome: supported
  summary: CM001144 resolves to exact DSMZ1661 and the unique maintained owner. Stock
    595 SL-10,777 selenite-tungstate and5980 tenfold vitamins correspond to the current
    primary’s320/385/120 subsections and have separately inspected local IDs CM014713/CM015156/CM014721.
    MediaDive161 contributes only existing evidence for5980; no parent-medium or organism
    claim is inherited.
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - record
  - owner-0
  - id-search
  - dsmz1661
  - mediadive1661api
  - stock-evidence-recheck
- assessment_id: source-stage-consistency
  area: consistency
  topic: Main nominal amounts versus undiluted stock strengths
  outcome: concern
  summary: All 58 medium concentration instances and 25 stock-context concentrations
    are assessed. Seven main local numbers agree with rounded provider g/L on the
    nominal 1003 mL declaration, without evidence. All 22 stock-derived medium entries
    are misplaced undiluted stock values, including unjustified HCl 2.5 g/L. The three
    1 mL doses and source water are absent from the structured medium. Later ferric/Mg
    stock volume and pH adjustment prevent treating the table’s 1003 mL liquid sum
    as measured final medium volume.
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - record
  - owner-0
  - quantity-inventory
  - quantity-local-fields
  - stock-evidence-recheck
  - dsmz1661
  - mediadive1661api
- assessment_id: forms
  area: grounding
  topic: Nickel hydrate and ferric product specificity
  outcome: concern
  summary: The source explicitly uses nickel dichloride hexahydrate, while medium
    primary/secondary CHEBI:34887 has formula 2Cl.Ni. The maintained 595 stock already
    withdrew this assertion; it is still present in the medium. Ferric citrate is
    explicitly 19% Fe and 7.3 g product, whereas generic CHEBI:144421 does not establish
    that product specification. Calcium D-(+)-pantothenate is compatible with the
    inspected stereospecific term; DL lipoic acid is not narrowed by the unspecified
    structural term. Other explicit stock hydrates match the inspected term structures.
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - record
  - owner-0
  - dsmz1661
  - chebi34887
  - chebi144421
  - chebi31345
  - chebi16494
  - stock-evidence-recheck
- assessment_id: preparation
  area: completeness
  topic: Preserved main instructions and misplaced stock instruction
  outcome: concern
  summary: Main N2 sparging 30–45 min, pH 9.5, ferric 10% w/v stock with pH 7.5–8.0
    and filtered vitamins are preserved but lack attached evidence. The SL-10 make-up
    to 1000 mL instruction is placed as a main step without a stock object. Restore
    the hierarchy and claim linkage; the exact source supplies no numeric autoclave
    cycle.
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - record
  - owner-0
  - dsmz1661
  - quantity-inventory
- assessment_id: stock-context-history
  area: provenance
  topic: Existing stock curation is distinct from medium state
  outcome: supported
  summary: The complete three stock YAMLs contain 25 composition rows and 26 evidence
    objects. Current snippets and capture hashes match exact endpoints, with one additional
    5980 recipe snapshot scoped within 161. Historical placeholder removals, HCl/water
    repairs and nickel withdrawal are preserved in appended changes; they do not certify
    the unchanged medium. All 27 stock timestamp instances were read, including six
    timezone-naive historical values; no old event is rewritten.
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - stock-evidence-recheck
  - solution595
  - solution777
  - solution5980
  - mediadive161api
- assessment_id: classification
  area: scope
  topic: Complex liquid and absent biological assertions
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID fit the yeast-extract liquid source. There
    is no specific strain/taxon/assembly or DOI/PMID growth claim to transfer from
    a dependency. Source accession and stock identity do not establish experimentally
    observed growth for an organism inferred from the medium name.
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - record
  - owner-0
  - dsmz1661
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 15 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: generation
  area: provenance
  topic: Current importer and stale flattened representation
  outcome: concern
  summary: The generated target matches the maintained flat owner; later stock-specific
    repairs did not alter it. Current composition parsing separates the first primary
    solution from later stock definitions; its preparation extraction still iterates
    solution steps. Exact source/context hashes identify maintenance responsibilities
    without claiming a historical replay.
  target_ids:
  - CultureMech:001144
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  - stock-evidence-recheck
  - writer-context-0
  - writer-context-1
  - writer-context-2
findings:
- finding_id: f1
  issue_key: culturemech.001144.stock-flattening
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Undiluted stock compositions are represented as the medium
  description: Three 1 mL stock additions are replaced by 22 direct ingredient strengths
    from SL-10, selenium/tungsten and tenfold vitamins. HCl 25% 10 mL becomes 2.5
    g/L without an explicit percentage basis or density. These combined stage/unit
    errors materially alter the named formulation.
  target_ids:
  - CultureMech:001144
  field_paths:
  - ingredients[7]
  - ingredients[8]
  - ingredients[16]
  - ingredients[19]
  - solutions
  evidence_ids:
  - record
  - owner-0
  - dsmz1661
  - mediadive1661api
  - quantity-inventory
  - stock-evidence-recheck
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml
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
  issue_key: culturemech.001144.supplied-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and ferric product qualification are not preserved
  description: Nickel hexahydrate is grounded to a no-water term in both medium linkage
    fields, although the inspected 595 stock already removed that assertion. The ferric
    ingredient omits the exact 19% Fe product qualification; a generic stoichiometric
    iron(III)citrate identifier does not validate that supplied material.
  target_ids:
  - CultureMech:001144
  field_paths:
  - ingredients[14].term
  - ingredients[14].mediaingredientmech_chebi_term
  - ingredients[5]
  evidence_ids:
  - record
  - owner-0
  - dsmz1661
  - chebi34887
  - chebi144421
  - stock-evidence-recheck
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml
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
  issue_key: culturemech.001144.preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: SL-10 make-up is misplaced as a main preparation step
  description: The second step’s 1000 mL final make-up belongs to SL-10; treating
    it as a main instruction conflicts with distinct source stages. Main preparation
    is largely retained but the stock definitions and claim evidence needed to interpret
    it are missing.
  target_ids:
  - CultureMech:001144
  field_paths:
  - preparation_steps[1]
  - solutions
  - references
  evidence_ids:
  - record
  - owner-0
  - dsmz1661
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3.5 is normalized to major because misassigning the final-volume
    instruction to the main medium changes preparation scope.
actions:
- action_id: a1
  description: Restore three separate stocks, their 1 mL additions, source water and
    exact supplied forms. Retain HCl volume/percentage as stated, and distinguish
    nominal provider concentrations from measured final volume. Attach source evidence
    to the maintained owner before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001144
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml
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
  description: Restore source-specific hydrate/product scope and verify any replacement
    identifier independently. Preserve source masses and ferric-stock strength; do
    not apply anhydrous molecular weights or silently replace the 19% Fe product.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001144
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml
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
  description: Move the retained SL-10 instruction into the correct stock and preserve
    main pH 9.5 versus ferric-stock pH 7.5–8.0, gas, order and filtered vitamins with
    evidence. Do not invent an autoclave cycle or final medium denominator.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001144
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_namsaraevii_medium.yaml
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
- Main 1003 mL and stock 777/5980 nominal 1 L declarations are provider bases, not
  measured volumes after dissolution/titration. SL-10 alone explicitly specifies final
  make-up to 1000 mL.
- HCl 25% percentage basis and density remain unknown. Ferric-citrate19% Fe is a supplied-product
  qualifier. No exact molarity or replacement chemical identifier is inferred.
- Stock historical retrieval-time claims are preserved as history; current literal/hash
  agreement is checked independently and does not authenticate the original retrieval
  event.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-023
- generated-medium
```
