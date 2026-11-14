# Source and formulation review: ae_medium (CultureMech:006656)

- Review: 20261021T115304Z-culturemech-006656-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T11:43:28Z
- Finished UTC: 2026-10-21T11:53:04Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated AE medium still has six ingredient rows, mass units for two source liquid volumes, and no preparation, while both maintained owners contain a later seven-row repair with water, volume units and source preparation. The exact DSMZ 849 formulation is available, but narrow amount evidence and owner-only supply identities need qualification. Exact KOMODO detail verification remains unavailable, so source coverage is partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 189; batch 019 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eighteen task batches contain 180 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 182 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006656 | data/merge_yaml/merged/AE_MEDIUM.yaml | generated | ae_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006656 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006656 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch019/189/strict.tsv |
| validate-terms | passed | True | CultureMech:006656 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006656 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006656 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo849detail | unavailable | True | CultureMech:006656 | The exact KOMODO MediaInfo=849 public request returned HTTP 403. Required verification of this contributor-specific detail remains unavailable. Accessible DSMZ 849 and current MediaDive evidence establish their own formulation, not the inaccessible historical KOMODO detail. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006656.

The four documented recipes completed; interpret the scope of each separately.

### Exact accession, contributors and duplicate links

identity: supported. Targets: CultureMech:006656.

CultureMech:006656 is the generated KOMODO 849 record merged with the DSMZ 849 owner CultureMech:002006. The explicit source-duplicate paths and IDs resolve exactly, and both current owner ingredient arrays agree. Their source mapping is supported; a fingerprint alone is not the identity evidence. Exact KOMODO detail remains an unavailable source check.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006656.

9 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence. All 20 ingredient and stock-dose concentration instances across the target and maintained owners are explicitly covered; additional rows retain preparation quantities and source-only components.

[
  {
    "quantity_id": "q1",
    "ingredient_or_context": "Glucose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AE_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ae_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_scope": "5 g in the DSMZ-listed batch; preserve exact source grade and the explicitly identified 1000 ml provider normalization basis.",
    "source_snippets": [
      {
        "source_key": "mediadive849api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/849",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 27.7531,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8"
      }
    ],
    "rationale": "Both current owners retain the source number and correct dimensional unit but have source/notes/reference annotations rather than attached exact concentration evidence. The scalar agrees with the provider g_l value; retain that nominal denominator separately from the primary batch table."
  },
  {
    "quantity_id": "q2",
    "ingredient_or_context": "Yeast extract",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AE_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ae_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_scope": "3 g in the DSMZ-listed batch; preserve exact source grade and the explicitly identified 1000 ml provider normalization basis.",
    "source_snippets": [
      {
        "source_key": "mediadive849api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/849",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8"
      }
    ],
    "rationale": "Both current owners retain the source number and correct dimensional unit but have source/notes/reference annotations rather than attached exact concentration evidence. The scalar agrees with the provider g_l value; retain that nominal denominator separately from the primary batch table."
  },
  {
    "quantity_id": "q3",
    "ingredient_or_context": "Peptone",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AE_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "4.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ae_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "4.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_scope": "4 g in the DSMZ-listed batch; preserve exact source grade and the explicitly identified 1000 ml provider normalization basis.",
    "source_snippets": [
      {
        "source_key": "mediadive849api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/849",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\": 1,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8"
      }
    ],
    "rationale": "Both current owners retain the source number and correct dimensional unit but have source/notes/reference annotations rather than attached exact concentration evidence. The scalar agrees with the provider g_l value; retain that nominal denominator separately from the primary batch table."
  },
  {
    "quantity_id": "q4",
    "ingredient_or_context": "Absolute ethanol",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AE_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "30.0",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ae_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "30.0",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_scope": "30 ml in the DSMZ-listed batch; preserve exact source grade and the explicitly identified 1000 ml provider normalization basis.",
    "source_snippets": [
      {
        "source_key": "mediadive849api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/849",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Absolute ethanol\",\n                        \"compound_id\": 788,\n                        \"amount\": 30,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8"
      }
    ],
    "rationale": "Both current owners retain the source number and correct dimensional unit but have source/notes/reference annotations rather than attached exact concentration evidence. The generated G_PER_L field is wrong for the source ml dose. Do not convert volume to mass using an assumed density."
  },
  {
    "quantity_id": "q5",
    "ingredient_or_context": "Glacial acetic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AE_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "30.0",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ae_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "30.0",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_scope": "30 ml in the DSMZ-listed batch; preserve exact source grade and the explicitly identified 1000 ml provider normalization basis.",
    "source_snippets": [
      {
        "source_key": "mediadive849api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/849",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Glacial acetic acid\",\n                        \"compound_id\": 787,\n                        \"amount\": 30,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8"
      }
    ],
    "rationale": "Both current owners retain the source number and correct dimensional unit but have source/notes/reference annotations rather than attached exact concentration evidence. The generated G_PER_L field is wrong for the source ml dose. Do not convert volume to mass using an assumed density."
  },
  {
    "quantity_id": "q6",
    "ingredient_or_context": "Agar",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AE_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "9",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "9.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ae_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "9.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_scope": "9 g in the DSMZ-listed batch; preserve exact source grade and the explicitly identified 1000 ml provider normalization basis.",
    "source_snippets": [
      {
        "source_key": "mediadive849api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/849",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 9,\n                        \"unit\": \"g\",\n                        \"g_l\": 9,\n                        \"mmol_l\": 26.7594,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8"
      }
    ],
    "rationale": "Both current owners retain the source number and correct dimensional unit but have source/notes/reference annotations rather than attached exact concentration evidence. The scalar agrees with the provider g_l value; retain that nominal denominator separately from the primary batch table. This amount belongs to the agar-bearing solid preparation. The source also names liquid media; it does not quantify a separate liquid-branch agar row, and no zero or universal agar dose is invented."
  },
  {
    "quantity_id": "q7",
    "ingredient_or_context": "Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AE_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "940.0",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ae_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "940.0",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_scope": "940 ml in the DSMZ-listed batch; preserve exact source grade and the explicitly identified 1000 ml provider normalization basis.",
    "source_snippets": [
      {
        "source_key": "mediadive849api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/849",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 940,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8"
      }
    ],
    "rationale": "Both current owners retain the source number and correct dimensional unit but have source/notes/reference annotations rather than attached exact concentration evidence. Water is absent from the generated target and present in both owners as 940 ML_PER_L. Preserve the listed water volume rather than an inferred water mass."
  },
  {
    "quantity_id": "q8",
    "ingredient_or_context": "Provider-declared volume",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AE_MEDIUM.yaml",
        "field_path": "notes",
        "stored": "Source: KOMODO ModelSEED &#124; ID: 849 &#124; DSMZ Medium: 849 (mediadive.medium:849) &#124; Aerobic: No",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml",
        "field_path": "notes",
        "stored": "Source: KOMODO ModelSEED &#124; ID: 849 &#124; DSMZ Medium: 849 (mediadive.medium:849) &#124; Aerobic: No",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/ae_medium.yaml",
        "field_path": "notes",
        "stored": "Source: DSMZ &#124; Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium849.pdf",
        "decision": "add"
      }
    ],
    "proposed_source_scope": "Retain 1000 ml as the provider-declared batch basis; list 940 ml water plus two 30 ml liquids separately.",
    "source_snippets": [
      {
        "source_key": "mediadive849api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/849",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8"
      }
    ],
    "rationale": "940+30+30=1000 ml listed liquid inputs; the source does not report measured final volume after dissolution and mixing."
  },
  {
    "quantity_id": "q9",
    "ingredient_or_context": "Plate-specific humidity threshold",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AE_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": "Incubate plates in sealed containers to keep humidity high above 90%.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ae_medium.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": "Incubate plates in sealed containers to keep humidity high above 90%.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_scope": "Preserve the source &gt;90% humidity qualifier only for plates in sealed containers.",
    "source_snippets": [
      {
        "source_key": "mediadive849api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/849",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "humidity high (&gt; 90%).",
        "snapshot_sha256": "9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8"
      }
    ],
    "rationale": "Both owners already preserve above 90% in prose; the generated record omits the preparation. This is a plate-specific humidity context, not a solution concentration or inferred organism growth optimum."
  }
]

### Source-specific forms and current CHEBI-based secondary correspondence

grounding: concern. Targets: CultureMech:006656.

7 distinct asserted chemical IDs resolve as nonobsolete. 0 local label instances differ from canonical labels. 5 of 5 distinct current CHEBI-based secondary keys have exact mapped preferred-term rows in the pinned index; unresolved keys: []. This does not validate historical legacy MIM IDs, supplied hydrates, stereochemistry or catalog products. Target primary/secondary linkage covers glucose and agar only. Both later owners add ethanol, acetic acid, water, FOODON yeast extract and MICRO peptone. The two non-CHEBI supply identities need source-specific qualification despite matching canonical labels; neither annotation validates concentration.

{"metrics": [{"input": "data/merge_yaml/merged/AE_MEDIUM.yaml", "ingredient_instances": 6, "primary": 2, "current_secondary": 2, "primary_percent": 33.333333333333336, "current_secondary_percent": 33.333333333333336}, {"input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml", "ingredient_instances": 7, "primary": 7, "current_secondary": 5, "primary_percent": 100.0, "current_secondary_percent": 71.42857142857143}, {"input": "data/normalized_yaml/bacterial/ae_medium.yaml", "ingredient_instances": 7, "primary": 7, "current_secondary": 5, "primary_percent": 100.0, "current_secondary_percent": 71.42857142857143}], "definition": "Ingredient-instance linkage percentages on a 0–100 scale, using each stated layer denominator; these are not scientific correctness scores.", "label_drift": []}

### Source-scoped preparation, conditions and physical-state branches

completeness: concern. Targets: CultureMech:006656.

The generated record omits all preparation. Both owners preserve separate ethanol/acetic-acid treatment, the source filtration-or-closed-bottle-autoclaving alternatives, and plate humidity. Preserve the alternatives in structured method scope: the owner FILTER_STERILIZE action tag must not erase its own autoclave option, and the MIX-tagged plate incubation text is not a mixing instruction. No temperature/time is printed, so no cycle is inferred.

### Medium classification, applications and organism claim scope

scope: supported. Targets: CultureMech:006656.

COMPLEX/UNDEFINED is appropriate for yeast extract and peptone. SOLID_AGAR matches the table containing agar but represents only the solid preparation; the source also names liquid media. No universal agar requirement, organism identity, aerobic phenotype or optimal growth follows from the name or KOMODO flag.

### Exact supplied chemical forms and mixture identity

grounding: concern. Targets: CultureMech:006656.

Source ethanol is absolute and acid is glacial; preserve these grade names. Generic yeast extract does not establish the FOODON not-heat-treated annotation, and generic peptone does not establish MICRO mammalian enzymatic supply identity. This is unverified narrowing, not a claim that the identifiers do not exist.

### Claim-level formulation evidence and current annotations

evidence: concern. Targets: CultureMech:006656.

The later source-specific repair adds owner notes, source fields, a primary reference and ingredient-curated flags, but no exact ingredient evidence. Target lacks those repair fields. Attach narrow source snippets and explain provider normalization; a flag or root reference alone cannot make a quantity verified.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006656.

21 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Later maintained repair versus stale generated target

ownership: concern. Targets: CultureMech:006656.

The target merge events are dated August 6; both owners contain the September 11 source-specific repair. Regenerate only after source scope, amount evidence and supply identities are settled in both owners and their named repair helper. Do not repeat already repaired owner liquid-unit errors as though they remain there.

## Findings

### f1: The generated recipe retains mass units for liquid doses and omits water

blocker / open / confirmed; issue key: cm006656-stale-liquid-units-water.

Target ingredients[3] and [4] give 30 G_PER_L, whereas DSMZ 849 lists 30 ml of each liquid. Target lacks the 940 ml water row. Both maintained owners already contain the corrected volume units and water, so this is also an exact generated-freshness discrepancy.

### f2: Later owner identifiers narrow unspecified ingredient supply identities

major / open / confirmed; issue key: cm006656-owner-supply-specificity.

Only the maintained owners assign MICRO:0000178 to unqualified peptone and FOODON:03315426 to yeast extract. The former specifies mammalian enzymatic digest and the latter carries a not-heat-treated SIREN annotation; the DSMZ source does not specify either supply restriction. The target itself does not assert these two terms.

### f3: Generated preparation and narrow formulation evidence remain incomplete

major / open / confirmed; issue key: cm006656-preparation-branch-evidence.

The target loses the later owner preparation entirely. Owner prose retains the important separate liquid handling and humidity context, but typed action tags must preserve alternatives and incubation scope. Neither layer has narrow formulation evidence, and the solid recipe should be distinguished from the source-mentioned liquid preparation.

### f4: Inherited timestamps do not provide a parseable chronology

minor / open / confirmed; issue key: cm006656-history-timestamp-context.

The target and KOMODO owner each retain an import timestamp with literal .fZ and a timezone-naive resolver timestamp. Other history, including the later repair, remains separate. Passing deterministic checks do not turn these strings into reliable dated events.

## Recommended Actions And Acceptance Checks

### a1

Preserve the existing owner repair, qualify its provider batch basis and attach exact evidence. After completing the bounded owner work, regenerate the target so corrected liquid units and the source water row survive; do not patch the generated file.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

In both normalized owners and the named repair helper, qualify or remove unsupported supply-specific narrowing unless exact product evidence is obtained. Preserve the mixture names and source amounts; do not invent a replacement ontology ID or transplant Bacto product composition.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach exact evidence to each quantity and scoped preparation claim in both owners, retain source alternatives and plate-only context, and document the represented physical-state branch. Regenerate only afterward. Do not invent cycle parameters or a complete liquid variant.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve the historical entries and append a bounded clarification when curation is authorized. Do not invent the missing fractional seconds or timezone, or rewrite earlier events through the repair helper.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AE_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/ae_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AE_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AE_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch019/189/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch019/189/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AE_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AE_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AE_MEDIUM.yaml:1:id: CultureMech:006656<br>./data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml:1:id: CultureMech:006656<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch019/source-preflight-bound/189/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 11 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| dsmz849 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium849.pdf; Complete seven-row table and preparation paragraph | supports | DSMZ 849 identifies AE medium, its exact batch amounts, both liquid and solid preparation scope, separate ethanol/acetic-acid handling and a plate-specific humidity condition. No sterilization cycle or named organism is supplied. |
| mediadive849api | https://mediadive.dsmz.de/rest/medium/849; $.data.medium; $.data.solutions[0] | supports | Provider solution 1737 has seven recipe rows, declares 1000 ml and supplies four g_l values; all liquid additions remain ml. Listed liquids sum to 1000 ml, without independently measured final-volume evidence. |
| komodoMediaList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Actual table header and exact first-cell 849 mapping row | supports | The exact public table supports the KOMODO 849 to DSMZ 849 accession mapping. Aerobic metadata is catalog provenance, not a demonstrated phenotype or instruction for this medium. |
| komodo849detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=849; Preserved exact public retrieval result | context_only | The exact KOMODO MediaInfo=849 public request returned HTTP 403. Required verification of this contributor-specific detail remains unavailable. Accessible DSMZ 849 and current MediaDive evidence establish their own formulation, not the inaccessible historical KOMODO detail. |
| supply-foodon | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; Exact term description/SIREN annotation | supports | Owner-only FOODON:03315426 resolves to yeast extract, with a SIREN annotation for not heat-treated material. The unqualified source yeast-extract row does not establish this supplier processing state. |
| supply-micro | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178; Exact annotation.definition and definition source | supports | Owner-only MICRO:0000178 resolves to peptone but its definition specifies an enzymatic digest of mammalian animal protein; the exact source only says peptone. The accompanying Bacto product source is not evidence that DSMZ 849 uses that product. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch019/189/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15366 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15366; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | CHEBI:15366: acetic acid. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | CHEBI:15377: water. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| chebi16236 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16236; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | CHEBI:16236: ethanol. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | CHEBI:17234: glucose. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | CHEBI:2509: agar. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | FOODON:03315426: yeast extract. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| micro0000178 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178; Exact OLS identifier, canonical label, nonobsolete status, definitions and chemical annotations | supports | MICRO:0000178: peptone. Source-specific forms are assessed separately; valid ontology metadata is not proof of supplied-form correspondence. |
| chemical-context | /private/tmp/culturemech-review-work-batch019/189/chemical-grounding-context.json; Every primary and current CHEBI-based secondary ingredient term in the target and maintained owners | context_only | Full OLS annotations, local instance locators, label differences, pinned exact-key MIM rows and layer-specific linkage metrics. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact identifier rows and pinned metadata source commit; no fuzzy replacements | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "current_secondary_rows": {"CHEBI:15366": [{"label": "Acetic acid", "match_type": "preferred_term", "identifier": "CHEBI:15366", "preferred_term": "Acetic acid", "ontology_id": "CHEBI:15366", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16236": [{"label": "Ethanol", "match_type": "preferred_term", "identifier": "CHEBI:16236", "preferred_term": "Ethanol", "ontology_id": "CHEBI:16236", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing": []} |
| history-metadata | data/merge_yaml/merged/AE_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml; data/normalized_yaml/bacterial/ae_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:03.159005"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:03.159005"}]}, {"input": "data/normalized_yaml/bacterial/ae_medium.yaml", "events": 6, "timestamp_issues": []}] |
| writer-0 | scripts/repair_dsmz_849_ae_score15.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The exact repair helper explicitly replaces the old six-row signature with seven rows, changes ethanol/acetic acid to ML_PER_L, adds water and preparation, and assigns the owner-only FOODON/MICRO IDs. It adds references but no ingredient evidence. Its existing-event branch rewrites a matching history event; follow-up must instead preserve append-only history. Current merge compares formulation scope; no generator was executed or historical replay inferred. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The exact repair helper explicitly replaces the old six-row signature with seven rows, changes ethanol/acetic acid to ML_PER_L, adds water and preparation, and assigns the owner-only FOODON/MICRO IDs. It adds references but no ingredient evidence. Its existing-event branch rewrites a matching history event; follow-up must instead preserve append-only history. Current merge compares formulation scope; no generator was executed or historical replay inferred. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact KOMODO MediaInfo=849 public request returned HTTP 403. Required verification of this contributor-specific detail remains unavailable. Accessible DSMZ 849 and current MediaDive evidence establish their own formulation, not the inaccessible historical KOMODO detail.
- Partial source coverage rests on the unavailable exact KOMODO detail, not on the available DSMZ primary. Current public mapping and the primary do not authenticate a historical resolver fetch.
- The source table and provider normalization are kept separate from measured final volume. No growth or taxonomy assertion is added from the source phrase this organism or the catalog aerobic flag.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T115304Z-culturemech-006656-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: ae_medium (CultureMech:006656)'
started_at: '2026-10-21T11:43:28Z'
finished_at: '2026-10-21T11:53:04Z'
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
summary: The generated AE medium still has six ingredient rows, mass units for two
  source liquid volumes, and no preparation, while both maintained owners contain
  a later seven-row repair with water, volume units and source preparation. The exact
  DSMZ 849 formulation is available, but narrow amount evidence and owner-only supply
  identities need qualification. Exact KOMODO detail verification remains unavailable,
  so source coverage is partial.
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
  - path: data/merge_yaml/merged/AE_MEDIUM.yaml
    sha256: c7fa9f6fefd0e1ddee5c0109436e288d35da88f47aa8007194eab48cf6c5b9ff
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml
    sha256: 3c53299493bac8510d1e357092c297a071d5a7935154424e3a121838afa96829
    role: context
  - path: data/normalized_yaml/bacterial/ae_medium.yaml
    sha256: b75660bfeda5a4c2daddb2a3d63a384cdc458414d5b8e9285f600bf2ecbe5484
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
  - path: scripts/fetch_medium_concentration_sources.py
    sha256: 746c2828863e6ee409d88409a540ea0a8d01ffad3e38be4a4a47f47bec5bbeb5
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/record_io.py
    sha256: bff4715f85d7ff2ff681b88f0a2de2667e5767d7a2c196bd50a37d5d329957ac
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_dsmz_849_ae_score15.py
    sha256: dad411e6835547a6fe0f168d5c6036b0592dc508466617cbecd3fd7662c08633
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
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 189; batch 019 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding eighteen task batches
    contain 180 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 182 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006656
targets:
- target_id: CultureMech:006656
  path: data/merge_yaml/merged/AE_MEDIUM.yaml
  label: ae_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ae_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AE_MEDIUM.yaml --workers 1
    --out /private/tmp/culturemech-review-work-batch019/189/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch019/189/strict.tsv"
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006656
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
  - CultureMech:006656
- check_id: komodo849detail-source-access
  name: 'Exact source content access: komodo849detail'
  required: true
  status: unavailable
  summary: The exact KOMODO MediaInfo=849 public request returned HTTP 403. Required
    verification of this contributor-specific detail remains unavailable. Accessible
    DSMZ 849 and current MediaDive evidence establish their own formulation, not the
    inaccessible historical KOMODO detail.
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - komodo849detail-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AE_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:53:03Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:53:03Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/ae_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:53:03Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:38.964723Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AE_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch019/189/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:40.509003Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch019/189/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:42.348002Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:43.339603Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:53:03Z'
  support: supports
  summary: './data/merge_yaml/merged/AE_MEDIUM.yaml:1:id: CultureMech:006656

    ./data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml:1:id: CultureMech:006656

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/source-preflight-bound/189/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:53:03Z'
  support: supports
  summary: 11 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 3f4d60334a0fae38a0fcabeacbc9476021498f0664470d0094765635189399bc
- evidence_id: dsmz849
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium849.pdf
  locator: Complete seven-row table and preparation paragraph
  accessed_at: '2026-10-21T11:30:39.774195Z'
  support: supports
  summary: DSMZ 849 identifies AE medium, its exact batch amounts, both liquid and
    solid preparation scope, separate ethanol/acetic-acid handling and a plate-specific
    humidity condition. No sterilization cycle or named organism is supplied.
  snapshot_sha256: 4772d2aaff26d0b03affe536b7da737b7c697e30ac494a83d138edbb29f79c64
- evidence_id: mediadive849api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/849
  locator: $.data.medium; $.data.solutions[0]
  accessed_at: '2026-10-21T11:30:38.449706Z'
  support: supports
  summary: Provider solution 1737 has seven recipe rows, declares 1000 ml and supplies
    four g_l values; all liquid additions remain ml. Listed liquids sum to 1000 ml,
    without independently measured final-volume evidence.
  snapshot_sha256: 9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8
- evidence_id: komodoMediaList
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Actual table header and exact first-cell 849 mapping row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The exact public table supports the KOMODO 849 to DSMZ 849 accession mapping.
    Aerobic metadata is catalog provenance, not a demonstrated phenotype or instruction
    for this medium.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo849detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=849
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T11:30:38.449464Z'
  support: context_only
  summary: The exact KOMODO MediaInfo=849 public request returned HTTP 403. Required
    verification of this contributor-specific detail remains unavailable. Accessible
    DSMZ 849 and current MediaDive evidence establish their own formulation, not the
    inaccessible historical KOMODO detail.
  snapshot_sha256: 8c2173c57afd3370dc24dcfc23f06dfb9fe1082f2ccd0d0ef622688818388b27
- evidence_id: supply-foodon
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: Exact term description/SIREN annotation
  accessed_at: '2026-10-21T08:00:49.388263Z'
  support: supports
  summary: Owner-only FOODON:03315426 resolves to yeast extract, with a SIREN annotation
    for not heat-treated material. The unqualified source yeast-extract row does not
    establish this supplier processing state.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: supply-micro
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178
  locator: Exact annotation.definition and definition source
  accessed_at: '2026-10-21T08:00:49.423450Z'
  support: supports
  summary: Owner-only MICRO:0000178 resolves to peptone but its definition specifies
    an enzymatic digest of mammalian animal protein; the exact source only says peptone.
    The accompanying Bacto product source is not evidence that DSMZ 849 uses that
    product.
  snapshot_sha256: ef45aa186438f91d015280171fde8ccb25740a50cc6f2c6e848de6aad3339b31
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/189/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:53:03Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 9ad74e2a9a64ed2d32618d3496ec2216b785f089dddbb12e61c3a7d237ad43a0
- evidence_id: chebi15366
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15366
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-21T11:29:08.353669Z'
  support: supports
  summary: 'CHEBI:15366: acetic acid. Source-specific forms are assessed separately;
    valid ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: b887e3ee7d15164ff6fa8efd11f052ea16965afb730d69ccf31744ffb64d2139
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: 'CHEBI:15377: water. Source-specific forms are assessed separately; valid
    ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi16236
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16236
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-21T10:07:16.961534Z'
  support: supports
  summary: 'CHEBI:16236: ethanol. Source-specific forms are assessed separately; valid
    ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: afdacc5e401c6545f51974e897eb96eee2a5fa3aef15119edbd415cb7bb802b8
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: 'CHEBI:17234: glucose. Source-specific forms are assessed separately; valid
    ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: 'CHEBI:2509: agar. Source-specific forms are assessed separately; valid
    ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: foodon03315426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-21T08:00:49.388263Z'
  support: supports
  summary: 'FOODON:03315426: yeast extract. Source-specific forms are assessed separately;
    valid ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: micro0000178
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178
  locator: Exact OLS identifier, canonical label, nonobsolete status, definitions
    and chemical annotations
  accessed_at: '2026-10-21T08:00:49.423450Z'
  support: supports
  summary: 'MICRO:0000178: peptone. Source-specific forms are assessed separately;
    valid ontology metadata is not proof of supplied-form correspondence.'
  snapshot_sha256: ef45aa186438f91d015280171fde8ccb25740a50cc6f2c6e848de6aad3339b31
- evidence_id: chemical-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/189/chemical-grounding-context.json
  locator: Every primary and current CHEBI-based secondary ingredient term in the
    target and maintained owners
  accessed_at: '2026-10-21T11:53:03Z'
  support: context_only
  summary: Full OLS annotations, local instance locators, label differences, pinned
    exact-key MIM rows and layer-specific linkage metrics.
  snapshot_sha256: b80a5189d83f6647e79b1f65e94de6551542aedf969d2160542cc7f854914e2e
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact identifier rows and pinned metadata source commit; no fuzzy replacements
  accessed_at: '2026-10-21T11:53:03Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "current_secondary_rows":
    {"CHEBI:15366": [{"label": "Acetic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:15366", "preferred_term": "Acetic acid", "ontology_id": "CHEBI:15366",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label":
    "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:16236": [{"label": "Ethanol", "match_type":
    "preferred_term", "identifier": "CHEBI:16236", "preferred_term": "Ethanol", "ontology_id":
    "CHEBI:16236", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234":
    [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AE_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml;
    data/normalized_yaml/bacterial/ae_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:53:03Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:03.159005"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:03.159005"}]}, {"input": "data/normalized_yaml/bacterial/ae_medium.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_dsmz_849_ae_score15.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:53:03Z'
  support: context_only
  summary: The exact repair helper explicitly replaces the old six-row signature with
    seven rows, changes ethanol/acetic acid to ML_PER_L, adds water and preparation,
    and assigns the owner-only FOODON/MICRO IDs. It adds references but no ingredient
    evidence. Its existing-event branch rewrites a matching history event; follow-up
    must instead preserve append-only history. Current merge compares formulation
    scope; no generator was executed or historical replay inferred.
  snapshot_sha256: dad411e6835547a6fe0f168d5c6036b0592dc508466617cbecd3fd7662c08633
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:53:03Z'
  support: context_only
  summary: The exact repair helper explicitly replaces the old six-row signature with
    seven rows, changes ethanol/acetic acid to ML_PER_L, adds water and preparation,
    and assigns the owner-only FOODON/MICRO IDs. It adds references but no ingredient
    evidence. Its existing-event branch rewrites a matching history event; follow-up
    must instead preserve append-only history. Current merge compares formulation
    scope; no generator was executed or historical replay inferred.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact accession, contributors and duplicate links
  outcome: supported
  summary: CultureMech:006656 is the generated KOMODO 849 record merged with the DSMZ
    849 owner CultureMech:002006. The explicit source-duplicate paths and IDs resolve
    exactly, and both current owner ingredient arrays agree. Their source mapping
    is supported; a fingerprint alone is not the identity evidence. Exact KOMODO detail
    remains an unavailable source check.
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - id-search
  - dsmz849
  - mediadive849api
  - komodoMediaList
  - komodo849detail-attempt
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 9 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence. All 20 ingredient and stock-dose concentration instances across
    the target and maintained owners are explicitly covered; additional rows retain
    preparation quantities and source-only components.
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"ingredient_or_context\": \"\
    Glucose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/AE_MEDIUM.yaml\",\n      \
    \  \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5.0\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"5 g in the DSMZ-listed batch; preserve exact source grade and the explicitly\
    \ identified 1000 ml provider normalization basis.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive849api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/849\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\":\
    \ 5,\\n                        \\\"amount\\\": 5,\\n                        \\\
    \"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n          \
    \              \\\"mmol_l\\\": 27.7531,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8\"\
    \n      }\n    ],\n    \"rationale\": \"Both current owners retain the source\
    \ number and correct dimensional unit but have source/notes/reference annotations\
    \ rather than attached exact concentration evidence. The scalar agrees with the\
    \ provider g_l value; retain that nominal denominator separately from the primary\
    \ batch table.\"\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"ingredient_or_context\"\
    : \"Yeast extract\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AE_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"3.0\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"3 g in the DSMZ-listed batch; preserve exact source grade and the explicitly\
    \ identified 1000 ml provider normalization basis.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive849api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/849\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8\"\
    \n      }\n    ],\n    \"rationale\": \"Both current owners retain the source\
    \ number and correct dimensional unit but have source/notes/reference annotations\
    \ rather than attached exact concentration evidence. The scalar agrees with the\
    \ provider g_l value; retain that nominal denominator separately from the primary\
    \ batch table.\"\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"ingredient_or_context\"\
    : \"Peptone\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AE_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"4.0\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"4 g in the DSMZ-listed batch; preserve exact source grade and the explicitly\
    \ identified 1000 ml provider normalization basis.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive849api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/849\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Peptone\\\",\\n                        \\\"compound_id\\\":\
    \ 1,\\n                        \\\"amount\\\": 4,\\n                        \\\
    \"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 4,\\n          \
    \              \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8\"\n     \
    \ }\n    ],\n    \"rationale\": \"Both current owners retain the source number\
    \ and correct dimensional unit but have source/notes/reference annotations rather\
    \ than attached exact concentration evidence. The scalar agrees with the provider\
    \ g_l value; retain that nominal denominator separately from the primary batch\
    \ table.\"\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"ingredient_or_context\"\
    : \"Absolute ethanol\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AE_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/ae_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"30.0\",\n          \"unit\": \"ML_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_scope\": \"30 ml in\
    \ the DSMZ-listed batch; preserve exact source grade and the explicitly identified\
    \ 1000 ml provider normalization basis.\",\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive849api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/849\",\n        \"source_locator\": \"$.data.solutions[0].recipe[3]\"\
    ,\n        \"exact_source_quote\": \"{\\n                        \\\"recipe_order\\\
    \": 4,\\n                        \\\"compound\\\": \\\"Absolute ethanol\\\",\\\
    n                        \\\"compound_id\\\": 788,\\n                        \\\
    \"amount\\\": 30,\\n                        \\\"unit\\\": \\\"ml\\\",\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8\"\
    \n      }\n    ],\n    \"rationale\": \"Both current owners retain the source\
    \ number and correct dimensional unit but have source/notes/reference annotations\
    \ rather than attached exact concentration evidence. The generated G_PER_L field\
    \ is wrong for the source ml dose. Do not convert volume to mass using an assumed\
    \ density.\"\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"ingredient_or_context\"\
    : \"Glacial acetic acid\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AE_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/ae_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"30.0\",\n          \"unit\": \"ML_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_scope\": \"30 ml in\
    \ the DSMZ-listed batch; preserve exact source grade and the explicitly identified\
    \ 1000 ml provider normalization basis.\",\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive849api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/849\",\n        \"source_locator\": \"$.data.solutions[0].recipe[4]\"\
    ,\n        \"exact_source_quote\": \"{\\n                        \\\"recipe_order\\\
    \": 5,\\n                        \\\"compound\\\": \\\"Glacial acetic acid\\\"\
    ,\\n                        \\\"compound_id\\\": 787,\\n                     \
    \   \\\"amount\\\": 30,\\n                        \\\"unit\\\": \\\"ml\\\",\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8\"\
    \n      }\n    ],\n    \"rationale\": \"Both current owners retain the source\
    \ number and correct dimensional unit but have source/notes/reference annotations\
    \ rather than attached exact concentration evidence. The generated G_PER_L field\
    \ is wrong for the source ml dose. Do not convert volume to mass using an assumed\
    \ density.\"\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"ingredient_or_context\"\
    : \"Agar\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/AE_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"9\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"9.0\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"9.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_scope\"\
    : \"9 g in the DSMZ-listed batch; preserve exact source grade and the explicitly\
    \ identified 1000 ml provider normalization basis.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive849api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/849\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\": 3,\\\
    n                        \\\"amount\\\": 9,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 9,\\n                  \
    \      \\\"mmol_l\\\": 26.7594,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8\"\
    \n      }\n    ],\n    \"rationale\": \"Both current owners retain the source\
    \ number and correct dimensional unit but have source/notes/reference annotations\
    \ rather than attached exact concentration evidence. The scalar agrees with the\
    \ provider g_l value; retain that nominal denominator separately from the primary\
    \ batch table. This amount belongs to the agar-bearing solid preparation. The\
    \ source also names liquid media; it does not quantify a separate liquid-branch\
    \ agar row, and no zero or universal agar dose is invented.\"\n  },\n  {\n   \
    \ \"quantity_id\": \"q7\",\n    \"ingredient_or_context\": \"Distilled water\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AE_MEDIUM.yaml\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"940.0\",\n          \"unit\": \"ML_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/ae_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"940.0\",\n          \"unit\": \"ML_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_scope\": \"940 ml\
    \ in the DSMZ-listed batch; preserve exact source grade and the explicitly identified\
    \ 1000 ml provider normalization basis.\",\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive849api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/849\",\n        \"source_locator\": \"$.data.solutions[0].recipe[6]\"\
    ,\n        \"exact_source_quote\": \"{\\n                        \\\"recipe_order\\\
    \": 7,\\n                        \\\"compound\\\": \\\"Distilled water\\\",\\\
    n                        \\\"compound_id\\\": 4,\\n                        \\\"\
    amount\\\": 940,\\n                        \\\"unit\\\": \\\"ml\\\",\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8\"\
    \n      }\n    ],\n    \"rationale\": \"Both current owners retain the source\
    \ number and correct dimensional unit but have source/notes/reference annotations\
    \ rather than attached exact concentration evidence. Water is absent from the\
    \ generated target and present in both owners as 940 ML_PER_L. Preserve the listed\
    \ water volume rather than an inferred water mass.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q8\",\n    \"ingredient_or_context\": \"Provider-declared volume\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/AE_MEDIUM.yaml\",\n        \"field_path\": \"notes\",\n\
    \        \"stored\": \"Source: KOMODO ModelSEED | ID: 849 | DSMZ Medium: 849 (mediadive.medium:849)\
    \ | Aerobic: No\",\n        \"decision\": \"add\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml\",\n \
    \       \"field_path\": \"notes\",\n        \"stored\": \"Source: KOMODO ModelSEED\
    \ | ID: 849 | DSMZ Medium: 849 (mediadive.medium:849) | Aerobic: No\",\n     \
    \   \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ae_medium.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: DSMZ | Link:\
    \ https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium849.pdf\",\n      \
    \  \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_scope\": \"Retain\
    \ 1000 ml as the provider-declared batch basis; list 940 ml water plus two 30\
    \ ml liquids separately.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive849api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/849\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8\"\
    \n      }\n    ],\n    \"rationale\": \"940+30+30=1000 ml listed liquid inputs;\
    \ the source does not report measured final volume after dissolution and mixing.\"\
    \n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"ingredient_or_context\": \"Plate-specific\
    \ humidity threshold\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AE_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n     \
    \   \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[3].description\",\n        \"stored\"\
    : \"Incubate plates in sealed containers to keep humidity high above 90%.\",\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/ae_medium.yaml\",\n        \"field_path\":\
    \ \"preparation_steps[3].description\",\n        \"stored\": \"Incubate plates\
    \ in sealed containers to keep humidity high above 90%.\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_scope\": \"Preserve\
    \ the source >90% humidity qualifier only for plates in sealed containers.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive849api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/849\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n        \"\
    exact_source_quote\": \"humidity high (> 90%).\",\n        \"snapshot_sha256\"\
    : \"9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8\"\n     \
    \ }\n    ],\n    \"rationale\": \"Both owners already preserve above 90% in prose;\
    \ the generated record omits the preparation. This is a plate-specific humidity\
    \ context, not a solution concentration or inferred organism growth optimum.\"\
    \n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Source-specific forms and current CHEBI-based secondary correspondence
  outcome: concern
  summary: '7 distinct asserted chemical IDs resolve as nonobsolete. 0 local label
    instances differ from canonical labels. 5 of 5 distinct current CHEBI-based secondary
    keys have exact mapped preferred-term rows in the pinned index; unresolved keys:
    []. This does not validate historical legacy MIM IDs, supplied hydrates, stereochemistry
    or catalog products. Target primary/secondary linkage covers glucose and agar
    only. Both later owners add ethanol, acetic acid, water, FOODON yeast extract
    and MICRO peptone. The two non-CHEBI supply identities need source-specific qualification
    despite matching canonical labels; neither annotation validates concentration.'
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - record
  - chemical-context
  - mim
  - owner-0
  - owner-1
  - chebi15366
  - chebi15377
  - chebi16236
  - chebi17234
  - chebi2509
  - foodon03315426
  - micro0000178
  details: '{"metrics": [{"input": "data/merge_yaml/merged/AE_MEDIUM.yaml", "ingredient_instances":
    6, "primary": 2, "current_secondary": 2, "primary_percent": 33.333333333333336,
    "current_secondary_percent": 33.333333333333336}, {"input": "data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml",
    "ingredient_instances": 7, "primary": 7, "current_secondary": 5, "primary_percent":
    100.0, "current_secondary_percent": 71.42857142857143}, {"input": "data/normalized_yaml/bacterial/ae_medium.yaml",
    "ingredient_instances": 7, "primary": 7, "current_secondary": 5, "primary_percent":
    100.0, "current_secondary_percent": 71.42857142857143}], "definition": "Ingredient-instance
    linkage percentages on a 0–100 scale, using each stated layer denominator; these
    are not scientific correctness scores.", "label_drift": []}'
- assessment_id: preparation
  area: completeness
  topic: Source-scoped preparation, conditions and physical-state branches
  outcome: concern
  summary: 'The generated record omits all preparation. Both owners preserve separate
    ethanol/acetic-acid treatment, the source filtration-or-closed-bottle-autoclaving
    alternatives, and plate humidity. Preserve the alternatives in structured method
    scope: the owner FILTER_STERILIZE action tag must not erase its own autoclave
    option, and the MIX-tagged plate incubation text is not a mixing instruction.
    No temperature/time is printed, so no cycle is inferred.'
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz849
  - mediadive849api
  - supply-foodon
  - supply-micro
- assessment_id: classification
  area: scope
  topic: Medium classification, applications and organism claim scope
  outcome: supported
  summary: COMPLEX/UNDEFINED is appropriate for yeast extract and peptone. SOLID_AGAR
    matches the table containing agar but represents only the solid preparation; the
    source also names liquid media. No universal agar requirement, organism identity,
    aerobic phenotype or optimal growth follows from the name or KOMODO flag.
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz849
  - mediadive849api
  - supply-foodon
  - supply-micro
- assessment_id: forms
  area: grounding
  topic: Exact supplied chemical forms and mixture identity
  outcome: concern
  summary: Source ethanol is absolute and acid is glacial; preserve these grade names.
    Generic yeast extract does not establish the FOODON not-heat-treated annotation,
    and generic peptone does not establish MICRO mammalian enzymatic supply identity.
    This is unverified narrowing, not a claim that the identifiers do not exist.
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - record
  - chemical-context
  - owner-0
  - owner-1
  - dsmz849
  - mediadive849api
  - supply-foodon
  - supply-micro
- assessment_id: evidence-placement
  area: evidence
  topic: Claim-level formulation evidence and current annotations
  outcome: concern
  summary: The later source-specific repair adds owner notes, source fields, a primary
    reference and ingredient-curated flags, but no exact ingredient evidence. Target
    lacks those repair fields. Attach narrow source snippets and explain provider
    normalization; a flag or root reference alone cannot make a quantity verified.
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - record
  - quantity-inventory
  - owner-0
  - owner-1
  - dsmz849
  - mediadive849api
  - supply-foodon
  - supply-micro
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 21 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: ownership
  area: ownership
  topic: Later maintained repair versus stale generated target
  outcome: concern
  summary: The target merge events are dated August 6; both owners contain the September
    11 source-specific repair. Regenerate only after source scope, amount evidence
    and supply identities are settled in both owners and their named repair helper.
    Do not repeat already repaired owner liquid-unit errors as though they remain
    there.
  target_ids:
  - CultureMech:006656
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - writer-0
  - writer-1
findings:
- finding_id: f1
  issue_key: cm006656-stale-liquid-units-water
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: The generated recipe retains mass units for liquid doses and omits water
  description: Target ingredients[3] and [4] give 30 G_PER_L, whereas DSMZ 849 lists
    30 ml of each liquid. Target lacks the 940 ml water row. Both maintained owners
    already contain the corrected volume units and water, so this is also an exact
    generated-freshness discrepancy.
  target_ids:
  - CultureMech:006656
  field_paths:
  - ingredients[3].concentration
  - ingredients[4].concentration
  - ingredients
  - merge_fingerprint
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - quantity-inventory
  - dsmz849
  - mediadive849api
  - writer-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ae_medium.yaml
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
  issue_key: cm006656-owner-supply-specificity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Later owner identifiers narrow unspecified ingredient supply identities
  description: Only the maintained owners assign MICRO:0000178 to unqualified peptone
    and FOODON:03315426 to yeast extract. The former specifies mammalian enzymatic
    digest and the latter carries a not-heat-treated SIREN annotation; the DSMZ source
    does not specify either supply restriction. The target itself does not assert
    these two terms.
  target_ids:
  - CultureMech:006656
  field_paths:
  - ingredients[1]
  - ingredients[2]
  evidence_ids:
  - owner-0
  - owner-1
  - supply-micro
  - supply-foodon
  - chemical-context
  - dsmz849
  - writer-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ae_medium.yaml
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
  issue_key: cm006656-preparation-branch-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated preparation and narrow formulation evidence remain incomplete
  description: The target loses the later owner preparation entirely. Owner prose
    retains the important separate liquid handling and humidity context, but typed
    action tags must preserve alternatives and incubation scope. Neither layer has
    narrow formulation evidence, and the solid recipe should be distinguished from
    the source-mentioned liquid preparation.
  target_ids:
  - CultureMech:006656
  field_paths:
  - preparation_steps
  - sterilization
  - physical_state
  - references
  - ingredients[*].evidence
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - quantity-inventory
  - dsmz849
  - mediadive849api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ae_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: cm006656-history-timestamp-context
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Inherited timestamps do not provide a parseable chronology
  description: The target and KOMODO owner each retain an import timestamp with literal
    .fZ and a timezone-naive resolver timestamp. Other history, including the later
    repair, remains separate. Passing deterministic checks do not turn these strings
    into reliable dated events.
  target_ids:
  - CultureMech:006656
  field_paths:
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ae_medium.yaml
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
  description: Preserve the existing owner repair, qualify its provider batch basis
    and attach exact evidence. After completing the bounded owner work, regenerate
    the target so corrected liquid units and the source water row survive; do not
    patch the generated file.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006656
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ae_medium.yaml
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
  description: In both normalized owners and the named repair helper, qualify or remove
    unsupported supply-specific narrowing unless exact product evidence is obtained.
    Preserve the mixture names and source amounts; do not invent a replacement ontology
    ID or transplant Bacto product composition.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006656
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ae_medium.yaml
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
  description: Attach exact evidence to each quantity and scoped preparation claim
    in both owners, retain source alternatives and plate-only context, and document
    the represented physical-state branch. Regenerate only afterward. Do not invent
    cycle parameters or a complete liquid variant.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006656
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ae_medium.yaml
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
  description: Preserve the historical entries and append a bounded clarification
    when curation is authorized. Do not invent the missing fractional seconds or timezone,
    or rewrite earlier events through the repair helper.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006656
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ae_medium.yaml
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
- The exact KOMODO MediaInfo=849 public request returned HTTP 403. Required verification
  of this contributor-specific detail remains unavailable. Accessible DSMZ 849 and
  current MediaDive evidence establish their own formulation, not the inaccessible
  historical KOMODO detail.
- Partial source coverage rests on the unavailable exact KOMODO detail, not on the
  available DSMZ primary. Current public mapping and the primary do not authenticate
  a historical resolver fetch.
- The source table and provider normalization are kept separate from measured final
  volume. No growth or taxonomy assertion is added from the source phrase this organism
  or the catalog aerobic flag.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-019
- generated-medium
```
