# Source and formulation review: acidicaldus_medium (CultureMech:003552)

- Review: 20261021T105256Z-culturemech-003552-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T10:48:41Z
- Finished UTC: 2026-10-21T10:52:56Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 1038 supports the seven-ingredient formulation, supplied chemical forms and pH. The generated target and KOMODO owner omit the primary preparation sequence and concentration evidence retained by the DSMZ owner. Historical KOMODO detail access remains unavailable; source-catalog identity is independently supported.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 161; batch 017 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding sixteen task batches contain 160 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 162 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003552 | data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml | generated | acidicaldus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003552 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003552 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/161/strict.tsv |
| validate-terms | passed | True | CultureMech:003552 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003552 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003552 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo1038 | unavailable | False | CultureMech:003552 | Exact KOMODO MediaInfo=1038 capture returned HTTP 403. The catalog and DSMZ PDF/API independently establish the mapped current recipe; the precise historical KOMODO detail payload remains unavailable. This optional provenance limit does not prevent assessment of the current DSMZ formulation. The catalog header Is Aerobic and exact 1038 row false support the local oxygen annotation as source metadata only, not as physiological growth evidence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003552.

The four documented recipes completed; interpret the scope of each separately.

### Both maintained contributors and source-duplicate linkage

identity: supported. Targets: CultureMech:003552.

The target resolves to KOMODO 1038 and DSMZ 1038 with seven matching ingredient values, pH 2.5 and reciprocal SOURCE_DUPLICATE paths/IDs. Exact ingredient signatures do not establish equivalent preparation or evidence coverage. No organism/strain growth assertion is inferred from the title or generic application.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003552.

27 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "input": "target",
    "field_path": "ingredients[0].concentration",
    "ingredient": "(NH4)2SO4",
    "existing": {
      "value": "0.45",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.45,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.45 g / (1000 ml / 1000 ml per L) = 0.45 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact (NH4)2SO4 table row",
        "exact_source_quote": "(NH4)2SO4 0.45 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.45,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.45,\n                        \"mmol_l\": 3.40548,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml",
    "field_path": "ingredients[0].concentration",
    "ingredient": "(NH4)2SO4",
    "existing": {
      "value": "0.45",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.45,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.45 g / (1000 ml / 1000 ml per L) = 0.45 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact (NH4)2SO4 table row",
        "exact_source_quote": "(NH4)2SO4 0.45 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.45,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.45,\n                        \"mmol_l\": 3.40548,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidicaldus_medium.yaml",
    "field_path": "ingredients[0].concentration",
    "ingredient": "(NH4)2SO4",
    "existing": {
      "value": "0.45",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.45,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; retain existing exact evidence.",
    "calculation": "0.45 g / (1000 ml / 1000 ml per L) = 0.45 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact (NH4)2SO4 table row",
        "exact_source_quote": "(NH4)2SO4 0.45 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.45,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.45,\n                        \"mmol_l\": 3.40548,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ingredients[1].concentration",
    "ingredient": "KCl",
    "existing": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.05,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.05 g / (1000 ml / 1000 ml per L) = 0.05 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact KCl table row",
        "exact_source_quote": "KCl 0.05 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.670691,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml",
    "field_path": "ingredients[1].concentration",
    "ingredient": "KCl",
    "existing": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.05,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.05 g / (1000 ml / 1000 ml per L) = 0.05 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact KCl table row",
        "exact_source_quote": "KCl 0.05 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.670691,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidicaldus_medium.yaml",
    "field_path": "ingredients[1].concentration",
    "ingredient": "KCl",
    "existing": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.05,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; retain existing exact evidence.",
    "calculation": "0.05 g / (1000 ml / 1000 ml per L) = 0.05 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact KCl table row",
        "exact_source_quote": "KCl 0.05 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.670691,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ingredients[2].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "existing": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.5 g / (1000 ml / 1000 ml per L) = 0.5 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact MgSO4 x 7 H2O table row",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml",
    "field_path": "ingredients[2].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "existing": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.5 g / (1000 ml / 1000 ml per L) = 0.5 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact MgSO4 x 7 H2O table row",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidicaldus_medium.yaml",
    "field_path": "ingredients[2].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "existing": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; retain existing exact evidence.",
    "calculation": "0.5 g / (1000 ml / 1000 ml per L) = 0.5 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact MgSO4 x 7 H2O table row",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ingredients[3].concentration",
    "ingredient": "KH2PO4",
    "existing": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.05,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.05 g / (1000 ml / 1000 ml per L) = 0.05 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact KH2PO4 table row",
        "exact_source_quote": "KH2PO4 0.05 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.367417,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml",
    "field_path": "ingredients[3].concentration",
    "ingredient": "KH2PO4",
    "existing": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.05,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.05 g / (1000 ml / 1000 ml per L) = 0.05 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact KH2PO4 table row",
        "exact_source_quote": "KH2PO4 0.05 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.367417,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidicaldus_medium.yaml",
    "field_path": "ingredients[3].concentration",
    "ingredient": "KH2PO4",
    "existing": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.05,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; retain existing exact evidence.",
    "calculation": "0.05 g / (1000 ml / 1000 ml per L) = 0.05 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact KH2PO4 table row",
        "exact_source_quote": "KH2PO4 0.05 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.367417,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ingredients[4].concentration",
    "ingredient": "Ca(NO3)2 x 4 H2O",
    "existing": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.02,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.02 g / (1000 ml / 1000 ml per L) = 0.02 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact Ca(NO3)2 x 4 H2O table row",
        "exact_source_quote": "Ca(NO3)2 x 4 H2O 0.02 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Ca(NO3)2 x 4 H2O\",\n                        \"compound_id\": 213,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0846923,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml",
    "field_path": "ingredients[4].concentration",
    "ingredient": "Ca(NO3)2 x 4 H2O",
    "existing": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.02,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.02 g / (1000 ml / 1000 ml per L) = 0.02 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact Ca(NO3)2 x 4 H2O table row",
        "exact_source_quote": "Ca(NO3)2 x 4 H2O 0.02 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Ca(NO3)2 x 4 H2O\",\n                        \"compound_id\": 213,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0846923,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidicaldus_medium.yaml",
    "field_path": "ingredients[4].concentration",
    "ingredient": "Ca(NO3)2 x 4 H2O",
    "existing": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.02,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; retain existing exact evidence.",
    "calculation": "0.02 g / (1000 ml / 1000 ml per L) = 0.02 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact Ca(NO3)2 x 4 H2O table row",
        "exact_source_quote": "Ca(NO3)2 x 4 H2O 0.02 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Ca(NO3)2 x 4 H2O\",\n                        \"compound_id\": 213,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0846923,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ingredients[5].concentration",
    "ingredient": "D-Glucose",
    "existing": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 1,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "1 g / (1000 ml / 1000 ml per L) = 1 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact D-Glucose table row",
        "exact_source_quote": "D-Glucose 1.00 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml",
    "field_path": "ingredients[5].concentration",
    "ingredient": "D-Glucose",
    "existing": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 1,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "1 g / (1000 ml / 1000 ml per L) = 1 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact D-Glucose table row",
        "exact_source_quote": "D-Glucose 1.00 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidicaldus_medium.yaml",
    "field_path": "ingredients[5].concentration",
    "ingredient": "D-Glucose",
    "existing": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 1,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; retain existing exact evidence.",
    "calculation": "1 g / (1000 ml / 1000 ml per L) = 1 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact D-Glucose table row",
        "exact_source_quote": "D-Glucose 1.00 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ingredients[6].concentration",
    "ingredient": "Yeast extract",
    "existing": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.2,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.2 g / (1000 ml / 1000 ml per L) = 0.2 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact Yeast extract table row",
        "exact_source_quote": "Yeast extract (OXOID) 0.20 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"OXOID\",\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml",
    "field_path": "ingredients[6].concentration",
    "ingredient": "Yeast extract",
    "existing": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.2,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.2 g / (1000 ml / 1000 ml per L) = 0.2 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact Yeast extract table row",
        "exact_source_quote": "Yeast extract (OXOID) 0.20 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"OXOID\",\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidicaldus_medium.yaml",
    "field_path": "ingredients[6].concentration",
    "ingredient": "Yeast extract",
    "existing": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks after autoclaving",
    "source_amount": {
      "value": 0.2,
      "unit": "g"
    },
    "basis": "Provider explicitly reports volume 1000 ml and g_l; not independently measured final volume after unquantified stock additions.",
    "proposed": "Retain provider-declared value; attach exact claim-level source evidence.",
    "calculation": "0.2 g / (1000 ml / 1000 ml per L) = 0.2 g/L on the provider-declared basis only.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, exact Yeast extract table row",
        "exact_source_quote": "Yeast extract (OXOID) 0.20 g",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"OXOID\",\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "target and both owners",
    "field_path": "ingredients (source-only water basis)",
    "decision": "add",
    "source_stage": "Main-recipe solvent before subsequent sterile stock additions",
    "source_amount": {
      "value": 1000,
      "unit": "ml"
    },
    "proposed": "Represent the solvent quantity and preparation basis; do not infer a measured final volume.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, distilled-water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      },
      {
        "source_key": "mediadive1038api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1038",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ph_value",
    "existing": 2.5,
    "decision": "evidence_only",
    "source_stage": "Adjustment before dispensing and autoclaving",
    "proposed": "Retain target pH 2.5 and attach stage-specific evidence. This does not assert measured final pH.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, preparation paragraph",
        "exact_source_quote": "adjust pH to 2.5",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml",
    "field_path": "ph_value",
    "existing": 2.5,
    "decision": "evidence_only",
    "source_stage": "Adjustment before dispensing and autoclaving",
    "proposed": "Retain target pH 2.5 and attach stage-specific evidence. This does not assert measured final pH.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, preparation paragraph",
        "exact_source_quote": "adjust pH to 2.5",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidicaldus_medium.yaml",
    "field_path": "ph_value",
    "existing": 2.5,
    "decision": "evidence_only",
    "source_stage": "Adjustment before dispensing and autoclaving",
    "proposed": "Retain target pH 2.5 and attach stage-specific evidence. This does not assert measured final pH.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, preparation paragraph",
        "exact_source_quote": "adjust pH to 2.5",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      }
    ]
  },
  {
    "input": "target and both owners",
    "field_path": "solutions / preparation_steps (sterile stock context)",
    "ingredient": "D-Glucose",
    "decision": "not_quantified",
    "source_stage": "After autoclaving",
    "proposed": "Preserve the specified main-recipe mass and separate sterile-stock addition stage; stock concentration and addition volume are not supplied and must not be guessed.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, final preparation sentence",
        "exact_source_quote": "Add glucose and yeast extract after autoclaving\nfrom sterile stock solutions.",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      }
    ]
  },
  {
    "input": "target and both owners",
    "field_path": "solutions / preparation_steps (sterile stock context)",
    "ingredient": "Yeast extract",
    "decision": "not_quantified",
    "source_stage": "After autoclaving",
    "proposed": "Preserve the specified main-recipe mass and separate sterile-stock addition stage; stock concentration and addition volume are not supplied and must not be guessed.",
    "source_snippets": [
      {
        "source_key": "dsmz1038",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf",
        "source_locator": "PDF p.1, final preparation sentence",
        "exact_source_quote": "Add glucose and yeast extract after autoclaving\nfrom sterile stock solutions.",
        "snapshot_sha256": "92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708",
        "parsed_text_sha256": "d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461"
      }
    ]
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: supported. Targets: CultureMech:003552.

6 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 6/7 primary and 6/7 secondary instances; all asserted secondary keys have exact pinned MIM rows. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 7: primary 85.71%; secondary 85.71%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Source-specific chemical forms and complex ingredient

grounding: supported. Targets: CultureMech:003552.

The six asserted pure-compound forms match the primary: ammonium sulfate, KCl, magnesium sulfate heptahydrate, KH2PO4, calcium nitrate tetrahydrate and D-glucose. Yeast extract is an unresolved complex mixture rather than a pure molecule; OXOID is a source product attribute absent locally. No unsupported hydrate, stoichiometry or organism inference was added.

### Medium category, physical state and applications

scope: supported. Targets: CultureMech:003552.

COMPLEX / SEMI_DEFINED is consistent with defined salts plus yeast extract; LIQUID is consistent with the source and no gelling ingredient. Bacterial category and generic microbial-cultivation application are retained as corpus metadata, not species-specific growth evidence. The KOMODO catalog header Is Aerobic and exact 1038 row false support Aerobic: No as imported source metadata. It is not treated as independently established physiology or an oxygen requirement.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003552.

23 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

## Findings

### f1: Generated target omits the source-supported preparation sequence

major / open / confirmed; issue key: culturemech.003552.preparation-omitted.

The DSMZ owner retains the full primary instruction to withhold glucose and yeast extract during autoclaving and add them later from sterile stocks. The KOMODO owner and generated target contain no preparation_steps. Ingredient equality and SOURCE_DUPLICATE links do not preserve this material stage boundary. Water 1000 ml and the OXOID yeast-extract attribute also remain source-only; no absent stock dose or autoclave setting can be invented.

### f2: Exact owner concentration evidence is absent from the generated layer

minor / open / confirmed; issue key: culturemech.003552.claim-evidence-gap.

Six DSMZ-owner ingredient evidence objects exactly match the current API bytes and correctly qualify the 1000 ml provider basis. The target and KOMODO owner contain none of those claim attachments; yeast extract and pH lack such evidence in all layers. Correct values without attached evidence are evidence_only, not verified. Source bibliography alone does not establish every claim.

### f3: KOMODO-derived historical timestamps are malformed or lack a timezone

minor / open / confirmed; issue key: culturemech.003552.history-timestamp-shape.

The target and KOMODO owner each retain 2026-01-27T01:15:01.fZ and timezone-naive 2026-02-03T11:19:12.401541. These four instances prevent a precise timestamp interpretation; deterministic recipe checks did not reject them. No true historical timezone or fractional seconds were recovered.

## Recommended Actions And Acceptance Checks

### a1

Maintain source-scoped preparation and solvent/product context in the normalized contributors; preserve the two sterile-stock stages and use the maintained merge workflow to retain them in the derived target.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve existing DSMZ evidence verbatim; add missing bounded evidence and use source-compatible merge behavior rather than treating another contributor’s evidence as inherited.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve historical bytes and append a provenance clarification describing the malformed and timezone-naive values; do not fabricate corrected timestamps.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/acidicaldus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch017/161/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/161/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml:1:id: CultureMech:003552<br>./data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml:1:id: CultureMech:003552<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch017/source-preflight-bound/161/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 10 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf; PDF page 1, complete ingredient table and preparation paragraph | supports | All eight source rows and complete preparation read; no stock strength, stock dose, autoclave temperature or duration supplied. |
| provider | https://mediadive.dsmz.de/rest/medium/1038; $.data.medium; $.data.solutions[0] (2106), all recipe rows, volume and steps | supports | Exact DSMZ source identity, explicit main-recipe volume 1000 ml and provider g_l values inspected. Raw hash equals the six existing DSMZ-owner evidence objects. |
| komodo-catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact MediaInfo=1038 table row and source-link column | supports | Exact KOMODO 1038 title, pH and DSMZ 1038 link resolve. Catalog metadata is not direct historical formulation content. |
| komodo1038-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1038; Preserved exact public retrieval result | context_only | Exact KOMODO MediaInfo=1038 capture returned HTTP 403. The catalog and DSMZ PDF/API independently establish the mapped current recipe; the precise historical KOMODO detail payload remains unavailable. This optional provenance limit does not prevent assessment of the current DSMZ formulation. The catalog header Is Aerobic and exact 1038 row false support the local oxygen annotation as source metadata only, not as physiological growth evidence. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch017/161/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86159 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86159; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86159 resolves to calcium nitrate tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86159": [{"label": "Ca(NO3)2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml; data/normalized_yaml/bacterial/acidicaldus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:12.401541"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:12.401541"}]}, {"input": "data/normalized_yaml/bacterial/acidicaldus_medium.yaml", "events": 7, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source import, composition enrichment and formulation-aware merge code read as maintenance context. No historical replay or regeneration was run; the August generated artifact predates October owner evidence and retains KOMODO-specific metadata. |
| writer-1 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source import, composition enrichment and formulation-aware merge code read as maintenance context. No historical replay or regeneration was run; the August generated artifact predates October owner evidence and retains KOMODO-specific metadata. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source import, composition enrichment and formulation-aware merge code read as maintenance context. No historical replay or regeneration was run; the August generated artifact predates October owner evidence and retains KOMODO-specific metadata. |
| writer-3 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source import, composition enrichment and formulation-aware merge code read as maintenance context. No historical replay or regeneration was run; the August generated artifact predates October owner evidence and retains KOMODO-specific metadata. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact KOMODO MediaInfo=1038 capture returned HTTP 403. The catalog and DSMZ PDF/API independently establish the mapped current recipe; the precise historical KOMODO detail payload remains unavailable. This optional provenance limit does not prevent assessment of the current DSMZ formulation. The catalog header Is Aerobic and exact 1038 row false support the local oxygen annotation as source metadata only, not as physiological growth evidence.
- No strain, taxon, growth range, oxygen requirement or optimal condition is established by the medium title, catalog flags or generic application. DSMZ does not quantify the sterile stock strengths/doses or autoclave settings; no such values were inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T105256Z-culturemech-003552-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidicaldus_medium (CultureMech:003552)'
started_at: '2026-10-21T10:48:41Z'
finished_at: '2026-10-21T10:52:56Z'
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
summary: DSMZ 1038 supports the seven-ingredient formulation, supplied chemical forms
  and pH. The generated target and KOMODO owner omit the primary preparation sequence
  and concentration evidence retained by the DSMZ owner. Historical KOMODO detail
  access remains unavailable; source-catalog identity is independently supported.
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
  - path: data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml
    sha256: c90005645eb865bcfcd8532745eade22efa5be18ce4e61596589498b20cbeb89
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml
    sha256: 37db94c80f50f3c7a7bf192331d93b667faddef93dc73473e19184f76b4b295d
    role: context
  - path: data/normalized_yaml/bacterial/acidicaldus_medium.yaml
    sha256: 5d00962c449b3119fa62ab3aad7178c4fc8d358e5d8be9200cdd319b942fe3c3
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
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
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
  - path: scripts/propose_media_variant_links.py
    sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
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
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 161; batch 017 item 1 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding sixteen task batches
    contain 160 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 162 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003552
targets:
- target_id: CultureMech:003552
  path: data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml
  label: acidicaldus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidicaldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003552
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch017/161/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/161/strict.tsv"
  target_ids:
  - CultureMech:003552
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003552
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003552
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
  - CultureMech:003552
- check_id: komodo1038-source-access
  name: 'Exact source content access: komodo1038'
  required: false
  status: unavailable
  summary: Exact KOMODO MediaInfo=1038 capture returned HTTP 403. The catalog and
    DSMZ PDF/API independently establish the mapped current recipe; the precise historical
    KOMODO detail payload remains unavailable. This optional provenance limit does
    not prevent assessment of the current DSMZ formulation. The catalog header Is
    Aerobic and exact 1038 row false support the local oxygen annotation as source
    metadata only, not as physiological growth evidence.
  target_ids:
  - CultureMech:003552
  evidence_ids:
  - komodo1038-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:52:54Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:52:54Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/acidicaldus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:52:54Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:03.256987Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch017/161/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:04.510959Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/161/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:06.476233Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:07.468938Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T10:52:54Z'
  support: supports
  summary: './data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml:1:id: CultureMech:003552

    ./data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml:1:id: CultureMech:003552

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/source-preflight-bound/161/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T10:52:54Z'
  support: supports
  summary: 10 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 19174d62622ba2816398c2a8a72c2441a116d7ace867a108ad543c4c90f540eb
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf
  locator: PDF page 1, complete ingredient table and preparation paragraph
  accessed_at: '2026-10-21T10:33:40.369150Z'
  support: supports
  summary: All eight source rows and complete preparation read; no stock strength,
    stock dose, autoclave temperature or duration supplied.
  snapshot_sha256: 92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1038
  locator: $.data.medium; $.data.solutions[0] (2106), all recipe rows, volume and
    steps
  accessed_at: '2026-10-21T10:33:38.860542Z'
  support: supports
  summary: Exact DSMZ source identity, explicit main-recipe volume 1000 ml and provider
    g_l values inspected. Raw hash equals the six existing DSMZ-owner evidence objects.
  snapshot_sha256: 71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f
- evidence_id: komodo-catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact MediaInfo=1038 table row and source-link column
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Exact KOMODO 1038 title, pH and DSMZ 1038 link resolve. Catalog metadata
    is not direct historical formulation content.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1038'\
    \ >1038</a></TD>\n\t\t\t\t\t<TD>ACIDICALDUS medium</TD>\n\t\t\t\t\t<TD> 2.5</TD>\n\
    \t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\
    <TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo1038-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1038
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T10:33:38.859824Z'
  support: context_only
  summary: Exact KOMODO MediaInfo=1038 capture returned HTTP 403. The catalog and
    DSMZ PDF/API independently establish the mapped current recipe; the precise historical
    KOMODO detail payload remains unavailable. This optional provenance limit does
    not prevent assessment of the current DSMZ formulation. The catalog header Is
    Aerobic and exact 1038 row false support the local oxygen annotation as source
    metadata only, not as physiological growth evidence.
  snapshot_sha256: b775986b7bf40e5d2d3ebaf9b42a3ffb7bc75013b86af919c350886556a5e14f
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/161/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T10:52:54Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 2cb0425e53c185494566e3ae15f558dcacff74fd59bec4b3d903bdc11b10898e
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
- evidence_id: chebi86159
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86159
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T10:33:40.461439Z'
  support: supports
  summary: CHEBI:86159 resolves to calcium nitrate tetrahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: d2b0e9caef5876c00ed00136113d600d34a071b137bdd8c661c734ad5435682f
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T10:52:54Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17634":
    [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634",
    "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:31795": [{"label": "MgSO4 x
    7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type":
    "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id":
    "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946":
    [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946",
    "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86159":
    [{"label": "Ca(NO3)2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86159",
    "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml;
    data/normalized_yaml/bacterial/acidicaldus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T10:52:54Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:12.401541"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:12.401541"}]}, {"input": "data/normalized_yaml/bacterial/acidicaldus_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:52:54Z'
  support: context_only
  summary: Current source import, composition enrichment and formulation-aware merge
    code read as maintenance context. No historical replay or regeneration was run;
    the August generated artifact predates October owner evidence and retains KOMODO-specific
    metadata.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:52:54Z'
  support: context_only
  summary: Current source import, composition enrichment and formulation-aware merge
    code read as maintenance context. No historical replay or regeneration was run;
    the August generated artifact predates October owner evidence and retains KOMODO-specific
    metadata.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:52:54Z'
  support: context_only
  summary: Current source import, composition enrichment and formulation-aware merge
    code read as maintenance context. No historical replay or regeneration was run;
    the August generated artifact predates October owner evidence and retains KOMODO-specific
    metadata.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:52:54Z'
  support: context_only
  summary: Current source import, composition enrichment and formulation-aware merge
    code read as maintenance context. No historical replay or regeneration was run;
    the August generated artifact predates October owner evidence and retains KOMODO-specific
    metadata.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003552
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Both maintained contributors and source-duplicate linkage
  outcome: supported
  summary: The target resolves to KOMODO 1038 and DSMZ 1038 with seven matching ingredient
    values, pH 2.5 and reciprocal SOURCE_DUPLICATE paths/IDs. Exact ingredient signatures
    do not establish equivalent preparation or evidence coverage. No organism/strain
    growth assertion is inferred from the title or generic application.
  target_ids:
  - CultureMech:003552
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - komodo-catalog
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 27 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003552
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"input\": \"target\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"ingredient\": \"(NH4)2SO4\",\n    \"existing\": {\n      \"value\": \"\
    0.45\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"DSMZ 1038 main-recipe amount; glucose and yeast extract\
    \ are added from sterile stocks after autoclaving\",\n    \"source_amount\": {\n\
    \      \"value\": 0.45,\n      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider\
    \ explicitly reports volume 1000 ml and g_l; not independently measured final\
    \ volume after unquantified stock additions.\",\n    \"proposed\": \"Retain provider-declared\
    \ value; attach exact claim-level source evidence.\",\n    \"calculation\": \"\
    0.45 g / (1000 ml / 1000 ml per L) = 0.45 g/L on the provider-declared basis only.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1038\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, exact (NH4)2SO4 table row\",\n     \
    \   \"exact_source_quote\": \"(NH4)2SO4 0.45 g\",\n        \"snapshot_sha256\"\
    : \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\",\n    \
    \    \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 0.45,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.45,\\n \
    \                       \\\"mmol_l\\\": 3.40548,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"ingredient\":\
    \ \"(NH4)2SO4\",\n    \"existing\": {\n      \"value\": \"0.45\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile\
    \ stocks after autoclaving\",\n    \"source_amount\": {\n      \"value\": 0.45,\n\
    \      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; attach\
    \ exact claim-level source evidence.\",\n    \"calculation\": \"0.45 g / (1000\
    \ ml / 1000 ml per L) = 0.45 g/L on the provider-declared basis only.\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1038\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, exact (NH4)2SO4 table row\",\n     \
    \   \"exact_source_quote\": \"(NH4)2SO4 0.45 g\",\n        \"snapshot_sha256\"\
    : \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\",\n    \
    \    \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 0.45,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.45,\\n \
    \                       \\\"mmol_l\\\": 3.40548,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidicaldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"ingredient\":\
    \ \"(NH4)2SO4\",\n    \"existing\": {\n      \"value\": \"0.45\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\":\
    \ \"DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile\
    \ stocks after autoclaving\",\n    \"source_amount\": {\n      \"value\": 0.45,\n\
    \      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; retain\
    \ existing exact evidence.\",\n    \"calculation\": \"0.45 g / (1000 ml / 1000\
    \ ml per L) = 0.45 g/L on the provider-declared basis only.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, exact (NH4)2SO4 table row\",\n        \"exact_source_quote\"\
    : \"(NH4)2SO4 0.45 g\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 0.45,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.45,\\n \
    \                       \\\"mmol_l\\\": 3.40548,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ingredients[1].concentration\",\n    \"ingredient\": \"KCl\",\n    \"existing\"\
    : {\n      \"value\": \"0.05\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"DSMZ 1038 main-recipe amount; glucose\
    \ and yeast extract are added from sterile stocks after autoclaving\",\n    \"\
    source_amount\": {\n      \"value\": 0.05,\n      \"unit\": \"g\"\n    },\n  \
    \  \"basis\": \"Provider explicitly reports volume 1000 ml and g_l; not independently\
    \ measured final volume after unquantified stock additions.\",\n    \"proposed\"\
    : \"Retain provider-declared value; attach exact claim-level source evidence.\"\
    ,\n    \"calculation\": \"0.05 g / (1000 ml / 1000 ml per L) = 0.05 g/L on the\
    \ provider-declared basis only.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz1038\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, exact KCl table row\",\n        \"exact_source_quote\"\
    : \"KCl 0.05 g\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.05,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\n         \
    \               \\\"mmol_l\\\": 0.670691,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[1].concentration\",\n    \"ingredient\":\
    \ \"KCl\",\n    \"existing\": {\n      \"value\": \"0.05\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile\
    \ stocks after autoclaving\",\n    \"source_amount\": {\n      \"value\": 0.05,\n\
    \      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; attach\
    \ exact claim-level source evidence.\",\n    \"calculation\": \"0.05 g / (1000\
    \ ml / 1000 ml per L) = 0.05 g/L on the provider-declared basis only.\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1038\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, exact KCl table row\",\n        \"exact_source_quote\"\
    : \"KCl 0.05 g\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.05,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\n         \
    \               \\\"mmol_l\\\": 0.670691,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidicaldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[1].concentration\",\n    \"ingredient\":\
    \ \"KCl\",\n    \"existing\": {\n      \"value\": \"0.05\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\": \"DSMZ\
    \ 1038 main-recipe amount; glucose and yeast extract are added from sterile stocks\
    \ after autoclaving\",\n    \"source_amount\": {\n      \"value\": 0.05,\n   \
    \   \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; retain\
    \ existing exact evidence.\",\n    \"calculation\": \"0.05 g / (1000 ml / 1000\
    \ ml per L) = 0.05 g/L on the provider-declared basis only.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, exact KCl table row\",\n        \"exact_source_quote\"\
    : \"KCl 0.05 g\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.05,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\n         \
    \               \\\"mmol_l\\\": 0.670691,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ingredients[2].concentration\",\n    \"ingredient\": \"MgSO4 x 7 H2O\",\n    \"\
    existing\": {\n      \"value\": \"0.5\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"decision\": \"evidence_only\",\n    \"source_stage\": \"DSMZ 1038 main-recipe\
    \ amount; glucose and yeast extract are added from sterile stocks after autoclaving\"\
    ,\n    \"source_amount\": {\n      \"value\": 0.5,\n      \"unit\": \"g\"\n  \
    \  },\n    \"basis\": \"Provider explicitly reports volume 1000 ml and g_l; not\
    \ independently measured final volume after unquantified stock additions.\",\n\
    \    \"proposed\": \"Retain provider-declared value; attach exact claim-level\
    \ source evidence.\",\n    \"calculation\": \"0.5 g / (1000 ml / 1000 ml per L)\
    \ = 0.5 g/L on the provider-declared basis only.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, exact MgSO4 x 7 H2O table row\",\n        \"\
    exact_source_quote\": \"MgSO4 x 7 H2O 0.50 g\",\n        \"snapshot_sha256\":\
    \ \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\",\n    \
    \    \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n  \
    \                      \\\"mmol_l\\\": 2.02859,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[2].concentration\",\n    \"ingredient\":\
    \ \"MgSO4 x 7 H2O\",\n    \"existing\": {\n      \"value\": \"0.5\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile\
    \ stocks after autoclaving\",\n    \"source_amount\": {\n      \"value\": 0.5,\n\
    \      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; attach\
    \ exact claim-level source evidence.\",\n    \"calculation\": \"0.5 g / (1000\
    \ ml / 1000 ml per L) = 0.5 g/L on the provider-declared basis only.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz1038\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, exact MgSO4 x 7 H2O table row\",\n \
    \       \"exact_source_quote\": \"MgSO4 x 7 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\",\n    \
    \    \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n  \
    \                      \\\"mmol_l\\\": 2.02859,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidicaldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[2].concentration\",\n    \"ingredient\":\
    \ \"MgSO4 x 7 H2O\",\n    \"existing\": {\n      \"value\": \"0.5\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\"\
    : \"DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile\
    \ stocks after autoclaving\",\n    \"source_amount\": {\n      \"value\": 0.5,\n\
    \      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; retain\
    \ existing exact evidence.\",\n    \"calculation\": \"0.5 g / (1000 ml / 1000\
    \ ml per L) = 0.5 g/L on the provider-declared basis only.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, exact MgSO4 x 7 H2O table row\",\n        \"\
    exact_source_quote\": \"MgSO4 x 7 H2O 0.50 g\",\n        \"snapshot_sha256\":\
    \ \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\",\n    \
    \    \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n  \
    \                      \\\"mmol_l\\\": 2.02859,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ingredients[3].concentration\",\n    \"ingredient\": \"KH2PO4\",\n    \"existing\"\
    : {\n      \"value\": \"0.05\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"DSMZ 1038 main-recipe amount; glucose\
    \ and yeast extract are added from sterile stocks after autoclaving\",\n    \"\
    source_amount\": {\n      \"value\": 0.05,\n      \"unit\": \"g\"\n    },\n  \
    \  \"basis\": \"Provider explicitly reports volume 1000 ml and g_l; not independently\
    \ measured final volume after unquantified stock additions.\",\n    \"proposed\"\
    : \"Retain provider-declared value; attach exact claim-level source evidence.\"\
    ,\n    \"calculation\": \"0.05 g / (1000 ml / 1000 ml per L) = 0.05 g/L on the\
    \ provider-declared basis only.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz1038\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, exact KH2PO4 table row\",\n        \"\
    exact_source_quote\": \"KH2PO4 0.05 g\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.05,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\n         \
    \               \\\"mmol_l\\\": 0.367417,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[3].concentration\",\n    \"ingredient\":\
    \ \"KH2PO4\",\n    \"existing\": {\n      \"value\": \"0.05\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile\
    \ stocks after autoclaving\",\n    \"source_amount\": {\n      \"value\": 0.05,\n\
    \      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; attach\
    \ exact claim-level source evidence.\",\n    \"calculation\": \"0.05 g / (1000\
    \ ml / 1000 ml per L) = 0.05 g/L on the provider-declared basis only.\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1038\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, exact KH2PO4 table row\",\n        \"\
    exact_source_quote\": \"KH2PO4 0.05 g\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.05,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\n         \
    \               \\\"mmol_l\\\": 0.367417,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidicaldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[3].concentration\",\n    \"ingredient\":\
    \ \"KH2PO4\",\n    \"existing\": {\n      \"value\": \"0.05\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\":\
    \ \"DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile\
    \ stocks after autoclaving\",\n    \"source_amount\": {\n      \"value\": 0.05,\n\
    \      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; retain\
    \ existing exact evidence.\",\n    \"calculation\": \"0.05 g / (1000 ml / 1000\
    \ ml per L) = 0.05 g/L on the provider-declared basis only.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, exact KH2PO4 table row\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.05 g\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.05,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\n         \
    \               \\\"mmol_l\\\": 0.367417,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ingredients[4].concentration\",\n    \"ingredient\": \"Ca(NO3)2 x 4 H2O\",\n \
    \   \"existing\": {\n      \"value\": \"0.02\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\": \"DSMZ 1038\
    \ main-recipe amount; glucose and yeast extract are added from sterile stocks\
    \ after autoclaving\",\n    \"source_amount\": {\n      \"value\": 0.02,\n   \
    \   \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; attach\
    \ exact claim-level source evidence.\",\n    \"calculation\": \"0.02 g / (1000\
    \ ml / 1000 ml per L) = 0.02 g/L on the provider-declared basis only.\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1038\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, exact Ca(NO3)2 x 4 H2O table row\",\n\
    \        \"exact_source_quote\": \"Ca(NO3)2 x 4 H2O 0.02 g\",\n        \"snapshot_sha256\"\
    : \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\",\n    \
    \    \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Ca(NO3)2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 213,\\n                        \\\"amount\\\": 0.02,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\\
    n                        \\\"mmol_l\\\": 0.0846923,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\n     \
    \ }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[4].concentration\",\n    \"ingredient\":\
    \ \"Ca(NO3)2 x 4 H2O\",\n    \"existing\": {\n      \"value\": \"0.02\",\n   \
    \   \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"\
    source_stage\": \"DSMZ 1038 main-recipe amount; glucose and yeast extract are\
    \ added from sterile stocks after autoclaving\",\n    \"source_amount\": {\n \
    \     \"value\": 0.02,\n      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider\
    \ explicitly reports volume 1000 ml and g_l; not independently measured final\
    \ volume after unquantified stock additions.\",\n    \"proposed\": \"Retain provider-declared\
    \ value; attach exact claim-level source evidence.\",\n    \"calculation\": \"\
    0.02 g / (1000 ml / 1000 ml per L) = 0.02 g/L on the provider-declared basis only.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1038\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, exact Ca(NO3)2 x 4 H2O table row\",\n\
    \        \"exact_source_quote\": \"Ca(NO3)2 x 4 H2O 0.02 g\",\n        \"snapshot_sha256\"\
    : \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\",\n    \
    \    \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Ca(NO3)2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 213,\\n                        \\\"amount\\\": 0.02,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\\
    n                        \\\"mmol_l\\\": 0.0846923,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\n     \
    \ }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidicaldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[4].concentration\",\n    \"ingredient\":\
    \ \"Ca(NO3)2 x 4 H2O\",\n    \"existing\": {\n      \"value\": \"0.02\",\n   \
    \   \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\"\
    : \"DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile\
    \ stocks after autoclaving\",\n    \"source_amount\": {\n      \"value\": 0.02,\n\
    \      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; retain\
    \ existing exact evidence.\",\n    \"calculation\": \"0.02 g / (1000 ml / 1000\
    \ ml per L) = 0.02 g/L on the provider-declared basis only.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, exact Ca(NO3)2 x 4 H2O table row\",\n       \
    \ \"exact_source_quote\": \"Ca(NO3)2 x 4 H2O 0.02 g\",\n        \"snapshot_sha256\"\
    : \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\",\n    \
    \    \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Ca(NO3)2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 213,\\n                        \\\"amount\\\": 0.02,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\\
    n                        \\\"mmol_l\\\": 0.0846923,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\n     \
    \ }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"ingredients[5].concentration\"\
    ,\n    \"ingredient\": \"D-Glucose\",\n    \"existing\": {\n      \"value\": \"\
    1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"DSMZ 1038 main-recipe amount; glucose and yeast extract\
    \ are added from sterile stocks after autoclaving\",\n    \"source_amount\": {\n\
    \      \"value\": 1,\n      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider\
    \ explicitly reports volume 1000 ml and g_l; not independently measured final\
    \ volume after unquantified stock additions.\",\n    \"proposed\": \"Retain provider-declared\
    \ value; attach exact claim-level source evidence.\",\n    \"calculation\": \"\
    1 g / (1000 ml / 1000 ml per L) = 1 g/L on the provider-declared basis only.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1038\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, exact D-Glucose table row\",\n     \
    \   \"exact_source_quote\": \"D-Glucose 1.00 g\",\n        \"snapshot_sha256\"\
    : \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\",\n    \
    \    \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"D-Glucose\\\",\\n                        \\\"compound_id\\\"\
    : 211,\\n                        \\\"amount\\\": 1,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n      \
    \                  \\\"mmol_l\\\": 5.55062,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[5].concentration\",\n    \"ingredient\":\
    \ \"D-Glucose\",\n    \"existing\": {\n      \"value\": \"1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile\
    \ stocks after autoclaving\",\n    \"source_amount\": {\n      \"value\": 1,\n\
    \      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; attach\
    \ exact claim-level source evidence.\",\n    \"calculation\": \"1 g / (1000 ml\
    \ / 1000 ml per L) = 1 g/L on the provider-declared basis only.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, exact D-Glucose table row\",\n        \"exact_source_quote\"\
    : \"D-Glucose 1.00 g\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"D-Glucose\\\",\\n                        \\\"compound_id\\\"\
    : 211,\\n                        \\\"amount\\\": 1,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n      \
    \                  \\\"mmol_l\\\": 5.55062,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidicaldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[5].concentration\",\n    \"ingredient\":\
    \ \"D-Glucose\",\n    \"existing\": {\n      \"value\": \"1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\":\
    \ \"DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile\
    \ stocks after autoclaving\",\n    \"source_amount\": {\n      \"value\": 1,\n\
    \      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; retain\
    \ existing exact evidence.\",\n    \"calculation\": \"1 g / (1000 ml / 1000 ml\
    \ per L) = 1 g/L on the provider-declared basis only.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, exact D-Glucose table row\",\n        \"exact_source_quote\"\
    : \"D-Glucose 1.00 g\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"D-Glucose\\\",\\n                        \\\"compound_id\\\"\
    : 211,\\n                        \\\"amount\\\": 1,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n      \
    \                  \\\"mmol_l\\\": 5.55062,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ingredients[6].concentration\",\n    \"ingredient\": \"Yeast extract\",\n    \"\
    existing\": {\n      \"value\": \"0.2\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"decision\": \"evidence_only\",\n    \"source_stage\": \"DSMZ 1038 main-recipe\
    \ amount; glucose and yeast extract are added from sterile stocks after autoclaving\"\
    ,\n    \"source_amount\": {\n      \"value\": 0.2,\n      \"unit\": \"g\"\n  \
    \  },\n    \"basis\": \"Provider explicitly reports volume 1000 ml and g_l; not\
    \ independently measured final volume after unquantified stock additions.\",\n\
    \    \"proposed\": \"Retain provider-declared value; attach exact claim-level\
    \ source evidence.\",\n    \"calculation\": \"0.2 g / (1000 ml / 1000 ml per L)\
    \ = 0.2 g/L on the provider-declared basis only.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, exact Yeast extract table row\",\n        \"\
    exact_source_quote\": \"Yeast extract (OXOID) 0.20 g\",\n        \"snapshot_sha256\"\
    : \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\",\n    \
    \    \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"attribute\\\": \\\"OXOID\\\",\\n       \
    \                 \\\"amount\\\": 0.2,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\n     \
    \ }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[6].concentration\",\n    \"ingredient\":\
    \ \"Yeast extract\",\n    \"existing\": {\n      \"value\": \"0.2\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile\
    \ stocks after autoclaving\",\n    \"source_amount\": {\n      \"value\": 0.2,\n\
    \      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; attach\
    \ exact claim-level source evidence.\",\n    \"calculation\": \"0.2 g / (1000\
    \ ml / 1000 ml per L) = 0.2 g/L on the provider-declared basis only.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz1038\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, exact Yeast extract table row\",\n \
    \       \"exact_source_quote\": \"Yeast extract (OXOID) 0.20 g\",\n        \"\
    snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"attribute\\\": \\\"OXOID\\\",\\n       \
    \                 \\\"amount\\\": 0.2,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\n     \
    \ }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidicaldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[6].concentration\",\n    \"ingredient\":\
    \ \"Yeast extract\",\n    \"existing\": {\n      \"value\": \"0.2\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"DSMZ 1038 main-recipe amount; glucose and yeast extract are added from sterile\
    \ stocks after autoclaving\",\n    \"source_amount\": {\n      \"value\": 0.2,\n\
    \      \"unit\": \"g\"\n    },\n    \"basis\": \"Provider explicitly reports volume\
    \ 1000 ml and g_l; not independently measured final volume after unquantified\
    \ stock additions.\",\n    \"proposed\": \"Retain provider-declared value; attach\
    \ exact claim-level source evidence.\",\n    \"calculation\": \"0.2 g / (1000\
    \ ml / 1000 ml per L) = 0.2 g/L on the provider-declared basis only.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz1038\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, exact Yeast extract table row\",\n \
    \       \"exact_source_quote\": \"Yeast extract (OXOID) 0.20 g\",\n        \"\
    snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"attribute\\\": \\\"OXOID\\\",\\n       \
    \                 \\\"amount\\\": 0.2,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\n     \
    \ }\n    ]\n  },\n  {\n    \"input\": \"target and both owners\",\n    \"field_path\"\
    : \"ingredients (source-only water basis)\",\n    \"decision\": \"add\",\n   \
    \ \"source_stage\": \"Main-recipe solvent before subsequent sterile stock additions\"\
    ,\n    \"source_amount\": {\n      \"value\": 1000,\n      \"unit\": \"ml\"\n\
    \    },\n    \"proposed\": \"Represent the solvent quantity and preparation basis;\
    \ do not infer a measured final volume.\",\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, distilled-water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1038api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1038\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"71b6c363ca855c0f99bdb1b7fcbd658cc38844f11c587ec5d0f24e5052ee3f7f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ph_value\",\n    \"existing\": 2.5,\n    \"decision\": \"evidence_only\",\n  \
    \  \"source_stage\": \"Adjustment before dispensing and autoclaving\",\n    \"\
    proposed\": \"Retain target pH 2.5 and attach stage-specific evidence. This does\
    \ not assert measured final pH.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz1038\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, preparation paragraph\",\n        \"\
    exact_source_quote\": \"adjust pH to 2.5\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml\"\
    ,\n    \"field_path\": \"ph_value\",\n    \"existing\": 2.5,\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Adjustment before dispensing and\
    \ autoclaving\",\n    \"proposed\": \"Retain target pH 2.5 and attach stage-specific\
    \ evidence. This does not assert measured final pH.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, preparation paragraph\",\n        \"exact_source_quote\"\
    : \"adjust pH to 2.5\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidicaldus_medium.yaml\"\
    ,\n    \"field_path\": \"ph_value\",\n    \"existing\": 2.5,\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Adjustment before dispensing and\
    \ autoclaving\",\n    \"proposed\": \"Retain target pH 2.5 and attach stage-specific\
    \ evidence. This does not assert measured final pH.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, preparation paragraph\",\n        \"exact_source_quote\"\
    : \"adjust pH to 2.5\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target and both owners\",\n    \"\
    field_path\": \"solutions / preparation_steps (sterile stock context)\",\n   \
    \ \"ingredient\": \"D-Glucose\",\n    \"decision\": \"not_quantified\",\n    \"\
    source_stage\": \"After autoclaving\",\n    \"proposed\": \"Preserve the specified\
    \ main-recipe mass and separate sterile-stock addition stage; stock concentration\
    \ and addition volume are not supplied and must not be guessed.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1038\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, final preparation sentence\",\n        \"exact_source_quote\"\
    : \"Add glucose and yeast extract after autoclaving\\nfrom sterile stock solutions.\"\
    ,\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target and both owners\",\n    \"\
    field_path\": \"solutions / preparation_steps (sterile stock context)\",\n   \
    \ \"ingredient\": \"Yeast extract\",\n    \"decision\": \"not_quantified\",\n\
    \    \"source_stage\": \"After autoclaving\",\n    \"proposed\": \"Preserve the\
    \ specified main-recipe mass and separate sterile-stock addition stage; stock\
    \ concentration and addition volume are not supplied and must not be guessed.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1038\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1038.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, final preparation sentence\",\n    \
    \    \"exact_source_quote\": \"Add glucose and yeast extract after autoclaving\\\
    nfrom sterile stock solutions.\",\n        \"snapshot_sha256\": \"92756e1184f3704da7dc8dd778da20684d5abee5ce844b2fba1ad2e94833b708\"\
    ,\n        \"parsed_text_sha256\": \"d0500ee4c500783275a16ec863ef39544ae6c4b2d08fead2721b02b0fc704461\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: supported
  summary: '6 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 6/7 primary and 6/7 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Source forms
    are assessed separately.'
  target_ids:
  - CultureMech:003552
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi17634
  - chebi31795
  - chebi32588
  - chebi62946
  - chebi63036
  - chebi86159
  details: 'Instance coverage on a 0–100 percent scale, denominator 7: primary 85.71%;
    secondary 85.71%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: chemical-forms
  area: grounding
  topic: Source-specific chemical forms and complex ingredient
  outcome: supported
  summary: 'The six asserted pure-compound forms match the primary: ammonium sulfate,
    KCl, magnesium sulfate heptahydrate, KH2PO4, calcium nitrate tetrahydrate and
    D-glucose. Yeast extract is an unresolved complex mixture rather than a pure molecule;
    OXOID is a source product attribute absent locally. No unsupported hydrate, stoichiometry
    or organism inference was added.'
  target_ids:
  - CultureMech:003552
  evidence_ids:
  - primary
  - provider
  - mim
  - chebi17634
  - chebi31795
  - chebi32588
  - chebi62946
  - chebi63036
  - chebi86159
- assessment_id: classification
  area: scope
  topic: Medium category, physical state and applications
  outcome: supported
  summary: 'COMPLEX / SEMI_DEFINED is consistent with defined salts plus yeast extract;
    LIQUID is consistent with the source and no gelling ingredient. Bacterial category
    and generic microbial-cultivation application are retained as corpus metadata,
    not species-specific growth evidence. The KOMODO catalog header Is Aerobic and
    exact 1038 row false support Aerobic: No as imported source metadata. It is not
    treated as independently established physiology or an oxygen requirement.'
  target_ids:
  - CultureMech:003552
  evidence_ids:
  - record
  - primary
  - provider
  - komodo-catalog
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 23 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003552
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
findings:
- finding_id: f1
  issue_key: culturemech.003552.preparation-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated target omits the source-supported preparation sequence
  description: The DSMZ owner retains the full primary instruction to withhold glucose
    and yeast extract during autoclaving and add them later from sterile stocks. The
    KOMODO owner and generated target contain no preparation_steps. Ingredient equality
    and SOURCE_DUPLICATE links do not preserve this material stage boundary. Water
    1000 ml and the OXOID yeast-extract attribute also remain source-only; no absent
    stock dose or autoclave setting can be invented.
  target_ids:
  - CultureMech:003552
  field_paths:
  - preparation_steps
  - ingredients[5]
  - ingredients[6]
  - merged_from
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidicaldus_medium.yaml
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
  issue_key: culturemech.003552.claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Exact owner concentration evidence is absent from the generated layer
  description: Six DSMZ-owner ingredient evidence objects exactly match the current
    API bytes and correctly qualify the 1000 ml provider basis. The target and KOMODO
    owner contain none of those claim attachments; yeast extract and pH lack such
    evidence in all layers. Correct values without attached evidence are evidence_only,
    not verified. Source bibliography alone does not establish every claim.
  target_ids:
  - CultureMech:003552
  field_paths:
  - ingredients
  - references
  - ph_value
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidicaldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.003552.history-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO-derived historical timestamps are malformed or lack a timezone
  description: The target and KOMODO owner each retain 2026-01-27T01:15:01.fZ and
    timezone-naive 2026-02-03T11:19:12.401541. These four instances prevent a precise
    timestamp interpretation; deterministic recipe checks did not reject them. No
    true historical timezone or fractional seconds were recovered.
  target_ids:
  - CultureMech:003552
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidicaldus_medium.yaml
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
  description: Maintain source-scoped preparation and solvent/product context in the
    normalized contributors; preserve the two sterile-stock stages and use the maintained
    merge workflow to retain them in the derived target.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003552
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidicaldus_medium.yaml
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
  description: Preserve existing DSMZ evidence verbatim; add missing bounded evidence
    and use source-compatible merge behavior rather than treating another contributor’s
    evidence as inherited.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003552
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidicaldus_medium.yaml
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
  description: Preserve historical bytes and append a provenance clarification describing
    the malformed and timezone-naive values; do not fabricate corrected timestamps.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003552
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidicaldus_medium.yaml
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
- Exact KOMODO MediaInfo=1038 capture returned HTTP 403. The catalog and DSMZ PDF/API
  independently establish the mapped current recipe; the precise historical KOMODO
  detail payload remains unavailable. This optional provenance limit does not prevent
  assessment of the current DSMZ formulation. The catalog header Is Aerobic and exact
  1038 row false support the local oxygen annotation as source metadata only, not
  as physiological growth evidence.
- No strain, taxon, growth range, oxygen requirement or optimal condition is established
  by the medium title, catalog flags or generic application. DSMZ does not quantify
  the sterile stock strengths/doses or autoclave settings; no such values were inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-017
- generated-medium
```
