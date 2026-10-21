# Source and formulation review: acidic_diluted_asm_medium (CultureMech:010266)

- Review: 20261021T105424Z-culturemech-010266-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T10:48:42Z
- Finished UTC: 2026-10-21T10:54:24Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 815 / TOGO M850 identity is supported, but three stock recipes are flattened into the receiving medium and their additions use mass-concentration units. The generated water sum is also stale relative to the owner. Source preparation, supplied hydrate forms and pH-variant boundaries require curation; direct current JCM 816 content remains unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 162; batch 017 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding sixteen task batches contain 160 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 162 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010266 | data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml | generated | acidic_diluted_asm_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010266 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010266 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/162/strict.tsv |
| validate-terms | passed | True | CultureMech:010266 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010266 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010266 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: jcm816 | unavailable | True | CultureMech:010266 | The current exact JCM 816 URL returned HTTP 200 with Nothing found, not a recipe. TOGO M851 and the reciprocal local PH_VARIANT links support the pH 6.7 wrapper, but direct current collection confirmation of that linked variant remains unavailable. The complete JCM 815 base formulation is accessible and assessed. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010266.

The four documented recipes completed; interpret the scope of each separately.

### Generated base identity and distinct linked variant

identity: supported. Targets: CultureMech:010266.

The exact base is TOGO M850 / JCM 815 / CultureMech:010266. The owner links PH_VARIANT CultureMech:010267 at the exact M851 path; the child reciprocally names this base. No pH 6.7 child condition is applied to the base. The stock identifier mediadive.solution:4768 resolves to the matching phosphate recipe.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:010266.

35 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "input": "target",
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "source_stage": "Basal solvent, separate from each stock solvent",
    "existing": {
      "value": "4.0",
      "unit": "G_PER_L"
    },
    "proposed": "Represent basal 1 L water and separate each stock water quantity; neither 4 g/L nor collapsed 1 g/L represents the source.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 basal table, distilled-water row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "source_amount": {
      "value": 1,
      "unit": "L"
    }
  },
  {
    "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "source_stage": "Basal solvent, separate from each stock solvent",
    "existing": {
      "value": "1.0",
      "unit": "G_PER_L"
    },
    "proposed": "Represent basal 1 L water and separate each stock water quantity; neither 4 g/L nor collapsed 1 g/L represents the source.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 basal table, distilled-water row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "source_amount": {
      "value": 1,
      "unit": "L"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[1].concentration",
    "decision": "correct",
    "source_stage": "Basal batch before stock additions and acid adjustment",
    "existing": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": "Retain the source batch mass with its stage and 1 L water basis; do not assert a measured final-medium g/L from solvent volume alone.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 basal table, exact MgSO4・7H2O row",
        "exact_source_quote": "MgSO 4 ·7H 2 O 0.1 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[2].concentration",
    "decision": "correct",
    "source_stage": "Basal batch before stock additions and acid adjustment",
    "existing": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "proposed": "Retain the source batch mass with its stage and 1 L water basis; do not assert a measured final-medium g/L from solvent volume alone.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 basal table, exact CaCl2・2H2O row",
        "exact_source_quote": "CaCl 2 ·2H 2 O 0.02 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[3].concentration",
    "decision": "correct",
    "source_stage": "Basal batch before stock additions and acid adjustment",
    "existing": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": "Retain the source batch mass with its stage and 1 L water basis; do not assert a measured final-medium g/L from solvent volume alone.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 basal table, exact NH4Cl row",
        "exact_source_quote": "NH 4 Cl 0.1 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[4].concentration",
    "decision": "not_quantified",
    "source_stage": "Titrant dose during pH adjustment",
    "existing": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "proposed": "The amount of titrant is not fixed; keep variable dose while separately recording its 1 N strength and target pH.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 completion paragraph",
        "exact_source_quote": "adjust pH to 3.0 with sterile 1 N HCl solution.",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"HCl\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"N\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[5].concentration",
    "decision": "correct",
    "source_stage": "Gas added to the culture-bottle headspace",
    "existing": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "proposed": "Replace the unqualified variable gas representation with the explicit 100 ml headspace addition per specified bottle; do not convert it to a liquid concentration.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 completion paragraph",
        "exact_source_quote": "Add 100 ml methane gas (filter-sterilized) into the head space of the culture bottle through a syringe.",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"Methane gas\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "source_amount": {
      "value": 100,
      "unit": "ml gas per specified bottle"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[6].concentration",
    "decision": "correct",
    "source_stage": "Trace element solution composition, not receiving-medium ingredient",
    "existing": {
      "value": "0.04",
      "unit": "G_PER_L"
    },
    "proposed": "Move the unchanged source mass to its named stock recipe and retain the source-specific 1 L water basis. Do not use the stock mass concentration as a final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Trace element solution subsection, exact ingredient row",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 0.04 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.04,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "source_stage": "Trace element solution composition, not receiving-medium ingredient",
    "existing": {
      "value": "0.015",
      "unit": "G_PER_L"
    },
    "proposed": "Move the unchanged source mass to its named stock recipe and retain the source-specific 1 L water basis. Do not use the stock mass concentration as a final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Trace element solution subsection, exact ingredient row",
        "exact_source_quote": "H 3 BO 3 0.015 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 0.015,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "source_stage": "Trace element solution composition, not receiving-medium ingredient",
    "existing": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "proposed": "Move the unchanged source mass to its named stock recipe and retain the source-specific 1 L water basis. Do not use the stock mass concentration as a final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Trace element solution subsection, exact ingredient row",
        "exact_source_quote": "MnCl 2 ·4H 2 O 0.02 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "source_stage": "Trace element solution composition, not receiving-medium ingredient",
    "existing": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "proposed": "Move the unchanged source mass to its named stock recipe and retain the source-specific 1 L water basis. Do not use the stock mass concentration as a final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Trace element solution subsection, exact ingredient row",
        "exact_source_quote": "CoCl 2 ·6H 2 O 0.05 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 0.05,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "source_stage": "Trace element solution composition, not receiving-medium ingredient",
    "existing": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "proposed": "Move the unchanged source mass to its named stock recipe and retain the source-specific 1 L water basis. Do not use the stock mass concentration as a final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Trace element solution subsection, exact ingredient row",
        "exact_source_quote": "NiCl 2 ·6H 2 O 0.01 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "source_stage": "Trace element solution composition, not receiving-medium ingredient",
    "existing": {
      "value": "0.4",
      "unit": "G_PER_L"
    },
    "proposed": "Move the unchanged source mass to its named stock recipe and retain the source-specific 1 L water basis. Do not use the stock mass concentration as a final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Trace element solution subsection, exact ingredient row",
        "exact_source_quote": "ZnSO 4 ·7H 2 O 0.4 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "source_stage": "Trace element solution composition, not receiving-medium ingredient",
    "existing": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "proposed": "Move the unchanged source mass to its named stock recipe and retain the source-specific 1 L water basis. Do not use the stock mass concentration as a final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Trace element solution subsection, exact ingredient row",
        "exact_source_quote": "CuSO 4 ·5H 2 O 0.2 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[7]",
        "exact_source_quote": "\"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "source_stage": "Trace element solution composition, not receiving-medium ingredient",
    "existing": {
      "value": "0.25",
      "unit": "G_PER_L"
    },
    "proposed": "Move the unchanged source mass to its named stock recipe and retain the source-specific 1 L water basis. Do not use the stock mass concentration as a final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Trace element solution subsection, exact ingredient row",
        "exact_source_quote": "EDTA·2Na 0.25 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[8]",
        "exact_source_quote": "\"component_name\": \"EDTA・2Na\",\n          \"volume\": 0.25,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "source_stage": "Iron stock solution composition, not receiving-medium ingredient",
    "existing": {
      "value": "4.5",
      "unit": "G_PER_L"
    },
    "proposed": "Move the unchanged source mass to its named stock recipe and retain the source-specific 1 L water basis. Do not use the stock mass concentration as a final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Iron stock solution subsection, exact ingredient row",
        "exact_source_quote": "EDTA·Fe(III) 4.5 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"EDTA・Fe(III)\",\n          \"volume\": 4.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[15].concentration",
    "decision": "correct",
    "source_stage": "Phosphate buffer stock solution composition, not receiving-medium ingredient",
    "existing": {
      "value": "37.425",
      "unit": "G_PER_L"
    },
    "proposed": "Move the unchanged source mass to its named stock recipe and retain the source-specific 1 L water basis. Do not use the stock mass concentration as a final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Phosphate buffer stock solution subsection, exact ingredient row",
        "exact_source_quote": "KH 2 PO 4 37.425 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[4].items[1]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 37.425,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ingredients[16].concentration",
    "decision": "correct",
    "source_stage": "Phosphate buffer stock solution composition, not receiving-medium ingredient",
    "existing": {
      "value": "48.95",
      "unit": "G_PER_L"
    },
    "proposed": "Move the unchanged source mass to its named stock recipe and retain the source-specific 1 L water basis. Do not use the stock mass concentration as a final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Phosphate buffer stock solution subsection, exact ingredient row",
        "exact_source_quote": "Na 2 HPO 4 ·2H 2 O 48.950 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[4].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2HPO4・2H2O\",\n          \"volume\": 48.95,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "solutions[0].concentration",
    "decision": "correct",
    "source_stage": "Basal mixture before autoclaving",
    "existing": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": "Represent the source ml addition per prepared batch, not G_PER_L. Retain a typed/reference-resolved or inline stock recipe.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 exact stock-addition row",
        "exact_source_quote": "Trace element solution (see below) 0.1 ml",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"Trace element solution (see below)\",\n          \"volume\": 0.1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "source_amount": {
      "value": 0.1,
      "unit": "ml"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "solutions[1].concentration",
    "decision": "correct",
    "source_stage": "Basal mixture before autoclaving",
    "existing": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": "Represent the source ml addition per prepared batch, not G_PER_L. Retain a typed/reference-resolved or inline stock recipe.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 exact stock-addition row",
        "exact_source_quote": "Iron stock solution (see below) 0.1 ml",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"Iron stock solution (see below)\",\n          \"volume\": 0.1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "source_amount": {
      "value": 0.1,
      "unit": "ml"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "solutions[2].concentration",
    "decision": "correct",
    "source_stage": "After cooling, separately autoclaved phosphate stock",
    "existing": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "proposed": "Represent the source ml addition per prepared batch, not G_PER_L. Retain a typed/reference-resolved or inline stock recipe.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 exact stock-addition row",
        "exact_source_quote": "Phosphate buffer stock solution 2.0 ml",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Phosphate buffer stock solution\",\n          \"volume\": 2,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "source_amount": {
      "value": 2,
      "unit": "ml"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "solutions (source-only stock solvent)",
    "decision": "add",
    "source_stage": "Trace element solution preparation",
    "existing": null,
    "proposed": "Keep this 1 L solvent only within its own stock. It must not be summed with the basal water or other stock batches.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Trace element solution subsection, distilled-water row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "source_amount": {
      "value": 1,
      "unit": "L"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "solutions (source-only stock solvent)",
    "decision": "add",
    "source_stage": "Iron stock solution preparation",
    "existing": null,
    "proposed": "Keep this 1 L solvent only within its own stock. It must not be summed with the basal water or other stock batches.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Iron stock solution subsection, distilled-water row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "source_amount": {
      "value": 1,
      "unit": "L"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "solutions (source-only stock solvent)",
    "decision": "add",
    "source_stage": "Phosphate buffer stock solution preparation",
    "existing": null,
    "proposed": "Keep this 1 L solvent only within its own stock. It must not be summed with the basal water or other stock batches.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 Phosphate buffer stock solution subsection, distilled-water row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[4].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "source_amount": {
      "value": 1,
      "unit": "L"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "ph_value",
    "decision": "add",
    "source_stage": "Completed base medium before aliquoting",
    "existing": null,
    "proposed": "Record pH 3.0 as the target for the base, distinct from child pH 6.7.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 preparation paragraph or qualified page instruction",
        "exact_source_quote": "adjust pH to 3.0",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "preparation_steps (adjustment-stock strength)",
    "decision": "add",
    "source_stage": "Sterile HCl titrant",
    "existing": null,
    "proposed": "Record 1 N strength; no fixed titrant volume or molar conversion is inferred.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 preparation paragraph or qualified page instruction",
        "exact_source_quote": "sterile 1 N HCl solution",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "preparation_steps (liquid aliquot)",
    "decision": "add",
    "source_stage": "Bottle dispensing",
    "existing": null,
    "proposed": "Record 20 ml liquid aliquots in the specified bottle context.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 preparation paragraph or qualified page instruction",
        "exact_source_quote": "distribute 20 ml-aliquots of the medium",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "preparation_steps (bottle volume)",
    "decision": "add",
    "source_stage": "Bottle dispensing",
    "existing": null,
    "proposed": "Record vessel nominal volume 120 ml; it is not a recipe-volume denominator.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 preparation paragraph or qualified page instruction",
        "exact_source_quote": "sterile 120 ml-serum bottles",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "preparation_steps (default sterilization temperature)",
    "decision": "add",
    "source_stage": "Site default, only where no specific alternative is stated",
    "existing": null,
    "proposed": "Retain 121°C with the explicit unless-otherwise-stated qualifier; methane remains filter-sterilized.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 preparation paragraph or qualified page instruction",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml"
    ],
    "field_path": "preparation_steps (default sterilization duration)",
    "decision": "add",
    "source_stage": "Site default, only where no specific alternative is stated",
    "existing": null,
    "proposed": "Retain 15 min with the explicit unless-otherwise-stated qualifier.",
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Medium815 preparation paragraph or qualified page instruction",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml",
    "field_path": "composition[0].concentration",
    "ingredient": "KH2PO4",
    "existing": {
      "value": "37.425",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "Independent solution4768 stock composition only",
    "basis": "Provider-declared 1000 ml stock basis; the water row is a batch dose. No receiving-medium g/L is implied.",
    "source_snippets": [
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"KH2PO4\",\n                \"compound_id\": 11,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 37.425,\n                \"unit\": \"g\",\n                \"g_l\": 37.425,\n                \"mmol_l\": 275.01,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      }
    ],
    "proposed": "Retain exact existing source evidence in the stock; independently attach the target stock-addition evidence."
  },
  {
    "input": "data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml",
    "field_path": "composition[1].concentration",
    "ingredient": "Na2HPO4 x 2 H2O",
    "existing": {
      "value": "48.95",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "Independent solution4768 stock composition only",
    "basis": "Provider-declared 1000 ml stock basis; the water row is a batch dose. No receiving-medium g/L is implied.",
    "source_snippets": [
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Na2HPO4 x 2 H2O\",\n                \"compound_id\": 181,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 48.95,\n                \"unit\": \"g\",\n                \"g_l\": 48.95,\n                \"mmol_l\": 344.818,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      }
    ],
    "proposed": "Retain exact existing source evidence in the stock; independently attach the target stock-addition evidence."
  },
  {
    "input": "data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml",
    "field_path": "composition[2].concentration",
    "ingredient": "Distilled water",
    "existing": {
      "value": "1",
      "unit": "L"
    },
    "decision": "verified",
    "source_stage": "Independent solution4768 stock composition only",
    "basis": "Provider-declared 1000 ml stock basis; the water row is a batch dose. No receiving-medium g/L is implied.",
    "source_snippets": [
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      }
    ],
    "proposed": "Retain exact existing source evidence in the stock; independently attach the target stock-addition evidence."
  },
  {
    "input": "data/normalized_yaml/bacterial/TOGO_M851_Diluted_ASM_Medium.yaml",
    "field_path": "ph_value",
    "existing": 6.7,
    "decision": "evidence_only",
    "source_stage": "Separate TOGO M851 / JCM816 child",
    "proposed": "Retain pH 6.7 with exact provider linkage; direct current JCM816 page is unavailable. Do not apply this pH to the base.",
    "source_snippets": [
      {
        "source_key": "togoM851",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M851",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "Prepare Medium No. [815] and adjust pH to 6.7.",
        "snapshot_sha256": "69876dcbc941f2bb1c9b552f2eeacbc978ad69460d519baddccdb69a1e224e8b"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/TOGO_M851_Diluted_ASM_Medium.yaml",
    "field_path": "solutions[0].concentration",
    "existing": {
      "value": "1000",
      "unit": "ML_PER_L"
    },
    "decision": "correct",
    "source_stage": "Prepared-parent medium quantity in separate child",
    "proposed": "Provider gives 1 L prepared parent, not an independently supported per-final-litre dose. Preserve the source batch quantity and explicit child scope.",
    "source_snippets": [
      {
        "source_key": "togoM851",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M851",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"ACIDIC DILUTED ASM MEDIUM (see Medium [M850])\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "69876dcbc941f2bb1c9b552f2eeacbc978ad69460d519baddccdb69a1e224e8b"
      }
    ]
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:010266.

15 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 15/17 primary and 5/17 secondary instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 17: primary 88.24%; secondary 29.41%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:010266.

29 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### All source preparation stages and dose bases

completeness: concern. Targets: CultureMech:010266.

The source distinguishes basal autoclaving, later separately autoclaved phosphate, sterile 1 N HCl adjustment to pH 3.0, 20 ml aliquots in 120 ml bottles and 100 ml filter-sterilized methane to headspace. Both local layers omit preparation and base pH. Numeric quantities and the qualified default sterilization instruction are in the inventory; no final liquid volume or gas-to-liquid concentration is derived.

### Defined chemistry versus inherited COMPLEX/UNDEFINED labels

scope: concern. Targets: CultureMech:010266.

The inspected recipe is a specified mineral/chelate/gas formulation without yeast extract, peptone or another stated complex biological ingredient. COMPLEX / UNDEFINED lacks source-specific justification; exact chelate/form resolution and proper stock separation should precede choosing replacement enum values. LIQUID is supported. Generic category/application metadata does not establish growth for a named strain.

## Findings

### f1: Three stock recipes and four solvent quantities are conflated with the receiving medium

blocker / open / confirmed; issue key: culturemech.010266.stock-flattening-water.

Eleven direct ingredient entries are actually eight trace-stock solutes, one iron-stock solute and two phosphate-stock solutes. Their stock amounts appear as receiving-medium G_PER_L values beside empty stock nodes. The target also sums four distinct 1 L source water batches into 4 G_PER_L; the owner’s later collapse to 1 G_PER_L remains dimensionally and stage-wise wrong. This changes the represented formulation, despite passing schema checks.

### f2: Stock-addition volumes are represented as mass concentrations

major / open / confirmed; issue key: culturemech.010266.stock-dose-units.

Trace and iron stocks are each 0.1 ml per prepared batch; phosphate is 2 ml added after cooling. All three local nodes instead use G_PER_L. The basal salt source masses likewise require their source batch basis rather than a measured final-volume assumption.

### f3: Three hydrate labels map to nonhydrate structures and EDTA specificity is unproven

major / open / confirmed; issue key: culturemech.010266.supplied-form-mismatch.

The source specifies cobalt chloride hexahydrate, nickel chloride hexahydrate and disodium hydrogenphosphate dihydrate, but CHEBI:35696, CHEBI:34887 and CHEBI:34683 carry formulas without hydration water. EDTA·2Na is mapped to explicitly anhydrous CHEBI:64734 although the source does not resolve that hydration state. Exact canonical labels pass while supplied forms remain wrong or over-specific. The independent phosphate stock already uses a dihydrate identity; its concentration evidence does not validate the target’s nonhydrate term.

### f4: Source pH, staged sterilization and quantified methane context are absent

major / open / confirmed; issue key: culturemech.010266.preparation-and-gas.

Both layers omit the full preparation and base pH. Methane is VARIABLE even though the exact source provides a 100 ml bottle-headspace addition, with a 20 ml liquid aliquot and 120 ml vessel context. HCl dose is genuinely variable, but its 1 N stock strength and target pH 3.0 are missing. These quantities must not be collapsed into final liquid concentration.

### f5: Generated target omits the maintained pH-variant relationship

minor / open / confirmed; issue key: culturemech.010266.variant-link-stale.

The normalized owner’s September reciprocal PH_VARIANT link to CultureMech:010267 is missing from the August generated target. The provider supports a distinct pH 6.7 child; it must remain separate from the pH 3.0 base. Current JCM816 source content is unavailable and is not replaced with an invented primary assertion.

### f6: COMPLEX and UNDEFINED lack formulation-specific support

minor / open / confirmed; issue key: culturemech.010266.classification-evidence.

The primary describes a specified mineral/chelate/gas recipe and separately defined stocks. No complex biological mixture is stated. The inherited labels should be reassessed with proper stock and chemical-form representation; no replacement classification is inferred solely from a validator pass.

## Recommended Actions And Acceptance Checks

### a1

Restore the three scoped stock recipes and basal solvent in the normalized owner; preserve exact source labels/amounts and typed phosphate identity, then regenerate via maintained stage-aware import/merge paths. Do not sum stock preparation water or infer final concentrations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore ml stock doses with preparation-stage evidence and source batch masses/basis. Keep stock composition concentration distinct from receiving-medium concentration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Correct the supported hydrate identities after exact term verification; retain EDTA disodium identity without asserting an unverified hydrate state. Keep HCl solution strength and Fe(III)-EDTA identity separately scoped; do not invent unresolved links.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Restore the exact source preparation, sterile adjustment/gas stages and qualified general autoclave context. Record bottle and headspace quantities at their own stages, retaining an unquantified titrant dose.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Preserve the source-qualified reciprocal variant relation when regenerating; retain the direct-primary access limit and do not overwrite the base pH with the child condition.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Reassess and evidence the classification after resolving stock/chelate representation; preserve the supported liquid state and avoid organism-growth claims from the medium name.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch017/162/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/162/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml:1:id: CultureMech:010266<br>./data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml:1:id: CultureMech:010266<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch017/source-preflight-bound/162/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 21 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815; Medium 815, complete basal and three stock tables, preparation paragraphs and qualified site sterilization instruction | supports | All receiving-medium, trace-element, iron and phosphate stock stages inspected independently; water additions do not establish measured final volume. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850; $.meta; $.components[0:5]; $.comments[0:2] | supports | Exact source accession JCM_M815, four separately scoped 1 L water quantities, three stock doses, adjustment stock and bottle/headspace instructions agree with the primary. |
| phosphate-provider | https://mediadive.dsmz.de/rest/solution/4768; $.data.id/name/volume; $.data.recipe[0:3] | supports | The exact 4768 stock has the same two phosphate compounds and 1000 ml water basis; its concentrations apply within the stock, not the receiving medium. |
| variant-provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M851; $.meta; $.components[0].items[0]; $.comments[1] | supports | TOGO M851 explicitly prepares JCM 815 then adjusts pH to 6.7; this is a distinct PH_VARIANT, not the pH 3.0 base. |
| jcm816-attempt | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=816; Preserved exact public retrieval result | context_only | The current exact JCM 816 URL returned HTTP 200 with Nothing found, not a recipe. TOGO M851 and the reciprocal local PH_VARIANT links support the pH 6.7 wrapper, but direct current collection confirmation of that linked variant remains unavailable. The complete JCM 815 base formulation is accessible and assessed. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch017/162/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64734; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:64734 resolves to EDTA disodium salt (anhydrous). Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| stock-dihydrate-term | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258; Exact OLS ID/label and supplied-form annotations | supports | The standalone stock explicitly represents disodium hydrogenphosphate dihydrate. This term metadata supports comparison of chemical form; it is not evidence for a receiving-medium amount. |
| dependency-stock | data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml; Entire independent SolutionRecipe, composition/evidence/history and legacy placeholder flags | context_only | All three composition evidence objects literally match current solution4768 raw bytes/hash, with correct stock-only qualifications. The legacy See source for composition ingredient and incomplete_composition flag are not the actual stock composition and are not transferred into the target. |
| dependency-variant | data/normalized_yaml/bacterial/TOGO_M851_Diluted_ASM_Medium.yaml; Entire child record, typed parent, preparation, references and history | context_only | Exact parent path/ID and pH-variant relationship resolve. The wrapper’s 1000 ML_PER_L representation is not independently established by a provider 1 L batch row. This is dependency context only, not a second full record review. |
| history-metadata | data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 14, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml", "events": 15, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current _extract_primary_components, _solution_from_item and local-stock functions separate source stages; current duplicate cleanup avoids summing conflicting values. These current routines were not executed or historically replayed. The August target predates September owner repair/link events. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current _extract_primary_components, _solution_from_item and local-stock functions separate source stages; current duplicate cleanup avoids summing conflicting values. These current routines were not executed or historically replayed. The August target predates September owner repair/link events. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current _extract_primary_components, _solution_from_item and local-stock functions separate source stages; current duplicate cleanup avoids summing conflicting values. These current routines were not executed or historically replayed. The August target predates September owner repair/link events. |
| historical-writer-search | /private/tmp/culturemech-record-review-20261019-batch-017; Exact basename search with ignored and hidden files included | context_only | The historical repair_jcm_reference_wrappers_score40.py named in the September owner/child events is not present in this owned tree. Current code is not substituted as proof of the historical transformation. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The current exact JCM 816 URL returned HTTP 200 with Nothing found, not a recipe. TOGO M851 and the reciprocal local PH_VARIANT links support the pH 6.7 wrapper, but direct current collection confirmation of that linked variant remains unavailable. The complete JCM 815 base formulation is accessible and assessed.
- No measured final-medium volume, methane partial pressure, dissolved-gas concentration, growth temperature, strain performance or complete chelate hydration specification was inferred. The independent stock and child records were inspected as dependencies only. Current code and history establish context, not proof of the historical writer execution.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T105424Z-culturemech-010266-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidic_diluted_asm_medium (CultureMech:010266)'
started_at: '2026-10-21T10:48:42Z'
finished_at: '2026-10-21T10:54:24Z'
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
summary: JCM 815 / TOGO M850 identity is supported, but three stock recipes are flattened
  into the receiving medium and their additions use mass-concentration units. The
  generated water sum is also stale relative to the owner. Source preparation, supplied
  hydrate forms and pH-variant boundaries require curation; direct current JCM 816
  content remains unavailable.
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
  - path: data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml
    sha256: f9be9417bf9f537e2022d80a21dc8242252e05e1236942a2279754e15710baa2
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
    sha256: e68c62bea1f376623654e0f5235d433a3380d9c19fea05061eb2d13de8ec9678
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M851_Diluted_ASM_Medium.yaml
    sha256: aab16d49d90f093f69cbf00a0f2f63f1a184c27f9d5bf837d35481168f4a1826
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml
    sha256: 0616e7b8dfeb6a49f26c17de757518844bd43b65e7255012e1e58da144e2dc91
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
  - path: scripts/repair_jcm_parent_wrappers_score20.py
    sha256: 422fbced1f73eb86835f6d061e7e7620beecf9e456554c0a897138d286db277d
    role: context
  - path: scripts/repair_jcm_wrappers_direct_score20.py
    sha256: e0c3ad4ec2e015bf9b8a8870fdcd67c513c473c6fd3342d7610769b106cbd188
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
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 162; batch 017 item 2 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding sixteen task batches
    contain 160 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 162 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010266
targets:
- target_id: CultureMech:010266
  path: data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml
  label: acidic_diluted_asm_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010266
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch017/162/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/162/strict.tsv"
  target_ids:
  - CultureMech:010266
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010266
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010266
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
  - CultureMech:010266
- check_id: jcm816-source-access
  name: 'Exact source content access: jcm816'
  required: true
  status: unavailable
  summary: The current exact JCM 816 URL returned HTTP 200 with Nothing found, not
    a recipe. TOGO M851 and the reciprocal local PH_VARIANT links support the pH 6.7
    wrapper, but direct current collection confirmation of that linked variant remains
    unavailable. The complete JCM 815 base formulation is accessible and assessed.
  target_ids:
  - CultureMech:010266
  evidence_ids:
  - jcm816-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:54:21Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:54:21Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:08.376848Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch017/162/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:09.752533Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/162/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:11.201694Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:12.466486Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T10:54:21Z'
  support: supports
  summary: './data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml:1:id: CultureMech:010266

    ./data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml:1:id:
    CultureMech:010266

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/source-preflight-bound/162/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T10:54:21Z'
  support: supports
  summary: 21 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 1bfc2943bd333916e581aa6d9bee06bbb043d5fc373ea8405e7b70593e5d9100
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815
  locator: Medium 815, complete basal and three stock tables, preparation paragraphs
    and qualified site sterilization instruction
  accessed_at: '2026-10-21T10:33:41.274966Z'
  support: supports
  summary: All receiving-medium, trace-element, iron and phosphate stock stages inspected
    independently; water additions do not establish measured final volume.
  snapshot_sha256: 21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850
  locator: $.meta; $.components[0:5]; $.comments[0:2]
  accessed_at: '2026-10-21T10:33:39.735634Z'
  support: supports
  summary: Exact source accession JCM_M815, four separately scoped 1 L water quantities,
    three stock doses, adjustment stock and bottle/headspace instructions agree with
    the primary.
  snapshot_sha256: 034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b
- evidence_id: phosphate-provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4768
  locator: $.data.id/name/volume; $.data.recipe[0:3]
  accessed_at: '2026-10-21T10:33:38.860496Z'
  support: supports
  summary: The exact 4768 stock has the same two phosphate compounds and 1000 ml water
    basis; its concentrations apply within the stock, not the receiving medium.
  snapshot_sha256: 8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67
- evidence_id: variant-provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M851
  locator: $.meta; $.components[0].items[0]; $.comments[1]
  accessed_at: '2026-10-21T10:33:39.770947Z'
  support: supports
  summary: TOGO M851 explicitly prepares JCM 815 then adjusts pH to 6.7; this is a
    distinct PH_VARIANT, not the pH 3.0 base.
  quote: Prepare Medium No. [815] and adjust pH to 6.7.
  snapshot_sha256: 69876dcbc941f2bb1c9b552f2eeacbc978ad69460d519baddccdb69a1e224e8b
- evidence_id: jcm816-attempt
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=816
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T10:33:41.433440Z'
  support: context_only
  summary: The current exact JCM 816 URL returned HTTP 200 with Nothing found, not
    a recipe. TOGO M851 and the reciprocal local PH_VARIANT links support the pH 6.7
    wrapper, but direct current collection confirmation of that linked variant remains
    unavailable. The complete JCM 815 base formulation is accessible and assessed.
  snapshot_sha256: 89ee7c81a4cbb244a093138d3cbdcf32873c6c205b28b9e8920d455650600afb
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/162/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T10:54:21Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: aa5a925e3289a7165d348f34ba0f1d3ab4ac83e5bc726e6c31735e6f1728006e
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
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
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
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
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
- evidence_id: chebi64734
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64734
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.449302Z'
  support: supports
  summary: CHEBI:64734 resolves to EDTA disodium salt (anhydrous). Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 95b7557b1867dcce37a69714dbad0a6a6a6c11c66dde39c6793a2307a7fb0e1c
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
  accessed_at: '2026-10-21T10:54:21Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17883": [{"label": "HCl", "match_type":
    "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id":
    "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: stock-dihydrate-term
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258
  locator: Exact OLS ID/label and supplied-form annotations
  accessed_at: '2026-10-21T09:28:27.054091Z'
  support: supports
  summary: The standalone stock explicitly represents disodium hydrogenphosphate dihydrate.
    This term metadata supports comparison of chemical form; it is not evidence for
    a receiving-medium amount.
  snapshot_sha256: f6c74e6e0b876aadf2fe47494521d320abb79244773bf4c44da7b288b1e27319
- evidence_id: dependency-stock
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml
  locator: Entire independent SolutionRecipe, composition/evidence/history and legacy
    placeholder flags
  accessed_at: '2026-10-21T10:54:21Z'
  support: context_only
  summary: All three composition evidence objects literally match current solution4768
    raw bytes/hash, with correct stock-only qualifications. The legacy See source
    for composition ingredient and incomplete_composition flag are not the actual
    stock composition and are not transferred into the target.
  snapshot_sha256: 0616e7b8dfeb6a49f26c17de757518844bd43b65e7255012e1e58da144e2dc91
- evidence_id: dependency-variant
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M851_Diluted_ASM_Medium.yaml
  locator: Entire child record, typed parent, preparation, references and history
  accessed_at: '2026-10-21T10:54:21Z'
  support: context_only
  summary: Exact parent path/ID and pH-variant relationship resolve. The wrapper’s
    1000 ML_PER_L representation is not independently established by a provider 1
    L batch row. This is dependency context only, not a second full record review.
  snapshot_sha256: aab16d49d90f093f69cbf00a0f2f63f1a184c27f9d5bf837d35481168f4a1826
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIC_DILUTED_ASM_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T10:54:21Z'
  support: context_only
  summary: '[{"input": "target", "events": 14, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml", "events":
    15, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:54:21Z'
  support: context_only
  summary: Current _extract_primary_components, _solution_from_item and local-stock
    functions separate source stages; current duplicate cleanup avoids summing conflicting
    values. These current routines were not executed or historically replayed. The
    August target predates September owner repair/link events.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:54:21Z'
  support: context_only
  summary: Current _extract_primary_components, _solution_from_item and local-stock
    functions separate source stages; current duplicate cleanup avoids summing conflicting
    values. These current routines were not executed or historically replayed. The
    August target predates September owner repair/link events.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:54:21Z'
  support: context_only
  summary: Current _extract_primary_components, _solution_from_item and local-stock
    functions separate source stages; current duplicate cleanup avoids summing conflicting
    values. These current routines were not executed or historically replayed. The
    August target predates September owner repair/link events.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: historical-writer-search
  kind: search
  reference: /private/tmp/culturemech-record-review-20261019-batch-017
  locator: Exact basename search with ignored and hidden files included
  accessed_at: '2026-10-21T10:54:21Z'
  support: context_only
  summary: The historical repair_jcm_reference_wrappers_score40.py named in the September
    owner/child events is not present in this owned tree. Current code is not substituted
    as proof of the historical transformation.
  search_scope: rg --no-ignore --hidden --files -g repair_jcm_reference_wrappers_score40.py
    over the complete owned batch017 checkout including ignored files.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010266
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Generated base identity and distinct linked variant
  outcome: supported
  summary: The exact base is TOGO M850 / JCM 815 / CultureMech:010266. The owner links
    PH_VARIANT CultureMech:010267 at the exact M851 path; the child reciprocally names
    this base. No pH 6.7 child condition is applied to the base. The stock identifier
    mediadive.solution:4768 resolves to the matching phosphate recipe.
  target_ids:
  - CultureMech:010266
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - variant-provider
  - phosphate-provider
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 35 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:010266
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"input\": \"target\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Basal solvent, separate\
    \ from each stock solvent\",\n    \"existing\": {\n      \"value\": \"4.0\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Represent basal 1 L\
    \ water and separate each stock water quantity; neither 4 g/L nor collapsed 1\
    \ g/L represents the source.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 basal table, distilled-water row\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1.0 L\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"source_amount\": {\n      \"value\": 1,\n      \"unit\"\
    : \"L\"\n    }\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"decision\": \"\
    correct\",\n    \"source_stage\": \"Basal solvent, separate from each stock solvent\"\
    ,\n    \"existing\": {\n      \"value\": \"1.0\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"proposed\": \"Represent basal 1 L water and separate each stock\
    \ water quantity; neither 4 g/L nor collapsed 1 g/L represents the source.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 basal table, distilled-water row\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1.0 L\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"source_amount\": {\n      \"value\": 1,\n      \"unit\"\
    : \"L\"\n    }\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[1].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Basal batch before stock additions and\
    \ acid adjustment\",\n    \"existing\": {\n      \"value\": \"0.1\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Retain the source batch mass\
    \ with its stage and 1 L water basis; do not assert a measured final-medium g/L\
    \ from solvent volume alone.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 basal table, exact MgSO4・7H2O row\"\
    ,\n        \"exact_source_quote\": \"MgSO 4 ·7H 2 O 0.1 g\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4・7H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[2].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Basal batch before stock additions and\
    \ acid adjustment\",\n    \"existing\": {\n      \"value\": \"0.02\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Retain the source batch mass\
    \ with its stage and 1 L water basis; do not assert a measured final-medium g/L\
    \ from solvent volume alone.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 basal table, exact CaCl2・2H2O row\"\
    ,\n        \"exact_source_quote\": \"CaCl 2 ·2H 2 O 0.02 g\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 0.02,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[3].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Basal batch before stock additions and\
    \ acid adjustment\",\n    \"existing\": {\n      \"value\": \"0.1\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Retain the source batch mass\
    \ with its stage and 1 L water basis; do not assert a measured final-medium g/L\
    \ from solvent volume alone.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 basal table, exact NH4Cl row\",\n \
    \       \"exact_source_quote\": \"NH 4 Cl 0.1 g\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[4].concentration\",\n    \"decision\"\
    : \"not_quantified\",\n    \"source_stage\": \"Titrant dose during pH adjustment\"\
    ,\n    \"existing\": {\n      \"value\": \"variable\",\n      \"unit\": \"VARIABLE\"\
    \n    },\n    \"proposed\": \"The amount of titrant is not fixed; keep variable\
    \ dose while separately recording its 1 N strength and target pH.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm815\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\",\n        \"source_locator\"\
    : \"Medium815 completion paragraph\",\n        \"exact_source_quote\": \"adjust\
    \ pH to 3.0 with sterile 1 N HCl solution.\",\n        \"snapshot_sha256\": \"\
    21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n        \"\
    parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"HCl\\\",\\n          \\\"conc_value\\\": 1,\\\
    n          \\\"conc_unit\\\": \\\"N\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[5].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Gas added to the culture-bottle headspace\"\
    ,\n    \"existing\": {\n      \"value\": \"variable\",\n      \"unit\": \"VARIABLE\"\
    \n    },\n    \"proposed\": \"Replace the unqualified variable gas representation\
    \ with the explicit 100 ml headspace addition per specified bottle; do not convert\
    \ it to a liquid concentration.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 completion paragraph\",\n        \"\
    exact_source_quote\": \"Add 100 ml methane gas (filter-sterilized) into the head\
    \ space of the culture bottle through a syringe.\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Methane gas\\\"\",\n        \"snapshot_sha256\"\
    : \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\n     \
    \ }\n    ],\n    \"source_amount\": {\n      \"value\": 100,\n      \"unit\":\
    \ \"ml gas per specified bottle\"\n    }\n  },\n  {\n    \"input\": [\n      \"\
    target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[6].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element solution composition, not\
    \ receiving-medium ingredient\",\n    \"existing\": {\n      \"value\": \"0.04\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Move the unchanged\
    \ source mass to its named stock recipe and retain the source-specific 1 L water\
    \ basis. Do not use the stock mass concentration as a final-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Trace element solution subsection,\
    \ exact ingredient row\",\n        \"exact_source_quote\": \"Na 2 MoO 4 ·2H 2\
    \ O 0.04 g\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 0.04,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\n      }\n\
    \    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[7].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element solution composition, not\
    \ receiving-medium ingredient\",\n    \"existing\": {\n      \"value\": \"0.015\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Move the unchanged\
    \ source mass to its named stock recipe and retain the source-specific 1 L water\
    \ basis. Do not use the stock mass concentration as a final-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Trace element solution subsection,\
    \ exact ingredient row\",\n        \"exact_source_quote\": \"H 3 BO 3 0.015 g\"\
    ,\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 0.015,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[8].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element solution composition, not\
    \ receiving-medium ingredient\",\n    \"existing\": {\n      \"value\": \"0.02\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Move the unchanged\
    \ source mass to its named stock recipe and retain the source-specific 1 L water\
    \ basis. Do not use the stock mass concentration as a final-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Trace element solution subsection,\
    \ exact ingredient row\",\n        \"exact_source_quote\": \"MnCl 2 ·4H 2 O 0.02\
    \ g\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2・4H2O\\\",\\n          \\\"volume\\\": 0.02,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[9].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element solution composition, not\
    \ receiving-medium ingredient\",\n    \"existing\": {\n      \"value\": \"0.05\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Move the unchanged\
    \ source mass to its named stock recipe and retain the source-specific 1 L water\
    \ basis. Do not use the stock mass concentration as a final-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Trace element solution subsection,\
    \ exact ingredient row\",\n        \"exact_source_quote\": \"CoCl 2 ·6H 2 O 0.05\
    \ g\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 0.05,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[10].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element solution composition, not\
    \ receiving-medium ingredient\",\n    \"existing\": {\n      \"value\": \"0.01\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Move the unchanged\
    \ source mass to its named stock recipe and retain the source-specific 1 L water\
    \ basis. Do not use the stock mass concentration as a final-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Trace element solution subsection,\
    \ exact ingredient row\",\n        \"exact_source_quote\": \"NiCl 2 ·6H 2 O 0.01\
    \ g\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2・6H2O\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[11].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element solution composition, not\
    \ receiving-medium ingredient\",\n    \"existing\": {\n      \"value\": \"0.4\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Move the unchanged\
    \ source mass to its named stock recipe and retain the source-specific 1 L water\
    \ basis. Do not use the stock mass concentration as a final-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Trace element solution subsection,\
    \ exact ingredient row\",\n        \"exact_source_quote\": \"ZnSO 4 ·7H 2 O 0.4\
    \ g\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 0.4,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[12].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element solution composition, not\
    \ receiving-medium ingredient\",\n    \"existing\": {\n      \"value\": \"0.2\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Move the unchanged\
    \ source mass to its named stock recipe and retain the source-specific 1 L water\
    \ basis. Do not use the stock mass concentration as a final-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Trace element solution subsection,\
    \ exact ingredient row\",\n        \"exact_source_quote\": \"CuSO 4 ·5H 2 O 0.2\
    \ g\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[2].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuSO4・5H2O\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[13].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace element solution composition, not\
    \ receiving-medium ingredient\",\n    \"existing\": {\n      \"value\": \"0.25\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Move the unchanged\
    \ source mass to its named stock recipe and retain the source-specific 1 L water\
    \ basis. Do not use the stock mass concentration as a final-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Trace element solution subsection,\
    \ exact ingredient row\",\n        \"exact_source_quote\": \"EDTA·2Na 0.25 g\"\
    ,\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[2].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"EDTA・2Na\\\",\\n          \\\"volume\\\": 0.25,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[14].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Iron stock solution composition, not receiving-medium\
    \ ingredient\",\n    \"existing\": {\n      \"value\": \"4.5\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": \"Move the unchanged source mass to its\
    \ named stock recipe and retain the source-specific 1 L water basis. Do not use\
    \ the stock mass concentration as a final-medium concentration.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm815\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\",\n        \"source_locator\"\
    : \"Medium815 Iron stock solution subsection, exact ingredient row\",\n      \
    \  \"exact_source_quote\": \"EDTA·Fe(III) 4.5 g\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"EDTA・Fe(III)\\\",\\n          \\\"volume\\\":\
    \ 4.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\n      }\n\
    \    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[15].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Phosphate buffer stock solution composition,\
    \ not receiving-medium ingredient\",\n    \"existing\": {\n      \"value\": \"\
    37.425\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Move the unchanged\
    \ source mass to its named stock recipe and retain the source-specific 1 L water\
    \ basis. Do not use the stock mass concentration as a final-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Phosphate buffer stock solution subsection,\
    \ exact ingredient row\",\n        \"exact_source_quote\": \"KH 2 PO 4 37.425\
    \ g\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[4].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 37.425,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[16].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Phosphate buffer stock solution composition,\
    \ not receiving-medium ingredient\",\n    \"existing\": {\n      \"value\": \"\
    48.95\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Move the unchanged\
    \ source mass to its named stock recipe and retain the source-specific 1 L water\
    \ basis. Do not use the stock mass concentration as a final-medium concentration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Phosphate buffer stock solution subsection,\
    \ exact ingredient row\",\n        \"exact_source_quote\": \"Na 2 HPO 4 ·2H 2\
    \ O 48.950 g\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[4].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2HPO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 48.95,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\n     \
    \ }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[0].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Basal mixture before autoclaving\",\n\
    \    \"existing\": {\n      \"value\": \"0.1\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"proposed\": \"Represent the source ml addition per prepared batch,\
    \ not G_PER_L. Retain a typed/reference-resolved or inline stock recipe.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 exact stock-addition row\",\n     \
    \   \"exact_source_quote\": \"Trace element solution (see below) 0.1 ml\",\n \
    \       \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution (see below)\\\",\\n   \
    \       \\\"volume\\\": 0.1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n       \
    \ \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"source_amount\": {\n      \"value\": 0.1,\n      \"unit\"\
    : \"ml\"\n    }\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[1].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Basal mixture before autoclaving\",\n\
    \    \"existing\": {\n      \"value\": \"0.1\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"proposed\": \"Represent the source ml addition per prepared batch,\
    \ not G_PER_L. Retain a typed/reference-resolved or inline stock recipe.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 exact stock-addition row\",\n     \
    \   \"exact_source_quote\": \"Iron stock solution (see below) 0.1 ml\",\n    \
    \    \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Iron stock solution (see below)\\\",\\n      \
    \    \\\"volume\\\": 0.1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"source_amount\": {\n      \"value\": 0.1,\n      \"unit\"\
    : \"ml\"\n    }\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[2].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"After cooling, separately autoclaved phosphate\
    \ stock\",\n    \"existing\": {\n      \"value\": \"2\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"proposed\": \"Represent the source ml addition per prepared batch,\
    \ not G_PER_L. Retain a typed/reference-resolved or inline stock recipe.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 exact stock-addition row\",\n     \
    \   \"exact_source_quote\": \"Phosphate buffer stock solution 2.0 ml\",\n    \
    \    \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Phosphate buffer stock solution\\\",\\n      \
    \    \\\"volume\\\": 2,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\"\
    : \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\n     \
    \ }\n    ],\n    \"source_amount\": {\n      \"value\": 2,\n      \"unit\": \"\
    ml\"\n    }\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions (source-only stock solvent)\",\n   \
    \ \"decision\": \"add\",\n    \"source_stage\": \"Trace element solution preparation\"\
    ,\n    \"existing\": null,\n    \"proposed\": \"Keep this 1 L solvent only within\
    \ its own stock. It must not be summed with the basal water or other stock batches.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Trace element solution subsection,\
    \ distilled-water row\",\n        \"exact_source_quote\": \"Distilled water 1.0\
    \ L\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"source_amount\": {\n      \"value\": 1,\n      \"unit\"\
    : \"L\"\n    }\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions (source-only stock solvent)\",\n   \
    \ \"decision\": \"add\",\n    \"source_stage\": \"Iron stock solution preparation\"\
    ,\n    \"existing\": null,\n    \"proposed\": \"Keep this 1 L solvent only within\
    \ its own stock. It must not be summed with the basal water or other stock batches.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Iron stock solution subsection, distilled-water\
    \ row\",\n        \"exact_source_quote\": \"Distilled water 1.0 L\",\n       \
    \ \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"source_amount\": {\n      \"value\": 1,\n      \"unit\"\
    : \"L\"\n    }\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions (source-only stock solvent)\",\n   \
    \ \"decision\": \"add\",\n    \"source_stage\": \"Phosphate buffer stock solution\
    \ preparation\",\n    \"existing\": null,\n    \"proposed\": \"Keep this 1 L solvent\
    \ only within its own stock. It must not be summed with the basal water or other\
    \ stock batches.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 Phosphate buffer stock solution subsection,\
    \ distilled-water row\",\n        \"exact_source_quote\": \"Distilled water 1.0\
    \ L\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\",\n \
    \       \"source_locator\": \"$.components[4].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"source_amount\": {\n      \"value\": 1,\n      \"unit\"\
    : \"L\"\n    }\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ph_value\",\n    \"decision\": \"add\",\n    \"\
    source_stage\": \"Completed base medium before aliquoting\",\n    \"existing\"\
    : null,\n    \"proposed\": \"Record pH 3.0 as the target for the base, distinct\
    \ from child pH 6.7.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 preparation paragraph or qualified\
    \ page instruction\",\n        \"exact_source_quote\": \"adjust pH to 3.0\",\n\
    \        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"preparation_steps (adjustment-stock strength)\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Sterile HCl titrant\",\n\
    \    \"existing\": null,\n    \"proposed\": \"Record 1 N strength; no fixed titrant\
    \ volume or molar conversion is inferred.\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 preparation paragraph or qualified\
    \ page instruction\",\n        \"exact_source_quote\": \"sterile 1 N HCl solution\"\
    ,\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"preparation_steps (liquid aliquot)\",\n    \"\
    decision\": \"add\",\n    \"source_stage\": \"Bottle dispensing\",\n    \"existing\"\
    : null,\n    \"proposed\": \"Record 20 ml liquid aliquots in the specified bottle\
    \ context.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 preparation paragraph or qualified\
    \ page instruction\",\n        \"exact_source_quote\": \"distribute 20 ml-aliquots\
    \ of the medium\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"preparation_steps (bottle volume)\",\n    \"decision\"\
    : \"add\",\n    \"source_stage\": \"Bottle dispensing\",\n    \"existing\": null,\n\
    \    \"proposed\": \"Record vessel nominal volume 120 ml; it is not a recipe-volume\
    \ denominator.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 preparation paragraph or qualified\
    \ page instruction\",\n        \"exact_source_quote\": \"sterile 120 ml-serum\
    \ bottles\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"preparation_steps (default sterilization temperature)\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Site default, only where\
    \ no specific alternative is stated\",\n    \"existing\": null,\n    \"proposed\"\
    : \"Retain 121°C with the explicit unless-otherwise-stated qualifier; methane\
    \ remains filter-sterilized.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 preparation paragraph or qualified\
    \ page instruction\",\n        \"exact_source_quote\": \"Unless otherwise stated,\
    \ sterilize media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"preparation_steps (default sterilization duration)\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Site default, only where\
    \ no specific alternative is stated\",\n    \"existing\": null,\n    \"proposed\"\
    : \"Retain 15 min with the explicit unless-otherwise-stated qualifier.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Medium815 preparation paragraph or qualified\
    \ page instruction\",\n        \"exact_source_quote\": \"Unless otherwise stated,\
    \ sterilize media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml\"\
    ,\n    \"field_path\": \"composition[0].concentration\",\n    \"ingredient\":\
    \ \"KH2PO4\",\n    \"existing\": {\n      \"value\": \"37.425\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\":\
    \ \"Independent solution4768 stock composition only\",\n    \"basis\": \"Provider-declared\
    \ 1000 ml stock basis; the water row is a batch dose. No receiving-medium g/L\
    \ is implied.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4768\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4768\"\
    ,\n        \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 1,\\n                \\\"compound\\\
    \": \\\"KH2PO4\\\",\\n                \\\"compound_id\\\": 11,\\n            \
    \    \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n \
    \               \\\"condition\\\": null,\\n                \\\"attribute\\\":\
    \ null,\\n                \\\"amount\\\": 37.425,\\n                \\\"unit\\\
    \": \\\"g\\\",\\n                \\\"g_l\\\": 37.425,\\n                \\\"mmol_l\\\
    \": 275.01,\\n                \\\"optional\\\": 0\\n            }\",\n       \
    \ \"snapshot_sha256\": \"8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67\"\
    \n      }\n    ],\n    \"proposed\": \"Retain exact existing source evidence in\
    \ the stock; independently attach the target stock-addition evidence.\"\n  },\n\
    \  {\n    \"input\": \"data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml\"\
    ,\n    \"field_path\": \"composition[1].concentration\",\n    \"ingredient\":\
    \ \"Na2HPO4 x 2 H2O\",\n    \"existing\": {\n      \"value\": \"48.95\",\n   \
    \   \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\"\
    : \"Independent solution4768 stock composition only\",\n    \"basis\": \"Provider-declared\
    \ 1000 ml stock basis; the water row is a batch dose. No receiving-medium g/L\
    \ is implied.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4768\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4768\"\
    ,\n        \"source_locator\": \"$.data.recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 2,\\n                \\\"compound\\\
    \": \\\"Na2HPO4 x 2 H2O\\\",\\n                \\\"compound_id\\\": 181,\\n  \
    \              \\\"solution\\\": null,\\n                \\\"solution_id\\\":\
    \ null,\\n                \\\"condition\\\": null,\\n                \\\"attribute\\\
    \": null,\\n                \\\"amount\\\": 48.95,\\n                \\\"unit\\\
    \": \\\"g\\\",\\n                \\\"g_l\\\": 48.95,\\n                \\\"mmol_l\\\
    \": 344.818,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67\"\
    \n      }\n    ],\n    \"proposed\": \"Retain exact existing source evidence in\
    \ the stock; independently attach the target stock-addition evidence.\"\n  },\n\
    \  {\n    \"input\": \"data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml\"\
    ,\n    \"field_path\": \"composition[2].concentration\",\n    \"ingredient\":\
    \ \"Distilled water\",\n    \"existing\": {\n      \"value\": \"1\",\n      \"\
    unit\": \"L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\":\
    \ \"Independent solution4768 stock composition only\",\n    \"basis\": \"Provider-declared\
    \ 1000 ml stock basis; the water row is a batch dose. No receiving-medium g/L\
    \ is implied.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4768\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4768\"\
    ,\n        \"source_locator\": \"$.data.recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 3,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 1000,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67\"\
    \n      }\n    ],\n    \"proposed\": \"Retain exact existing source evidence in\
    \ the stock; independently attach the target stock-addition evidence.\"\n  },\n\
    \  {\n    \"input\": \"data/normalized_yaml/bacterial/TOGO_M851_Diluted_ASM_Medium.yaml\"\
    ,\n    \"field_path\": \"ph_value\",\n    \"existing\": 6.7,\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Separate TOGO M851 / JCM816 child\"\
    ,\n    \"proposed\": \"Retain pH 6.7 with exact provider linkage; direct current\
    \ JCM816 page is unavailable. Do not apply this pH to the base.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM851\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M851\",\n     \
    \   \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"Prepare Medium No. [815] and adjust pH to 6.7.\",\n        \"snapshot_sha256\"\
    : \"69876dcbc941f2bb1c9b552f2eeacbc978ad69460d519baddccdb69a1e224e8b\"\n     \
    \ }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/TOGO_M851_Diluted_ASM_Medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].concentration\",\n    \"existing\": {\n\
    \      \"value\": \"1000\",\n      \"unit\": \"ML_PER_L\"\n    },\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Prepared-parent medium quantity in separate\
    \ child\",\n    \"proposed\": \"Provider gives 1 L prepared parent, not an independently\
    \ supported per-final-litre dose. Preserve the source batch quantity and explicit\
    \ child scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM851\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M851\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ACIDIC DILUTED ASM MEDIUM (see Medium [M850])\\\
    \",\\n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n  \
    \      \"snapshot_sha256\": \"69876dcbc941f2bb1c9b552f2eeacbc978ad69460d519baddccdb69a1e224e8b\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '15 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 15/17 primary and 5/17 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form
    mismatch is addressed separately; valid IDs and labels do not establish correct
    source grounding.'
  target_ids:
  - CultureMech:010266
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi17883
  - chebi31206
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi33118
  - chebi34683
  - chebi34887
  - chebi35696
  - chebi63036
  - chebi64734
  - chebi75213
  - chebi86158
  - chebi86368
  details: 'Instance coverage on a 0–100 percent scale, denominator 17: primary 88.24%;
    secondary 29.41%. These are linkage metrics, not correctness scores. Missing optional
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
  - CultureMech:010266
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: preparation
  area: completeness
  topic: All source preparation stages and dose bases
  outcome: concern
  summary: The source distinguishes basal autoclaving, later separately autoclaved
    phosphate, sterile 1 N HCl adjustment to pH 3.0, 20 ml aliquots in 120 ml bottles
    and 100 ml filter-sterilized methane to headspace. Both local layers omit preparation
    and base pH. Numeric quantities and the qualified default sterilization instruction
    are in the inventory; no final liquid volume or gas-to-liquid concentration is
    derived.
  target_ids:
  - CultureMech:010266
  evidence_ids:
  - primary
  - provider
  - quantity-inventory
  - record
  - owner-0
- assessment_id: classification
  area: scope
  topic: Defined chemistry versus inherited COMPLEX/UNDEFINED labels
  outcome: concern
  summary: The inspected recipe is a specified mineral/chelate/gas formulation without
    yeast extract, peptone or another stated complex biological ingredient. COMPLEX
    / UNDEFINED lacks source-specific justification; exact chelate/form resolution
    and proper stock separation should precede choosing replacement enum values. LIQUID
    is supported. Generic category/application metadata does not establish growth
    for a named strain.
  target_ids:
  - CultureMech:010266
  evidence_ids:
  - primary
  - provider
  - record
findings:
- finding_id: f1
  issue_key: culturemech.010266.stock-flattening-water
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Three stock recipes and four solvent quantities are conflated with the receiving
    medium
  description: Eleven direct ingredient entries are actually eight trace-stock solutes,
    one iron-stock solute and two phosphate-stock solutes. Their stock amounts appear
    as receiving-medium G_PER_L values beside empty stock nodes. The target also sums
    four distinct 1 L source water batches into 4 G_PER_L; the owner’s later collapse
    to 1 G_PER_L remains dimensionally and stage-wise wrong. This changes the represented
    formulation, despite passing schema checks.
  target_ids:
  - CultureMech:010266
  field_paths:
  - ingredients[0]
  - ingredients[6:17]
  - solutions
  - merge_fingerprint
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
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
  issue_key: culturemech.010266.stock-dose-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock-addition volumes are represented as mass concentrations
  description: Trace and iron stocks are each 0.1 ml per prepared batch; phosphate
    is 2 ml added after cooling. All three local nodes instead use G_PER_L. The basal
    salt source masses likewise require their source batch basis rather than a measured
    final-volume assumption.
  target_ids:
  - CultureMech:010266
  field_paths:
  - solutions[0].concentration
  - solutions[1].concentration
  - solutions[2].concentration
  - ingredients[1:4].concentration
  evidence_ids:
  - primary
  - provider
  - phosphate-provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
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
  issue_key: culturemech.010266.supplied-form-mismatch
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Three hydrate labels map to nonhydrate structures and EDTA specificity is
    unproven
  description: The source specifies cobalt chloride hexahydrate, nickel chloride hexahydrate
    and disodium hydrogenphosphate dihydrate, but CHEBI:35696, CHEBI:34887 and CHEBI:34683
    carry formulas without hydration water. EDTA·2Na is mapped to explicitly anhydrous
    CHEBI:64734 although the source does not resolve that hydration state. Exact canonical
    labels pass while supplied forms remain wrong or over-specific. The independent
    phosphate stock already uses a dihydrate identity; its concentration evidence
    does not validate the target’s nonhydrate term.
  target_ids:
  - CultureMech:010266
  field_paths:
  - ingredients[9].term
  - ingredients[10].term
  - ingredients[13].term
  - ingredients[16].term
  evidence_ids:
  - primary
  - provider
  - chebi35696
  - chebi34887
  - chebi64734
  - chebi34683
  - stock-dihydrate-term
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
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
  issue_key: culturemech.010266.preparation-and-gas
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source pH, staged sterilization and quantified methane context are absent
  description: Both layers omit the full preparation and base pH. Methane is VARIABLE
    even though the exact source provides a 100 ml bottle-headspace addition, with
    a 20 ml liquid aliquot and 120 ml vessel context. HCl dose is genuinely variable,
    but its 1 N stock strength and target pH 3.0 are missing. These quantities must
    not be collapsed into final liquid concentration.
  target_ids:
  - CultureMech:010266
  field_paths:
  - ph_value
  - preparation_steps
  - ingredients[4]
  - ingredients[5]
  evidence_ids:
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
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
  issue_key: culturemech.010266.variant-link-stale
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated target omits the maintained pH-variant relationship
  description: The normalized owner’s September reciprocal PH_VARIANT link to CultureMech:010267
    is missing from the August generated target. The provider supports a distinct
    pH 6.7 child; it must remain separate from the pH 3.0 base. Current JCM816 source
    content is unavailable and is not replaced with an invented primary assertion.
  target_ids:
  - CultureMech:010266
  field_paths:
  - variant_children
  - curation_history
  - merged_from
  evidence_ids:
  - record
  - owner-0
  - dependency-variant
  - variant-provider
  - jcm816-attempt
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: culturemech.010266.classification-evidence
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: COMPLEX and UNDEFINED lack formulation-specific support
  description: The primary describes a specified mineral/chelate/gas recipe and separately
    defined stocks. No complex biological mixture is stated. The inherited labels
    should be reassessed with proper stock and chemical-form representation; no replacement
    classification is inferred solely from a validator pass.
  target_ids:
  - CultureMech:010266
  field_paths:
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - primary
  - provider
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
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
  description: Restore the three scoped stock recipes and basal solvent in the normalized
    owner; preserve exact source labels/amounts and typed phosphate identity, then
    regenerate via maintained stage-aware import/merge paths. Do not sum stock preparation
    water or infer final concentrations.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010266
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
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
  description: Restore ml stock doses with preparation-stage evidence and source batch
    masses/basis. Keep stock composition concentration distinct from receiving-medium
    concentration.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010266
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
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
  description: Correct the supported hydrate identities after exact term verification;
    retain EDTA disodium identity without asserting an unverified hydrate state. Keep
    HCl solution strength and Fe(III)-EDTA identity separately scoped; do not invent
    unresolved links.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010266
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
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
  description: Restore the exact source preparation, sterile adjustment/gas stages
    and qualified general autoclave context. Record bottle and headspace quantities
    at their own stages, retaining an unquantified titrant dose.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010266
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
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
  description: Preserve the source-qualified reciprocal variant relation when regenerating;
    retain the direct-primary access limit and do not overwrite the base pH with the
    child condition.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:010266
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
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
  description: Reassess and evidence the classification after resolving stock/chelate
    representation; preserve the supported liquid state and avoid organism-growth
    claims from the medium name.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:010266
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
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
- The current exact JCM 816 URL returned HTTP 200 with Nothing found, not a recipe.
  TOGO M851 and the reciprocal local PH_VARIANT links support the pH 6.7 wrapper,
  but direct current collection confirmation of that linked variant remains unavailable.
  The complete JCM 815 base formulation is accessible and assessed.
- No measured final-medium volume, methane partial pressure, dissolved-gas concentration,
  growth temperature, strain performance or complete chelate hydration specification
  was inferred. The independent stock and child records were inspected as dependencies
  only. Current code and history establish context, not proof of the historical writer
  execution.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-017
- generated-medium
```
