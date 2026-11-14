# Source and formulation review: alkalithermobacter_medium (CultureMech:001745)

- Review: 20261021T133540Z-culturemech-001745-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:27:16Z
- Finished UTC: 2026-10-21T13:35:40Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The primary DSMZ 616 resolves the DSM 8682 branch: carbonate 4.40 g/L and pH 9, unlike the base 5.30 g/L and pH 10. The generated record collapses these distinct identities and the KOMODO owner retains the wrong carbonate amount. Six later DSMZ owner evidence objects remain valid for their base claims. Sodium resazurin is grounded to the free acid. Current scientific comparison is complete despite optional historical KOMODO detail access failure.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 230; batch 023 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-two task batches contain 220 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 223 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001745 | data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml | generated | alkalithermobacter_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001745 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001745 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch023/230/strict.tsv |
| validate-terms | passed | True | CultureMech:001745 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001745 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001745 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo616_8682detail | unavailable | False | CultureMech:001745 | Exact KOMODO 616_8682 detail returned HTTP 403. The current primary explicitly resolves the strain-qualified carbonate/pH branch, and exact catalog identity is available. This optional historical-detail failure does not make current scientific comparison incomplete; historical import chronology remains unproved. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001745.

The four documented recipes completed; interpret the scope of each separately.

### Later maintained-owner evidence and generated snapshot

evidence: concern. Targets: CultureMech:001745.

Six DSMZ-owner amount claims have attached matching evidence and are verified for the base. Target and KOMODO lack these objects; the target predates the owner evidence update. Preserve all six complete objects and the owner reference/history; do not copy base carbonate evidence as support for the different DSM 8682 amount. Current merge code is not blamed for the older snapshot.

[{"field_path": "ingredients[0].evidence[0]", "evidence": {"reference": "https://mediadive.dsmz.de/rest/medium/616", "supports": "SUPPORT", "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2HPO4 x 2 H2O\",\n                        \"compound_id\": 181,\n                        \"amount\": 0.36,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.36,\n                        \"mmol_l\": 2.53594,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[0].concentration (Na2HPO4 x 2 H2O) in MediaDive medium 616; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=0.36; check: 0.36 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.36 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:27.985479+00:00; response SHA256=fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47."}}, {"field_path": "ingredients[1].evidence[0]", "evidence": {"reference": "https://mediadive.dsmz.de/rest/medium/616", "supports": "SUPPORT", "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.08,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 1.07311,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[1].concentration (KCl) in MediaDive medium 616; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=0.08; check: 0.08 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.08 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:27.985479+00:00; response SHA256=fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47."}}, {"field_path": "ingredients[5].evidence[0]", "evidence": {"reference": "https://mediadive.dsmz.de/rest/medium/616", "supports": "SUPPORT", "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 5.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.3,\n                        \"mmol_l\": 50.0057,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[5].concentration (Na2CO3) in MediaDive medium 616; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=5.3; check: 5.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 5.3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:27.985479+00:00; response SHA256=fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47."}}, {"field_path": "ingredients[6].evidence[0]", "evidence": {"reference": "https://mediadive.dsmz.de/rest/medium/616", "supports": "SUPPORT", "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 16.6519,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[6].concentration (D-Glucose) in MediaDive medium 616; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:27.985479+00:00; response SHA256=fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47."}}, {"field_path": "ingredients[7].evidence[0]", "evidence": {"reference": "https://mediadive.dsmz.de/rest/medium/616", "supports": "SUPPORT", "snippet": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.13872,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[7].concentration (L-Cysteine HCl x H2O) in MediaDive medium 616; locator=$.data.solutions[0].recipe[7]. Provider explicitly reports g_l=0.2; check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:27.985479+00:00; response SHA256=fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47."}}, {"field_path": "ingredients[8].evidence[0]", "evidence": {"reference": "https://mediadive.dsmz.de/rest/medium/616", "supports": "SUPPORT", "snippet": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.832702,\n                        \"optional\": 0\n                    }", "explanation": "Concentration evidence for ingredients[8].concentration (Na2S x 9 H2O) in MediaDive medium 616; locator=$.data.solutions[0].recipe[8]. Provider explicitly reports g_l=0.2; check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:27.985479+00:00; response SHA256=fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47."}}]

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001745.

23 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Na2HPO4 x 2 H2O main amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.36",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.36",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.36",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "0.36 g in the explicitly 1000 mL base recipe; local 0.36 g/L agrees.",
    "rationale": "Verified applies only to the DSMZ owner at its six attached-evidence positions. Target and KOMODO need claim evidence; the latter carbonate is wrong for its explicitly named variant. The primary branch changes only carbonate and pH, so other retained quantities are interpreted within that stated modification scope.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2HPO4 x 2 H2O\",\n                        \"compound_id\": 181,\n                        \"amount\": 0.36,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.36,\n                        \"mmol_l\": 2.53594,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      },
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1000 ml",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "KCl main amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.08",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.08",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.08",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "0.08 g in the explicitly 1000 mL base recipe; local 0.08 g/L agrees.",
    "rationale": "Verified applies only to the DSMZ owner at its six attached-evidence positions. Target and KOMODO need claim evidence; the latter carbonate is wrong for its explicitly named variant. The primary branch changes only carbonate and pH, so other retained quantities are interpreted within that stated modification scope.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.08,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 1.07311,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      },
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1000 ml",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Yeast extract main amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "5 g in the explicitly 1000 mL base recipe; local 5 g/L agrees.",
    "rationale": "Verified applies only to the DSMZ owner at its six attached-evidence positions. Target and KOMODO need claim evidence; the latter carbonate is wrong for its explicitly named variant. The primary branch changes only carbonate and pH, so other retained quantities are interpreted within that stated modification scope.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"OXOID\",\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      },
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1000 ml",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Tryptone main amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "10 g in the explicitly 1000 mL base recipe; local 10 g/L agrees.",
    "rationale": "Verified applies only to the DSMZ owner at its six attached-evidence positions. Target and KOMODO need claim evidence; the latter carbonate is wrong for its explicitly named variant. The primary branch changes only carbonate and pH, so other retained quantities are interpreted within that stated modification scope.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\": 71,\n                        \"attribute\": \"BD Bacto\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 140.687,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      },
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1000 ml",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Sodium resazurin main amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0005",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0005",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0005",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "0.50 mL of 0.1% w/v sodium-resazurin stock contributes 0.0005 g per explicitly 1000 mL main recipe; the local mass number agrees, but the sodium salt identifier needs correction.",
    "rationale": "Verified applies only to the DSMZ owner at its six attached-evidence positions. Target and KOMODO need claim evidence; the latter carbonate is wrong for its explicitly named variant. The primary branch changes only carbonate and pH, so other retained quantities are interpreted within that stated modification scope.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      },
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1000 ml",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Na2CO3 main amount",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5.3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5.3",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Base carbonate remains 5.30 g per explicitly 1000 mL; DSM 8682 owner requires 4.40 g/L, with branch pH 9.",
    "rationale": "Verified applies only to the DSMZ owner at its six attached-evidence positions. Target and KOMODO need claim evidence; the latter carbonate is wrong for its explicitly named variant. The primary branch changes only carbonate and pH, so other retained quantities are interpreted within that stated modification scope.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 5.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.3,\n                        \"mmol_l\": 50.0057,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      },
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1000 ml",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      },
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 explicit DSM 8682 branch",
        "exact_source_quote": "For DSM 8682: Reduce amount of carbonate to 4.40 g/l and adjust pH of complete medium\nto 9.0.",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "D-Glucose main amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "3 g in the explicitly 1000 mL base recipe; local 3 g/L agrees.",
    "rationale": "Verified applies only to the DSMZ owner at its six attached-evidence positions. Target and KOMODO need claim evidence; the latter carbonate is wrong for its explicitly named variant. The primary branch changes only carbonate and pH, so other retained quantities are interpreted within that stated modification scope.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 16.6519,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      },
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1000 ml",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "L-Cysteine HCl x H2O main amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "0.2 g in the explicitly 1000 mL base recipe; local 0.2 g/L agrees.",
    "rationale": "Verified applies only to the DSMZ owner at its six attached-evidence positions. Target and KOMODO need claim evidence; the latter carbonate is wrong for its explicitly named variant. The primary branch changes only carbonate and pH, so other retained quantities are interpreted within that stated modification scope.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.13872,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      },
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1000 ml",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Na2S x 9 H2O main amount",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "0.2 g in the explicitly 1000 mL base recipe; local 0.2 g/L agrees.",
    "rationale": "Verified applies only to the DSMZ owner at its six attached-evidence positions. Target and KOMODO need claim evidence; the latter carbonate is wrong for its explicitly named variant. The primary branch changes only carbonate and pH, so other retained quantities are interpreted within that stated modification scope.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.832702,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      },
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1000 ml",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Sodium-resazurin stock mass/volume percentage",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "0.1% w/v sodium-resazurin stock = 1 g/L stock, explicitly distinct from main concentration.",
    "rationale": "The primary provides the percentage basis here. Preserve sodium salt identity and stock stage; 1 g/L times 0.0005 L contributes 0.0005 g.",
    "source_snippets": [
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Sodium-resazurin stock receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "0.50 mL of the specified stock in the main recipe.",
    "rationale": "Preserve the original stock delivery representation alongside the supported final-medium mass; do not reinterpret it as 0.50 g or free-acid mass.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Main water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1000 mL listed distilled water, distinct from the explicitly labeled final-volume statement.",
    "rationale": "Water is a volume, not a solute g/L; do not infer a different final denominator by summing a stock dose into listed water when the primary explicitly supplies the main final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Explicit main final volume",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps[1]",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "preparation_steps[1]",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "preparation_steps[1]",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1000 mL final base recipe as explicitly stated by the current primary.",
    "rationale": "Retain source water and final-volume statements separately; this is declared source volume, not an independent measurement.",
    "source_snippets": [
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1000 ml",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Base final pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 10.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "ph_value",
        "stored": 10.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Base pH 10 applies to the target base and DSMZ owner; do not overwrite the explicitly modified owner pH 9.",
    "rationale": "Existing base pH and preparation match. Variant-specific pH is assessed separately and must not be collapsed into a synonym.",
    "source_snippets": [
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final pH: 10.0",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      },
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "adjust pH to 10",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "DSM 8682 carbonate branch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "For the DSM 8682 formulation only, carbonate 4.40 g/L. Keep base 5.30 g/L separate.",
    "rationale": "The exact current primary resolves this branch; the unavailable historical detail page does not prevent source comparison. This is a formulation qualifier, not an assertion of growth or a new taxonomy assignment.",
    "source_snippets": [
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 explicit DSM 8682 branch",
        "exact_source_quote": "For DSM 8682: Reduce amount of carbonate to 4.40 g/l and adjust pH of complete medium\nto 9.0.",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "DSM 8682 pH branch",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "ph_value",
        "stored": 9.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "For DSM 8682 only, complete-medium pH 9.0; existing KOMODO value is supported.",
    "rationale": "Preserve the correctly differing owner pH and represent the branch explicitly rather than claiming an exact source duplicate.",
    "source_snippets": [
      {
        "source_key": "dsmz616",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf",
        "source_locator": "Page 1 explicit DSM 8682 branch",
        "exact_source_quote": "For DSM 8682: Reduce amount of carbonate to 4.40 g/l and adjust pH of complete medium\nto 9.0.",
        "snapshot_sha256": "c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9",
        "parsed_text_sha256": "48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Nitrogen proportion",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "100% nitrogen for the named main and sterile stock stages.",
    "rationale": "Target/DSMZ already retain base procedure (evidence_only); KOMODO lacks preparation (add). Recover the source procedure with the explicit DSM 8682 pH override, never copy base pH 10 unqualified into that owner. No default autoclave cycle is supplied.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "100% N2 gas",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Main sparging duration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "30–45 minutes in main preparation.",
    "rationale": "Target/DSMZ already retain base procedure (evidence_only); KOMODO lacks preparation (add). Recover the source procedure with the explicit DSM 8682 pH override, never copy base pH 10 unqualified into that owner. No default autoclave cycle is supplied.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "30 - 45 min",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Adjustment stock normality",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "3 N NaOH for the base final pH adjustment; preserve exact source concentration and do not mistake it for a final-medium concentration.",
    "rationale": "Target/DSMZ already retain base procedure (evidence_only); KOMODO lacks preparation (add). Recover the source procedure with the explicit DSM 8682 pH override, never copy base pH 10 unqualified into that owner. No default autoclave cycle is supplied.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "3 N NaOH",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "NaOH receiving amount",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "NaOH receiving amount is unquantified.",
    "rationale": "The source gives a stock normality and pH endpoint, not a dose; preserve branch-specific pH.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "glucose separate stock strength/volume",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Glucose is delivered from a separate sterile anoxic stock; its stock strength and receiving volume are unquantified. The final main amount is separately specified.",
    "rationale": "Do not invent stock formulations or transfer unspecified sterilization conditions; preserve timing before use and source atmosphere.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "cysteine separate stock strength/volume",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Cysteine is delivered from a separate sterile anoxic stock; its stock strength and receiving volume are unquantified. The final main amount is separately specified.",
    "rationale": "Do not invent stock formulations or transfer unspecified sterilization conditions; preserve timing before use and source atmosphere.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "sulfide separate stock strength/volume",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH to 10 by adding sterile anoxic 3 N NaOH.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Sulfide is delivered from a separate sterile anoxic stock; its stock strength and receiving volume are unquantified. The final main amount is separately specified.",
    "rationale": "Do not invent stock formulations or transfer unspecified sterilization conditions; preserve timing before use and source atmosphere.",
    "source_snippets": [
      {
        "source_key": "mediadive616api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/616",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Before use add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas",
        "snapshot_sha256": "fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47"
      }
    ]
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:001745.

7 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 7/9 primary and 6/9 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 9: primary 77.78%; secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Source accession and maintained ownership

identity: concern. Targets: CultureMech:001745.

CM001745 base DSMZ 616 and CM006107 KOMODO 616_8682 are exact inspected contributors with resolving relationship paths. They are not formulation duplicates: the primary explicitly supplies the modified carbonate/pH branch. The target synonym and SOURCE_DUPLICATE relationship collapse that distinction.

### Claim-level amount support and source scope

evidence: concern. Targets: CultureMech:001745.

The DSMZ owner retains six exact attached amount evidence objects and a source reference that match the bound API bytes/hash. Target/KOMODO lack them; remaining amounts need claim-level evidence. Verified is limited to those six owner/base claims. The primary explicit 1000 mL final volume supports current main arithmetic, while variant carbonate/pH evidence is separately scoped.

### Preparation stages, source-only additions and owner differences

completeness: concern. Targets: CultureMech:001745.

Base main preparation is retained in target/DSMZ, including pre-use glucose/cysteine/sulfide stocks, nitrogen, duration and 3 N NaOH. KOMODO omits it; recovery must preserve its primary pH 9 override rather than copying base pH 10. Stock strengths/doses except the resazurin delivery are not specified.

### Composition and physical-state classification

scope: supported. Targets: CultureMech:001745.

COMPLEX/UNDEFINED and LIQUID are supported by yeast extract, tryptone and no gelling agent. Neither the title nor the source strain qualifier establishes phenotype, a new taxonomy assignment or experimental growth.

### Supplied forms and chemical specificity

grounding: concern. Targets: CultureMech:001745.

CHEBI:8806 has formula C12H7NO4 and no sodium; it does not represent the explicitly supplied sodium resazurin stock. Other asserted primary/current CHEBI-based secondary IDs and forms are supported at the stated source specificity, with no unresolved legacy secondary keys in these layers.

### Growth, organism taxonomy and graph claims

scope: not_applicable. Targets: CultureMech:001745.

The title, generic Microbial cultivation application and catalog Aerobic flags are not experimental growth or taxonomy evidence. No growth assertions, current taxonomy IDs or graph membership are added. Explicit source strain qualifiers remain formulation scope only.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:001745.

22 timestamp instances inspected; 2 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Authoritative inputs and current writer scope

provenance: concern. Targets: CultureMech:001745.

Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction.

## Findings

### f1: The resolved DSM 8682 formulation is collapsed into the base recipe

blocker / open / confirmed; issue key: collapsed-explicit-variant.

The target synonym and SOURCE_DUPLICATE child/parent claims collapse base DSMZ 616 with explicitly modified KOMODO 616_8682. The primary says carbonate 4.40 g/L and pH 9 for DSM 8682. KOMODO already has pH 9 but retains base carbonate 5.3 g/L; target/DSMZ base pH 10 and carbonate 5.3 remain appropriate only for the base.

### f2: Sodium resazurin is mapped to the sodium-free acid

major / open / confirmed; issue key: sodium-resazurin-form.

ingredients[4] names sodium resazurin and the source specifies a sodium-resazurin stock, while CHEBI:8806 is the neutral sodium-free C12H7NO4 form. The 0.0005 g/L mass calculation is supported by 0.1% w/v, 0.50 mL and explicit final volume; correct arithmetic does not validate salt identity.

### f3: The modified owner omits preparation and source delivery stages

major / open / confirmed; issue key: preparation-variant-and-source-stages.

KOMODO owner has no preparation while target/DSMZ retain the base procedure. All layers omit explicit water/final-volume and sodium-resazurin stock representation. Recovering base prose verbatim would introduce the wrong pH into the modified owner unless the primary override is applied.

### f4: The generated snapshot lacks six later base-owner evidence objects

minor / open / confirmed; issue key: later-owner-evidence-retention.

The maintained DSMZ owner has six complete October 7 evidence objects and a reference/history event; the target merged on August 6 lacks these later additions. Literal snippets and response hash match the bound API. This observed snapshot difference does not prove loss in current merge code.

### f5: Two KOMODO history timestamps lack valid timezone-aware form

minor / open / confirmed; issue key: historical-timestamp-shape.

Only the KOMODO owner retains one malformed import timestamp and one timezone-naive resolver timestamp; target and DSMZ-owner timestamps are well formed. These two of 22 inspected instances cannot establish exact historical source chronology.

## Recommended Actions And Acceptance Checks

### a1

Keep the exact normalized base and strain-qualified variant distinct, correct the modified owner carbonate to the explicit primary branch, and preserve its correct pH 9. Reassess SOURCE_DUPLICATE relationships and generated synonym/merge scope; do not alter the base carbonate using the variant value. Append clarification and regenerate only after owner correction and separate authorization.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify the exact sodium-salt ontology correspondence in both normalized contributors and replace the unsupported free-acid grounding only with validated evidence. Preserve source stock strength, delivery dose and supported mass; do not invent an unverified replacement ID or transfer free-acid molecular mass.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve existing base preparation, recover exact missing modified-owner context with its pH 9 branch, and retain explicit water, final volume and resazurin stock stages. Keep unspecified glucose/cysteine/sulfide stock strengths and NaOH dose unquantified; add no default sterilization parameters.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve all six complete evidence objects, their timestamps, hashes, reference and original history. Carry them into the corresponding base assertions during future authorized regeneration; attach separate primary evidence to variant carbonate/pH instead of transferring base support. Append clarification rather than rewriting prior curation events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Preserve original history, and append a clarification identifying the two exact malformed/naive KOMODO timestamps during authorized owner curation. Do not fabricate historical times or source sequence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch023/230/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch023/230/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml:1:id: CultureMech:001745<br>./data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml:1:id: CultureMech:001745<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch023/source-preflight-bound/230/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 11 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch023/source-preflight-bound/230/evidence-context-original.json; Complete frozen target/owners, source stages, exact secondary lookup and ignored-inclusive relationships | context_only | Full captured records re-read and compared by exact equality with fresh inspected records. Context is supporting provenance; exact bound primary/provider captures independently support scientific claims. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf; Page 1: explicit final volume, main table/procedure and DSM 8682 branch | supports | The primary explicitly gives final volume 1000 mL, base carbonate 5.30 g and pH 10; the DSM 8682 branch explicitly changes carbonate to 4.40 g/L and pH to 9. Sodium resazurin is added as 0.50 mL of 0.1% w/v stock. |
| provider | https://mediadive.dsmz.de/rest/medium/616; data.medium and solution 1322 full recipe/steps | supports | Exact provider base recipe declares 1000 mL and supports the six attached DSMZ-owner claim excerpts. It does not override the primary DSM 8682 branch or establish historical chronology. |
| komodo-catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact row accession 616_8682 | supports | The exact catalog identifies MEDIUM 616 MODIFIED FOR DSM 8682 and maps to DSMZ 616. It is not evidence that the modified recipe equals the base. Aerobic metadata is not a growth assertion. |
| komodo616_8682detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=616_8682; Preserved exact public retrieval result | context_only | Exact KOMODO 616_8682 detail returned HTTP 403. The current primary explicitly resolves the strain-qualified carbonate/pH branch, and exact catalog identity is available. This optional historical-detail failure does not make current scientific comparison incomplete; historical import chronology remains unproved. |
| existing-owner-evidence | data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml; Six exact later evidence objects at ingredients[0,1,5,6,7,8].evidence[0] | supports | All six original snippets literally match bound medium 616 JSON and every recorded response hash equals its captured SHA256. Their explanations restrict support to provider-declared base quantities, not secondary mapping or variants. They postdate the generated merge and remain intact. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch023/230/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91258 resolves to disodium hydrogenphosphate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91258": [{"label": "Na2HPO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml; data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.832078"}]}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-1 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact KOMODO 616_8682 detail returned HTTP 403. The current primary explicitly resolves the strain-qualified carbonate/pH branch, and exact catalog identity is available. This optional historical-detail failure does not make current scientific comparison incomplete; historical import chronology remains unproved.
- Only exact per-record bound captures are used. Current collection and provider differences do not establish their temporal order or the historical imported formulation.
- Source stock concentrations, receiving doses and listed water amounts do not independently establish a measured final mixture volume. No density, percent basis, exact hydration, default sterilization cycle or stock volume is invented.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T133540Z-culturemech-001745-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkalithermobacter_medium (CultureMech:001745)'
started_at: '2026-10-21T13:27:16Z'
finished_at: '2026-10-21T13:35:40Z'
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
summary: 'The primary DSMZ 616 resolves the DSM 8682 branch: carbonate 4.40 g/L and
  pH 9, unlike the base 5.30 g/L and pH 10. The generated record collapses these distinct
  identities and the KOMODO owner retains the wrong carbonate amount. Six later DSMZ
  owner evidence objects remain valid for their base claims. Sodium resazurin is grounded
  to the free acid. Current scientific comparison is complete despite optional historical
  KOMODO detail access failure.'
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
  - path: data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml
    sha256: 69c8d0870ed10db2a87bce0e6af0a1996902727def886dbe9c20e33ba0405e14
    role: target
  - path: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
    sha256: 397d9c35b5b7a9f2c3c0acaa8cc5225d3e895100db9514e1d2229dc06c6f5635
    role: context
  - path: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
    sha256: ba8938482d0c22799e11bc88bc6096c5cd0857250b71ab822025f584041fb17f
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
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
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
  selection: Task review 230; batch 023 item 10 of 10, selected in Python lexicographic
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
  - CultureMech:001745
targets:
- target_id: CultureMech:001745
  path: data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml
  label: alkalithermobacter_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch023/230/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch023/230/strict.tsv"
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001745
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
  - CultureMech:001745
- check_id: komodo616_8682detail-source-access
  name: 'Exact source content access: komodo616_8682detail'
  required: false
  status: unavailable
  summary: Exact KOMODO 616_8682 detail returned HTTP 403. The current primary explicitly
    resolves the strain-qualified carbonate/pH branch, and exact catalog identity
    is available. This optional historical-detail failure does not make current scientific
    comparison incomplete; historical import chronology remains unproved.
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - komodo616_8682detail-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:35:39Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:35:39Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:35:39Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:28:16.235132Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch023/230/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:28:17.791171Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch023/230/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:28:19.318316Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:28:20.336477Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:35:39Z'
  support: supports
  summary: './data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml:1:id: CultureMech:001745

    ./data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml:1:id: CultureMech:001745

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/source-preflight-bound/230/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:35:39Z'
  support: supports
  summary: 11 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: d9fd4725afc84b1e4ee3f373ba8208ea5e7322c155d0ca0d8aa15b24744f4e66
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/source-preflight-bound/230/evidence-context-original.json
  locator: Complete frozen target/owners, source stages, exact secondary lookup and
    ignored-inclusive relationships
  accessed_at: '2026-10-21T13:35:39Z'
  support: context_only
  summary: Full captured records re-read and compared by exact equality with fresh
    inspected records. Context is supporting provenance; exact bound primary/provider
    captures independently support scientific claims.
  snapshot_sha256: 2ec138780b597b9131df87d349dabe90c782a7355c57ecc08f13c575b8a6cd11
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf
  locator: 'Page 1: explicit final volume, main table/procedure and DSM 8682 branch'
  accessed_at: '2026-10-21T13:16:22.205205Z'
  support: supports
  summary: The primary explicitly gives final volume 1000 mL, base carbonate 5.30
    g and pH 10; the DSM 8682 branch explicitly changes carbonate to 4.40 g/L and
    pH to 9. Sodium resazurin is added as 0.50 mL of 0.1% w/v stock.
  snapshot_sha256: c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/616
  locator: data.medium and solution 1322 full recipe/steps
  accessed_at: '2026-10-21T13:16:20.995974Z'
  support: supports
  summary: Exact provider base recipe declares 1000 mL and supports the six attached
    DSMZ-owner claim excerpts. It does not override the primary DSM 8682 branch or
    establish historical chronology.
  snapshot_sha256: fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47
- evidence_id: komodo-catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact row accession 616_8682
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The exact catalog identifies MEDIUM 616 MODIFIED FOR DSM 8682 and maps
    to DSMZ 616. It is not evidence that the modified recipe equals the base. Aerobic
    metadata is not a growth assertion.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo616_8682detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=616_8682
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T13:16:20.702293Z'
  support: context_only
  summary: Exact KOMODO 616_8682 detail returned HTTP 403. The current primary explicitly
    resolves the strain-qualified carbonate/pH branch, and exact catalog identity
    is available. This optional historical-detail failure does not make current scientific
    comparison incomplete; historical import chronology remains unproved.
  snapshot_sha256: efeac945f6e7cd087c07e55bc1a98f21af9f7799256c3645d80b508682d9ad74
- evidence_id: existing-owner-evidence
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
  locator: Six exact later evidence objects at ingredients[0,1,5,6,7,8].evidence[0]
  accessed_at: '2026-10-21T13:35:39Z'
  support: supports
  summary: All six original snippets literally match bound medium 616 JSON and every
    recorded response hash equals its captured SHA256. Their explanations restrict
    support to provider-declared base quantities, not secondary mapping or variants.
    They postdate the generated merge and remain intact.
  snapshot_sha256: 397d9c35b5b7a9f2c3c0acaa8cc5225d3e895100db9514e1d2229dc06c6f5635
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/230/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:35:39Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 494db180da2c1e50e5aeb12883023080f80ebe1eeadc11f48ed281aa90b1f9ab
- evidence_id: chebi17634
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:33.425023Z'
  support: supports
  summary: CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
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
  accessed_at: '2026-10-21T13:35:39Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17634":
    [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634",
    "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:29377": [{"label": "Na2CO3",
    "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588":
    [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O",
    "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id":
    "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91258":
    [{"label": "Na2HPO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91258",
    "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml;
    data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:35:39Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml",
    "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:59.832078"}]}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:35:39Z'
  support: context_only
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:35:39Z'
  support: context_only
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:35:39Z'
  support: context_only
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:35:39Z'
  support: context_only
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: later-evidence
  area: evidence
  topic: Later maintained-owner evidence and generated snapshot
  outcome: concern
  summary: Six DSMZ-owner amount claims have attached matching evidence and are verified
    for the base. Target and KOMODO lack these objects; the target predates the owner
    evidence update. Preserve all six complete objects and the owner reference/history;
    do not copy base carbonate evidence as support for the different DSM 8682 amount.
    Current merge code is not blamed for the older snapshot.
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - record
  - owner-0
  - existing-owner-evidence
  - provider
  details: '[{"field_path": "ingredients[0].evidence[0]", "evidence": {"reference":
    "https://mediadive.dsmz.de/rest/medium/616", "supports": "SUPPORT", "snippet":
    "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Na2HPO4 x 2 H2O\",\n                        \"compound_id\": 181,\n                        \"amount\":
    0.36,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.36,\n                        \"mmol_l\": 2.53594,\n                        \"optional\":
    0\n                    }", "explanation": "Concentration evidence for ingredients[0].concentration
    (Na2HPO4 x 2 H2O) in MediaDive medium 616; locator=$.data.solutions[0].recipe[0].
    Provider explicitly reports g_l=0.36; check: 0.36 g * 1 g/g / (1000 ml / 1000
    ml per L) = 0.36 g/L. This supports the provider-declared main-recipe concentration,
    not an independently measured final volume, a stock composition, or a downstream
    assay dilution. Water alone does not establish final volume. Exact source ingredient
    labels/forms are matched; secondary ontology mappings are not validated by this
    evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved
    2026-10-07T12:16:27.985479+00:00; response SHA256=fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47."}},
    {"field_path": "ingredients[1].evidence[0]", "evidence": {"reference": "https://mediadive.dsmz.de/rest/medium/616",
    "supports": "SUPPORT", "snippet": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.08,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\":
    1.07311,\n                        \"optional\": 0\n                    }", "explanation":
    "Concentration evidence for ingredients[1].concentration (KCl) in MediaDive medium
    616; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=0.08;
    check: 0.08 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.08 g/L. This supports the
    provider-declared main-recipe concentration, not an independently measured final
    volume, a stock composition, or a downstream assay dilution. Water alone does
    not establish final volume. Exact source ingredient labels/forms are matched;
    secondary ontology mappings are not validated by this evidence. Additional exact
    value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:27.985479+00:00;
    response SHA256=fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47."}},
    {"field_path": "ingredients[5].evidence[0]", "evidence": {"reference": "https://mediadive.dsmz.de/rest/medium/616",
    "supports": "SUPPORT", "snippet": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 5.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.3,\n                        \"mmol_l\":
    50.0057,\n                        \"optional\": 0\n                    }", "explanation":
    "Concentration evidence for ingredients[5].concentration (Na2CO3) in MediaDive
    medium 616; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports
    g_l=5.3; check: 5.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 5.3 g/L. This supports
    the provider-declared main-recipe concentration, not an independently measured
    final volume, a stock composition, or a downstream assay dilution. Water alone
    does not establish final volume. Exact source ingredient labels/forms are matched;
    secondary ontology mappings are not validated by this evidence. Additional exact
    value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:27.985479+00:00;
    response SHA256=fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47."}},
    {"field_path": "ingredients[6].evidence[0]", "evidence": {"reference": "https://mediadive.dsmz.de/rest/medium/616",
    "supports": "SUPPORT", "snippet": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\":
    211,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    16.6519,\n                        \"optional\": 0\n                    }", "explanation":
    "Concentration evidence for ingredients[6].concentration (D-Glucose) in MediaDive
    medium 616; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports
    g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the
    provider-declared main-recipe concentration, not an independently measured final
    volume, a stock composition, or a downstream assay dilution. Water alone does
    not establish final volume. Exact source ingredient labels/forms are matched;
    secondary ontology mappings are not validated by this evidence. Additional exact
    value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:27.985479+00:00;
    response SHA256=fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47."}},
    {"field_path": "ingredients[7].evidence[0]", "evidence": {"reference": "https://mediadive.dsmz.de/rest/medium/616",
    "supports": "SUPPORT", "snippet": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.13872,\n                        \"optional\": 0\n                    }", "explanation":
    "Concentration evidence for ingredients[7].concentration (L-Cysteine HCl x H2O)
    in MediaDive medium 616; locator=$.data.solutions[0].recipe[7]. Provider explicitly
    reports g_l=0.2; check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This
    supports the provider-declared main-recipe concentration, not an independently
    measured final volume, a stock composition, or a downstream assay dilution. Water
    alone does not establish final volume. Exact source ingredient labels/forms are
    matched; secondary ontology mappings are not validated by this evidence. Additional
    exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:27.985479+00:00;
    response SHA256=fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47."}},
    {"field_path": "ingredients[8].evidence[0]", "evidence": {"reference": "https://mediadive.dsmz.de/rest/medium/616",
    "supports": "SUPPORT", "snippet": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.832702,\n                        \"optional\": 0\n                    }", "explanation":
    "Concentration evidence for ingredients[8].concentration (Na2S x 9 H2O) in MediaDive
    medium 616; locator=$.data.solutions[0].recipe[8]. Provider explicitly reports
    g_l=0.2; check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This supports
    the provider-declared main-recipe concentration, not an independently measured
    final volume, a stock composition, or a downstream assay dilution. Water alone
    does not establish final volume. Exact source ingredient labels/forms are matched;
    secondary ontology mappings are not validated by this evidence. Additional exact
    value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:27.985479+00:00;
    response SHA256=fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47."}}]'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 23 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Na2HPO4 x 2 H2O main amount\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.36\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.36\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\",\n    \
    \    \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.36\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"0.36 g in the explicitly 1000 mL base recipe; local 0.36 g/L agrees.\",\n\
    \    \"rationale\": \"Verified applies only to the DSMZ owner at its six attached-evidence\
    \ positions. Target and KOMODO need claim evidence; the latter carbonate is wrong\
    \ for its explicitly named variant. The primary branch changes only carbonate\
    \ and pH, so other retained quantities are interpreted within that stated modification\
    \ scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Na2HPO4 x 2 H2O\\\",\\n                        \\\
    \"compound_id\\\": 181,\\n                        \\\"amount\\\": 0.36,\\n   \
    \                     \\\"unit\\\": \\\"g\\\",\\n                        \\\"\
    g_l\\\": 0.36,\\n                        \\\"mmol_l\\\": 2.53594,\\n         \
    \               \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz616\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\",\n        \"\
    source_locator\": \"Page 1 header\",\n        \"exact_source_quote\": \"Final\
    \ volume: 1000 ml\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"KCl main amount\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.08\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.08\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\",\n    \
    \    \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.08\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"0.08 g in the explicitly 1000 mL base recipe; local 0.08 g/L agrees.\",\n\
    \    \"rationale\": \"Verified applies only to the DSMZ owner at its six attached-evidence\
    \ positions. Target and KOMODO need claim evidence; the latter carbonate is wrong\
    \ for its explicitly named variant. The primary branch changes only carbonate\
    \ and pH, so other retained quantities are interpreted within that stated modification\
    \ scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\
    \": 61,\\n                        \\\"amount\\\": 0.08,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.08,\\\
    n                        \\\"mmol_l\\\": 1.07311,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz616\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\"\
    ,\n        \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1000 ml\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"Yeast extract main amount\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\",\n    \
    \    \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"5 g in the explicitly 1000 mL base recipe; local 5 g/L agrees.\",\n    \"\
    rationale\": \"Verified applies only to the DSMZ owner at its six attached-evidence\
    \ positions. Target and KOMODO need claim evidence; the latter carbonate is wrong\
    \ for its explicitly named variant. The primary branch changes only carbonate\
    \ and pH, so other retained quantities are interpreted within that stated modification\
    \ scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"\
    compound_id\\\": 16,\\n                        \\\"attribute\\\": \\\"OXOID\\\"\
    ,\\n                        \\\"amount\\\": 5,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n            \
    \            \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz616\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\",\n        \"\
    source_locator\": \"Page 1 header\",\n        \"exact_source_quote\": \"Final\
    \ volume: 1000 ml\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"Tryptone main amount\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\",\n\
    \        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"10 g in the explicitly 1000 mL base recipe; local 10 g/L agrees.\",\n    \"\
    rationale\": \"Verified applies only to the DSMZ owner at its six attached-evidence\
    \ positions. Target and KOMODO need claim evidence; the latter carbonate is wrong\
    \ for its explicitly named variant. The primary branch changes only carbonate\
    \ and pH, so other retained quantities are interpreted within that stated modification\
    \ scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"Tryptone\\\",\\n                        \\\"compound_id\\\
    \": 71,\\n                        \\\"attribute\\\": \\\"BD Bacto\\\",\\n    \
    \                    \\\"amount\\\": 10,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n                   \
    \     \\\"mmol_l\\\": 140.687,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\
    \n      },\n      {\n        \"source_key\": \"dsmz616\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\",\n    \
    \    \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1000 ml\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"Sodium resazurin main amount\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0005\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0005\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0005\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"0.50 mL of 0.1% w/v sodium-resazurin stock contributes 0.0005 g per explicitly\
    \ 1000 mL main recipe; the local mass number agrees, but the sodium salt identifier\
    \ needs correction.\",\n    \"rationale\": \"Verified applies only to the DSMZ\
    \ owner at its six attached-evidence positions. Target and KOMODO need claim evidence;\
    \ the latter carbonate is wrong for its explicitly named variant. The primary\
    \ branch changes only carbonate and pH, so other retained quantities are interpreted\
    \ within that stated modification scope.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"mediadive616api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/616\",\n        \"source_locator\": \"$.data.solutions[0].recipe[4]\"\
    ,\n        \"exact_source_quote\": \"{\\n                        \\\"recipe_order\\\
    \": 5,\\n                        \\\"compound\\\": \\\"Sodium resazurin\\\",\\\
    n                        \\\"compound_id\\\": 1852,\\n                       \
    \ \\\"attribute\\\": \\\"0.1% w/v\\\",\\n                        \\\"amount\\\"\
    : 0.5,\\n                        \\\"unit\\\": \\\"ml\\\",\\n                \
    \        \\\"g_l\\\": 0.0005,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\
    \n      },\n      {\n        \"source_key\": \"dsmz616\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\",\n    \
    \    \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1000 ml\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"Na2CO3 main amount\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"5.3\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"verified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Base carbonate remains 5.30 g per explicitly 1000 mL; DSM 8682 owner requires\
    \ 4.40 g/L, with branch pH 9.\",\n    \"rationale\": \"Verified applies only to\
    \ the DSMZ owner at its six attached-evidence positions. Target and KOMODO need\
    \ claim evidence; the latter carbonate is wrong for its explicitly named variant.\
    \ The primary branch changes only carbonate and pH, so other retained quantities\
    \ are interpreted within that stated modification scope.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive616api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/616\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Na2CO3\\\",\\n                        \\\"compound_id\\\": 32,\\\
    n                        \\\"amount\\\": 5.3,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 5.3,\\n                \
    \        \\\"mmol_l\\\": 50.0057,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\
    \n      },\n      {\n        \"source_key\": \"dsmz616\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\",\n    \
    \    \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1000 ml\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      },\n      {\n        \"source_key\": \"dsmz616\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\",\n    \
    \    \"source_locator\": \"Page 1 explicit DSM 8682 branch\",\n        \"exact_source_quote\"\
    : \"For DSM 8682: Reduce amount of carbonate to 4.40 g/l and adjust pH of complete\
    \ medium\\nto 9.0.\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"D-Glucose main amount\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"verified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"3 g in the explicitly 1000 mL base recipe; local 3 g/L agrees.\",\n    \"\
    rationale\": \"Verified applies only to the DSMZ owner at its six attached-evidence\
    \ positions. Target and KOMODO need claim evidence; the latter carbonate is wrong\
    \ for its explicitly named variant. The primary branch changes only carbonate\
    \ and pH, so other retained quantities are interpreted within that stated modification\
    \ scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"D-Glucose\\\",\\n                        \\\"compound_id\\\
    \": 211,\\n                        \\\"amount\\\": 3,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n    \
    \                    \\\"mmol_l\\\": 16.6519,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\
    \n      },\n      {\n        \"source_key\": \"dsmz616\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\",\n    \
    \    \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1000 ml\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"L-Cysteine HCl x H2O main amount\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"verified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"0.2 g in the explicitly 1000 mL base recipe; local 0.2 g/L agrees.\",\n  \
    \  \"rationale\": \"Verified applies only to the DSMZ owner at its six attached-evidence\
    \ positions. Target and KOMODO need claim evidence; the latter carbonate is wrong\
    \ for its explicitly named variant. The primary branch changes only carbonate\
    \ and pH, so other retained quantities are interpreted within that stated modification\
    \ scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"L-Cysteine HCl x H2O\\\",\\n                    \
    \    \\\"compound_id\\\": 770,\\n                        \\\"amount\\\": 0.2,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.2,\\n                        \\\"mmol_l\\\": 1.13872,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz616\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\",\n        \"\
    source_locator\": \"Page 1 header\",\n        \"exact_source_quote\": \"Final\
    \ volume: 1000 ml\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Na2S x 9 H2O main amount\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"verified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"0.2 g in the explicitly 1000 mL base recipe; local 0.2 g/L agrees.\",\n  \
    \  \"rationale\": \"Verified applies only to the DSMZ owner at its six attached-evidence\
    \ positions. Target and KOMODO need claim evidence; the latter carbonate is wrong\
    \ for its explicitly named variant. The primary branch changes only carbonate\
    \ and pH, so other retained quantities are interpreted within that stated modification\
    \ scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Na2S x 9 H2O\\\",\\n                        \\\"\
    compound_id\\\": 54,\\n                        \\\"amount\\\": 0.2,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.2,\\n                        \\\"mmol_l\\\": 0.832702,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz616\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\",\n        \"\
    source_locator\": \"Page 1 header\",\n        \"exact_source_quote\": \"Final\
    \ volume: 1000 ml\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Sodium-resazurin stock mass/volume percentage\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"0.1% w/v sodium-resazurin stock = 1 g/L stock, explicitly distinct from main\
    \ concentration.\",\n    \"rationale\": \"The primary provides the percentage\
    \ basis here. Preserve sodium salt identity and stock stage; 1 g/L times 0.0005\
    \ L contributes 0.0005 g.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz616\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Sodium-resazurin stock receiving dose\",\n    \"decision\": \"add\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"0.50 mL of the specified stock in the main recipe.\",\n    \"rationale\":\
    \ \"Preserve the original stock delivery representation alongside the supported\
    \ final-medium mass; do not reinterpret it as 0.50 g or free-acid mass.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\
    \"compound_id\\\": 1852,\\n                        \\\"attribute\\\": \\\"0.1%\
    \ w/v\\\",\\n                        \\\"amount\\\": 0.5,\\n                 \
    \       \\\"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.0005,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"Main water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[9].concentration\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1000 mL listed distilled water, distinct from the explicitly labeled final-volume\
    \ statement.\",\n    \"rationale\": \"Water is a volume, not a solute g/L; do\
    \ not infer a different final denominator by summing a stock dose into listed\
    \ water when the primary explicitly supplies the main final volume.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n    \
    \    \"source_locator\": \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 10,\\n                 \
    \       \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 1000,\\n     \
    \                   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"Explicit main final volume\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1]\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1]\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1]\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1000 mL final base recipe as explicitly stated by the current primary.\",\n\
    \    \"rationale\": \"Retain source water and final-volume statements separately;\
    \ this is declared source volume, not an independent measurement.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz616\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\",\n        \"\
    source_locator\": \"Page 1 header\",\n        \"exact_source_quote\": \"Final\
    \ volume: 1000 ml\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Base final pH\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 10.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 10.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"Base pH 10 applies\
    \ to the target base and DSMZ owner; do not overwrite the explicitly modified\
    \ owner pH 9.\",\n    \"rationale\": \"Existing base pH and preparation match.\
    \ Variant-specific pH is assessed separately and must not be collapsed into a\
    \ synonym.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz616\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\"\
    ,\n        \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\"\
    : \"Final pH: 10.0\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      },\n      {\n        \"source_key\": \"mediadive616api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"adjust\
    \ pH to 10\",\n        \"snapshot_sha256\": \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"DSM 8682 carbonate branch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"For the DSM 8682 formulation only, carbonate 4.40 g/L. Keep base 5.30 g/L\
    \ separate.\",\n    \"rationale\": \"The exact current primary resolves this branch;\
    \ the unavailable historical detail page does not prevent source comparison. This\
    \ is a formulation qualifier, not an assertion of growth or a new taxonomy assignment.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz616\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\"\
    ,\n        \"source_locator\": \"Page 1 explicit DSM 8682 branch\",\n        \"\
    exact_source_quote\": \"For DSM 8682: Reduce amount of carbonate to 4.40 g/l and\
    \ adjust pH of complete medium\\nto 9.0.\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"DSM 8682 pH branch\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"For DSM 8682 only, complete-medium pH 9.0; existing KOMODO value is supported.\"\
    ,\n    \"rationale\": \"Preserve the correctly differing owner pH and represent\
    \ the branch explicitly rather than claiming an exact source duplicate.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz616\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium616.pdf\"\
    ,\n        \"source_locator\": \"Page 1 explicit DSM 8682 branch\",\n        \"\
    exact_source_quote\": \"For DSM 8682: Reduce amount of carbonate to 4.40 g/l and\
    \ adjust pH of complete medium\\nto 9.0.\",\n        \"snapshot_sha256\": \"c36b25388c59f809efaa7d811df7cc49457719a2a76a1c474640326ecf3cc4c9\"\
    ,\n        \"parsed_text_sha256\": \"48837231211bf863641925e3235e16367e487962256128c13d0e4b9767504a69\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"Nitrogen proportion\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"100% nitrogen for the named main and sterile stock stages.\",\n    \"rationale\"\
    : \"Target/DSMZ already retain base procedure (evidence_only); KOMODO lacks preparation\
    \ (add). Recover the source procedure with the explicit DSM 8682 pH override,\
    \ never copy base pH 10 unqualified into that owner. No default autoclave cycle\
    \ is supplied.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive616api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n      \
    \  \"exact_source_quote\": \"100% N2 gas\",\n        \"snapshot_sha256\": \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"Main sparging duration\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"30–45 minutes in main preparation.\",\n    \"rationale\": \"Target/DSMZ already\
    \ retain base procedure (evidence_only); KOMODO lacks preparation (add). Recover\
    \ the source procedure with the explicit DSM 8682 pH override, never copy base\
    \ pH 10 unqualified into that owner. No default autoclave cycle is supplied.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n        \"\
    exact_source_quote\": \"30 - 45 min\",\n        \"snapshot_sha256\": \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"Adjustment stock normality\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"3 N NaOH for the base final pH adjustment; preserve exact source concentration\
    \ and do not mistake it for a final-medium concentration.\",\n    \"rationale\"\
    : \"Target/DSMZ already retain base procedure (evidence_only); KOMODO lacks preparation\
    \ (add). Recover the source procedure with the explicit DSM 8682 pH override,\
    \ never copy base pH 10 unqualified into that owner. No default autoclave cycle\
    \ is supplied.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive616api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n      \
    \  \"exact_source_quote\": \"3 N NaOH\",\n        \"snapshot_sha256\": \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"NaOH receiving amount\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"NaOH receiving amount is unquantified.\",\n    \"rationale\": \"The source\
    \ gives a stock normality and pH endpoint, not a dose; preserve branch-specific\
    \ pH.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n        \"\
    exact_source_quote\": \"adjust pH to 10 by adding sterile anoxic 3 N NaOH.\",\n\
    \        \"snapshot_sha256\": \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"glucose separate stock strength/volume\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Glucose is delivered from a separate sterile anoxic stock; its stock strength\
    \ and receiving volume are unquantified. The final main amount is separately specified.\"\
    ,\n    \"rationale\": \"Do not invent stock formulations or transfer unspecified\
    \ sterilization conditions; preserve timing before use and source atmosphere.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n        \"\
    exact_source_quote\": \"Before use add glucose, cysteine and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas\",\n        \"snapshot_sha256\"\
    : \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"cysteine separate stock strength/volume\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Cysteine is delivered from a separate sterile anoxic stock; its stock strength\
    \ and receiving volume are unquantified. The final main amount is separately specified.\"\
    ,\n    \"rationale\": \"Do not invent stock formulations or transfer unspecified\
    \ sterilization conditions; preserve timing before use and source atmosphere.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n        \"\
    exact_source_quote\": \"Before use add glucose, cysteine and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas\",\n        \"snapshot_sha256\"\
    : \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"sulfide separate stock strength/volume\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALITHERMOBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except carbonate, glucose, cysteine and sulfide) and\
    \ sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\
    \ carbonate, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Before use add glucose, cysteine and sulfide\
    \ from sterile anoxic stock solutions prepared under 100% N2 gas and adjust pH\
    \ to 10 by adding sterile anoxic 3 N NaOH.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Sulfide is delivered from a separate sterile anoxic stock; its stock strength\
    \ and receiving volume are unquantified. The final main amount is separately specified.\"\
    ,\n    \"rationale\": \"Do not invent stock formulations or transfer unspecified\
    \ sterilization conditions; preserve timing before use and source atmosphere.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive616api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/616\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n        \"\
    exact_source_quote\": \"Before use add glucose, cysteine and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas\",\n        \"snapshot_sha256\"\
    : \"fd0d426cc642a474eb890a539f49ae7b2fcba66d1624c785772a2132db718c47\"\n     \
    \ }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '7 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 7/9 primary and 6/9 secondary
    instances; all asserted current mediaingredientmech_chebi_term keys have exact
    pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs
    and labels do not establish correct source grounding.'
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi17634
  - chebi29377
  - chebi32588
  - chebi76209
  - chebi8806
  - chebi91248
  - chebi91258
  details: 'Instance coverage on a 0–100 percent scale, denominator 9: primary 77.78%;
    secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Source accession and maintained ownership
  outcome: concern
  summary: 'CM001745 base DSMZ 616 and CM006107 KOMODO 616_8682 are exact inspected
    contributors with resolving relationship paths. They are not formulation duplicates:
    the primary explicitly supplies the modified carbonate/pH branch. The target synonym
    and SOURCE_DUPLICATE relationship collapse that distinction.'
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - record
  - id-search
  - bound-owner-context
  - owner-0
  - owner-1
  - primary
  - provider
  - komodo-catalog
- assessment_id: evidence
  area: evidence
  topic: Claim-level amount support and source scope
  outcome: concern
  summary: The DSMZ owner retains six exact attached amount evidence objects and a
    source reference that match the bound API bytes/hash. Target/KOMODO lack them;
    remaining amounts need claim-level evidence. Verified is limited to those six
    owner/base claims. The primary explicit 1000 mL final volume supports current
    main arithmetic, while variant carbonate/pH evidence is separately scoped.
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - komodo-catalog
  - existing-owner-evidence
- assessment_id: preparation
  area: completeness
  topic: Preparation stages, source-only additions and owner differences
  outcome: concern
  summary: Base main preparation is retained in target/DSMZ, including pre-use glucose/cysteine/sulfide
    stocks, nitrogen, duration and 3 N NaOH. KOMODO omits it; recovery must preserve
    its primary pH 9 override rather than copying base pH 10. Stock strengths/doses
    except the resazurin delivery are not specified.
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - komodo-catalog
- assessment_id: classification
  area: scope
  topic: Composition and physical-state classification
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID are supported by yeast extract, tryptone and
    no gelling agent. Neither the title nor the source strain qualifier establishes
    phenotype, a new taxonomy assignment or experimental growth.
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - record
  - primary
  - provider
  - komodo-catalog
- assessment_id: forms
  area: grounding
  topic: Supplied forms and chemical specificity
  outcome: concern
  summary: CHEBI:8806 has formula C12H7NO4 and no sodium; it does not represent the
    explicitly supplied sodium resazurin stock. Other asserted primary/current CHEBI-based
    secondary IDs and forms are supported at the stated source specificity, with no
    unresolved legacy secondary keys in these layers.
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - record
  - primary
  - provider
  - komodo-catalog
- assessment_id: growth
  area: scope
  topic: Growth, organism taxonomy and graph claims
  outcome: not_applicable
  summary: The title, generic Microbial cultivation application and catalog Aerobic
    flags are not experimental growth or taxonomy evidence. No growth assertions,
    current taxonomy IDs or graph membership are added. Explicit source strain qualifiers
    remain formulation scope only.
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - record
  - primary
  - provider
  - komodo-catalog
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 22 timestamp instances inspected; 2 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: writer
  area: provenance
  topic: Authoritative inputs and current writer scope
  outcome: concern
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  target_ids:
  - CultureMech:001745
  evidence_ids:
  - record
  - writer-0
  - writer-1
  - writer-2
  - writer-3
findings:
- finding_id: f1
  issue_key: collapsed-explicit-variant
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The resolved DSM 8682 formulation is collapsed into the base recipe
  description: The target synonym and SOURCE_DUPLICATE child/parent claims collapse
    base DSMZ 616 with explicitly modified KOMODO 616_8682. The primary says carbonate
    4.40 g/L and pH 9 for DSM 8682. KOMODO already has pH 9 but retains base carbonate
    5.3 g/L; target/DSMZ base pH 10 and carbonate 5.3 remain appropriate only for
    the base.
  target_ids:
  - CultureMech:001745
  field_paths:
  - variant_children
  - synonyms
  - ingredients[5].concentration
  - ph_value
  - merged_from
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - komodo-catalog
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
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
  issue_key: sodium-resazurin-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium resazurin is mapped to the sodium-free acid
  description: ingredients[4] names sodium resazurin and the source specifies a sodium-resazurin
    stock, while CHEBI:8806 is the neutral sodium-free C12H7NO4 form. The 0.0005 g/L
    mass calculation is supported by 0.1% w/v, 0.50 mL and explicit final volume;
    correct arithmetic does not validate salt identity.
  target_ids:
  - CultureMech:001745
  field_paths:
  - ingredients[4].term
  - ingredients[4].preferred_term
  evidence_ids:
  - record
  - primary
  - provider
  - chebi8806
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: preparation-variant-and-source-stages
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The modified owner omits preparation and source delivery stages
  description: KOMODO owner has no preparation while target/DSMZ retain the base procedure.
    All layers omit explicit water/final-volume and sodium-resazurin stock representation.
    Recovering base prose verbatim would introduce the wrong pH into the modified
    owner unless the primary override is applied.
  target_ids:
  - CultureMech:001745
  field_paths:
  - preparation_steps
  - solutions
  - ingredients
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3.5
  normalization_reason: P3.5 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: later-owner-evidence-retention
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The generated snapshot lacks six later base-owner evidence objects
  description: The maintained DSMZ owner has six complete October 7 evidence objects
    and a reference/history event; the target merged on August 6 lacks these later
    additions. Literal snippets and response hash match the bound API. This observed
    snapshot difference does not prove loss in current merge code.
  target_ids:
  - CultureMech:001745
  field_paths:
  - ingredients
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - existing-owner-evidence
  - provider
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: historical-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Two KOMODO history timestamps lack valid timezone-aware form
  description: Only the KOMODO owner retains one malformed import timestamp and one
    timezone-naive resolver timestamp; target and DSMZ-owner timestamps are well formed.
    These two of 22 inspected instances cannot establish exact historical source chronology.
  target_ids:
  - CultureMech:001745
  field_paths:
  - curation_history
  evidence_ids:
  - record
  - owner-1
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
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
  description: Keep the exact normalized base and strain-qualified variant distinct,
    correct the modified owner carbonate to the explicit primary branch, and preserve
    its correct pH 9. Reassess SOURCE_DUPLICATE relationships and generated synonym/merge
    scope; do not alter the base carbonate using the variant value. Append clarification
    and regenerate only after owner correction and separate authorization.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001745
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
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
  description: Verify the exact sodium-salt ontology correspondence in both normalized
    contributors and replace the unsupported free-acid grounding only with validated
    evidence. Preserve source stock strength, delivery dose and supported mass; do
    not invent an unverified replacement ID or transfer free-acid molecular mass.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001745
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
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
  description: Preserve existing base preparation, recover exact missing modified-owner
    context with its pH 9 branch, and retain explicit water, final volume and resazurin
    stock stages. Keep unspecified glucose/cysteine/sulfide stock strengths and NaOH
    dose unquantified; add no default sterilization parameters.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001745
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
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
  description: Preserve all six complete evidence objects, their timestamps, hashes,
    reference and original history. Carry them into the corresponding base assertions
    during future authorized regeneration; attach separate primary evidence to variant
    carbonate/pH instead of transferring base support. Append clarification rather
    than rewriting prior curation events.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001745
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
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
  description: Preserve original history, and append a clarification identifying the
    two exact malformed/naive KOMODO timestamps during authorized owner curation.
    Do not fabricate historical times or source sequence.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001745
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalithermobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_616_modified_for_dsm_8682.yaml
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
- Exact KOMODO 616_8682 detail returned HTTP 403. The current primary explicitly resolves
  the strain-qualified carbonate/pH branch, and exact catalog identity is available.
  This optional historical-detail failure does not make current scientific comparison
  incomplete; historical import chronology remains unproved.
- Only exact per-record bound captures are used. Current collection and provider differences
  do not establish their temporal order or the historical imported formulation.
- Source stock concentrations, receiving doses and listed water amounts do not independently
  establish a measured final mixture volume. No density, percent basis, exact hydration,
  default sterilization cycle or stock volume is invented.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-023
- generated-medium
```
