# Source and formulation review: allisonella_medium (CultureMech:003506)

- Review: 20261021T140357Z-culturemech-003506-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:52:36Z
- Finished UTC: 2026-10-21T14:03:57Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated ALLISONELLA record is stale relative to both repaired maintained owners: it retains a false LB-Miller expansion, promotes fatty-acid stock quantities to finished-medium g/L, omits DL-2-methylbutyric acid and source preparation, and still asserts duplicate equivalence. The October repairs already preserve distinct KOMODO rates/nulls and the DSMZ batch/stock formula with evidence; reconcile and regenerate those versions rather than repeat their repair. Sodium-resazurin grounding remains incorrect in the target and DSMZ stock. No final volume, density conversion or growth claim is inferred.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 233; batch 024 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-three task batches contain 230 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 233 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003506 | data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml | generated | allisonella_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003506 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003506 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-024/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch024/233/strict.tsv |
| validate-terms | passed | True | CultureMech:003506 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003506 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003506 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodoMediaList | unavailable | False | CultureMech:003506 | Preserved komodoMediaList retrieval failed (403). No content is claimed from this attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006 formulation provide the required source comparison; the LB page cannot establish membership in this recipe. |
| Exact source content access: komodo1006 | unavailable | False | CultureMech:003506 | Preserved komodo1006 retrieval failed (403). No content is claimed from this attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006 formulation provide the required source comparison; the LB page cannot establish membership in this recipe. |
| Exact source content access: komodoDetail1006 | unavailable | False | CultureMech:003506 | Preserved komodoDetail1006 retrieval failed (403). No content is claimed from this attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006 formulation provide the required source comparison; the LB page cannot establish membership in this recipe. |
| Exact source content access: lbMillerNotes | unavailable | False | CultureMech:003506 | Preserved lbMillerNotes retrieval failed (None). No content is claimed from this attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006 formulation provide the required source comparison; the LB page cannot establish membership in this recipe. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003506.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:003506.

18 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 19/21 primary and 14/21 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 21: primary 90.48%; secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003506.

52 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "DSMZ main: DL-Histidine",
    "field_path": "main_recipe[0]",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"DL-Histidine\",\n                        \"compound_id\": 916,\n                        \"amount\": 7.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 7.76892,\n                        \"mmol_l\": 50.072,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact DL-Histidine table row",
        "exact_source_quote": "   DL-Histidine                                                       7.80         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The repaired DSMZ owner retains the exact batch input with attached API/primary evidence. Its absent final concentration is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured final volume. The target copies a provider g_l value without this basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "7.76892",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "Source batch input: 7.8 g. Preserve the exact mass in notes; API g_l=7.76892 uses the provider's main-volume encoding and is not an independently verified final-medium concentration.",
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "arithmetic": "7.8 g = 7.8 g batch input. On the provider-declared 1.004 L basis, division gives 7.768924302788844621513944223 g/L; source g_l=7.76892 retains its reported precision. Do not silently replace it by the unrounded quotient or recertify the denominator."
  },
  {
    "ingredient_or_context": "DSMZ main: Yeast extract",
    "field_path": "main_recipe[1]",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.98406,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Yeast extract table row",
        "exact_source_quote": "   Yeast extract                                                      4.00         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The repaired DSMZ owner retains the exact batch input with attached API/primary evidence. Its absent final concentration is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured final volume. The target copies a provider g_l value without this basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.98406",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "Source batch input: 4 g. Preserve the exact mass in notes; API g_l=3.98406 uses the provider's main-volume encoding and is not an independently verified final-medium concentration.",
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "arithmetic": "4 g = 4 g batch input. On the provider-declared 1.004 L basis, division gives 3.984063745019920318725099602 g/L; source g_l=3.98406 retains its reported precision. Do not silently replace it by the unrounded quotient or recertify the denominator."
  },
  {
    "ingredient_or_context": "DSMZ main: Trypticase peptone",
    "field_path": "main_recipe[2]",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"attribute\": \"BD BBL\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.996016,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Trypticase peptone (BD BBL) table row",
        "exact_source_quote": "   Trypticase peptone (BD BBL)                                        1.00         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The repaired DSMZ owner retains the exact batch input with attached API/primary evidence. Its absent final concentration is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured final volume. The target copies a provider g_l value without this basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.996016",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "Source batch input: 1 g. Preserve the exact mass in notes; API g_l=0.996016 uses the provider's main-volume encoding and is not an independently verified final-medium concentration. Source material qualifier: BD BBL.",
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "arithmetic": "1 g = 1 g batch input. On the provider-declared 1.004 L basis, division gives 0.9960159362549800796812749004 g/L; source g_l=0.996016 retains its reported precision. Do not silently replace it by the unrounded quotient or recertify the denominator."
  },
  {
    "ingredient_or_context": "DSMZ main: K2HPO4",
    "field_path": "main_recipe[3]",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.29,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.288845,\n                        \"mmol_l\": 1.65835,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact K2HPO4 table row",
        "exact_source_quote": "   K2HPO4                                                             0.29         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The repaired DSMZ owner retains the exact batch input with attached API/primary evidence. Its absent final concentration is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured final volume. The target copies a provider g_l value without this basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.288845",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Source batch input: 0.29 g. Preserve the exact mass in notes; API g_l=0.288845 uses the provider's main-volume encoding and is not an independently verified final-medium concentration.",
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "arithmetic": "0.29 g = 0.29 g batch input. On the provider-declared 1.004 L basis, division gives 0.2888446215139442231075697211 g/L; source g_l=0.288845 retains its reported precision. Do not silently replace it by the unrounded quotient or recertify the denominator."
  },
  {
    "ingredient_or_context": "DSMZ main: KH2PO4",
    "field_path": "main_recipe[4]",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.29,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.288845,\n                        \"mmol_l\": 2.12253,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact KH2PO4 table row",
        "exact_source_quote": "   KH2PO4                                                             0.29         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The repaired DSMZ owner retains the exact batch input with attached API/primary evidence. Its absent final concentration is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured final volume. The target copies a provider g_l value without this basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.288845",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Source batch input: 0.29 g. Preserve the exact mass in notes; API g_l=0.288845 uses the provider's main-volume encoding and is not an independently verified final-medium concentration.",
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "arithmetic": "0.29 g = 0.29 g batch input. On the provider-declared 1.004 L basis, division gives 0.2888446215139442231075697211 g/L; source g_l=0.288845 retains its reported precision. Do not silently replace it by the unrounded quotient or recertify the denominator."
  },
  {
    "ingredient_or_context": "DSMZ main: (NH4)2SO4",
    "field_path": "main_recipe[5]",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.48,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.478088,\n                        \"mmol_l\": 3.61804,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact (NH4)2SO4 table row",
        "exact_source_quote": "   (NH4)2SO4                                                          0.48         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The repaired DSMZ owner retains the exact batch input with attached API/primary evidence. Its absent final concentration is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured final volume. The target copies a provider g_l value without this basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.478088",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "Source batch input: 0.48 g. Preserve the exact mass in notes; API g_l=0.478088 uses the provider's main-volume encoding and is not an independently verified final-medium concentration.",
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "arithmetic": "0.48 g = 0.48 g batch input. On the provider-declared 1.004 L basis, division gives 0.4780876494023904382470119522 g/L; source g_l=0.478088 retains its reported precision. Do not silently replace it by the unrounded quotient or recertify the denominator."
  },
  {
    "ingredient_or_context": "DSMZ main: NaCl",
    "field_path": "main_recipe[6]",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.48,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.478088,\n                        \"mmol_l\": 8.18083,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact NaCl table row",
        "exact_source_quote": "   NaCl                                                               0.48         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The repaired DSMZ owner retains the exact batch input with attached API/primary evidence. Its absent final concentration is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured final volume. The target copies a provider g_l value without this basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.478088",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "Source batch input: 0.48 g. Preserve the exact mass in notes; API g_l=0.478088 uses the provider's main-volume encoding and is not an independently verified final-medium concentration.",
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "arithmetic": "0.48 g = 0.48 g batch input. On the provider-declared 1.004 L basis, division gives 0.4780876494023904382470119522 g/L; source g_l=0.478088 retains its reported precision. Do not silently replace it by the unrounded quotient or recertify the denominator."
  },
  {
    "ingredient_or_context": "DSMZ main: MgSO4 x 7 H2O",
    "field_path": "main_recipe[7]",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0996016,\n                        \"mmol_l\": 0.404103,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact MgSO4 x 7 H2O table row",
        "exact_source_quote": "   MgSO4 x 7 H2O                                                      0.10         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The repaired DSMZ owner retains the exact batch input with attached API/primary evidence. Its absent final concentration is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured final volume. The target copies a provider g_l value without this basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.0996016",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "Source batch input: 0.1 g. Preserve the exact mass in notes; API g_l=0.0996016 uses the provider's main-volume encoding and is not an independently verified final-medium concentration.",
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "arithmetic": "0.1 g = 0.1 g batch input. On the provider-declared 1.004 L basis, division gives 0.09960159362549800796812749004 g/L; source g_l=0.0996016 retains its reported precision. Do not silently replace it by the unrounded quotient or recertify the denominator."
  },
  {
    "ingredient_or_context": "DSMZ main: CaCl2 x 2 H2O",
    "field_path": "main_recipe[8]",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 64,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.063745,\n                        \"mmol_l\": 0.433595,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact CaCl2 x 2 H2O table row",
        "exact_source_quote": "   CaCl2 x 2 H2O                                                    64.00        mg",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The repaired DSMZ owner retains the exact batch input with attached API/primary evidence. Its absent final concentration is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured final volume. The target copies a provider g_l value without this basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.063745",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[8].notes",
        "stored": "Source batch input: 64 mg. Preserve the exact mass in notes; API g_l=0.063745 uses the provider's main-volume encoding and is not an independently verified final-medium concentration.",
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "arithmetic": "64 mg = 0.064 g batch input. On the provider-declared 1.004 L basis, division gives 0.06374501992031872509960159363 g/L; source g_l=0.063745 retains its reported precision. Do not silently replace it by the unrounded quotient or recertify the denominator."
  },
  {
    "ingredient_or_context": "DSMZ main: Sodium resazurin",
    "field_path": "main_recipe[9]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498008,\n                        \"mmol_l\": 0.00198275,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Sodium resazurin (0.1% w/v) table row",
        "exact_source_quote": "   Sodium resazurin (0.1% w/v)                                        0.50        ml",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The DSMZ owner already preserves this receiving-medium stock dose with matching attached evidence. The target has no stock container. The amount is a stock addition, not a finished-medium mass concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "0.0005",
          "unit": "L"
        },
        "decision": "verified"
      },
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.000498008",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "0.5 mL ÷ 1000 = 0.0005 L added stock. 0.1% w/v = 0.001 g/mL stock; 0.50 mL supplies 0.0005 g sodium resazurin. Division by the provider nominal 1.004 L gives about 0.000498008 g/L, not an independently measured final concentration."
  },
  {
    "ingredient_or_context": "DSMZ main: Na2CO3",
    "field_path": "main_recipe[10]",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.98406,\n                        \"mmol_l\": 37.5898,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Na2CO3 table row",
        "exact_source_quote": "   Na2CO3                                                             4.00         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The repaired DSMZ owner retains the exact batch input with attached API/primary evidence. Its absent final concentration is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured final volume. The target copies a provider g_l value without this basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "3.98406",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[9].notes",
        "stored": "Source batch input: 4 g. Preserve the exact mass in notes; API g_l=3.98406 uses the provider's main-volume encoding and is not an independently verified final-medium concentration.",
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "arithmetic": "4 g = 4 g batch input. On the provider-declared 1.004 L basis, division gives 3.984063745019920318725099602 g/L; source g_l=3.98406 retains its reported precision. Do not silently replace it by the unrounded quotient or recertify the denominator."
  },
  {
    "ingredient_or_context": "DSMZ main: Volatile fatty acid mixture",
    "field_path": "main_recipe[11]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Volatile fatty acid mixture\",\n                        \"solution_id\": 608,\n                        \"amount\": 3.1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Volatile fatty acid mixture table row",
        "exact_source_quote": "   Volatile fatty acid mixture                                        3.10        ml",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The DSMZ owner already preserves this receiving-medium stock dose with matching attached evidence. The target has no stock container. The amount is a stock addition, not a finished-medium mass concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "0.0031",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "3.1 mL ÷ 1000 = 0.0031 L added stock. "
  },
  {
    "ingredient_or_context": "DSMZ main: L-Cysteine HCl x H2O",
    "field_path": "main_recipe[12]",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498008,\n                        \"mmol_l\": 2.83545,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact L-Cysteine HCl x H2O table row",
        "exact_source_quote": "   L-Cysteine HCl x H2O                                               0.50         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The repaired DSMZ owner retains the exact batch input with attached API/primary evidence. Its absent final concentration is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured final volume. The target copies a provider g_l value without this basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.498008",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[10].notes",
        "stored": "Source batch input: 0.5 g. Preserve the exact mass in notes; API g_l=0.498008 uses the provider's main-volume encoding and is not an independently verified final-medium concentration.",
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "arithmetic": "0.5 g = 0.5 g batch input. On the provider-declared 1.004 L basis, division gives 0.4980079681274900398406374502 g/L; source g_l=0.498008 retains its reported precision. Do not silently replace it by the unrounded quotient or recertify the denominator."
  },
  {
    "ingredient_or_context": "DSMZ main: Distilled water",
    "field_path": "main_recipe[13]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Distilled water table row",
        "exact_source_quote": "   Distilled water                                               1000.00          ml",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The DSMZ owner correctly preserves 1000 mL water as 1 L solvent input with attached evidence. The target omits it; this is not a final-volume denominator.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "1000 mL ÷ 1000 = 1 L water input; listed liquid additions 1000+0.50+3.10 = 1003.60 mL, distinct from provider 1004 mL and from an unmeasured final volume."
  },
  {
    "ingredient_or_context": "DSMZ fatty-acid stock: Acetic acid",
    "field_path": "solutions[1].composition[0].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Acetic acid\",\n                        \"compound_id\": 380,\n                        \"amount\": 548.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 573.182,\n                        \"mmol_l\": 9545.09,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Acetic acid table row",
        "exact_source_quote": "   Acetic acid                                                     548.50         ml",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The DSMZ owner already records the exact stock liquid volume in L with matching API and primary evidence. The target promotes a stock quantity to finished-medium g/L. The target value equals the provider stock g_l, whose density basis is not established by the primary; it is not the diluted receiving-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "573.182",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "0.5485",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "548.5 mL ÷ 1000 = 0.5485 L stock input. The separate stock dose is 3.10 mL. No liquid-density mass conversion or final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "DSMZ fatty-acid stock: Propionic acid",
    "field_path": "solutions[1].composition[1].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Propionic acid\",\n                        \"compound_id\": 381,\n                        \"amount\": 193.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 192.145,\n                        \"mmol_l\": 2593.76,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Propionic acid table row",
        "exact_source_quote": "   Propionic acid                                                  193.50         ml",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The DSMZ owner already records the exact stock liquid volume in L with matching API and primary evidence. The target promotes a stock quantity to finished-medium g/L. The target value equals the provider stock g_l, whose density basis is not established by the primary; it is not the diluted receiving-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "192.145",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "solutions[1].composition[1].concentration",
        "stored": {
          "value": "0.1935",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "193.5 mL ÷ 1000 = 0.1935 L stock input. The separate stock dose is 3.10 mL. No liquid-density mass conversion or final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "DSMZ fatty-acid stock: Butyric acid",
    "field_path": "solutions[1].composition[2].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Butyric acid\",\n                        \"compound_id\": 314,\n                        \"amount\": 129,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Butyric acid table row",
        "exact_source_quote": "   Butyric acid                                                    129.00         ml",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The DSMZ owner already records the exact stock liquid volume in L with matching API and primary evidence. The target promotes a stock quantity to finished-medium g/L. Specifically, 129 mL butyric acid is represented as 129 g/L although this API row supplies no g_l; no density justifies that unit change.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "129",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "solutions[1].composition[2].concentration",
        "stored": {
          "value": "0.129",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "129 mL ÷ 1000 = 0.129 L stock input. The separate stock dose is 3.10 mL. No liquid-density mass conversion or final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "DSMZ fatty-acid stock: n-Valeric acid",
    "field_path": "solutions[1].composition[3].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"n-Valeric acid\",\n                        \"compound_id\": 288,\n                        \"amount\": 32.25,\n                        \"unit\": \"ml\",\n                        \"g_l\": 30.2827,\n                        \"mmol_l\": 296.512,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact n-Valeric acid table row",
        "exact_source_quote": "   n-Valeric acid                                                   32.25         ml",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The DSMZ owner already records the exact stock liquid volume in L with matching API and primary evidence. The target promotes a stock quantity to finished-medium g/L. The target value equals the provider stock g_l, whose density basis is not established by the primary; it is not the diluted receiving-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "30.2827",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "solutions[1].composition[3].concentration",
        "stored": {
          "value": "0.03225",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "32.25 mL ÷ 1000 = 0.03225 L stock input. The separate stock dose is 3.10 mL. No liquid-density mass conversion or final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "DSMZ fatty-acid stock: iso-Butyric acid",
    "field_path": "solutions[1].composition[4].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"iso-Butyric acid\",\n                        \"compound_id\": 377,\n                        \"amount\": 32.25,\n                        \"unit\": \"ml\",\n                        \"g_l\": 30.6375,\n                        \"mmol_l\": 347.719,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact iso-Butyric acid table row",
        "exact_source_quote": "   iso-Butyric acid                                                 32.25         ml",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The DSMZ owner already records the exact stock liquid volume in L with matching API and primary evidence. The target promotes a stock quantity to finished-medium g/L. The target value equals the provider stock g_l, whose density basis is not established by the primary; it is not the diluted receiving-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "30.6375",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "solutions[1].composition[4].concentration",
        "stored": {
          "value": "0.03225",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "32.25 mL ÷ 1000 = 0.03225 L stock input. The separate stock dose is 3.10 mL. No liquid-density mass conversion or final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "DSMZ fatty-acid stock: DL-2-Methylbutyric acid",
    "field_path": "solutions[1].composition[5].concentration",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"DL-2-Methylbutyric acid\",\n                        \"compound_id\": 223,\n                        \"amount\": 32.25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact DL-2-Methylbutyric acid table row",
        "exact_source_quote": "   DL-2-Methylbutyric acid                                          32.25         ml",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The source and repaired owner contain DL-2-methylbutyric acid 32.25 mL in the stock. It is absent from the target; no mass or final concentration is supplied by this API row.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "solutions[1].composition[5].concentration",
        "stored": {
          "value": "0.03225",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "32.25 mL ÷ 1000 = 0.03225 L stock input. The separate stock dose is 3.10 mL. No liquid-density mass conversion or final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "DSMZ fatty-acid stock: iso-Valeric acid",
    "field_path": "solutions[1].composition[6].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"iso-Valeric acid\",\n                        \"compound_id\": 378,\n                        \"amount\": 32.25,\n                        \"unit\": \"ml\",\n                        \"g_l\": 30.0247,\n                        \"mmol_l\": 293.986,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact iso-Valeric acid table row",
        "exact_source_quote": "   iso-Valeric acid                                                 32.25         ml",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The DSMZ owner already records the exact stock liquid volume in L with matching API and primary evidence. The target promotes a stock quantity to finished-medium g/L. The target value equals the provider stock g_l, whose density basis is not established by the primary; it is not the diluted receiving-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "30.0247",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "solutions[1].composition[6].concentration",
        "stored": {
          "value": "0.03225",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "32.25 mL ÷ 1000 = 0.03225 L stock input. The separate stock dose is 3.10 mL. No liquid-density mass conversion or final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "Sodium-resazurin stock strength",
    "field_path": "solutions[0].composition[0].concentration",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498008,\n                        \"mmol_l\": 0.00198275,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Sodium resazurin (0.1% w/v) table row",
        "exact_source_quote": "   Sodium resazurin (0.1% w/v)                                        0.50        ml",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The source explicitly gives 0.1% w/v stock strength separately from 0.50 mL dose. The DSMZ owner correctly retains this with attached evidence; the target lacks the stock.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "0.1",
          "unit": "PERCENT_W_V"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "0.1 g per 100 mL stock; not 0.1% in the receiving medium. The chemical identifier is assessed separately from the amount."
  },
  {
    "ingredient_or_context": "KOMODO reported medium: Na2CO3",
    "field_path": "ingredients[0].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row1; extracted HTML text",
        "exact_source_quote": "Na2CO3 Sodium carbonate SEED-cpd00242#cpd00971## 3.99 0.04",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific Gram Amount rate and displayed precision with attached evidence. This verifies the reported provider quantity only; linked DSMZ batch masses do not establish its normalization or make the two formulations exact duplicates.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "3.99",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: iso-Valeric acid",
    "field_path": "ingredients[1].concentration",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row2; extracted HTML text",
        "exact_source_quote": "iso-Valeric acid iso-Valeric acid SEED-cpd05178### null null",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific null amount with attached evidence; missing is not zero. Do not infer an acid dose, gas quantity, water volume or final concentration from the separate SEED aggregate table.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: DL-histidine",
    "field_path": "ingredients[2].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row3; extracted HTML text",
        "exact_source_quote": "DL-histidine DL-histidine SEED-cpd00572### 7.78 0.05",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific Gram Amount rate and displayed precision with attached evidence. This verifies the reported provider quantity only; linked DSMZ batch masses do not establish its normalization or make the two formulations exact duplicates.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "7.78",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: Cysteine-HCl x H2O",
    "field_path": "ingredients[3].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row4; extracted HTML text",
        "exact_source_quote": "Cysteine-HCl x H2O Cysteine-HCl SEED-cpd00084#cpd00099## 0.50 0.00",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific Gram Amount rate and displayed precision with attached evidence. This verifies the reported provider quantity only; linked DSMZ batch masses do not establish its normalization or make the two formulations exact duplicates.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.50",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: Propionic acid",
    "field_path": "ingredients[4].concentration",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row5; extracted HTML text",
        "exact_source_quote": "Propionic acid Propionic acid SEED-cpd00141### null null",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific null amount with attached evidence; missing is not zero. Do not infer an acid dose, gas quantity, water volume or final concentration from the separate SEED aggregate table.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: CO2",
    "field_path": "ingredients[5].concentration",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row6; extracted HTML text",
        "exact_source_quote": "CO2 CO2 SEED-cpd00011### null null",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific null amount with attached evidence; missing is not zero. Do not infer an acid dose, gas quantity, water volume or final concentration from the separate SEED aggregate table.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: Distilled water",
    "field_path": "ingredients[6].concentration",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row7; extracted HTML text",
        "exact_source_quote": "Distilled water H2O SEED-cpd00001### null null",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific null amount with attached evidence; missing is not zero. Do not infer an acid dose, gas quantity, water volume or final concentration from the separate SEED aggregate table.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: DL-2-Methyl butyric acid",
    "field_path": "ingredients[7].concentration",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row8; extracted HTML text",
        "exact_source_quote": "DL-2-Methyl butyric acid DL-2-Methylbutyric acid 2-Methylbutyric acid# null null",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific null amount with attached evidence; missing is not zero. Do not infer an acid dose, gas quantity, water volume or final concentration from the separate SEED aggregate table.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: K2HPO4",
    "field_path": "ingredients[8].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row9; extracted HTML text",
        "exact_source_quote": "K2HPO4 di Potassium hydrogen phosphate SEED-cpd00009#cpd00205## 0.29 0.00",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific Gram Amount rate and displayed precision with attached evidence. This verifies the reported provider quantity only; linked DSMZ batch masses do not establish its normalization or make the two formulations exact duplicates.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.29",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: KH2PO4",
    "field_path": "ingredients[9].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row10; extracted HTML text",
        "exact_source_quote": "KH2PO4 Potassium dihydrogen phosphate SEED-cpd00009#cpd00205## 0.29 0.00",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific Gram Amount rate and displayed precision with attached evidence. This verifies the reported provider quantity only; linked DSMZ batch masses do not establish its normalization or make the two formulations exact duplicates.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.29",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: iso-Butyric acid",
    "field_path": "ingredients[10].concentration",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row11; extracted HTML text",
        "exact_source_quote": "iso-Butyric acid iso-Butyric acid SEED-cpd01711### null null",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific null amount with attached evidence; missing is not zero. Do not infer an acid dose, gas quantity, water volume or final concentration from the separate SEED aggregate table.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: n-Valeric acid",
    "field_path": "ingredients[11].concentration",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row12; extracted HTML text",
        "exact_source_quote": "n-Valeric acid n-Valeric acid SEED-cpd00597### null null",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific null amount with attached evidence; missing is not zero. Do not infer an acid dose, gas quantity, water volume or final concentration from the separate SEED aggregate table.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: MgSO4 x 7 H2O",
    "field_path": "ingredients[12].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row13; extracted HTML text",
        "exact_source_quote": "MgSO4 x 7 H2O Magnesium sulfate SEED-cpd00048#cpd00254## 0.10 0.00",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific Gram Amount rate and displayed precision with attached evidence. This verifies the reported provider quantity only; linked DSMZ batch masses do not establish its normalization or make the two formulations exact duplicates.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.10",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: Butyric acid",
    "field_path": "ingredients[13].concentration",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row14; extracted HTML text",
        "exact_source_quote": "Butyric acid Butyric acid SEED-cpd00211### null null",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific null amount with attached evidence; missing is not zero. Do not infer an acid dose, gas quantity, water volume or final concentration from the separate SEED aggregate table.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: CaCl2 x 2 H2O",
    "field_path": "ingredients[14].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row15; extracted HTML text",
        "exact_source_quote": "CaCl2 x 2 H2O Calcium chloride SEED-cpd00063#cpd00099## 0.06 0.00",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific Gram Amount rate and displayed precision with attached evidence. This verifies the reported provider quantity only; linked DSMZ batch masses do not establish its normalization or make the two formulations exact duplicates.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.06",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: Yeast extract",
    "field_path": "ingredients[15].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row16; extracted HTML text",
        "exact_source_quote": "Yeast extract Yeast extract rich-peptone# 3.99 null",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific Gram Amount rate and displayed precision with attached evidence. This verifies the reported provider quantity only; linked DSMZ batch masses do not establish its normalization or make the two formulations exact duplicates.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "3.99",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: Trypticase",
    "field_path": "ingredients[16].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row17; extracted HTML text",
        "exact_source_quote": "Trypticase Trypticase rich-peptone# 1.00 null",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific Gram Amount rate and displayed precision with attached evidence. This verifies the reported provider quantity only; linked DSMZ batch masses do not establish its normalization or make the two formulations exact duplicates.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "1.00",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: Resazurin",
    "field_path": "ingredients[17].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row18; extracted HTML text",
        "exact_source_quote": "Resazurin Resazurin SEED-cpd08053### 9.97E-4 4.35E-6",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific Gram Amount rate and displayed precision with attached evidence. This verifies the reported provider quantity only; linked DSMZ batch masses do not establish its normalization or make the two formulations exact duplicates.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "9.97E-4",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: NaCl",
    "field_path": "ingredients[18].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row19; extracted HTML text",
        "exact_source_quote": "NaCl NaCl SEED-cpd00099#cpd00971## 0.48 0.01",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific Gram Amount rate and displayed precision with attached evidence. This verifies the reported provider quantity only; linked DSMZ batch masses do not establish its normalization or make the two formulations exact duplicates.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.48",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: Acetic acid",
    "field_path": "ingredients[19].concentration",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row20; extracted HTML text",
        "exact_source_quote": "Acetic acid Acetic acid SEED-cpd00029### null null",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific null amount with attached evidence; missing is not zero. Do not infer an acid dose, gas quantity, water volume or final concentration from the separate SEED aggregate table.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "KOMODO reported medium: (NH4)2SO4",
    "field_path": "ingredients[20].concentration",
    "decision": "verified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound recipe table row21; extracted HTML text",
        "exact_source_quote": "(NH4)2SO4 Ammonium sulfate SEED-cpd00013#cpd00048## 0.48 0.00",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Compound table basis; extracted HTML text",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "The maintained KOMODO owner matches its source-specific Gram Amount rate and displayed precision with attached evidence. This verifies the reported provider quantity only; linked DSMZ batch masses do not establish its normalization or make the two formulations exact duplicates.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.48",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Unsupported target LB expansion: Tryptone",
    "field_path": "ingredients[17].concentration",
    "decision": "unsupported",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"attribute\": \"BD BBL\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.996016,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Trypticase peptone (BD BBL) table row",
        "exact_source_quote": "   Trypticase peptone (BD BBL)                                        1.00         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "This supplier-tagged LB expansion is additional to the genuine source ingredient. Neither complete exact recipe contains LB Miller. Both maintained owners already removed these three false rows and retained their history; reconcile the generated target rather than adding these masses to genuine ingredients.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "Unsupported target LB expansion: Yeast extract",
    "field_path": "ingredients[18].concentration",
    "decision": "unsupported",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.98406,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Yeast extract table row",
        "exact_source_quote": "   Yeast extract                                                      4.00         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "This supplier-tagged LB expansion is additional to the genuine source ingredient. Neither complete exact recipe contains LB Miller. Both maintained owners already removed these three false rows and retained their history; reconcile the generated target rather than adding these masses to genuine ingredients.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "Unsupported target LB expansion: Sodium chloride",
    "field_path": "ingredients[19].concentration",
    "decision": "unsupported",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.48,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.478088,\n                        \"mmol_l\": 8.18083,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact NaCl table row",
        "exact_source_quote": "   NaCl                                                               0.48         g",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "This supplier-tagged LB expansion is additional to the genuine source ingredient. Neither complete exact recipe contains LB Miller. Both maintained owners already removed these three false rows and retained their history; reconcile the generated target rather than adding these masses to genuine ingredients.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ preparation: Cooling atmosphere",
    "field_path": "preparation_steps[0].description",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "100% CO2 gas atmosphere",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      }
    ],
    "rationale": "The DSMZ owner already preserves this exact preparation condition with attached root-level evidence. Add its source-attributed context to any regenerated DSMZ representation; do not reinterpret a gas percentage as a fixed gas ingredient dose or overwrite KOMODO aerobic metadata without preserving the conflict. The KOMODO owner’s attached 100% CO2 note, where listed, is verified only as attributed linked-DSMZ context, not an asserted aerobic/anaerobic biological resolution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, fatty acid mixture and cysteine), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add solid carbonate, fatty acid mixture and cysteine and adjust pH to 6.0. Dispense medium under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Adjust pH of complete medium to 6.0, if necessary.",
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "notes",
        "stored": "Source: KOMODO ModelSEED &#124; ID: 1006 &#124; DSMZ Medium: 1006 (mediadive.medium:1006) &#124; Aerobic: Yes\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product: LB Medium (Luria-Bertani, Miller formulation)\nSupplier: Multiple suppliers (Difco, Sigma, etc.)\nCatalog: Multiple (L3522 Sigma, 244520 BD)\nSource: https://www.laboratorynotes.com/preparation-of-luria-bertani-lb-miller-broth/\nAccessed: 2026-03-28\n\nConstituent composition researched from product specification.\n\nKOMODO reports Is Aerobic: true, while its linked DSMZ original uses 100% CO2 and anoxic vessels. Preserve this source conflict, not a resolved oxygen requirement or quantitative gas addition.\n\nThe linked original specifies anoxic preparation; it does not establish a quantitative CO2 ingredient amount or justify replacing this provider's source-specific rates.\n\nArchive the complete prior ingredient nodes, including the copied L-cysteine and sodium-resazurin annotations, in append-only history. Their source-specific replacements do not inherit unverified chemical forms.\n\nSource-specific ingredient identities and quantity scopes supersede copied flattened amounts. Unknown gas amounts, densities and final volumes remain unknown. Other existing chemical annotations and all prior history are preserved, not recertified. No taxa-media association is added.",
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ preparation: Dispensing atmosphere",
    "field_path": "preparation_steps[0].description",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Dispense medium under 100% CO2 gas atmosphere",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      }
    ],
    "rationale": "The DSMZ owner already preserves this exact preparation condition with attached root-level evidence. Add its source-attributed context to any regenerated DSMZ representation; do not reinterpret a gas percentage as a fixed gas ingredient dose or overwrite KOMODO aerobic metadata without preserving the conflict. The KOMODO owner’s attached 100% CO2 note, where listed, is verified only as attributed linked-DSMZ context, not an asserted aerobic/anaerobic biological resolution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, fatty acid mixture and cysteine), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add solid carbonate, fatty acid mixture and cysteine and adjust pH to 6.0. Dispense medium under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Adjust pH of complete medium to 6.0, if necessary.",
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ preparation: Initial pH",
    "field_path": "preparation_steps[0].description",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "adjust pH to 6.0",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      }
    ],
    "rationale": "The DSMZ owner already preserves this exact preparation condition with attached root-level evidence. Add its source-attributed context to any regenerated DSMZ representation; do not reinterpret a gas percentage as a fixed gas ingredient dose or overwrite KOMODO aerobic metadata without preserving the conflict. The KOMODO owner’s attached 100% CO2 note, where listed, is verified only as attributed linked-DSMZ context, not an asserted aerobic/anaerobic biological resolution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, fatty acid mixture and cysteine), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add solid carbonate, fatty acid mixture and cysteine and adjust pH to 6.0. Dispense medium under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Adjust pH of complete medium to 6.0, if necessary.",
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ preparation: Completed-medium pH",
    "field_path": "preparation_steps[0].description",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Adjust pH of complete medium to 6.0, if necessary.",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      }
    ],
    "rationale": "The DSMZ owner already preserves this exact preparation condition with attached root-level evidence. Add its source-attributed context to any regenerated DSMZ representation; do not reinterpret a gas percentage as a fixed gas ingredient dose or overwrite KOMODO aerobic metadata without preserving the conflict. The KOMODO owner’s attached 100% CO2 note, where listed, is verified only as attributed linked-DSMZ context, not an asserted aerobic/anaerobic biological resolution.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, fatty acid mixture and cysteine), bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere. Add solid carbonate, fatty acid mixture and cysteine and adjust pH to 6.0. Dispense medium under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Adjust pH of complete medium to 6.0, if necessary.",
        "decision": "verified"
      }
    ]
  },
  {
    "ingredient_or_context": "Recorded pH 6.0",
    "field_path": "ph_value",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "adjust pH to 6.0",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "komodo1006Archived",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
        "source_locator": "Medium features; extracted HTML text",
        "exact_source_quote": "PH Info: 6.0",
        "snapshot_sha256": "a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7",
        "parsed_text_sha256": "58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2"
      }
    ],
    "rationale": "All three scalar pH values agree with their source. Existing attached preparation evidence is assessed at its actual preparation/notes scope; this scalar ledger does not claim a new field-specific attachment.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 6.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
        "field_path": "ph_value",
        "stored": 6.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "ph_value",
        "stored": 6.0,
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Unknown final-volume and conversion basis",
    "field_path": "notes",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1006api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1006",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1004",
        "snapshot_sha256": "e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f"
      },
      {
        "source_key": "dsmz1006",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
        "source_locator": "Page1 exact Distilled water table row",
        "exact_source_quote": "   Distilled water                                               1000.00          ml",
        "snapshot_sha256": "8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283",
        "parsed_text_sha256": "49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31"
      }
    ],
    "rationale": "The provider declares 1004 mL; the primary prints 1000 mL water plus stock additions without measured final-volume makeup. The DSMZ owner explicitly preserves that limit; target notes omit it. Acid densities are not given. No measured final concentration or unknown titrant dose is filled.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "notes",
        "stored": "Source: KOMODO ModelSEED &#124; ID: 1006 &#124; DSMZ Medium: 1006 (mediadive.medium:1006) &#124; Aerobic: Yes\n\nCommercial Product: LB Medium (Luria-Bertani, Miller formulation)\nSupplier: Multiple suppliers (Difco, Sigma, etc.)\nCatalog: Multiple (L3522 Sigma, 244520 BD)\nSource: https://www.laboratorynotes.com/preparation-of-luria-bertani-lb-miller-broth/\nAccessed: 2026-03-28\n\nConstituent composition researched from product specification.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
        "field_path": "notes",
        "stored": "Source: DSMZ &#124; Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product: LB Medium (Luria-Bertani, Miller formulation)\nSupplier: Multiple suppliers (Difco, Sigma, etc.)\nCatalog: Multiple (L3522 Sigma, 244520 BD)\nSource: https://www.laboratorynotes.com/preparation-of-luria-bertani-lb-miller-broth/\nAccessed: 2026-03-28\n\nConstituent composition researched from product specification.\n\nThe original recipe adds carbonate, fatty-acid stock and cysteine after cooling under CO2, then dispenses and autoclaves. The API main volume of 1004 ml is a provider encoding, not evidence of measured final volume or verified density conversions.\n\nSource-specific ingredient identities and quantity scopes supersede copied flattened amounts. Unknown gas amounts, densities and final volumes remain unknown. Other existing chemical annotations and all prior history are preserved, not recertified. No taxa-media association is added.",
        "decision": "verified"
      }
    ],
    "arithmetic": "Seven stock liquid inputs sum 1000.00 mL, which is an input sum rather than an independently measured mixed-stock volume. Main listed liquids sum 1003.60 mL; no physical-volume equality or corrected final denominator is asserted."
  }
]

### Stale merged product versus distinct repaired source owners

identity: concern. Targets: CultureMech:003506.

Both named contributors resolve to the inspected files and permanent IDs. Their October 9 repairs postdate the target’s August 6 merge. KOMODO now has 21 source-specific compound rows including 9 nulls and 12 rates; DSMZ has 12 direct inputs and two stocks. Reciprocal DERIVED_FROM links replace prior SOURCE_DUPLICATE. The target still presents the earlier copied formulation and duplicate relationship. Its existing path is identified, but it is not a scientifically faithful current representative of either owner.

### Batch masses, stock liquid volumes and provider rates

consistency: concern. Targets: CultureMech:003506.

The exhaustive ledger separates 14 DSMZ main rows, seven fatty-acid inputs, resazurin strength, 21 KOMODO compound rows, three unsupported LB amounts and numeric preparation/basis contexts. Target main g/L values reproduce API nominal 1004 mL conversions but omit that scope; acid values are stock-level or an unsupported mL-to-g/L substitution. The repaired DSMZ owner already retains source batch masses in notes, water and dose volumes in L, and stock volumes without inventing final concentrations. Numerical agreement with one provider field does not validate the target recipe.

### Source-specific salt, hydrate, stereochemistry and product claims

grounding: concern. Targets: CultureMech:003506.

Primary DL-histidine is compatible with the nonspecific histidine term; magnesium sulfate heptahydrate, calcium chloride dihydrate, the two potassium phosphate salts, ammonium sulfate, sodium carbonate, L-cysteine hydrochloride monohydrate and named acid identities agree with their supplied forms. The DSMZ Trypticase BD BBL qualifier is retained in owner notes. CHEBI:8806 is neutral Resazurin, formula C12H7NO4 without sodium; it does not encode the explicit sodium resazurin stock. KOMODO’s nonspecific cysteine and resazurin names appropriately no longer inherit L/sodium annotations. MICRO:0000182 and FOODON:03315426 labels resolve, but do not authenticate the unsupported LB expansion. No replacement chemical ID or missing density is guessed.

### Anoxic source sequence, gas conditions and pH

completeness: concern. Targets: CultureMech:003506.

Target preparation is absent. DSMZ specifies boiling the base, cooling under 100% CO2, adding carbonate/fatty-acid stock/cysteine, adjusting pH 6, dispensing under 100% CO2 into anoxic vessels, then autoclaving and readjusting completed-medium pH 6 if necessary. Its owner already retains the full sequence with evidence; no temperature/duration is printed. KOMODO aerobic:true is conflicting catalog metadata and its repaired owner explicitly preserves that conflict. No gas mass, titrant amount or generic sterilization cycle is invented.

### Complex liquid formulation and bounded biology

scope: supported. Targets: CultureMech:003506.

COMPLEX/UNDEFINED and LIQUID agree with yeast extract/Trypticase and absence of agar in the exact formula. pH 6 is source-backed; aerobic catalog metadata is not an experimentally resolved oxygen requirement. The name ALLISONELLA and generic microbial-cultivation application are not strain-specific growth evidence. No organism/taxon, DOI/PMID, assembly, measured growth or temperature claim is added.

### Retained isovaleric-acid legacy MIM link

grounding: concern. Targets: CultureMech:003506.

The target and both source owners retain MediaIngredientMech:000378 in different quantity scopes. The exact current pinned catalog/tree lookup completed without that identifier; CHEBI-based secondary mappings resolve separately. Historical correspondence remains unresolved, and the numerically similar MediaDive compound 378 is not proof of equivalence.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003506.

27 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Existing repair, commercial-expansion history and current generators

provenance: concern. Targets: CultureMech:003506.

The inspected repair_allisonella_acids.py and preserved October 9 changes explain why current owners removed the false supplier-tagged LB rows, restored DL-2-methylbutyric acid, separated DSMZ stocks and changed reciprocal relationships. Those repairs already exist and must be retained. Current formulation merging requires compatible scientific content and unions scoped evidence; it does not justify collapsing these distinct owner recipes. Current importer stock handling is context, not a replay or evidence that historical artifacts are correct. The old laboratorynotes URL documents expansion provenance only; its failed request provides no formulation evidence.

## Findings

### f1: Stale merged recipe retains false LB additions and flattened acid stocks

blocker / open / confirmed; issue key: culturemech.003506.stale-flattened-formula.

The generated record retains extra 10 g/L tryptone, 5 g/L yeast and 10 g/L NaCl from an unsupported LB-Miller expansion, omits DL-2-methylbutyric acid, and lists stock acid values as final-medium g/L, including 129 mL butyric acid represented as 129 g/L. These errors make the named formula unusable as a faithful recipe. Both maintained owners already repaired these defects and preserve different source-specific rates/nulls versus batch/stock quantities.

### f2: Generated duplicate relationship contradicts repaired source distinction

major / open / confirmed; issue key: culturemech.003506.stale-source-equivalence.

The target still asserts SOURCE_DUPLICATE and copied-equality notes even though current maintained owners carry reciprocal DERIVED_FROM relationships and different source-specific amounts, nulls and forms. Exact linked source identity supports derivation, not formula equivalence.

### f3: Sodium resazurin is grounded to the neutral compound

major / open / confirmed; issue key: culturemech.003506.sodium-resazurin-form.

Target ingredients[9] and the repaired DSMZ owner’s solutions[0].composition[0] name sodium resazurin but carry CHEBI:8806, whose formula C12H7NO4 contains no sodium. Correct stock quantities and canonical label checks do not resolve supplied-salt identity.

### f4: Generated record omits the source anoxic preparation and oxygen caveat

major / open / confirmed; issue key: culturemech.003506.preparation-source-conflict.

The target drops the DSMZ owner’s evidence-backed boiling/cooling/addition sequence, two 100% CO2 atmosphere stages, anoxic dispensing/autoclaving and final pH check while leaving Aerobic:Yes catalog text without the repaired owner’s explicit conflict explanation. Reproduction and interpretation require these source-specific conditions.

### f5: Legacy isovaleric-acid MIM identifier remains unresolved

minor / open / confirmed; issue key: culturemech.003506.legacy-link.

MediaIngredientMech:000378 persists in target and both owner layers, while the complete current pinned catalog/tree lacks that legacy key. Current CHEBI-key correspondence does not establish its historical identity.

### f6: Inherited import/copy timestamps lack reliable UTC interpretation

minor / open / confirmed; issue key: culturemech.003506.history-timing.

Target and KOMODO owner retain invalid .fZ import timestamps and timezone-naive copy timestamps: four problematic current history instances. Later repair timestamps do not retrospectively authenticate the old access times; the primary historical 49cf hash is layout text, not PDF bytes.

## Recommended Actions And Acceptance Checks

### a1

Reconcile and regenerate from the already repaired owners, preserving separate source formulations and their evidence. Remove the stale unsupported LB expansion and retain the full acid stock/dose hierarchy and unknown final-volume basis; do not repeat the completed owner repair, sum duplicate nutrients, or copy provider stock g/L as final concentrations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the current owner DERIVED_FROM evidence and source identities in reconciliation/regeneration. Do not merge them solely by names, historical ingredient fingerprint or copied pre-repair concentration signatures.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve the explicit sodium-salt grounding in the DSMZ owner with a verified appropriate term before regeneration, preserving 0.1% w/v stock strength and 0.50 mL dose. Keep KOMODO’s separately unqualified resazurin assertion distinct; no replacement identifier is proposed here.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Restore the appropriate source-specific preparation and explicit catalog-versus-primary oxygen caveat during reconciliation. Retain existing owner evidence; do not invent a temperature, duration, gas quantity or resolve the biological oxygen requirement without evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Resolve the legacy link through explicit historical provenance or retain an unresolved annotation; do not infer correspondence from MediaDive numeric 378 or silently rewrite history.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Preserve old events and explicitly distinguish source versions, hash formats and unverified times in any append-only clarification. Do not invent historical UTC values or describe the 49cf extraction hash as the raw PDF hash.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/allisonella_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch024/233/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-024/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch024/233/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml:1:id: CultureMech:003506<br>./data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml:1:id: CultureMech:003506<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch024/source-preflight-bound/233/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 29 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch024/source-preflight-bound/233/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| dsmz1006 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf; Complete one-page primary, both tables and preparation; page image independently inspected | supports | Source versions and stages remain separate. Primary batch masses, stock liquid inputs and provider-reported rates are not interchangeable. Archived KOMODO is a preserved public response, not a successful present retrieval. |
| mediadive1006api | https://mediadive.dsmz.de/rest/medium/1006; Complete main solution 2052 and referenced stock 608, all 14+7 rows and preparation | supports | Source versions and stages remain separate. Primary batch masses, stock liquid inputs and provider-reported rates are not interchangeable. Archived KOMODO is a preserved public response, not a successful present retrieval. |
| solution608 | https://mediadive.dsmz.de/rest/solution/608; Complete exact seven-row stock endpoint; identity and amount/unit correspondence | supports | Source versions and stages remain separate. Primary batch masses, stock liquid inputs and provider-reported rates are not interchangeable. Archived KOMODO is a preserved public response, not a successful present retrieval. |
| komodo1006Archived | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006; Complete archived public HTML, 21-row compound table, features and separate SEED table | supports | Source versions and stages remain separate. Primary batch masses, stock liquid inputs and provider-reported rates are not interchangeable. Archived KOMODO is a preserved public response, not a successful present retrieval. |
| komodoMediaList-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaList; Preserved exact public retrieval result | context_only | Preserved komodoMediaList retrieval failed (403). No content is claimed from this attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006 formulation provide the required source comparison; the LB page cannot establish membership in this recipe. |
| komodo1006-attempt | https://komodo.modelseed.org/servlet/Komodo?medium=1006; Preserved exact public retrieval result | context_only | Preserved komodo1006 retrieval failed (403). No content is claimed from this attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006 formulation provide the required source comparison; the LB page cannot establish membership in this recipe. |
| komodoDetail1006-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006; Preserved exact public retrieval result | context_only | Preserved komodoDetail1006 retrieval failed (403). No content is claimed from this attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006 formulation provide the required source comparison; the LB page cannot establish membership in this recipe. |
| lbMillerNotes-attempt | https://www.laboratorynotes.com/preparation-of-luria-bertani-lb-miller-broth/; Preserved exact public retrieval result | context_only | Preserved lbMillerNotes retrieval failed (None). No content is claimed from this attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006 formulation provide the required source comparison; the LB page cannot establish membership in this recipe. |
| komodo1006-catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact byte-literal HTML table row for MediaInfo=1006 | supports | Source catalog identity, DSMZ cross-reference and encoded metadata only. This does not authenticate the historical copied formulation or establish growth/atmosphere. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15366 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15366; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15366 resolves to acetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16135 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16135; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16135 resolves to isobutyric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17418 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17418; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17418 resolves to valeric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27570 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27570; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27570 resolves to histidine. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi28484 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28484; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:28484 resolves to isovaleric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30768 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30768; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30768 resolves to propionic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30772 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30772; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30772 resolves to butyric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | FOODON:03315426 resolves to yeast extract. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| micro0000182 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | MICRO:0000182 resolves to tryptone. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15366": [{"label": "Acetic acid", "match_type": "preferred_term", "identifier": "CHEBI:15366", "preferred_term": "Acetic acid", "ontology_id": "CHEBI:15366", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16135": [{"label": "Isobutyric acid", "match_type": "preferred_term", "identifier": "CHEBI:16135", "preferred_term": "Isobutyric acid", "ontology_id": "CHEBI:16135", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17418": [{"label": "Valeric acid", "match_type": "preferred_term", "identifier": "CHEBI:17418", "preferred_term": "Valeric acid", "ontology_id": "CHEBI:17418", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27570": [{"label": "DL-Histidine", "match_type": "preferred_term", "identifier": "CHEBI:27570", "preferred_term": "DL-Histidine", "ontology_id": "CHEBI:27570", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30768": [{"label": "Propionic acid", "match_type": "preferred_term", "identifier": "CHEBI:30768", "preferred_term": "Propionic acid", "ontology_id": "CHEBI:30768", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30772": [{"label": "Butyric acid", "match_type": "preferred_term", "identifier": "CHEBI:30772", "preferred_term": "Butyric acid", "ontology_id": "CHEBI:30772", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| attached-evidence | /private/tmp/culturemech-review-work-batch024/233/existing-evidence-recheck.json; All 67 current owner evidence objects, snippets/explanations and source hashes | supports | Current attached evidence is retained per source and per field. KOMODO snippets are extracted HTML text; primary snippets use layout text. The archived raw response and current PDF raw hash remain separately identified. |
| historical-reading | /private/tmp/culturemech-review-work-batch023/233-owner-lossless-reading/manifest.json; Lossless partition of both complete owner YAMLs into current fields/evidence/history, with exact reconstruction hashes | context_only | Specialist preflight reading covered the complete archived nodes and repeated explanations through lossless deduplicated views. The independent cache audit verified 67 evidence objects, 127 additional excerpts and 194 timestamp instances across its scoped cache. This review reread current fields, distinct claims, source tables and current evidence; root history reading is not claimed. |
| independent-cache-audit | /private/tmp/culturemech-review-work-batch023/batch024-firstfive-independent-audit.json; Independent frozen first-five cache audit; exact current owner evidence and raw catalog slices | context_only | Independent audit supports source integrity and historical excerpt correspondence. Parsed catalog literal_html was serialized HTML, so this review quotes the separately extracted raw row instead. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch024/233/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch024/233/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Complete pinned public catalog/tree at 6643131b0f12ab40b66f98135245fca04027e0e9; exact token and numeric filename scope | supports | The bounded current lookup found no legacy 000378 identifier or corresponding numeric filename. This is not a search of all historical revisions and does not establish a replacement ID. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Complete pinned public catalog/tree at 6643131b0f12ab40b66f98135245fca04027e0e9; exact token and numeric filename scope | supports | The bounded current lookup found no legacy 000378 identifier or corresponding numeric filename. This is not a search of all historical revisions and does not establish a replacement ID. |
| legacy-mim-search | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Exact legacy token and filename check in both complete captured files | context_only | Completed negative lookup in the pinned current release; historical correspondence of the retained link remains unresolved. MediaDive compound 378 is a different identifier namespace. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-3 | scripts/repair_allisonella_acids.py; sources lines 52–100; Review lines 107–536 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| history-metadata | data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml; data/normalized_yaml/bacterial/allisonella_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": [{"index": 1, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 2, "issue": "timezone absent", "value": "2026-02-03T11:19:05.235270"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml", "events": 9, "timestamp_issues": [{"index": 1, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 2, "issue": "timezone absent", "value": "2026-02-03T11:19:05.235270"}]}, {"input": "data/normalized_yaml/bacterial/allisonella_medium.yaml", "events": 8, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Preserved komodoMediaList retrieval failed (403). No content is claimed from this attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006 formulation provide the required source comparison; the LB page cannot establish membership in this recipe.
- Preserved komodo1006 retrieval failed (403). No content is claimed from this attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006 formulation provide the required source comparison; the LB page cannot establish membership in this recipe.
- Preserved komodoDetail1006 retrieval failed (403). No content is claimed from this attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006 formulation provide the required source comparison; the LB page cannot establish membership in this recipe.
- Preserved lbMillerNotes retrieval failed (None). No content is claimed from this attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006 formulation provide the required source comparison; the LB page cannot establish membership in this recipe.
- The primary and archived public provider recipe are available, so failed present KOMODO/LB requests do not make the required formulation review partial. Their failures and original successful archive access time remain separate.
- Provider 1004 mL, stock 1000 mL and input-volume sums are nominal declarations/context, not measured final volumes. No acid-density conversion, new molarity, gas amount or unspecified autoclave cycle is asserted.
- Full historical archived-node reading is attributed to the specialist preflight and independent audit, with exact owner reconstruction hashes. Root reading of every repeated archived explanation is not claimed.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T140357Z-culturemech-003506-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: allisonella_medium (CultureMech:003506)'
started_at: '2026-10-21T13:52:36Z'
finished_at: '2026-10-21T14:03:57Z'
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
summary: 'The generated ALLISONELLA record is stale relative to both repaired maintained
  owners: it retains a false LB-Miller expansion, promotes fatty-acid stock quantities
  to finished-medium g/L, omits DL-2-methylbutyric acid and source preparation, and
  still asserts duplicate equivalence. The October repairs already preserve distinct
  KOMODO rates/nulls and the DSMZ batch/stock formula with evidence; reconcile and
  regenerate those versions rather than repeat their repair. Sodium-resazurin grounding
  remains incorrect in the target and DSMZ stock. No final volume, density conversion
  or growth claim is inferred.'
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
  - path: data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml
    sha256: a1d87e0fe96fcd6c1b9fcabc58333d2eba7c86bff49f8c7c487a251aa1e4384f
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    sha256: 703ca91ad8af07e196693c712f257c7171088e55d65cf9ace47addc985bda21a
    role: context
  - path: data/normalized_yaml/bacterial/allisonella_medium.yaml
    sha256: a393bc7710cc4dc1b5e9abc2de5f6e67082fc0bf3c15c4b88f59099f2df6ad4a
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
  - path: reports/ingredient_concentration_curation/20261009-allisonella-acids/context.json
    sha256: dae45cfd1b14facc31aa8691044e6718031b2cd9f8f258b4e5ae141553bfc61f
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
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_allisonella_acids.py
    sha256: 7ce960516354a7952acc81e29920459296f4e7af9bbb18f27763674233c141ef
    role: context
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
    role: context
  - path: scripts/repair_lactalbumin_formulations.py
    sha256: 3c16a3f4a2e543d280d3ccbb20a63138f2b409602d8b168b7fc742abe63b1769
    role: context
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/repair_methanogen_stock_boundaries.py
    sha256: 8d4d32c7dc3cb2586242a188f958087482df3aff553d1dbc468c422eddb037ba
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
  - path: src/culturemech/curate/curation_event.py
    sha256: e8aa053ba6dd06485b29ca5da640f91ef96513feff18492a72adc12f40130024
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
  - path: src/culturemech/validation/recipe_references.py
    sha256: 5d49d3db2f043a82b253e5a0bed03239004043922e1daab43c399a84d64fc237
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 233; batch 024 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-three task batches
    contain 230 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 233 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003506
targets:
- target_id: CultureMech:003506
  path: data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml
  label: allisonella_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch024/233/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-024/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch024/233/strict.tsv"
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003506
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
  - CultureMech:003506
- check_id: komodoMediaList-source-access
  name: 'Exact source content access: komodoMediaList'
  required: false
  status: unavailable
  summary: Preserved komodoMediaList retrieval failed (403). No content is claimed
    from this attempt. Exact DSMZ1006, current API and the separately hashed archived
    public KOMODO1006 formulation provide the required source comparison; the LB page
    cannot establish membership in this recipe.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - komodoMediaList-attempt
- check_id: komodo1006-source-access
  name: 'Exact source content access: komodo1006'
  required: false
  status: unavailable
  summary: Preserved komodo1006 retrieval failed (403). No content is claimed from
    this attempt. Exact DSMZ1006, current API and the separately hashed archived public
    KOMODO1006 formulation provide the required source comparison; the LB page cannot
    establish membership in this recipe.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - komodo1006-attempt
- check_id: komodoDetail1006-source-access
  name: 'Exact source content access: komodoDetail1006'
  required: false
  status: unavailable
  summary: Preserved komodoDetail1006 retrieval failed (403). No content is claimed
    from this attempt. Exact DSMZ1006, current API and the separately hashed archived
    public KOMODO1006 formulation provide the required source comparison; the LB page
    cannot establish membership in this recipe.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - komodoDetail1006-attempt
- check_id: lbMillerNotes-source-access
  name: 'Exact source content access: lbMillerNotes'
  required: false
  status: unavailable
  summary: Preserved lbMillerNotes retrieval failed (None). No content is claimed
    from this attempt. Exact DSMZ1006, current API and the separately hashed archived
    public KOMODO1006 formulation provide the required source comparison; the LB page
    cannot establish membership in this recipe.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - lbMillerNotes-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/allisonella_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:53:05.414792Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch024/233/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:53:06.814965Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-024/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch024/233/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:53:08.400541Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:53:09.483168Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T14:03:56Z'
  support: supports
  summary: './data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml:1:id: CultureMech:003506

    ./data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml:1:id: CultureMech:003506

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch024/source-preflight-bound/233/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T14:03:56Z'
  support: supports
  summary: 29 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: f13a0f131f77fc67f7a79d7f3d8f4c5ba3e4502c3f98eea0945f65435dc16b44
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch024/source-preflight-bound/233/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: 3d45df59bc5d11215aa87c0adc4f77298b8fef33092f84f1bd8e2667c0c05e27
- evidence_id: dsmz1006
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf
  locator: Complete one-page primary, both tables and preparation; page image independently
    inspected
  accessed_at: '2026-10-21T13:41:00.635240Z'
  support: supports
  summary: Source versions and stages remain separate. Primary batch masses, stock
    liquid inputs and provider-reported rates are not interchangeable. Archived KOMODO
    is a preserved public response, not a successful present retrieval.
  snapshot_sha256: 8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283
- evidence_id: mediadive1006api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1006
  locator: Complete main solution 2052 and referenced stock 608, all 14+7 rows and
    preparation
  accessed_at: '2026-10-21T13:40:59.752615Z'
  support: supports
  summary: Source versions and stages remain separate. Primary batch masses, stock
    liquid inputs and provider-reported rates are not interchangeable. Archived KOMODO
    is a preserved public response, not a successful present retrieval.
  snapshot_sha256: e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f
- evidence_id: solution608
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/608
  locator: Complete exact seven-row stock endpoint; identity and amount/unit correspondence
  accessed_at: '2026-10-21T13:42:26.127322Z'
  support: supports
  summary: Source versions and stages remain separate. Primary batch masses, stock
    liquid inputs and provider-reported rates are not interchangeable. Archived KOMODO
    is a preserved public response, not a successful present retrieval.
  snapshot_sha256: c82c2f685260a674c13acb93c21e12eebc4e31b713fc952da3fa85c37d1ebcca
- evidence_id: komodo1006Archived
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006
  locator: Complete archived public HTML, 21-row compound table, features and separate
    SEED table
  accessed_at: '2026-10-09T01:48:14.608032Z'
  support: supports
  summary: Source versions and stages remain separate. Primary batch masses, stock
    liquid inputs and provider-reported rates are not interchangeable. Archived KOMODO
    is a preserved public response, not a successful present retrieval.
  snapshot_sha256: a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7
- evidence_id: komodoMediaList-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaList
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T13:40:59.461854Z'
  support: context_only
  summary: Preserved komodoMediaList retrieval failed (403). No content is claimed
    from this attempt. Exact DSMZ1006, current API and the separately hashed archived
    public KOMODO1006 formulation provide the required source comparison; the LB page
    cannot establish membership in this recipe.
  snapshot_sha256: 6fd54c15a816e47cf87c082f1738a09522dc88f8d69043b2a2ead24ccfe4b1d4
- evidence_id: komodo1006-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?medium=1006
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T13:40:59.462183Z'
  support: context_only
  summary: Preserved komodo1006 retrieval failed (403). No content is claimed from
    this attempt. Exact DSMZ1006, current API and the separately hashed archived public
    KOMODO1006 formulation provide the required source comparison; the LB page cannot
    establish membership in this recipe.
  snapshot_sha256: 83640eb5d76cd291f84a5986b46d44d930d174705724b289e2e8b1771c526b13
- evidence_id: komodoDetail1006-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T13:42:25.900917Z'
  support: context_only
  summary: Preserved komodoDetail1006 retrieval failed (403). No content is claimed
    from this attempt. Exact DSMZ1006, current API and the separately hashed archived
    public KOMODO1006 formulation provide the required source comparison; the LB page
    cannot establish membership in this recipe.
  snapshot_sha256: db433dbf1096f7a17313141b65ec54e358d30d2693e9d79a95557096ac30adc6
- evidence_id: lbMillerNotes-attempt
  kind: database
  reference: https://www.laboratorynotes.com/preparation-of-luria-bertani-lb-miller-broth/
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T13:41:02.586238Z'
  support: context_only
  summary: Preserved lbMillerNotes retrieval failed (None). No content is claimed
    from this attempt. Exact DSMZ1006, current API and the separately hashed archived
    public KOMODO1006 formulation provide the required source comparison; the LB page
    cannot establish membership in this recipe.
- evidence_id: komodo1006-catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact byte-literal HTML table row for MediaInfo=1006
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Source catalog identity, DSMZ cross-reference and encoded metadata only.
    This does not authenticate the historical copied formulation or establish growth/atmosphere.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006'\
    \ >1006</a></TD>\n\t\t\t\t\t<TD>ALLISONELLA medium</TD>\n\t\t\t\t\t<TD> 6.0</TD>\n\
    \t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n<TD><a\
    \ href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
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
- evidence_id: chebi15366
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15366
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:29:08.353669Z'
  support: supports
  summary: CHEBI:15366 resolves to acetic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b887e3ee7d15164ff6fa8efd11f052ea16965afb730d69ccf31744ffb64d2139
- evidence_id: chebi16135
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16135
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:29:08.576156Z'
  support: supports
  summary: CHEBI:16135 resolves to isobutyric acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 9066add4e624c1d66e8ed2b31b6d8cd83aee6227fe29e0fe5a7bf1d36fedb4ab
- evidence_id: chebi17418
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17418
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:29:08.845270Z'
  support: supports
  summary: CHEBI:17418 resolves to valeric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 6546fe66aa87af53dc1299ff42f673250bf3224d190f83b9b21df72da4eb863b
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
- evidence_id: chebi27570
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27570
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T13:41:01.910442Z'
  support: supports
  summary: CHEBI:27570 resolves to histidine. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: d1ed5791c2b88708d660cb40aaabb0e5d9520bb00bfd69d40810420e14538d7d
- evidence_id: chebi28484
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28484
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:29:08.988065Z'
  support: supports
  summary: CHEBI:28484 resolves to isovaleric acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2b4dfb8baa01781ecd4134258216b42713d7a04212539eab80e08ba7f10e1a72
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
- evidence_id: chebi30768
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30768
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:29:09.188555Z'
  support: supports
  summary: CHEBI:30768 resolves to propionic acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 80537b4c820ccc6f118b47ad4c3cefcd2592c467d49b3097b4caf5bc6d993e59
- evidence_id: chebi30772
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30772
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T13:41:02.576317Z'
  support: supports
  summary: CHEBI:30772 resolves to butyric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: a8b9cd95297c39fb4d94870da094fa17f751fe3504c3b2ebffafa0605c740eff
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
- evidence_id: foodon03315426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:00:49.388263Z'
  support: supports
  summary: FOODON:03315426 resolves to yeast extract. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: micro0000182
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:37:21.973857Z'
  support: supports
  summary: MICRO:0000182 resolves to tryptone. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 01875997c482a49e4d41eb35c6c697e190afd236a8527625e94b6f96df3872b0
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T14:03:56Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:15366": [{"label": "Acetic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:15366", "preferred_term": "Acetic acid",
    "ontology_id": "CHEBI:15366", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:16135": [{"label": "Isobutyric acid", "match_type": "preferred_term", "identifier":
    "CHEBI:16135", "preferred_term": "Isobutyric acid", "ontology_id": "CHEBI:16135",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17418": [{"label":
    "Valeric acid", "match_type": "preferred_term", "identifier": "CHEBI:17418", "preferred_term":
    "Valeric acid", "ontology_id": "CHEBI:17418", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27570": [{"label":
    "DL-Histidine", "match_type": "preferred_term", "identifier": "CHEBI:27570", "preferred_term":
    "DL-Histidine", "ontology_id": "CHEBI:27570", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate
    solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:30768": [{"label": "Propionic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:30768", "preferred_term": "Propionic acid",
    "ontology_id": "CHEBI:30768", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:30772": [{"label": "Butyric acid", "match_type": "preferred_term", "identifier":
    "CHEBI:30772", "preferred_term": "Butyric acid", "ontology_id": "CHEBI:30772",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label":
    "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label":
    "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term":
    "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label":
    "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x
    H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term":
    "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: attached-evidence
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch024/233/existing-evidence-recheck.json
  locator: All 67 current owner evidence objects, snippets/explanations and source
    hashes
  accessed_at: '2026-10-21T14:03:56Z'
  support: supports
  summary: Current attached evidence is retained per source and per field. KOMODO
    snippets are extracted HTML text; primary snippets use layout text. The archived
    raw response and current PDF raw hash remain separately identified.
  snapshot_sha256: 763b1053e1c4ba80d9a12d5d6531266502d959315e0ba068550ec4f07f049122
- evidence_id: historical-reading
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/233-owner-lossless-reading/manifest.json
  locator: Lossless partition of both complete owner YAMLs into current fields/evidence/history,
    with exact reconstruction hashes
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: Specialist preflight reading covered the complete archived nodes and repeated
    explanations through lossless deduplicated views. The independent cache audit
    verified 67 evidence objects, 127 additional excerpts and 194 timestamp instances
    across its scoped cache. This review reread current fields, distinct claims, source
    tables and current evidence; root history reading is not claimed.
  snapshot_sha256: 56fecb2b41645990ed39b26ecb9a93a5144d1224018d89f6eb0a7ac4951b6161
- evidence_id: independent-cache-audit
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/batch024-firstfive-independent-audit.json
  locator: Independent frozen first-five cache audit; exact current owner evidence
    and raw catalog slices
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: Independent audit supports source integrity and historical excerpt correspondence.
    Parsed catalog literal_html was serialized HTML, so this review quotes the separately
    extracted raw row instead.
  snapshot_sha256: 2b4da62f90db4018d6191c16b9a3f497192ca59630b913334a3b7c74647caf41
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch024/233/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 32ac8d6d9116f3125e78a4fe297a45baa97c8fdb69b51368f7877134eacf777b
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch024/233/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: c74a708692f9036624917241c25835290f9bc075c0481332711391c56cec607e
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Complete pinned public catalog/tree at 6643131b0f12ab40b66f98135245fca04027e0e9;
    exact token and numeric filename scope
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: The bounded current lookup found no legacy 000378 identifier or corresponding
    numeric filename. This is not a search of all historical revisions and does not
    establish a replacement ID.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Complete pinned public catalog/tree at 6643131b0f12ab40b66f98135245fca04027e0e9;
    exact token and numeric filename scope
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: supports
  summary: The bounded current lookup found no legacy 000378 identifier or corresponding
    numeric filename. This is not a search of all historical revisions and does not
    establish a replacement ID.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: legacy-mim-search
  kind: search
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json;
    https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Exact legacy token and filename check in both complete captured files
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: Completed negative lookup in the pinned current release; historical correspondence
    of the retained link remains unresolved. MediaDive compound 378 is a different
    identifier namespace.
  search_scope: Only complete captured public MIM catalog and recursive Git tree pinned
    to6643131b0f12ab40b66f98135245fca04027e0e9, exact MediaIngredientMech:000378 and
    numeric filename378/000378; no historical revision search or remote absence claim.
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T14:03:56Z'
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
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-context-3
  kind: record_content
  reference: scripts/repair_allisonella_acids.py
  locator: sources lines 52–100; Review lines 107–536
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 7ce960516354a7952acc81e29920459296f4e7af9bbb18f27763674233c141ef
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALLISONELLA_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml;
    data/normalized_yaml/bacterial/allisonella_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T14:03:56Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": [{"index": 1, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 2, "issue":
    "timezone absent", "value": "2026-02-03T11:19:05.235270"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml",
    "events": 9, "timestamp_issues": [{"index": 1, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 2, "issue": "timezone absent", "value":
    "2026-02-03T11:19:05.235270"}]}, {"input": "data/normalized_yaml/bacterial/allisonella_medium.yaml",
    "events": 8, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '18 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 19/21
    primary and 14/21 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131527
  - chebi15366
  - chebi16135
  - chebi17418
  - chebi26710
  - chebi27570
  - chebi28484
  - chebi29377
  - chebi30768
  - chebi30772
  - chebi31795
  - chebi62946
  - chebi63036
  - chebi86158
  - chebi8806
  - chebi91248
  - foodon03315426
  - micro0000182
  details: 'Instance coverage on a 0–100 percent scale, denominator 21: primary 90.48%;
    secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 52 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"DSMZ main: DL-Histidine\",\n\
    \    \"field_path\": \"main_recipe[0]\",\n    \"decision\": \"correct\",\n   \
    \ \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"DL-Histidine\\\",\\n          \
    \              \\\"compound_id\\\": 916,\\n                        \\\"amount\\\
    \": 7.8,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 7.76892,\\n                        \\\"mmol_l\\\": 50.072,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact DL-Histidine table row\",\n        \"\
    exact_source_quote\": \"   DL-Histidine                                      \
    \                 7.80         g\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The repaired DSMZ owner retains the exact\
    \ batch input with attached API/primary evidence. Its absent final concentration\
    \ is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured\
    \ final volume. The target copies a provider g_l value without this basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"7.76892\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"Source\
    \ batch input: 7.8 g. Preserve the exact mass in notes; API g_l=7.76892 uses the\
    \ provider's main-volume encoding and is not an independently verified final-medium\
    \ concentration.\",\n        \"decision\": \"verified\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"7.8 g = 7.8 g batch input. On the provider-declared 1.004 L basis, division\
    \ gives 7.768924302788844621513944223 g/L; source g_l=7.76892 retains its reported\
    \ precision. Do not silently replace it by the unrounded quotient or recertify\
    \ the denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ main: Yeast\
    \ extract\",\n    \"field_path\": \"main_recipe[1]\",\n    \"decision\": \"correct\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Yeast extract\\\",\\n         \
    \               \\\"compound_id\\\": 16,\\n                        \\\"amount\\\
    \": 4,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 3.98406,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact Yeast extract table row\",\n        \"\
    exact_source_quote\": \"   Yeast extract                                     \
    \                 4.00         g\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The repaired DSMZ owner retains the exact\
    \ batch input with attached API/primary evidence. Its absent final concentration\
    \ is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured\
    \ final volume. The target copies a provider g_l value without this basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"3.98406\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"Source\
    \ batch input: 4 g. Preserve the exact mass in notes; API g_l=3.98406 uses the\
    \ provider's main-volume encoding and is not an independently verified final-medium\
    \ concentration.\",\n        \"decision\": \"verified\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"4 g = 4 g batch input. On the provider-declared 1.004 L basis, division gives\
    \ 3.984063745019920318725099602 g/L; source g_l=3.98406 retains its reported precision.\
    \ Do not silently replace it by the unrounded quotient or recertify the denominator.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"DSMZ main: Trypticase peptone\"\
    ,\n    \"field_path\": \"main_recipe[2]\",\n    \"decision\": \"correct\",\n \
    \   \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 3,\\\
    n                        \\\"compound\\\": \\\"Trypticase peptone\\\",\\n    \
    \                    \\\"compound_id\\\": 124,\\n                        \\\"\
    attribute\\\": \\\"BD BBL\\\",\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.996016,\\n                        \\\"optional\\\": 0\\n        \
    \            }\",\n        \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact Trypticase peptone (BD BBL) table row\"\
    ,\n        \"exact_source_quote\": \"   Trypticase peptone (BD BBL)          \
    \                              1.00         g\",\n        \"snapshot_sha256\"\
    : \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\",\n    \
    \    \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The repaired DSMZ owner retains the exact\
    \ batch input with attached API/primary evidence. Its absent final concentration\
    \ is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured\
    \ final volume. The target copies a provider g_l value without this basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.996016\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"Source\
    \ batch input: 1 g. Preserve the exact mass in notes; API g_l=0.996016 uses the\
    \ provider's main-volume encoding and is not an independently verified final-medium\
    \ concentration. Source material qualifier: BD BBL.\",\n        \"decision\":\
    \ \"verified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"1 g = 1 g batch input. On the provider-declared 1.004 L basis, division gives\
    \ 0.9960159362549800796812749004 g/L; source g_l=0.996016 retains its reported\
    \ precision. Do not silently replace it by the unrounded quotient or recertify\
    \ the denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ main: K2HPO4\"\
    ,\n    \"field_path\": \"main_recipe[3]\",\n    \"decision\": \"correct\",\n \
    \   \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 4,\\\
    n                        \\\"compound\\\": \\\"K2HPO4\\\",\\n                \
    \        \\\"compound_id\\\": 10,\\n                        \\\"amount\\\": 0.29,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.288845,\\n                        \\\"mmol_l\\\": 1.65835,\\n   \
    \                     \\\"optional\\\": 0\\n                    }\",\n       \
    \ \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact K2HPO4 table row\",\n        \"exact_source_quote\"\
    : \"   K2HPO4                                                             0.29\
    \         g\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The repaired DSMZ owner retains the exact\
    \ batch input with attached API/primary evidence. Its absent final concentration\
    \ is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured\
    \ final volume. The target copies a provider g_l value without this basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.288845\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Source\
    \ batch input: 0.29 g. Preserve the exact mass in notes; API g_l=0.288845 uses\
    \ the provider's main-volume encoding and is not an independently verified final-medium\
    \ concentration.\",\n        \"decision\": \"verified\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"0.29 g = 0.29 g batch input. On the provider-declared 1.004 L basis, division\
    \ gives 0.2888446215139442231075697211 g/L; source g_l=0.288845 retains its reported\
    \ precision. Do not silently replace it by the unrounded quotient or recertify\
    \ the denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ main: KH2PO4\"\
    ,\n    \"field_path\": \"main_recipe[4]\",\n    \"decision\": \"correct\",\n \
    \   \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 5,\\\
    n                        \\\"compound\\\": \\\"KH2PO4\\\",\\n                \
    \        \\\"compound_id\\\": 11,\\n                        \\\"amount\\\": 0.29,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.288845,\\n                        \\\"mmol_l\\\": 2.12253,\\n   \
    \                     \\\"optional\\\": 0\\n                    }\",\n       \
    \ \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact KH2PO4 table row\",\n        \"exact_source_quote\"\
    : \"   KH2PO4                                                             0.29\
    \         g\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The repaired DSMZ owner retains the exact\
    \ batch input with attached API/primary evidence. Its absent final concentration\
    \ is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured\
    \ final volume. The target copies a provider g_l value without this basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.288845\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Source\
    \ batch input: 0.29 g. Preserve the exact mass in notes; API g_l=0.288845 uses\
    \ the provider's main-volume encoding and is not an independently verified final-medium\
    \ concentration.\",\n        \"decision\": \"verified\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"0.29 g = 0.29 g batch input. On the provider-declared 1.004 L basis, division\
    \ gives 0.2888446215139442231075697211 g/L; source g_l=0.288845 retains its reported\
    \ precision. Do not silently replace it by the unrounded quotient or recertify\
    \ the denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ main: (NH4)2SO4\"\
    ,\n    \"field_path\": \"main_recipe[5]\",\n    \"decision\": \"correct\",\n \
    \   \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"(NH4)2SO4\\\",\\n             \
    \           \\\"compound_id\\\": 27,\\n                        \\\"amount\\\"\
    : 0.48,\\n                        \\\"unit\\\": \\\"g\\\",\\n                \
    \        \\\"g_l\\\": 0.478088,\\n                        \\\"mmol_l\\\": 3.61804,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact (NH4)2SO4 table row\",\n        \"exact_source_quote\"\
    : \"   (NH4)2SO4                                                          0.48\
    \         g\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The repaired DSMZ owner retains the exact\
    \ batch input with attached API/primary evidence. Its absent final concentration\
    \ is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured\
    \ final volume. The target copies a provider g_l value without this basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.478088\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"Source\
    \ batch input: 0.48 g. Preserve the exact mass in notes; API g_l=0.478088 uses\
    \ the provider's main-volume encoding and is not an independently verified final-medium\
    \ concentration.\",\n        \"decision\": \"verified\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"0.48 g = 0.48 g batch input. On the provider-declared 1.004 L basis, division\
    \ gives 0.4780876494023904382470119522 g/L; source g_l=0.478088 retains its reported\
    \ precision. Do not silently replace it by the unrounded quotient or recertify\
    \ the denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ main: NaCl\"\
    ,\n    \"field_path\": \"main_recipe[6]\",\n    \"decision\": \"correct\",\n \
    \   \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 7,\\\
    n                        \\\"compound\\\": \\\"NaCl\\\",\\n                  \
    \      \\\"compound_id\\\": 43,\\n                        \\\"amount\\\": 0.48,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.478088,\\n                        \\\"mmol_l\\\": 8.18083,\\n   \
    \                     \\\"optional\\\": 0\\n                    }\",\n       \
    \ \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact NaCl table row\",\n        \"exact_source_quote\"\
    : \"   NaCl                                                               0.48\
    \         g\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The repaired DSMZ owner retains the exact\
    \ batch input with attached API/primary evidence. Its absent final concentration\
    \ is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured\
    \ final volume. The target copies a provider g_l value without this basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.478088\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"Source\
    \ batch input: 0.48 g. Preserve the exact mass in notes; API g_l=0.478088 uses\
    \ the provider's main-volume encoding and is not an independently verified final-medium\
    \ concentration.\",\n        \"decision\": \"verified\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"0.48 g = 0.48 g batch input. On the provider-declared 1.004 L basis, division\
    \ gives 0.4780876494023904382470119522 g/L; source g_l=0.478088 retains its reported\
    \ precision. Do not silently replace it by the unrounded quotient or recertify\
    \ the denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ main: MgSO4\
    \ x 7 H2O\",\n    \"field_path\": \"main_recipe[7]\",\n    \"decision\": \"correct\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 8,\\\
    n                        \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 8,\\n                        \\\"amount\\\
    \": 0.1,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 0.0996016,\\n                        \\\"mmol_l\\\": 0.404103,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact MgSO4 x 7 H2O table row\",\n        \"\
    exact_source_quote\": \"   MgSO4 x 7 H2O                                     \
    \                 0.10         g\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The repaired DSMZ owner retains the exact\
    \ batch input with attached API/primary evidence. Its absent final concentration\
    \ is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured\
    \ final volume. The target copies a provider g_l value without this basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.0996016\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].notes\",\n        \"stored\": \"Source\
    \ batch input: 0.1 g. Preserve the exact mass in notes; API g_l=0.0996016 uses\
    \ the provider's main-volume encoding and is not an independently verified final-medium\
    \ concentration.\",\n        \"decision\": \"verified\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"0.1 g = 0.1 g batch input. On the provider-declared 1.004 L basis, division\
    \ gives 0.09960159362549800796812749004 g/L; source g_l=0.0996016 retains its\
    \ reported precision. Do not silently replace it by the unrounded quotient or\
    \ recertify the denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ\
    \ main: CaCl2 x 2 H2O\",\n    \"field_path\": \"main_recipe[8]\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 7,\\n                        \\\"amount\\\
    \": 64,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.063745,\\n                        \\\"mmol_l\\\": 0.433595,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact CaCl2 x 2 H2O table row\",\n        \"\
    exact_source_quote\": \"   CaCl2 x 2 H2O                                     \
    \               64.00        mg\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The repaired DSMZ owner retains the exact\
    \ batch input with attached API/primary evidence. Its absent final concentration\
    \ is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured\
    \ final volume. The target copies a provider g_l value without this basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[8].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.063745\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].notes\",\n        \"stored\": \"Source\
    \ batch input: 64 mg. Preserve the exact mass in notes; API g_l=0.063745 uses\
    \ the provider's main-volume encoding and is not an independently verified final-medium\
    \ concentration.\",\n        \"decision\": \"verified\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"64 mg = 0.064 g batch input. On the provider-declared 1.004 L basis, division\
    \ gives 0.06374501992031872509960159363 g/L; source g_l=0.063745 retains its reported\
    \ precision. Do not silently replace it by the unrounded quotient or recertify\
    \ the denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ main: Sodium\
    \ resazurin\",\n    \"field_path\": \"main_recipe[9]\",\n    \"decision\": \"\
    add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[9]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 10,\\\
    n                        \\\"compound\\\": \\\"Sodium resazurin\\\",\\n      \
    \                  \\\"compound_id\\\": 1852,\\n                        \\\"attribute\\\
    \": \\\"0.1% w/v\\\",\\n                        \\\"amount\\\": 0.5,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\
    \": 0.000498008,\\n                        \\\"mmol_l\\\": 0.00198275,\\n    \
    \                    \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact Sodium resazurin (0.1% w/v) table row\"\
    ,\n        \"exact_source_quote\": \"   Sodium resazurin (0.1% w/v)          \
    \                              0.50        ml\",\n        \"snapshot_sha256\"\
    : \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\",\n    \
    \    \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner already preserves this\
    \ receiving-medium stock dose with matching attached evidence. The target has\
    \ no stock container. The amount is a stock addition, not a finished-medium mass\
    \ concentration.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0005\",\n          \"unit\": \"L\"\n        },\n\
    \        \"decision\": \"verified\"\n      },\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[9].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"0.000498008\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      }\n    ],\n  \
    \  \"arithmetic\": \"0.5 mL ÷ 1000 = 0.0005 L added stock. 0.1% w/v = 0.001 g/mL\
    \ stock; 0.50 mL supplies 0.0005 g sodium resazurin. Division by the provider\
    \ nominal 1.004 L gives about 0.000498008 g/L, not an independently measured final\
    \ concentration.\"\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ main: Na2CO3\"\
    ,\n    \"field_path\": \"main_recipe[10]\",\n    \"decision\": \"correct\",\n\
    \    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[10]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 11,\\\
    n                        \\\"compound\\\": \\\"Na2CO3\\\",\\n                \
    \        \\\"compound_id\\\": 32,\\n                        \\\"amount\\\": 4,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 3.98406,\\n                        \\\"mmol_l\\\": 37.5898,\\n    \
    \                    \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact Na2CO3 table row\",\n        \"exact_source_quote\"\
    : \"   Na2CO3                                                             4.00\
    \         g\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The repaired DSMZ owner retains the exact\
    \ batch input with attached API/primary evidence. Its absent final concentration\
    \ is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured\
    \ final volume. The target copies a provider g_l value without this basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"3.98406\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].notes\",\n        \"stored\": \"Source\
    \ batch input: 4 g. Preserve the exact mass in notes; API g_l=3.98406 uses the\
    \ provider's main-volume encoding and is not an independently verified final-medium\
    \ concentration.\",\n        \"decision\": \"verified\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"4 g = 4 g batch input. On the provider-declared 1.004 L basis, division gives\
    \ 3.984063745019920318725099602 g/L; source g_l=3.98406 retains its reported precision.\
    \ Do not silently replace it by the unrounded quotient or recertify the denominator.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"DSMZ main: Volatile fatty acid mixture\"\
    ,\n    \"field_path\": \"main_recipe[11]\",\n    \"decision\": \"add\",\n    \"\
    local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[11]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 12,\\\
    n                        \\\"solution\\\": \\\"Volatile fatty acid mixture\\\"\
    ,\\n                        \\\"solution_id\\\": 608,\\n                     \
    \   \\\"amount\\\": 3.1,\\n                        \\\"unit\\\": \\\"ml\\\",\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact Volatile fatty acid mixture table row\"\
    ,\n        \"exact_source_quote\": \"   Volatile fatty acid mixture          \
    \                              3.10        ml\",\n        \"snapshot_sha256\"\
    : \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\",\n    \
    \    \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner already preserves this\
    \ receiving-medium stock dose with matching attached evidence. The target has\
    \ no stock container. The amount is a stock addition, not a finished-medium mass\
    \ concentration.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0031\",\n          \"unit\": \"L\"\n        },\n\
    \        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\": \"3.1\
    \ mL ÷ 1000 = 0.0031 L added stock. \"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ main: L-Cysteine HCl x H2O\",\n    \"field_path\": \"main_recipe[12]\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"L-Cysteine HCl x H2O\\\",\\n                        \\\"compound_id\\\
    \": 770,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.498008,\\\
    n                        \\\"mmol_l\\\": 2.83545,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\"\
    ,\n        \"source_locator\": \"Page1 exact L-Cysteine HCl x H2O table row\"\
    ,\n        \"exact_source_quote\": \"   L-Cysteine HCl x H2O                 \
    \                              0.50         g\",\n        \"snapshot_sha256\"\
    : \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\",\n    \
    \    \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The repaired DSMZ owner retains the exact\
    \ batch input with attached API/primary evidence. Its absent final concentration\
    \ is deliberate: neither 1000 mL water nor provider 1004 mL establishes measured\
    \ final volume. The target copies a provider g_l value without this basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[11].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.498008\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].notes\",\n        \"stored\": \"\
    Source batch input: 0.5 g. Preserve the exact mass in notes; API g_l=0.498008\
    \ uses the provider's main-volume encoding and is not an independently verified\
    \ final-medium concentration.\",\n        \"decision\": \"verified\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"0.5 g = 0.5 g batch input. On the provider-declared 1.004 L basis, division\
    \ gives 0.4980079681274900398406374502 g/L; source g_l=0.498008 retains its reported\
    \ precision. Do not silently replace it by the unrounded quotient or recertify\
    \ the denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ main: Distilled\
    \ water\",\n    \"field_path\": \"main_recipe[13]\",\n    \"decision\": \"add\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[13]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 14,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact Distilled water table row\",\n       \
    \ \"exact_source_quote\": \"   Distilled water                               \
    \                1000.00          ml\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner correctly preserves 1000\
    \ mL water as 1 L solvent input with attached evidence. The target omits it; this\
    \ is not a final-volume denominator.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/allisonella_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[11].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"L\"\n        },\n        \"decision\": \"verified\"\
    \n      }\n    ],\n    \"arithmetic\": \"1000 mL ÷ 1000 = 1 L water input; listed\
    \ liquid additions 1000+0.50+3.10 = 1003.60 mL, distinct from provider 1004 mL\
    \ and from an unmeasured final volume.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ fatty-acid stock: Acetic acid\",\n    \"field_path\": \"solutions[1].composition[0].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Acetic acid\\\",\\n                        \\\"compound_id\\\
    \": 380,\\n                        \\\"amount\\\": 548.5,\\n                 \
    \       \\\"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\": 573.182,\\\
    n                        \\\"mmol_l\\\": 9545.09,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\"\
    ,\n        \"source_locator\": \"Page1 exact Acetic acid table row\",\n      \
    \  \"exact_source_quote\": \"   Acetic acid                                  \
    \                   548.50         ml\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner already records the exact\
    \ stock liquid volume in L with matching API and primary evidence. The target\
    \ promotes a stock quantity to finished-medium g/L. The target value equals the\
    \ provider stock g_l, whose density basis is not established by the primary; it\
    \ is not the diluted receiving-medium concentration.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"573.182\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.5485\",\n          \"unit\": \"\
    L\"\n        },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"548.5 mL ÷ 1000 = 0.5485 L stock input. The separate stock dose is 3.10 mL.\
    \ No liquid-density mass conversion or final-medium denominator is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"DSMZ fatty-acid stock: Propionic\
    \ acid\",\n    \"field_path\": \"solutions[1].composition[1].concentration\",\n\
    \    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Propionic acid\\\",\\n                        \\\"compound_id\\\
    \": 381,\\n                        \\\"amount\\\": 193.5,\\n                 \
    \       \\\"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\": 192.145,\\\
    n                        \\\"mmol_l\\\": 2593.76,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\"\
    ,\n        \"source_locator\": \"Page1 exact Propionic acid table row\",\n   \
    \     \"exact_source_quote\": \"   Propionic acid                            \
    \                      193.50         ml\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner already records the exact\
    \ stock liquid volume in L with matching API and primary evidence. The target\
    \ promotes a stock quantity to finished-medium g/L. The target value equals the\
    \ provider stock g_l, whose density basis is not established by the primary; it\
    \ is not the diluted receiving-medium concentration.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[13].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"192.145\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.1935\",\n          \"unit\": \"\
    L\"\n        },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"193.5 mL ÷ 1000 = 0.1935 L stock input. The separate stock dose is 3.10 mL.\
    \ No liquid-density mass conversion or final-medium denominator is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"DSMZ fatty-acid stock: Butyric acid\"\
    ,\n    \"field_path\": \"solutions[1].composition[2].concentration\",\n    \"\
    decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Butyric acid\\\",\\n                        \\\"compound_id\\\
    \": 314,\\n                        \\\"amount\\\": 129,\\n                   \
    \     \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact Butyric acid table row\",\n        \"\
    exact_source_quote\": \"   Butyric acid                                      \
    \              129.00         ml\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner already records the exact\
    \ stock liquid volume in L with matching API and primary evidence. The target\
    \ promotes a stock quantity to finished-medium g/L. Specifically, 129 mL butyric\
    \ acid is represented as 129 g/L although this API row supplies no g_l; no density\
    \ justifies that unit change.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"129\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.129\",\n          \"unit\": \"\
    L\"\n        },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"129 mL ÷ 1000 = 0.129 L stock input. The separate stock dose is 3.10 mL. No\
    \ liquid-density mass conversion or final-medium denominator is inferred.\"\n\
    \  },\n  {\n    \"ingredient_or_context\": \"DSMZ fatty-acid stock: n-Valeric\
    \ acid\",\n    \"field_path\": \"solutions[1].composition[3].concentration\",\n\
    \    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"n-Valeric acid\\\",\\n                        \\\"compound_id\\\
    \": 288,\\n                        \\\"amount\\\": 32.25,\\n                 \
    \       \\\"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\": 30.2827,\\\
    n                        \\\"mmol_l\\\": 296.512,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\"\
    ,\n        \"source_locator\": \"Page1 exact n-Valeric acid table row\",\n   \
    \     \"exact_source_quote\": \"   n-Valeric acid                            \
    \                       32.25         ml\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner already records the exact\
    \ stock liquid volume in L with matching API and primary evidence. The target\
    \ promotes a stock quantity to finished-medium g/L. The target value equals the\
    \ provider stock g_l, whose density basis is not established by the primary; it\
    \ is not the diluted receiving-medium concentration.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[15].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"30.2827\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.03225\",\n          \"unit\": \"\
    L\"\n        },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"32.25 mL ÷ 1000 = 0.03225 L stock input. The separate stock dose is 3.10 mL.\
    \ No liquid-density mass conversion or final-medium denominator is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"DSMZ fatty-acid stock: iso-Butyric\
    \ acid\",\n    \"field_path\": \"solutions[1].composition[4].concentration\",\n\
    \    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"iso-Butyric acid\\\",\\n                        \\\"compound_id\\\
    \": 377,\\n                        \\\"amount\\\": 32.25,\\n                 \
    \       \\\"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\": 30.6375,\\\
    n                        \\\"mmol_l\\\": 347.719,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\"\
    ,\n        \"source_locator\": \"Page1 exact iso-Butyric acid table row\",\n \
    \       \"exact_source_quote\": \"   iso-Butyric acid                        \
    \                         32.25         ml\",\n        \"snapshot_sha256\": \"\
    8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\",\n        \"\
    parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner already records the exact\
    \ stock liquid volume in L with matching API and primary evidence. The target\
    \ promotes a stock quantity to finished-medium g/L. The target value equals the\
    \ provider stock g_l, whose density basis is not established by the primary; it\
    \ is not the diluted receiving-medium concentration.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[16].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"30.6375\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.03225\",\n          \"unit\": \"\
    L\"\n        },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"32.25 mL ÷ 1000 = 0.03225 L stock input. The separate stock dose is 3.10 mL.\
    \ No liquid-density mass conversion or final-medium denominator is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"DSMZ fatty-acid stock: DL-2-Methylbutyric\
    \ acid\",\n    \"field_path\": \"solutions[1].composition[5].concentration\",\n\
    \    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"DL-2-Methylbutyric acid\\\",\\n                        \\\"\
    compound_id\\\": 223,\\n                        \\\"amount\\\": 32.25,\\n    \
    \                    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact DL-2-Methylbutyric acid table row\",\n\
    \        \"exact_source_quote\": \"   DL-2-Methylbutyric acid                \
    \                          32.25         ml\",\n        \"snapshot_sha256\": \"\
    8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\",\n        \"\
    parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The source and repaired owner contain\
    \ DL-2-methylbutyric acid 32.25 mL in the stock. It is absent from the target;\
    \ no mass or final concentration is supplied by this API row.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\",\n\
    \        \"field_path\": \"solutions[1].composition[5].concentration\",\n    \
    \    \"stored\": {\n          \"value\": \"0.03225\",\n          \"unit\": \"\
    L\"\n        },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"32.25 mL ÷ 1000 = 0.03225 L stock input. The separate stock dose is 3.10 mL.\
    \ No liquid-density mass conversion or final-medium denominator is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"DSMZ fatty-acid stock: iso-Valeric\
    \ acid\",\n    \"field_path\": \"solutions[1].composition[6].concentration\",\n\
    \    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"iso-Valeric acid\\\",\\n                        \\\"compound_id\\\
    \": 378,\\n                        \\\"amount\\\": 32.25,\\n                 \
    \       \\\"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\": 30.0247,\\\
    n                        \\\"mmol_l\\\": 293.986,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\"\
    ,\n        \"source_locator\": \"Page1 exact iso-Valeric acid table row\",\n \
    \       \"exact_source_quote\": \"   iso-Valeric acid                        \
    \                         32.25         ml\",\n        \"snapshot_sha256\": \"\
    8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\",\n        \"\
    parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner already records the exact\
    \ stock liquid volume in L with matching API and primary evidence. The target\
    \ promotes a stock quantity to finished-medium g/L. The target value equals the\
    \ provider stock g_l, whose density basis is not established by the primary; it\
    \ is not the diluted receiving-medium concentration.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[20].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"30.0247\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.03225\",\n          \"unit\": \"\
    L\"\n        },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"32.25 mL ÷ 1000 = 0.03225 L stock input. The separate stock dose is 3.10 mL.\
    \ No liquid-density mass conversion or final-medium denominator is inferred.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Sodium-resazurin stock strength\"\
    ,\n    \"field_path\": \"solutions[0].composition[0].concentration\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\": \"\
    $.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 10,\\n                        \\\"compound\\\
    \": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\": 1852,\\\
    n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n             \
    \           \\\"amount\\\": 0.5,\\n                        \\\"unit\\\": \\\"\
    ml\\\",\\n                        \\\"g_l\\\": 0.000498008,\\n               \
    \         \\\"mmol_l\\\": 0.00198275,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact Sodium resazurin (0.1% w/v) table row\"\
    ,\n        \"exact_source_quote\": \"   Sodium resazurin (0.1% w/v)          \
    \                              0.50        ml\",\n        \"snapshot_sha256\"\
    : \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\",\n    \
    \    \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The source explicitly gives 0.1% w/v stock\
    \ strength separately from 0.50 mL dose. The DSMZ owner correctly retains this\
    \ with attached evidence; the target lacks the stock.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\",\n\
    \        \"field_path\": \"solutions[0].composition[0].concentration\",\n    \
    \    \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"0.1 g per 100 mL stock; not 0.1% in the receiving medium. The chemical identifier\
    \ is assessed separately from the amount.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"KOMODO reported medium: Na2CO3\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row1; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"Na2CO3 Sodium carbonate SEED-cpd00242#cpd00971##\
    \ 3.99 0.04\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific Gram Amount rate and displayed precision with attached evidence.\
    \ This verifies the reported provider quantity only; linked DSMZ batch masses\
    \ do not establish its normalization or make the two formulations exact duplicates.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.99\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"KOMODO reported medium: iso-Valeric acid\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row2; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"iso-Valeric acid iso-Valeric acid SEED-cpd05178###\
    \ null null\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific null amount with attached evidence; missing is not zero. Do\
    \ not infer an acid dose, gas quantity, water volume or final concentration from\
    \ the separate SEED aggregate table.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[1].concentration\",\n        \"stored\":\
    \ null,\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"KOMODO reported medium: DL-histidine\",\n  \
    \  \"field_path\": \"ingredients[2].concentration\",\n    \"decision\": \"verified\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"komodo1006Archived\",\n        \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row3; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"DL-histidine DL-histidine SEED-cpd00572###\
    \ 7.78 0.05\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific Gram Amount rate and displayed precision with attached evidence.\
    \ This verifies the reported provider quantity only; linked DSMZ batch masses\
    \ do not establish its normalization or make the two formulations exact duplicates.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7.78\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"KOMODO reported medium: Cysteine-HCl x H2O\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row4; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"Cysteine-HCl x H2O Cysteine-HCl SEED-cpd00084#cpd00099##\
    \ 0.50 0.00\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific Gram Amount rate and displayed precision with attached evidence.\
    \ This verifies the reported provider quantity only; linked DSMZ batch masses\
    \ do not establish its normalization or make the two formulations exact duplicates.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.50\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"KOMODO reported medium: Propionic acid\",\n    \"field_path\": \"ingredients[4].concentration\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row5; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"Propionic acid Propionic acid SEED-cpd00141###\
    \ null null\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific null amount with attached evidence; missing is not zero. Do\
    \ not infer an acid dose, gas quantity, water volume or final concentration from\
    \ the separate SEED aggregate table.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[4].concentration\",\n        \"stored\":\
    \ null,\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"KOMODO reported medium: CO2\",\n    \"field_path\"\
    : \"ingredients[5].concentration\",\n    \"decision\": \"not_quantified\",\n \
    \   \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"komodo1006Archived\",\n        \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row6; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"CO2 CO2 SEED-cpd00011### null null\",\n \
    \       \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific null amount with attached evidence; missing is not zero. Do\
    \ not infer an acid dose, gas quantity, water volume or final concentration from\
    \ the separate SEED aggregate table.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[5].concentration\",\n        \"stored\":\
    \ null,\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"KOMODO reported medium: Distilled water\",\n\
    \    \"field_path\": \"ingredients[6].concentration\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"komodo1006Archived\",\n        \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row7; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"Distilled water H2O SEED-cpd00001### null\
    \ null\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific null amount with attached evidence; missing is not zero. Do\
    \ not infer an acid dose, gas quantity, water volume or final concentration from\
    \ the separate SEED aggregate table.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[6].concentration\",\n        \"stored\":\
    \ null,\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"KOMODO reported medium: DL-2-Methyl butyric\
    \ acid\",\n    \"field_path\": \"ingredients[7].concentration\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row8; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"DL-2-Methyl butyric acid DL-2-Methylbutyric\
    \ acid 2-Methylbutyric acid# null null\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific null amount with attached evidence; missing is not zero. Do\
    \ not infer an acid dose, gas quantity, water volume or final concentration from\
    \ the separate SEED aggregate table.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[7].concentration\",\n        \"stored\":\
    \ null,\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"KOMODO reported medium: K2HPO4\",\n    \"field_path\"\
    : \"ingredients[8].concentration\",\n    \"decision\": \"verified\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"komodo1006Archived\"\
    ,\n        \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row9; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"K2HPO4 di Potassium hydrogen phosphate SEED-cpd00009#cpd00205##\
    \ 0.29 0.00\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific Gram Amount rate and displayed precision with attached evidence.\
    \ This verifies the reported provider quantity only; linked DSMZ batch masses\
    \ do not establish its normalization or make the two formulations exact duplicates.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.29\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"KOMODO reported medium: KH2PO4\",\n    \"field_path\": \"ingredients[9].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row10; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"KH2PO4 Potassium dihydrogen phosphate SEED-cpd00009#cpd00205##\
    \ 0.29 0.00\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific Gram Amount rate and displayed precision with attached evidence.\
    \ This verifies the reported provider quantity only; linked DSMZ batch masses\
    \ do not establish its normalization or make the two formulations exact duplicates.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.29\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"KOMODO reported medium: iso-Butyric acid\",\n    \"field_path\": \"ingredients[10].concentration\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row11; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"iso-Butyric acid iso-Butyric acid SEED-cpd01711###\
    \ null null\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific null amount with attached evidence; missing is not zero. Do\
    \ not infer an acid dose, gas quantity, water volume or final concentration from\
    \ the separate SEED aggregate table.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"KOMODO reported medium: n-Valeric acid\",\n\
    \    \"field_path\": \"ingredients[11].concentration\",\n    \"decision\": \"\
    not_quantified\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"komodo1006Archived\",\n        \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row12; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"n-Valeric acid n-Valeric acid SEED-cpd00597###\
    \ null null\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific null amount with attached evidence; missing is not zero. Do\
    \ not infer an acid dose, gas quantity, water volume or final concentration from\
    \ the separate SEED aggregate table.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"KOMODO reported medium: MgSO4 x 7 H2O\",\n \
    \   \"field_path\": \"ingredients[12].concentration\",\n    \"decision\": \"verified\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"komodo1006Archived\",\n        \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row13; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O Magnesium sulfate SEED-cpd00048#cpd00254##\
    \ 0.10 0.00\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific Gram Amount rate and displayed precision with attached evidence.\
    \ This verifies the reported provider quantity only; linked DSMZ batch masses\
    \ do not establish its normalization or make the two formulations exact duplicates.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.10\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"KOMODO reported medium: Butyric acid\",\n    \"field_path\": \"ingredients[13].concentration\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row14; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"Butyric acid Butyric acid SEED-cpd00211###\
    \ null null\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific null amount with attached evidence; missing is not zero. Do\
    \ not infer an acid dose, gas quantity, water volume or final concentration from\
    \ the separate SEED aggregate table.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"KOMODO reported medium: CaCl2 x 2 H2O\",\n \
    \   \"field_path\": \"ingredients[14].concentration\",\n    \"decision\": \"verified\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"komodo1006Archived\",\n        \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row15; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"CaCl2 x 2 H2O Calcium chloride SEED-cpd00063#cpd00099##\
    \ 0.06 0.00\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific Gram Amount rate and displayed precision with attached evidence.\
    \ This verifies the reported provider quantity only; linked DSMZ batch masses\
    \ do not establish its normalization or make the two formulations exact duplicates.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.06\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"KOMODO reported medium: Yeast extract\",\n    \"field_path\": \"ingredients[15].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row16; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"Yeast extract Yeast extract rich-peptone#\
    \ 3.99 null\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific Gram Amount rate and displayed precision with attached evidence.\
    \ This verifies the reported provider quantity only; linked DSMZ batch masses\
    \ do not establish its normalization or make the two formulations exact duplicates.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.99\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"KOMODO reported medium: Trypticase\",\n    \"field_path\": \"ingredients[16].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row17; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"Trypticase Trypticase rich-peptone# 1.00\
    \ null\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific Gram Amount rate and displayed precision with attached evidence.\
    \ This verifies the reported provider quantity only; linked DSMZ batch masses\
    \ do not establish its normalization or make the two formulations exact duplicates.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.00\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"KOMODO reported medium: Resazurin\",\n    \"field_path\": \"ingredients[17].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row18; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"Resazurin Resazurin SEED-cpd08053### 9.97E-4\
    \ 4.35E-6\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific Gram Amount rate and displayed precision with attached evidence.\
    \ This verifies the reported provider quantity only; linked DSMZ batch masses\
    \ do not establish its normalization or make the two formulations exact duplicates.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"9.97E-4\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"\
    ingredient_or_context\": \"KOMODO reported medium: NaCl\",\n    \"field_path\"\
    : \"ingredients[18].concentration\",\n    \"decision\": \"verified\",\n    \"\
    local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    komodo1006Archived\",\n        \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row19; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"NaCl NaCl SEED-cpd00099#cpd00971## 0.48 0.01\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific Gram Amount rate and displayed precision with attached evidence.\
    \ This verifies the reported provider quantity only; linked DSMZ batch masses\
    \ do not establish its normalization or make the two formulations exact duplicates.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.48\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"KOMODO reported medium: Acetic acid\",\n    \"field_path\": \"ingredients[19].concentration\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row20; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"Acetic acid Acetic acid SEED-cpd00029###\
    \ null null\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific null amount with attached evidence; missing is not zero. Do\
    \ not infer an acid dose, gas quantity, water volume or final concentration from\
    \ the separate SEED aggregate table.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"KOMODO reported medium: (NH4)2SO4\",\n    \"\
    field_path\": \"ingredients[20].concentration\",\n    \"decision\": \"verified\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"komodo1006Archived\",\n        \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound recipe table row21; extracted HTML text\"\
    ,\n        \"exact_source_quote\": \"(NH4)2SO4 Ammonium sulfate SEED-cpd00013#cpd00048##\
    \ 0.48 0.00\",\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      },\n      {\n        \"source_key\": \"komodo1006Archived\",\n       \
    \ \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Compound table basis; extracted HTML text\",\n\
    \        \"exact_source_quote\": \"Gram & Mol amounts are per Liter of medium.\"\
    ,\n        \"snapshot_sha256\": \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\"\
    ,\n        \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"The maintained KOMODO owner matches its\
    \ source-specific Gram Amount rate and displayed precision with attached evidence.\
    \ This verifies the reported provider quantity only; linked DSMZ batch masses\
    \ do not establish its normalization or make the two formulations exact duplicates.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.48\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Unsupported target LB expansion: Tryptone\",\n    \"field_path\": \"ingredients[17].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Trypticase peptone\\\",\\n                        \\\"compound_id\\\
    \": 124,\\n                        \\\"attribute\\\": \\\"BD BBL\\\",\\n     \
    \                   \\\"amount\\\": 1,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.996016,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact Trypticase peptone (BD BBL) table row\"\
    ,\n        \"exact_source_quote\": \"   Trypticase peptone (BD BBL)          \
    \                              1.00         g\",\n        \"snapshot_sha256\"\
    : \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\",\n    \
    \    \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"This supplier-tagged LB expansion is additional\
    \ to the genuine source ingredient. Neither complete exact recipe contains LB\
    \ Miller. Both maintained owners already removed these three false rows and retained\
    \ their history; reconcile the generated target rather than adding these masses\
    \ to genuine ingredients.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[17].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Unsupported target LB expansion: Yeast extract\",\n    \"field_path\": \"\
    ingredients[18].concentration\",\n    \"decision\": \"unsupported\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1006api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"\
    compound_id\\\": 16,\\n                        \\\"amount\\\": 4,\\n         \
    \               \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 3.98406,\\n                        \\\"optional\\\": 0\\n                  \
    \  }\",\n        \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact Yeast extract table row\",\n        \"\
    exact_source_quote\": \"   Yeast extract                                     \
    \                 4.00         g\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"This supplier-tagged LB expansion is additional\
    \ to the genuine source ingredient. Neither complete exact recipe contains LB\
    \ Miller. Both maintained owners already removed these three false rows and retained\
    \ their history; reconcile the generated target rather than adding these masses\
    \ to genuine ingredients.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[18].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Unsupported target LB expansion: Sodium chloride\",\n    \"field_path\": \"\
    ingredients[19].concentration\",\n    \"decision\": \"unsupported\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1006api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\
    \": 43,\\n                        \\\"amount\\\": 0.48,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.478088,\\\
    n                        \\\"mmol_l\\\": 8.18083,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\"\
    ,\n        \"source_locator\": \"Page1 exact NaCl table row\",\n        \"exact_source_quote\"\
    : \"   NaCl                                                               0.48\
    \         g\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"This supplier-tagged LB expansion is additional\
    \ to the genuine source ingredient. Neither complete exact recipe contains LB\
    \ Miller. Both maintained owners already removed these three false rows and retained\
    \ their history; reconcile the generated target rather than adding these masses\
    \ to genuine ingredients.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[19].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ preparation: Cooling atmosphere\",\n    \"field_path\": \"preparation_steps[0].description\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"100%\
    \ CO2 gas atmosphere\",\n        \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner already preserves this\
    \ exact preparation condition with attached root-level evidence. Add its source-attributed\
    \ context to any regenerated DSMZ representation; do not reinterpret a gas percentage\
    \ as a fixed gas ingredient dose or overwrite KOMODO aerobic metadata without\
    \ preserving the conflict. The KOMODO owner’s attached 100% CO2 note, where listed,\
    \ is verified only as attributed linked-DSMZ context, not an asserted aerobic/anaerobic\
    \ biological resolution.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n      \
    \  \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, fatty acid mixture and cysteine),\
    \ bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere.\
    \ Add solid carbonate, fatty acid mixture and cysteine and adjust pH to 6.0. Dispense\
    \ medium under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Adjust pH of complete medium to 6.0, if necessary.\",\n\
    \        \"decision\": \"verified\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\",\n      \
    \  \"field_path\": \"notes\",\n        \"stored\": \"Source: KOMODO ModelSEED\
    \ | ID: 1006 | DSMZ Medium: 1006 (mediadive.medium:1006) | Aerobic: Yes\\n\\nSuperseded\
    \ historical provenance (not a current formulation claim):\\nCommercial Product:\
    \ LB Medium (Luria-Bertani, Miller formulation)\\nSupplier: Multiple suppliers\
    \ (Difco, Sigma, etc.)\\nCatalog: Multiple (L3522 Sigma, 244520 BD)\\nSource:\
    \ https://www.laboratorynotes.com/preparation-of-luria-bertani-lb-miller-broth/\\\
    nAccessed: 2026-03-28\\n\\nConstituent composition researched from product specification.\\\
    n\\nKOMODO reports Is Aerobic: true, while its linked DSMZ original uses 100%\
    \ CO2 and anoxic vessels. Preserve this source conflict, not a resolved oxygen\
    \ requirement or quantitative gas addition.\\n\\nThe linked original specifies\
    \ anoxic preparation; it does not establish a quantitative CO2 ingredient amount\
    \ or justify replacing this provider's source-specific rates.\\n\\nArchive the\
    \ complete prior ingredient nodes, including the copied L-cysteine and sodium-resazurin\
    \ annotations, in append-only history. Their source-specific replacements do not\
    \ inherit unverified chemical forms.\\n\\nSource-specific ingredient identities\
    \ and quantity scopes supersede copied flattened amounts. Unknown gas amounts,\
    \ densities and final volumes remain unknown. Other existing chemical annotations\
    \ and all prior history are preserved, not recertified. No taxa-media association\
    \ is added.\",\n        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"DSMZ preparation: Dispensing atmosphere\",\n\
    \    \"field_path\": \"preparation_steps[0].description\",\n    \"decision\":\
    \ \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n      \
    \  \"exact_source_quote\": \"Dispense medium under 100% CO2 gas atmosphere\",\n\
    \        \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner already preserves this\
    \ exact preparation condition with attached root-level evidence. Add its source-attributed\
    \ context to any regenerated DSMZ representation; do not reinterpret a gas percentage\
    \ as a fixed gas ingredient dose or overwrite KOMODO aerobic metadata without\
    \ preserving the conflict. The KOMODO owner’s attached 100% CO2 note, where listed,\
    \ is verified only as attributed linked-DSMZ context, not an asserted aerobic/anaerobic\
    \ biological resolution.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n      \
    \  \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, fatty acid mixture and cysteine),\
    \ bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere.\
    \ Add solid carbonate, fatty acid mixture and cysteine and adjust pH to 6.0. Dispense\
    \ medium under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Adjust pH of complete medium to 6.0, if necessary.\",\n\
    \        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ preparation: Initial pH\",\n    \"field_path\": \"preparation_steps[0].description\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"adjust\
    \ pH to 6.0\",\n        \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner already preserves this\
    \ exact preparation condition with attached root-level evidence. Add its source-attributed\
    \ context to any regenerated DSMZ representation; do not reinterpret a gas percentage\
    \ as a fixed gas ingredient dose or overwrite KOMODO aerobic metadata without\
    \ preserving the conflict. The KOMODO owner’s attached 100% CO2 note, where listed,\
    \ is verified only as attributed linked-DSMZ context, not an asserted aerobic/anaerobic\
    \ biological resolution.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n      \
    \  \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, fatty acid mixture and cysteine),\
    \ bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere.\
    \ Add solid carbonate, fatty acid mixture and cysteine and adjust pH to 6.0. Dispense\
    \ medium under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Adjust pH of complete medium to 6.0, if necessary.\",\n\
    \        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ preparation: Completed-medium pH\",\n    \"field_path\": \"preparation_steps[0].description\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Adjust\
    \ pH of complete medium to 6.0, if necessary.\",\n        \"snapshot_sha256\"\
    : \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\n     \
    \ }\n    ],\n    \"rationale\": \"The DSMZ owner already preserves this exact\
    \ preparation condition with attached root-level evidence. Add its source-attributed\
    \ context to any regenerated DSMZ representation; do not reinterpret a gas percentage\
    \ as a fixed gas ingredient dose or overwrite KOMODO aerobic metadata without\
    \ preserving the conflict. The KOMODO owner’s attached 100% CO2 note, where listed,\
    \ is verified only as attributed linked-DSMZ context, not an asserted aerobic/anaerobic\
    \ biological resolution.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n      \
    \  \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, fatty acid mixture and cysteine),\
    \ bring medium to the boil, then cool to room temperature under 100% CO2 gas atmosphere.\
    \ Add solid carbonate, fatty acid mixture and cysteine and adjust pH to 6.0. Dispense\
    \ medium under 100% CO2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Adjust pH of complete medium to 6.0, if necessary.\",\n\
    \        \"decision\": \"verified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Recorded pH 6.0\",\n    \"field_path\": \"ph_value\",\n    \"decision\": \"\
    evidence_only\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive1006api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1006\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n      \
    \  \"exact_source_quote\": \"adjust pH to 6.0\",\n        \"snapshot_sha256\"\
    : \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\n     \
    \ },\n      {\n        \"source_key\": \"komodo1006Archived\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006\"\
    ,\n        \"source_locator\": \"Medium features; extracted HTML text\",\n   \
    \     \"exact_source_quote\": \"PH Info: 6.0\",\n        \"snapshot_sha256\":\
    \ \"a589509cce9d95acc1437091b62ab3d764268e261e8bdec15fb5b1b8ab4a6fa7\",\n    \
    \    \"parsed_text_sha256\": \"58908ed07aef35d8dcfa119e9969ec48f230aa684ccaa063e0d55ac1012408e2\"\
    \n      }\n    ],\n    \"rationale\": \"All three scalar pH values agree with\
    \ their source. Existing attached preparation evidence is assessed at its actual\
    \ preparation/notes scope; this scalar ledger does not claim a new field-specific\
    \ attachment.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ph_value\",\n        \"stored\": 6.0,\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/allisonella_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.0,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Unknown final-volume and conversion basis\",\n    \"field_path\": \"notes\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1006api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1006\",\n        \"source_locator\"\
    : \"$.data.solutions[0].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 1004\",\n        \"snapshot_sha256\": \"e50433d297dd2634146821ee10e55f5146cfeb37e0827e8367d8484fc418b26f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1006\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\",\n   \
    \     \"source_locator\": \"Page1 exact Distilled water table row\",\n       \
    \ \"exact_source_quote\": \"   Distilled water                               \
    \                1000.00          ml\",\n        \"snapshot_sha256\": \"8c43bfd254ab2d20065d50cd8214fa06256be7b43d01f58d1b93a9f1ff8c6283\"\
    ,\n        \"parsed_text_sha256\": \"49cf2b7bcf99912a841a517872f72586d3937c3163106d2c186bf8dcc0a52f31\"\
    \n      }\n    ],\n    \"rationale\": \"The provider declares 1004 mL; the primary\
    \ prints 1000 mL water plus stock additions without measured final-volume makeup.\
    \ The DSMZ owner explicitly preserves that limit; target notes omit it. Acid densities\
    \ are not given. No measured final concentration or unknown titrant dose is filled.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"notes\"\
    ,\n        \"stored\": \"Source: KOMODO ModelSEED | ID: 1006 | DSMZ Medium: 1006\
    \ (mediadive.medium:1006) | Aerobic: Yes\\n\\nCommercial Product: LB Medium (Luria-Bertani,\
    \ Miller formulation)\\nSupplier: Multiple suppliers (Difco, Sigma, etc.)\\nCatalog:\
    \ Multiple (L3522 Sigma, 244520 BD)\\nSource: https://www.laboratorynotes.com/preparation-of-luria-bertani-lb-miller-broth/\\\
    nAccessed: 2026-03-28\\n\\nConstituent composition researched from product specification.\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/allisonella_medium.yaml\",\n        \"field_path\"\
    : \"notes\",\n        \"stored\": \"Source: DSMZ | Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf\\\
    n\\nSuperseded historical provenance (not a current formulation claim):\\nCommercial\
    \ Product: LB Medium (Luria-Bertani, Miller formulation)\\nSupplier: Multiple\
    \ suppliers (Difco, Sigma, etc.)\\nCatalog: Multiple (L3522 Sigma, 244520 BD)\\\
    nSource: https://www.laboratorynotes.com/preparation-of-luria-bertani-lb-miller-broth/\\\
    nAccessed: 2026-03-28\\n\\nConstituent composition researched from product specification.\\\
    n\\nThe original recipe adds carbonate, fatty-acid stock and cysteine after cooling\
    \ under CO2, then dispenses and autoclaves. The API main volume of 1004 ml is\
    \ a provider encoding, not evidence of measured final volume or verified density\
    \ conversions.\\n\\nSource-specific ingredient identities and quantity scopes\
    \ supersede copied flattened amounts. Unknown gas amounts, densities and final\
    \ volumes remain unknown. Other existing chemical annotations and all prior history\
    \ are preserved, not recertified. No taxa-media association is added.\",\n   \
    \     \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Seven\
    \ stock liquid inputs sum 1000.00 mL, which is an input sum rather than an independently\
    \ measured mixed-stock volume. Main listed liquids sum 1003.60 mL; no physical-volume\
    \ equality or corrected final denominator is asserted.\"\n  }\n]"
- assessment_id: identity
  area: identity
  topic: Stale merged product versus distinct repaired source owners
  outcome: concern
  summary: Both named contributors resolve to the inspected files and permanent IDs.
    Their October 9 repairs postdate the target’s August 6 merge. KOMODO now has 21
    source-specific compound rows including 9 nulls and 12 rates; DSMZ has 12 direct
    inputs and two stocks. Reciprocal DERIVED_FROM links replace prior SOURCE_DUPLICATE.
    The target still presents the earlier copied formulation and duplicate relationship.
    Its existing path is identified, but it is not a scientifically faithful current
    representative of either owner.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - id-search
  - komodo1006Archived
  - dsmz1006
  - attached-evidence
  - historical-reading
- assessment_id: source-stage-consistency
  area: consistency
  topic: Batch masses, stock liquid volumes and provider rates
  outcome: concern
  summary: The exhaustive ledger separates 14 DSMZ main rows, seven fatty-acid inputs,
    resazurin strength, 21 KOMODO compound rows, three unsupported LB amounts and
    numeric preparation/basis contexts. Target main g/L values reproduce API nominal
    1004 mL conversions but omit that scope; acid values are stock-level or an unsupported
    mL-to-g/L substitution. The repaired DSMZ owner already retains source batch masses
    in notes, water and dose volumes in L, and stock volumes without inventing final
    concentrations. Numerical agreement with one provider field does not validate
    the target recipe.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1006
  - mediadive1006api
  - solution608
  - komodo1006Archived
  - quantity-inventory
  - quantity-local-fields
  - attached-evidence
- assessment_id: forms
  area: grounding
  topic: Source-specific salt, hydrate, stereochemistry and product claims
  outcome: concern
  summary: Primary DL-histidine is compatible with the nonspecific histidine term;
    magnesium sulfate heptahydrate, calcium chloride dihydrate, the two potassium
    phosphate salts, ammonium sulfate, sodium carbonate, L-cysteine hydrochloride
    monohydrate and named acid identities agree with their supplied forms. The DSMZ
    Trypticase BD BBL qualifier is retained in owner notes. CHEBI:8806 is neutral
    Resazurin, formula C12H7NO4 without sodium; it does not encode the explicit sodium
    resazurin stock. KOMODO’s nonspecific cysteine and resazurin names appropriately
    no longer inherit L/sodium annotations. MICRO:0000182 and FOODON:03315426 labels
    resolve, but do not authenticate the unsupported LB expansion. No replacement
    chemical ID or missing density is guessed.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1006
  - komodo1006Archived
  - chebi8806
  - chebi91248
  - chebi27570
  - micro0000182
  - foodon03315426
  - attached-evidence
- assessment_id: preparation
  area: completeness
  topic: Anoxic source sequence, gas conditions and pH
  outcome: concern
  summary: Target preparation is absent. DSMZ specifies boiling the base, cooling
    under 100% CO2, adding carbonate/fatty-acid stock/cysteine, adjusting pH 6, dispensing
    under 100% CO2 into anoxic vessels, then autoclaving and readjusting completed-medium
    pH 6 if necessary. Its owner already retains the full sequence with evidence;
    no temperature/duration is printed. KOMODO aerobic:true is conflicting catalog
    metadata and its repaired owner explicitly preserves that conflict. No gas mass,
    titrant amount or generic sterilization cycle is invented.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1006
  - mediadive1006api
  - komodo1006Archived
  - quantity-inventory
  - attached-evidence
- assessment_id: classification
  area: scope
  topic: Complex liquid formulation and bounded biology
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID agree with yeast extract/Trypticase and absence
    of agar in the exact formula. pH 6 is source-backed; aerobic catalog metadata
    is not an experimentally resolved oxygen requirement. The name ALLISONELLA and
    generic microbial-cultivation application are not strain-specific growth evidence.
    No organism/taxon, DOI/PMID, assembly, measured growth or temperature claim is
    added.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1006
  - komodo1006Archived
- assessment_id: legacy-correspondence
  area: grounding
  topic: Retained isovaleric-acid legacy MIM link
  outcome: concern
  summary: The target and both source owners retain MediaIngredientMech:000378 in
    different quantity scopes. The exact current pinned catalog/tree lookup completed
    without that identifier; CHEBI-based secondary mappings resolve separately. Historical
    correspondence remains unresolved, and the numerically similar MediaDive compound
    378 is not proof of equivalence.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - mim
  - mimPinnedCatalog
  - mimPinnedTree
  - legacy-mim-search
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 27 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: generation
  area: provenance
  topic: Existing repair, commercial-expansion history and current generators
  outcome: concern
  summary: The inspected repair_allisonella_acids.py and preserved October 9 changes
    explain why current owners removed the false supplier-tagged LB rows, restored
    DL-2-methylbutyric acid, separated DSMZ stocks and changed reciprocal relationships.
    Those repairs already exist and must be retained. Current formulation merging
    requires compatible scientific content and unions scoped evidence; it does not
    justify collapsing these distinct owner recipes. Current importer stock handling
    is context, not a replay or evidence that historical artifacts are correct. The
    old laboratorynotes URL documents expansion provenance only; its failed request
    provides no formulation evidence.
  target_ids:
  - CultureMech:003506
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - attached-evidence
  - historical-reading
  - independent-cache-audit
  - bound-context
  - writer-context-0
  - writer-context-1
  - writer-context-2
  - writer-context-3
findings:
- finding_id: f1
  issue_key: culturemech.003506.stale-flattened-formula
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stale merged recipe retains false LB additions and flattened acid stocks
  description: The generated record retains extra 10 g/L tryptone, 5 g/L yeast and
    10 g/L NaCl from an unsupported LB-Miller expansion, omits DL-2-methylbutyric
    acid, and lists stock acid values as final-medium g/L, including 129 mL butyric
    acid represented as 129 g/L. These errors make the named formula unusable as a
    faithful recipe. Both maintained owners already repaired these defects and preserve
    different source-specific rates/nulls versus batch/stock quantities.
  target_ids:
  - CultureMech:003506
  field_paths:
  - ingredients
  - solutions
  - notes
  - references
  - evidence
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1006
  - mediadive1006api
  - solution608
  - komodo1006Archived
  - quantity-inventory
  - attached-evidence
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
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
  issue_key: culturemech.003506.stale-source-equivalence
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Generated duplicate relationship contradicts repaired source distinction
  description: The target still asserts SOURCE_DUPLICATE and copied-equality notes
    even though current maintained owners carry reciprocal DERIVED_FROM relationships
    and different source-specific amounts, nulls and forms. Exact linked source identity
    supports derivation, not formula equivalence.
  target_ids:
  - CultureMech:003506
  field_paths:
  - parent_media
  - variant_relationship
  - variant_modifications
  - merged_from
  - synonyms
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - komodo1006Archived
  - dsmz1006
  - attached-evidence
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.5
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.003506.sodium-resazurin-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium resazurin is grounded to the neutral compound
  description: Target ingredients[9] and the repaired DSMZ owner’s solutions[0].composition[0]
    name sodium resazurin but carry CHEBI:8806, whose formula C12H7NO4 contains no
    sodium. Correct stock quantities and canonical label checks do not resolve supplied-salt
    identity.
  target_ids:
  - CultureMech:003506
  field_paths:
  - ingredients[9].term
  - solutions[0].composition[0].term
  evidence_ids:
  - record
  - owner-1
  - dsmz1006
  - chebi8806
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.003506.preparation-source-conflict
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated record omits the source anoxic preparation and oxygen caveat
  description: The target drops the DSMZ owner’s evidence-backed boiling/cooling/addition
    sequence, two 100% CO2 atmosphere stages, anoxic dispensing/autoclaving and final
    pH check while leaving Aerobic:Yes catalog text without the repaired owner’s explicit
    conflict explanation. Reproduction and interpretation require these source-specific
    conditions.
  target_ids:
  - CultureMech:003506
  field_paths:
  - preparation_steps
  - notes
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1006
  - mediadive1006api
  - komodo1006Archived
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: culturemech.003506.legacy-link
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Legacy isovaleric-acid MIM identifier remains unresolved
  description: MediaIngredientMech:000378 persists in target and both owner layers,
    while the complete current pinned catalog/tree lacks that legacy key. Current
    CHEBI-key correspondence does not establish its historical identity.
  target_ids:
  - CultureMech:003506
  field_paths:
  - ingredients
  - solutions[1].composition
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - mim
  - legacy-mim-search
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: culturemech.003506.history-timing
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Inherited import/copy timestamps lack reliable UTC interpretation
  description: 'Target and KOMODO owner retain invalid .fZ import timestamps and timezone-naive
    copy timestamps: four problematic current history instances. Later repair timestamps
    do not retrospectively authenticate the old access times; the primary historical
    49cf hash is layout text, not PDF bytes.'
  target_ids:
  - CultureMech:003506
  field_paths:
  - curation_history
  - references
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - history-metadata
  - attached-evidence
  - historical-reading
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
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
  description: Reconcile and regenerate from the already repaired owners, preserving
    separate source formulations and their evidence. Remove the stale unsupported
    LB expansion and retain the full acid stock/dose hierarchy and unknown final-volume
    basis; do not repeat the completed owner repair, sum duplicate nutrients, or copy
    provider stock g/L as final concentrations.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003506
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
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
  description: Preserve the current owner DERIVED_FROM evidence and source identities
    in reconciliation/regeneration. Do not merge them solely by names, historical
    ingredient fingerprint or copied pre-repair concentration signatures.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003506
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
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
  description: Resolve the explicit sodium-salt grounding in the DSMZ owner with a
    verified appropriate term before regeneration, preserving 0.1% w/v stock strength
    and 0.50 mL dose. Keep KOMODO’s separately unqualified resazurin assertion distinct;
    no replacement identifier is proposed here.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003506
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
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
  description: Restore the appropriate source-specific preparation and explicit catalog-versus-primary
    oxygen caveat during reconciliation. Retain existing owner evidence; do not invent
    a temperature, duration, gas quantity or resolve the biological oxygen requirement
    without evidence.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003506
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
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
  description: Resolve the legacy link through explicit historical provenance or retain
    an unresolved annotation; do not infer correspondence from MediaDive numeric 378
    or silently rewrite history.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:003506
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
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
  description: Preserve old events and explicitly distinguish source versions, hash
    formats and unverified times in any append-only clarification. Do not invent historical
    UTC values or describe the 49cf extraction hash as the raw PDF hash.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:003506
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/allisonella_medium.yaml
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
- Preserved komodoMediaList retrieval failed (403). No content is claimed from this
  attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006
  formulation provide the required source comparison; the LB page cannot establish
  membership in this recipe.
- Preserved komodo1006 retrieval failed (403). No content is claimed from this attempt.
  Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006
  formulation provide the required source comparison; the LB page cannot establish
  membership in this recipe.
- Preserved komodoDetail1006 retrieval failed (403). No content is claimed from this
  attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006
  formulation provide the required source comparison; the LB page cannot establish
  membership in this recipe.
- Preserved lbMillerNotes retrieval failed (None). No content is claimed from this
  attempt. Exact DSMZ1006, current API and the separately hashed archived public KOMODO1006
  formulation provide the required source comparison; the LB page cannot establish
  membership in this recipe.
- The primary and archived public provider recipe are available, so failed present
  KOMODO/LB requests do not make the required formulation review partial. Their failures
  and original successful archive access time remain separate.
- Provider 1004 mL, stock 1000 mL and input-volume sums are nominal declarations/context,
  not measured final volumes. No acid-density conversion, new molarity, gas amount
  or unspecified autoclave cycle is asserted.
- Full historical archived-node reading is attributed to the specialist preflight
  and independent audit, with exact owner reconstruction hashes. Root reading of every
  repeated archived explanation is not claimed.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-024
- generated-medium
```
