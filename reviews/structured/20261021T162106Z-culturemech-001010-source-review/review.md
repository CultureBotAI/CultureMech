# Source and formulation review: antibiotic_medium_1 (CultureMech:001010)

- Review: 20261021T162106Z-culturemech-001010-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T16:17:55Z
- Finished UTC: 2026-10-21T16:21:06Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSMZ 1532 primary supports the six named batch masses and pH 6.55, but prints no water or volume denominator. The maintained owner has six later amount-evidence objects whose excerpts and historical hash/time match local derivative reports; the full cited API response was not recovered and current requests return HTTP 503. The generated target omits those later evidence and grounding additions. Retain the unresolved per-liter basis, reconcile scalar pH 6.5 with retained preparation pH 6.55, and qualify source-specific complex-ingredient grounding. This review is partial for the unavailable provider/formulation basis.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 289; batch 029 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-eight task batches contain 280 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 283 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001010 | data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml | generated | antibiotic_medium_1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001010 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001010 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch029/289/strict.tsv |
| validate-terms | passed | True | CultureMech:001010 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001010 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001010 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive1532api | unavailable | True | CultureMech:001010 | Exact MediaDive 1532 returned HTTP 503 in the initial attempt and separately preserved retry. The cited original f1376f… response is not recovered; derivative local excerpts retain historical claims but cannot authenticate the full provider volume basis. Required formulation-provenance verification remains incomplete. |
| Exact source content access: mediadive1532retry | unavailable | True | CultureMech:001010 | Exact MediaDive 1532 returned HTTP 503 in the initial attempt and separately preserved retry. The cited original f1376f… response is not recovered; derivative local excerpts retain historical claims but cannot authenticate the full provider volume basis. Required formulation-provenance verification remains incomplete. |
| Exact source content access: bd226340 | unavailable | False | CultureMech:001010 | The exact BD 226340 supplier page returned 403. The collection explicitly names the alternative product, but no independent supplier formulation or reconstitution dose is inferred. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001010.

The four documented recipes completed; interpret the scope of each separately.

### Every asserted ontology identifier and current secondary key

grounding: concern. Targets: CultureMech:001010.

Six distinct asserted primary IDs are nonobsolete. Four owner labels differ only by capitalization from exact FOODON/MICRO labels; target has only the glucose and agar primary IDs. Both asserted secondary CHEBI keys have exact mapped preferred rows in the pinned MIM index. Target linkage is 2/6 primary and 2/6 secondary (33.33% each); owner linkage is 6/6 primary (100%) and 2/6 secondary (33.33%), on a 0–100 linkage scale, not correctness scores. No legacy MIM field is asserted.

[
  {
    "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
    "field_path": "ingredients[1].term",
    "label": "Beef extract",
    "id": "FOODON:03302088",
    "canonical_label": "beef extract"
  },
  {
    "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
    "field_path": "ingredients[0].term",
    "label": "Yeast extract",
    "id": "FOODON:03315426",
    "canonical_label": "yeast extract"
  },
  {
    "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
    "field_path": "ingredients[3].term",
    "label": "Peptone",
    "id": "MICRO:0000178",
    "canonical_label": "peptone"
  },
  {
    "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
    "field_path": "ingredients[2].term",
    "label": "Tryptone",
    "id": "MICRO:0000182",
    "canonical_label": "tryptone"
  }
]

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001010.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact medium and supplier identity

identity: supported. Targets: CultureMech:001010.

The exact primary title, DSMZ 1532 and local stable identity agree. The sole maintained owner is resolved from the complete merge event. The source names BD 226340 as an alternative, without establishing every commercial formulation detail. No DOI/PMID, taxon, strain, parent/child medium or standalone stock reference is asserted.

### Complex agar formulation and source scope

scope: supported. Targets: CultureMech:001010.

Complex/undefined classification is supported by yeast/beef extracts and digests; solid-agar is supported by the mandatory agar row. G_PER_L is not intrinsically invalid for a recipe that gels: its unresolved denominator is the actual issue. Generic microbial-cultivation text is not evidence for a particular organism or experimental growth outcome.

### Complex ingredient specificity and exact label spelling

grounding: concern. Targets: CultureMech:001010.

The source pancreatic digest of casein agrees with MICRO tryptone wording. Generic peptone does not itself establish the mammalian enzymatic origin in MICRO:0000178. FOODON:03315426 adds a not-heat-treated qualification and FOODON:03302088 adds fully-heat-treated context not established by the source labels. These are specificity limits, not proof the materials have the opposite properties. Preserve valid glucose/agar identity and do not guess replacement terms.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001010.

17 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "label": "Yeast extract — target",
    "decision": "unsupported",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "attached_evidence": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Ingredient table row1, complete primary has no volume denominator",
        "exact_source_quote": "Yeast extract 3.0 g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The printed batch mass matches the local numeral. Its G_PER_L denominator cannot be independently verified from the primary; retain the historical provider claim without calling the value disproven. No amount evidence is attached in this generated layer."
  },
  {
    "decision_id": "q2",
    "label": "Yeast extract — owner",
    "decision": "unsupported",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "attached_evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1532",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[0].concentration (Yeast extract) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec."
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Ingredient table row1, complete primary has no volume denominator",
        "exact_source_quote": "Yeast extract 3.0 g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The printed batch mass matches the local numeral. Its G_PER_L denominator cannot be independently verified from the primary; retain the historical provider claim without calling the value disproven. Six owner excerpts match the dated local plan/report, but full cited raw 1532 bytes are unavailable. Do not mark verified from derivative equality alone."
  },
  {
    "decision_id": "q3",
    "label": "Beef extract — target",
    "decision": "unsupported",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "attached_evidence": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Ingredient table row2, complete primary has no volume denominator",
        "exact_source_quote": "Beef extract 1.5 g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The printed batch mass matches the local numeral. Its G_PER_L denominator cannot be independently verified from the primary; retain the historical provider claim without calling the value disproven. No amount evidence is attached in this generated layer."
  },
  {
    "decision_id": "q4",
    "label": "Beef extract — owner",
    "decision": "unsupported",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "attached_evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1532",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Beef extract\",\n                        \"compound_id\": 85,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[1].concentration (Beef extract) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec."
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Ingredient table row2, complete primary has no volume denominator",
        "exact_source_quote": "Beef extract 1.5 g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The printed batch mass matches the local numeral. Its G_PER_L denominator cannot be independently verified from the primary; retain the historical provider claim without calling the value disproven. Six owner excerpts match the dated local plan/report, but full cited raw 1532 bytes are unavailable. Do not mark verified from derivative equality alone."
  },
  {
    "decision_id": "q5",
    "label": "Pancreatic digest of casein — target",
    "decision": "unsupported",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        },
        "attached_evidence": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Ingredient table row3, complete primary has no volume denominator",
        "exact_source_quote": "Pancreatic Digest of Casein 4.0 g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The printed batch mass matches the local numeral. Its G_PER_L denominator cannot be independently verified from the primary; retain the historical provider claim without calling the value disproven. No amount evidence is attached in this generated layer."
  },
  {
    "decision_id": "q6",
    "label": "Pancreatic digest of casein — owner",
    "decision": "unsupported",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        },
        "attached_evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1532",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pancreatic digest of casein\",\n                        \"compound_id\": 531,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[2].concentration (Pancreatic digest of casein) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=4; check: 4 g * 1 g/g / (1000 ml / 1000 ml per L) = 4 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec."
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Ingredient table row3, complete primary has no volume denominator",
        "exact_source_quote": "Pancreatic Digest of Casein 4.0 g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The printed batch mass matches the local numeral. Its G_PER_L denominator cannot be independently verified from the primary; retain the historical provider claim without calling the value disproven. Six owner excerpts match the dated local plan/report, but full cited raw 1532 bytes are unavailable. Do not mark verified from derivative equality alone."
  },
  {
    "decision_id": "q7",
    "label": "Peptone — target",
    "decision": "unsupported",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "attached_evidence": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Ingredient table row4, complete primary has no volume denominator",
        "exact_source_quote": "Peptone 6.0 g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The printed batch mass matches the local numeral. Its G_PER_L denominator cannot be independently verified from the primary; retain the historical provider claim without calling the value disproven. No amount evidence is attached in this generated layer."
  },
  {
    "decision_id": "q8",
    "label": "Peptone — owner",
    "decision": "unsupported",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "attached_evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1532",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\": 1,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[3].concentration (Peptone) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=6; check: 6 g * 1 g/g / (1000 ml / 1000 ml per L) = 6 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec."
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Ingredient table row4, complete primary has no volume denominator",
        "exact_source_quote": "Peptone 6.0 g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The printed batch mass matches the local numeral. Its G_PER_L denominator cannot be independently verified from the primary; retain the historical provider claim without calling the value disproven. Six owner excerpts match the dated local plan/report, but full cited raw 1532 bytes are unavailable. Do not mark verified from derivative equality alone."
  },
  {
    "decision_id": "q9",
    "label": "Glucose — target",
    "decision": "unsupported",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "attached_evidence": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Ingredient table row5, complete primary has no volume denominator",
        "exact_source_quote": "Glucose 1.0  g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The printed batch mass matches the local numeral. Its G_PER_L denominator cannot be independently verified from the primary; retain the historical provider claim without calling the value disproven. No amount evidence is attached in this generated layer."
  },
  {
    "decision_id": "q10",
    "label": "Glucose — owner",
    "decision": "unsupported",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "attached_evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1532",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[4].concentration (Glucose) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=1; check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec."
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Ingredient table row5, complete primary has no volume denominator",
        "exact_source_quote": "Glucose 1.0  g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The printed batch mass matches the local numeral. Its G_PER_L denominator cannot be independently verified from the primary; retain the historical provider claim without calling the value disproven. Six owner excerpts match the dated local plan/report, but full cited raw 1532 bytes are unavailable. Do not mark verified from derivative equality alone."
  },
  {
    "decision_id": "q11",
    "label": "Agar — target",
    "decision": "unsupported",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "attached_evidence": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Ingredient table row6, complete primary has no volume denominator",
        "exact_source_quote": "Agar 20.0 g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The printed batch mass matches the local numeral. Its G_PER_L denominator cannot be independently verified from the primary; retain the historical provider claim without calling the value disproven. No amount evidence is attached in this generated layer."
  },
  {
    "decision_id": "q12",
    "label": "Agar — owner",
    "decision": "unsupported",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "attached_evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1532",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 59.4654,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[5].concentration (Agar) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=20; check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) = 20 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec."
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Ingredient table row6, complete primary has no volume denominator",
        "exact_source_quote": "Agar 20.0 g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The printed batch mass matches the local numeral. Its G_PER_L denominator cannot be independently verified from the primary; retain the historical provider claim without calling the value disproven. Six owner excerpts match the dated local plan/report, but full cited raw 1532 bytes are unavailable. Do not mark verified from derivative equality alone."
  },
  {
    "decision_id": "q13",
    "label": "Scalar pH",
    "decision": "correct",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml",
        "field_path": "ph_value",
        "stored": 6.5
      },
      {
        "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
        "field_path": "ph_value",
        "stored": 6.5
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Primary pH line",
        "exact_source_quote": "pH 6.55",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The source explicitly gives 6.55; scalar 6.5 loses precision and disagrees with the already retained preparation text. Do not claim pH is wholly missing."
  },
  {
    "decision_id": "q14",
    "label": "Retained preparation pH",
    "decision": "evidence_only",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "pH 6.55"
      },
      {
        "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "pH 6.55"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Primary pH line",
        "exact_source_quote": "pH 6.55",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The preparation sentence already contains the exact pH 6.55. Attach narrow evidence and reconcile scalar precision."
  },
  {
    "decision_id": "q15",
    "label": "Supplier alternative",
    "decision": "evidence_only",
    "source_stage": "Main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "or Difco Antibiotic Medium 1 (BD, order number 226340)"
      },
      {
        "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "or Difco Antibiotic Medium 1 (BD, order number 226340)"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Primary final sentence",
        "exact_source_quote": "or Difco Antibiotic Medium 1 (BD, order number 226340)",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "226340 is a product identifier, not a dose. This retained alternative is supported; commercial formula and reconstitution dose are not independently established."
  },
  {
    "decision_id": "q16",
    "label": "Historical water-only lead",
    "decision": "unsupported",
    "source_stage": "Historical provider-only context",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Beef extract",
            "concentration": {
              "value": "1.5",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Pancreatic digest of casein",
            "concentration": {
              "value": "4",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Peptone",
            "concentration": {
              "value": "6",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Glucose",
            "term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ],
        "missing_item": "Distilled water"
      },
      {
        "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "term": {
              "id": "FOODON:03315426",
              "label": "Yeast extract"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1532",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[0].concentration (Yeast extract) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec."
              }
            ]
          },
          {
            "preferred_term": "Beef extract",
            "concentration": {
              "value": "1.5",
              "unit": "G_PER_L"
            },
            "term": {
              "id": "FOODON:03302088",
              "label": "Beef extract"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1532",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Beef extract\",\n                        \"compound_id\": 85,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[1].concentration (Beef extract) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec."
              }
            ]
          },
          {
            "preferred_term": "Pancreatic digest of casein",
            "concentration": {
              "value": "4",
              "unit": "G_PER_L"
            },
            "term": {
              "id": "MICRO:0000182",
              "label": "Tryptone"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1532",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pancreatic digest of casein\",\n                        \"compound_id\": 531,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[2].concentration (Pancreatic digest of casein) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=4; check: 4 g * 1 g/g / (1000 ml / 1000 ml per L) = 4 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec."
              }
            ]
          },
          {
            "preferred_term": "Peptone",
            "concentration": {
              "value": "6",
              "unit": "G_PER_L"
            },
            "term": {
              "id": "MICRO:0000178",
              "label": "Peptone"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1532",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\": 1,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[3].concentration (Peptone) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=6; check: 6 g * 1 g/g / (1000 ml / 1000 ml per L) = 6 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec."
              }
            ]
          },
          {
            "preferred_term": "Glucose",
            "term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1532",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[4].concentration (Glucose) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=1; check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec."
              }
            ]
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1532",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 59.4654,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[5].concentration (Agar) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=20; check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) = 20 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec."
              }
            ]
          }
        ],
        "missing_item": "Distilled water"
      }
    ],
    "source_snippets": [
      {
        "source_key": "historical-plan",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1532",
        "source_locator": "Historical plan $.records[134].claims[6]; alleged original $.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26",
        "quotation_kind": "Exact decoded snippet in pinned local derivative plan; original remote response hash is not available for verification"
      }
    ],
    "interpretation": "The local historical plan quotes 1000 ml water and reports a provider 1000 ml volume. No full original response was recovered, and current primary has neither. Preserve as a historical follow-up lead, not an authenticated new solvent amount or measured final volume."
  },
  {
    "decision_id": "q17",
    "label": "Final volume and sterilization quantities",
    "decision": "not_quantified",
    "source_stage": "Unspecified source preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "pH 6.55"
          },
          {
            "step_number": 2,
            "action": "MIX",
            "description": "or Difco Antibiotic Medium 1 (BD, order number 226340)"
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "pH 6.55"
          },
          {
            "step_number": 2,
            "action": "MIX",
            "description": "or Difco Antibiotic Medium 1 (BD, order number 226340)"
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Last primary ingredient row",
        "exact_source_quote": "Agar 20.0 g",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      },
      {
        "source_key": "dsmz1532",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf",
        "source_locator": "Primary pH line",
        "exact_source_quote": "pH 6.55",
        "snapshot_sha256": "bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8",
        "parsed_text_sha256": "1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920"
      }
    ],
    "interpretation": "The entire inspected primary provides no final-volume statement, sterilization time/temperature or adjustment reagent dose. Do not add typical values; the six G_PER_L claims remain explicitly unresolved."
  }
]

### One maintained owner and bounded follow-up

ownership: supported. Targets: CultureMech:001010.

The normalized antibiotic_medium_1.yaml owns corrections; generated target and pages are not edit surfaces. Current code was inspected without execution. Existing history is preserved and no record-level scientific status is promoted.

## Findings

### f1: Per-liter basis is unresolved despite matching batch masses

major / open / confirmed; issue key: cm001010-basis-unverified.

All six local G_PER_L numerals match printed primary gram amounts, but the primary has no solvent or volume denominator. The owner has appropriately scoped historical provider attachments; current 503 responses and absence of full recovered raw bytes prevent independent confirmation of their 1000 ml basis. This is an evidential limitation, not proof the six numbers are wrong.

### f2: Some owner complex-material terms assert unsupported specificity

major / open / confirmed; issue key: cm001010-complex-form-specificity.

The source names yeast extract, beef extract and peptone but does not establish their FOODON heat-treatment qualifiers or MICRO mammalian enzymatic origin. The exact pancreatic casein digest is separately supported as tryptone. Valid identifier existence does not settle these narrower material claims.

### f3: Scalar pH 6.5 disagrees with source and retained pH 6.55

minor / open / confirmed; issue key: cm001010-ph-precision.

Both layers retain exact pH 6.55 in preparation but scalar ph_value is 6.5. The discrepancy is bounded precision/representation loss rather than wholly absent pH.

### f4: Generated target lacks later owner evidence and canonical label spelling differs

minor / open / confirmed; issue key: cm001010-generated-evidence-labels.

The August merged target omits six October owner amount attachments, its references entry and four September primary term additions. Four owner term labels differ only by capitalization from live canonical labels. Reconciliation must first assess source-specific term support and historical evidence limits; copying later annotations is not automatic scientific approval.

## Recommended Actions And Acceptance Checks

### a1

Recover the exact cited source response or another exact primary with a stated denominator, preserve source batch masses and historical attachments, and qualify any unresolved normalization. Do not invent final volume or erase evidence because current access failed.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify the exact material/product specifications or retain appropriately qualified unresolved grounding. Preserve source wording and supported tryptone identity; do not infer a replacement ID.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Align the scalar with source precision and preserve the existing correct preparation sentence with exact evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Correct verified maintained annotations, preserve original evidence/history, then regenerate under separate authorization and check exact evidence retention and canonical labels.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/antibiotic_medium_1.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch029/289/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch029/289/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml:1:id: CultureMech:001010<br>./data/normalized_yaml/bacterial/antibiotic_medium_1.yaml:1:id: CultureMech:001010<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch029/source-preflight-bound/289/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 10 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf; Complete one-page recipe, six amount rows, pH and supplier alternative | supports | Exact collection identity and batch amounts. The complete page has no water row or explicit final-volume denominator. Copyright 2007 is not treated as a publication date. |
| ph | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf; pH line immediately after six ingredients | supports | Exact pH is 6.55; both local layers retain this in preparation but scalar ph_value is 6.5. |
| supplier | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf; Alternative product sentence | supports | The primary explicitly names this supplier product as an alternative; no independently inspected supplier formula is available. |
| history-plan | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json; $.records[134] | context_only | Full local dated plan: six amount excerpts, one omitted water row and two preparation contexts. It is derivative context, not recovered remote response bytes. |
| history-fetch | reports/ingredient_concentration_curation/20261007-medium-source-fetch-1500-2000.json; $.records[134] | context_only | Local original fetch receipt asserts HTTP 200, accessed_at 2026-10-07T13:43:16.000018+00:00 and response hash f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec; the raw response is unavailable now. |
| raw-search | Owned exact checkout and frozen preflight search receipt; Ignored-inclusive exact cited response-hash and medium1532 URL search | context_only | The complete recorded search found current owner, plan/fetch/record reports and derivative inventories, with no full embedded API payload recovered. Individual excerpts are not reconstructed into an invented response. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact live obo_id, canonical label, obsolete flag, definition and source-specific form metadata | supports | CHEBI:17234 resolves to glucose. Canonical label and source-specific complex-material identity are separate claims. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact live obo_id, canonical label, obsolete flag, definition and source-specific form metadata | supports | CHEBI:2509 resolves to agar. Canonical label and source-specific complex-material identity are separate claims. |
| foodon03302088 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03302088; Exact live obo_id, canonical label, obsolete flag, definition and source-specific form metadata | supports | FOODON:03302088 resolves to beef extract. Canonical label and source-specific complex-material identity are separate claims. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; Exact live obo_id, canonical label, obsolete flag, definition and source-specific form metadata | supports | FOODON:03315426 resolves to yeast extract. Canonical label and source-specific complex-material identity are separate claims. |
| micro0000178 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178; Exact live obo_id, canonical label, obsolete flag, definition and source-specific form metadata | supports | MICRO:0000178 resolves to peptone. Canonical label and source-specific complex-material identity are separate claims. |
| micro0000182 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182; Exact live obo_id, canonical label, obsolete flag, definition and source-specific form metadata | supports | MICRO:0000182 resolves to tryptone. Canonical label and source-specific complex-material identity are separate claims. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete pinned index exact lookup of the two asserted current secondary keys | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows": {"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml; data/normalized_yaml/bacterial/antibiotic_medium_1.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml", "events": 7, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current API amount/evidence processing, exact-term repair and generated merge code are inspected input context only. September/October owner additions postdate the August target; do not claim current code caused the older target or rerun a mutator. |
| writer-1 | scripts/review_medium_concentration_evidence.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current API amount/evidence processing, exact-term repair and generated merge code are inspected input context only. September/October owner additions postdate the August target; do not claim current code caused the older target or rerun a mutator. |
| writer-2 | scripts/repair_bacterial_score10_exact_terms_batch2.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current API amount/evidence processing, exact-term repair and generated merge code are inspected input context only. September/October owner additions postdate the August target; do not claim current code caused the older target or rerun a mutator. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current API amount/evidence processing, exact-term repair and generated merge code are inspected input context only. September/October owner additions postdate the August target; do not claim current code caused the older target or rerun a mutator. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch029/289/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| mediadive1532api-attempt | https://mediadive.dsmz.de/rest/medium/1532; Preserved exact public retrieval result | context_only | Exact MediaDive 1532 returned HTTP 503 in the initial attempt and separately preserved retry. The cited original f1376f… response is not recovered; derivative local excerpts retain historical claims but cannot authenticate the full provider volume basis. Required formulation-provenance verification remains incomplete. |
| mediadive1532retry-attempt | https://mediadive.dsmz.de/rest/medium/1532; Preserved exact public retrieval result | context_only | Exact MediaDive 1532 returned HTTP 503 in the initial attempt and separately preserved retry. The cited original f1376f… response is not recovered; derivative local excerpts retain historical claims but cannot authenticate the full provider volume basis. Required formulation-provenance verification remains incomplete. |
| bd226340-attempt | https://www.bd.com/en-us/products-and-solutions/products/product-page.226340; Preserved exact public retrieval result | context_only | The exact BD 226340 supplier page returned 403. The collection explicitly names the alternative product, but no independent supplier formulation or reconstitution dose is inferred. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact MediaDive 1532 returned HTTP 503 in the initial attempt and separately preserved retry. The cited original f1376f… response is not recovered; derivative local excerpts retain historical claims but cannot authenticate the full provider volume basis. Required formulation-provenance verification remains incomplete.
- Exact MediaDive 1532 returned HTTP 503 in the initial attempt and separately preserved retry. The cited original f1376f… response is not recovered; derivative local excerpts retain historical claims but cannot authenticate the full provider volume basis. Required formulation-provenance verification remains incomplete.
- The exact BD 226340 supplier page returned 403. The collection explicitly names the alternative product, but no independent supplier formulation or reconstitution dose is inferred.
- Historical amount evidence was read and matched to the exact local plan/report, not discarded. This partial review makes no claim that inaccessible provider history is false; it distinguishes primary batch-mass support from an unverified per-liter denominator. No typical sterilization or growth conditions were supplied.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T162106Z-culturemech-001010-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: antibiotic_medium_1 (CultureMech:001010)'
started_at: '2026-10-21T16:17:55Z'
finished_at: '2026-10-21T16:21:06Z'
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
summary: The exact DSMZ 1532 primary supports the six named batch masses and pH 6.55,
  but prints no water or volume denominator. The maintained owner has six later amount-evidence
  objects whose excerpts and historical hash/time match local derivative reports;
  the full cited API response was not recovered and current requests return HTTP 503.
  The generated target omits those later evidence and grounding additions. Retain
  the unresolved per-liter basis, reconcile scalar pH 6.5 with retained preparation
  pH 6.55, and qualify source-specific complex-ingredient grounding. This review is
  partial for the unavailable provider/formulation basis.
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
  - path: data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml
    sha256: d8fefd5e0f9cddd145c4bc4882453cebec2756b3072d8643a441ad227d054ffa
    role: target
  - path: data/normalized_yaml/bacterial/antibiotic_medium_1.yaml
    sha256: 352c418edfb5f4ac885564ec22a33340c412ceb184b7618d2776ceb866110621
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
    sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/antibiotic_medium_1.yaml.md
    sha256: 9ce2141de1fffa5f0c53da4c332872ffe46d9bfd32f883b8ad855d716c4264f4
    role: context
  - path: reports/ingredient_concentration_curation/20261007-medium-source-fetch-1500-2000.json
    sha256: b6856e96be7c57a5ae4f670acf8869af50abbd0b8b52aa087ebe850b48fc7472
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
  - path: scripts/repair_bacterial_score10_exact_terms_batch2.py
    sha256: b598b051c7cbec73cb52d49e116d8d1c33c052e3d9cf74877041ce1e58a16a44
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
  selection: Task review 289; batch 029 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-eight task batches
    contain 280 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 283 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001010
targets:
- target_id: CultureMech:001010
  path: data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml
  label: antibiotic_medium_1
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/antibiotic_medium_1.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch029/289/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch029/289/strict.tsv"
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001010
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
  - CultureMech:001010
- check_id: mediadive1532api-source-access
  name: 'Exact source content access: mediadive1532api'
  required: true
  status: unavailable
  summary: Exact MediaDive 1532 returned HTTP 503 in the initial attempt and separately
    preserved retry. The cited original f1376f… response is not recovered; derivative
    local excerpts retain historical claims but cannot authenticate the full provider
    volume basis. Required formulation-provenance verification remains incomplete.
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - mediadive1532api-attempt
- check_id: mediadive1532retry-source-access
  name: 'Exact source content access: mediadive1532retry'
  required: true
  status: unavailable
  summary: Exact MediaDive 1532 returned HTTP 503 in the initial attempt and separately
    preserved retry. The cited original f1376f… response is not recovered; derivative
    local excerpts retain historical claims but cannot authenticate the full provider
    volume basis. Required formulation-provenance verification remains incomplete.
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - mediadive1532retry-attempt
- check_id: bd226340-source-access
  name: 'Exact source content access: bd226340'
  required: false
  status: unavailable
  summary: The exact BD 226340 supplier page returned 403. The collection explicitly
    names the alternative product, but no independent supplier formulation or reconstitution
    dose is inferred.
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - bd226340-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T16:21:05Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/antibiotic_medium_1.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:21:05Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:38.895584Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch029/289/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:40.074157Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch029/289/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:41.433679Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:42.244258Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T16:21:05Z'
  support: supports
  summary: './data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml:1:id: CultureMech:001010

    ./data/normalized_yaml/bacterial/antibiotic_medium_1.yaml:1:id: CultureMech:001010

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/source-preflight-bound/289/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T16:21:05Z'
  support: supports
  summary: 10 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: fecab4de83fe053ef9c801a3a754977a6be6043a92407552d57d662792abd8a1
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf
  locator: Complete one-page recipe, six amount rows, pH and supplier alternative
  accessed_at: '2026-10-21T16:01:40.701665Z'
  support: supports
  summary: Exact collection identity and batch amounts. The complete page has no water
    row or explicit final-volume denominator. Copyright 2007 is not treated as a publication
    date.
  quote: 1532. ANTIBIOTIC MEDIUM 1
  snapshot_sha256: bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8
- evidence_id: ph
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf
  locator: pH line immediately after six ingredients
  accessed_at: '2026-10-21T16:01:40.701665Z'
  support: supports
  summary: Exact pH is 6.55; both local layers retain this in preparation but scalar
    ph_value is 6.5.
  quote: pH 6.55
  snapshot_sha256: bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8
- evidence_id: supplier
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf
  locator: Alternative product sentence
  accessed_at: '2026-10-21T16:01:40.701665Z'
  support: supports
  summary: The primary explicitly names this supplier product as an alternative; no
    independently inspected supplier formula is available.
  quote: or Difco Antibiotic Medium 1 (BD, order number 226340)
  snapshot_sha256: bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8
- evidence_id: history-plan
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
  locator: $.records[134]
  accessed_at: '2026-10-21T16:21:05Z'
  support: context_only
  summary: 'Full local dated plan: six amount excerpts, one omitted water row and
    two preparation contexts. It is derivative context, not recovered remote response
    bytes.'
  snapshot_sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
- evidence_id: history-fetch
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-medium-source-fetch-1500-2000.json
  locator: $.records[134]
  accessed_at: '2026-10-21T16:21:05Z'
  support: context_only
  summary: Local original fetch receipt asserts HTTP 200, accessed_at 2026-10-07T13:43:16.000018+00:00
    and response hash f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec;
    the raw response is unavailable now.
  snapshot_sha256: b6856e96be7c57a5ae4f670acf8869af50abbd0b8b52aa087ebe850b48fc7472
- evidence_id: raw-search
  kind: search
  reference: Owned exact checkout and frozen preflight search receipt
  locator: Ignored-inclusive exact cited response-hash and medium1532 URL search
  accessed_at: '2026-10-21T16:21:05Z'
  support: context_only
  summary: The complete recorded search found current owner, plan/fetch/record reports
    and derivative inventories, with no full embedded API payload recovered. Individual
    excerpts are not reconstructed into an invented response.
  snapshot_sha256: 53d6e99bd525995f61a334ed984eea3de38ff4e20c7f9802406261acb71abefc
  search_scope: /private/tmp/culturemech-record-review-20261019-batch-028; rg --no-ignore
    --hidden -l f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec|mediadive\.dsmz\.de/rest/medium/1532
    .
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact live obo_id, canonical label, obsolete flag, definition and source-specific
    form metadata
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose. Canonical label and source-specific complex-material
    identity are separate claims.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact live obo_id, canonical label, obsolete flag, definition and source-specific
    form metadata
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 resolves to agar. Canonical label and source-specific complex-material
    identity are separate claims.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: foodon03302088
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03302088
  locator: Exact live obo_id, canonical label, obsolete flag, definition and source-specific
    form metadata
  accessed_at: '2026-10-21T08:00:49.378816Z'
  support: supports
  summary: FOODON:03302088 resolves to beef extract. Canonical label and source-specific
    complex-material identity are separate claims.
  snapshot_sha256: ee2e9f57bae58d8170d339f9a0575ea59cda36ff7c8a09fcf457358dcc894f22
- evidence_id: foodon03315426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: Exact live obo_id, canonical label, obsolete flag, definition and source-specific
    form metadata
  accessed_at: '2026-10-21T08:00:49.388263Z'
  support: supports
  summary: FOODON:03315426 resolves to yeast extract. Canonical label and source-specific
    complex-material identity are separate claims.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: micro0000178
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178
  locator: Exact live obo_id, canonical label, obsolete flag, definition and source-specific
    form metadata
  accessed_at: '2026-10-21T08:00:49.423450Z'
  support: supports
  summary: MICRO:0000178 resolves to peptone. Canonical label and source-specific
    complex-material identity are separate claims.
  snapshot_sha256: ef45aa186438f91d015280171fde8ccb25740a50cc6f2c6e848de6aad3339b31
- evidence_id: micro0000182
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182
  locator: Exact live obo_id, canonical label, obsolete flag, definition and source-specific
    form metadata
  accessed_at: '2026-10-20T07:37:21.973857Z'
  support: supports
  summary: MICRO:0000182 resolves to tryptone. Canonical label and source-specific
    complex-material identity are separate claims.
  snapshot_sha256: 01875997c482a49e4d41eb35c6c697e190afd236a8527625e94b6f96df3872b0
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete pinned index exact lookup of the two asserted current secondary
    keys
  accessed_at: '2026-10-21T16:21:05Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows":
    {"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier":
    "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type":
    "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml; data/normalized_yaml/bacterial/antibiotic_medium_1.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T16:21:05Z'
  support: context_only
  summary: '[{"input": "target", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/antibiotic_medium_1.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:21:05Z'
  support: context_only
  summary: Current API amount/evidence processing, exact-term repair and generated
    merge code are inspected input context only. September/October owner additions
    postdate the August target; do not claim current code caused the older target
    or rerun a mutator.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: scripts/review_medium_concentration_evidence.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:21:05Z'
  support: context_only
  summary: Current API amount/evidence processing, exact-term repair and generated
    merge code are inspected input context only. September/October owner additions
    postdate the August target; do not claim current code caused the older target
    or rerun a mutator.
  snapshot_sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
- evidence_id: writer-2
  kind: record_content
  reference: scripts/repair_bacterial_score10_exact_terms_batch2.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:21:05Z'
  support: context_only
  summary: Current API amount/evidence processing, exact-term repair and generated
    merge code are inspected input context only. September/October owner additions
    postdate the August target; do not claim current code caused the older target
    or rerun a mutator.
  snapshot_sha256: b598b051c7cbec73cb52d49e116d8d1c33c052e3d9cf74877041ce1e58a16a44
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:21:05Z'
  support: context_only
  summary: Current API amount/evidence processing, exact-term repair and generated
    merge code are inspected input context only. September/October owner additions
    postdate the August target; do not claim current code caused the older target
    or rerun a mutator.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/289/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T16:21:05Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 61ad254e1ab82312be43892f3732b2b26f1d306e34a29d671fb53a148e1feee1
- evidence_id: mediadive1532api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1532
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:01:39.342585Z'
  support: context_only
  summary: Exact MediaDive 1532 returned HTTP 503 in the initial attempt and separately
    preserved retry. The cited original f1376f… response is not recovered; derivative
    local excerpts retain historical claims but cannot authenticate the full provider
    volume basis. Required formulation-provenance verification remains incomplete.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive1532retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1532
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:03:01.045401Z'
  support: context_only
  summary: Exact MediaDive 1532 returned HTTP 503 in the initial attempt and separately
    preserved retry. The cited original f1376f… response is not recovered; derivative
    local excerpts retain historical claims but cannot authenticate the full provider
    volume basis. Required formulation-provenance verification remains incomplete.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: bd226340-attempt
  kind: database
  reference: https://www.bd.com/en-us/products-and-solutions/products/product-page.226340
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:03:01.818254Z'
  support: context_only
  summary: The exact BD 226340 supplier page returned 403. The collection explicitly
    names the alternative product, but no independent supplier formulation or reconstitution
    dose is inferred.
  snapshot_sha256: 54ef917005125e1bced87c42cc5ae3b4e7a9448fb36a54f8ffe2c90e77929bfa
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Every asserted ontology identifier and current secondary key
  outcome: concern
  summary: Six distinct asserted primary IDs are nonobsolete. Four owner labels differ
    only by capitalization from exact FOODON/MICRO labels; target has only the glucose
    and agar primary IDs. Both asserted secondary CHEBI keys have exact mapped preferred
    rows in the pinned MIM index. Target linkage is 2/6 primary and 2/6 secondary
    (33.33% each); owner linkage is 6/6 primary (100%) and 2/6 secondary (33.33%),
    on a 0–100 linkage scale, not correctness scores. No legacy MIM field is asserted.
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - record
  - owner-0
  - mim
  - chebi17234
  - chebi2509
  - foodon03302088
  - foodon03315426
  - micro0000178
  - micro0000182
  details: "[\n  {\n    \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n    \"field_path\": \"ingredients[1].term\",\n    \"label\": \"Beef extract\"\
    ,\n    \"id\": \"FOODON:03302088\",\n    \"canonical_label\": \"beef extract\"\
    \n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n    \"field_path\": \"ingredients[0].term\",\n    \"label\": \"Yeast extract\"\
    ,\n    \"id\": \"FOODON:03315426\",\n    \"canonical_label\": \"yeast extract\"\
    \n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n    \"field_path\": \"ingredients[3].term\",\n    \"label\": \"Peptone\",\n\
    \    \"id\": \"MICRO:0000178\",\n    \"canonical_label\": \"peptone\"\n  },\n\
    \  {\n    \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n    \"field_path\": \"ingredients[2].term\",\n    \"label\": \"Tryptone\",\n\
    \    \"id\": \"MICRO:0000182\",\n    \"canonical_label\": \"tryptone\"\n  }\n]"
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact medium and supplier identity
  outcome: supported
  summary: The exact primary title, DSMZ 1532 and local stable identity agree. The
    sole maintained owner is resolved from the complete merge event. The source names
    BD 226340 as an alternative, without establishing every commercial formulation
    detail. No DOI/PMID, taxon, strain, parent/child medium or standalone stock reference
    is asserted.
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - record
  - owner-0
  - primary
  - supplier
  - id-search
- assessment_id: classification
  area: scope
  topic: Complex agar formulation and source scope
  outcome: supported
  summary: 'Complex/undefined classification is supported by yeast/beef extracts and
    digests; solid-agar is supported by the mandatory agar row. G_PER_L is not intrinsically
    invalid for a recipe that gels: its unresolved denominator is the actual issue.
    Generic microbial-cultivation text is not evidence for a particular organism or
    experimental growth outcome.'
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - record
  - owner-0
  - primary
- assessment_id: source-forms
  area: grounding
  topic: Complex ingredient specificity and exact label spelling
  outcome: concern
  summary: The source pancreatic digest of casein agrees with MICRO tryptone wording.
    Generic peptone does not itself establish the mammalian enzymatic origin in MICRO:0000178.
    FOODON:03315426 adds a not-heat-treated qualification and FOODON:03302088 adds
    fully-heat-treated context not established by the source labels. These are specificity
    limits, not proof the materials have the opposite properties. Preserve valid glucose/agar
    identity and do not guess replacement terms.
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - primary
  - foodon03315426
  - foodon03302088
  - micro0000178
  - micro0000182
  - chebi17234
  - chebi2509
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 17 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"label\": \"Yeast extract —\
    \ target\",\n    \"decision\": \"unsupported\",\n    \"source_stage\": \"Main\
    \ recipe\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"attached_evidence\": []\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz1532\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\",\n       \
    \ \"source_locator\": \"Ingredient table row1, complete primary has no volume\
    \ denominator\",\n        \"exact_source_quote\": \"Yeast extract 3.0 g\",\n \
    \       \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed batch mass matches the\
    \ local numeral. Its G_PER_L denominator cannot be independently verified from\
    \ the primary; retain the historical provider claim without calling the value\
    \ disproven. No amount evidence is attached in this generated layer.\"\n  },\n\
    \  {\n    \"decision_id\": \"q2\",\n    \"label\": \"Yeast extract — owner\",\n\
    \    \"decision\": \"unsupported\",\n    \"source_stage\": \"Main recipe\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"attached_evidence\": [\n          {\n            \"reference\": \"\
    https://mediadive.dsmz.de/rest/medium/1532\",\n            \"supports\": \"SUPPORT\"\
    ,\n            \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 1,\\n                        \\\"compound\\\": \\\"Yeast extract\\\",\\n   \
    \                     \\\"compound_id\\\": 16,\\n                        \\\"\
    amount\\\": 3,\\n                        \\\"unit\\\": \\\"g\\\",\\n         \
    \               \\\"g_l\\\": 3,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n            \"explanation\": \"Concentration evidence\
    \ for ingredients[0].concentration (Yeast extract) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[0].\
    \ Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per\
    \ L) = 3 g/L. This supports the provider-declared main-recipe concentration, not\
    \ an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec.\"\
    \n          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1532\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\"\
    ,\n        \"source_locator\": \"Ingredient table row1, complete primary has no\
    \ volume denominator\",\n        \"exact_source_quote\": \"Yeast extract 3.0 g\"\
    ,\n        \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed batch mass matches the\
    \ local numeral. Its G_PER_L denominator cannot be independently verified from\
    \ the primary; retain the historical provider claim without calling the value\
    \ disproven. Six owner excerpts match the dated local plan/report, but full cited\
    \ raw 1532 bytes are unavailable. Do not mark verified from derivative equality\
    \ alone.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n    \"label\": \"Beef extract\
    \ — target\",\n    \"decision\": \"unsupported\",\n    \"source_stage\": \"Main\
    \ recipe\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"attached_evidence\": []\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz1532\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\",\n       \
    \ \"source_locator\": \"Ingredient table row2, complete primary has no volume\
    \ denominator\",\n        \"exact_source_quote\": \"Beef extract 1.5 g\",\n  \
    \      \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed batch mass matches the\
    \ local numeral. Its G_PER_L denominator cannot be independently verified from\
    \ the primary; retain the historical provider claim without calling the value\
    \ disproven. No amount evidence is attached in this generated layer.\"\n  },\n\
    \  {\n    \"decision_id\": \"q4\",\n    \"label\": \"Beef extract — owner\",\n\
    \    \"decision\": \"unsupported\",\n    \"source_stage\": \"Main recipe\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"attached_evidence\": [\n          {\n            \"reference\": \"\
    https://mediadive.dsmz.de/rest/medium/1532\",\n            \"supports\": \"SUPPORT\"\
    ,\n            \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 2,\\n                        \\\"compound\\\": \\\"Beef extract\\\",\\n    \
    \                    \\\"compound_id\\\": 85,\\n                        \\\"amount\\\
    \": 1.5,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 1.5,\\n                        \\\"optional\\\": 0\\n \
    \                   }\",\n            \"explanation\": \"Concentration evidence\
    \ for ingredients[1].concentration (Beef extract) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[1].\
    \ Provider explicitly reports g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000\
    \ ml per L) = 1.5 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec.\"\
    \n          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1532\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\"\
    ,\n        \"source_locator\": \"Ingredient table row2, complete primary has no\
    \ volume denominator\",\n        \"exact_source_quote\": \"Beef extract 1.5 g\"\
    ,\n        \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed batch mass matches the\
    \ local numeral. Its G_PER_L denominator cannot be independently verified from\
    \ the primary; retain the historical provider claim without calling the value\
    \ disproven. Six owner excerpts match the dated local plan/report, but full cited\
    \ raw 1532 bytes are unavailable. Do not mark verified from derivative equality\
    \ alone.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"label\": \"Pancreatic\
    \ digest of casein — target\",\n    \"decision\": \"unsupported\",\n    \"source_stage\"\
    : \"Main recipe\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"attached_evidence\": []\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz1532\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\",\n       \
    \ \"source_locator\": \"Ingredient table row3, complete primary has no volume\
    \ denominator\",\n        \"exact_source_quote\": \"Pancreatic Digest of Casein\
    \ 4.0 g\",\n        \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed batch mass matches the\
    \ local numeral. Its G_PER_L denominator cannot be independently verified from\
    \ the primary; retain the historical provider claim without calling the value\
    \ disproven. No amount evidence is attached in this generated layer.\"\n  },\n\
    \  {\n    \"decision_id\": \"q6\",\n    \"label\": \"Pancreatic digest of casein\
    \ — owner\",\n    \"decision\": \"unsupported\",\n    \"source_stage\": \"Main\
    \ recipe\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"attached_evidence\": [\n          {\n            \"reference\": \"\
    https://mediadive.dsmz.de/rest/medium/1532\",\n            \"supports\": \"SUPPORT\"\
    ,\n            \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 3,\\n                        \\\"compound\\\": \\\"Pancreatic digest of casein\\\
    \",\\n                        \\\"compound_id\\\": 531,\\n                   \
    \     \\\"amount\\\": 4,\\n                        \\\"unit\\\": \\\"g\\\",\\\
    n                        \\\"g_l\\\": 4,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n            \"explanation\": \"Concentration\
    \ evidence for ingredients[2].concentration (Pancreatic digest of casein) in MediaDive\
    \ medium 1532; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports\
    \ g_l=4; check: 4 g * 1 g/g / (1000 ml / 1000 ml per L) = 4 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00;\
    \ response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec.\"\
    \n          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1532\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\"\
    ,\n        \"source_locator\": \"Ingredient table row3, complete primary has no\
    \ volume denominator\",\n        \"exact_source_quote\": \"Pancreatic Digest of\
    \ Casein 4.0 g\",\n        \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed batch mass matches the\
    \ local numeral. Its G_PER_L denominator cannot be independently verified from\
    \ the primary; retain the historical provider claim without calling the value\
    \ disproven. Six owner excerpts match the dated local plan/report, but full cited\
    \ raw 1532 bytes are unavailable. Do not mark verified from derivative equality\
    \ alone.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"label\": \"Peptone\
    \ — target\",\n    \"decision\": \"unsupported\",\n    \"source_stage\": \"Main\
    \ recipe\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"attached_evidence\": []\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz1532\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\",\n       \
    \ \"source_locator\": \"Ingredient table row4, complete primary has no volume\
    \ denominator\",\n        \"exact_source_quote\": \"Peptone 6.0 g\",\n       \
    \ \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed batch mass matches the\
    \ local numeral. Its G_PER_L denominator cannot be independently verified from\
    \ the primary; retain the historical provider claim without calling the value\
    \ disproven. No amount evidence is attached in this generated layer.\"\n  },\n\
    \  {\n    \"decision_id\": \"q8\",\n    \"label\": \"Peptone — owner\",\n    \"\
    decision\": \"unsupported\",\n    \"source_stage\": \"Main recipe\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"attached_evidence\": [\n          {\n            \"reference\": \"\
    https://mediadive.dsmz.de/rest/medium/1532\",\n            \"supports\": \"SUPPORT\"\
    ,\n            \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 4,\\n                        \\\"compound\\\": \\\"Peptone\\\",\\n         \
    \               \\\"compound_id\\\": 1,\\n                        \\\"amount\\\
    \": 6,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 6,\\n                        \\\"optional\\\": 0\\n     \
    \               }\",\n            \"explanation\": \"Concentration evidence for\
    \ ingredients[3].concentration (Peptone) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[3].\
    \ Provider explicitly reports g_l=6; check: 6 g * 1 g/g / (1000 ml / 1000 ml per\
    \ L) = 6 g/L. This supports the provider-declared main-recipe concentration, not\
    \ an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec.\"\
    \n          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1532\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\"\
    ,\n        \"source_locator\": \"Ingredient table row4, complete primary has no\
    \ volume denominator\",\n        \"exact_source_quote\": \"Peptone 6.0 g\",\n\
    \        \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed batch mass matches the\
    \ local numeral. Its G_PER_L denominator cannot be independently verified from\
    \ the primary; retain the historical provider claim without calling the value\
    \ disproven. Six owner excerpts match the dated local plan/report, but full cited\
    \ raw 1532 bytes are unavailable. Do not mark verified from derivative equality\
    \ alone.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n    \"label\": \"Glucose\
    \ — target\",\n    \"decision\": \"unsupported\",\n    \"source_stage\": \"Main\
    \ recipe\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"attached_evidence\": []\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz1532\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\",\n       \
    \ \"source_locator\": \"Ingredient table row5, complete primary has no volume\
    \ denominator\",\n        \"exact_source_quote\": \"Glucose 1.0  g\",\n      \
    \  \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed batch mass matches the\
    \ local numeral. Its G_PER_L denominator cannot be independently verified from\
    \ the primary; retain the historical provider claim without calling the value\
    \ disproven. No amount evidence is attached in this generated layer.\"\n  },\n\
    \  {\n    \"decision_id\": \"q10\",\n    \"label\": \"Glucose — owner\",\n   \
    \ \"decision\": \"unsupported\",\n    \"source_stage\": \"Main recipe\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"attached_evidence\": [\n          {\n            \"reference\": \"\
    https://mediadive.dsmz.de/rest/medium/1532\",\n            \"supports\": \"SUPPORT\"\
    ,\n            \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 5,\\n                        \\\"compound\\\": \\\"Glucose\\\",\\n         \
    \               \\\"compound_id\\\": 5,\\n                        \\\"amount\\\
    \": 1,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 1,\\n                        \\\"mmol_l\\\": 5.55062,\\n\
    \                        \\\"optional\\\": 0\\n                    }\",\n    \
    \        \"explanation\": \"Concentration evidence for ingredients[4].concentration\
    \ (Glucose) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[4]. Provider\
    \ explicitly reports g_l=1; check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1\
    \ g/L. This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00;\
    \ response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec.\"\
    \n          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1532\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\"\
    ,\n        \"source_locator\": \"Ingredient table row5, complete primary has no\
    \ volume denominator\",\n        \"exact_source_quote\": \"Glucose 1.0  g\",\n\
    \        \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed batch mass matches the\
    \ local numeral. Its G_PER_L denominator cannot be independently verified from\
    \ the primary; retain the historical provider claim without calling the value\
    \ disproven. Six owner excerpts match the dated local plan/report, but full cited\
    \ raw 1532 bytes are unavailable. Do not mark verified from derivative equality\
    \ alone.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"label\": \"Agar —\
    \ target\",\n    \"decision\": \"unsupported\",\n    \"source_stage\": \"Main\
    \ recipe\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"attached_evidence\": []\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz1532\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\",\n       \
    \ \"source_locator\": \"Ingredient table row6, complete primary has no volume\
    \ denominator\",\n        \"exact_source_quote\": \"Agar 20.0 g\",\n        \"\
    snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed batch mass matches the\
    \ local numeral. Its G_PER_L denominator cannot be independently verified from\
    \ the primary; retain the historical provider claim without calling the value\
    \ disproven. No amount evidence is attached in this generated layer.\"\n  },\n\
    \  {\n    \"decision_id\": \"q12\",\n    \"label\": \"Agar — owner\",\n    \"\
    decision\": \"unsupported\",\n    \"source_stage\": \"Main recipe\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"attached_evidence\": [\n          {\n            \"reference\": \"\
    https://mediadive.dsmz.de/rest/medium/1532\",\n            \"supports\": \"SUPPORT\"\
    ,\n            \"snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 6,\\n                        \\\"compound\\\": \\\"Agar\\\",\\n            \
    \            \\\"compound_id\\\": 3,\\n                        \\\"amount\\\"\
    : 20,\\n                        \\\"unit\\\": \\\"g\\\",\\n                  \
    \      \\\"g_l\\\": 20,\\n                        \\\"mmol_l\\\": 59.4654,\\n\
    \                        \\\"optional\\\": 0\\n                    }\",\n    \
    \        \"explanation\": \"Concentration evidence for ingredients[5].concentration\
    \ (Agar) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[5]. Provider\
    \ explicitly reports g_l=20; check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) =\
    \ 20 g/L. This supports the provider-declared main-recipe concentration, not an\
    \ independently measured final volume, a stock composition, or a downstream assay\
    \ dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec.\"\
    \n          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1532\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\"\
    ,\n        \"source_locator\": \"Ingredient table row6, complete primary has no\
    \ volume denominator\",\n        \"exact_source_quote\": \"Agar 20.0 g\",\n  \
    \      \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The printed batch mass matches the\
    \ local numeral. Its G_PER_L denominator cannot be independently verified from\
    \ the primary; retain the historical provider claim without calling the value\
    \ disproven. Six owner excerpts match the dated local plan/report, but full cited\
    \ raw 1532 bytes are unavailable. Do not mark verified from derivative equality\
    \ alone.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"label\": \"Scalar\
    \ pH\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Main recipe\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.5\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.5\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1532\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\"\
    ,\n        \"source_locator\": \"Primary pH line\",\n        \"exact_source_quote\"\
    : \"pH 6.55\",\n        \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The source explicitly gives 6.55;\
    \ scalar 6.5 loses precision and disagrees with the already retained preparation\
    \ text. Do not claim pH is wholly missing.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q14\",\n    \"label\": \"Retained preparation pH\",\n    \"decision\": \"\
    evidence_only\",\n    \"source_stage\": \"Main recipe\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"pH 6.55\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"pH 6.55\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz1532\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\"\
    ,\n        \"source_locator\": \"Primary pH line\",\n        \"exact_source_quote\"\
    : \"pH 6.55\",\n        \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The preparation sentence already\
    \ contains the exact pH 6.55. Attach narrow evidence and reconcile scalar precision.\"\
    \n  },\n  {\n    \"decision_id\": \"q15\",\n    \"label\": \"Supplier alternative\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_stage\": \"Main recipe\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"or Difco Antibiotic Medium 1 (BD, order number 226340)\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"or Difco Antibiotic Medium 1 (BD, order number 226340)\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1532\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\"\
    ,\n        \"source_locator\": \"Primary final sentence\",\n        \"exact_source_quote\"\
    : \"or Difco Antibiotic Medium 1 (BD, order number 226340)\",\n        \"snapshot_sha256\"\
    : \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\",\n    \
    \    \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"226340 is a product identifier, not\
    \ a dose. This retained alternative is supported; commercial formula and reconstitution\
    \ dose are not independently established.\"\n  },\n  {\n    \"decision_id\": \"\
    q16\",\n    \"label\": \"Historical water-only lead\",\n    \"decision\": \"unsupported\"\
    ,\n    \"source_stage\": \"Historical provider-only context\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Yeast extract\",\n            \"concentration\"\
    : {\n              \"value\": \"3\",\n              \"unit\": \"G_PER_L\"\n  \
    \          }\n          },\n          {\n            \"preferred_term\": \"Beef\
    \ extract\",\n            \"concentration\": {\n              \"value\": \"1.5\"\
    ,\n              \"unit\": \"G_PER_L\"\n            }\n          },\n        \
    \  {\n            \"preferred_term\": \"Pancreatic digest of casein\",\n     \
    \       \"concentration\": {\n              \"value\": \"4\",\n              \"\
    unit\": \"G_PER_L\"\n            }\n          },\n          {\n            \"\
    preferred_term\": \"Peptone\",\n            \"concentration\": {\n           \
    \   \"value\": \"6\",\n              \"unit\": \"G_PER_L\"\n            }\n  \
    \        },\n          {\n            \"preferred_term\": \"Glucose\",\n     \
    \       \"term\": {\n              \"id\": \"CHEBI:17234\",\n              \"\
    label\": \"glucose\"\n            },\n            \"concentration\": {\n     \
    \         \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n           \
    \ },\n            \"mediaingredientmech_chebi_term\": {\n              \"id\"\
    : \"CHEBI:17234\",\n              \"label\": \"glucose\"\n            }\n    \
    \      },\n          {\n            \"preferred_term\": \"Agar\",\n          \
    \  \"term\": {\n              \"id\": \"CHEBI:2509\",\n              \"label\"\
    : \"agar\"\n            },\n            \"concentration\": {\n              \"\
    value\": \"20\",\n              \"unit\": \"G_PER_L\"\n            },\n      \
    \      \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\"\
    ,\n              \"label\": \"agar\"\n            }\n          }\n        ],\n\
    \        \"missing_item\": \"Distilled water\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\",\n      \
    \  \"field_path\": \"ingredients\",\n        \"stored\": [\n          {\n    \
    \        \"preferred_term\": \"Yeast extract\",\n            \"concentration\"\
    : {\n              \"value\": \"3\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"term\": {\n              \"id\": \"FOODON:03315426\"\
    ,\n              \"label\": \"Yeast extract\"\n            },\n            \"\
    evidence\": [\n              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1532\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 1,\\n                      \
    \  \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n         \
    \       \"explanation\": \"Concentration evidence for ingredients[0].concentration\
    \ (Yeast extract) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[0].\
    \ Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per\
    \ L) = 3 g/L. This supports the provider-declared main-recipe concentration, not\
    \ an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Beef extract\",\n            \"concentration\": {\n              \"value\"\
    : \"1.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    term\": {\n              \"id\": \"FOODON:03302088\",\n              \"label\"\
    : \"Beef extract\"\n            },\n            \"evidence\": [\n            \
    \  {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1532\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 2,\\n                      \
    \  \\\"compound\\\": \\\"Beef extract\\\",\\n                        \\\"compound_id\\\
    \": 85,\\n                        \\\"amount\\\": 1.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n \
    \                       \\\"optional\\\": 0\\n                    }\",\n     \
    \           \"explanation\": \"Concentration evidence for ingredients[1].concentration\
    \ (Beef extract) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[1].\
    \ Provider explicitly reports g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000\
    \ ml per L) = 1.5 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Pancreatic digest of casein\",\n            \"concentration\": {\n       \
    \       \"value\": \"4\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"term\": {\n              \"id\": \"MICRO:0000182\",\n         \
    \     \"label\": \"Tryptone\"\n            },\n            \"evidence\": [\n \
    \             {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1532\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 3,\\n                      \
    \  \\\"compound\\\": \\\"Pancreatic digest of casein\\\",\\n                 \
    \       \\\"compound_id\\\": 531,\\n                        \\\"amount\\\": 4,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 4,\\n                        \\\"optional\\\": 0\\n               \
    \     }\",\n                \"explanation\": \"Concentration evidence for ingredients[2].concentration\
    \ (Pancreatic digest of casein) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[2].\
    \ Provider explicitly reports g_l=4; check: 4 g * 1 g/g / (1000 ml / 1000 ml per\
    \ L) = 4 g/L. This supports the provider-declared main-recipe concentration, not\
    \ an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Peptone\",\n            \"concentration\": {\n              \"value\": \"\
    6\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"term\"\
    : {\n              \"id\": \"MICRO:0000178\",\n              \"label\": \"Peptone\"\
    \n            },\n            \"evidence\": [\n              {\n             \
    \   \"reference\": \"https://mediadive.dsmz.de/rest/medium/1532\",\n         \
    \       \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\n      \
    \                  \\\"recipe_order\\\": 4,\\n                        \\\"compound\\\
    \": \\\"Peptone\\\",\\n                        \\\"compound_id\\\": 1,\\n    \
    \                    \\\"amount\\\": 6,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 6,\\n                    \
    \    \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[3].concentration (Peptone) in MediaDive\
    \ medium 1532; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports\
    \ g_l=6; check: 6 g * 1 g/g / (1000 ml / 1000 ml per L) = 6 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00;\
    \ response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Glucose\",\n            \"term\": {\n              \"id\": \"CHEBI:17234\"\
    ,\n              \"label\": \"glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:17234\",\n              \"label\": \"glucose\"\n         \
    \   },\n            \"evidence\": [\n              {\n                \"reference\"\
    : \"https://mediadive.dsmz.de/rest/medium/1532\",\n                \"supports\"\
    : \"SUPPORT\",\n                \"snippet\": \"{\\n                        \\\"\
    recipe_order\\\": 5,\\n                        \\\"compound\\\": \\\"Glucose\\\
    \",\\n                        \\\"compound_id\\\": 5,\\n                     \
    \   \\\"amount\\\": 1,\\n                        \\\"unit\\\": \\\"g\\\",\\n \
    \                       \\\"g_l\\\": 1,\\n                        \\\"mmol_l\\\
    \": 5.55062,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n                \"explanation\": \"Concentration evidence for ingredients[4].concentration\
    \ (Glucose) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[4]. Provider\
    \ explicitly reports g_l=1; check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1\
    \ g/L. This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:43:16.000018+00:00;\
    \ response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"20\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"mediaingredientmech_chebi_term\": {\n          \
    \    \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n            },\n\
    \            \"evidence\": [\n              {\n                \"reference\":\
    \ \"https://mediadive.dsmz.de/rest/medium/1532\",\n                \"supports\"\
    : \"SUPPORT\",\n                \"snippet\": \"{\\n                        \\\"\
    recipe_order\\\": 6,\\n                        \\\"compound\\\": \\\"Agar\\\"\
    ,\\n                        \\\"compound_id\\\": 3,\\n                       \
    \ \\\"amount\\\": 20,\\n                        \\\"unit\\\": \\\"g\\\",\\n  \
    \                      \\\"g_l\\\": 20,\\n                        \\\"mmol_l\\\
    \": 59.4654,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n                \"explanation\": \"Concentration evidence for ingredients[5].concentration\
    \ (Agar) in MediaDive medium 1532; locator=$.data.solutions[0].recipe[5]. Provider\
    \ explicitly reports g_l=20; check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) =\
    \ 20 g/L. This supports the provider-declared main-recipe concentration, not an\
    \ independently measured final volume, a stock composition, or a downstream assay\
    \ dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:43:16.000018+00:00; response SHA256=f1376f4052e0f1e99f6b3fb5557ff110b477b713919c6daf4cda7c741ce02cec.\"\
    \n              }\n            ]\n          }\n        ],\n        \"missing_item\"\
    : \"Distilled water\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"historical-plan\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1532\"\
    ,\n        \"source_locator\": \"Historical plan $.records[134].claims[6]; alleged\
    \ original $.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"\
    {\\n                        \\\"recipe_order\\\": 7,\\n                      \
    \  \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26\"\
    ,\n        \"quotation_kind\": \"Exact decoded snippet in pinned local derivative\
    \ plan; original remote response hash is not available for verification\"\n  \
    \    }\n    ],\n    \"interpretation\": \"The local historical plan quotes 1000\
    \ ml water and reports a provider 1000 ml volume. No full original response was\
    \ recovered, and current primary has neither. Preserve as a historical follow-up\
    \ lead, not an authenticated new solvent amount or measured final volume.\"\n\
    \  },\n  {\n    \"decision_id\": \"q17\",\n    \"label\": \"Final volume and sterilization\
    \ quantities\",\n    \"decision\": \"not_quantified\",\n    \"source_stage\":\
    \ \"Unspecified source preparation\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml\",\n       \
    \ \"field_path\": \"preparation_steps\",\n        \"stored\": [\n          {\n\
    \            \"step_number\": 1,\n            \"action\": \"MIX\",\n         \
    \   \"description\": \"pH 6.55\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"MIX\",\n            \"description\": \"or Difco\
    \ Antibiotic Medium 1 (BD, order number 226340)\"\n          }\n        ]\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/antibiotic_medium_1.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"pH 6.55\"\n          },\n          {\n       \
    \     \"step_number\": 2,\n            \"action\": \"MIX\",\n            \"description\"\
    : \"or Difco Antibiotic Medium 1 (BD, order number 226340)\"\n          }\n  \
    \      ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1532\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\"\
    ,\n        \"source_locator\": \"Last primary ingredient row\",\n        \"exact_source_quote\"\
    : \"Agar 20.0 g\",\n        \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1532\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1532.pdf\",\n   \
    \     \"source_locator\": \"Primary pH line\",\n        \"exact_source_quote\"\
    : \"pH 6.55\",\n        \"snapshot_sha256\": \"bd461a3a8e6a3aa7543c8855a5fd118aafbeeb544cc1ca5675c32554f9f921a8\"\
    ,\n        \"parsed_text_sha256\": \"1f782216eac733b93631cff37cc3c808854f2c97c192646f2d0ec130eba4a920\"\
    \n      }\n    ],\n    \"interpretation\": \"The entire inspected primary provides\
    \ no final-volume statement, sterilization time/temperature or adjustment reagent\
    \ dose. Do not add typical values; the six G_PER_L claims remain explicitly unresolved.\"\
    \n  }\n]"
- assessment_id: ownership
  area: ownership
  topic: One maintained owner and bounded follow-up
  outcome: supported
  summary: The normalized antibiotic_medium_1.yaml owns corrections; generated target
    and pages are not edit surfaces. Current code was inspected without execution.
    Existing history is preserved and no record-level scientific status is promoted.
  target_ids:
  - CultureMech:001010
  evidence_ids:
  - record
  - owner-0
  - writer-0
  - writer-1
  - writer-2
  - writer-3
findings:
- finding_id: f1
  issue_key: cm001010-basis-unverified
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Per-liter basis is unresolved despite matching batch masses
  description: All six local G_PER_L numerals match printed primary gram amounts,
    but the primary has no solvent or volume denominator. The owner has appropriately
    scoped historical provider attachments; current 503 responses and absence of full
    recovered raw bytes prevent independent confirmation of their 1000 ml basis. This
    is an evidential limitation, not proof the six numbers are wrong.
  target_ids:
  - CultureMech:001010
  field_paths:
  - ingredients[*].concentration
  - ingredients[*].evidence
  evidence_ids:
  - primary
  - history-plan
  - history-fetch
  - raw-search
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/antibiotic_medium_1.yaml
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
  issue_key: cm001010-complex-form-specificity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Some owner complex-material terms assert unsupported specificity
  description: The source names yeast extract, beef extract and peptone but does not
    establish their FOODON heat-treatment qualifiers or MICRO mammalian enzymatic
    origin. The exact pancreatic casein digest is separately supported as tryptone.
    Valid identifier existence does not settle these narrower material claims.
  target_ids:
  - CultureMech:001010
  field_paths:
  - ingredients[0].term
  - ingredients[1].term
  - ingredients[3].term
  evidence_ids:
  - primary
  - owner-0
  - foodon03315426
  - foodon03302088
  - micro0000178
  - micro0000182
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/antibiotic_medium_1.yaml
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
  issue_key: cm001010-ph-precision
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Scalar pH 6.5 disagrees with source and retained pH 6.55
  description: Both layers retain exact pH 6.55 in preparation but scalar ph_value
    is 6.5. The discrepancy is bounded precision/representation loss rather than wholly
    absent pH.
  target_ids:
  - CultureMech:001010
  field_paths:
  - ph_value
  - preparation_steps[0].description
  evidence_ids:
  - ph
  - record
  - owner-0
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/antibiotic_medium_1.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: cm001010-generated-evidence-labels
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated target lacks later owner evidence and canonical label spelling
    differs
  description: The August merged target omits six October owner amount attachments,
    its references entry and four September primary term additions. Four owner term
    labels differ only by capitalization from live canonical labels. Reconciliation
    must first assess source-specific term support and historical evidence limits;
    copying later annotations is not automatic scientific approval.
  target_ids:
  - CultureMech:001010
  field_paths:
  - ingredients[*].evidence
  - ingredients[0:4].term
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - history-plan
  - history-metadata
  - foodon03315426
  - foodon03302088
  - micro0000178
  - micro0000182
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/antibiotic_medium_1.yaml
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
  description: Recover the exact cited source response or another exact primary with
    a stated denominator, preserve source batch masses and historical attachments,
    and qualify any unresolved normalization. Do not invent final volume or erase
    evidence because current access failed.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001010
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/antibiotic_medium_1.yaml
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
  description: Verify the exact material/product specifications or retain appropriately
    qualified unresolved grounding. Preserve source wording and supported tryptone
    identity; do not infer a replacement ID.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001010
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/antibiotic_medium_1.yaml
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
  description: Align the scalar with source precision and preserve the existing correct
    preparation sentence with exact evidence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001010
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/antibiotic_medium_1.yaml
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
  description: Correct verified maintained annotations, preserve original evidence/history,
    then regenerate under separate authorization and check exact evidence retention
    and canonical labels.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001010
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/antibiotic_medium_1.yaml
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
- Exact MediaDive 1532 returned HTTP 503 in the initial attempt and separately preserved
  retry. The cited original f1376f… response is not recovered; derivative local excerpts
  retain historical claims but cannot authenticate the full provider volume basis.
  Required formulation-provenance verification remains incomplete.
- Exact MediaDive 1532 returned HTTP 503 in the initial attempt and separately preserved
  retry. The cited original f1376f… response is not recovered; derivative local excerpts
  retain historical claims but cannot authenticate the full provider volume basis.
  Required formulation-provenance verification remains incomplete.
- The exact BD 226340 supplier page returned 403. The collection explicitly names
  the alternative product, but no independent supplier formulation or reconstitution
  dose is inferred.
- Historical amount evidence was read and matched to the exact local plan/report,
  not discarded. This partial review makes no claim that inaccessible provider history
  is false; it distinguishes primary batch-mass support from an unverified per-liter
  denominator. No typical sterilization or growth conditions were supplied.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-029
- generated-medium
```
