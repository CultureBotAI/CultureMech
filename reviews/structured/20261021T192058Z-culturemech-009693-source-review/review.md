# Source and formulation review: alkaline_diluted_ams_medium (CultureMech:009693)

- Review: 20261021T192058Z-culturemech-009693-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T19:13:57Z
- Finished UTC: 2026-10-21T19:20:58Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 1428 explicitly modifies JCM 815. The maintained owner preserves the child pH, gas ratio and nested stocks, while the generated target remains stale. Batch-denominator and claim-evidence qualifications remain necessary; exact historical MediaDive 4767 authentication is unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 349; batch 035 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-four task batches contain 340 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 343 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009693 | data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml | generated | alkaline_diluted_ams_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009693 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009693 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch035/349/strict.tsv |
| validate-terms | passed | True | CultureMech:009693 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009693 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009693 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: solution4767 | unavailable | True | CultureMech:009693 | Exact MediaDive 4767 and its separately preserved retry return 503. Two historical local excerpts remain derivative-only; original response cf7e5be177e4c6e16506daa65f21cef4189eecade344fab01f83de936f8f825f was not recovered. Required asserted-stock identity/evidence authentication is incomplete, though JCM 815 directly supports the named stock recipe. |
| Exact source content access: solution4767Retry1 | unavailable | False | CultureMech:009693 | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |
| Exact source content access: mediadiveJ1428 | unavailable | False | CultureMech:009693 | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |
| Exact source content access: mediadiveJ1428Retry1 | unavailable | False | CultureMech:009693 | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |
| Exact source content access: mediadiveJ815 | unavailable | False | CultureMech:009693 | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |
| Exact source content access: mediadiveJ815Retry1 | unavailable | False | CultureMech:009693 | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |
| Exact source content access: togoM3279 | unavailable | False | CultureMech:009693 | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |
| Exact source content access: togoM850 | unavailable | False | CultureMech:009693 | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009693.

The four documented recipes completed; interpret the scope of each separately.

### Exact child and explicitly invoked parent

identity: supported. Targets: CultureMech:009693.

TOGO M3279/JCM 1428 explicitly invokes JCM 815 with pH 8.0, 1 ml phosphate stock per liter and methane-air 80:20 v/v. The maintained owner and target share the exact stable ID and complete merge provenance. Parent pH 3.0, parent phosphate 2 ml and 100 ml pure methane are excluded from child transfer. No species-specific growth evidence is asserted.

### Repaired maintained source versus stale generated target

ownership: concern. Targets: CultureMech:009693.

The September owner repair nests all three stock compositions, restores volume units, pH and gas preparation, and removes the parent acid adjustment. The generated target retains old empty stocks, mass units for liquid additions, gas placeholders and HCl. Owner notes and bare source references do not authenticate quantities or final-volume denominators.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009693.

63 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "ingredient": "NH4Cl",
    "decision": "correct",
    "stage": "Inherited basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Basal recipe; NH4Cl",
        "exact_source_quote": "NH 4 Cl 0.1 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM3279original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a"
      }
    ],
    "interpretation": "Preserve the exact original batch amount and the separately listed 1 L water. The owner numerical conversion does not establish a final measured denominator; its notes call the printed amount g/L or ml/L although the primary table gives batch grams or water volume."
  },
  {
    "decision_id": "q2",
    "ingredient": "MgSO4·7H2O",
    "decision": "correct",
    "stage": "Inherited basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Basal recipe; MgSO4·7H2O",
        "exact_source_quote": "MgSO 4 ·7H 2 O 0.1 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM3279original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4·7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a"
      }
    ],
    "interpretation": "Preserve the exact original batch amount and the separately listed 1 L water. The owner numerical conversion does not establish a final measured denominator; its notes call the printed amount g/L or ml/L although the primary table gives batch grams or water volume."
  },
  {
    "decision_id": "q3",
    "ingredient": "CaCl2·2H2O",
    "decision": "correct",
    "stage": "Inherited basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Basal recipe; CaCl2·2H2O",
        "exact_source_quote": "CaCl 2 ·2H 2 O 0.02 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM3279original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"CaCl2·2H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a"
      }
    ],
    "interpretation": "Preserve the exact original batch amount and the separately listed 1 L water. The owner numerical conversion does not establish a final measured denominator; its notes call the printed amount g/L or ml/L although the primary table gives batch grams or water volume."
  },
  {
    "decision_id": "q4",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "Inherited basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Basal recipe; Distilled water",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM3279original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a"
      }
    ],
    "interpretation": "Preserve the exact original batch amount and the separately listed 1 L water. The owner numerical conversion does not establish a final measured denominator; its notes call the printed amount g/L or ml/L although the primary table gives batch grams or water volume. The target additionally stores water as 1 G_PER_L, which is a wrong unit."
  },
  {
    "decision_id": "q5",
    "ingredient": "Trace element solution",
    "decision": "correct",
    "stage": "Basal stock addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "0.1",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "DISSOLVE",
          "description": "Dissolve NH4Cl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O in distilled water with 0.1 ml/L Trace element solution and 0.1 ml/L Iron stock solution."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Basal table; Trace element solution",
        "exact_source_quote": "Trace element solution (see below) 0.1 ml",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM3279original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"Trace element solution (see Medium [M850])\",\n          \"volume\": 0.1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a"
      }
    ],
    "interpretation": "The target uses G_PER_L for a 0.1 ml dose. The owner restores volume but calls it ml/L; qualify it as the stated basal batch addition unless an explicit final denominator is documented. Do not add the whole stock preparation to the basal batch."
  },
  {
    "decision_id": "q6",
    "ingredient": "Iron stock solution",
    "decision": "correct",
    "stage": "Basal stock addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "0.1",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "DISSOLVE",
          "description": "Dissolve NH4Cl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O in distilled water with 0.1 ml/L Trace element solution and 0.1 ml/L Iron stock solution."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Basal table; Iron stock solution",
        "exact_source_quote": "Iron stock solution (see below) 0.1 ml",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM3279original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"Iron stock solution (see Medium [M850])\",\n          \"volume\": 0.1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a"
      }
    ],
    "interpretation": "The target uses G_PER_L for a 0.1 ml dose. The owner restores volume but calls it ml/L; qualify it as the stated basal batch addition unless an explicit final denominator is documented. Do not add the whole stock preparation to the basal batch."
  },
  {
    "decision_id": "q7",
    "ingredient": "Phosphate stock addition",
    "decision": "correct",
    "stage": "Child final-medium addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Child phosphate addition override",
        "exact_source_quote": "Reduce the amount of phosphate buffer stock solution to 1.0 ml per liter of the medium.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      },
      {
        "source_key": "togoM3279original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Phosphate buffer stock solution (see Medium [M850])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a"
      }
    ],
    "interpretation": "The child explicitly supplies 1 ml per liter. Correct target G_PER_L to the liquid addition basis; do not inherit the parent 2 ml dose."
  },
  {
    "decision_id": "q8",
    "ingredient": "Phosphate stock addition",
    "decision": "evidence_only",
    "stage": "Child final-medium addition",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "preparation_steps[3]",
        "stored": {
          "step_number": 4,
          "action": "MIX",
          "description": "After cooling, add 1.0 ml/L sterile Phosphate buffer stock solution to the basal medium."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Child phosphate addition override",
        "exact_source_quote": "Reduce the amount of phosphate buffer stock solution to 1.0 ml per liter of the medium.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "The owner already retains 1.0 ML_PER_L and the correct after-cooling addition. Attach claim-level evidence; its current references alone are not an attached amount excerpt."
  },
  {
    "decision_id": "q9",
    "ingredient": "ZnSO4 x 7 H2O",
    "decision": "correct",
    "stage": "Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; ZnSO4 x 7 H2O",
        "exact_source_quote": "ZnSO 4 ·7H 2 O 0.4 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. The primary prints batch grams with 1 L water. Preserve those original units and qualify the owner note that claims the primary prints g/L; do not assert a measured stock volume or final-medium concentration."
  },
  {
    "decision_id": "q10",
    "ingredient": "ZnSO4 x 7 H2O",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; ZnSO4 x 7 H2O",
        "exact_source_quote": "ZnSO 4 ·7H 2 O 0.4 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration."
  },
  {
    "decision_id": "q11",
    "ingredient": "EDTA x 2Na",
    "decision": "correct",
    "stage": "Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; EDTA x 2Na",
        "exact_source_quote": "EDTA·2Na 0.25 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[8]",
        "exact_source_quote": "\"component_name\": \"EDTA・2Na\",\n          \"volume\": 0.25,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. The primary prints batch grams with 1 L water. Preserve those original units and qualify the owner note that claims the primary prints g/L; do not assert a measured stock volume or final-medium concentration."
  },
  {
    "decision_id": "q12",
    "ingredient": "EDTA x 2Na",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; EDTA x 2Na",
        "exact_source_quote": "EDTA·2Na 0.25 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[8]",
        "exact_source_quote": "\"component_name\": \"EDTA・2Na\",\n          \"volume\": 0.25,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration."
  },
  {
    "decision_id": "q13",
    "ingredient": "MnCl2 x 4 H2O",
    "decision": "correct",
    "stage": "Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[0].composition[2].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; MnCl2 x 4 H2O",
        "exact_source_quote": "MnCl 2 ·4H 2 O 0.02 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. The primary prints batch grams with 1 L water. Preserve those original units and qualify the owner note that claims the primary prints g/L; do not assert a measured stock volume or final-medium concentration."
  },
  {
    "decision_id": "q14",
    "ingredient": "MnCl2 x 4 H2O",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; MnCl2 x 4 H2O",
        "exact_source_quote": "MnCl 2 ·4H 2 O 0.02 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration."
  },
  {
    "decision_id": "q15",
    "ingredient": "H3BO3",
    "decision": "correct",
    "stage": "Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[0].composition[3].concentration",
        "stored": {
          "value": "0.015",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; H3BO3",
        "exact_source_quote": "H 3 BO 3 0.015 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 0.015,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. The primary prints batch grams with 1 L water. Preserve those original units and qualify the owner note that claims the primary prints g/L; do not assert a measured stock volume or final-medium concentration."
  },
  {
    "decision_id": "q16",
    "ingredient": "H3BO3",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.015",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; H3BO3",
        "exact_source_quote": "H 3 BO 3 0.015 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 0.015,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration."
  },
  {
    "decision_id": "q17",
    "ingredient": "Na2MoO4 x 2 H2O",
    "decision": "correct",
    "stage": "Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[0].composition[4].concentration",
        "stored": {
          "value": "0.04",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; Na2MoO4 x 2 H2O",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 0.04 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.04,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. The primary prints batch grams with 1 L water. Preserve those original units and qualify the owner note that claims the primary prints g/L; do not assert a measured stock volume or final-medium concentration."
  },
  {
    "decision_id": "q18",
    "ingredient": "Na2MoO4 x 2 H2O",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.04",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; Na2MoO4 x 2 H2O",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 0.04 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.04,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration."
  },
  {
    "decision_id": "q19",
    "ingredient": "NiCl2 x 6 H2O",
    "decision": "correct",
    "stage": "Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[0].composition[5].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; NiCl2 x 6 H2O",
        "exact_source_quote": "NiCl 2 ·6H 2 O 0.01 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. The primary prints batch grams with 1 L water. Preserve those original units and qualify the owner note that claims the primary prints g/L; do not assert a measured stock volume or final-medium concentration."
  },
  {
    "decision_id": "q20",
    "ingredient": "NiCl2 x 6 H2O",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; NiCl2 x 6 H2O",
        "exact_source_quote": "NiCl 2 ·6H 2 O 0.01 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration."
  },
  {
    "decision_id": "q21",
    "ingredient": "CuSO4 x 5 H2O",
    "decision": "correct",
    "stage": "Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[0].composition[6].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; CuSO4 x 5 H2O",
        "exact_source_quote": "CuSO 4 ·5H 2 O 0.2 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[7]",
        "exact_source_quote": "\"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. The primary prints batch grams with 1 L water. Preserve those original units and qualify the owner note that claims the primary prints g/L; do not assert a measured stock volume or final-medium concentration."
  },
  {
    "decision_id": "q22",
    "ingredient": "CuSO4 x 5 H2O",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; CuSO4 x 5 H2O",
        "exact_source_quote": "CuSO 4 ·5H 2 O 0.2 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[7]",
        "exact_source_quote": "\"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration."
  },
  {
    "decision_id": "q23",
    "ingredient": "CoCl2 x 6 H2O",
    "decision": "correct",
    "stage": "Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[0].composition[7].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; CoCl2 x 6 H2O",
        "exact_source_quote": "CoCl 2 ·6H 2 O 0.05 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 0.05,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. The primary prints batch grams with 1 L water. Preserve those original units and qualify the owner note that claims the primary prints g/L; do not assert a measured stock volume or final-medium concentration."
  },
  {
    "decision_id": "q24",
    "ingredient": "CoCl2 x 6 H2O",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; CoCl2 x 6 H2O",
        "exact_source_quote": "CoCl 2 ·6H 2 O 0.05 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 0.05,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration."
  },
  {
    "decision_id": "q25",
    "ingredient": "Distilled water",
    "decision": "evidence_only",
    "stage": "Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[0].composition[8].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; Distilled water",
        "exact_source_quote": "Trace element solution: ZnSO 4 ·7H 2 O 0.4 g EDTA·2Na 0.25 g MnCl 2 ·4H 2 O 0.02 g H 3 BO 3 0.015 g Na 2 MoO 4 ·2H 2 O 0.04 g NiCl 2 ·6H 2 O 0.01 g CuSO 4 ·5H 2 O 0.2 g CoCl 2 ·6H 2 O 0.05 g Distilled water 1.0 L ",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. Its 1 L water is a preparation input within this stock, not extra water added to the receiving medium or a measured final volume."
  },
  {
    "decision_id": "q26",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Trace element solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution subsection; Distilled water",
        "exact_source_quote": "Trace element solution: ZnSO 4 ·7H 2 O 0.4 g EDTA·2Na 0.25 g MnCl 2 ·4H 2 O 0.02 g H 3 BO 3 0.015 g Na 2 MoO 4 ·2H 2 O 0.04 g NiCl 2 ·6H 2 O 0.01 g CuSO 4 ·5H 2 O 0.2 g CoCl 2 ·6H 2 O 0.05 g Distilled water 1.0 L ",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration. The single collapsed water field cannot stand for all basal and three stock water inputs."
  },
  {
    "decision_id": "q27",
    "ingredient": "EDTA x Fe(III)",
    "decision": "correct",
    "stage": "Iron stock solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "4.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Iron stock solution subsection; EDTA x Fe(III)",
        "exact_source_quote": "EDTA·Fe(III) 4.5 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"EDTA・Fe(III)\",\n          \"volume\": 4.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. The primary prints batch grams with 1 L water. Preserve those original units and qualify the owner note that claims the primary prints g/L; do not assert a measured stock volume or final-medium concentration."
  },
  {
    "decision_id": "q28",
    "ingredient": "EDTA x Fe(III)",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Iron stock solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "4.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Iron stock solution subsection; EDTA x Fe(III)",
        "exact_source_quote": "EDTA·Fe(III) 4.5 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"EDTA・Fe(III)\",\n          \"volume\": 4.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration."
  },
  {
    "decision_id": "q29",
    "ingredient": "Distilled water",
    "decision": "evidence_only",
    "stage": "Iron stock solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[1].composition[1].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Iron stock solution subsection; Distilled water",
        "exact_source_quote": "Iron stock solution: EDTA·Fe(III) 4.5 g Distilled water 1.0 L ",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. Its 1 L water is a preparation input within this stock, not extra water added to the receiving medium or a measured final volume."
  },
  {
    "decision_id": "q30",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Iron stock solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Iron stock solution subsection; Distilled water",
        "exact_source_quote": "Iron stock solution: EDTA·Fe(III) 4.5 g Distilled water 1.0 L ",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration. The single collapsed water field cannot stand for all basal and three stock water inputs."
  },
  {
    "decision_id": "q31",
    "ingredient": "KH2PO4",
    "decision": "evidence_only",
    "stage": "Phosphate buffer stock solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[2].composition[0].concentration",
        "stored": {
          "value": "37.425",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Phosphate buffer stock solution subsection; KH2PO4",
        "exact_source_quote": "KH 2 PO 4 37.425 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[4].items[1]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 37.425,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      },
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"KH2PO4\",\n                \"compound_id\": 11,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 37.425,\n                \"unit\": \"g\",\n                \"g_l\": 37.425,\n                \"mmol_l\": 275.01,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. The independent exact phosphate API explicitly declares the same stock g/L value and 1000 ml basis. That support does not transfer an existing evidence attachment from the external stock into this owner."
  },
  {
    "decision_id": "q32",
    "ingredient": "KH2PO4",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Phosphate buffer stock solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "37.425",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Phosphate buffer stock solution subsection; KH2PO4",
        "exact_source_quote": "KH 2 PO 4 37.425 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[4].items[1]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 37.425,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      },
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"KH2PO4\",\n                \"compound_id\": 11,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 37.425,\n                \"unit\": \"g\",\n                \"g_l\": 37.425,\n                \"mmol_l\": 275.01,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration."
  },
  {
    "decision_id": "q33",
    "ingredient": "Na2HPO4 x 2 H2O",
    "decision": "evidence_only",
    "stage": "Phosphate buffer stock solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[2].composition[1].concentration",
        "stored": {
          "value": "48.950",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Phosphate buffer stock solution subsection; Na2HPO4 x 2 H2O",
        "exact_source_quote": "Na 2 HPO 4 ·2H 2 O 48.950 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[4].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2HPO4・2H2O\",\n          \"volume\": 48.95,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      },
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Na2HPO4 x 2 H2O\",\n                \"compound_id\": 181,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 48.95,\n                \"unit\": \"g\",\n                \"g_l\": 48.95,\n                \"mmol_l\": 344.818,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. The independent exact phosphate API explicitly declares the same stock g/L value and 1000 ml basis. That support does not transfer an existing evidence attachment from the external stock into this owner."
  },
  {
    "decision_id": "q34",
    "ingredient": "Na2HPO4 x 2 H2O",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Phosphate buffer stock solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "48.95",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Phosphate buffer stock solution subsection; Na2HPO4 x 2 H2O",
        "exact_source_quote": "Na 2 HPO 4 ·2H 2 O 48.950 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[4].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2HPO4・2H2O\",\n          \"volume\": 48.95,\n          \"unit\": \"g\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      },
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Na2HPO4 x 2 H2O\",\n                \"compound_id\": 181,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 48.95,\n                \"unit\": \"g\",\n                \"g_l\": 48.95,\n                \"mmol_l\": 344.818,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration."
  },
  {
    "decision_id": "q35",
    "ingredient": "Distilled water",
    "decision": "evidence_only",
    "stage": "Phosphate buffer stock solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "solutions[2].composition[2].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Phosphate buffer stock solution subsection; Distilled water",
        "exact_source_quote": "Phosphate buffer stock solution: KH 2 PO 4 37.425 g Na 2 HPO 4 ·2H 2 O 48.950 g Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[4].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "The owner preserves this stock-local amount and has no attached claim evidence. Its 1 L water is a preparation input within this stock, not extra water added to the receiving medium or a measured final volume."
  },
  {
    "decision_id": "q36",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "Flattened M850 dependency; Phosphate buffer stock solution",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Phosphate buffer stock solution subsection; Distilled water",
        "exact_source_quote": "Phosphate buffer stock solution: KH 2 PO 4 37.425 g Na 2 HPO 4 ·2H 2 O 48.950 g Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "togoM850original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850",
        "source_locator": "$.components[4].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b"
      }
    ],
    "interpretation": "This parent-context field flattens a named stock amount into direct ingredients; retain its exact stock stage for the child. The local parent value is not evidence of final-medium concentration. The single collapsed water field cannot stand for all basal and three stock water inputs."
  },
  {
    "decision_id": "q37",
    "ingredient": "Trace element solution composition",
    "decision": "add",
    "stage": "Target missing named stock composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Trace element solution complete subsection",
        "exact_source_quote": "Trace element solution: ZnSO 4 ·7H 2 O 0.4 g EDTA·2Na 0.25 g MnCl 2 ·4H 2 O 0.02 g H 3 BO 3 0.015 g Na 2 MoO 4 ·2H 2 O 0.04 g NiCl 2 ·6H 2 O 0.01 g CuSO 4 ·5H 2 O 0.2 g CoCl 2 ·6H 2 O 0.05 g Distilled water 1.0 L ",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ],
    "interpretation": "Target composition is empty. Curate the exact named stock definition, with separate preparation basis and receiving dose; the owner already contains it and requires evidence/denominator qualification rather than duplication."
  },
  {
    "decision_id": "q38",
    "ingredient": "Iron stock solution composition",
    "decision": "add",
    "stage": "Target missing named stock composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Iron stock solution complete subsection",
        "exact_source_quote": "Iron stock solution: EDTA·Fe(III) 4.5 g Distilled water 1.0 L ",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ],
    "interpretation": "Target composition is empty. Curate the exact named stock definition, with separate preparation basis and receiving dose; the owner already contains it and requires evidence/denominator qualification rather than duplication."
  },
  {
    "decision_id": "q39",
    "ingredient": "Phosphate buffer stock solution composition",
    "decision": "add",
    "stage": "Target missing named stock composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Phosphate buffer stock solution complete subsection",
        "exact_source_quote": "Phosphate buffer stock solution: KH 2 PO 4 37.425 g Na 2 HPO 4 ·2H 2 O 48.950 g Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ],
    "interpretation": "Target composition is empty. Curate the exact named stock definition, with separate preparation basis and receiving dose; the owner already contains it and requires evidence/denominator qualification rather than duplication."
  },
  {
    "decision_id": "q40",
    "ingredient": "Child pH",
    "decision": "add",
    "stage": "Child condition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Child instruction; Child pH",
        "exact_source_quote": "Use Medium No. 815 adjusted pH to 8.0.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "The owner retains the correct target pH 8.0; the target omits it. No adjustment reagent or dose is specified for the child."
  },
  {
    "decision_id": "q41",
    "ingredient": "Child pH",
    "decision": "evidence_only",
    "stage": "Child condition",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "ph_value",
        "stored": 8.0
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Child instruction; Child pH",
        "exact_source_quote": "Use Medium No. 815 adjusted pH to 8.0.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "The owner retains the correct target pH 8.0; the target omits it. No adjustment reagent or dose is specified for the child."
  },
  {
    "decision_id": "q42",
    "ingredient": "Gas composition",
    "decision": "add",
    "stage": "Child condition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "aeration",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Child instruction; Gas composition",
        "exact_source_quote": "Replace the gas phase to methane-air (80:20, v/v).",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "The owner retains the exact 80:20 v/v methane-air mixture. The target separate VARIABLE gas ingredients do not express this condition. No total gas dose or pressure is specified."
  },
  {
    "decision_id": "q43",
    "ingredient": "Gas composition",
    "decision": "evidence_only",
    "stage": "Child condition",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "aeration",
        "stored": "methane-air (80:20, v/v)"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Child instruction; Gas composition",
        "exact_source_quote": "Replace the gas phase to methane-air (80:20, v/v).",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "The owner retains the exact 80:20 v/v methane-air mixture. The target separate VARIABLE gas ingredients do not express this condition. No total gas dose or pressure is specified."
  },
  {
    "decision_id": "q44",
    "ingredient": "Methane and air placeholders",
    "decision": "correct",
    "stage": "Child gas-phase representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "preparation_steps[6]",
        "stored": {
          "step_number": 7,
          "action": "FILTER_STERILIZE",
          "description": "Replace the gas phase with filter-sterilized methane-air (80:20, v/v)."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Gas override",
        "exact_source_quote": "Replace the gas phase to methane-air (80:20, v/v).",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "Represent the specified gas mixture as preparation/atmosphere, not unqualified independent ingredient amounts. The owner preparation retains this ratio and filter-sterilization by scoped parent inheritance; neither volume nor pressure is established."
  },
  {
    "decision_id": "q45",
    "ingredient": "Parent HCl strength and dose",
    "decision": "unsupported",
    "stage": "Excluded parent acid adjustment",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Parent adjustment explicitly overridden",
        "exact_source_quote": "To complete medium, adjust pH to 3.0 with sterile 1 N HCl solution.",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Child pH override",
        "exact_source_quote": "Use Medium No. 815 adjusted pH to 8.0.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      },
      {
        "source_key": "togoM3279original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"1 N HCl solution\"",
        "snapshot_sha256": "d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a"
      }
    ],
    "interpretation": "The target retains a 1 N HCl placeholder copied from the parent. The child overrides pH 3.0 and does not authorize a particular acid/base dose; the owner appropriately removes this inherited instruction. The provider object is retained as source tension, not proof of child use."
  },
  {
    "decision_id": "q46",
    "ingredient": "Parent phosphate 2 ml",
    "decision": "unsupported",
    "stage": "Excluded parent addition",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Parent post-cooling addition",
        "exact_source_quote": "Phosphate buffer stock solution 2.0 ml",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Child phosphate addition override",
        "exact_source_quote": "Reduce the amount of phosphate buffer stock solution to 1.0 ml per liter of the medium.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "The parent 2 ml addition is overridden by the child 1 ml per liter instruction. The M850 mass-unit field is not transferred to this target."
  },
  {
    "decision_id": "q47",
    "ingredient": "Parent pure-methane 100 ml dose",
    "decision": "unsupported",
    "stage": "Excluded parent gas phase",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "preparation_steps[6]",
        "stored": {
          "step_number": 7,
          "action": "FILTER_STERILIZE",
          "description": "Replace the gas phase with filter-sterilized methane-air (80:20, v/v)."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Parent gas instruction",
        "exact_source_quote": "Add 100 ml methane gas (filter-sterilized) into the head space of the culture bottle through a syringe.",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Child gas override",
        "exact_source_quote": "Replace the gas phase to methane-air (80:20, v/v).",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "Do not combine a 100 ml pure-methane injection with the child replacement mixture. The child gas amount and pressure are unquantified."
  },
  {
    "decision_id": "q48",
    "ingredient": "20 ml aliquot",
    "decision": "add",
    "stage": "Inherited parent vessel preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Vessel/aliquot instruction",
        "exact_source_quote": "Then, distribute 20 ml-aliquots of the medium into sterile 120 ml-serum bottles and seal with butyl rubber stoppers.",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Explicit parent invocation",
        "exact_source_quote": "Use Medium No. 815 adjusted pH to 8.0.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "The child invokes the parent and does not override this vessel instruction. Preserve the aliquot and container capacity separately; neither establishes the child gas dose."
  },
  {
    "decision_id": "q49",
    "ingredient": "20 ml aliquot",
    "decision": "evidence_only",
    "stage": "Inherited parent vessel preparation",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "preparation_steps[5]",
        "stored": {
          "step_number": 6,
          "action": "ALIQUOT",
          "description": "Distribute 20 ml aliquots into sterile 120 ml serum bottles and seal with butyl rubber stoppers."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Vessel/aliquot instruction",
        "exact_source_quote": "Then, distribute 20 ml-aliquots of the medium into sterile 120 ml-serum bottles and seal with butyl rubber stoppers.",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Explicit parent invocation",
        "exact_source_quote": "Use Medium No. 815 adjusted pH to 8.0.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "The owner already preserves the exact 20 ml aliquot and 120 ml vessel context; attach evidence without inferring gas amount from capacity."
  },
  {
    "decision_id": "q50",
    "ingredient": "120 ml bottle capacity",
    "decision": "add",
    "stage": "Inherited parent vessel preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Vessel/aliquot instruction",
        "exact_source_quote": "Then, distribute 20 ml-aliquots of the medium into sterile 120 ml-serum bottles and seal with butyl rubber stoppers.",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Explicit parent invocation",
        "exact_source_quote": "Use Medium No. 815 adjusted pH to 8.0.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "The child invokes the parent and does not override this vessel instruction. Preserve the aliquot and container capacity separately; neither establishes the child gas dose."
  },
  {
    "decision_id": "q51",
    "ingredient": "120 ml bottle capacity",
    "decision": "evidence_only",
    "stage": "Inherited parent vessel preparation",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "preparation_steps[5]",
        "stored": {
          "step_number": 6,
          "action": "ALIQUOT",
          "description": "Distribute 20 ml aliquots into sterile 120 ml serum bottles and seal with butyl rubber stoppers."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Vessel/aliquot instruction",
        "exact_source_quote": "Then, distribute 20 ml-aliquots of the medium into sterile 120 ml-serum bottles and seal with butyl rubber stoppers.",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Explicit parent invocation",
        "exact_source_quote": "Use Medium No. 815 adjusted pH to 8.0.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "The owner already preserves the exact 20 ml aliquot and 120 ml vessel context; attach evidence without inferring gas amount from capacity."
  },
  {
    "decision_id": "q52",
    "ingredient": "Autoclave temperature 121°C",
    "decision": "add",
    "stage": "Displayed JCM default for applicable autoclaving",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE",
          "notes": "Autoclave the basal medium and Phosphate buffer stock solution separately; filter-sterilize the methane-air gas phase."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Displayed page default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      },
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Displayed page default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ],
    "interpretation": "Both exact pages display this default, which applies only to autoclaving, not filter-sterilized gas. The owner retains method but no numeric cycle; target has neither. Preserve the unless-otherwise-stated qualification."
  },
  {
    "decision_id": "q53",
    "ingredient": "Autoclave duration 15 min",
    "decision": "add",
    "stage": "Displayed JCM default for applicable autoclaving",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE",
          "notes": "Autoclave the basal medium and Phosphate buffer stock solution separately; filter-sterilize the methane-air gas phase."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Displayed page default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      },
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Displayed page default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ],
    "interpretation": "Both exact pages display this default, which applies only to autoclaving, not filter-sterilized gas. The owner retains method but no numeric cycle; target has neither. Preserve the unless-otherwise-stated qualification."
  },
  {
    "decision_id": "q54",
    "ingredient": "Separate basal/phosphate sterilization and cooling",
    "decision": "add",
    "stage": "Inherited preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Basal and phosphate preparation",
        "exact_source_quote": "Mix components and autoclave. After cooling, add the following solution (autoclaved) to the medium:",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ],
    "interpretation": "The target omits preparation. Preserve basal autoclaving, separately autoclaved phosphate and addition after cooling, with the child phosphate dose override."
  },
  {
    "decision_id": "q55",
    "ingredient": "Separate basal/phosphate sterilization and cooling",
    "decision": "evidence_only",
    "stage": "Inherited preparation",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "preparation_steps[1]",
        "stored": {
          "step_number": 2,
          "action": "AUTOCLAVE",
          "description": "Autoclave the basal medium."
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "preparation_steps[2]",
        "stored": {
          "step_number": 3,
          "action": "AUTOCLAVE",
          "description": "Autoclave the Phosphate buffer stock solution separately."
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE",
          "notes": "Autoclave the basal medium and Phosphate buffer stock solution separately; filter-sterilize the methane-air gas phase."
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Basal and phosphate preparation",
        "exact_source_quote": "Mix components and autoclave. After cooling, add the following solution (autoclaved) to the medium:",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ],
    "interpretation": "The owner already retains the correct sequence and method; attach scoped evidence without treating it as independent experimental verification."
  },
  {
    "decision_id": "q56",
    "ingredient": "Measured final-medium volume",
    "decision": "not_quantified",
    "stage": "Basal preparation plus additions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "DISSOLVE",
            "description": "Dissolve NH4Cl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O in distilled water with 0.1 ml/L Trace element solution and 0.1 ml/L Iron stock solution."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave the basal medium."
          },
          {
            "step_number": 3,
            "action": "AUTOCLAVE",
            "description": "Autoclave the Phosphate buffer stock solution separately."
          },
          {
            "step_number": 4,
            "action": "MIX",
            "description": "After cooling, add 1.0 ml/L sterile Phosphate buffer stock solution to the basal medium."
          },
          {
            "step_number": 5,
            "action": "ADJUST_PH",
            "description": "Adjust the medium to pH 8.0."
          },
          {
            "step_number": 6,
            "action": "ALIQUOT",
            "description": "Distribute 20 ml aliquots into sterile 120 ml serum bottles and seal with butyl rubber stoppers."
          },
          {
            "step_number": 7,
            "action": "FILTER_STERILIZE",
            "description": "Replace the gas phase with filter-sterilized methane-air (80:20, v/v)."
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Basal water entry",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      },
      {
        "source_key": "jcm1428",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428",
        "source_locator": "Child phosphate addition override",
        "exact_source_quote": "Reduce the amount of phosphate buffer stock solution to 1.0 ml per liter of the medium.",
        "snapshot_sha256": "cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9",
        "parsed_text_sha256": "74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef"
      }
    ],
    "interpretation": "Water 1 L plus later stocks is not a measured final volume. The child phosphate dose is explicitly per liter; the remaining batch quantities must retain their stated basis rather than silently treating water as a make-up instruction."
  },
  {
    "decision_id": "q57",
    "ingredient": "KH2PO4",
    "decision": "verified",
    "stage": "External phosphate stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "37.425",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"KH2PO4\",\n                \"compound_id\": 11,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 37.425,\n                \"unit\": \"g\",\n                \"g_l\": 37.425,\n                \"mmol_l\": 275.01,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      },
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      }
    ],
    "interpretation": "Existing attached exact snippet and historical response SHA match the captured bytes; the two g/L values are provider-declared stock concentrations and water is a 1 L batch addition. Verification is limited to this external stock layer, not inherited by owner or target."
  },
  {
    "decision_id": "q58",
    "ingredient": "Na2HPO4 x 2 H2O",
    "decision": "verified",
    "stage": "External phosphate stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "48.95",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Na2HPO4 x 2 H2O\",\n                \"compound_id\": 181,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 48.95,\n                \"unit\": \"g\",\n                \"g_l\": 48.95,\n                \"mmol_l\": 344.818,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      },
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      }
    ],
    "interpretation": "Existing attached exact snippet and historical response SHA match the captured bytes; the two g/L values are provider-declared stock concentrations and water is a 1 L batch addition. Verification is limited to this external stock layer, not inherited by owner or target."
  },
  {
    "decision_id": "q59",
    "ingredient": "Distilled water",
    "decision": "verified",
    "stage": "External phosphate stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      },
      {
        "source_key": "solution4768",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4768",
        "source_locator": "$.data.volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67"
      }
    ],
    "interpretation": "Existing attached exact snippet and historical response SHA match the captured bytes; the two g/L values are provider-declared stock concentrations and water is a 1 L batch addition. Verification is limited to this external stock layer, not inherited by owner or target."
  },
  {
    "decision_id": "q60",
    "ingredient": "Fe(III)-EDTA",
    "decision": "unsupported",
    "stage": "External iron stock, historical source unavailable",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4767_Iron_stock_solution_4_5_g_L.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "4.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Iron stock subsection",
        "exact_source_quote": "EDTA·Fe(III) 4.5 g",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ],
    "interpretation": "The two existing historical API excerpts are preserved in a pinned local derivative plan, but original response cf7e5be1… is not recovered and current requests return 503. Primary supports stock recipe mass/water, not authentication of the historical API g_l/volume declaration. Do not label those existing attachments verified or inherit them into this owner."
  },
  {
    "decision_id": "q61",
    "ingredient": "Distilled water",
    "decision": "evidence_only",
    "stage": "External iron stock, historical source unavailable",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4767_Iron_stock_solution_4_5_g_L.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Iron stock subsection",
        "exact_source_quote": "Iron stock solution: EDTA·Fe(III) 4.5 g Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ],
    "interpretation": "The two existing historical API excerpts are preserved in a pinned local derivative plan, but original response cf7e5be1… is not recovered and current requests return 503. Primary supports stock recipe mass/water, not authentication of the historical API g_l/volume declaration. Do not label those existing attachments verified or inherit them into this owner."
  },
  {
    "decision_id": "q62",
    "ingredient": "Placeholder ingredient",
    "decision": "not_quantified",
    "stage": "External stock placeholder only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4767_Iron_stock_solution_4_5_g_L.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Named stock subsection",
        "exact_source_quote": "Iron stock solution: EDTA·Fe(III) 4.5 g Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ],
    "interpretation": "The VARIABLE see-source placeholder is not an additional chemical or quantified ingredient. Real composition is separate; do not transfer the placeholder into the medium."
  },
  {
    "decision_id": "q63",
    "ingredient": "Placeholder ingredient",
    "decision": "not_quantified",
    "stage": "External stock placeholder only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm815",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815",
        "source_locator": "Named stock subsection",
        "exact_source_quote": "Phosphate buffer stock solution: KH 2 PO 4 37.425 g Na 2 HPO 4 ·2H 2 O 48.950 g Distilled water 1.0 L",
        "snapshot_sha256": "21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae",
        "parsed_text_sha256": "daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005"
      }
    ],
    "interpretation": "The VARIABLE see-source placeholder is not an additional chemical or quantified ingredient. Real composition is separate; do not transfer the placeholder into the medium."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:009693.

15 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 4/6 primary and 4/6 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 6: primary 66.67%; secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Hydrates, EDTA identity and missing reagent specificity

grounding: concern. Targets: CultureMech:009693.

The repaired owner uses explicit source-supported Co/Ni hexahydrates and phosphate dihydrate, whereas parent-context old groundings are anhydrous and are not inherited. Source EDTA·2Na does not specify hydration, so anhydrous CHEBI:64734 needs source-form qualification. EDTA·Fe(III) supports an iron-EDTA moiety but does not specify a counterion or hydration; CHEBI:30729 is an anion, not proof of the weighed reagent salt. No replacement form or molarity is guessed.

### Child overrides and inherited preparation

completeness: concern. Targets: CultureMech:009693.

The owner correctly retains pH 8, methane-air 80:20 v/v, separate phosphate sterilization and 20 ml/120 ml vessel preparation. The target lacks these and retains an obsolete acid placeholder. Displayed 121°C/15 min defaults are available for applicable autoclaving. Child adjustment dose, gas dose/pressure and final measured volume remain unspecified.

### Chemical composition and atmosphere annotations

scope: concern. Targets: CultureMech:009693.

The target COMPLEX/UNDEFINED classification has no listed complex nutrient mixture and differs from the repaired owner DEFINED classification. Reconsider with source-specific reagent/form limits; no automatic score establishes complete chemical definition. LIQUID agrees with the recipe. Owner MICROAEROPHILIC is an interpretation of the specified gas mixture, not an independent physiological growth observation. Nitrogen-source and phosphate-buffer roles are chemically consistent but do not authenticate quantities.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009693.

26 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Record references and external-stock historical evidence

evidence: concern. Targets: CultureMech:009693.

The owner has three bare references and source/notes fields but no attached amount or preparation excerpts. Target has source notes only. All three external 4768 attachments match exact raw/hash; both external 4767 attachments are derivative-only and cannot be authenticated against the unavailable original response. These evidentiary states do not transfer between layers.

## Findings

### f1: Generated target omits the maintained child formulation repair

major / open / confirmed; issue key: stale-generated-representation.

The target retains 1 G_PER_L water, mass-unit liquid stocks, empty stock compositions, unqualified gas ingredients and parent acid placeholder. The owner already restores nested stocks, pH 8 and the child gas mixture.

### f2: Repaired per-liter statements exceed the printed batch basis

major / open / confirmed; issue key: batch-denominator-overstatement.

The owner describes basal grams, 1 L water and 0.1 ml stocks as explicit per-liter source values. The primary prints batch amounts and water without a measured final volume. The trace stock likewise prints batch grams; phosphate stock has separate provider-declared concentrations and the child explicitly declares its 1 ml/L dose.

### f3: EDTA reagent form is more specific than the source establishes

major / open / confirmed; issue key: edta-form-specificity.

The source does not specify hydration for EDTA·2Na or the counterion/hydration of EDTA·Fe(III). The owner asserts anhydrous disodium EDTA and an iron-EDTA anion without reagent-level evidence.

### f4: Claim evidence and exact iron-stock authentication remain incomplete

major / open / confirmed; issue key: source-evidence-and-stock-authentication.

Three owner references are bare URLs, and no owner/target quantity or preparation claim has attached evidence. The asserted 4767 stock retains two historical excerpts whose original raw response is unavailable; exact 4768 evidence is independently authenticated only within that external stock.

### f5: Available sterilization default and classification need scoped curation

minor / open / confirmed; issue key: preparation-default-and-classification.

Exact JCM pages display 121°C for 15 min unless otherwise stated; owner keeps only the autoclave method. Target classification and preparation remain stale. Reagent form limits and interpreted atmosphere labels should remain explicit.

## Recommended Actions And Acceptance Checks

### a1

Reconcile and evidence the maintained owner first, then regenerate the target through the declared generator; verify nested stocks, exact child overrides and evidence survive.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain original batch amounts and water inputs, distinguish nominal preparation bases from measured volume, and preserve explicit provider/child per-liter declarations only within their exact scope.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Qualify the unresolved reagent form and independently verify any proposed supplied-form mapping; do not infer a salt, hydration state or molar conversion.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach source-specific excerpts and metadata; recover exact 4767 accession/response evidence before treating its historical attachments as verified. Preserve required-unavailable status and keep external evidence scope separate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Record the displayed conditional autoclave default at applicable stages and reassess classification from the exact source without converting catalogue intent into observed growth.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch035/349/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch035/349/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml:1:id: CultureMech:009693<br>./data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml:1:id: CultureMech:009693<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch035/source-preflight-bound/349/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 34 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| child | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428; Complete JCM 1428 child instructions | supports | The child overrides parent pH, phosphate dose and gas composition. |
| parent | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815; Basal recipe, preparation and three named stock recipes | supports | The exact parent supplies basal quantities and explicitly named stock formulas; child overrides take precedence. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279; $.meta, two components and comments | supports | TOGO identifies JCM 1428 but retains a parent HCl object alongside child pH 8.0 instructions; the primary resolves that scope tension. |
| parent-provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850; $.meta and named stock components[2..4] | supports | Only the named stock definitions and corresponding parent context support this child; local flattened parent fields do not establish final-medium quantities. |
| parent-local | data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml; Complete pinned input; source-scoped dependency only | context_only | Read full source/context record, including all fields, histories and attached evidence. No entire-parent formula or attachment is inherited by the target. |
| iron-local | data/normalized_yaml/bacterial/mediadive_4767_Iron_stock_solution_4_5_g_L.yaml; Complete pinned input; source-scoped dependency only | context_only | Read full source/context record, including all fields, histories and attached evidence. No entire-parent formula or attachment is inherited by the target. |
| phosphate-local | data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml; Complete pinned input; source-scoped dependency only | context_only | Read full source/context record, including all fields, histories and attached evidence. No entire-parent formula or attachment is inherited by the target. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch035/349/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30729 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30729; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30729 resolves to ethylenediaminetetraacetatoferrate(1-). Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53542 resolves to nickel chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64734; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:64734 resolves to EDTA disodium salt (anhydrous). Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91258 resolves to disodium hydrogenphosphate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30729": [{"label": "Fe(III)-EDTA", "match_type": "preferred_term", "identifier": "CHEBI:30729", "preferred_term": "Fe(III)-EDTA", "ontology_id": "CHEBI:30729", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53542": [{"label": "Nickel (II) chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53542", "preferred_term": "Nickel (II) chloride hexahydrate", "ontology_id": "CHEBI:53542", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:64734": [{"label": "Na2-EDTA", "match_type": "preferred_term", "identifier": "CHEBI:64734", "preferred_term": "Na2-EDTA", "ontology_id": "CHEBI:64734", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91258": [{"label": "Na2HPO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml; data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml", "events": 13, "timestamp_issues": []}] |
| writer-0 | scripts/repair_togo_m3279_alkaline_diluted_ams_score15.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Full current targeted repair source was read. It writes fixed per-liter signatures, forms, three bare references and quality flags after an exact-ID/signature guard; it does not supply claim-level excerpts or establish measured final volumes. Current code and recorded September history are provenance, not authenticated historical remote responses. |
| writer-1 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Full current targeted repair source was read. It writes fixed per-liter signatures, forms, three bare references and quality flags after an exact-ID/signature guard; it does not supply claim-level excerpts or establish measured final volumes. Current code and recorded September history are provenance, not authenticated historical remote responses. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Full current targeted repair source was read. It writes fixed per-liter signatures, forms, three bare references and quality flags after an exact-ID/signature guard; it does not supply claim-level excerpts or establish measured final volumes. Current code and recorded September history are provenance, not authenticated historical remote responses. |
| historical-0 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/records/bacterial/mediadive_4767_Iron_stock_solution_4_5_g_L.yaml.md; Pinned historical concentration plan/report; exact row correspondence | context_only | Local derivative documentation corroborates recorded decisions but is not original public response bytes. Only the independent matching 4768 raw capture authenticates its three stock attachments. |
| historical-1 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/records/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml.md; Pinned historical concentration plan/report; exact row correspondence | context_only | Local derivative documentation corroborates recorded decisions but is not original public response bytes. Only the independent matching 4768 raw capture authenticates its three stock attachments. |
| phosphate-api | https://mediadive.dsmz.de/rest/solution/4768; $.data complete exact stock response | supports | The stock accession and its three evidence objects match the exact historical response hash; this verification stays inside the external stock. |
| solution4767-attempt | https://mediadive.dsmz.de/rest/solution/4767; Preserved exact public retrieval result | context_only | Exact MediaDive 4767 and its separately preserved retry return 503. Two historical local excerpts remain derivative-only; original response cf7e5be177e4c6e16506daa65f21cef4189eecade344fab01f83de936f8f825f was not recovered. Required asserted-stock identity/evidence authentication is incomplete, though JCM 815 directly supports the named stock recipe. |
| solution4767Retry1-attempt | https://mediadive.dsmz.de/rest/solution/4767; Preserved exact public retrieval result | context_only | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |
| mediadiveJ1428-attempt | https://mediadive.dsmz.de/rest/medium/J1428; Preserved exact public retrieval result | context_only | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |
| mediadiveJ1428Retry1-attempt | https://mediadive.dsmz.de/rest/medium/J1428; Preserved exact public retrieval result | context_only | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |
| mediadiveJ815-attempt | https://mediadive.dsmz.de/rest/medium/J815; Preserved exact public retrieval result | context_only | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |
| mediadiveJ815Retry1-attempt | https://mediadive.dsmz.de/rest/medium/J815; Preserved exact public retrieval result | context_only | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |
| togoM3279-attempt | https://mediumapi.dbcls.jp/medium/M3279; Preserved exact public retrieval result | context_only | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |
| togoM850-attempt | https://mediumapi.dbcls.jp/medium/M850; Preserved exact public retrieval result | context_only | Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact MediaDive 4767 and its separately preserved retry return 503. Two historical local excerpts remain derivative-only; original response cf7e5be177e4c6e16506daa65f21cef4189eecade344fab01f83de936f8f825f was not recovered. Required asserted-stock identity/evidence authentication is incomplete, though JCM 815 directly supports the named stock recipe.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO endpoints remain usable. This attempt does not supply absent original historical bytes.
- Only explicitly invoked parent basal and named stock recipes are transferred. Parent pH 3.0, phosphate 2 ml and 100 ml pure methane are overridden. Parent M850 unrelated variant-child pH 6.7, old anhydrous mappings and flattened amounts are not inherited. No percent basis, reagent counterion, gas dose or measured final volume is invented.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T192058Z-culturemech-009693-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaline_diluted_ams_medium (CultureMech:009693)'
started_at: '2026-10-21T19:13:57Z'
finished_at: '2026-10-21T19:20:58Z'
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
summary: JCM 1428 explicitly modifies JCM 815. The maintained owner preserves the
  child pH, gas ratio and nested stocks, while the generated target remains stale.
  Batch-denominator and claim-evidence qualifications remain necessary; exact historical
  MediaDive 4767 authentication is unavailable.
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
  - path: data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml
    sha256: 2b1e0c2fcf6c4da7d78b56ac278b4c78b91b23a1ba9e2817db27faef95a65489
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
    sha256: e68c62bea1f376623654e0f5235d433a3380d9c19fea05061eb2d13de8ec9678
    role: context
  - path: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
    sha256: 91f15b59bcfbd0b4f9a773d1fa7e0ebbc5d17dc8f6b9f320834f9f26ed55a83a
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4767_Iron_stock_solution_4_5_g_L.yaml
    sha256: d83c8553482d6523b1ac8c0af65a5a451558057b468bf0f78773eeefd25aeabc
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
    sha256: 60a2ad5d759b91ea153f23d8b3ae4bc7ead87f38accac1219fe4806fd5272ab0
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/plan.json
    sha256: 8b48afea717d9dd21cbd91fa1d7dff8b329d3ba973435a466ec236b436b8240c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/records/bacterial/mediadive_4767_Iron_stock_solution_4_5_g_L.yaml.md
    sha256: 0be19c48f4ad3cdc823e68c89807f53e13d57af73820c29455d685d94a405146
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/records/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml.md
    sha256: bdd6c39996ef7a679d4aa7865039dd5c2694d91ced720af748e6e8d41d247888
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
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/record_io.py
    sha256: bff4715f85d7ff2ff681b88f0a2de2667e5767d7a2c196bd50a37d5d329957ac
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/repair_togo_m3279_alkaline_diluted_ams_score15.py
    sha256: 846001cfb9ad2215d838414ecda604e535c27419cb7407c58d369cb148e8d041
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
    sha256: 64a778108fd3197a8cc08082f80c1de3ec33eda58350cee5df612ab61d23cea1
    role: context
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 349; batch 035 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-four task batches
    contain 340 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 343 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009693
targets:
- target_id: CultureMech:009693
  path: data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml
  label: alkaline_diluted_ams_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch035/349/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch035/349/strict.tsv"
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009693
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
  - CultureMech:009693
- check_id: solution4767-source-access
  name: 'Exact source content access: solution4767'
  required: true
  status: unavailable
  summary: Exact MediaDive 4767 and its separately preserved retry return 503. Two
    historical local excerpts remain derivative-only; original response cf7e5be177e4c6e16506daa65f21cef4189eecade344fab01f83de936f8f825f
    was not recovered. Required asserted-stock identity/evidence authentication is
    incomplete, though JCM 815 directly supports the named stock recipe.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - solution4767-attempt
- check_id: solution4767Retry1-source-access
  name: 'Exact source content access: solution4767Retry1'
  required: false
  status: unavailable
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - solution4767Retry1-attempt
- check_id: mediadiveJ1428-source-access
  name: 'Exact source content access: mediadiveJ1428'
  required: false
  status: unavailable
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - mediadiveJ1428-attempt
- check_id: mediadiveJ1428Retry1-source-access
  name: 'Exact source content access: mediadiveJ1428Retry1'
  required: false
  status: unavailable
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - mediadiveJ1428Retry1-attempt
- check_id: mediadiveJ815-source-access
  name: 'Exact source content access: mediadiveJ815'
  required: false
  status: unavailable
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - mediadiveJ815-attempt
- check_id: mediadiveJ815Retry1-source-access
  name: 'Exact source content access: mediadiveJ815Retry1'
  required: false
  status: unavailable
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - mediadiveJ815Retry1-attempt
- check_id: togoM3279-source-access
  name: 'Exact source content access: togoM3279'
  required: false
  status: unavailable
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - togoM3279-attempt
- check_id: togoM850-source-access
  name: 'Exact source content access: togoM850'
  required: false
  status: unavailable
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - togoM850-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T19:20:56Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T19:20:56Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:46.381990Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch035/349/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:47.596428Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch035/349/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:48.939081Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:49.767174Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T19:20:56Z'
  support: supports
  summary: './data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml:1:id: CultureMech:009693

    ./data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml:1:id: CultureMech:009693

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/source-preflight-bound/349/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T19:20:56Z'
  support: supports
  summary: 34 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 7831614cd91253c5f2a0208b59627d730ee9f1e5e8a3e3d6cb9c238db1d2f6e5
- evidence_id: child
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428
  locator: Complete JCM 1428 child instructions
  accessed_at: '2026-10-21T19:02:24.938518Z'
  support: supports
  summary: The child overrides parent pH, phosphate dose and gas composition.
  quote: Use Medium No. 815 adjusted pH to 8.0.  Reduce the amount of phosphate buffer
    stock solution to 1.0 ml per liter of the medium.  Replace the gas phase to methane-air
    (80:20, v/v).
  snapshot_sha256: cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9
- evidence_id: parent
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815
  locator: Basal recipe, preparation and three named stock recipes
  accessed_at: '2026-10-21T10:33:41.274966Z'
  support: supports
  summary: The exact parent supplies basal quantities and explicitly named stock formulas;
    child overrides take precedence.
  quote: 'NH 4 Cl 0.1 g MgSO 4 ·7H 2 O 0.1 g CaCl 2 ·2H 2 O 0.02 g Trace element solution
    (see below) 0.1 ml Iron stock solution (see below) 0.1 ml Distilled water 1.0
    L Mix components and autoclave. After cooling, add the following solution (autoclaved)
    to the medium: Phosphate buffer stock solution 2.0 ml To complete medium, adjust
    pH to 3.0 with sterile 1 N HCl solution.  Then, distribute 20 ml-aliquots of the
    medium into sterile 120 ml-serum bottles and seal with butyl rubber stoppers.  Add
    100 ml methane gas (filter-sterilized) into the head space of the culture bottle
    through a syringe. Trace element solution: ZnSO 4 ·7H 2 O 0.4 g EDTA·2Na 0.25
    g MnCl 2 ·4H 2 O 0.02 g H 3 BO 3 0.015 g Na 2 MoO 4 ·2H 2 O 0.04 g NiCl 2 ·6H
    2 O 0.01 g CuSO 4 ·5H 2 O 0.2 g CoCl 2 ·6H 2 O 0.05 g Distilled water 1.0 L Iron
    stock solution: EDTA·Fe(III) 4.5 g Distilled water 1.0 L Phosphate buffer stock
    solution: KH 2 PO 4 37.425 g Na 2 HPO 4 ·2H 2 O 48.950 g Distilled water 1.0 L'
  snapshot_sha256: 21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279
  locator: $.meta, two components and comments
  accessed_at: '2026-10-21T19:02:24.348747Z'
  support: supports
  summary: TOGO identifies JCM 1428 but retains a parent HCl object alongside child
    pH 8.0 instructions; the primary resolves that scope tension.
  quote: '"original_media_id": "JCM_M1428"'
  snapshot_sha256: d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a
- evidence_id: parent-provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850
  locator: $.meta and named stock components[2..4]
  accessed_at: '2026-10-21T10:33:39.735634Z'
  support: supports
  summary: Only the named stock definitions and corresponding parent context support
    this child; local flattened parent fields do not establish final-medium quantities.
  quote: '"original_media_id": "JCM_M815"'
  snapshot_sha256: 034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b
- evidence_id: parent-local
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml
  locator: Complete pinned input; source-scoped dependency only
  accessed_at: '2026-10-21T19:20:56Z'
  support: context_only
  summary: Read full source/context record, including all fields, histories and attached
    evidence. No entire-parent formula or attachment is inherited by the target.
  snapshot_sha256: e68c62bea1f376623654e0f5235d433a3380d9c19fea05061eb2d13de8ec9678
- evidence_id: iron-local
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_4767_Iron_stock_solution_4_5_g_L.yaml
  locator: Complete pinned input; source-scoped dependency only
  accessed_at: '2026-10-21T19:20:56Z'
  support: context_only
  summary: Read full source/context record, including all fields, histories and attached
    evidence. No entire-parent formula or attachment is inherited by the target.
  snapshot_sha256: d83c8553482d6523b1ac8c0af65a5a451558057b468bf0f78773eeefd25aeabc
- evidence_id: phosphate-local
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml
  locator: Complete pinned input; source-scoped dependency only
  accessed_at: '2026-10-21T19:20:56Z'
  support: context_only
  summary: Read full source/context record, including all fields, histories and attached
    evidence. No entire-parent formula or attachment is inherited by the target.
  snapshot_sha256: 0616e7b8dfeb6a49f26c17de757518844bd43b65e7255012e1e58da144e2dc91
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/349/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T19:20:56Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 958f2033c94afb0b1e149b2e388bc4c12de641eb35972f22b72584c18ec745e5
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
- evidence_id: chebi30729
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30729
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T14:35:47.488497Z'
  support: supports
  summary: CHEBI:30729 resolves to ethylenediaminetetraacetatoferrate(1-). Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: e9163d86299489e8bf0a7c758ba8664b3643bb582761cd2fe670f96af028721c
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
- evidence_id: chebi53542
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:31.075912Z'
  support: supports
  summary: CHEBI:53542 resolves to nickel chloride hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
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
  accessed_at: '2026-10-21T19:20:56Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:30729": [{"label": "Fe(III)-EDTA", "match_type":
    "preferred_term", "identifier": "CHEBI:30729", "preferred_term": "Fe(III)-EDTA",
    "ontology_id": "CHEBI:30729", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier":
    "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118":
    [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate",
    "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:53542": [{"label": "Nickel (II) chloride
    hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53542", "preferred_term":
    "Nickel (II) chloride hexahydrate", "ontology_id": "CHEBI:53542", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:64734":
    [{"label": "Na2-EDTA", "match_type": "preferred_term", "identifier": "CHEBI:64734",
    "preferred_term": "Na2-EDTA", "ontology_id": "CHEBI:64734", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368":
    [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91258": [{"label": "Na2HPO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:91258", "preferred_term":
    "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml; data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T19:20:56Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml", "events": 13,
    "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_togo_m3279_alkaline_diluted_ams_score15.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:20:56Z'
  support: context_only
  summary: Full current targeted repair source was read. It writes fixed per-liter
    signatures, forms, three bare references and quality flags after an exact-ID/signature
    guard; it does not supply claim-level excerpts or establish measured final volumes.
    Current code and recorded September history are provenance, not authenticated
    historical remote responses.
  snapshot_sha256: 846001cfb9ad2215d838414ecda604e535c27419cb7407c58d369cb148e8d041
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:20:56Z'
  support: context_only
  summary: Full current targeted repair source was read. It writes fixed per-liter
    signatures, forms, three bare references and quality flags after an exact-ID/signature
    guard; it does not supply claim-level excerpts or establish measured final volumes.
    Current code and recorded September history are provenance, not authenticated
    historical remote responses.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:20:56Z'
  support: context_only
  summary: Full current targeted repair source was read. It writes fixed per-liter
    signatures, forms, three bare references and quality flags after an exact-ID/signature
    guard; it does not supply claim-level excerpts or establish measured final volumes.
    Current code and recorded September history are provenance, not authenticated
    historical remote responses.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: historical-0
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/records/bacterial/mediadive_4767_Iron_stock_solution_4_5_g_L.yaml.md
  locator: Pinned historical concentration plan/report; exact row correspondence
  accessed_at: '2026-10-21T19:20:56Z'
  support: context_only
  summary: Local derivative documentation corroborates recorded decisions but is not
    original public response bytes. Only the independent matching 4768 raw capture
    authenticates its three stock attachments.
  snapshot_sha256: 0be19c48f4ad3cdc823e68c89807f53e13d57af73820c29455d685d94a405146
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/records/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml.md
  locator: Pinned historical concentration plan/report; exact row correspondence
  accessed_at: '2026-10-21T19:20:56Z'
  support: context_only
  summary: Local derivative documentation corroborates recorded decisions but is not
    original public response bytes. Only the independent matching 4768 raw capture
    authenticates its three stock attachments.
  snapshot_sha256: bdd6c39996ef7a679d4aa7865039dd5c2694d91ced720af748e6e8d41d247888
- evidence_id: phosphate-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4768
  locator: $.data complete exact stock response
  accessed_at: '2026-10-21T10:33:38.860496Z'
  support: supports
  summary: The stock accession and its three evidence objects match the exact historical
    response hash; this verification stays inside the external stock.
  quote: '"id": 4768'
  snapshot_sha256: 8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67
- evidence_id: solution4767-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4767
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:02:23.205616Z'
  support: context_only
  summary: Exact MediaDive 4767 and its separately preserved retry return 503. Two
    historical local excerpts remain derivative-only; original response cf7e5be177e4c6e16506daa65f21cef4189eecade344fab01f83de936f8f825f
    was not recovered. Required asserted-stock identity/evidence authentication is
    incomplete, though JCM 815 directly supports the named stock recipe.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: solution4767Retry1-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4767
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:03:32.500814Z'
  support: context_only
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ1428-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1428
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:02:22.563616Z'
  support: context_only
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ1428Retry1-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1428
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:03:31.440096Z'
  support: context_only
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ815-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J815
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:02:22.563693Z'
  support: context_only
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ815Retry1-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J815
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:03:31.968774Z'
  support: context_only
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: togoM3279-attempt
  kind: database
  reference: https://mediumapi.dbcls.jp/medium/M3279
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:02:23.295997Z'
  support: context_only
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
- evidence_id: togoM850-attempt
  kind: database
  reference: https://mediumapi.dbcls.jp/medium/M850
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:02:23.296114Z'
  support: context_only
  summary: Preserved alternate/current endpoint failure; exact JCM primaries and original
    TOGO endpoints remain usable. This attempt does not supply absent original historical
    bytes.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact child and explicitly invoked parent
  outcome: supported
  summary: TOGO M3279/JCM 1428 explicitly invokes JCM 815 with pH 8.0, 1 ml phosphate
    stock per liter and methane-air 80:20 v/v. The maintained owner and target share
    the exact stable ID and complete merge provenance. Parent pH 3.0, parent phosphate
    2 ml and 100 ml pure methane are excluded from child transfer. No species-specific
    growth evidence is asserted.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - record
  - owner-0
  - child
  - parent
  - provider
- assessment_id: ownership
  area: ownership
  topic: Repaired maintained source versus stale generated target
  outcome: concern
  summary: The September owner repair nests all three stock compositions, restores
    volume units, pH and gas preparation, and removes the parent acid adjustment.
    The generated target retains old empty stocks, mass units for liquid additions,
    gas placeholders and HCl. Owner notes and bare source references do not authenticate
    quantities or final-volume denominators.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - record
  - owner-0
  - child
  - parent
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 63 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"ingredient\": \"NH4Cl\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"Inherited basal batch\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Basal recipe; NH4Cl\",\n        \"exact_source_quote\"\
    : \"NH 4 Cl 0.1 g\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM3279original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact original batch\
    \ amount and the separately listed 1 L water. The owner numerical conversion does\
    \ not establish a final measured denominator; its notes call the printed amount\
    \ g/L or ml/L although the primary table gives batch grams or water volume.\"\n\
    \  },\n  {\n    \"decision_id\": \"q2\",\n    \"ingredient\": \"MgSO4·7H2O\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"Inherited basal batch\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Basal recipe; MgSO4·7H2O\",\n        \"exact_source_quote\"\
    : \"MgSO 4 ·7H 2 O 0.1 g\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM3279original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4·7H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact original batch\
    \ amount and the separately listed 1 L water. The owner numerical conversion does\
    \ not establish a final measured denominator; its notes call the printed amount\
    \ g/L or ml/L although the primary table gives batch grams or water volume.\"\n\
    \  },\n  {\n    \"decision_id\": \"q3\",\n    \"ingredient\": \"CaCl2·2H2O\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"Inherited basal batch\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Basal recipe; CaCl2·2H2O\",\n        \"exact_source_quote\"\
    : \"CaCl 2 ·2H 2 O 0.02 g\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM3279original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2·2H2O\\\",\\n          \\\"volume\\\": 0.02,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact original batch\
    \ amount and the separately listed 1 L water. The owner numerical conversion does\
    \ not establish a final measured denominator; its notes call the printed amount\
    \ g/L or ml/L although the primary table gives batch grams or water volume.\"\n\
    \  },\n  {\n    \"decision_id\": \"q4\",\n    \"ingredient\": \"Distilled water\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Inherited basal batch\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"ML_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Basal recipe; Distilled water\",\n        \"\
    exact_source_quote\": \"Distilled water 1.0 L\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM3279original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact original batch\
    \ amount and the separately listed 1 L water. The owner numerical conversion does\
    \ not establish a final measured denominator; its notes call the printed amount\
    \ g/L or ml/L although the primary table gives batch grams or water volume. The\
    \ target additionally stores water as 1 G_PER_L, which is a wrong unit.\"\n  },\n\
    \  {\n    \"decision_id\": \"q5\",\n    \"ingredient\": \"Trace element solution\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Basal stock addition\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"DISSOLVE\",\n        \
    \  \"description\": \"Dissolve NH4Cl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O in distilled\
    \ water with 0.1 ml/L Trace element solution and 0.1 ml/L Iron stock solution.\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Basal table; Trace element solution\",\n    \
    \    \"exact_source_quote\": \"Trace element solution (see below) 0.1 ml\",\n\
    \        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM3279original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution (see Medium [M850])\\\"\
    ,\\n          \\\"volume\\\": 0.1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n \
    \       \"snapshot_sha256\": \"d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a\"\
    \n      }\n    ],\n    \"interpretation\": \"The target uses G_PER_L for a 0.1\
    \ ml dose. The owner restores volume but calls it ml/L; qualify it as the stated\
    \ basal batch addition unless an explicit final denominator is documented. Do\
    \ not add the whole stock preparation to the basal batch.\"\n  },\n  {\n    \"\
    decision_id\": \"q6\",\n    \"ingredient\": \"Iron stock solution\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Basal stock addition\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"DISSOLVE\",\n        \
    \  \"description\": \"Dissolve NH4Cl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O in distilled\
    \ water with 0.1 ml/L Trace element solution and 0.1 ml/L Iron stock solution.\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Basal table; Iron stock solution\",\n       \
    \ \"exact_source_quote\": \"Iron stock solution (see below) 0.1 ml\",\n      \
    \  \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM3279original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Iron stock solution (see Medium [M850])\\\",\\\
    n          \\\"volume\\\": 0.1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n    \
    \    \"snapshot_sha256\": \"d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a\"\
    \n      }\n    ],\n    \"interpretation\": \"The target uses G_PER_L for a 0.1\
    \ ml dose. The owner restores volume but calls it ml/L; qualify it as the stated\
    \ basal batch addition unless an explicit final denominator is documented. Do\
    \ not add the whole stock preparation to the basal batch.\"\n  },\n  {\n    \"\
    decision_id\": \"q7\",\n    \"ingredient\": \"Phosphate stock addition\",\n  \
    \  \"decision\": \"correct\",\n    \"stage\": \"Child final-medium addition\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1428\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\"\
    ,\n        \"source_locator\": \"Child phosphate addition override\",\n      \
    \  \"exact_source_quote\": \"Reduce the amount of phosphate buffer stock solution\
    \ to 1.0 ml per liter of the medium.\",\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      },\n      {\n        \"source_key\": \"togoM3279original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Phosphate buffer stock solution (see Medium [M850])\\\
    \",\\n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n \
    \       \"snapshot_sha256\": \"d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a\"\
    \n      }\n    ],\n    \"interpretation\": \"The child explicitly supplies 1 ml\
    \ per liter. Correct target G_PER_L to the liquid addition basis; do not inherit\
    \ the parent 2 ml dose.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"ingredient\"\
    : \"Phosphate stock addition\",\n    \"decision\": \"evidence_only\",\n    \"\
    stage\": \"Child final-medium addition\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[3]\",\n        \"stored\": {\n\
    \          \"step_number\": 4,\n          \"action\": \"MIX\",\n          \"description\"\
    : \"After cooling, add 1.0 ml/L sterile Phosphate buffer stock solution to the\
    \ basal medium.\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"jcm1428\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\"\
    ,\n        \"source_locator\": \"Child phosphate addition override\",\n      \
    \  \"exact_source_quote\": \"Reduce the amount of phosphate buffer stock solution\
    \ to 1.0 ml per liter of the medium.\",\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner already retains 1.0 ML_PER_L\
    \ and the correct after-cooling addition. Attach claim-level evidence; its current\
    \ references alone are not an attached amount excerpt.\"\n  },\n  {\n    \"decision_id\"\
    : \"q9\",\n    \"ingredient\": \"ZnSO4 x 7 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"stage\": \"Trace element solution\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; ZnSO4 x 7\
    \ H2O\",\n        \"exact_source_quote\": \"ZnSO 4 ·7H 2 O 0.4 g\",\n        \"\
    snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 0.4,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner preserves this stock-local\
    \ amount and has no attached claim evidence. The primary prints batch grams with\
    \ 1 L water. Preserve those original units and qualify the owner note that claims\
    \ the primary prints g/L; do not assert a measured stock volume or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q10\",\n    \"ingredient\"\
    : \"ZnSO4 x 7 H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened\
    \ M850 dependency; Trace element solution\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; ZnSO4 x 7\
    \ H2O\",\n        \"exact_source_quote\": \"ZnSO 4 ·7H 2 O 0.4 g\",\n        \"\
    snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 0.4,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"This parent-context field flattens\
    \ a named stock amount into direct ingredients; retain its exact stock stage for\
    \ the child. The local parent value is not evidence of final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q11\",\n    \"ingredient\": \"EDTA x 2Na\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Trace element solution\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; EDTA x 2Na\"\
    ,\n        \"exact_source_quote\": \"EDTA·2Na 0.25 g\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"EDTA・2Na\\\",\\n          \\\"volume\\\": 0.25,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner preserves this stock-local\
    \ amount and has no attached claim evidence. The primary prints batch grams with\
    \ 1 L water. Preserve those original units and qualify the owner note that claims\
    \ the primary prints g/L; do not assert a measured stock volume or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n    \"ingredient\"\
    : \"EDTA x 2Na\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened\
    \ M850 dependency; Trace element solution\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; EDTA x 2Na\"\
    ,\n        \"exact_source_quote\": \"EDTA·2Na 0.25 g\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"EDTA・2Na\\\",\\n          \\\"volume\\\": 0.25,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"This parent-context field flattens\
    \ a named stock amount into direct ingredients; retain its exact stock stage for\
    \ the child. The local parent value is not evidence of final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q13\",\n    \"ingredient\": \"MnCl2 x 4 H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Trace element solution\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; MnCl2 x 4\
    \ H2O\",\n        \"exact_source_quote\": \"MnCl 2 ·4H 2 O 0.02 g\",\n       \
    \ \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2・4H2O\\\",\\n          \\\"volume\\\": 0.02,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner preserves this stock-local\
    \ amount and has no attached claim evidence. The primary prints batch grams with\
    \ 1 L water. Preserve those original units and qualify the owner note that claims\
    \ the primary prints g/L; do not assert a measured stock volume or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"ingredient\"\
    : \"MnCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened\
    \ M850 dependency; Trace element solution\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; MnCl2 x 4\
    \ H2O\",\n        \"exact_source_quote\": \"MnCl 2 ·4H 2 O 0.02 g\",\n       \
    \ \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2・4H2O\\\",\\n          \\\"volume\\\": 0.02,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"This parent-context field flattens\
    \ a named stock amount into direct ingredients; retain its exact stock stage for\
    \ the child. The local parent value is not evidence of final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q15\",\n    \"ingredient\": \"H3BO3\",\n \
    \   \"decision\": \"correct\",\n    \"stage\": \"Trace element solution\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.015\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; H3BO3\",\n\
    \        \"exact_source_quote\": \"H 3 BO 3 0.015 g\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 0.015,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner preserves this stock-local\
    \ amount and has no attached claim evidence. The primary prints batch grams with\
    \ 1 L water. Preserve those original units and qualify the owner note that claims\
    \ the primary prints g/L; do not assert a measured stock volume or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"ingredient\"\
    : \"H3BO3\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened M850\
    \ dependency; Trace element solution\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.015\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; H3BO3\",\n\
    \        \"exact_source_quote\": \"H 3 BO 3 0.015 g\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 0.015,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"This parent-context field flattens\
    \ a named stock amount into direct ingredients; retain its exact stock stage for\
    \ the child. The local parent value is not evidence of final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q17\",\n    \"ingredient\": \"Na2MoO4 x 2\
    \ H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Trace element solution\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[4].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.04\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; Na2MoO4 x\
    \ 2 H2O\",\n        \"exact_source_quote\": \"Na 2 MoO 4 ·2H 2 O 0.04 g\",\n \
    \       \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 0.04,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\n      }\n\
    \    ],\n    \"interpretation\": \"The owner preserves this stock-local amount\
    \ and has no attached claim evidence. The primary prints batch grams with 1 L\
    \ water. Preserve those original units and qualify the owner note that claims\
    \ the primary prints g/L; do not assert a measured stock volume or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n    \"ingredient\"\
    : \"Na2MoO4 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened\
    \ M850 dependency; Trace element solution\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.04\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; Na2MoO4 x\
    \ 2 H2O\",\n        \"exact_source_quote\": \"Na 2 MoO 4 ·2H 2 O 0.04 g\",\n \
    \       \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 0.04,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\n      }\n\
    \    ],\n    \"interpretation\": \"This parent-context field flattens a named\
    \ stock amount into direct ingredients; retain its exact stock stage for the child.\
    \ The local parent value is not evidence of final-medium concentration.\"\n  },\n\
    \  {\n    \"decision_id\": \"q19\",\n    \"ingredient\": \"NiCl2 x 6 H2O\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"Trace element solution\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[5].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; NiCl2 x 6\
    \ H2O\",\n        \"exact_source_quote\": \"NiCl 2 ·6H 2 O 0.01 g\",\n       \
    \ \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2・6H2O\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner preserves this stock-local\
    \ amount and has no attached claim evidence. The primary prints batch grams with\
    \ 1 L water. Preserve those original units and qualify the owner note that claims\
    \ the primary prints g/L; do not assert a measured stock volume or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q20\",\n    \"ingredient\"\
    : \"NiCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened\
    \ M850 dependency; Trace element solution\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; NiCl2 x 6\
    \ H2O\",\n        \"exact_source_quote\": \"NiCl 2 ·6H 2 O 0.01 g\",\n       \
    \ \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2・6H2O\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"This parent-context field flattens\
    \ a named stock amount into direct ingredients; retain its exact stock stage for\
    \ the child. The local parent value is not evidence of final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q21\",\n    \"ingredient\": \"CuSO4 x 5 H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Trace element solution\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[6].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; CuSO4 x 5\
    \ H2O\",\n        \"exact_source_quote\": \"CuSO 4 ·5H 2 O 0.2 g\",\n        \"\
    snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuSO4・5H2O\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner preserves this stock-local\
    \ amount and has no attached claim evidence. The primary prints batch grams with\
    \ 1 L water. Preserve those original units and qualify the owner note that claims\
    \ the primary prints g/L; do not assert a measured stock volume or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"ingredient\"\
    : \"CuSO4 x 5 H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened\
    \ M850 dependency; Trace element solution\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; CuSO4 x 5\
    \ H2O\",\n        \"exact_source_quote\": \"CuSO 4 ·5H 2 O 0.2 g\",\n        \"\
    snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuSO4・5H2O\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"This parent-context field flattens\
    \ a named stock amount into direct ingredients; retain its exact stock stage for\
    \ the child. The local parent value is not evidence of final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q23\",\n    \"ingredient\": \"CoCl2 x 6 H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Trace element solution\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[7].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; CoCl2 x 6\
    \ H2O\",\n        \"exact_source_quote\": \"CoCl 2 ·6H 2 O 0.05 g\",\n       \
    \ \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 0.05,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner preserves this stock-local\
    \ amount and has no attached claim evidence. The primary prints batch grams with\
    \ 1 L water. Preserve those original units and qualify the owner note that claims\
    \ the primary prints g/L; do not assert a measured stock volume or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q24\",\n    \"ingredient\"\
    : \"CoCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened\
    \ M850 dependency; Trace element solution\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; CoCl2 x 6\
    \ H2O\",\n        \"exact_source_quote\": \"CoCl 2 ·6H 2 O 0.05 g\",\n       \
    \ \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 0.05,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"This parent-context field flattens\
    \ a named stock amount into direct ingredients; retain its exact stock stage for\
    \ the child. The local parent value is not evidence of final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q25\",\n    \"ingredient\": \"Distilled water\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Trace element solution\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[8].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; Distilled\
    \ water\",\n        \"exact_source_quote\": \"Trace element solution: ZnSO 4 ·7H\
    \ 2 O 0.4 g EDTA·2Na 0.25 g MnCl 2 ·4H 2 O 0.02 g H 3 BO 3 0.015 g Na 2 MoO 4\
    \ ·2H 2 O 0.04 g NiCl 2 ·6H 2 O 0.01 g CuSO 4 ·5H 2 O 0.2 g CoCl 2 ·6H 2 O 0.05\
    \ g Distilled water 1.0 L \",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner preserves this stock-local\
    \ amount and has no attached claim evidence. Its 1 L water is a preparation input\
    \ within this stock, not extra water added to the receiving medium or a measured\
    \ final volume.\"\n  },\n  {\n    \"decision_id\": \"q26\",\n    \"ingredient\"\
    : \"Distilled water\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened\
    \ M850 dependency; Trace element solution\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution subsection; Distilled\
    \ water\",\n        \"exact_source_quote\": \"Trace element solution: ZnSO 4 ·7H\
    \ 2 O 0.4 g EDTA·2Na 0.25 g MnCl 2 ·4H 2 O 0.02 g H 3 BO 3 0.015 g Na 2 MoO 4\
    \ ·2H 2 O 0.04 g NiCl 2 ·6H 2 O 0.01 g CuSO 4 ·5H 2 O 0.2 g CoCl 2 ·6H 2 O 0.05\
    \ g Distilled water 1.0 L \",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"This parent-context field flattens\
    \ a named stock amount into direct ingredients; retain its exact stock stage for\
    \ the child. The local parent value is not evidence of final-medium concentration.\
    \ The single collapsed water field cannot stand for all basal and three stock\
    \ water inputs.\"\n  },\n  {\n    \"decision_id\": \"q27\",\n    \"ingredient\"\
    : \"EDTA x Fe(III)\",\n    \"decision\": \"correct\",\n    \"stage\": \"Iron stock\
    \ solution\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"4.5\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Iron stock solution subsection; EDTA x Fe(III)\"\
    ,\n        \"exact_source_quote\": \"EDTA·Fe(III) 4.5 g\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"EDTA・Fe(III)\\\",\\n          \\\"volume\\\":\
    \ 4.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\n      }\n\
    \    ],\n    \"interpretation\": \"The owner preserves this stock-local amount\
    \ and has no attached claim evidence. The primary prints batch grams with 1 L\
    \ water. Preserve those original units and qualify the owner note that claims\
    \ the primary prints g/L; do not assert a measured stock volume or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q28\",\n    \"ingredient\"\
    : \"EDTA x Fe(III)\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened\
    \ M850 dependency; Iron stock solution\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Iron stock solution subsection; EDTA x Fe(III)\"\
    ,\n        \"exact_source_quote\": \"EDTA·Fe(III) 4.5 g\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"EDTA・Fe(III)\\\",\\n          \\\"volume\\\":\
    \ 4.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\n      }\n\
    \    ],\n    \"interpretation\": \"This parent-context field flattens a named\
    \ stock amount into direct ingredients; retain its exact stock stage for the child.\
    \ The local parent value is not evidence of final-medium concentration.\"\n  },\n\
    \  {\n    \"decision_id\": \"q29\",\n    \"ingredient\": \"Distilled water\",\n\
    \    \"decision\": \"evidence_only\",\n    \"stage\": \"Iron stock solution\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Iron stock solution subsection; Distilled water\"\
    ,\n        \"exact_source_quote\": \"Iron stock solution: EDTA·Fe(III) 4.5 g Distilled\
    \ water 1.0 L \",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner preserves this stock-local\
    \ amount and has no attached claim evidence. Its 1 L water is a preparation input\
    \ within this stock, not extra water added to the receiving medium or a measured\
    \ final volume.\"\n  },\n  {\n    \"decision_id\": \"q30\",\n    \"ingredient\"\
    : \"Distilled water\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened\
    \ M850 dependency; Iron stock solution\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Iron stock solution subsection; Distilled water\"\
    ,\n        \"exact_source_quote\": \"Iron stock solution: EDTA·Fe(III) 4.5 g Distilled\
    \ water 1.0 L \",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"This parent-context field flattens\
    \ a named stock amount into direct ingredients; retain its exact stock stage for\
    \ the child. The local parent value is not evidence of final-medium concentration.\
    \ The single collapsed water field cannot stand for all basal and three stock\
    \ water inputs.\"\n  },\n  {\n    \"decision_id\": \"q31\",\n    \"ingredient\"\
    : \"KH2PO4\",\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Phosphate\
    \ buffer stock solution\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\",\n     \
    \   \"field_path\": \"solutions[2].composition[0].concentration\",\n        \"\
    stored\": {\n          \"value\": \"37.425\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Phosphate buffer stock solution subsection; KH2PO4\"\
    ,\n        \"exact_source_quote\": \"KH 2 PO 4 37.425 g\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[4].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 37.425,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      },\n      {\n        \"source_key\": \"solution4768\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4768\",\n        \"source_locator\"\
    : \"$.data.recipe[0]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 1,\\n                \\\"compound\\\": \\\"KH2PO4\\\"\
    ,\\n                \\\"compound_id\\\": 11,\\n                \\\"solution\\\"\
    : null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 37.425,\\n                \\\"unit\\\": \\\"g\\\",\\n                \\\"\
    g_l\\\": 37.425,\\n                \\\"mmol_l\\\": 275.01,\\n                \\\
    \"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\": \"8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner preserves this stock-local\
    \ amount and has no attached claim evidence. The independent exact phosphate API\
    \ explicitly declares the same stock g/L value and 1000 ml basis. That support\
    \ does not transfer an existing evidence attachment from the external stock into\
    \ this owner.\"\n  },\n  {\n    \"decision_id\": \"q32\",\n    \"ingredient\"\
    : \"KH2PO4\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened M850\
    \ dependency; Phosphate buffer stock solution\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"37.425\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Phosphate buffer stock solution subsection; KH2PO4\"\
    ,\n        \"exact_source_quote\": \"KH 2 PO 4 37.425 g\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[4].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 37.425,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      },\n      {\n        \"source_key\": \"solution4768\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4768\",\n        \"source_locator\"\
    : \"$.data.recipe[0]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 1,\\n                \\\"compound\\\": \\\"KH2PO4\\\"\
    ,\\n                \\\"compound_id\\\": 11,\\n                \\\"solution\\\"\
    : null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 37.425,\\n                \\\"unit\\\": \\\"g\\\",\\n                \\\"\
    g_l\\\": 37.425,\\n                \\\"mmol_l\\\": 275.01,\\n                \\\
    \"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\": \"8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67\"\
    \n      }\n    ],\n    \"interpretation\": \"This parent-context field flattens\
    \ a named stock amount into direct ingredients; retain its exact stock stage for\
    \ the child. The local parent value is not evidence of final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q33\",\n    \"ingredient\": \"Na2HPO4 x 2\
    \ H2O\",\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Phosphate buffer\
    \ stock solution\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"48.950\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Phosphate buffer stock solution subsection; Na2HPO4\
    \ x 2 H2O\",\n        \"exact_source_quote\": \"Na 2 HPO 4 ·2H 2 O 48.950 g\"\
    ,\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[4].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2HPO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 48.95,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\n     \
    \ },\n      {\n        \"source_key\": \"solution4768\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4768\",\n        \"source_locator\"\
    : \"$.data.recipe[1]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 2,\\n                \\\"compound\\\": \\\"Na2HPO4 x\
    \ 2 H2O\\\",\\n                \\\"compound_id\\\": 181,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 48.95,\\n                \\\"unit\\\": \\\"g\\\
    \",\\n                \\\"g_l\\\": 48.95,\\n                \\\"mmol_l\\\": 344.818,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The owner preserves this stock-local amount\
    \ and has no attached claim evidence. The independent exact phosphate API explicitly\
    \ declares the same stock g/L value and 1000 ml basis. That support does not transfer\
    \ an existing evidence attachment from the external stock into this owner.\"\n\
    \  },\n  {\n    \"decision_id\": \"q34\",\n    \"ingredient\": \"Na2HPO4 x 2 H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened M850 dependency;\
    \ Phosphate buffer stock solution\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"48.95\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Phosphate buffer stock solution subsection; Na2HPO4\
    \ x 2 H2O\",\n        \"exact_source_quote\": \"Na 2 HPO 4 ·2H 2 O 48.950 g\"\
    ,\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[4].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2HPO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 48.95,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\n     \
    \ },\n      {\n        \"source_key\": \"solution4768\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4768\",\n        \"source_locator\"\
    : \"$.data.recipe[1]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 2,\\n                \\\"compound\\\": \\\"Na2HPO4 x\
    \ 2 H2O\\\",\\n                \\\"compound_id\\\": 181,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 48.95,\\n                \\\"unit\\\": \\\"g\\\
    \",\\n                \\\"g_l\\\": 48.95,\\n                \\\"mmol_l\\\": 344.818,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67\"\n     \
    \ }\n    ],\n    \"interpretation\": \"This parent-context field flattens a named\
    \ stock amount into direct ingredients; retain its exact stock stage for the child.\
    \ The local parent value is not evidence of final-medium concentration.\"\n  },\n\
    \  {\n    \"decision_id\": \"q35\",\n    \"ingredient\": \"Distilled water\",\n\
    \    \"decision\": \"evidence_only\",\n    \"stage\": \"Phosphate buffer stock\
    \ solution\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Phosphate buffer stock solution subsection; Distilled\
    \ water\",\n        \"exact_source_quote\": \"Phosphate buffer stock solution:\
    \ KH 2 PO 4 37.425 g Na 2 HPO 4 ·2H 2 O 48.950 g Distilled water 1.0 L\",\n  \
    \      \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[4].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner preserves this stock-local\
    \ amount and has no attached claim evidence. Its 1 L water is a preparation input\
    \ within this stock, not extra water added to the receiving medium or a measured\
    \ final volume.\"\n  },\n  {\n    \"decision_id\": \"q36\",\n    \"ingredient\"\
    : \"Distilled water\",\n    \"decision\": \"correct\",\n    \"stage\": \"Flattened\
    \ M850 dependency; Phosphate buffer stock solution\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Phosphate buffer stock solution subsection; Distilled\
    \ water\",\n        \"exact_source_quote\": \"Phosphate buffer stock solution:\
    \ KH 2 PO 4 37.425 g Na 2 HPO 4 ·2H 2 O 48.950 g Distilled water 1.0 L\",\n  \
    \      \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"togoM850original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M850\"\
    ,\n        \"source_locator\": \"$.components[4].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"034cd091a879d4861231c40171e1d96c02587dcc8ed399a34fc207e651a02f4b\"\
    \n      }\n    ],\n    \"interpretation\": \"This parent-context field flattens\
    \ a named stock amount into direct ingredients; retain its exact stock stage for\
    \ the child. The local parent value is not evidence of final-medium concentration.\
    \ The single collapsed water field cannot stand for all basal and three stock\
    \ water inputs.\"\n  },\n  {\n    \"decision_id\": \"q37\",\n    \"ingredient\"\
    : \"Trace element solution composition\",\n    \"decision\": \"add\",\n    \"\
    stage\": \"Target missing named stock composition\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Trace element solution complete subsection\"\
    ,\n        \"exact_source_quote\": \"Trace element solution: ZnSO 4 ·7H 2 O 0.4\
    \ g EDTA·2Na 0.25 g MnCl 2 ·4H 2 O 0.02 g H 3 BO 3 0.015 g Na 2 MoO 4 ·2H 2 O\
    \ 0.04 g NiCl 2 ·6H 2 O 0.01 g CuSO 4 ·5H 2 O 0.2 g CoCl 2 ·6H 2 O 0.05 g Distilled\
    \ water 1.0 L \",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ],\n    \"interpretation\": \"Target composition is empty. Curate\
    \ the exact named stock definition, with separate preparation basis and receiving\
    \ dose; the owner already contains it and requires evidence/denominator qualification\
    \ rather than duplication.\"\n  },\n  {\n    \"decision_id\": \"q38\",\n    \"\
    ingredient\": \"Iron stock solution composition\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"Target missing named stock composition\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Iron stock solution complete subsection\",\n\
    \        \"exact_source_quote\": \"Iron stock solution: EDTA·Fe(III) 4.5 g Distilled\
    \ water 1.0 L \",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ],\n    \"interpretation\": \"Target composition is empty. Curate\
    \ the exact named stock definition, with separate preparation basis and receiving\
    \ dose; the owner already contains it and requires evidence/denominator qualification\
    \ rather than duplication.\"\n  },\n  {\n    \"decision_id\": \"q39\",\n    \"\
    ingredient\": \"Phosphate buffer stock solution composition\",\n    \"decision\"\
    : \"add\",\n    \"stage\": \"Target missing named stock composition\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Phosphate buffer stock solution complete subsection\"\
    ,\n        \"exact_source_quote\": \"Phosphate buffer stock solution: KH 2 PO\
    \ 4 37.425 g Na 2 HPO 4 ·2H 2 O 48.950 g Distilled water 1.0 L\",\n        \"\
    snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ],\n    \"interpretation\": \"Target composition is empty. Curate\
    \ the exact named stock definition, with separate preparation basis and receiving\
    \ dose; the owner already contains it and requires evidence/denominator qualification\
    \ rather than duplication.\"\n  },\n  {\n    \"decision_id\": \"q40\",\n    \"\
    ingredient\": \"Child pH\",\n    \"decision\": \"add\",\n    \"stage\": \"Child\
    \ condition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1428\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\"\
    ,\n        \"source_locator\": \"Child instruction; Child pH\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 815 adjusted pH to 8.0.\",\n        \"snapshot_sha256\": \"\
    cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\",\n        \"\
    parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner retains the correct target\
    \ pH 8.0; the target omits it. No adjustment reagent or dose is specified for\
    \ the child.\"\n  },\n  {\n    \"decision_id\": \"q41\",\n    \"ingredient\":\
    \ \"Child pH\",\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Child\
    \ condition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 8.0\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1428\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\"\
    ,\n        \"source_locator\": \"Child instruction; Child pH\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 815 adjusted pH to 8.0.\",\n        \"snapshot_sha256\": \"\
    cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\",\n        \"\
    parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner retains the correct target\
    \ pH 8.0; the target omits it. No adjustment reagent or dose is specified for\
    \ the child.\"\n  },\n  {\n    \"decision_id\": \"q42\",\n    \"ingredient\":\
    \ \"Gas composition\",\n    \"decision\": \"add\",\n    \"stage\": \"Child condition\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"aeration\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1428\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\"\
    ,\n        \"source_locator\": \"Child instruction; Gas composition\",\n     \
    \   \"exact_source_quote\": \"Replace the gas phase to methane-air (80:20, v/v).\"\
    ,\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner retains the exact 80:20\
    \ v/v methane-air mixture. The target separate VARIABLE gas ingredients do not\
    \ express this condition. No total gas dose or pressure is specified.\"\n  },\n\
    \  {\n    \"decision_id\": \"q43\",\n    \"ingredient\": \"Gas composition\",\n\
    \    \"decision\": \"evidence_only\",\n    \"stage\": \"Child condition\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"aeration\",\n        \"stored\": \"methane-air (80:20,\
    \ v/v)\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1428\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\"\
    ,\n        \"source_locator\": \"Child instruction; Gas composition\",\n     \
    \   \"exact_source_quote\": \"Replace the gas phase to methane-air (80:20, v/v).\"\
    ,\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner retains the exact 80:20\
    \ v/v methane-air mixture. The target separate VARIABLE gas ingredients do not\
    \ express this condition. No total gas dose or pressure is specified.\"\n  },\n\
    \  {\n    \"decision_id\": \"q44\",\n    \"ingredient\": \"Methane and air placeholders\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Child gas-phase representation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[6]\",\n        \"stored\": {\n\
    \          \"step_number\": 7,\n          \"action\": \"FILTER_STERILIZE\",\n\
    \          \"description\": \"Replace the gas phase with filter-sterilized methane-air\
    \ (80:20, v/v).\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"jcm1428\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\"\
    ,\n        \"source_locator\": \"Gas override\",\n        \"exact_source_quote\"\
    : \"Replace the gas phase to methane-air (80:20, v/v).\",\n        \"snapshot_sha256\"\
    : \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\",\n    \
    \    \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the specified gas mixture\
    \ as preparation/atmosphere, not unqualified independent ingredient amounts. The\
    \ owner preparation retains this ratio and filter-sterilization by scoped parent\
    \ inheritance; neither volume nor pressure is established.\"\n  },\n  {\n    \"\
    decision_id\": \"q45\",\n    \"ingredient\": \"Parent HCl strength and dose\"\
    ,\n    \"decision\": \"unsupported\",\n    \"stage\": \"Excluded parent acid adjustment\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Parent adjustment explicitly overridden\",\n\
    \        \"exact_source_quote\": \"To complete medium, adjust pH to 3.0 with sterile\
    \ 1 N HCl solution.\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"jcm1428\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\",\n        \"source_locator\"\
    : \"Child pH override\",\n        \"exact_source_quote\": \"Use Medium No. 815\
    \ adjusted pH to 8.0.\",\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      },\n      {\n        \"source_key\": \"togoM3279original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3279\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"1 N HCl solution\\\"\",\n        \"snapshot_sha256\"\
    : \"d6ccb9f9cf915c440007ea085d787a736155d5ed81ba11e77bd82b009e19287a\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The target retains a 1 N HCl placeholder\
    \ copied from the parent. The child overrides pH 3.0 and does not authorize a\
    \ particular acid/base dose; the owner appropriately removes this inherited instruction.\
    \ The provider object is retained as source tension, not proof of child use.\"\
    \n  },\n  {\n    \"decision_id\": \"q46\",\n    \"ingredient\": \"Parent phosphate\
    \ 2 ml\",\n    \"decision\": \"unsupported\",\n    \"stage\": \"Excluded parent\
    \ addition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M850_Acidic_Diluted_ASM_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Parent post-cooling addition\",\n        \"exact_source_quote\"\
    : \"Phosphate buffer stock solution 2.0 ml\",\n        \"snapshot_sha256\": \"\
    21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n        \"\
    parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"jcm1428\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\",\n        \"source_locator\"\
    : \"Child phosphate addition override\",\n        \"exact_source_quote\": \"Reduce\
    \ the amount of phosphate buffer stock solution to 1.0 ml per liter of the medium.\"\
    ,\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"The parent 2 ml addition is overridden\
    \ by the child 1 ml per liter instruction. The M850 mass-unit field is not transferred\
    \ to this target.\"\n  },\n  {\n    \"decision_id\": \"q47\",\n    \"ingredient\"\
    : \"Parent pure-methane 100 ml dose\",\n    \"decision\": \"unsupported\",\n \
    \   \"stage\": \"Excluded parent gas phase\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[6]\",\n        \"stored\": {\n\
    \          \"step_number\": 7,\n          \"action\": \"FILTER_STERILIZE\",\n\
    \          \"description\": \"Replace the gas phase with filter-sterilized methane-air\
    \ (80:20, v/v).\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Parent gas instruction\",\n        \"exact_source_quote\"\
    : \"Add 100 ml methane gas (filter-sterilized) into the head space of the culture\
    \ bottle through a syringe.\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"jcm1428\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\",\n        \"source_locator\"\
    : \"Child gas override\",\n        \"exact_source_quote\": \"Replace the gas phase\
    \ to methane-air (80:20, v/v).\",\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"Do not combine a 100 ml pure-methane\
    \ injection with the child replacement mixture. The child gas amount and pressure\
    \ are unquantified.\"\n  },\n  {\n    \"decision_id\": \"q48\",\n    \"ingredient\"\
    : \"20 ml aliquot\",\n    \"decision\": \"add\",\n    \"stage\": \"Inherited parent\
    \ vessel preparation\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm815\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\",\n        \"source_locator\"\
    : \"Vessel/aliquot instruction\",\n        \"exact_source_quote\": \"Then, distribute\
    \ 20 ml-aliquots of the medium into sterile 120 ml-serum bottles and seal with\
    \ butyl rubber stoppers.\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"jcm1428\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\",\n        \"source_locator\"\
    : \"Explicit parent invocation\",\n        \"exact_source_quote\": \"Use Medium\
    \ No. 815 adjusted pH to 8.0.\",\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"The child invokes the parent and\
    \ does not override this vessel instruction. Preserve the aliquot and container\
    \ capacity separately; neither establishes the child gas dose.\"\n  },\n  {\n\
    \    \"decision_id\": \"q49\",\n    \"ingredient\": \"20 ml aliquot\",\n    \"\
    decision\": \"evidence_only\",\n    \"stage\": \"Inherited parent vessel preparation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[5]\",\n        \"stored\": {\n\
    \          \"step_number\": 6,\n          \"action\": \"ALIQUOT\",\n         \
    \ \"description\": \"Distribute 20 ml aliquots into sterile 120 ml serum bottles\
    \ and seal with butyl rubber stoppers.\"\n        }\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm815\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\",\n        \"source_locator\"\
    : \"Vessel/aliquot instruction\",\n        \"exact_source_quote\": \"Then, distribute\
    \ 20 ml-aliquots of the medium into sterile 120 ml-serum bottles and seal with\
    \ butyl rubber stoppers.\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"jcm1428\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\",\n        \"source_locator\"\
    : \"Explicit parent invocation\",\n        \"exact_source_quote\": \"Use Medium\
    \ No. 815 adjusted pH to 8.0.\",\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner already preserves the exact\
    \ 20 ml aliquot and 120 ml vessel context; attach evidence without inferring gas\
    \ amount from capacity.\"\n  },\n  {\n    \"decision_id\": \"q50\",\n    \"ingredient\"\
    : \"120 ml bottle capacity\",\n    \"decision\": \"add\",\n    \"stage\": \"Inherited\
    \ parent vessel preparation\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm815\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\",\n        \"source_locator\"\
    : \"Vessel/aliquot instruction\",\n        \"exact_source_quote\": \"Then, distribute\
    \ 20 ml-aliquots of the medium into sterile 120 ml-serum bottles and seal with\
    \ butyl rubber stoppers.\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"jcm1428\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\",\n        \"source_locator\"\
    : \"Explicit parent invocation\",\n        \"exact_source_quote\": \"Use Medium\
    \ No. 815 adjusted pH to 8.0.\",\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"The child invokes the parent and\
    \ does not override this vessel instruction. Preserve the aliquot and container\
    \ capacity separately; neither establishes the child gas dose.\"\n  },\n  {\n\
    \    \"decision_id\": \"q51\",\n    \"ingredient\": \"120 ml bottle capacity\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Inherited parent vessel\
    \ preparation\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[5]\",\n        \"stored\": {\n\
    \          \"step_number\": 6,\n          \"action\": \"ALIQUOT\",\n         \
    \ \"description\": \"Distribute 20 ml aliquots into sterile 120 ml serum bottles\
    \ and seal with butyl rubber stoppers.\"\n        }\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm815\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\",\n        \"source_locator\"\
    : \"Vessel/aliquot instruction\",\n        \"exact_source_quote\": \"Then, distribute\
    \ 20 ml-aliquots of the medium into sterile 120 ml-serum bottles and seal with\
    \ butyl rubber stoppers.\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"jcm1428\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\",\n        \"source_locator\"\
    : \"Explicit parent invocation\",\n        \"exact_source_quote\": \"Use Medium\
    \ No. 815 adjusted pH to 8.0.\",\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner already preserves the exact\
    \ 20 ml aliquot and 120 ml vessel context; attach evidence without inferring gas\
    \ amount from capacity.\"\n  },\n  {\n    \"decision_id\": \"q52\",\n    \"ingredient\"\
    : \"Autoclave temperature 121°C\",\n    \"decision\": \"add\",\n    \"stage\"\
    : \"Displayed JCM default for applicable autoclaving\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\",\n          \"notes\": \"Autoclave the basal medium\
    \ and Phosphate buffer stock solution separately; filter-sterilize the methane-air\
    \ gas phase.\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"jcm1428\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\"\
    ,\n        \"source_locator\": \"Displayed page default\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      },\n      {\n        \"source_key\": \"jcm815\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\",\n        \"source_locator\"\
    : \"Displayed page default\",\n        \"exact_source_quote\": \"Unless otherwise\
    \ stated, sterilize media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ],\n    \"interpretation\": \"Both exact pages display this default,\
    \ which applies only to autoclaving, not filter-sterilized gas. The owner retains\
    \ method but no numeric cycle; target has neither. Preserve the unless-otherwise-stated\
    \ qualification.\"\n  },\n  {\n    \"decision_id\": \"q53\",\n    \"ingredient\"\
    : \"Autoclave duration 15 min\",\n    \"decision\": \"add\",\n    \"stage\": \"\
    Displayed JCM default for applicable autoclaving\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\",\n          \"notes\": \"Autoclave the basal medium\
    \ and Phosphate buffer stock solution separately; filter-sterilize the methane-air\
    \ gas phase.\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"jcm1428\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\"\
    ,\n        \"source_locator\": \"Displayed page default\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      },\n      {\n        \"source_key\": \"jcm815\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\",\n        \"source_locator\"\
    : \"Displayed page default\",\n        \"exact_source_quote\": \"Unless otherwise\
    \ stated, sterilize media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\"\
    : \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\",\n    \
    \    \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ],\n    \"interpretation\": \"Both exact pages display this default,\
    \ which applies only to autoclaving, not filter-sterilized gas. The owner retains\
    \ method but no numeric cycle; target has neither. Preserve the unless-otherwise-stated\
    \ qualification.\"\n  },\n  {\n    \"decision_id\": \"q54\",\n    \"ingredient\"\
    : \"Separate basal/phosphate sterilization and cooling\",\n    \"decision\": \"\
    add\",\n    \"stage\": \"Inherited preparation\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Basal and phosphate preparation\",\n        \"\
    exact_source_quote\": \"Mix components and autoclave. After cooling, add the following\
    \ solution (autoclaved) to the medium:\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ],\n    \"interpretation\": \"The target omits preparation. Preserve\
    \ basal autoclaving, separately autoclaved phosphate and addition after cooling,\
    \ with the child phosphate dose override.\"\n  },\n  {\n    \"decision_id\": \"\
    q55\",\n    \"ingredient\": \"Separate basal/phosphate sterilization and cooling\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Inherited preparation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1]\",\n        \"stored\": {\n\
    \          \"step_number\": 2,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Autoclave the basal medium.\"\n        }\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2]\",\n        \"stored\": {\n\
    \          \"step_number\": 3,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Autoclave the Phosphate buffer stock solution separately.\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\",\n          \"notes\": \"Autoclave the basal medium\
    \ and Phosphate buffer stock solution separately; filter-sterilize the methane-air\
    \ gas phase.\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Basal and phosphate preparation\",\n        \"\
    exact_source_quote\": \"Mix components and autoclave. After cooling, add the following\
    \ solution (autoclaved) to the medium:\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ],\n    \"interpretation\": \"The owner already retains the correct\
    \ sequence and method; attach scoped evidence without treating it as independent\
    \ experimental verification.\"\n  },\n  {\n    \"decision_id\": \"q56\",\n   \
    \ \"ingredient\": \"Measured final-medium volume\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"stage\": \"Basal preparation plus additions\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Diluted_AMS_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"DISSOLVE\"\
    ,\n            \"description\": \"Dissolve NH4Cl, MgSO4 x 7 H2O, and CaCl2 x 2\
    \ H2O in distilled water with 0.1 ml/L Trace element solution and 0.1 ml/L Iron\
    \ stock solution.\"\n          },\n          {\n            \"step_number\": 2,\n\
    \            \"action\": \"AUTOCLAVE\",\n            \"description\": \"Autoclave\
    \ the basal medium.\"\n          },\n          {\n            \"step_number\"\
    : 3,\n            \"action\": \"AUTOCLAVE\",\n            \"description\": \"\
    Autoclave the Phosphate buffer stock solution separately.\"\n          },\n  \
    \        {\n            \"step_number\": 4,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"After cooling, add 1.0 ml/L sterile Phosphate\
    \ buffer stock solution to the basal medium.\"\n          },\n          {\n  \
    \          \"step_number\": 5,\n            \"action\": \"ADJUST_PH\",\n     \
    \       \"description\": \"Adjust the medium to pH 8.0.\"\n          },\n    \
    \      {\n            \"step_number\": 6,\n            \"action\": \"ALIQUOT\"\
    ,\n            \"description\": \"Distribute 20 ml aliquots into sterile 120 ml\
    \ serum bottles and seal with butyl rubber stoppers.\"\n          },\n       \
    \   {\n            \"step_number\": 7,\n            \"action\": \"FILTER_STERILIZE\"\
    ,\n            \"description\": \"Replace the gas phase with filter-sterilized\
    \ methane-air (80:20, v/v).\"\n          }\n        ]\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm815\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\",\n  \
    \      \"source_locator\": \"Basal water entry\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      },\n      {\n        \"source_key\": \"jcm1428\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428\",\n        \"source_locator\"\
    : \"Child phosphate addition override\",\n        \"exact_source_quote\": \"Reduce\
    \ the amount of phosphate buffer stock solution to 1.0 ml per liter of the medium.\"\
    ,\n        \"snapshot_sha256\": \"cd864505b23e28349932918803c6e51ec6ef2e58df32e792eceecafbe9285fd9\"\
    ,\n        \"parsed_text_sha256\": \"74d5125dd8e1ed668eb95b22d615cf773a86719d1abe895c9b733635e1126eef\"\
    \n      }\n    ],\n    \"interpretation\": \"Water 1 L plus later stocks is not\
    \ a measured final volume. The child phosphate dose is explicitly per liter; the\
    \ remaining batch quantities must retain their stated basis rather than silently\
    \ treating water as a make-up instruction.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q57\",\n    \"ingredient\": \"KH2PO4\",\n    \"decision\": \"verified\",\n\
    \    \"stage\": \"External phosphate stock only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"37.425\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
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
    \n      },\n      {\n        \"source_key\": \"solution4768\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4768\",\n        \"source_locator\"\
    : \"$.data.volume\",\n        \"exact_source_quote\": \"\\\"volume\\\": 1000\"\
    ,\n        \"snapshot_sha256\": \"8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing attached exact snippet and\
    \ historical response SHA match the captured bytes; the two g/L values are provider-declared\
    \ stock concentrations and water is a 1 L batch addition. Verification is limited\
    \ to this external stock layer, not inherited by owner or target.\"\n  },\n  {\n\
    \    \"decision_id\": \"q58\",\n    \"ingredient\": \"Na2HPO4 x 2 H2O\",\n   \
    \ \"decision\": \"verified\",\n    \"stage\": \"External phosphate stock only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"48.95\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
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
    \n      },\n      {\n        \"source_key\": \"solution4768\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4768\",\n        \"source_locator\"\
    : \"$.data.volume\",\n        \"exact_source_quote\": \"\\\"volume\\\": 1000\"\
    ,\n        \"snapshot_sha256\": \"8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing attached exact snippet and\
    \ historical response SHA match the captured bytes; the two g/L values are provider-declared\
    \ stock concentrations and water is a 1 L batch addition. Verification is limited\
    \ to this external stock layer, not inherited by owner or target.\"\n  },\n  {\n\
    \    \"decision_id\": \"q59\",\n    \"ingredient\": \"Distilled water\",\n   \
    \ \"decision\": \"verified\",\n    \"stage\": \"External phosphate stock only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        }\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"solution4768\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4768\",\n\
    \        \"source_locator\": \"$.data.recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 3,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 1000,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67\"\
    \n      },\n      {\n        \"source_key\": \"solution4768\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4768\",\n        \"source_locator\"\
    : \"$.data.volume\",\n        \"exact_source_quote\": \"\\\"volume\\\": 1000\"\
    ,\n        \"snapshot_sha256\": \"8433ae440986f80624703f925963ba80e1f7bc5e0372112ef61b614dcd8fff67\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing attached exact snippet and\
    \ historical response SHA match the captured bytes; the two g/L values are provider-declared\
    \ stock concentrations and water is a 1 L batch addition. Verification is limited\
    \ to this external stock layer, not inherited by owner or target.\"\n  },\n  {\n\
    \    \"decision_id\": \"q60\",\n    \"ingredient\": \"Fe(III)-EDTA\",\n    \"\
    decision\": \"unsupported\",\n    \"stage\": \"External iron stock, historical\
    \ source unavailable\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/mediadive_4767_Iron_stock_solution_4_5_g_L.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Iron stock subsection\",\n        \"exact_source_quote\"\
    : \"EDTA·Fe(III) 4.5 g\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ],\n    \"interpretation\": \"The two existing historical API excerpts\
    \ are preserved in a pinned local derivative plan, but original response cf7e5be1…\
    \ is not recovered and current requests return 503. Primary supports stock recipe\
    \ mass/water, not authentication of the historical API g_l/volume declaration.\
    \ Do not label those existing attachments verified or inherit them into this owner.\"\
    \n  },\n  {\n    \"decision_id\": \"q61\",\n    \"ingredient\": \"Distilled water\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"stage\": \"External iron stock,\
    \ historical source unavailable\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/mediadive_4767_Iron_stock_solution_4_5_g_L.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        }\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm815\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Iron stock subsection\",\n        \"exact_source_quote\"\
    : \"Iron stock solution: EDTA·Fe(III) 4.5 g Distilled water 1.0 L\",\n       \
    \ \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ],\n    \"interpretation\": \"The two existing historical API excerpts\
    \ are preserved in a pinned local derivative plan, but original response cf7e5be1…\
    \ is not recovered and current requests return 503. Primary supports stock recipe\
    \ mass/water, not authentication of the historical API g_l/volume declaration.\
    \ Do not label those existing attachments verified or inherit them into this owner.\"\
    \n  },\n  {\n    \"decision_id\": \"q62\",\n    \"ingredient\": \"Placeholder\
    \ ingredient\",\n    \"decision\": \"not_quantified\",\n    \"stage\": \"External\
    \ stock placeholder only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/mediadive_4767_Iron_stock_solution_4_5_g_L.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Named stock subsection\",\n        \"exact_source_quote\"\
    : \"Iron stock solution: EDTA·Fe(III) 4.5 g Distilled water 1.0 L\",\n       \
    \ \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ],\n    \"interpretation\": \"The VARIABLE see-source placeholder\
    \ is not an additional chemical or quantified ingredient. Real composition is\
    \ separate; do not transfer the placeholder into the medium.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q63\",\n    \"ingredient\": \"Placeholder ingredient\",\n\
    \    \"decision\": \"not_quantified\",\n    \"stage\": \"External stock placeholder\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4768_Phosphate_buffer_stock_solution.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm815\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815\"\
    ,\n        \"source_locator\": \"Named stock subsection\",\n        \"exact_source_quote\"\
    : \"Phosphate buffer stock solution: KH 2 PO 4 37.425 g Na 2 HPO 4 ·2H 2 O 48.950\
    \ g Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"21e3c9b4ac98aff864f265752cf5fc38936e18f8e217464201aa7bfd707d65ae\"\
    ,\n        \"parsed_text_sha256\": \"daec80130a9fd0b3af0fb31a3dcad0369da2193038793af586c8efcd6f752005\"\
    \n      }\n    ],\n    \"interpretation\": \"The VARIABLE see-source placeholder\
    \ is not an additional chemical or quantified ingredient. Real composition is\
    \ separate; do not transfer the placeholder into the medium.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '15 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 4/6 primary
    and 4/6 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi30729
  - chebi31206
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi33118
  - chebi53503
  - chebi53542
  - chebi63036
  - chebi64734
  - chebi75213
  - chebi86158
  - chebi86368
  - chebi91258
  details: 'Instance coverage on a 0–100 percent scale, denominator 6: primary 66.67%;
    secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: forms
  area: grounding
  topic: Hydrates, EDTA identity and missing reagent specificity
  outcome: concern
  summary: The repaired owner uses explicit source-supported Co/Ni hexahydrates and
    phosphate dihydrate, whereas parent-context old groundings are anhydrous and are
    not inherited. Source EDTA·2Na does not specify hydration, so anhydrous CHEBI:64734
    needs source-form qualification. EDTA·Fe(III) supports an iron-EDTA moiety but
    does not specify a counterion or hydration; CHEBI:30729 is an anion, not proof
    of the weighed reagent salt. No replacement form or molarity is guessed.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - parent
  - chebi64734
  - chebi30729
  - chebi53503
  - chebi53542
  - chebi91258
- assessment_id: preparation
  area: completeness
  topic: Child overrides and inherited preparation
  outcome: concern
  summary: The owner correctly retains pH 8, methane-air 80:20 v/v, separate phosphate
    sterilization and 20 ml/120 ml vessel preparation. The target lacks these and
    retains an obsolete acid placeholder. Displayed 121°C/15 min defaults are available
    for applicable autoclaving. Child adjustment dose, gas dose/pressure and final
    measured volume remain unspecified.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - child
  - parent
  - record
  - owner-0
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Chemical composition and atmosphere annotations
  outcome: concern
  summary: The target COMPLEX/UNDEFINED classification has no listed complex nutrient
    mixture and differs from the repaired owner DEFINED classification. Reconsider
    with source-specific reagent/form limits; no automatic score establishes complete
    chemical definition. LIQUID agrees with the recipe. Owner MICROAEROPHILIC is an
    interpretation of the specified gas mixture, not an independent physiological
    growth observation. Nitrogen-source and phosphate-buffer roles are chemically
    consistent but do not authenticate quantities.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - record
  - owner-0
  - child
  - parent
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 26 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: provenance
  area: evidence
  topic: Record references and external-stock historical evidence
  outcome: concern
  summary: The owner has three bare references and source/notes fields but no attached
    amount or preparation excerpts. Target has source notes only. All three external
    4768 attachments match exact raw/hash; both external 4767 attachments are derivative-only
    and cannot be authenticated against the unavailable original response. These evidentiary
    states do not transfer between layers.
  target_ids:
  - CultureMech:009693
  evidence_ids:
  - record
  - owner-0
  - iron-local
  - phosphate-local
  - phosphate-api
  - quantity-inventory
findings:
- finding_id: f1
  issue_key: stale-generated-representation
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Generated target omits the maintained child formulation repair
  description: The target retains 1 G_PER_L water, mass-unit liquid stocks, empty
    stock compositions, unqualified gas ingredients and parent acid placeholder. The
    owner already restores nested stocks, pH 8 and the child gas mixture.
  target_ids:
  - CultureMech:009693
  field_paths:
  - ingredients
  - solutions
  - ph_value
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - child
  - parent
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
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
  issue_key: batch-denominator-overstatement
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Repaired per-liter statements exceed the printed batch basis
  description: The owner describes basal grams, 1 L water and 0.1 ml stocks as explicit
    per-liter source values. The primary prints batch amounts and water without a
    measured final volume. The trace stock likewise prints batch grams; phosphate
    stock has separate provider-declared concentrations and the child explicitly declares
    its 1 ml/L dose.
  target_ids:
  - CultureMech:009693
  field_paths:
  - ingredients
  - solutions[0]
  - solutions[1]
  - preparation_steps[0]
  evidence_ids:
  - parent
  - child
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
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
  issue_key: edta-form-specificity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: EDTA reagent form is more specific than the source establishes
  description: The source does not specify hydration for EDTA·2Na or the counterion/hydration
    of EDTA·Fe(III). The owner asserts anhydrous disodium EDTA and an iron-EDTA anion
    without reagent-level evidence.
  target_ids:
  - CultureMech:009693
  field_paths:
  - solutions[0].composition[1].term
  - solutions[1].composition[0].term
  evidence_ids:
  - parent
  - chebi64734
  - chebi30729
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
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
  issue_key: source-evidence-and-stock-authentication
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Claim evidence and exact iron-stock authentication remain incomplete
  description: Three owner references are bare URLs, and no owner/target quantity
    or preparation claim has attached evidence. The asserted 4767 stock retains two
    historical excerpts whose original raw response is unavailable; exact 4768 evidence
    is independently authenticated only within that external stock.
  target_ids:
  - CultureMech:009693
  field_paths:
  - references
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - iron-local
  - phosphate-local
  - phosphate-api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
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
  issue_key: preparation-default-and-classification
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Available sterilization default and classification need scoped curation
  description: Exact JCM pages display 121°C for 15 min unless otherwise stated; owner
    keeps only the autoclave method. Target classification and preparation remain
    stale. Reagent form limits and interpreted atmosphere labels should remain explicit.
  target_ids:
  - CultureMech:009693
  field_paths:
  - sterilization
  - medium_type
  - composition_type
  - incubation_atmosphere
  evidence_ids:
  - child
  - parent
  - record
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
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
  description: Reconcile and evidence the maintained owner first, then regenerate
    the target through the declared generator; verify nested stocks, exact child overrides
    and evidence survive.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009693
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
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
  description: Retain original batch amounts and water inputs, distinguish nominal
    preparation bases from measured volume, and preserve explicit provider/child per-liter
    declarations only within their exact scope.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009693
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
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
  description: Qualify the unresolved reagent form and independently verify any proposed
    supplied-form mapping; do not infer a salt, hydration state or molar conversion.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009693
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
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
  description: Attach source-specific excerpts and metadata; recover exact 4767 accession/response
    evidence before treating its historical attachments as verified. Preserve required-unavailable
    status and keep external evidence scope separate.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009693
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
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
  description: Record the displayed conditional autoclave default at applicable stages
    and reassess classification from the exact source without converting catalogue
    intent into observed growth.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009693
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml
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
- Exact MediaDive 4767 and its separately preserved retry return 503. Two historical
  local excerpts remain derivative-only; original response cf7e5be177e4c6e16506daa65f21cef4189eecade344fab01f83de936f8f825f
  was not recovered. Required asserted-stock identity/evidence authentication is incomplete,
  though JCM 815 directly supports the named stock recipe.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO
  endpoints remain usable. This attempt does not supply absent original historical
  bytes.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO
  endpoints remain usable. This attempt does not supply absent original historical
  bytes.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO
  endpoints remain usable. This attempt does not supply absent original historical
  bytes.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO
  endpoints remain usable. This attempt does not supply absent original historical
  bytes.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO
  endpoints remain usable. This attempt does not supply absent original historical
  bytes.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO
  endpoints remain usable. This attempt does not supply absent original historical
  bytes.
- Preserved alternate/current endpoint failure; exact JCM primaries and original TOGO
  endpoints remain usable. This attempt does not supply absent original historical
  bytes.
- Only explicitly invoked parent basal and named stock recipes are transferred. Parent
  pH 3.0, phosphate 2 ml and 100 ml pure methane are overridden. Parent M850 unrelated
  variant-child pH 6.7, old anhydrous mappings and flattened amounts are not inherited.
  No percent basis, reagent counterion, gas dose or measured final volume is invented.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-035
- generated-medium
```
