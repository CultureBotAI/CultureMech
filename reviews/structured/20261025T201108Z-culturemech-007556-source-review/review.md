# Source and formulation review: cejfb1t_medium (CultureMech:007556)

- Review: 20261025T201108Z-culturemech-007556-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-25T20:08:28Z
- Finished UTC: 2026-10-25T20:11:08Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

CEJFB1T is correctly identified as TOGO M1040 / JCM 987. The selected target and owner retain the nominal ingredients but encode water, resazurin and stock additions in incompatible dimensions, omit the staged preparation, and leave five stock placeholders. Only the named M439 trace subsection is transferred; its cobalt and nickel hydrate groundings need correction. Listed liquid totals do not establish a measured final volume.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 521; batch 053 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fifty-two task batches contain 520 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 231e0ba71b41d45362168d539efebe7991823464 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 523 of 6325 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 231e0ba71b41d45362168d539efebe7991823464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007556 | data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml | generated | cejfb1t_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007556 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007556 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch053/521/strict.tsv |
| validate-terms | passed | True | CultureMech:007556 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007556 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007556 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007556.

The four documented recipes completed; interpret the scope of each separately.

### Scoped current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:007556.

49 scoped ontology slots and 20 distinct nonobsolete IDs checked; label agreement is not supplied-form validation. 17 current secondary slots and 0 legacy slots have explicit exact-key lookups. Target linkage: primary 12/15 (80.00%), current secondary 8/15 (53.33%); these are linkage counts, not correctness scores.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:007556.

25 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact selected accession and bounded trace dependency

identity: supported. Targets: CultureMech:007556.

TOGO M1040 explicitly identifies JCM 987; both primary and provider name CEJFB1T. The selected owner and generated target share the same scientific fields. M439 resolves as a maintained record, but only its trace-element subsection is relevant. Neither missing stock content nor an unassessed historical namesake is treated as a broken identifier.

### Supplied salts, hydrates and dependency annotations

grounding: concern. Targets: CultureMech:007556.

The selected base named salts, L-cysteine hydrochloride monohydrate and generic resazurin have compatible asserted identities. No sodium-resazurin defect is invented where the source says only resazurin. In the scoped M439 trace fields, CoCl2·6H2O uses anhydrous cobalt dichloride CHEBI:35696 and NiCl2·6H2O uses anhydrous nickel dichloride CHEBI:34887. Their labels resolve correctly but their formulas omit the six waters. The other explicitly named trace hydrates agree with their asserted forms.

### Ordered preparation and stock boundaries

completeness: concern. Targets: CultureMech:007556.

Both selected layers omit the source pH adjustment to 7.6, N2–CO2 4:1 volume ratio, autoclaving, after-cooling anaerobic additions, gas-stream distribution and butyl-rubber sealing, and late sulfide addition. KOH and gas VARIABLE entries are not substitutes for those stages. Five solution placeholders and the top-level MgSO4 stock fail to represent the six named additions clearly.

### Complex liquid medium and growth limits

scope: supported. Targets: CultureMech:007556.

Yeast extract and tryptone support complex, undefined classification; no gelling agent is specified. The source identity and medium name do not establish a particular strain growth observation, incubation time, temperature, gas pressure or gas-flow rate. The high_metal flag is an imported qualitative annotation with no source threshold verified here.

### Earlier review and current writer limits

provenance: supported. Targets: CultureMech:007556.

All four exact historical reports were read: October 5 target/owner and M439 rows are source-unchecked inventories; the September 22 report describes the same unit, stock and preparation issues. Its historical namesake claims do not establish a current owner or authorize merger. Its description of the trace addition as post-autoclave is not adopted: the current primary places that 1 ml trace row in the initial mix. Current source stages govern. No original external raw is recovered by this record’s twelve-parent search.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:007556.

39 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "Receiving batch Distilled water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "855",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "855",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 855,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The source prints 855 ml water = 0.855 L as a batch input, not 855 g/L. No water density or final-volume makeup is inferred."
  },
  {
    "decision_id": "q2",
    "subject": "Receiving batch NaCl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 200,\n          \"unit\": \"g\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The source directly prints this batch mass. Its numerical equality to the stored value does not establish a final-litre concentration: 855 ml water and separately staged stock additions are not an explicit final-volume instruction."
  },
  {
    "decision_id": "q3",
    "subject": "Receiving batch CaCl2・2H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The source directly prints this batch mass. Its numerical equality to the stored value does not establish a final-litre concentration: 855 ml water and separately staged stock additions are not an explicit final-volume instruction."
  },
  {
    "decision_id": "q4",
    "subject": "Receiving batch NH4Cl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The source directly prints this batch mass. Its numerical equality to the stored value does not establish a final-litre concentration: 855 ml water and separately staged stock additions are not an explicit final-volume instruction."
  },
  {
    "decision_id": "q5",
    "subject": "Receiving batch K2HPO4",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The source directly prints this batch mass. Its numerical equality to the stored value does not establish a final-litre concentration: 855 ml water and separately staged stock additions are not an explicit final-volume instruction."
  },
  {
    "decision_id": "q6",
    "subject": "Receiving batch Resazurin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The source prints 0.5 mg resazurin, not 0.5 g/L. Preserve the milligram batch amount; no unsupported final-litre rate or sodium-salt identity is substituted."
  },
  {
    "decision_id": "q7",
    "subject": "Receiving batch KCl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.8,\n          \"unit\": \"g\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The source directly prints this batch mass. Its numerical equality to the stored value does not establish a final-litre concentration: 855 ml water and separately staged stock additions are not an explicit final-volume instruction."
  },
  {
    "decision_id": "q8",
    "subject": "Receiving batch Sodium acetate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"Sodium acetate\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The source directly prints this batch mass. Its numerical equality to the stored value does not establish a final-litre concentration: 855 ml water and separately staged stock additions are not an explicit final-volume instruction."
  },
  {
    "decision_id": "q9",
    "subject": "Receiving batch Yeast extract (BD-Difco)",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The source directly prints this batch mass. Its numerical equality to the stored value does not establish a final-litre concentration: 855 ml water and separately staged stock additions are not an explicit final-volume instruction."
  },
  {
    "decision_id": "q10",
    "subject": "Receiving batch Tryptone (BD-Difco)",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Tryptone (BD-Difco)\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The source directly prints this batch mass. Its numerical equality to the stored value does not establish a final-litre concentration: 855 ml water and separately staged stock additions are not an explicit final-volume instruction."
  },
  {
    "decision_id": "q11",
    "subject": "Receiving batch L-Cysteine・HCl・H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"L-Cysteine・HCl・H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The source directly prints this batch mass. Its numerical equality to the stored value does not establish a final-litre concentration: 855 ml water and separately staged stock additions are not an explicit final-volume instruction."
  },
  {
    "decision_id": "q12",
    "subject": "Preparation reagent KOH",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[12]",
        "exact_source_quote": "\"component_name\": \"KOH\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      },
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly, adjust pH to 7.6 with KOH and autoclave under aN2--CO2 (4:1, v/v) gas mixture. After cooling, add the following solutions from anaerobic stocks (autoclaved or *filter-sterilized):",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "No fixed mass or concentration is supplied. KOH is a pH-adjustment reagent and the gases define the stated atmosphere; VARIABLE does not establish a quantitative ingredient dose, pressure or flow rate."
  },
  {
    "decision_id": "q13",
    "subject": "Preparation reagent Carbon dioxide gas",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[13]",
        "exact_source_quote": "\"component_name\": \"Carbon dioxide gas\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      },
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly, adjust pH to 7.6 with KOH and autoclave under aN2--CO2 (4:1, v/v) gas mixture. After cooling, add the following solutions from anaerobic stocks (autoclaved or *filter-sterilized):",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "No fixed mass or concentration is supplied. KOH is a pH-adjustment reagent and the gases define the stated atmosphere; VARIABLE does not establish a quantitative ingredient dose, pressure or flow rate."
  },
  {
    "decision_id": "q14",
    "subject": "Preparation reagent Nitrogen gas",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[14]",
        "exact_source_quote": "\"component_name\": \"Nitrogen gas\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      },
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly, adjust pH to 7.6 with KOH and autoclave under aN2--CO2 (4:1, v/v) gas mixture. After cooling, add the following solutions from anaerobic stocks (autoclaved or *filter-sterilized):",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "No fixed mass or concentration is supplied. KOH is a pH-adjustment reagent and the gases define the stated atmosphere; VARIABLE does not establish a quantitative ingredient dose, pressure or flow rate."
  },
  {
    "decision_id": "q15",
    "subject": "Magnesium sulfate stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"10% MgSO4・7H2O\",\n          \"volume\": 50,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      },
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly, adjust pH to 7.6 with KOH and autoclave under aN2--CO2 (4:1, v/v) gas mixture. After cooling, add the following solutions from anaerobic stocks (autoclaved or *filter-sterilized):",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "50 ml = 0.05 L is the volume of a 10% MgSO4·7H2O stock added after cooling, not 50 g/L magnesium sulfate. Preserve the stock separately. Bare 10% does not establish a mass/volume basis."
  },
  {
    "decision_id": "q16",
    "subject": "Receiving Trace element solution (see Medium [M439])",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[0].items[11]",
        "exact_source_quote": "\"component_name\": \"Trace element solution (see Medium [M439])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The printed value is a stock-addition volume, not G_PER_L. Preserve the named source stock and absolute batch dose; do not infer a final-medium concentration. This trace addition belongs to the initial mixture, not the after-cooling table."
  },
  {
    "decision_id": "q17",
    "subject": "Receiving 8% NaHCO3 solution*",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"8% NaHCO3 solution*\",\n          \"volume\": 25,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The printed value is a stock-addition volume, not G_PER_L. Preserve the named source stock and absolute batch dose; do not infer a final-medium concentration. The stated percent strength lacks a mass/volume or mass/mass basis."
  },
  {
    "decision_id": "q18",
    "subject": "Receiving 1 M Glucose solution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"1 M Glucose solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The printed value is a stock-addition volume, not G_PER_L. Preserve the named source stock and absolute batch dose; do not infer a final-medium concentration. The 1 M glucose strength is explicit; 20 ml contains 0.020 mol, but final-medium molarity remains unresolved without an explicit final volume."
  },
  {
    "decision_id": "q19",
    "subject": "Receiving 10% Tryptone solution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"10% Tryptone solution\",\n          \"volume\": 50,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The printed value is a stock-addition volume, not G_PER_L. Preserve the named source stock and absolute batch dose; do not infer a final-medium concentration. The stated percent strength lacks a mass/volume or mass/mass basis."
  },
  {
    "decision_id": "q20",
    "subject": "Receiving 5% Na2S・9H2O solution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"5% Na2S・9H2O solution\",\n          \"volume\": 8,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      },
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "Aseptically distribute the medium into culture vessels under a stream of N2--CO2 (4:1, v/v), and seal with butyl rubber stoppers. Prior to inoculation, add per liter the following solution from an anaerobic stock (autoclave and store under a N2 atmosphere).",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "The final paragraph explicitly gives 8 ml per liter of 5% Na2S·9H2O stock before inoculation. A dose of 8 ML_PER_L is source-supported; 8 G_PER_L is not. Bare 5% does not justify a sulfide mass concentration, and this per-litre instruction does not retroactively supply a measured denominator for the preceding batch."
  },
  {
    "decision_id": "q21",
    "subject": "M439 trace batch HCl (25%)",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "12.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"HCl (25%)\",\n          \"volume\": 12.5,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      },
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 987,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "rationale": "This trace-stock source amount is in ml, not a receiving-medium G_PER_L value. Preserve its stock batch scope; listed water does not establish final stock volume. HCl is 25% with unspecified basis; do not infer density or mass."
  },
  {
    "decision_id": "q22",
    "subject": "M439 trace batch Na2MoO4・2H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "36",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      },
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 987,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "rationale": "This trace-stock source amount is in mg, not a receiving-medium G_PER_L value. Preserve its stock batch scope; listed water does not establish final stock volume."
  },
  {
    "decision_id": "q23",
    "subject": "M439 trace batch H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 30,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      },
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 987,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "rationale": "This trace-stock source amount is in mg, not a receiving-medium G_PER_L value. Preserve its stock batch scope; listed water does not establish final stock volume."
  },
  {
    "decision_id": "q24",
    "subject": "M439 trace batch FeSO4・7H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "2.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[4]",
        "exact_source_quote": "\"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 2.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      },
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 987,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "rationale": "This trace-stock source amount is in g, not a receiving-medium G_PER_L value. Preserve its stock batch scope; listed water does not establish final stock volume."
  },
  {
    "decision_id": "q25",
    "subject": "M439 trace batch MnCl2・4H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[5]",
        "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      },
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 987,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "rationale": "This trace-stock source amount is in mg, not a receiving-medium G_PER_L value. Preserve its stock batch scope; listed water does not establish final stock volume."
  },
  {
    "decision_id": "q26",
    "subject": "M439 trace batch CoCl2・6H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "190",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[6]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      },
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 987,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "rationale": "This trace-stock source amount is in mg, not a receiving-medium G_PER_L value. Preserve its stock batch scope; listed water does not establish final stock volume."
  },
  {
    "decision_id": "q27",
    "subject": "M439 trace batch NiCl2・6H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "24",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[7]",
        "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      },
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 987,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "rationale": "This trace-stock source amount is in mg, not a receiving-medium G_PER_L value. Preserve its stock batch scope; listed water does not establish final stock volume."
  },
  {
    "decision_id": "q28",
    "subject": "M439 trace batch ZnSO4・7H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "144",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[8]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 144,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      },
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 987,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "rationale": "This trace-stock source amount is in mg, not a receiving-medium G_PER_L value. Preserve its stock batch scope; listed water does not establish final stock volume."
  },
  {
    "decision_id": "q29",
    "subject": "M439 trace batch CuCl2・2H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[9]",
        "exact_source_quote": "\"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      },
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 987,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "rationale": "This trace-stock source amount is in mg, not a receiving-medium G_PER_L value. Preserve its stock batch scope; listed water does not establish final stock volume."
  },
  {
    "decision_id": "q30",
    "subject": "M439 trace water",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 987,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "rationale": "Retain 987 ml water for this stock only. The merged parent water and other parent recipes are excluded, and 987 ml water plus 12.5 ml acid is not an explicit final-volume instruction."
  },
  {
    "decision_id": "q31",
    "subject": "8% bicarbonate stock strength",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"8% NaHCO3 solution*\",\n          \"volume\": 25,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "Preserve the stated stock strength separately from dose. The molarity is explicit for glucose; every bare percent remains basis-unspecified and is not converted to grams or final-medium concentration."
  },
  {
    "decision_id": "q32",
    "subject": "10% magnesium sulfate stock strength",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"10% MgSO4・7H2O\",\n          \"volume\": 50,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "Preserve the stated stock strength separately from dose. The molarity is explicit for glucose; every bare percent remains basis-unspecified and is not converted to grams or final-medium concentration."
  },
  {
    "decision_id": "q33",
    "subject": "1 M glucose stock strength",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"1 M Glucose solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "Preserve the stated stock strength separately from dose. The molarity is explicit for glucose; every bare percent remains basis-unspecified and is not converted to grams or final-medium concentration."
  },
  {
    "decision_id": "q34",
    "subject": "10% tryptone stock strength",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"10% Tryptone solution\",\n          \"volume\": 50,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "Preserve the stated stock strength separately from dose. The molarity is explicit for glucose; every bare percent remains basis-unspecified and is not converted to grams or final-medium concentration."
  },
  {
    "decision_id": "q35",
    "subject": "5% sulfide stock strength",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"5% Na2S・9H2O solution\",\n          \"volume\": 8,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "Preserve the stated stock strength separately from dose. The molarity is explicit for glucose; every bare percent remains basis-unspecified and is not converted to grams or final-medium concentration."
  },
  {
    "decision_id": "q36",
    "subject": "25% hydrochloric acid stock strength",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "togoM439",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"HCl (25%)\",\n          \"volume\": 12.5,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "rationale": "Preserve the stated stock strength separately from dose. The molarity is explicit for glucose; every bare percent remains basis-unspecified and is not converted to grams or final-medium concentration."
  },
  {
    "decision_id": "q37",
    "subject": "Initial pH, gas ratio and post-cooling boundary",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly, adjust pH to 7.6 with KOH and autoclave under aN2--CO2 (4:1, v/v) gas mixture. After cooling, add the following solutions from anaerobic stocks (autoclaved or *filter-sterilized):",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "Retain pH 7.6 with KOH, N2–CO2 4:1 (v/v), initial autoclaving and after-cooling anaerobic additions. The asterisk identifies filter-sterilized bicarbonate in the primary table. No pressure, flow rate or final-medium denominator is supplied."
  },
  {
    "decision_id": "q38",
    "subject": "Distribution and late sulfide sequence",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "togoM1040",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "Aseptically distribute the medium into culture vessels under a stream of N2--CO2 (4:1, v/v), and seal with butyl rubber stoppers. Prior to inoculation, add per liter the following solution from an anaerobic stock (autoclave and store under a N2 atmosphere).",
        "snapshot_sha256": "9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498"
      }
    ],
    "rationale": "Preserve gas-stream distribution, butyl-rubber sealing, pre-inoculation timing and sulfide-stock autoclaving/storage under N2. These are receiving-medium stages, not M439 parent preparation."
  },
  {
    "decision_id": "q39",
    "subject": "JCM 987 autoclave default",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm987",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=987",
        "source_locator": "Extracted text line 4",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "44d12e927566387e3e394d950289f0f15241b0e0618ecbf30a869bc7fb3768d6",
        "parsed_text_sha256": "ecb4488c51dd75c5c866e44ff9b60c5bb44ca94f7f9d7cdc15d3d45e2bb7f208"
      }
    ],
    "rationale": "The selected JCM 987 page gives 121°C for 15 min unless otherwise stated. Retain the source-specific default and explicit filter/autoclave stock distinctions; do not borrow defaults from other recipes."
  }
]

## Findings

### f1: Water, indicator and stock doses lose their source dimensions

major / open / confirmed; issue key: cm007556-unit-stock-boundaries.

Both selected layers store water 855 G_PER_L, resazurin 0.5 G_PER_L and milliliter stock doses as G_PER_L. Five stocks are unnamed empty placeholders; the 50 ml magnesium-sulfate stock remains a top-level ingredient. Other batch masses also lack an established final-litre denominator.

### f2: Referenced trace stock uses anhydrous cobalt and nickel IDs

major / open / confirmed; issue key: cm007556-trace-hydrate-scope.

The M439 trace dependency ingredients[17].term and ingredients[18].term name cobalt and nickel hexahydrates but identify anhydrous CHEBI:35696 and CHEBI:34887. These are dependency-only locations, not target ingredient indices. The selected base salt annotations are not implicated.

### f3: Ordered source preparation is absent

major / open / confirmed; issue key: cm007556-preparation-stages.

The selected target and owner omit source pH adjustment, gas ratio, sterilization and cooling boundaries, stock-treatment distinction, vessel sealing and pre-inoculation sulfide addition. Variable gas/KOH ingredients cannot encode these facts.

### f4: Import history conflates the TOGO and JCM accessions

minor / open / confirmed; issue key: cm007556-history-source-accession.

The initial event says Source: JCM, ID: M1040. M1040 is the TOGO accession; the source metadata identifies JCM_M987. Existing history should remain append-only.

## Recommended Actions And Acceptance Checks

### a1

Correct source-labelled water, mass and dose dimensions in the maintained owner; preserve six distinct stock additions and their stages. Use 8 ML_PER_L only for the explicitly per-litre late sulfide dose. Preserve unspecified percentage bases and avoid final-volume assumptions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve exact hexahydrate identifiers in the scoped maintained trace definition, with new source-form evidence, before reusing it. Preserve unrelated parent stocks and conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add exact source-scoped ordered preparation and stock strengths to the maintained owner, then regenerate and verify freshness. Preserve absent incubation and gas-pressure values as unknown.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Append a narrow provenance clarification distinguishing TOGO M1040 and JCM 987 during authorized curation; retain the original event and actual source access dates.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch053/521/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch053/521/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml:1:id: CultureMech:007556<br>./data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml:1:id: CultureMech:007556<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch053/source-preflight-bound/521/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 27 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch053/521/grounding-inventory.json; Exact path-qualified inventory; original values and scope retained | context_only | All scoped current ontology slots, exact raw scientific objects and current MIM rows; legacy negatives remain snapshot-specific. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi32035 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32035; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term metadata only | supports | Identifier properties and canonical-label correspondence; formulation, product, hydrate and preparation support are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact asserted secondary and legacy keys in pinned CSV; current catalog/tree separately pinned | context_only | The full exact-key rows and negative results are retained in grounding-inventory. Current absence is not historical invalidity. No inherited older capture-scope wording is applied to this record. |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Pinned current MIM catalog/tree; current slot scope in grounding-inventory | context_only | Current MIM inventory only; older reused content-limit annotations describe their original collection scope. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Pinned current MIM catalog/tree; current slot scope in grounding-inventory | context_only | Current MIM inventory only; older reused content-limit annotations describe their original collection scope. |
| history-metadata | data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml", "events": 12, "timestamp_issues": []}] |
| history-full | /private/tmp/culturemech-review-work-batch053/521/history-inventory.json; Exact path-qualified inventory; original values and scope retained | context_only | Complete current target, owner and scoped dependency history events, unchanged; dependency history does not transfer its receiving-medium conditions. |
| historical-inventory | /private/tmp/culturemech-review-work-batch053/521/historical-evidence-inventory.json; Exact path-qualified inventory; original values and scope retained | context_only | All existing attached claims, exact-header historical reports and qualified decoded-parent joins; full original bytes remain pinned. |
| old-report-0 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CEJFB1T_MEDIUM.md; Full exact-header historical derivative report; scoped current path membership | context_only | Historical evidence and unresolved decisions are retained. This derivative does not replace missing source raw or authenticate a new recipe variant. |
| old-report-1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.md; Full exact-header historical derivative report; scoped current path membership | context_only | Historical evidence and unresolved decisions are retained. This derivative does not replace missing source raw or authenticate a new recipe variant. |
| old-report-2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.md; Full exact-header historical derivative report; scoped current path membership | context_only | Historical evidence and unresolved decisions are retained. This derivative does not replace missing source raw or authenticate a new recipe variant. |
| old-report-3 | reports/yaml_record_review/20260922T063517Z-CEJFB1T_MEDIUM.md; Full exact-header historical derivative report; scoped current path membership | context_only | Historical evidence and unresolved decisions are retained. This derivative does not replace missing source raw or authenticate a new recipe variant. |
| primary987 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=987; Complete JCM 987 table, post-cooling additions, pre-inoculation sulfide paragraph and page sterilization default | supports | The collection prints absolute base masses and water, separate stock volumes, a 1 M glucose stock, unspecified percent bases and an explicit 8 ml per liter sulfide addition. No measured final volume is stated for the earlier batch. |
| provider1040 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040; Metadata, components[0:3] and both preparation comments | supports | The exact current transcription identifies JCM_M987 and preserves the source stages. GMO annotations and absolute component volumes do not independently establish final-medium concentrations. |
| trace439 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439; components[3] only | supports | Only the named trace-element batch is assessed. Parent basal recipe, other stocks, parent receiving dose and parent gas or preparation conditions do not transfer. |
| trace-jcm439 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439; Trace element solution subsection only | supports | Collection trace subsection independently supports the named salts, milligram versus gram quantities, 12.5 ml of 25% HCl and 987 ml water. No final-stock volume or percentage basis is declared. |
| writer-togo | src/culturemech/import/togo_importer.py; _ingredient_from_item; _local_batch_volume_ml; _local_solution_composition; _solution_from_item; _extract_primary_components; _extract_preparation_steps; _parse_unit | context_only | Current code preserves primary layers, referenced/local stocks and preparation comments. Its unit parser still maps bare masses and volumes to per-litre enums and bare percent to weight/volume; those assumptions require source-basis review. The current stage-preserving implementation is not asserted to be the code that produced this historical flattened record. Current code only; historical execution is not established. |
| writer-stock | scripts/migrate_solutions_from_ingredients.py; Complete SolutionMigrator body, especially _is_solution and _resolve_solution | context_only | Current migration recognizes solution names/references, creates empty stubs for unresolved definitions and copies existing concentrations without converting their dimensions. It therefore does not itself authenticate source quantities or stock identity. Current code only; historical execution is not established. |
| writer-merge | src/culturemech/merge/formulation.py; Complete formulation_content and merge_formulation_evidence | context_only | Current merger requires exact scientific assertions, including stock structure, amounts, notes and preparation. It does not license merging incompatible namesakes by ingredient-set similarity. Current code only; historical execution is not established. |
| field-census | /private/tmp/culturemech-review-work-batch053/521/field-census.json; Exact path-qualified inventory; original values and scope retained | context_only | All local scalar fields preserved; excluded dependency content is context and has no transferred source assessment. |
| quantity-coverage | /private/tmp/culturemech-review-work-batch053/521/coverage-inventory.json; Exact path-qualified inventory; original values and scope retained | context_only | Every selected/scoped concentration and numeric context joins exact local values; excluded parent quantities are explicitly retained outside transferred scope. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch053/521/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Twenty dependency concentration fields belong to excluded M439 parent recipes or its receiving dose and are not transferred. Current label/MIM agreement does not certify source chemical forms or historical mapping validity. No phenotype or growth experiment is asserted.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T201108Z-culturemech-007556-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: cejfb1t_medium (CultureMech:007556)'
started_at: '2026-10-25T20:08:28Z'
finished_at: '2026-10-25T20:11:08Z'
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
summary: CEJFB1T is correctly identified as TOGO M1040 / JCM 987. The selected target
  and owner retain the nominal ingredients but encode water, resazurin and stock additions
  in incompatible dimensions, omit the staged preparation, and leave five stock placeholders.
  Only the named M439 trace subsection is transferred; its cobalt and nickel hydrate
  groundings need correction. Listed liquid totals do not establish a measured final
  volume.
source:
  git_revision: 231e0ba71b41d45362168d539efebe7991823464
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
  - path: data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml
    sha256: 1c7225719fdccf9b7855d39e0c29e0ab52129c813815c1703bf379a96276281c
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml
    sha256: 4f3b8dcb75caa0069ca7b74c62c129efc66e2815982ca4e0f53f804dcdb2fef4
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml
    sha256: 61b72e39e60ca8f44e869309dd78d47a3277760d3bf16ffaaaac30da77fab6b0
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_650_CENTENUM_medium.yaml.md
    sha256: cea95c8bef224d7988c89e55916e6bfc1c85e40e1e04644c416ba76677bfaf5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_748_CENS_medium.yaml.md
    sha256: 013cdd23597b0f17ae16040cfcff4fa5612704583733ff2b59f4575da6a5ef4e
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/medium_650_modified_for_dsm_8319.yaml.md
    sha256: bf8b812d7257fd833fe40a0c3d65ecca0d062d667e5d7ef32e8da45fdc400b8d
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cellulosilyticum_medium.yaml.md
    sha256: 6fc71489fc62d3a8490420a79c8e85ef97b1bf00048f2b4a5f9cbde290926d95
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cens_medium.yaml.md
    sha256: 21cd5c7838ddcd4136764be9d06f0b560c3df459ffd3510ca5a9df7e1f34e292
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/centenum_medium.yaml.md
    sha256: 11adfae044a191efafa6569efa6dae001a26c2b4186bb1c4165f15ec06fb5aa7
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cgm.yaml.md
    sha256: 00bc6814a1dfc5789c97728aa09b3959c842ce63a226744cc526ee36a88f826e
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J295_CELLULOMONAS_FERMENTANS_MEDIUM.yaml.md
    sha256: 3338d620d73f8bd698294bbb4b0a267bb79d279ff8c96056cc4586cd8535f187
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5312_Solution_C.yaml.md
    sha256: e167b06340bce70ab77d6408c8f5e9cb6b1dbeef2c36e29ff20952990e3bfbd2
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5342_Solution_A.yaml.md
    sha256: f68b7d85766061aa31ffef0f0172844d47d0aae036221dc66d608c86e8dce7a6
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5343_Solution_B.yaml.md
    sha256: aca054ad3ae72ab8aee9908cb67ceac62a96adf84ff60a5141dda9b4f13ff6d8
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md
    sha256: 89725cdcefc5da88b06931c4db253e065a5f48c2d2b9c8c0a9bc07f6fdc157e8
    role: context
  - path: reports/ingredient_concentration_curation/20261008-m258-m260-stocks/records/M258.md
    sha256: fda8033086b0627144eb23d2558e66134a597bfa67939fec2f18992de7845747
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CEJFB1T_MEDIUM.md
    sha256: 49ac2c7b79c5da4e7d56b164324afa763d1f8301cb1794aacecb55c381582cb6
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.md
    sha256: a9112230e5f2b35a345d29058d2d06b1aec1b6c6e36d77e294ecbad9801f92ba
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOMONAS_FERMENTANS_MEDIUM.md
    sha256: d71859ea710d11f601c3f0c34e1740f6d2afbae9b6516f296dccbe34c913d948
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOSE_AGAR.md
    sha256: f90ca9219519b238b5b06d86a8ca2e84f6832a4ab67b0feabd05bdc3a9839381
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.md
    sha256: 3a3e74ac86eca9c6db45ec35f7ef0e6a76527941fffd6422ec02b9931c0c4212
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOSILYTICUM_RUMINICOLA_MEDIUM.md
    sha256: 63217cedf21217428eca34c2c1418b1982e2e1b435abc3a6130e2689216f9fb0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CENS_MEDIUM.md
    sha256: 597cb6a7938f9cd459897adf69983dff16ed4d88f1a910366ad8abe4b3928222
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CENTENUM_MEDIUM.md
    sha256: 64359ed6e4f323a585a64a19e0259164f4e54dd0e8d5c90443fca6183b6c91e1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CGM.md
    sha256: a07bbba50f039aeb8d2aa1f811f38913a6651995e329748e80f180b9a3d57a3b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CGY_Medium.md
    sha256: 2d2435a40efa8bac48c6238994b420ea1f7022e9d1a615b67aa2734a79397302
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/cgm.md
    sha256: 306c1cacb9be80fb75cde15b3ccffd282c046df9f6cf08ef2ff32055f4886ee4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M1148_Halanaeroarchaeum_Medium.md
    sha256: edfdd0b0fb57e8f9d9c328c8326da947773576733a6c38f9ecda66e70fb8e1a9
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M258_Methanomicrobium_Mobile_Medium.md
    sha256: 10dbfce058ee6e85485dcfdc15b611cc9e0b95cea52a03f631a3b54fe008fa04
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J295_CELLULOMONAS_FERMENTANS_MEDIUM.md
    sha256: 9a63092a34db92eb9ca60f2db910800f0034f5e7f0e6d1eb074e146061fa60d4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.md
    sha256: 9305c9cfd434cbb5f857fd99357fe9a811cb31a48a3d05d779959557c84250b2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_748_CENS_medium.md
    sha256: a9c41ec015e0f2f45bb92ed0065eb0ddc3f3852207c12751d1ce686377ba8326
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.md
    sha256: d3295a1ae91e3c543bac519713a5559b6da46ed2a5384def64ef0c9354ed6e4f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1264_Cellulolytic_Natronoarchaea_Medium.md
    sha256: 59c8979a006d9b770dd6d2b0ecdbdfd4a81fa2339fff1d33afd41e65932df4fc
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.md
    sha256: e43ae29a243274817a13192084b67ac0741248fff46309a4e2862aef08e1ef58
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.md
    sha256: 7a3396b4e01bffebe1a22b591ead29f62ecbfeaeeeb315bbcac5a84050435f83
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M653_Cellulosilyticum_Ruminicola_Medium.md
    sha256: a1adca9a9911e57b4bd66fce0a5f4db9d2feea7b745195bf0c6e53238beeb2d0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cellulosilyticum_medium.md
    sha256: da0b08c05cca15abca3721b4461c97a7cb8390a6cbb460045efe9dd04a956ec2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cens_medium.md
    sha256: 874c7e795a7cd6cb420776fb624326f85520f9879d26165de81a0638506b1de2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/centenum_medium.md
    sha256: fabcbe826c085e4f317e0f4dffb71c125ef8c93ca6d7c378eb5aa003bcbc9f94
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cgm.md
    sha256: aed676ac8b2825a51883505bc77e41d3fd59a20a6facce044c7c62a638aa64d1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cgy_medium.md
    sha256: 328084240301f3a0bd2140a55d72e331bb4d75dd7e40be3971155dff910193bc
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5312_Solution_C.md
    sha256: 64ab17db61f41d71c9fab76cb8c0838b8cdcd81c4e35f7f240c71642196f0ff3
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5342_Solution_A.md
    sha256: 31d821180b177a4395ac64cfe2eb443091729cb74309085beeb1b765ed2dd2f2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5343_Solution_B.md
    sha256: a1f8fb64c671e4aae298c328e3a93b1ad420e2d60c7400dbae6775f8081a0e33
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.md
    sha256: f8616b950028d94561a0c4a986c40d5fdcdfa14324af5f8fa130447d9f7d7bdb
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
    sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
    role: context
  - path: reports/yaml_record_review/20260922T063517Z-CEJFB1T_MEDIUM.md
    sha256: 1c833062655743da5d43f5f05638efd1b7bad9147a054541027cb892ea737379
    role: context
  - path: reports/yaml_record_review/20260922T063654Z-CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.md
    sha256: 812641f1e5b20ca4a328fc409a8fd1f8cf18a1b8c740c904170097e764dd491a
    role: context
  - path: reports/yaml_record_review/20260922T063822Z-CELLULOMONAS_FERMENTANS_MEDIUM.md
    sha256: cde23788b5a2bdfea2e67768ac9f27f0ad5200aeccb4c3e6fd8af84b3ac70c14
    role: context
  - path: reports/yaml_record_review/20260922T063942Z-CELLULOSE_AGAR.md
    sha256: 7d7df31cd5aa0b65511048a3ad7ea51ed128f3d111280455da6b27b77deeff3a
    role: context
  - path: reports/yaml_record_review/20260922T064115Z-CELLULOSILYTICUM_MEDIUM.md
    sha256: b3996678c78481e187be45d3a239865ef844eff74fcc663396ac72e9b986aaef
    role: context
  - path: reports/yaml_record_review/20260922T064238Z-CELLULOSILYTICUM_RUMINICOLA_MEDIUM.md
    sha256: 0b2275d6cbeebebbd700d25e120994c47e980a94f276e53b82544cbf4ab4ddff
    role: context
  - path: reports/yaml_record_review/20260922T064616Z-CENS_MEDIUM.md
    sha256: 6358d704259dc7ba50caf8263a8e95c81f311c9618f805c8f60587de73d37d16
    role: context
  - path: reports/yaml_record_review/20260922T064817Z-CENTENUM_MEDIUM.md
    sha256: 5a517b2db46fa7608fa93b1fd6f7ca36633e65d9e9187b38ed2f820fc9ff5c4c
    role: context
  - path: reports/yaml_record_review/20260922T064954Z-CGM.md
    sha256: b50dfb754feed998bcc620cfe9162a90071733ad665f78825ce24a6a870fe143
    role: context
  - path: reports/yaml_record_review/20260922T065133Z-CGY_Medium.md
    sha256: f24f1ad05b4a65ae735f976877698aed5a3ffa1df9130d14103914260882ae5a
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/audit_mim_sssom_divergence.py
    sha256: ad3478a5aeb757f2ce503be1b4720c86f0c1d90f5549918e1341dc7ac2c0f445
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
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_ccap_instruction_rows.py
    sha256: eb1a4c8c46eb45dcdde6a5d2f0f6833792dd0802c45603eefa1b63a3ff96fca5
    role: context
  - path: scripts/repair_ccap_sources_score10.py
    sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
    role: context
  - path: scripts/repair_dsmz650_752_762_preparations.py
    sha256: 0b955dd562a885fec75dd73bed1eaa00af707b3e2f9d35f7f16b066feb743e1a
    role: context
  - path: scripts/repair_komodo650_752_762_preparations.py
    sha256: 477e2e14b5ff6284e4e291986b333552215f44dca2473fc64cf1d60e0028c0bd
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/review_public_stock_concentrations.py
    sha256: 220dafdb1b826063f533a4b7e41dc3f2576adc433be92c65243605255fb97bb1
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
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/import/ccap_importer.py
    sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
    role: context
  - path: src/culturemech/import/komodo_importer.py
    sha256: 702733bd580e4ba28f77e183e1e8268f17ea2c1041cf7b3addd92919624f2706
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
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
  selection: Task review 521; batch 053 item 1 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding fifty-two task batches
    contain 520 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 231e0ba71b41d45362168d539efebe7991823464
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 523 of 6325 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007556
targets:
- target_id: CultureMech:007556
  path: data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml
  label: cejfb1t_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007556
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch053/521/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch053/521/strict.tsv"
  target_ids:
  - CultureMech:007556
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007556
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007556
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
  - CultureMech:007556
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:09:05.000602Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch053/521/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-25T20:09:08.424991Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch053/521/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:09:13.304418Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:09:16.265123Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-25T20:11:05Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml:1:id:
    CultureMech:007556

    ./data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml:1:id: CultureMech:007556

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/source-preflight-bound/521/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-25T20:11:05Z'
  support: supports
  summary: 27 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: a56288004712df9440a6007b04c47340021394d9b9a713b1b1b1b0e684e0afda
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/521/grounding-inventory.json
  locator: Exact path-qualified inventory; original values and scope retained
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: All scoped current ontology slots, exact raw scientific objects and current
    MIM rows; legacy negatives remain snapshot-specific.
  snapshot_sha256: 849adddefb0270a9bd0f7e22a4d29cfc6d03e6fbc18a82a154dfafc700f8d767
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:42:30.346522Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:43:09.378884Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:00:46.687620Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi32954
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:00:48.206583Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
- evidence_id: chebi91248
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:42:32.136441Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: chebi32035
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32035
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T06:57:47.017507Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: 6ed3df00965b4707265cfced80411c4b1937b727f8c2093addbc467f88ce2ec8
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:00:48.784931Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS obo_id/label/obsolete state/definition/formula/synonyms; term
    metadata only
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: Identifier properties and canonical-label correspondence; formulation,
    product, hydrate and preparation support are assessed separately.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact asserted secondary and legacy keys in pinned CSV; current catalog/tree
    separately pinned
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: The full exact-key rows and negative results are retained in grounding-inventory.
    Current absence is not historical invalidity. No inherited older capture-scope
    wording is applied to this record.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Pinned current MIM catalog/tree; current slot scope in grounding-inventory
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: context_only
  summary: Current MIM inventory only; older reused content-limit annotations describe
    their original collection scope.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Pinned current MIM catalog/tree; current slot scope in grounding-inventory
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: context_only
  summary: Current MIM inventory only; older reused content-limit annotations describe
    their original collection scope.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml", "events": 12,
    "timestamp_issues": []}]'
- evidence_id: history-full
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/521/history-inventory.json
  locator: Exact path-qualified inventory; original values and scope retained
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: Complete current target, owner and scoped dependency history events, unchanged;
    dependency history does not transfer its receiving-medium conditions.
  snapshot_sha256: 8aa1f5239efbd834b1f465f041ab36279832698d9c044453a778489bbcc2e69a
- evidence_id: historical-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/521/historical-evidence-inventory.json
  locator: Exact path-qualified inventory; original values and scope retained
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: All existing attached claims, exact-header historical reports and qualified
    decoded-parent joins; full original bytes remain pinned.
  snapshot_sha256: 9edf22644a10c49cdad3036be07363d82a6ecd996f2d75e2bdb7e25b05758fd6
- evidence_id: old-report-0
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CEJFB1T_MEDIUM.md
  locator: Full exact-header historical derivative report; scoped current path membership
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: Historical evidence and unresolved decisions are retained. This derivative
    does not replace missing source raw or authenticate a new recipe variant.
  snapshot_sha256: 49ac2c7b79c5da4e7d56b164324afa763d1f8301cb1794aacecb55c381582cb6
- evidence_id: old-report-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.md
  locator: Full exact-header historical derivative report; scoped current path membership
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: Historical evidence and unresolved decisions are retained. This derivative
    does not replace missing source raw or authenticate a new recipe variant.
  snapshot_sha256: d3295a1ae91e3c543bac519713a5559b6da46ed2a5384def64ef0c9354ed6e4f
- evidence_id: old-report-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.md
  locator: Full exact-header historical derivative report; scoped current path membership
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: Historical evidence and unresolved decisions are retained. This derivative
    does not replace missing source raw or authenticate a new recipe variant.
  snapshot_sha256: e43ae29a243274817a13192084b67ac0741248fff46309a4e2862aef08e1ef58
- evidence_id: old-report-3
  kind: record_content
  reference: reports/yaml_record_review/20260922T063517Z-CEJFB1T_MEDIUM.md
  locator: Full exact-header historical derivative report; scoped current path membership
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: Historical evidence and unresolved decisions are retained. This derivative
    does not replace missing source raw or authenticate a new recipe variant.
  snapshot_sha256: 1c833062655743da5d43f5f05638efd1b7bad9147a054541027cb892ea737379
- evidence_id: primary987
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=987
  locator: Complete JCM 987 table, post-cooling additions, pre-inoculation sulfide
    paragraph and page sterilization default
  accessed_at: '2026-10-22T09:27:09.283772Z'
  support: supports
  summary: The collection prints absolute base masses and water, separate stock volumes,
    a 1 M glucose stock, unspecified percent bases and an explicit 8 ml per liter
    sulfide addition. No measured final volume is stated for the earlier batch.
  snapshot_sha256: 44d12e927566387e3e394d950289f0f15241b0e0618ecbf30a869bc7fb3768d6
- evidence_id: provider1040
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040
  locator: Metadata, components[0:3] and both preparation comments
  accessed_at: '2026-10-22T09:27:07.780807Z'
  support: supports
  summary: The exact current transcription identifies JCM_M987 and preserves the source
    stages. GMO annotations and absolute component volumes do not independently establish
    final-medium concentrations.
  snapshot_sha256: 9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498
- evidence_id: trace439
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439
  locator: components[3] only
  accessed_at: '2026-10-21T13:13:19.779835Z'
  support: supports
  summary: Only the named trace-element batch is assessed. Parent basal recipe, other
    stocks, parent receiving dose and parent gas or preparation conditions do not
    transfer.
  snapshot_sha256: 8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c
- evidence_id: trace-jcm439
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439
  locator: Trace element solution subsection only
  accessed_at: '2026-10-21T13:13:22.895121Z'
  support: supports
  summary: Collection trace subsection independently supports the named salts, milligram
    versus gram quantities, 12.5 ml of 25% HCl and 987 ml water. No final-stock volume
    or percentage basis is declared.
  snapshot_sha256: 2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item; _local_batch_volume_ml; _local_solution_composition;
    _solution_from_item; _extract_primary_components; _extract_preparation_steps;
    _parse_unit
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: Current code preserves primary layers, referenced/local stocks and preparation
    comments. Its unit parser still maps bare masses and volumes to per-litre enums
    and bare percent to weight/volume; those assumptions require source-basis review.
    The current stage-preserving implementation is not asserted to be the code that
    produced this historical flattened record. Current code only; historical execution
    is not established.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-stock
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Complete SolutionMigrator body, especially _is_solution and _resolve_solution
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: Current migration recognizes solution names/references, creates empty stubs
    for unresolved definitions and copies existing concentrations without converting
    their dimensions. It therefore does not itself authenticate source quantities
    or stock identity. Current code only; historical execution is not established.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Complete formulation_content and merge_formulation_evidence
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: Current merger requires exact scientific assertions, including stock structure,
    amounts, notes and preparation. It does not license merging incompatible namesakes
    by ingredient-set similarity. Current code only; historical execution is not established.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: field-census
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/521/field-census.json
  locator: Exact path-qualified inventory; original values and scope retained
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: All local scalar fields preserved; excluded dependency content is context
    and has no transferred source assessment.
  snapshot_sha256: 40bd452fe16ff282d979c0746236adfbcf6603f72f637ffbfe9225ec3cbbf11c
- evidence_id: quantity-coverage
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/521/coverage-inventory.json
  locator: Exact path-qualified inventory; original values and scope retained
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: Every selected/scoped concentration and numeric context joins exact local
    values; excluded parent quantities are explicitly retained outside transferred
    scope.
  snapshot_sha256: dff7a8d082f00e01be118e1329568b38ba97f59de70019f93f5bd187dbf6d3b4
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/521/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-25T20:11:05Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: e1dc2fa43831c19a571264ce78f24df832f4b09fb86e2f5b69822d3ca97ea86b
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007556
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Scoped current ontology and MIM correspondence
  outcome: supported
  summary: '49 scoped ontology slots and 20 distinct nonobsolete IDs checked; label
    agreement is not supplied-form validation. 17 current secondary slots and 0 legacy
    slots have explicit exact-key lookups. Target linkage: primary 12/15 (80.00%),
    current secondary 8/15 (53.33%); these are linkage counts, not correctness scores.'
  target_ids:
  - CultureMech:007556
  evidence_ids:
  - grounding-inventory
  - mim
  - mimPinnedCatalog
  - mimPinnedTree
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:007556
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact selected accession and bounded trace dependency
  outcome: supported
  summary: TOGO M1040 explicitly identifies JCM 987; both primary and provider name
    CEJFB1T. The selected owner and generated target share the same scientific fields.
    M439 resolves as a maintained record, but only its trace-element subsection is
    relevant. Neither missing stock content nor an unassessed historical namesake
    is treated as a broken identifier.
  target_ids:
  - CultureMech:007556
  evidence_ids:
  - record
  - owner-0
  - primary987
  - provider1040
  - trace439
- assessment_id: source-forms
  area: grounding
  topic: Supplied salts, hydrates and dependency annotations
  outcome: concern
  summary: The selected base named salts, L-cysteine hydrochloride monohydrate and
    generic resazurin have compatible asserted identities. No sodium-resazurin defect
    is invented where the source says only resazurin. In the scoped M439 trace fields,
    CoCl2·6H2O uses anhydrous cobalt dichloride CHEBI:35696 and NiCl2·6H2O uses anhydrous
    nickel dichloride CHEBI:34887. Their labels resolve correctly but their formulas
    omit the six waters. The other explicitly named trace hydrates agree with their
    asserted forms.
  target_ids:
  - CultureMech:007556
  evidence_ids:
  - primary987
  - trace439
  - trace-jcm439
  - grounding-inventory
  - chebi35696
  - chebi34887
  - chebi8806
  - chebi91248
- assessment_id: preparation
  area: completeness
  topic: Ordered preparation and stock boundaries
  outcome: concern
  summary: Both selected layers omit the source pH adjustment to 7.6, N2–CO2 4:1 volume
    ratio, autoclaving, after-cooling anaerobic additions, gas-stream distribution
    and butyl-rubber sealing, and late sulfide addition. KOH and gas VARIABLE entries
    are not substitutes for those stages. Five solution placeholders and the top-level
    MgSO4 stock fail to represent the six named additions clearly.
  target_ids:
  - CultureMech:007556
  evidence_ids:
  - record
  - owner-0
  - primary987
  - provider1040
  - writer-stock
- assessment_id: classification
  area: scope
  topic: Complex liquid medium and growth limits
  outcome: supported
  summary: Yeast extract and tryptone support complex, undefined classification; no
    gelling agent is specified. The source identity and medium name do not establish
    a particular strain growth observation, incubation time, temperature, gas pressure
    or gas-flow rate. The high_metal flag is an imported qualitative annotation with
    no source threshold verified here.
  target_ids:
  - CultureMech:007556
  evidence_ids:
  - record
  - primary987
  - provider1040
- assessment_id: historical-scope
  area: provenance
  topic: Earlier review and current writer limits
  outcome: supported
  summary: 'All four exact historical reports were read: October 5 target/owner and
    M439 rows are source-unchecked inventories; the September 22 report describes
    the same unit, stock and preparation issues. Its historical namesake claims do
    not establish a current owner or authorize merger. Its description of the trace
    addition as post-autoclave is not adopted: the current primary places that 1 ml
    trace row in the initial mix. Current source stages govern. No original external
    raw is recovered by this record’s twelve-parent search.'
  target_ids:
  - CultureMech:007556
  evidence_ids:
  - historical-inventory
  - old-report-0
  - old-report-1
  - old-report-2
  - old-report-3
  - primary987
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 39 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:007556
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"Receiving batch\
    \ Distilled water\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"855\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"855\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 855,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n      }\n\
    \    ],\n    \"rationale\": \"The source prints 855 ml water = 0.855 L as a batch\
    \ input, not 855 g/L. No water density or final-volume makeup is inferred.\"\n\
    \  },\n  {\n    \"decision_id\": \"q2\",\n    \"subject\": \"Receiving batch NaCl\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"200\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"200\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 200,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      }\n    ],\n    \"rationale\": \"The source directly prints this batch\
    \ mass. Its numerical equality to the stored value does not establish a final-litre\
    \ concentration: 855 ml water and separately staged stock additions are not an\
    \ explicit final-volume instruction.\"\n  },\n  {\n    \"decision_id\": \"q3\"\
    ,\n    \"subject\": \"Receiving batch CaCl2・2H2O\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      }\n    ],\n    \"rationale\": \"The source directly prints this batch\
    \ mass. Its numerical equality to the stored value does not establish a final-litre\
    \ concentration: 855 ml water and separately staged stock additions are not an\
    \ explicit final-volume instruction.\"\n  },\n  {\n    \"decision_id\": \"q4\"\
    ,\n    \"subject\": \"Receiving batch NH4Cl\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 1,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      }\n    ],\n    \"rationale\": \"The source directly prints this batch\
    \ mass. Its numerical equality to the stored value does not establish a final-litre\
    \ concentration: 855 ml water and separately staged stock additions are not an\
    \ explicit final-volume instruction.\"\n  },\n  {\n    \"decision_id\": \"q5\"\
    ,\n    \"subject\": \"Receiving batch K2HPO4\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      }\n    ],\n    \"rationale\": \"The source directly prints this batch\
    \ mass. Its numerical equality to the stored value does not establish a final-litre\
    \ concentration: 855 ml water and separately staged stock additions are not an\
    \ explicit final-volume instruction.\"\n  },\n  {\n    \"decision_id\": \"q6\"\
    ,\n    \"subject\": \"Receiving batch Resazurin\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      }\n    ],\n    \"rationale\": \"The source prints 0.5 mg resazurin, not\
    \ 0.5 g/L. Preserve the milligram batch amount; no unsupported final-litre rate\
    \ or sodium-salt identity is substituted.\"\n  },\n  {\n    \"decision_id\": \"\
    q7\",\n    \"subject\": \"Receiving batch KCl\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.8,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      }\n    ],\n    \"rationale\": \"The source directly prints this batch\
    \ mass. Its numerical equality to the stored value does not establish a final-litre\
    \ concentration: 855 ml water and separately staged stock additions are not an\
    \ explicit final-volume instruction.\"\n  },\n  {\n    \"decision_id\": \"q8\"\
    ,\n    \"subject\": \"Receiving batch Sodium acetate\",\n    \"decision\": \"\
    unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sodium acetate\\\",\\n          \\\"volume\\\"\
    : 0.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n      }\n\
    \    ],\n    \"rationale\": \"The source directly prints this batch mass. Its\
    \ numerical equality to the stored value does not establish a final-litre concentration:\
    \ 855 ml water and separately staged stock additions are not an explicit final-volume\
    \ instruction.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n    \"subject\": \"\
    Receiving batch Yeast extract (BD-Difco)\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract (BD-Difco)\\\",\\n          \\\"\
    volume\\\": 1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"The source directly prints this batch mass.\
    \ Its numerical equality to the stored value does not establish a final-litre\
    \ concentration: 855 ml water and separately staged stock additions are not an\
    \ explicit final-volume instruction.\"\n  },\n  {\n    \"decision_id\": \"q10\"\
    ,\n    \"subject\": \"Receiving batch Tryptone (BD-Difco)\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Tryptone (BD-Difco)\\\",\\n          \\\"volume\\\
    \": 0.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"The source directly prints this batch mass.\
    \ Its numerical equality to the stored value does not establish a final-litre\
    \ concentration: 855 ml water and separately staged stock additions are not an\
    \ explicit final-volume instruction.\"\n  },\n  {\n    \"decision_id\": \"q11\"\
    ,\n    \"subject\": \"Receiving batch L-Cysteine・HCl・H2O\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"L-Cysteine・HCl・H2O\\\",\\n          \\\"volume\\\
    \": 0.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"The source directly prints this batch mass.\
    \ Its numerical equality to the stored value does not establish a final-litre\
    \ concentration: 855 ml water and separately staged stock additions are not an\
    \ explicit final-volume instruction.\"\n  },\n  {\n    \"decision_id\": \"q12\"\
    ,\n    \"subject\": \"Preparation reagent KOH\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KOH\\\"\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      },\n      {\n        \"source_key\": \"togoM1040\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\",\n\
    \        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly, adjust pH to 7.6 with KOH and autoclave under aN2--CO2\
    \ (4:1, v/v) gas mixture. After cooling, add the following solutions from anaerobic\
    \ stocks (autoclaved or *filter-sterilized):\",\n        \"snapshot_sha256\":\
    \ \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"No fixed mass or concentration is supplied.\
    \ KOH is a pH-adjustment reagent and the gases define the stated atmosphere; VARIABLE\
    \ does not establish a quantitative ingredient dose, pressure or flow rate.\"\n\
    \  },\n  {\n    \"decision_id\": \"q13\",\n    \"subject\": \"Preparation reagent\
    \ Carbon dioxide gas\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Carbon dioxide gas\\\"\",\n        \"snapshot_sha256\"\
    : \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM1040\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\",\n\
    \        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly, adjust pH to 7.6 with KOH and autoclave under aN2--CO2\
    \ (4:1, v/v) gas mixture. After cooling, add the following solutions from anaerobic\
    \ stocks (autoclaved or *filter-sterilized):\",\n        \"snapshot_sha256\":\
    \ \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"No fixed mass or concentration is supplied.\
    \ KOH is a pH-adjustment reagent and the gases define the stated atmosphere; VARIABLE\
    \ does not establish a quantitative ingredient dose, pressure or flow rate.\"\n\
    \  },\n  {\n    \"decision_id\": \"q14\",\n    \"subject\": \"Preparation reagent\
    \ Nitrogen gas\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[14]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrogen gas\\\"\",\n        \"snapshot_sha256\"\
    : \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM1040\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\",\n\
    \        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly, adjust pH to 7.6 with KOH and autoclave under aN2--CO2\
    \ (4:1, v/v) gas mixture. After cooling, add the following solutions from anaerobic\
    \ stocks (autoclaved or *filter-sterilized):\",\n        \"snapshot_sha256\":\
    \ \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"No fixed mass or concentration is supplied.\
    \ KOH is a pH-adjustment reagent and the gases define the stated atmosphere; VARIABLE\
    \ does not establish a quantitative ingredient dose, pressure or flow rate.\"\n\
    \  },\n  {\n    \"decision_id\": \"q15\",\n    \"subject\": \"Magnesium sulfate\
    \ stock addition\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% MgSO4・7H2O\\\",\\n          \\\"volume\\\"\
    : 50,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 10,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      },\n      {\n        \"source_key\": \"togoM1040\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\",\n\
    \        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly, adjust pH to 7.6 with KOH and autoclave under aN2--CO2\
    \ (4:1, v/v) gas mixture. After cooling, add the following solutions from anaerobic\
    \ stocks (autoclaved or *filter-sterilized):\",\n        \"snapshot_sha256\":\
    \ \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"50 ml = 0.05 L is the volume of a 10% MgSO4·7H2O\
    \ stock added after cooling, not 50 g/L magnesium sulfate. Preserve the stock\
    \ separately. Bare 10% does not establish a mass/volume basis.\"\n  },\n  {\n\
    \    \"decision_id\": \"q16\",\n    \"subject\": \"Receiving Trace element solution\
    \ (see Medium [M439])\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[0].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution (see Medium [M439])\\\"\
    ,\\n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n   \
    \     \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      }\n    ],\n    \"rationale\": \"The printed value is a stock-addition\
    \ volume, not G_PER_L. Preserve the named source stock and absolute batch dose;\
    \ do not infer a final-medium concentration. This trace addition belongs to the\
    \ initial mixture, not the after-cooling table.\"\n  },\n  {\n    \"decision_id\"\
    : \"q17\",\n    \"subject\": \"Receiving 8% NaHCO3 solution*\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"8% NaHCO3 solution*\\\",\\n          \\\"volume\\\
    \": 25,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 8,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"The printed value is a stock-addition volume,\
    \ not G_PER_L. Preserve the named source stock and absolute batch dose; do not\
    \ infer a final-medium concentration. The stated percent strength lacks a mass/volume\
    \ or mass/mass basis.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n    \"subject\"\
    : \"Receiving 1 M Glucose solution\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"1 M Glucose solution\\\",\\n          \\\"volume\\\
    \": 20,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 1,\\n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\"\
    : \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"The printed value is a stock-addition volume,\
    \ not G_PER_L. Preserve the named source stock and absolute batch dose; do not\
    \ infer a final-medium concentration. The 1 M glucose strength is explicit; 20\
    \ ml contains 0.020 mol, but final-medium molarity remains unresolved without\
    \ an explicit final volume.\"\n  },\n  {\n    \"decision_id\": \"q19\",\n    \"\
    subject\": \"Receiving 10% Tryptone solution\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% Tryptone solution\\\",\\n          \\\"volume\\\
    \": 50,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 10,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"The printed value is a stock-addition volume,\
    \ not G_PER_L. Preserve the named source stock and absolute batch dose; do not\
    \ infer a final-medium concentration. The stated percent strength lacks a mass/volume\
    \ or mass/mass basis.\"\n  },\n  {\n    \"decision_id\": \"q20\",\n    \"subject\"\
    : \"Receiving 5% Na2S・9H2O solution\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CEJFB1T_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% Na2S・9H2O solution\\\",\\n          \\\"volume\\\
    \": 8,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 5,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      },\n      {\n        \"source_key\": \"togoM1040\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\",\n\
    \        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"Aseptically distribute the medium into culture vessels under a stream of N2--CO2\
    \ (4:1, v/v), and seal with butyl rubber stoppers. Prior to inoculation, add per\
    \ liter the following solution from an anaerobic stock (autoclave and store under\
    \ a N2 atmosphere).\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      }\n    ],\n    \"rationale\": \"The final paragraph explicitly gives 8\
    \ ml per liter of 5% Na2S·9H2O stock before inoculation. A dose of 8 ML_PER_L\
    \ is source-supported; 8 G_PER_L is not. Bare 5% does not justify a sulfide mass\
    \ concentration, and this per-litre instruction does not retroactively supply\
    \ a measured denominator for the preceding batch.\"\n  },\n  {\n    \"decision_id\"\
    : \"q21\",\n    \"subject\": \"M439 trace batch HCl (25%)\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.5\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM439\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"HCl (25%)\\\",\\n          \\\"volume\\\": 12.5,\\\
    n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 25,\\n  \
    \        \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      },\n      {\n        \"source_key\": \"togoM439\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\",\n \
    \       \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 987,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"rationale\": \"This trace-stock source amount is in ml, not a receiving-medium\
    \ G_PER_L value. Preserve its stock batch scope; listed water does not establish\
    \ final stock volume. HCl is 25% with unspecified basis; do not infer density\
    \ or mass.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"subject\": \"M439\
    \ trace batch Na2MoO4・2H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"36\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM439\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 36,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      },\n\
    \      {\n        \"source_key\": \"togoM439\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 987,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"rationale\": \"This trace-stock source amount is in mg, not a receiving-medium\
    \ G_PER_L value. Preserve its stock batch scope; listed water does not establish\
    \ final stock volume.\"\n  },\n  {\n    \"decision_id\": \"q23\",\n    \"subject\"\
    : \"M439 trace batch H3BO3\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM439\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 30,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      },\n      {\n        \"source_key\": \"togoM439\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\",\n \
    \       \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 987,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"rationale\": \"This trace-stock source amount is in mg, not a receiving-medium\
    \ G_PER_L value. Preserve its stock batch scope; listed water does not establish\
    \ final stock volume.\"\n  },\n  {\n    \"decision_id\": \"q24\",\n    \"subject\"\
    : \"M439 trace batch FeSO4・7H2O\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM439\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4・7H2O\\\",\\n          \\\"volume\\\": 2.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      },\n      {\n        \"source_key\": \"togoM439\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\",\n \
    \       \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 987,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"rationale\": \"This trace-stock source amount is in g, not a receiving-medium\
    \ G_PER_L value. Preserve its stock batch scope; listed water does not establish\
    \ final stock volume.\"\n  },\n  {\n    \"decision_id\": \"q25\",\n    \"subject\"\
    : \"M439 trace batch MnCl2・4H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM439\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2・4H2O\\\",\\n          \\\"volume\\\": 100,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      },\n      {\n        \"source_key\": \"togoM439\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\",\n \
    \       \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 987,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"rationale\": \"This trace-stock source amount is in mg, not a receiving-medium\
    \ G_PER_L value. Preserve its stock batch scope; listed water does not establish\
    \ final stock volume.\"\n  },\n  {\n    \"decision_id\": \"q26\",\n    \"subject\"\
    : \"M439 trace batch CoCl2・6H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"190\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM439\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 190,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      },\n      {\n        \"source_key\": \"togoM439\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\",\n \
    \       \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 987,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"rationale\": \"This trace-stock source amount is in mg, not a receiving-medium\
    \ G_PER_L value. Preserve its stock batch scope; listed water does not establish\
    \ final stock volume.\"\n  },\n  {\n    \"decision_id\": \"q27\",\n    \"subject\"\
    : \"M439 trace batch NiCl2・6H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"24\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM439\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2・6H2O\\\",\\n          \\\"volume\\\": 24,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      },\n      {\n        \"source_key\": \"togoM439\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\",\n \
    \       \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 987,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"rationale\": \"This trace-stock source amount is in mg, not a receiving-medium\
    \ G_PER_L value. Preserve its stock batch scope; listed water does not establish\
    \ final stock volume.\"\n  },\n  {\n    \"decision_id\": \"q28\",\n    \"subject\"\
    : \"M439 trace batch ZnSO4・7H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"144\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM439\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 144,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      },\n      {\n        \"source_key\": \"togoM439\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\",\n \
    \       \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 987,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"rationale\": \"This trace-stock source amount is in mg, not a receiving-medium\
    \ G_PER_L value. Preserve its stock batch scope; listed water does not establish\
    \ final stock volume.\"\n  },\n  {\n    \"decision_id\": \"q29\",\n    \"subject\"\
    : \"M439 trace batch CuCl2・2H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM439\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2・2H2O\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      },\n      {\n        \"source_key\": \"togoM439\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\",\n \
    \       \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 987,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"rationale\": \"This trace-stock source amount is in mg, not a receiving-medium\
    \ G_PER_L value. Preserve its stock batch scope; listed water does not establish\
    \ final stock volume.\"\n  },\n  {\n    \"decision_id\": \"q30\",\n    \"subject\"\
    : \"M439 trace water\",\n    \"decision\": \"add\",\n    \"local_fields\": [],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM439\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 987,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"rationale\": \"Retain 987 ml water for this stock only. The merged\
    \ parent water and other parent recipes are excluded, and 987 ml water plus 12.5\
    \ ml acid is not an explicit final-volume instruction.\"\n  },\n  {\n    \"decision_id\"\
    : \"q31\",\n    \"subject\": \"8% bicarbonate stock strength\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"8% NaHCO3 solution*\\\",\\n          \\\"volume\\\
    \": 25,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 8,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"Preserve the stated stock strength separately\
    \ from dose. The molarity is explicit for glucose; every bare percent remains\
    \ basis-unspecified and is not converted to grams or final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q32\",\n    \"subject\": \"10% magnesium sulfate\
    \ stock strength\",\n    \"decision\": \"add\",\n    \"local_fields\": [],\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1040\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% MgSO4・7H2O\\\",\\n          \\\"volume\\\"\
    : 50,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 10,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the stated stock strength separately\
    \ from dose. The molarity is explicit for glucose; every bare percent remains\
    \ basis-unspecified and is not converted to grams or final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q33\",\n    \"subject\": \"1 M glucose stock\
    \ strength\",\n    \"decision\": \"add\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1040\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\",\n\
    \        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"1 M Glucose solution\\\",\\n          \\\"volume\\\
    \": 20,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 1,\\n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\"\
    : \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"Preserve the stated stock strength separately\
    \ from dose. The molarity is explicit for glucose; every bare percent remains\
    \ basis-unspecified and is not converted to grams or final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q34\",\n    \"subject\": \"10% tryptone stock\
    \ strength\",\n    \"decision\": \"add\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1040\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\",\n\
    \        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% Tryptone solution\\\",\\n          \\\"volume\\\
    \": 50,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 10,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"Preserve the stated stock strength separately\
    \ from dose. The molarity is explicit for glucose; every bare percent remains\
    \ basis-unspecified and is not converted to grams or final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q35\",\n    \"subject\": \"5% sulfide stock\
    \ strength\",\n    \"decision\": \"add\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1040\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\",\n\
    \        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% Na2S・9H2O solution\\\",\\n          \\\"volume\\\
    \": 8,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 5,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the stated stock strength separately\
    \ from dose. The molarity is explicit for glucose; every bare percent remains\
    \ basis-unspecified and is not converted to grams or final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q36\",\n    \"subject\": \"25% hydrochloric\
    \ acid stock strength\",\n    \"decision\": \"add\",\n    \"local_fields\": [],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM439\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"HCl (25%)\\\",\\n          \\\"volume\\\": 12.5,\\\
    n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 25,\\n  \
    \        \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the stated stock strength separately\
    \ from dose. The molarity is explicit for glucose; every bare percent remains\
    \ basis-unspecified and is not converted to grams or final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q37\",\n    \"subject\": \"Initial pH, gas\
    \ ratio and post-cooling boundary\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1040\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly, adjust pH to 7.6 with KOH and autoclave under aN2--CO2\
    \ (4:1, v/v) gas mixture. After cooling, add the following solutions from anaerobic\
    \ stocks (autoclaved or *filter-sterilized):\",\n        \"snapshot_sha256\":\
    \ \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\n     \
    \ }\n    ],\n    \"rationale\": \"Retain pH 7.6 with KOH, N2–CO2 4:1 (v/v), initial\
    \ autoclaving and after-cooling anaerobic additions. The asterisk identifies filter-sterilized\
    \ bicarbonate in the primary table. No pressure, flow rate or final-medium denominator\
    \ is supplied.\"\n  },\n  {\n    \"decision_id\": \"q38\",\n    \"subject\": \"\
    Distribution and late sulfide sequence\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1040\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1040\"\
    ,\n        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"Aseptically distribute the medium into culture vessels under a stream of N2--CO2\
    \ (4:1, v/v), and seal with butyl rubber stoppers. Prior to inoculation, add per\
    \ liter the following solution from an anaerobic stock (autoclave and store under\
    \ a N2 atmosphere).\",\n        \"snapshot_sha256\": \"9d493eb03ccaa65d9a6a73c208c6ff7fe507e128bdb8336be43444f3dcb7a498\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve gas-stream distribution, butyl-rubber\
    \ sealing, pre-inoculation timing and sulfide-stock autoclaving/storage under\
    \ N2. These are receiving-medium stages, not M439 parent preparation.\"\n  },\n\
    \  {\n    \"decision_id\": \"q39\",\n    \"subject\": \"JCM 987 autoclave default\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm987\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=987\",\n        \"source_locator\"\
    : \"Extracted text line 4\",\n        \"exact_source_quote\": \"Unless otherwise\
    \ stated, sterilize media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\"\
    : \"44d12e927566387e3e394d950289f0f15241b0e0618ecbf30a869bc7fb3768d6\",\n    \
    \    \"parsed_text_sha256\": \"ecb4488c51dd75c5c866e44ff9b60c5bb44ca94f7f9d7cdc15d3d45e2bb7f208\"\
    \n      }\n    ],\n    \"rationale\": \"The selected JCM 987 page gives 121°C\
    \ for 15 min unless otherwise stated. Retain the source-specific default and explicit\
    \ filter/autoclave stock distinctions; do not borrow defaults from other recipes.\"\
    \n  }\n]"
findings:
- finding_id: f1
  issue_key: cm007556-unit-stock-boundaries
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water, indicator and stock doses lose their source dimensions
  description: Both selected layers store water 855 G_PER_L, resazurin 0.5 G_PER_L
    and milliliter stock doses as G_PER_L. Five stocks are unnamed empty placeholders;
    the 50 ml magnesium-sulfate stock remains a top-level ingredient. Other batch
    masses also lack an established final-litre denominator.
  target_ids:
  - CultureMech:007556
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - primary987
  - provider1040
  - quantity-inventory
  - writer-togo
  - writer-stock
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: review-ingredient-concentrations:source-unit-basis
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: cm007556-trace-hydrate-scope
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Referenced trace stock uses anhydrous cobalt and nickel IDs
  description: The M439 trace dependency ingredients[17].term and ingredients[18].term
    name cobalt and nickel hexahydrates but identify anhydrous CHEBI:35696 and CHEBI:34887.
    These are dependency-only locations, not target ingredient indices. The selected
    base salt annotations are not implicated.
  target_ids:
  - CultureMech:007556
  field_paths:
  - solutions
  evidence_ids:
  - trace439
  - trace-jcm439
  - chebi35696
  - chebi34887
  - grounding-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml
    role: 'scoped dependency: solutions[0] identity and ingredients[12:21] trace composition
      only; parent dose excluded'
  rule_id: review-yaml-record:supplied-hydrate-correspondence
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: cm007556-preparation-stages
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Ordered source preparation is absent
  description: The selected target and owner omit source pH adjustment, gas ratio,
    sterilization and cooling boundaries, stock-treatment distinction, vessel sealing
    and pre-inoculation sulfide addition. Variable gas/KOH ingredients cannot encode
    these facts.
  target_ids:
  - CultureMech:007556
  field_paths:
  - preparation_steps
  evidence_ids:
  - primary987
  - provider1040
  - writer-togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: review-yaml-record:preparation-completeness
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: cm007556-history-source-accession
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Import history conflates the TOGO and JCM accessions
  description: 'The initial event says Source: JCM, ID: M1040. M1040 is the TOGO accession;
    the source metadata identifies JCM_M987. Existing history should remain append-only.'
  target_ids:
  - CultureMech:007556
  field_paths:
  - curation_history[0].notes
  evidence_ids:
  - provider1040
  - history-full
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: review-yaml-record:source-accession-history
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Correct source-labelled water, mass and dose dimensions in the maintained
    owner; preserve six distinct stock additions and their stages. Use 8 ML_PER_L
    only for the explicitly per-litre late sulfide dose. Preserve unspecified percentage
    bases and avoid final-volume assumptions.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007556
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml
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
  description: Resolve exact hexahydrate identifiers in the scoped maintained trace
    definition, with new source-form evidence, before reusing it. Preserve unrelated
    parent stocks and conditions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007556
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml
    role: 'scoped dependency: solutions[0] identity and ingredients[12:21] trace composition
      only; parent dose excluded'
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
  description: Add exact source-scoped ordered preparation and stock strengths to
    the maintained owner, then regenerate and verify freshness. Preserve absent incubation
    and gas-pressure values as unknown.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007556
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml
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
  description: Append a narrow provenance clarification distinguishing TOGO M1040
    and JCM 987 during authorized curation; retain the original event and actual source
    access dates.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007556
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.yaml
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
- Twenty dependency concentration fields belong to excluded M439 parent recipes or
  its receiving dose and are not transferred. Current label/MIM agreement does not
  certify source chemical forms or historical mapping validity. No phenotype or growth
  experiment is asserted.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-053
- generated-medium
```
