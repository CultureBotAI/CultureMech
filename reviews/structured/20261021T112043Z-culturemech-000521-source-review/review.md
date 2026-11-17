# Source and formulation review: acidiphilium_acidophilum_medium (CultureMech:000521)

- Review: 20261021T112043Z-culturemech-000521-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T11:17:40Z
- Finished UTC: 2026-10-21T11:20:43Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 108 identity, all eight ingredient values, chemical forms and solid-medium pH are supported in their stated scopes. The source iron-stock dose, stock composition and solvent volume are absent from both local layers; six correctly supported owner amounts and their provenance are absent from the older generated record. No recipe was edited.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 171; batch 018 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seventeen task batches contain 170 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 172 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000521 | data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml | generated | acidiphilium_acidophilum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000521 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000521 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch018/171/strict.tsv |
| validate-terms | passed | True | CultureMech:000521 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000521 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000521 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000521.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and pinned secondary identifier metadata

grounding: supported. Targets: CultureMech:000521.

8 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 8/8 primary and 8/8 secondary instances; all asserted secondary keys have exact pinned MIM rows. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 8: primary 100.00%; secondary 100.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Exact source accession and single maintained contributor

identity: supported. Targets: CultureMech:000521.

The target CultureMech:000521 and its only normalized contributor identify DSMZ108 / mediadive.medium:108. The official title and exact provider identifier agree. The merge event names this owner; no distinct medium is merged into the target.

### Supplied salts, hydrates, sugar and gelling agent

grounding: supported. Targets: CultureMech:000521.

The eight asserted chemical forms agree with the official formula: ammonium sulfate, potassium dihydrogen phosphate, magnesium sulfate heptahydrate, potassium chloride, calcium nitrate tetrahydrate, iron(II) sulfate heptahydrate, agar and D-glucose. All eight current secondary CHEBI keys have exact pinned MIM preferred-term rows. No pure-molecule molarity is assigned to agar.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:000521.

21 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "input_path": "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration",
    "ingredient": "(NH4)2SO4",
    "existing": {
      "value": "3",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 22.7032,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Existing amount and form agree with the provider-declared 1000 ml basis; attach narrow amount evidence in this local layer."
  },
  {
    "input_path": "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration",
    "ingredient": "KH2PO4",
    "existing": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 3.67415,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Existing amount and form agree with the provider-declared 1000 ml basis; attach narrow amount evidence in this local layer."
  },
  {
    "input_path": "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "existing": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.05719,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Existing amount and form agree with the provider-declared 1000 ml basis; attach narrow amount evidence in this local layer."
  },
  {
    "input_path": "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration",
    "ingredient": "KCl",
    "existing": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.34138,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Existing amount and form agree with the provider-declared 1000 ml basis; attach narrow amount evidence in this local layer."
  },
  {
    "input_path": "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration",
    "ingredient": "Ca(NO3)2 x 4 H2O",
    "existing": {
      "value": "0.018",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Ca(NO3)2 x 4 H2O\",\n                        \"compound_id\": 213,\n                        \"amount\": 18,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.018,\n                        \"mmol_l\": 0.0762231,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Existing amount and form agree with the provider-declared 1000 ml basis; attach narrow amount evidence in this local layer. 18 mg equals 0.018 g; no hydrate conversion is performed."
  },
  {
    "input_path": "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration",
    "ingredient": "FeSO4 x 7 H2O",
    "existing": {
      "value": "1e-05",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"attribute\": \"0.1% w/v in 0.1 N H2SO4\",\n                        \"amount\": 0.01,\n                        \"unit\": \"ml\",\n                        \"g_l\": 1.0e-5,\n                        \"mmol_l\": 3.59693e-5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Existing amount and form agree with the provider-declared 1000 ml basis; attach narrow amount evidence in this local layer. The reported 0.00001 g/L is the provider-derived delivered iron-salt equivalent: (0.1 g / 100 ml) * 0.01 ml = 0.00001 g per listed batch, then divided by the provider-declared 1 L. It is not the stock concentration. Add the actual acidified stock and dose separately without double counting; measured final volume is not established."
  },
  {
    "input_path": "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration",
    "ingredient": "Agar",
    "existing": {
      "value": "15",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"attribute\": \"\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 1\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Existing amount and form agree with the provider-declared 1000 ml basis; attach narrow amount evidence in this local layer. This 15 g/L value is conditional on the solid-medium option, explicitly preserved by the ingredient note and SOLID_AGAR metadata. It is not an unconditional liquid-medium ingredient."
  },
  {
    "input_path": "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration",
    "ingredient": "D-Glucose",
    "existing": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 55.5062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Existing amount and form agree with the provider-declared 1000 ml basis; attach narrow amount evidence in this local layer."
  },
  {
    "input_path": "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml",
    "field_path": "ingredients[0].concentration",
    "ingredient": "(NH4)2SO4",
    "existing": {
      "value": "3",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 22.7032,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Exact amount, supplied form and provider-declared 1000 ml basis agree; evidence is attached only in the specifically named local layer."
  },
  {
    "input_path": "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml",
    "field_path": "ingredients[1].concentration",
    "ingredient": "KH2PO4",
    "existing": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 3.67415,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Exact amount, supplied form and provider-declared 1000 ml basis agree; evidence is attached only in the specifically named local layer."
  },
  {
    "input_path": "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml",
    "field_path": "ingredients[2].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "existing": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.05719,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Exact amount, supplied form and provider-declared 1000 ml basis agree; evidence is attached only in the specifically named local layer."
  },
  {
    "input_path": "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml",
    "field_path": "ingredients[3].concentration",
    "ingredient": "KCl",
    "existing": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.34138,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Exact amount, supplied form and provider-declared 1000 ml basis agree; evidence is attached only in the specifically named local layer."
  },
  {
    "input_path": "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml",
    "field_path": "ingredients[4].concentration",
    "ingredient": "Ca(NO3)2 x 4 H2O",
    "existing": {
      "value": "0.018",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Ca(NO3)2 x 4 H2O\",\n                        \"compound_id\": 213,\n                        \"amount\": 18,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.018,\n                        \"mmol_l\": 0.0762231,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Exact amount, supplied form and provider-declared 1000 ml basis agree; evidence is attached only in the specifically named local layer. 18 mg equals 0.018 g; no hydrate conversion is performed."
  },
  {
    "input_path": "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml",
    "field_path": "ingredients[5].concentration",
    "ingredient": "FeSO4 x 7 H2O",
    "existing": {
      "value": "1e-05",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"attribute\": \"0.1% w/v in 0.1 N H2SO4\",\n                        \"amount\": 0.01,\n                        \"unit\": \"ml\",\n                        \"g_l\": 1.0e-5,\n                        \"mmol_l\": 3.59693e-5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Existing amount and form agree with the provider-declared 1000 ml basis; attach narrow amount evidence in this local layer. The reported 0.00001 g/L is the provider-derived delivered iron-salt equivalent: (0.1 g / 100 ml) * 0.01 ml = 0.00001 g per listed batch, then divided by the provider-declared 1 L. It is not the stock concentration. Add the actual acidified stock and dose separately without double counting; measured final volume is not established."
  },
  {
    "input_path": "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml",
    "field_path": "ingredients[6].concentration",
    "ingredient": "Agar",
    "existing": {
      "value": "15",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"attribute\": \"\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 1\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Existing amount and form agree with the provider-declared 1000 ml basis; attach narrow amount evidence in this local layer. This 15 g/L value is conditional on the solid-medium option, explicitly preserved by the ingredient note and SOLID_AGAR metadata. It is not an unconditional liquid-medium ingredient."
  },
  {
    "input_path": "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml",
    "field_path": "ingredients[7].concentration",
    "ingredient": "D-Glucose",
    "existing": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "main recipe, provider-declared 1000 ml basis; agar conditional on solid medium",
    "source_snippets": [
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 55.5062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Exact amount, supplied form and provider-declared 1000 ml basis agree; evidence is attached only in the specifically named local layer."
  },
  {
    "input_paths": [
      "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
      "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml"
    ],
    "field_path": "source-only iron-stock addition",
    "ingredient": "Acidified iron(II) sulfate heptahydrate stock",
    "existing": null,
    "decision": "add",
    "source_value": "0.01",
    "source_unit": "ml per listed batch",
    "source_stage": "acidified iron stock and its addition",
    "source_snippets": [
      {
        "source_key": "dsmz108",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium108.pdf",
        "source_locator": "Page1, iron-stock recipe row",
        "exact_source_quote": "FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4) 0.01 ml",
        "snapshot_sha256": "cec9e3df24fd970d77a089839003b8f86267b3380216b06185caf55c5f42b69d",
        "parsed_text_sha256": "5a04bf72743735ed150a345bc30d6af44117ade1ee8814b6e18e57da4c171fdc"
      }
    ],
    "interpretation": "Add the exact stock dose; preserve the primary batch basis and provider volume separately. This does not establish a stock-addition rate for other media."
  },
  {
    "input_paths": [
      "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
      "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml"
    ],
    "field_path": "source-only iron-stock composition",
    "ingredient": "Iron(II) sulfate heptahydrate",
    "existing": null,
    "decision": "add",
    "source_value": "0.1",
    "source_unit": "percent w/v in stock",
    "source_stage": "acidified iron stock and its addition",
    "source_snippets": [
      {
        "source_key": "dsmz108",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium108.pdf",
        "source_locator": "Page1, iron-stock recipe row",
        "exact_source_quote": "FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4) 0.01 ml",
        "snapshot_sha256": "cec9e3df24fd970d77a089839003b8f86267b3380216b06185caf55c5f42b69d",
        "parsed_text_sha256": "5a04bf72743735ed150a345bc30d6af44117ade1ee8814b6e18e57da4c171fdc"
      }
    ],
    "interpretation": "Retain 0.1% w/v as the stock concentration. A calculated 1 mg/ml stock strength is equivalent, but is not a main-medium concentration."
  },
  {
    "input_paths": [
      "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
      "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml"
    ],
    "field_path": "source-only iron-stock solvent",
    "ingredient": "Sulfuric acid",
    "existing": null,
    "decision": "add",
    "source_value": "0.1",
    "source_unit": "N in iron-stock solvent",
    "source_stage": "acidified iron stock and its addition",
    "source_snippets": [
      {
        "source_key": "dsmz108",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium108.pdf",
        "source_locator": "Page1, iron-stock recipe row",
        "exact_source_quote": "FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4) 0.01 ml",
        "snapshot_sha256": "cec9e3df24fd970d77a089839003b8f86267b3380216b06185caf55c5f42b69d",
        "parsed_text_sha256": "5a04bf72743735ed150a345bc30d6af44117ade1ee8814b6e18e57da4c171fdc"
      }
    ],
    "interpretation": "Retain the exact 0.1 N acid solvent strength in the stock context. It is not the strength or dose of the separate main-medium pH-adjusting acid; do not introduce a molarity conversion."
  },
  {
    "input_paths": [
      "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
      "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml"
    ],
    "field_path": "source-only preparation solvent",
    "ingredient": "Distilled water",
    "existing": null,
    "decision": "add",
    "source_value": "1000",
    "source_unit": "ml per listed batch",
    "source_stage": "main recipe solvent",
    "source_snippets": [
      {
        "source_key": "dsmz108",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium108.pdf",
        "source_locator": "Page1, final recipe row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "cec9e3df24fd970d77a089839003b8f86267b3380216b06185caf55c5f42b69d",
        "parsed_text_sha256": "5a04bf72743735ed150a345bc30d6af44117ade1ee8814b6e18e57da4c171fdc"
      },
      {
        "source_key": "mediadive108api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/108",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac"
      }
    ],
    "interpretation": "Record the solvent quantity in preparation context. The primary says water1000 ml, not make up to a measured final1000 ml; the separately declared provider volume must remain identified as such."
  },
  {
    "input_paths": [
      "data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml",
      "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml"
    ],
    "field_path": "preparation_steps[0].description / separate main-medium pH-adjustment acid",
    "ingredient": "Sulfuric acid for pH adjustment",
    "decision": "not_quantified",
    "source_stage": "liquid pH3.5 or solid pH4.5 after autoclaving",
    "source_snippets": [
      {
        "source_key": "dsmz108",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium108.pdf",
        "source_locator": "Page1, preparation paragraph",
        "exact_source_quote": "In liquid medium, the pH should be adjusted to 3.5 with H2SO4. In solid medium, the pH\nshould be adjusted to 4.5 with H2SO4 after autoclaving the medium.",
        "snapshot_sha256": "cec9e3df24fd970d77a089839003b8f86267b3380216b06185caf55c5f42b69d",
        "parsed_text_sha256": "5a04bf72743735ed150a345bc30d6af44117ade1ee8814b6e18e57da4c171fdc"
      }
    ],
    "interpretation": "The local prose preserves both pH targets. The source gives neither the amount nor strength of this separate acid addition. Do not transfer the iron-stock solvent strength0.1 N or assume a dose."
  }
]

### Stock preparation, solvent basis and sterilization stages

representation: concern. Targets: CultureMech:000521.

Both local layers retain the complete primary paragraph about liquid pH3.5, solid pH4.5 after autoclaving, and separately sterilized glucose. The single MIX action is coarse but its prose is informative. The iron-stock dose0.01 ml, stock0.1% w/v in0.1 N H2SO4 and solvent1000 ml are missing from the complete local recipe; the delivered iron equivalent alone cannot reproduce that stock. No autoclave temperature/time or separate glucose sterilization method is specified in the inspected source.

### Conditional physical state and pH

scope: supported. Targets: CultureMech:000521.

SOLID_AGAR, optional15 g/L agar and root pH4.5 represent the official solid option. The preserved description states liquid pH3.5 and solid acidification after autoclaving. The source does not establish incubation temperature, duration or atmosphere; none is invented.

### Defined basal formulation and bounded application

scope: supported. Targets: CultureMech:000521.

The provider labels medium108 complex_medium=no and the local record uses DEFINED. Its specified basal salts and D-glucose support that source classification; agar is a mixture used in the explicitly conditional solid option. This is not a claim that agar is a single chemical. The bacterial filing and generic microbial-cultivation application do not assert a strain-specific growth result.

### No experimentally verified growth claim inferred from the medium name

evidence: not_applicable. Targets: CultureMech:000521.

Neither local layer asserts a target organism, strain, growth outcome, DOI or PMID. The medium title and culture-collection recipe establish formulation identity, not direct evidence that every Acidiphilium strain grows under unspecified conditions. No growth assertions are added.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:000521.

14 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Current owner evidence versus older generated snapshot

provenance: concern. Targets: CultureMech:000521.

The October7 owner history and six ingredient evidence objects are genuine existing concentration support: their snippets, indices and captured response hash exactly match the bound provider108 response. The August6 generated record omits those six objects, the bibliography and October7 event. All ingredient values, forms and preparation prose remain identical between the layers. Preserve this bounded provenance difference; do not attribute it to current merge code without regeneration.

## Findings

### f1: Restore the source iron-stock protocol and solvent basis

major / open / confirmed; issue key: culturemech-000521-acidified-iron-stock-and-solvent-missing.

Both local layers contain the correct provider-derived iron equivalent, but omit the source dose0.01 ml of0.1% w/v iron(II) sulfate heptahydrate in0.1 N sulfuric acid, and omit1000 ml distilled water as preparation context. The existing preparation paragraph cannot reconstruct that stock. Keep the distinct unquantified pH-adjustment acid separate.

### f2: Regenerate the omitted existing concentration evidence

minor / open / confirmed; issue key: culturemech-000521-generated-evidence-lags-owner.

Six matching amount evidence objects, one provider bibliography entry and the October7 owner curation event are absent from the August6 generated target. The numeric formulation is unchanged. This is a bounded stale provenance gap, not a claim that the maintained evidence is unsupported.

## Recommended Actions And Acceptance Checks

### a1

In the maintained normalized owner, preserve the explicit iron stock, its0.01 ml batch dose, solvent strength and1000 ml preparation water with field-scoped primary evidence. Reconcile any importer-owned regeneration and avoid double counting the stock and its delivered iron equivalent. Do not invent final volume, main-acid strength, sterilization temperature/time or a glucose sterilization method.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

After resolving the maintained stock/preparation gap, regenerate through the current merge pipeline and confirm the six unchanged evidence objects and bibliography survive. Preserve existing history and stable identifiers.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch018/171/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch018/171/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml:1:id: CultureMech:000521<br>./data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml:1:id: CultureMech:000521<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch018/source-preflight-bound/171/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 10 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary108 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium108.pdf; Full one-page DSMZ Medium 108 formulation and preparation paragraph | supports | The official recipe distinguishes the iron stock from its dose, optional agar, and liquid versus solid preparation conditions. |
| provider108 | https://mediadive.dsmz.de/rest/medium/108; $.data.medium; complete $.data.solutions[0], id182 | supports | The exact provider medium108 and main solution182 declare volume1000 ml and eight g_l values; this provider basis is not an independent final-volume measurement. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86159 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86159; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86159 resolves to calcium nitrate tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86159": [{"label": "Ca(NO3)2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| quantity-inventory | /private/tmp/culturemech-review-work-batch018/171/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| history-metadata | data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml; data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml", "events": 7, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Read relevant current code: API composition skips stock additions and solvents; API solutions preserve percent-stock attributes; current formulation consolidation unions scoped evidence; the amount writer conservatively excludes attributed/optional rows. These explain current ownership and follow-up, not proof that old output was produced by the current functions. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Read relevant current code: API composition skips stock additions and solvents; API solutions preserve percent-stock attributes; current formulation consolidation unions scoped evidence; the amount writer conservatively excludes attributed/optional rows. These explain current ownership and follow-up, not proof that old output was produced by the current functions. |
| writer-2 | scripts/review_medium_concentration_evidence.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Read relevant current code: API composition skips stock additions and solvents; API solutions preserve percent-stock attributes; current formulation consolidation unions scoped evidence; the amount writer conservatively excludes attributed/optional rows. These explain current ownership and follow-up, not proof that old output was produced by the current functions. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Provider-declared volume1000 ml and g_l values support bounded provider amounts; primary water1000 ml does not independently prove final volume. Source instructions leave the pH-adjusting acid amount/strength and sterilization temperature/time or glucose method unspecified. No inference fills those gaps.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T112043Z-culturemech-000521-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidiphilium_acidophilum_medium (CultureMech:000521)'
started_at: '2026-10-21T11:17:40Z'
finished_at: '2026-10-21T11:20:43Z'
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
summary: DSMZ 108 identity, all eight ingredient values, chemical forms and solid-medium
  pH are supported in their stated scopes. The source iron-stock dose, stock composition
  and solvent volume are absent from both local layers; six correctly supported owner
  amounts and their provenance are absent from the older generated record. No recipe
  was edited.
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
  - path: data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml
    sha256: 79214455575a80e850478a119f48397f612abda354896869d9c71bf450194d09
    role: target
  - path: data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml
    sha256: 9a79ef21b2b14dd1d6d1ce4cdde081e1f038ada0102bad366c060c2fea32988c
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
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 171; batch 018 item 1 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding seventeen task batches
    contain 170 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 172 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000521
targets:
- target_id: CultureMech:000521
  path: data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml
  label: acidiphilium_acidophilum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch018/171/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch018/171/strict.tsv"
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000521
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
  - CultureMech:000521
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:20:41Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:20:41Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:18:14.515940Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch018/171/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T11:18:19.381537Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch018/171/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:18:24.336501Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:18:26.480229Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:20:41Z'
  support: supports
  summary: './data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml:1:id: CultureMech:000521

    ./data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml:1:id: CultureMech:000521

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch018/source-preflight-bound/171/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:20:41Z'
  support: supports
  summary: 10 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 2dbd7679a77700c0aa1b7880d8f0695ca297c0d131a3ad0a1894204e991a0773
- evidence_id: primary108
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium108.pdf
  locator: Full one-page DSMZ Medium 108 formulation and preparation paragraph
  accessed_at: '2026-10-21T11:02:38.067693Z'
  support: supports
  summary: The official recipe distinguishes the iron stock from its dose, optional
    agar, and liquid versus solid preparation conditions.
  quote: FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4) 0.01 ml
  snapshot_sha256: cec9e3df24fd970d77a089839003b8f86267b3380216b06185caf55c5f42b69d
- evidence_id: provider108
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/108
  locator: $.data.medium; complete $.data.solutions[0], id182
  accessed_at: '2026-10-21T11:02:37.423006Z'
  support: supports
  summary: The exact provider medium108 and main solution182 declare volume1000 ml
    and eight g_l values; this provider basis is not an independent final-volume measurement.
  snapshot_sha256: 655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac
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
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 resolves to agar. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
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
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi86159
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86159
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T10:35:29.712666Z'
  support: supports
  summary: CHEBI:86159 resolves to calcium nitrate tetrahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: d2b0e9caef5876c00ed00136113d600d34a071b137bdd8c661c734ad5435682f
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T11:20:41Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17634":
    [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634",
    "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:2509": [{"label": "Agar", "match_type":
    "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795":
    [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86159":
    [{"label": "Ca(NO3)2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86159",
    "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch018/171/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:20:41Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 06c263d97220a522314e6bf850401b94c86156597c2786383ea0d696f6899027
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml; data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:20:41Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:20:41Z'
  support: context_only
  summary: 'Read relevant current code: API composition skips stock additions and
    solvents; API solutions preserve percent-stock attributes; current formulation
    consolidation unions scoped evidence; the amount writer conservatively excludes
    attributed/optional rows. These explain current ownership and follow-up, not proof
    that old output was produced by the current functions.'
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:20:41Z'
  support: context_only
  summary: 'Read relevant current code: API composition skips stock additions and
    solvents; API solutions preserve percent-stock attributes; current formulation
    consolidation unions scoped evidence; the amount writer conservatively excludes
    attributed/optional rows. These explain current ownership and follow-up, not proof
    that old output was produced by the current functions.'
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-2
  kind: record_content
  reference: scripts/review_medium_concentration_evidence.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:20:41Z'
  support: context_only
  summary: 'Read relevant current code: API composition skips stock additions and
    solvents; API solutions preserve percent-stock attributes; current formulation
    consolidation unions scoped evidence; the amount writer conservatively excludes
    attributed/optional rows. These explain current ownership and follow-up, not proof
    that old output was produced by the current functions.'
  snapshot_sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: supported
  summary: '8 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 8/8 primary and 8/8 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Source forms
    are assessed separately.'
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi17634
  - chebi2509
  - chebi31795
  - chebi32588
  - chebi62946
  - chebi63036
  - chebi75836
  - chebi86159
  details: 'Instance coverage on a 0–100 percent scale, denominator 8: primary 100.00%;
    secondary 100.00%. These are linkage metrics, not correctness scores. Missing
    optional links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Exact source accession and single maintained contributor
  outcome: supported
  summary: The target CultureMech:000521 and its only normalized contributor identify
    DSMZ108 / mediadive.medium:108. The official title and exact provider identifier
    agree. The merge event names this owner; no distinct medium is merged into the
    target.
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - record
  - owner-0
  - id-search
  - primary108
  - provider108
- assessment_id: forms
  area: grounding
  topic: Supplied salts, hydrates, sugar and gelling agent
  outcome: supported
  summary: 'The eight asserted chemical forms agree with the official formula: ammonium
    sulfate, potassium dihydrogen phosphate, magnesium sulfate heptahydrate, potassium
    chloride, calcium nitrate tetrahydrate, iron(II) sulfate heptahydrate, agar and
    D-glucose. All eight current secondary CHEBI keys have exact pinned MIM preferred-term
    rows. No pure-molecule molarity is assigned to agar.'
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - record
  - owner-0
  - primary108
  - provider108
  - mim
  - chebi17634
  - chebi2509
  - chebi31795
  - chebi32588
  - chebi62946
  - chebi63036
  - chebi75836
  - chebi86159
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 21 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"input_path\": \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"ingredient\":\
    \ \"(NH4)2SO4\",\n    \"existing\": {\n      \"value\": \"3\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"main recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\
    \": 27,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"mmol_l\\\": 22.7032,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing amount and form agree with\
    \ the provider-declared 1000 ml basis; attach narrow amount evidence in this local\
    \ layer.\"\n  },\n  {\n    \"input_path\": \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[1].concentration\",\n    \"ingredient\":\
    \ \"KH2PO4\",\n    \"existing\": {\n      \"value\": \"0.5\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"main recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n \
    \                       \\\"mmol_l\\\": 3.67415,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing amount and form agree with\
    \ the provider-declared 1000 ml basis; attach narrow amount evidence in this local\
    \ layer.\"\n  },\n  {\n    \"input_path\": \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[2].concentration\",\n    \"ingredient\":\
    \ \"MgSO4 x 7 H2O\",\n    \"existing\": {\n      \"value\": \"1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"main recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 1,\\n          \
    \              \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 1,\\n                        \\\"mmol_l\\\": 4.05719,\\n                   \
    \     \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Existing amount and form agree with the\
    \ provider-declared 1000 ml basis; attach narrow amount evidence in this local\
    \ layer.\"\n  },\n  {\n    \"input_path\": \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[3].concentration\",\n    \"ingredient\":\
    \ \"KCl\",\n    \"existing\": {\n      \"value\": \"0.1\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"main recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\
    \": 61,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"mmol_l\\\": 1.34138,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing amount and form agree with\
    \ the provider-declared 1000 ml basis; attach narrow amount evidence in this local\
    \ layer.\"\n  },\n  {\n    \"input_path\": \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[4].concentration\",\n    \"ingredient\":\
    \ \"Ca(NO3)2 x 4 H2O\",\n    \"existing\": {\n      \"value\": \"0.018\",\n  \
    \    \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n   \
    \ \"source_stage\": \"main recipe, provider-declared 1000 ml basis; agar conditional\
    \ on solid medium\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive108api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 5,\\\
    n                        \\\"compound\\\": \\\"Ca(NO3)2 x 4 H2O\\\",\\n      \
    \                  \\\"compound_id\\\": 213,\\n                        \\\"amount\\\
    \": 18,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.018,\\n                        \\\"mmol_l\\\": 0.0762231,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing amount and form agree with\
    \ the provider-declared 1000 ml basis; attach narrow amount evidence in this local\
    \ layer. 18 mg equals 0.018 g; no hydrate conversion is performed.\"\n  },\n \
    \ {\n    \"input_path\": \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[5].concentration\",\n    \"ingredient\":\
    \ \"FeSO4 x 7 H2O\",\n    \"existing\": {\n      \"value\": \"1e-05\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"\
    source_stage\": \"main recipe, provider-declared 1000 ml basis; agar conditional\
    \ on solid medium\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive108api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 12,\\n                        \\\"attribute\\\
    \": \\\"0.1% w/v in 0.1 N H2SO4\\\",\\n                        \\\"amount\\\"\
    : 0.01,\\n                        \\\"unit\\\": \\\"ml\\\",\\n               \
    \         \\\"g_l\\\": 1.0e-5,\\n                        \\\"mmol_l\\\": 3.59693e-5,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing amount and form agree with\
    \ the provider-declared 1000 ml basis; attach narrow amount evidence in this local\
    \ layer. The reported 0.00001 g/L is the provider-derived delivered iron-salt\
    \ equivalent: (0.1 g / 100 ml) * 0.01 ml = 0.00001 g per listed batch, then divided\
    \ by the provider-declared 1 L. It is not the stock concentration. Add the actual\
    \ acidified stock and dose separately without double counting; measured final\
    \ volume is not established.\"\n  },\n  {\n    \"input_path\": \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[6].concentration\",\n    \"ingredient\":\
    \ \"Agar\",\n    \"existing\": {\n      \"value\": \"15\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"main recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\
    \": 3,\\n                        \\\"condition\\\": \\\"for solid medium\\\",\\\
    n                        \\\"attribute\\\": \\\"\\\",\\n                     \
    \   \\\"amount\\\": 15,\\n                        \\\"unit\\\": \\\"g\\\",\\n\
    \                        \\\"g_l\\\": 15,\\n                        \\\"mmol_l\\\
    \": 44.5991,\\n                        \\\"optional\\\": 1\\n                \
    \    }\",\n        \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing amount and form agree with\
    \ the provider-declared 1000 ml basis; attach narrow amount evidence in this local\
    \ layer. This 15 g/L value is conditional on the solid-medium option, explicitly\
    \ preserved by the ingredient note and SOLID_AGAR metadata. It is not an unconditional\
    \ liquid-medium ingredient.\"\n  },\n  {\n    \"input_path\": \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[7].concentration\",\n    \"ingredient\":\
    \ \"D-Glucose\",\n    \"existing\": {\n      \"value\": \"10\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"main recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"D-Glucose\\\",\\n                        \\\"compound_id\\\
    \": 211,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n  \
    \                      \\\"mmol_l\\\": 55.5062,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing amount and form agree with\
    \ the provider-declared 1000 ml basis; attach narrow amount evidence in this local\
    \ layer.\"\n  },\n  {\n    \"input_path\": \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"ingredient\":\
    \ \"(NH4)2SO4\",\n    \"existing\": {\n      \"value\": \"3\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\":\
    \ \"main recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\
    \": 27,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"mmol_l\\\": 22.7032,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Exact amount, supplied form and provider-declared\
    \ 1000 ml basis agree; evidence is attached only in the specifically named local\
    \ layer.\"\n  },\n  {\n    \"input_path\": \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[1].concentration\",\n    \"ingredient\":\
    \ \"KH2PO4\",\n    \"existing\": {\n      \"value\": \"0.5\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\":\
    \ \"main recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n \
    \                       \\\"mmol_l\\\": 3.67415,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Exact amount, supplied form and provider-declared\
    \ 1000 ml basis agree; evidence is attached only in the specifically named local\
    \ layer.\"\n  },\n  {\n    \"input_path\": \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[2].concentration\",\n    \"ingredient\":\
    \ \"MgSO4 x 7 H2O\",\n    \"existing\": {\n      \"value\": \"1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\":\
    \ \"main recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 1,\\n          \
    \              \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 1,\\n                        \\\"mmol_l\\\": 4.05719,\\n                   \
    \     \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Exact amount, supplied form and provider-declared\
    \ 1000 ml basis agree; evidence is attached only in the specifically named local\
    \ layer.\"\n  },\n  {\n    \"input_path\": \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[3].concentration\",\n    \"ingredient\":\
    \ \"KCl\",\n    \"existing\": {\n      \"value\": \"0.1\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\": \"main\
    \ recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\
    \": 61,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"mmol_l\\\": 1.34138,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Exact amount, supplied form and provider-declared\
    \ 1000 ml basis agree; evidence is attached only in the specifically named local\
    \ layer.\"\n  },\n  {\n    \"input_path\": \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[4].concentration\",\n    \"ingredient\":\
    \ \"Ca(NO3)2 x 4 H2O\",\n    \"existing\": {\n      \"value\": \"0.018\",\n  \
    \    \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\"\
    : \"main recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"Ca(NO3)2 x 4 H2O\\\",\\n                        \\\
    \"compound_id\\\": 213,\\n                        \\\"amount\\\": 18,\\n     \
    \                   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.018,\\n                        \\\"mmol_l\\\": 0.0762231,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Exact amount, supplied form and provider-declared\
    \ 1000 ml basis agree; evidence is attached only in the specifically named local\
    \ layer. 18 mg equals 0.018 g; no hydrate conversion is performed.\"\n  },\n \
    \ {\n    \"input_path\": \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[5].concentration\",\n    \"ingredient\":\
    \ \"FeSO4 x 7 H2O\",\n    \"existing\": {\n      \"value\": \"1e-05\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"\
    source_stage\": \"main recipe, provider-declared 1000 ml basis; agar conditional\
    \ on solid medium\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive108api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 12,\\n                        \\\"attribute\\\
    \": \\\"0.1% w/v in 0.1 N H2SO4\\\",\\n                        \\\"amount\\\"\
    : 0.01,\\n                        \\\"unit\\\": \\\"ml\\\",\\n               \
    \         \\\"g_l\\\": 1.0e-5,\\n                        \\\"mmol_l\\\": 3.59693e-5,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing amount and form agree with\
    \ the provider-declared 1000 ml basis; attach narrow amount evidence in this local\
    \ layer. The reported 0.00001 g/L is the provider-derived delivered iron-salt\
    \ equivalent: (0.1 g / 100 ml) * 0.01 ml = 0.00001 g per listed batch, then divided\
    \ by the provider-declared 1 L. It is not the stock concentration. Add the actual\
    \ acidified stock and dose separately without double counting; measured final\
    \ volume is not established.\"\n  },\n  {\n    \"input_path\": \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[6].concentration\",\n    \"ingredient\":\
    \ \"Agar\",\n    \"existing\": {\n      \"value\": \"15\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"main recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\
    \": 3,\\n                        \\\"condition\\\": \\\"for solid medium\\\",\\\
    n                        \\\"attribute\\\": \\\"\\\",\\n                     \
    \   \\\"amount\\\": 15,\\n                        \\\"unit\\\": \\\"g\\\",\\n\
    \                        \\\"g_l\\\": 15,\\n                        \\\"mmol_l\\\
    \": 44.5991,\\n                        \\\"optional\\\": 1\\n                \
    \    }\",\n        \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing amount and form agree with\
    \ the provider-declared 1000 ml basis; attach narrow amount evidence in this local\
    \ layer. This 15 g/L value is conditional on the solid-medium option, explicitly\
    \ preserved by the ingredient note and SOLID_AGAR metadata. It is not an unconditional\
    \ liquid-medium ingredient.\"\n  },\n  {\n    \"input_path\": \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[7].concentration\",\n    \"ingredient\":\
    \ \"D-Glucose\",\n    \"existing\": {\n      \"value\": \"10\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"verified\",\n    \"source_stage\":\
    \ \"main recipe, provider-declared 1000 ml basis; agar conditional on solid medium\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive108api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"D-Glucose\\\",\\n                        \\\"compound_id\\\
    \": 211,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n  \
    \                      \\\"mmol_l\\\": 55.5062,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Exact amount, supplied form and provider-declared\
    \ 1000 ml basis agree; evidence is attached only in the specifically named local\
    \ layer.\"\n  },\n  {\n    \"input_paths\": [\n      \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\"\
    ,\n      \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\
    \n    ],\n    \"field_path\": \"source-only iron-stock addition\",\n    \"ingredient\"\
    : \"Acidified iron(II) sulfate heptahydrate stock\",\n    \"existing\": null,\n\
    \    \"decision\": \"add\",\n    \"source_value\": \"0.01\",\n    \"source_unit\"\
    : \"ml per listed batch\",\n    \"source_stage\": \"acidified iron stock and its\
    \ addition\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz108\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium108.pdf\"\
    ,\n        \"source_locator\": \"Page1, iron-stock recipe row\",\n        \"exact_source_quote\"\
    : \"FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4) 0.01 ml\",\n        \"snapshot_sha256\"\
    : \"cec9e3df24fd970d77a089839003b8f86267b3380216b06185caf55c5f42b69d\",\n    \
    \    \"parsed_text_sha256\": \"5a04bf72743735ed150a345bc30d6af44117ade1ee8814b6e18e57da4c171fdc\"\
    \n      }\n    ],\n    \"interpretation\": \"Add the exact stock dose; preserve\
    \ the primary batch basis and provider volume separately. This does not establish\
    \ a stock-addition rate for other media.\"\n  },\n  {\n    \"input_paths\": [\n\
    \      \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\",\n    \
    \  \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\n \
    \   ],\n    \"field_path\": \"source-only iron-stock composition\",\n    \"ingredient\"\
    : \"Iron(II) sulfate heptahydrate\",\n    \"existing\": null,\n    \"decision\"\
    : \"add\",\n    \"source_value\": \"0.1\",\n    \"source_unit\": \"percent w/v\
    \ in stock\",\n    \"source_stage\": \"acidified iron stock and its addition\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz108\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium108.pdf\"\
    ,\n        \"source_locator\": \"Page1, iron-stock recipe row\",\n        \"exact_source_quote\"\
    : \"FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4) 0.01 ml\",\n        \"snapshot_sha256\"\
    : \"cec9e3df24fd970d77a089839003b8f86267b3380216b06185caf55c5f42b69d\",\n    \
    \    \"parsed_text_sha256\": \"5a04bf72743735ed150a345bc30d6af44117ade1ee8814b6e18e57da4c171fdc\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain 0.1% w/v as the stock concentration.\
    \ A calculated 1 mg/ml stock strength is equivalent, but is not a main-medium\
    \ concentration.\"\n  },\n  {\n    \"input_paths\": [\n      \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\"\
    ,\n      \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\
    \n    ],\n    \"field_path\": \"source-only iron-stock solvent\",\n    \"ingredient\"\
    : \"Sulfuric acid\",\n    \"existing\": null,\n    \"decision\": \"add\",\n  \
    \  \"source_value\": \"0.1\",\n    \"source_unit\": \"N in iron-stock solvent\"\
    ,\n    \"source_stage\": \"acidified iron stock and its addition\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz108\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium108.pdf\",\n        \"\
    source_locator\": \"Page1, iron-stock recipe row\",\n        \"exact_source_quote\"\
    : \"FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4) 0.01 ml\",\n        \"snapshot_sha256\"\
    : \"cec9e3df24fd970d77a089839003b8f86267b3380216b06185caf55c5f42b69d\",\n    \
    \    \"parsed_text_sha256\": \"5a04bf72743735ed150a345bc30d6af44117ade1ee8814b6e18e57da4c171fdc\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact 0.1 N acid solvent\
    \ strength in the stock context. It is not the strength or dose of the separate\
    \ main-medium pH-adjusting acid; do not introduce a molarity conversion.\"\n \
    \ },\n  {\n    \"input_paths\": [\n      \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\"\
    ,\n      \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\
    \n    ],\n    \"field_path\": \"source-only preparation solvent\",\n    \"ingredient\"\
    : \"Distilled water\",\n    \"existing\": null,\n    \"decision\": \"add\",\n\
    \    \"source_value\": \"1000\",\n    \"source_unit\": \"ml per listed batch\"\
    ,\n    \"source_stage\": \"main recipe solvent\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz108\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium108.pdf\"\
    ,\n        \"source_locator\": \"Page1, final recipe row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"cec9e3df24fd970d77a089839003b8f86267b3380216b06185caf55c5f42b69d\"\
    ,\n        \"parsed_text_sha256\": \"5a04bf72743735ed150a345bc30d6af44117ade1ee8814b6e18e57da4c171fdc\"\
    \n      },\n      {\n        \"source_key\": \"mediadive108api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/108\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"655a9032464bbce77701f8a17b66425e88aae2b77a54738f875acec3443ae7ac\"\
    \n      }\n    ],\n    \"interpretation\": \"Record the solvent quantity in preparation\
    \ context. The primary says water1000 ml, not make up to a measured final1000\
    \ ml; the separately declared provider volume must remain identified as such.\"\
    \n  },\n  {\n    \"input_paths\": [\n      \"data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml\"\
    ,\n      \"data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml\"\
    \n    ],\n    \"field_path\": \"preparation_steps[0].description / separate main-medium\
    \ pH-adjustment acid\",\n    \"ingredient\": \"Sulfuric acid for pH adjustment\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"source_stage\": \"liquid pH3.5\
    \ or solid pH4.5 after autoclaving\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz108\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium108.pdf\"\
    ,\n        \"source_locator\": \"Page1, preparation paragraph\",\n        \"exact_source_quote\"\
    : \"In liquid medium, the pH should be adjusted to 3.5 with H2SO4. In solid medium,\
    \ the pH\\nshould be adjusted to 4.5 with H2SO4 after autoclaving the medium.\"\
    ,\n        \"snapshot_sha256\": \"cec9e3df24fd970d77a089839003b8f86267b3380216b06185caf55c5f42b69d\"\
    ,\n        \"parsed_text_sha256\": \"5a04bf72743735ed150a345bc30d6af44117ade1ee8814b6e18e57da4c171fdc\"\
    \n      }\n    ],\n    \"interpretation\": \"The local prose preserves both pH\
    \ targets. The source gives neither the amount nor strength of this separate acid\
    \ addition. Do not transfer the iron-stock solvent strength0.1 N or assume a dose.\"\
    \n  }\n]"
- assessment_id: preparation
  area: representation
  topic: Stock preparation, solvent basis and sterilization stages
  outcome: concern
  summary: Both local layers retain the complete primary paragraph about liquid pH3.5,
    solid pH4.5 after autoclaving, and separately sterilized glucose. The single MIX
    action is coarse but its prose is informative. The iron-stock dose0.01 ml, stock0.1%
    w/v in0.1 N H2SO4 and solvent1000 ml are missing from the complete local recipe;
    the delivered iron equivalent alone cannot reproduce that stock. No autoclave
    temperature/time or separate glucose sterilization method is specified in the
    inspected source.
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - record
  - owner-0
  - primary108
  - provider108
  - quantity-inventory
- assessment_id: conditions
  area: scope
  topic: Conditional physical state and pH
  outcome: supported
  summary: SOLID_AGAR, optional15 g/L agar and root pH4.5 represent the official solid
    option. The preserved description states liquid pH3.5 and solid acidification
    after autoclaving. The source does not establish incubation temperature, duration
    or atmosphere; none is invented.
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - record
  - owner-0
  - primary108
  - provider108
- assessment_id: classification
  area: scope
  topic: Defined basal formulation and bounded application
  outcome: supported
  summary: The provider labels medium108 complex_medium=no and the local record uses
    DEFINED. Its specified basal salts and D-glucose support that source classification;
    agar is a mixture used in the explicitly conditional solid option. This is not
    a claim that agar is a single chemical. The bacterial filing and generic microbial-cultivation
    application do not assert a strain-specific growth result.
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - record
  - owner-0
  - provider108
  - primary108
  - chebi2509
- assessment_id: growth
  area: evidence
  topic: No experimentally verified growth claim inferred from the medium name
  outcome: not_applicable
  summary: Neither local layer asserts a target organism, strain, growth outcome,
    DOI or PMID. The medium title and culture-collection recipe establish formulation
    identity, not direct evidence that every Acidiphilium strain grows under unspecified
    conditions. No growth assertions are added.
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - record
  - owner-0
  - primary108
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 14 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: provenance
  area: provenance
  topic: Current owner evidence versus older generated snapshot
  outcome: concern
  summary: 'The October7 owner history and six ingredient evidence objects are genuine
    existing concentration support: their snippets, indices and captured response
    hash exactly match the bound provider108 response. The August6 generated record
    omits those six objects, the bibliography and October7 event. All ingredient values,
    forms and preparation prose remain identical between the layers. Preserve this
    bounded provenance difference; do not attribute it to current merge code without
    regeneration.'
  target_ids:
  - CultureMech:000521
  evidence_ids:
  - record
  - owner-0
  - provider108
  - quantity-inventory
  - history-metadata
findings:
- finding_id: f1
  issue_key: culturemech-000521-acidified-iron-stock-and-solvent-missing
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Restore the source iron-stock protocol and solvent basis
  description: Both local layers contain the correct provider-derived iron equivalent,
    but omit the source dose0.01 ml of0.1% w/v iron(II) sulfate heptahydrate in0.1
    N sulfuric acid, and omit1000 ml distilled water as preparation context. The existing
    preparation paragraph cannot reconstruct that stock. Keep the distinct unquantified
    pH-adjustment acid separate.
  target_ids:
  - CultureMech:000521
  field_paths:
  - ingredients[5]
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - primary108
  - provider108
  - quantity-inventory
  - writer-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: single-record-checklist.solutions-and-preparation
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: culturemech-000521-generated-evidence-lags-owner
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Regenerate the omitted existing concentration evidence
  description: Six matching amount evidence objects, one provider bibliography entry
    and the October7 owner curation event are absent from the August6 generated target.
    The numeric formulation is unchanged. This is a bounded stale provenance gap,
    not a claim that the maintained evidence is unsupported.
  target_ids:
  - CultureMech:000521
  field_paths:
  - ingredients[*].evidence
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - provider108
  - quantity-inventory
  - history-metadata
  - writer-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: single-record-checklist.source-provenance
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: In the maintained normalized owner, preserve the explicit iron stock,
    its0.01 ml batch dose, solvent strength and1000 ml preparation water with field-scoped
    primary evidence. Reconcile any importer-owned regeneration and avoid double counting
    the stock and its delivered iron equivalent. Do not invent final volume, main-acid
    strength, sterilization temperature/time or a glucose sterilization method.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000521
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml
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
  description: After resolving the maintained stock/preparation gap, regenerate through
    the current merge pipeline and confirm the six unchanged evidence objects and
    bibliography survive. Preserve existing history and stable identifiers.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000521
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml
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
- Provider-declared volume1000 ml and g_l values support bounded provider amounts;
  primary water1000 ml does not independently prove final volume. Source instructions
  leave the pH-adjusting acid amount/strength and sterilization temperature/time or
  glucose method unspecified. No inference fills those gaps.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-018
- generated-medium
```
