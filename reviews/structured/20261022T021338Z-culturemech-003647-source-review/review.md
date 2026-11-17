# Source and formulation review: brevibacillus_levickii_medium (CultureMech:003647)

- Review: 20261022T021338Z-culturemech-003647-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T02:02:39Z
- Finished UTC: 2026-10-22T02:13:38Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 1064 and the exact recovered historical API support all seven retained provider-declared rates, including the manganese and calcium milligram conversions. All layers omit 1000 ml water; the generated record and KOMODO owner omit the DSMZ owner preparation sentence. Authenticated owner amount evidence is also absent from the generated descriptors.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 445; batch 045 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-four task batches contain 440 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 443 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003647 | data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml | generated | brevibacillus_levickii_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003647 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003647 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch045/445/strict.tsv |
| validate-terms | passed | True | CultureMech:003647 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003647 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003647 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive1064api | unavailable | False | CultureMech:003647 | Current exact MediaDive 1064 returned HTTP 503. Exact historical raw and the complete collection primary are available, so this optional refresh failure does not make historical authentication partial. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003647.

The four documented recipes completed; interpret the scope of each separately.

### Complete current ontology and secondary linkage inventory

grounding: supported. Targets: CultureMech:003647.

6 distinct bound ontology IDs resolve and are nonobsolete. 0 literal canonical-label mismatches, 0 unverified provider slots and 0 legacy slots are retained explicitly. 6/6 asserted current secondary keys have exact pinned index rows. Target primary linkage is 6/7 (85.71%) and current secondary linkage is 6/7 (85.71%) on a 0–100 linkage scale, not a correctness score. Current missing keys do not prove historical invalidity; compatible generic source wording does not establish a stereochemical conflict.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003647.

24 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact source-duplicate identity with separate evidence roles

identity: supported. Targets: CultureMech:003647.

Both maintained owners and the generated record identify accession 1064, and the source-duplicate relationship agrees with the exact catalog link and primary title. Agar 18 g supports the retained solid branch and yeast extract supports complex composition. Collection title and catalog oxygen metadata do not supply a strain-specific growth claim or strict anaerobic requirement.

### Exact historical provider rates and primary mass conversions

quantity: supported. Targets: CultureMech:003647.

The raw API declares volume 1000 ml and g_l values matching all seven local rates. Manganese sulfate monohydrate 2.50 mg converts to 0.0025 g, and calcium chloride dihydrate 12.50 mg to 0.0125 g; the API separately supplies those rates. All fourteen owner amount snippets and cited hashes authenticate. The PDF corroborates nominal batch masses without proving measured final volume.

### Missing water and lost preparation despite correct pH

representation: concern. Targets: CultureMech:003647.

All three layers omit the primary 1000 ml water input. The scalar pH 5.5 is correct throughout; only the DSMZ owner retains the printed pH adjustment and 121-degree/15-minute autoclave sentence. The PDF and historical API print 121° without an explicit C letter; retain that source wording rather than silently increasing its unit specificity. No incubation temperature or titrant dose is given.

### Exact supported salt and hydrate identities

grounding: supported. Targets: CultureMech:003647.

Ammonium sulfate, potassium dihydrogen phosphate, manganese(II) sulfate monohydrate, magnesium sulfate heptahydrate and calcium chloride dihydrate agree with the primary supplied forms and bound ontology scientific properties. Yeast extract remains an ungrounded complex descriptor; no invented exact chemical identity or supplier composition is assigned. Current provider aggregate ions and rounded molar displays are not substitute formulation inputs.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003647.

21 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "Yeast extract generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'Yeast extract'",
        "exact_source_quote": "Yeast extract                                            2.00    g",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "The exact local value and G_PER_L basis match authenticated provider-declared g_l, but the generated descriptor lacks the attached matching amount claim. This is provider-declared normalization, not independently measured final volume."
  },
  {
    "decision_id": "q2",
    "subject": "Yeast extract maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'Yeast extract'",
        "exact_source_quote": "Yeast extract                                            2.00    g",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "Both maintained descriptors retain the exact supporting excerpt, original hash and source metadata, reauthenticated against recovered raw. The provider explicitly declares this g_l value. Preserve the separate primary batch and provider-rate bases."
  },
  {
    "decision_id": "q3",
    "subject": "(NH4)2SO4 generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing '(NH4)2SO4'",
        "exact_source_quote": "(NH4)2SO4                                                1.25    g",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 1.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.25,\n                        \"mmol_l\": 9.45966,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "The exact local value and G_PER_L basis match authenticated provider-declared g_l, but the generated descriptor lacks the attached matching amount claim. This is provider-declared normalization, not independently measured final volume."
  },
  {
    "decision_id": "q4",
    "subject": "(NH4)2SO4 maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.25",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing '(NH4)2SO4'",
        "exact_source_quote": "(NH4)2SO4                                                1.25    g",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 1.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.25,\n                        \"mmol_l\": 9.45966,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "Both maintained descriptors retain the exact supporting excerpt, original hash and source metadata, reauthenticated against recovered raw. The provider explicitly declares this g_l value. Preserve the separate primary batch and provider-rate bases."
  },
  {
    "decision_id": "q5",
    "subject": "KH2PO4 generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'KH2PO4'",
        "exact_source_quote": "KH2PO4                                                   1.50    g",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 11.0225,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "The exact local value and G_PER_L basis match authenticated provider-declared g_l, but the generated descriptor lacks the attached matching amount claim. This is provider-declared normalization, not independently measured final volume."
  },
  {
    "decision_id": "q6",
    "subject": "KH2PO4 maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'KH2PO4'",
        "exact_source_quote": "KH2PO4                                                   1.50    g",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 11.0225,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "Both maintained descriptors retain the exact supporting excerpt, original hash and source metadata, reauthenticated against recovered raw. The provider explicitly declares this g_l value. Preserve the separate primary batch and provider-rate bases."
  },
  {
    "decision_id": "q7",
    "subject": "MnSO4 x H2O generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.0025",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'MnSO4'",
        "exact_source_quote": "MnSO4 x H2O                                              2.50   mg",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 2.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0025,\n                        \"mmol_l\": 0.0147915,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "The exact local value and G_PER_L basis match authenticated provider-declared g_l, but the generated descriptor lacks the attached matching amount claim. The primary 2.50 mg equals 0.0025 g. This is provider-declared normalization, not independently measured final volume."
  },
  {
    "decision_id": "q8",
    "subject": "MnSO4 x H2O maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.0025",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.0025",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'MnSO4'",
        "exact_source_quote": "MnSO4 x H2O                                              2.50   mg",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 2.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0025,\n                        \"mmol_l\": 0.0147915,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "Both maintained descriptors retain the exact supporting excerpt, original hash and source metadata, reauthenticated against recovered raw. The provider explicitly declares this g_l value. The primary 2.50 mg equals 0.0025 g. Preserve the separate primary batch and provider-rate bases."
  },
  {
    "decision_id": "q9",
    "subject": "MgSO4 x 7 H2O generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'MgSO4'",
        "exact_source_quote": "MgSO4 x 7 H2O                                            0.10    g",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.405719,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "The exact local value and G_PER_L basis match authenticated provider-declared g_l, but the generated descriptor lacks the attached matching amount claim. This is provider-declared normalization, not independently measured final volume."
  },
  {
    "decision_id": "q10",
    "subject": "MgSO4 x 7 H2O maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'MgSO4'",
        "exact_source_quote": "MgSO4 x 7 H2O                                            0.10    g",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.405719,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "Both maintained descriptors retain the exact supporting excerpt, original hash and source metadata, reauthenticated against recovered raw. The provider explicitly declares this g_l value. Preserve the separate primary batch and provider-rate bases."
  },
  {
    "decision_id": "q11",
    "subject": "CaCl2 x 2 H2O generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.0125",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'CaCl2'",
        "exact_source_quote": "CaCl2 x 2 H2O                                           12.50   mg",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 12.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0125,\n                        \"mmol_l\": 0.0850253,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "The exact local value and G_PER_L basis match authenticated provider-declared g_l, but the generated descriptor lacks the attached matching amount claim. The primary 12.50 mg equals 0.0125 g. This is provider-declared normalization, not independently measured final volume."
  },
  {
    "decision_id": "q12",
    "subject": "CaCl2 x 2 H2O maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.0125",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.0125",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'CaCl2'",
        "exact_source_quote": "CaCl2 x 2 H2O                                           12.50   mg",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 12.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0125,\n                        \"mmol_l\": 0.0850253,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "Both maintained descriptors retain the exact supporting excerpt, original hash and source metadata, reauthenticated against recovered raw. The provider explicitly declares this g_l value. The primary 12.50 mg equals 0.0125 g. Preserve the separate primary batch and provider-rate bases."
  },
  {
    "decision_id": "q13",
    "subject": "Agar generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "18",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'Agar'",
        "exact_source_quote": "Agar                                                    18.00    g",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 18,\n                        \"unit\": \"g\",\n                        \"g_l\": 18,\n                        \"mmol_l\": 53.5189,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "The exact local value and G_PER_L basis match authenticated provider-declared g_l, but the generated descriptor lacks the attached matching amount claim. This is provider-declared normalization, not independently measured final volume."
  },
  {
    "decision_id": "q14",
    "subject": "Agar maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "18",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'Agar'",
        "exact_source_quote": "Agar                                                    18.00    g",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 18,\n                        \"unit\": \"g\",\n                        \"g_l\": 18,\n                        \"mmol_l\": 53.5189,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "Both maintained descriptors retain the exact supporting excerpt, original hash and source metadata, reauthenticated against recovered raw. The provider explicitly declares this g_l value. Preserve the separate primary batch and provider-rate bases."
  },
  {
    "decision_id": "q15",
    "subject": "Missing source water input",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "2",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "(NH4)2SO4",
            "term": {
              "id": "CHEBI:62946",
              "label": "ammonium sulfate"
            },
            "concentration": {
              "value": "1.25",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:62946",
              "label": "ammonium sulfate"
            }
          },
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "1.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            }
          },
          {
            "preferred_term": "MnSO4 x H2O",
            "term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            },
            "concentration": {
              "value": "0.0025",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            }
          },
          {
            "preferred_term": "MgSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "CaCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "concentration": {
              "value": "0.0125",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "2",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[0].concentration (Yeast extract) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=2; check: 2 g * 1 g/g / (1000 ml / 1000 ml per L) = 2 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6. KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "(NH4)2SO4",
            "term": {
              "id": "CHEBI:62946",
              "label": "ammonium sulfate"
            },
            "concentration": {
              "value": "1.25",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:62946",
              "label": "ammonium sulfate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 1.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.25,\n                        \"mmol_l\": 9.45966,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[1].concentration ((NH4)2SO4) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=1.25; check: 1.25 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.25 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6. KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "1.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 11.0225,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[2].concentration (KH2PO4) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6. KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "MnSO4 x H2O",
            "term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            },
            "concentration": {
              "value": "0.0025",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 2.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0025,\n                        \"mmol_l\": 0.0147915,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[3].concentration (MnSO4 x H2O) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=0.0025; check: 2.5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.0025 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6. KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "MgSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.405719,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[4].concentration (MgSO4 x 7 H2O) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6. KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "CaCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "concentration": {
              "value": "0.0125",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 12.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0125,\n                        \"mmol_l\": 0.0850253,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[5].concentration (CaCl2 x 2 H2O) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=0.0125; check: 12.5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.0125 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6. KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
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
              "value": "18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 18,\n                        \"unit\": \"g\",\n                        \"g_l\": 18,\n                        \"mmol_l\": 53.5189,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[6].concentration (Agar) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports g_l=18; check: 18 g * 1 g/g / (1000 ml / 1000 ml per L) = 18 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6. KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "2",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[0].concentration (Yeast extract) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=2; check: 2 g * 1 g/g / (1000 ml / 1000 ml per L) = 2 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6."
              }
            ]
          },
          {
            "preferred_term": "(NH4)2SO4",
            "term": {
              "id": "CHEBI:62946",
              "label": "ammonium sulfate"
            },
            "concentration": {
              "value": "1.25",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:62946",
              "label": "ammonium sulfate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 1.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.25,\n                        \"mmol_l\": 9.45966,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[1].concentration ((NH4)2SO4) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=1.25; check: 1.25 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.25 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6."
              }
            ]
          },
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "1.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 11.0225,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[2].concentration (KH2PO4) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6."
              }
            ]
          },
          {
            "preferred_term": "MnSO4 x H2O",
            "term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            },
            "concentration": {
              "value": "0.0025",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 2.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0025,\n                        \"mmol_l\": 0.0147915,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[3].concentration (MnSO4 x H2O) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=0.0025; check: 2.5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.0025 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6."
              }
            ]
          },
          {
            "preferred_term": "MgSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.405719,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[4].concentration (MgSO4 x 7 H2O) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6."
              }
            ]
          },
          {
            "preferred_term": "CaCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "concentration": {
              "value": "0.0125",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 12.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0125,\n                        \"mmol_l\": 0.0850253,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[5].concentration (CaCl2 x 2 H2O) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=0.0125; check: 12.5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.0125 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6."
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
              "value": "18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1064",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 18,\n                        \"unit\": \"g\",\n                        \"g_l\": 18,\n                        \"mmol_l\": 53.5189,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[6].concentration (Agar) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports g_l=18; check: 18 g * 1 g/g / (1000 ml / 1000 ml per L) = 18 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6."
              }
            ]
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'Distilled water'",
        "exact_source_quote": "Distilled water                                       1000.00   ml",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      },
      {
        "source_key": "historical1064api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1064",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6"
      }
    ],
    "rationale": "Add the exact 1000 ml water batch input. Do not relabel it as a mass concentration or a measured final-volume instruction."
  },
  {
    "decision_id": "q16",
    "subject": "pH 5.5 endpoint",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 5.5
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml",
        "field_path": "ph_value",
        "stored": 5.5
      },
      {
        "input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
        "field_path": "ph_value",
        "stored": 5.5
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'Adjust pH'",
        "exact_source_quote": "Adjust pH to 5.5; autoclave at 121 for 15 minutes.",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      }
    ],
    "rationale": "The scalar 5.5 agrees exactly with the primary endpoint. Attach claim-level preparation evidence; catalog identity evidence is not a preparation claim."
  },
  {
    "decision_id": "q17",
    "subject": "Missing generated and KOMODO preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'Adjust pH'",
        "exact_source_quote": "Adjust pH to 5.5; autoclave at 121 for 15 minutes.",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      }
    ],
    "rationale": "Retain the primary adjustment to pH 5.5 and printed 121-degree, 15-minute autoclave instruction. The DSMZ owner already preserves the same source sentence."
  },
  {
    "decision_id": "q18",
    "subject": "Existing DSMZ preparation sentence",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 5.5; autoclave at 121° for 15 minutes."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'Adjust pH'",
        "exact_source_quote": "Adjust pH to 5.5; autoclave at 121 for 15 minutes.",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      }
    ],
    "rationale": "The existing sentence retains the matching endpoint, printed 121° and 15-minute duration. Link exact primary support, preserving the original glyph/unit limitation."
  },
  {
    "decision_id": "q19",
    "subject": "Autoclave duration 15 minutes",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 5.5; autoclave at 121° for 15 minutes."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'Adjust pH'",
        "exact_source_quote": "Adjust pH to 5.5; autoclave at 121 for 15 minutes.",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      }
    ],
    "rationale": "The source duration is explicitly 15 minutes and correctly retained by the DSMZ owner. It is not a growth duration or a different stock sterilization cycle."
  },
  {
    "decision_id": "q20",
    "subject": "Titrant amount",
    "decision": "not_quantified",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'Adjust pH'",
        "exact_source_quote": "Adjust pH to 5.5; autoclave at 121 for 15 minutes.",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      }
    ],
    "rationale": "The pH endpoint is explicit but no fixed titrant identity or dose is printed. Do not infer one."
  },
  {
    "decision_id": "q21",
    "subject": "Incubation temperature",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1064",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf",
        "source_locator": "Exact extracted source line containing 'Adjust pH'",
        "exact_source_quote": "Adjust pH to 5.5; autoclave at 121 for 15 minutes.",
        "snapshot_sha256": "6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02",
        "parsed_text_sha256": "69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb"
      }
    ],
    "rationale": "The only printed temperature-like value belongs to autoclaving. No growth/incubation temperature is supplied, so a generic incubation value remains unsupported."
  }
]

## Findings

### f1: Restore water and preserve source preparation

major / open / confirmed; issue key: brevibacillus-water-preparation-completeness.

The 1000 ml water input is absent from all three layers. The generated and KOMODO layers omit the pH/autoclave procedure that the DSMZ owner already retains; their scalar pH 5.5 remains correct.

### f2: Preserve authenticated owner amount claims in the generated record

major / open / confirmed; issue key: brevibacillus-generated-amount-evidence.

All fourteen attached owner amount excerpts match the recovered October 7 API bytes and exact claimed raw hash. Generated rates remain correct but omit those claims. A current 503 response and rounded current calcium display do not invalidate or replace the authenticated historical values.

### f3: Historical timestamp precision remains unresolved

minor / open / confirmed; issue key: brevibacillus-history-timestamp-shape.

Original malformed or timezone-absent history values remain unchanged and do not prove a precise execution chronology.

## Recommended Actions And Acceptance Checks

### a1

Add the source water batch input and exact preparation evidence to the appropriate maintained records, retain the existing correct DSMZ sentence, and regenerate through the conservative merge workflow without invented incubation conditions or final-volume claims.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Carry exact evidence and original access metadata through authorized regeneration or a narrowly reviewed retention fix, preserving primary batch amounts separately from provider-declared g_l values.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Append an evidenced clarification if available while retaining original historical values and exact raw recovery provenance.

- Do not invent UTC normalization or infer old execution from current source code.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch045/445/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch045/445/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml:1:id: CultureMech:003647<br>./data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml:1:id: CultureMech:003647<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch045/source-preflight-bound/445/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 13 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch045/445/grounding-inventory.json; Complete path-qualified sidecar | context_only | Every asserted ingredient primary/secondary/legacy slot in target and exact owners, full OLS scientific properties, current exact index rows and any unverified provider identifiers. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact asserted current secondary identifiers in pinned 9077-row label index | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:62946": [{"label": "(NH4)2 SO4", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2S4", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2SO4(Fisher A 702)", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ammonium Sulfate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium sulfate (2:1)", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium sulphate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "diammonium sulfate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "diazanium sulfate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "mascagnite", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid ammonium salt (1:2)", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid, diammonium salt", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulphate of ammonia", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH PO", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4 (0.4 g/l)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4 (7% w/v)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4(Sigma P 0662)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MKP", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium dihydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium monophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium orthophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Orthophosphoric acid, monopotassium salt", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid, monopotassium salt", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid, potassium salt (1:1)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium acid phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dihydrogen orthophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dihydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium Phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium phosphate monobasic", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sorensen's potassium phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "Manganese (II) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate hydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulfate--water (1/1)", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulphate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) sulfate monohydrate", "match_type": "ontology_label", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "manganese(II) sulphate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganous sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 x 1 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MnSO4 x 1 H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 · H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 ⋅ H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4.H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4·H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4⋅H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4・xH2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "bitter salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsom salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsomite", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate anhydrous", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulphate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium(II) sulfate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO .7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (100 mM)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O solution (25%)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O to 15.0 g).", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 ·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulphate of magnesia", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl 2 X 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2  x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x  2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (50 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (5M)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O solution (7%)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2. 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2.2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl22H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CaCl22H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}, {"label": "CaCl2x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2·2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O (Sigma C-3881)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(CAS: 10035-04-8)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(Sigma C-3881)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Calcium chloride dihydrate", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "calcium chloride dihydrate", "match_type": "ontology_label", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar  (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (BD)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "agar (BD-Difco)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Difco)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (if needed)*", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Molecular Genetics)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Purified)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar* (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Bacteriological Agar", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "legacy": []} |
| history-metadata | data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml; data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:05.576097"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:05.576097"}]}, {"input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml", "events": 7, "timestamp_issues": []}] |
| history-full | /private/tmp/culturemech-review-work-batch045/445/history-inventory.json; Complete path-qualified sidecar | context_only | Full target and maintained-owner history events retained without rewriting malformed or timezone-absent values. |
| historical-inventory | /private/tmp/culturemech-review-work-batch045/445/historical-evidence-inventory.json; Complete path-qualified sidecar | context_only | Exact attached claim objects and decoded historical report joins; a decoded match is not original API-response authentication. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf; Complete DSMZ 1064 recipe and preparation | supports | Seven ingredient masses, 1000 ml water, pH 5.5 and a printed 121-degree, 15-minute autoclave instruction are explicit. Listed water does not establish measured final volume. |
| historical-api | https://mediadive.dsmz.de/rest/medium/1064; $.data.medium; $.data.solutions[0].volume, recipe and steps | supports | Exact original October 7 raw response recovered from a pinned report. The declared volume 1000 ml and exact g_l values authenticate fourteen attached owner amount claims. Original access time 2026-10-07T13:16:48.541400+00:00 is retained separately from current requests. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact seven-column catalog header and medium 1064 row | supports | KOMODO 1064 explicitly links DSMZ 1064; the exact identity snippet/hash is authenticated by the retained catalog bytes. The current catalog access date is distinct from the historical claim timestamp. Is Aerobic=false is catalog metadata, not an experimental strict-anaerobic requirement. |
| current-provider | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1064; Complete current medium 1064 header and metabolite rows | supports | The current display rounds calcium chloride dihydrate to 0.01 g/L; retain the exact 12.5 mg primary amount and historical 0.0125 g/L instead of replacing them with display precision. |
| mediadive1064api-attempt | https://mediadive.dsmz.de/rest/medium/1064; Preserved exact public retrieval result | context_only | Current exact MediaDive 1064 returned HTTP 503. Exact historical raw and the complete collection primary are available, so this optional refresh failure does not make historical authentication partial. |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current merger uses conservative scientific-field equality. Preserve already-correct owner evidence and the DSMZ preparation text when repairing maintained inputs and reconciling generated freshness; no historical execution or current blind set-based merging is inferred. |
| writer-1 | src/culturemech/merge/merge_recipes.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current merger uses conservative scientific-field equality. Preserve already-correct owner evidence and the DSMZ preparation text when repairing maintained inputs and reconciling generated freshness; no historical execution or current blind set-based merging is inferred. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current merger uses conservative scientific-field equality. Preserve already-correct owner evidence and the DSMZ preparation text when repairing maintained inputs and reconciling generated freshness; no historical execution or current blind set-based merging is inferred. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch045/445/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Current exact MediaDive 1064 returned HTTP 503. Exact historical raw and the complete collection primary are available, so this optional refresh failure does not make historical authentication partial.
- Current KOMODO oxygen metadata is not treated as a required anaerobic culture condition. The exact printed autoclave temperature is 121°; the missing C letter remains a source unit-specificity limitation, not a replacement recipe instruction.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T021338Z-culturemech-003647-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: brevibacillus_levickii_medium (CultureMech:003647)'
started_at: '2026-10-22T02:02:39Z'
finished_at: '2026-10-22T02:13:38Z'
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
summary: DSMZ 1064 and the exact recovered historical API support all seven retained
  provider-declared rates, including the manganese and calcium milligram conversions.
  All layers omit 1000 ml water; the generated record and KOMODO owner omit the DSMZ
  owner preparation sentence. Authenticated owner amount evidence is also absent from
  the generated descriptors.
source:
  git_revision: 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
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
  - path: data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml
    sha256: 8be2e5f98ebbaa4fc3240db255f44b377cc1ef33414ee48ab1eb2a1098703ee6
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml
    sha256: e1155112450465c131a93ef59b47574748683273db11b6221af33a1f8fa1a9d4
    role: context
  - path: data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml
    sha256: 63a8d519fefd9565082e5e7de58ca5093bb6085439de06ec8da39ef170d3e646
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json
    sha256: 0bb2da58a82dc2b4a90beef1224a7355fd5632db772be0ef053bde40754ded87
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json
    sha256: 1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml.md
    sha256: 3e12d072c510707791a4ee5a303cfa58d0282fc5a89b0bab427860212b0df60f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
    sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/brevibacillus_levickii_medium.yaml.md
    sha256: 0c40613f3c0adb749b564d9d8d8a5065ac4f0366335e581ff6da97e2f6bb2677
    role: context
  - path: reports/yaml_record_review/20260922T002159Z-BREVIBACILLUS_LEVICKII_MEDIUM.md
    sha256: 9a2099030422b7702952f19e34eef97dcc32231990a65c28188f2bee51581ca0
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 445; batch 045 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding forty-four task batches
    contain 440 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 443 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003647
targets:
- target_id: CultureMech:003647
  path: data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml
  label: brevibacillus_levickii_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003647
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch045/445/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch045/445/strict.tsv"
  target_ids:
  - CultureMech:003647
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003647
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003647
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
  - CultureMech:003647
- check_id: mediadive1064api-source-access
  name: 'Exact source content access: mediadive1064api'
  required: false
  status: unavailable
  summary: Current exact MediaDive 1064 returned HTTP 503. Exact historical raw and
    the complete collection primary are available, so this optional refresh failure
    does not make historical authentication partial.
  target_ids:
  - CultureMech:003647
  evidence_ids:
  - mediadive1064api-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T02:13:37Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:13:37Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:13:37Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:24.051962Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch045/445/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:25.509893Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch045/445/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:27.311214Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:28.318882Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T02:13:37Z'
  support: supports
  summary: './data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml:1:id: CultureMech:003647

    ./data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml:1:id:
    CultureMech:003647

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/source-preflight-bound/445/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T02:13:37Z'
  support: supports
  summary: 13 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 4583648e0d7aeff6e5245253286d3a6f5c715e6111d76c1228b4bb389d20defb
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/445/grounding-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:13:37Z'
  support: context_only
  summary: Every asserted ingredient primary/secondary/legacy slot in target and exact
    owners, full OLS scientific properties, current exact index rows and any unverified
    provider identifiers.
  snapshot_sha256: dd7a73844b6a58754dd9ccde6703e617fab2ff49933fe4be236fc921d053f8f0
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:43:08.324907Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi86364
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T07:33:35.036768Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:43:09.378884Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:37.629610Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact asserted current secondary identifiers in pinned 9077-row label index
  accessed_at: '2026-10-22T02:13:37Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:62946":
    [{"label": "(NH4)2 SO4", "match_type": "synonym", "identifier": "CHEBI:62946",
    "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2S4", "match_type": "synonym",
    "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4",
    "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "(NH4)2SO4(Fisher A 702)", "match_type": "synonym", "identifier": "CHEBI:62946",
    "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Ammonium Sulfate", "match_type":
    "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id":
    "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium
    sulfate (2:1)", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term":
    "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ammonium sulphate", "match_type": "synonym", "identifier":
    "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "diammonium sulfate", "match_type":
    "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id":
    "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "diazanium
    sulfate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term":
    "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "mascagnite", "match_type": "synonym", "identifier": "CHEBI:62946",
    "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid ammonium salt (1:2)",
    "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4",
    "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "sulfuric acid, diammonium salt", "match_type": "synonym", "identifier":
    "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sulphate of ammonia", "match_type":
    "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id":
    "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036":
    [{"label": "KH PO", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "KH2PO4 (0.4 g/l)", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4 (7% w/v)",
    "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4",
    "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "KH2PO4(Sigma P 0662)", "match_type": "synonym", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MKP", "match_type": "synonym", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium dihydrogen phosphate",
    "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4",
    "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Monopotassium monophosphate", "match_type": "synonym", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium orthophosphate", "match_type":
    "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium
    phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Orthophosphoric acid, monopotassium salt", "match_type":
    "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric
    acid, monopotassium salt", "match_type": "synonym", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Phosphoric acid, potassium salt (1:1)", "match_type":
    "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium
    acid phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Potassium dihydrogen orthophosphate", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dihydrogen
    phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Potassium Phosphate", "match_type": "synonym", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Potassium phosphate monobasic", "match_type":
    "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sorensen''s
    potassium phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86364": [{"label": "Manganese (II) sulfate monohydrate", "match_type":
    "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese
    sulfate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Manganese sulfate hydrate", "match_type": "synonym", "identifier":
    "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate
    monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "manganese(2+) sulfate monohydrate", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulfate--water
    (1/1)", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "manganese(2+) sulphate monohydrate", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) sulfate
    monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "manganese(II) sulfate monohydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "manganese(II) sulphate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364",
    "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Manganous sulfate monohydrate", "match_type":
    "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4
    . H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnSO4 x 1 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MnSO4 x 1 H2O",
    "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4
    x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 · H2O", "match_type":
    "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4
    ⋅ H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnSO4.H2O", "match_type": "synonym", "identifier": "CHEBI:86364",
    "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4·H2O", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4⋅H2O", "match_type":
    "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4・xH2O",
    "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4
    x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity":
    "unique"}], "CHEBI:31795": [{"label": ".MgSO4", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "bitter salt", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "epsom salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "epsomite", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate
    anhydrous", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Magnesium sulfate heptahydrate", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium
    sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate",
    "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water
    (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water
    (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "magnesium sulphate", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate
    heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium(II) sulfate",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO .7H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO
    4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO
    4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2·7H2O", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4
    . 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4
    x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (0.1%
    w/v)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgSO4 x 7 H2O (100 mM)", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O solution (25%)",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "MgSO4 x 7 H2O to 15.0 g).", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "MgSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 · 7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "MgSO4 ·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgSO47H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma
    230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS:
    10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma
    230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "sulfuric acid magnesium salt", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric
    acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "sulphate of magnesia", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl 2 X 2 H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2  x 2 H2O", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 . 2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 x  2 H2O", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (50
    g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 x 2 H2O (5M)", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O solution
    (7%)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2
    · 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2. 2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2.2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl22H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CaCl22H2O", "match_type":
    "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}, {"label":
    "CaCl2x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2·2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2•2H2O (Sigma C-3881)", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(CAS:
    10035-04-8)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2•2H2O(Sigma C-3881)", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Calcium chloride
    dihydrate", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "calcium chloride dihydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "calcium chloride--water
    (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:2509": [{"label":
    "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term":
    "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Agar  (if needed)", "match_type": "synonym", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Agar (BD)", "match_type": "synonym",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "agar (BD-Difco)",
    "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar",
    "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Agar (Difco)", "match_type": "synonym", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Agar (if needed)", "match_type": "synonym",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (if needed)*",
    "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar",
    "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Agar (Molecular Genetics)", "match_type": "synonym", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Purified)", "match_type": "synonym",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar* (if needed)",
    "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar",
    "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Bacteriological Agar", "match_type": "synonym", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, "legacy": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml;
    data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T02:13:37Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:05.576097"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:05.576097"}]}, {"input": "data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: history-full
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/445/history-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:13:37Z'
  support: context_only
  summary: Full target and maintained-owner history events retained without rewriting
    malformed or timezone-absent values.
  snapshot_sha256: 4a98932e9f4a7d53382a43fb714d2f8f27f6166d07861f6225bde2e1620fb31a
- evidence_id: historical-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/445/historical-evidence-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:13:37Z'
  support: context_only
  summary: Exact attached claim objects and decoded historical report joins; a decoded
    match is not original API-response authentication.
  snapshot_sha256: 279e80d34c8553c079bc47c2313631f622ef55c1053bccc0318bbecbc5c82696
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf
  locator: Complete DSMZ 1064 recipe and preparation
  accessed_at: '2026-10-22T01:49:20.215611Z'
  support: supports
  summary: Seven ingredient masses, 1000 ml water, pH 5.5 and a printed 121-degree,
    15-minute autoclave instruction are explicit. Listed water does not establish
    measured final volume.
  quote: 1064. BREVIBACILLUS LEVICKII MEDIUM
  snapshot_sha256: 6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02
- evidence_id: historical-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1064
  locator: $.data.medium; $.data.solutions[0].volume, recipe and steps
  accessed_at: '2026-10-07T13:16:48.541400Z'
  support: supports
  summary: Exact original October 7 raw response recovered from a pinned report. The
    declared volume 1000 ml and exact g_l values authenticate fourteen attached owner
    amount claims. Original access time 2026-10-07T13:16:48.541400+00:00 is retained
    separately from current requests.
  snapshot_sha256: 2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact seven-column catalog header and medium 1064 row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: KOMODO 1064 explicitly links DSMZ 1064; the exact identity snippet/hash
    is authenticated by the retained catalog bytes. The current catalog access date
    is distinct from the historical claim timestamp. Is Aerobic=false is catalog metadata,
    not an experimental strict-anaerobic requirement.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: current-provider
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1064
  locator: Complete current medium 1064 header and metabolite rows
  accessed_at: '2026-10-22T01:51:12.374547Z'
  support: supports
  summary: The current display rounds calcium chloride dihydrate to 0.01 g/L; retain
    the exact 12.5 mg primary amount and historical 0.0125 g/L instead of replacing
    them with display precision.
  snapshot_sha256: 1ef75163a0569d2fb268242d4ca79637047653cd1ea2e509e552d2fc5ef1722b
- evidence_id: mediadive1064api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1064
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T01:49:20.370246Z'
  support: context_only
  summary: Current exact MediaDive 1064 returned HTTP 503. Exact historical raw and
    the complete collection primary are available, so this optional refresh failure
    does not make historical authentication partial.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:13:37Z'
  support: context_only
  summary: The current merger uses conservative scientific-field equality. Preserve
    already-correct owner evidence and the DSMZ preparation text when repairing maintained
    inputs and reconciling generated freshness; no historical execution or current
    blind set-based merging is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merge_recipes.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:13:37Z'
  support: context_only
  summary: The current merger uses conservative scientific-field equality. Preserve
    already-correct owner evidence and the DSMZ preparation text when repairing maintained
    inputs and reconciling generated freshness; no historical execution or current
    blind set-based merging is inferred.
  snapshot_sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:13:37Z'
  support: context_only
  summary: The current merger uses conservative scientific-field equality. Preserve
    already-correct owner evidence and the DSMZ preparation text when repairing maintained
    inputs and reconciling generated freshness; no historical execution or current
    blind set-based merging is inferred.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/445/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T02:13:37Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 1fb389a070706354964176e895431cd59c0a967df7ef1782a6f5d4d594004a36
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003647
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Complete current ontology and secondary linkage inventory
  outcome: supported
  summary: 6 distinct bound ontology IDs resolve and are nonobsolete. 0 literal canonical-label
    mismatches, 0 unverified provider slots and 0 legacy slots are retained explicitly.
    6/6 asserted current secondary keys have exact pinned index rows. Target primary
    linkage is 6/7 (85.71%) and current secondary linkage is 6/7 (85.71%) on a 0–100
    linkage scale, not a correctness score. Current missing keys do not prove historical
    invalidity; compatible generic source wording does not establish a stereochemical
    conflict.
  target_ids:
  - CultureMech:003647
  evidence_ids:
  - grounding-inventory
  - mim
  - chebi62946
  - chebi63036
  - chebi86364
  - chebi31795
  - chebi86158
  - chebi2509
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 24 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003647
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: identity
  area: identity
  topic: Exact source-duplicate identity with separate evidence roles
  outcome: supported
  summary: Both maintained owners and the generated record identify accession 1064,
    and the source-duplicate relationship agrees with the exact catalog link and primary
    title. Agar 18 g supports the retained solid branch and yeast extract supports
    complex composition. Collection title and catalog oxygen metadata do not supply
    a strain-specific growth claim or strict anaerobic requirement.
  target_ids:
  - CultureMech:003647
  evidence_ids:
  - primary
  - catalog
  - record
  - owner-0
  - owner-1
- assessment_id: amounts
  area: quantity
  topic: Exact historical provider rates and primary mass conversions
  outcome: supported
  summary: The raw API declares volume 1000 ml and g_l values matching all seven local
    rates. Manganese sulfate monohydrate 2.50 mg converts to 0.0025 g, and calcium
    chloride dihydrate 12.50 mg to 0.0125 g; the API separately supplies those rates.
    All fourteen owner amount snippets and cited hashes authenticate. The PDF corroborates
    nominal batch masses without proving measured final volume.
  target_ids:
  - CultureMech:003647
  evidence_ids:
  - primary
  - historical-api
  - historical-inventory
- assessment_id: preparation
  area: representation
  topic: Missing water and lost preparation despite correct pH
  outcome: concern
  summary: All three layers omit the primary 1000 ml water input. The scalar pH 5.5
    is correct throughout; only the DSMZ owner retains the printed pH adjustment and
    121-degree/15-minute autoclave sentence. The PDF and historical API print 121°
    without an explicit C letter; retain that source wording rather than silently
    increasing its unit specificity. No incubation temperature or titrant dose is
    given.
  target_ids:
  - CultureMech:003647
  evidence_ids:
  - primary
  - historical-api
  - record
  - owner-0
  - owner-1
- assessment_id: chemical-forms
  area: grounding
  topic: Exact supported salt and hydrate identities
  outcome: supported
  summary: Ammonium sulfate, potassium dihydrogen phosphate, manganese(II) sulfate
    monohydrate, magnesium sulfate heptahydrate and calcium chloride dihydrate agree
    with the primary supplied forms and bound ontology scientific properties. Yeast
    extract remains an ungrounded complex descriptor; no invented exact chemical identity
    or supplier composition is assigned. Current provider aggregate ions and rounded
    molar displays are not substitute formulation inputs.
  target_ids:
  - CultureMech:003647
  evidence_ids:
  - primary
  - grounding-inventory
  - current-provider
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 21 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003647
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"Yeast extract\
    \ generated rate\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Yeast\
    \ extract'\",\n        \"exact_source_quote\": \"Yeast extract               \
    \                             2.00    g\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 2,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\
    \n      }\n    ],\n    \"rationale\": \"The exact local value and G_PER_L basis\
    \ match authenticated provider-declared g_l, but the generated descriptor lacks\
    \ the attached matching amount claim. This is provider-declared normalization,\
    \ not independently measured final volume.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q2\",\n    \"subject\": \"Yeast extract maintained rates\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Yeast\
    \ extract'\",\n        \"exact_source_quote\": \"Yeast extract               \
    \                             2.00    g\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 2,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\
    \n      }\n    ],\n    \"rationale\": \"Both maintained descriptors retain the\
    \ exact supporting excerpt, original hash and source metadata, reauthenticated\
    \ against recovered raw. The provider explicitly declares this g_l value. Preserve\
    \ the separate primary batch and provider-rate bases.\"\n  },\n  {\n    \"decision_id\"\
    : \"q3\",\n    \"subject\": \"(NH4)2SO4 generated rate\",\n    \"decision\": \"\
    evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing '(NH4)2SO4'\"\
    ,\n        \"exact_source_quote\": \"(NH4)2SO4                               \
    \                 1.25    g\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 1.25,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.25,\\n \
    \                       \\\"mmol_l\\\": 9.45966,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\
    \n      }\n    ],\n    \"rationale\": \"The exact local value and G_PER_L basis\
    \ match authenticated provider-declared g_l, but the generated descriptor lacks\
    \ the attached matching amount claim. This is provider-declared normalization,\
    \ not independently measured final volume.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q4\",\n    \"subject\": \"(NH4)2SO4 maintained rates\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing '(NH4)2SO4'\"\
    ,\n        \"exact_source_quote\": \"(NH4)2SO4                               \
    \                 1.25    g\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 1.25,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.25,\\n \
    \                       \\\"mmol_l\\\": 9.45966,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\
    \n      }\n    ],\n    \"rationale\": \"Both maintained descriptors retain the\
    \ exact supporting excerpt, original hash and source metadata, reauthenticated\
    \ against recovered raw. The provider explicitly declares this g_l value. Preserve\
    \ the separate primary batch and provider-rate bases.\"\n  },\n  {\n    \"decision_id\"\
    : \"q5\",\n    \"subject\": \"KH2PO4 generated rate\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'KH2PO4'\"\
    ,\n        \"exact_source_quote\": \"KH2PO4                                  \
    \                 1.50    g\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 1.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n                \
    \        \\\"mmol_l\\\": 11.0225,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\
    \n      }\n    ],\n    \"rationale\": \"The exact local value and G_PER_L basis\
    \ match authenticated provider-declared g_l, but the generated descriptor lacks\
    \ the attached matching amount claim. This is provider-declared normalization,\
    \ not independently measured final volume.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q6\",\n    \"subject\": \"KH2PO4 maintained rates\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'KH2PO4'\"\
    ,\n        \"exact_source_quote\": \"KH2PO4                                  \
    \                 1.50    g\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 1.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n                \
    \        \\\"mmol_l\\\": 11.0225,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\
    \n      }\n    ],\n    \"rationale\": \"Both maintained descriptors retain the\
    \ exact supporting excerpt, original hash and source metadata, reauthenticated\
    \ against recovered raw. The provider explicitly declares this g_l value. Preserve\
    \ the separate primary batch and provider-rate bases.\"\n  },\n  {\n    \"decision_id\"\
    : \"q7\",\n    \"subject\": \"MnSO4 x H2O generated rate\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0025\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1064\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'MnSO4'\"\
    ,\n        \"exact_source_quote\": \"MnSO4 x H2O                             \
    \                 2.50   mg\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 2.5,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0025,\\\
    n                        \\\"mmol_l\\\": 0.0147915,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\n     \
    \ }\n    ],\n    \"rationale\": \"The exact local value and G_PER_L basis match\
    \ authenticated provider-declared g_l, but the generated descriptor lacks the\
    \ attached matching amount claim. The primary 2.50 mg equals 0.0025 g. This is\
    \ provider-declared normalization, not independently measured final volume.\"\n\
    \  },\n  {\n    \"decision_id\": \"q8\",\n    \"subject\": \"MnSO4 x H2O maintained\
    \ rates\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0025\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0025\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'MnSO4'\"\
    ,\n        \"exact_source_quote\": \"MnSO4 x H2O                             \
    \                 2.50   mg\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 2.5,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0025,\\\
    n                        \\\"mmol_l\\\": 0.0147915,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\n     \
    \ }\n    ],\n    \"rationale\": \"Both maintained descriptors retain the exact\
    \ supporting excerpt, original hash and source metadata, reauthenticated against\
    \ recovered raw. The provider explicitly declares this g_l value. The primary\
    \ 2.50 mg equals 0.0025 g. Preserve the separate primary batch and provider-rate\
    \ bases.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n    \"subject\": \"MgSO4\
    \ x 7 H2O generated rate\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'MgSO4'\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O                           \
    \                 0.10    g\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.405719,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\
    \n      }\n    ],\n    \"rationale\": \"The exact local value and G_PER_L basis\
    \ match authenticated provider-declared g_l, but the generated descriptor lacks\
    \ the attached matching amount claim. This is provider-declared normalization,\
    \ not independently measured final volume.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q10\",\n    \"subject\": \"MgSO4 x 7 H2O maintained rates\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'MgSO4'\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O                           \
    \                 0.10    g\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.405719,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\
    \n      }\n    ],\n    \"rationale\": \"Both maintained descriptors retain the\
    \ exact supporting excerpt, original hash and source metadata, reauthenticated\
    \ against recovered raw. The provider explicitly declares this g_l value. Preserve\
    \ the separate primary batch and provider-rate bases.\"\n  },\n  {\n    \"decision_id\"\
    : \"q11\",\n    \"subject\": \"CaCl2 x 2 H2O generated rate\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0125\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1064\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'CaCl2'\"\
    ,\n        \"exact_source_quote\": \"CaCl2 x 2 H2O                           \
    \                12.50   mg\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 12.5,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0125,\\\
    n                        \\\"mmol_l\\\": 0.0850253,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\n     \
    \ }\n    ],\n    \"rationale\": \"The exact local value and G_PER_L basis match\
    \ authenticated provider-declared g_l, but the generated descriptor lacks the\
    \ attached matching amount claim. The primary 12.50 mg equals 0.0125 g. This is\
    \ provider-declared normalization, not independently measured final volume.\"\n\
    \  },\n  {\n    \"decision_id\": \"q12\",\n    \"subject\": \"CaCl2 x 2 H2O maintained\
    \ rates\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0125\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0125\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'CaCl2'\"\
    ,\n        \"exact_source_quote\": \"CaCl2 x 2 H2O                           \
    \                12.50   mg\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 12.5,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0125,\\\
    n                        \\\"mmol_l\\\": 0.0850253,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\n     \
    \ }\n    ],\n    \"rationale\": \"Both maintained descriptors retain the exact\
    \ supporting excerpt, original hash and source metadata, reauthenticated against\
    \ recovered raw. The provider explicitly declares this g_l value. The primary\
    \ 12.50 mg equals 0.0125 g. Preserve the separate primary batch and provider-rate\
    \ bases.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"subject\": \"Agar\
    \ generated rate\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"18\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Agar'\"\
    ,\n        \"exact_source_quote\": \"Agar                                    \
    \                18.00    g\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\": 3,\\\
    n                        \\\"amount\\\": 18,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 18,\\n                 \
    \       \\\"mmol_l\\\": 53.5189,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\
    \n      }\n    ],\n    \"rationale\": \"The exact local value and G_PER_L basis\
    \ match authenticated provider-declared g_l, but the generated descriptor lacks\
    \ the attached matching amount claim. This is provider-declared normalization,\
    \ not independently measured final volume.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q14\",\n    \"subject\": \"Agar maintained rates\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"18\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"18\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Agar'\"\
    ,\n        \"exact_source_quote\": \"Agar                                    \
    \                18.00    g\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\": 3,\\\
    n                        \\\"amount\\\": 18,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 18,\\n                 \
    \       \\\"mmol_l\\\": 53.5189,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\
    \n      }\n    ],\n    \"rationale\": \"Both maintained descriptors retain the\
    \ exact supporting excerpt, original hash and source metadata, reauthenticated\
    \ against recovered raw. The provider explicitly declares this g_l value. Preserve\
    \ the separate primary batch and provider-rate bases.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"subject\": \"Missing source water input\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Yeast extract\",\n            \"concentration\"\
    : {\n              \"value\": \"2\",\n              \"unit\": \"G_PER_L\"\n  \
    \          }\n          },\n          {\n            \"preferred_term\": \"(NH4)2SO4\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:62946\",\n         \
    \     \"label\": \"ammonium sulfate\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"1.25\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:62946\",\n              \"label\": \"ammonium sulfate\"\n\
    \            }\n          },\n          {\n            \"preferred_term\": \"\
    KH2PO4\",\n            \"term\": {\n              \"id\": \"CHEBI:63036\",\n \
    \             \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"1.5\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"MnSO4 x H2O\",\n            \"term\": {\n          \
    \    \"id\": \"CHEBI:86364\",\n              \"label\": \"manganese(II) sulfate\
    \ monohydrate\"\n            },\n            \"concentration\": {\n          \
    \    \"value\": \"0.0025\",\n              \"unit\": \"G_PER_L\"\n           \
    \ },\n            \"mediaingredientmech_chebi_term\": {\n              \"id\"\
    : \"CHEBI:86364\",\n              \"label\": \"manganese(II) sulfate monohydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    MgSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31795\"\
    ,\n              \"label\": \"magnesium sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.1\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31795\",\n              \"label\": \"magnesium\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"CaCl2 x 2 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:86158\",\n              \"label\": \"calcium chloride dihydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.0125\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:86158\",\n\
    \              \"label\": \"calcium chloride dihydrate\"\n            }\n    \
    \      },\n          {\n            \"preferred_term\": \"Agar\",\n          \
    \  \"term\": {\n              \"id\": \"CHEBI:2509\",\n              \"label\"\
    : \"agar\"\n            },\n            \"concentration\": {\n              \"\
    value\": \"18\",\n              \"unit\": \"G_PER_L\"\n            },\n      \
    \      \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\"\
    ,\n              \"label\": \"agar\"\n            }\n          }\n        ]\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Yeast extract\",\n            \"concentration\"\
    : {\n              \"value\": \"2\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"evidence\": [\n              {\n                \"\
    reference\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n               \
    \ \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\n            \
    \            \\\"recipe_order\\\": 1,\\n                        \\\"compound\\\
    \": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\": 16,\\\
    n                        \\\"amount\\\": 2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 2,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[0].concentration (Yeast extract) in\
    \ MediaDive medium 1064; locator=$.data.solutions[0].recipe[0]. Provider explicitly\
    \ reports g_l=2; check: 2 g * 1 g/g / (1000 ml / 1000 ml per L) = 2 g/L. This\
    \ supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00;\
    \ response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\
    \ KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"(NH4)2SO4\",\n            \"term\": {\n              \"id\": \"CHEBI:62946\"\
    ,\n              \"label\": \"ammonium sulfate\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"1.25\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:62946\",\n              \"label\": \"ammonium\
    \ sulfate\"\n            },\n            \"evidence\": [\n              {\n  \
    \              \"reference\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n\
    \                \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\\
    n                        \\\"recipe_order\\\": 2,\\n                        \\\
    \"compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\
    \": 27,\\n                        \\\"amount\\\": 1.25,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.25,\\\
    n                        \\\"mmol_l\\\": 9.45966,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[1].concentration ((NH4)2SO4) in MediaDive\
    \ medium 1064; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports\
    \ g_l=1.25; check: 1.25 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.25 g/L. This\
    \ supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00;\
    \ response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\
    \ KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"KH2PO4\",\n            \"term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"1.5\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1064\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 3,\\n                      \
    \  \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 1.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n \
    \                       \\\"mmol_l\\\": 11.0225,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[2].concentration (KH2PO4) in MediaDive\
    \ medium 1064; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports\
    \ g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00;\
    \ response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\
    \ KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"MnSO4 x H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86364\"\
    ,\n              \"label\": \"manganese(II) sulfate monohydrate\"\n          \
    \  },\n            \"concentration\": {\n              \"value\": \"0.0025\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86364\",\n              \"label\": \"manganese(II)\
    \ sulfate monohydrate\"\n            },\n            \"evidence\": [\n       \
    \       {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1064\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 4,\\n                      \
    \  \\\"compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 2.5,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0025,\\\
    n                        \\\"mmol_l\\\": 0.0147915,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[3].concentration (MnSO4 x H2O) in MediaDive\
    \ medium 1064; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports\
    \ g_l=0.0025; check: 2.5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.0025\
    \ g/L. This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00;\
    \ response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\
    \ KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31795\"\
    ,\n              \"label\": \"magnesium sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.1\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31795\",\n              \"label\": \"magnesium\
    \ sulfate heptahydrate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1064\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 5,\\n                      \
    \  \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.405719,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[4].concentration (MgSO4 x 7 H2O) in MediaDive\
    \ medium 1064; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports\
    \ g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00;\
    \ response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\
    \ KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"CaCl2 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86158\"\
    ,\n              \"label\": \"calcium chloride dihydrate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"0.0125\",\n     \
    \         \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86158\",\n              \"label\": \"calcium\
    \ chloride dihydrate\"\n            },\n            \"evidence\": [\n        \
    \      {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1064\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 6,\\n                      \
    \  \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 12.5,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0125,\\\
    n                        \\\"mmol_l\\\": 0.0850253,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[5].concentration (CaCl2 x 2 H2O) in\
    \ MediaDive medium 1064; locator=$.data.solutions[0].recipe[5]. Provider explicitly\
    \ reports g_l=0.0125; check: 12.5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L)\
    \ = 0.0125 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\
    \ KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"18\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"mediaingredientmech_chebi_term\": {\n          \
    \    \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n            },\n\
    \            \"evidence\": [\n              {\n                \"reference\":\
    \ \"https://mediadive.dsmz.de/rest/medium/1064\",\n                \"supports\"\
    : \"SUPPORT\",\n                \"snippet\": \"{\\n                        \\\"\
    recipe_order\\\": 7,\\n                        \\\"compound\\\": \\\"Agar\\\"\
    ,\\n                        \\\"compound_id\\\": 3,\\n                       \
    \ \\\"amount\\\": 18,\\n                        \\\"unit\\\": \\\"g\\\",\\n  \
    \                      \\\"g_l\\\": 18,\\n                        \\\"mmol_l\\\
    \": 53.5189,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n                \"explanation\": \"Concentration evidence for ingredients[6].concentration\
    \ (Agar) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[6]. Provider\
    \ explicitly reports g_l=18; check: 18 g * 1 g/g / (1000 ml / 1000 ml per L) =\
    \ 18 g/L. This supports the provider-declared main-recipe concentration, not an\
    \ independently measured final volume, a stock composition, or a downstream assay\
    \ dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\
    \ KOMODO accession 1064 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          }\n        ]\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Yeast extract\",\n            \"concentration\"\
    : {\n              \"value\": \"2\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"evidence\": [\n              {\n                \"\
    reference\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n               \
    \ \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\n            \
    \            \\\"recipe_order\\\": 1,\\n                        \\\"compound\\\
    \": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\": 16,\\\
    n                        \\\"amount\\\": 2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 2,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[0].concentration (Yeast extract) in\
    \ MediaDive medium 1064; locator=$.data.solutions[0].recipe[0]. Provider explicitly\
    \ reports g_l=2; check: 2 g * 1 g/g / (1000 ml / 1000 ml per L) = 2 g/L. This\
    \ supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00;\
    \ response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"(NH4)2SO4\",\n            \"term\": {\n              \"id\": \"CHEBI:62946\"\
    ,\n              \"label\": \"ammonium sulfate\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"1.25\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:62946\",\n              \"label\": \"ammonium\
    \ sulfate\"\n            },\n            \"evidence\": [\n              {\n  \
    \              \"reference\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n\
    \                \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\\
    n                        \\\"recipe_order\\\": 2,\\n                        \\\
    \"compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\
    \": 27,\\n                        \\\"amount\\\": 1.25,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.25,\\\
    n                        \\\"mmol_l\\\": 9.45966,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[1].concentration ((NH4)2SO4) in MediaDive\
    \ medium 1064; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports\
    \ g_l=1.25; check: 1.25 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.25 g/L. This\
    \ supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00;\
    \ response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"KH2PO4\",\n            \"term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"1.5\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1064\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 3,\\n                      \
    \  \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 1.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n \
    \                       \\\"mmol_l\\\": 11.0225,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[2].concentration (KH2PO4) in MediaDive\
    \ medium 1064; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports\
    \ g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00;\
    \ response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"MnSO4 x H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86364\"\
    ,\n              \"label\": \"manganese(II) sulfate monohydrate\"\n          \
    \  },\n            \"concentration\": {\n              \"value\": \"0.0025\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86364\",\n              \"label\": \"manganese(II)\
    \ sulfate monohydrate\"\n            },\n            \"evidence\": [\n       \
    \       {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1064\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 4,\\n                      \
    \  \\\"compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 2.5,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0025,\\\
    n                        \\\"mmol_l\\\": 0.0147915,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[3].concentration (MnSO4 x H2O) in MediaDive\
    \ medium 1064; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports\
    \ g_l=0.0025; check: 2.5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.0025\
    \ g/L. This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00;\
    \ response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31795\"\
    ,\n              \"label\": \"magnesium sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.1\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31795\",\n              \"label\": \"magnesium\
    \ sulfate heptahydrate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1064\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 5,\\n                      \
    \  \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.405719,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[4].concentration (MgSO4 x 7 H2O) in MediaDive\
    \ medium 1064; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports\
    \ g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:16:48.541400+00:00;\
    \ response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"CaCl2 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86158\"\
    ,\n              \"label\": \"calcium chloride dihydrate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"0.0125\",\n     \
    \         \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86158\",\n              \"label\": \"calcium\
    \ chloride dihydrate\"\n            },\n            \"evidence\": [\n        \
    \      {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1064\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 6,\\n                      \
    \  \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 12.5,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0125,\\\
    n                        \\\"mmol_l\\\": 0.0850253,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[5].concentration (CaCl2 x 2 H2O) in\
    \ MediaDive medium 1064; locator=$.data.solutions[0].recipe[5]. Provider explicitly\
    \ reports g_l=0.0125; check: 12.5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L)\
    \ = 0.0125 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"18\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"mediaingredientmech_chebi_term\": {\n          \
    \    \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n            },\n\
    \            \"evidence\": [\n              {\n                \"reference\":\
    \ \"https://mediadive.dsmz.de/rest/medium/1064\",\n                \"supports\"\
    : \"SUPPORT\",\n                \"snippet\": \"{\\n                        \\\"\
    recipe_order\\\": 7,\\n                        \\\"compound\\\": \\\"Agar\\\"\
    ,\\n                        \\\"compound_id\\\": 3,\\n                       \
    \ \\\"amount\\\": 18,\\n                        \\\"unit\\\": \\\"g\\\",\\n  \
    \                      \\\"g_l\\\": 18,\\n                        \\\"mmol_l\\\
    \": 53.5189,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n                \"explanation\": \"Concentration evidence for ingredients[6].concentration\
    \ (Agar) in MediaDive medium 1064; locator=$.data.solutions[0].recipe[6]. Provider\
    \ explicitly reports g_l=18; check: 18 g * 1 g/g / (1000 ml / 1000 ml per L) =\
    \ 18 g/L. This supports the provider-declared main-recipe concentration, not an\
    \ independently measured final volume, a stock composition, or a downstream assay\
    \ dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:16:48.541400+00:00; response SHA256=2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6.\"\
    \n              }\n            ]\n          }\n        ]\n      }\n    ],\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1064\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Distilled\
    \ water'\",\n        \"exact_source_quote\": \"Distilled water               \
    \                        1000.00   ml\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      },\n      {\n        \"source_key\": \"historical1064api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1064\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"2b88d39bec3542bf25ad0e6bfe6146ec55f0392f67fa82d29fc5c72cad0007d6\"\
    \n      }\n    ],\n    \"rationale\": \"Add the exact 1000 ml water batch input.\
    \ Do not relabel it as a mass concentration or a measured final-volume instruction.\"\
    \n  },\n  {\n    \"decision_id\": \"q16\",\n    \"subject\": \"pH 5.5 endpoint\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 5.5\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 5.5\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 5.5\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1064\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Adjust\
    \ pH'\",\n        \"exact_source_quote\": \"Adjust pH to 5.5; autoclave at 121\
    \ for 15 minutes.\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      }\n    ],\n    \"rationale\": \"The scalar 5.5 agrees exactly with the\
    \ primary endpoint. Attach claim-level preparation evidence; catalog identity\
    \ evidence is not a preparation claim.\"\n  },\n  {\n    \"decision_id\": \"q17\"\
    ,\n    \"subject\": \"Missing generated and KOMODO preparation\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Adjust\
    \ pH'\",\n        \"exact_source_quote\": \"Adjust pH to 5.5; autoclave at 121\
    \ for 15 minutes.\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the primary adjustment to pH 5.5\
    \ and printed 121-degree, 15-minute autoclave instruction. The DSMZ owner already\
    \ preserves the same source sentence.\"\n  },\n  {\n    \"decision_id\": \"q18\"\
    ,\n    \"subject\": \"Existing DSMZ preparation sentence\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml\",\n       \
    \ \"field_path\": \"preparation_steps[0].description\",\n        \"stored\": \"\
    Adjust pH to 5.5; autoclave at 121° for 15 minutes.\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz1064\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Adjust\
    \ pH'\",\n        \"exact_source_quote\": \"Adjust pH to 5.5; autoclave at 121\
    \ for 15 minutes.\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      }\n    ],\n    \"rationale\": \"The existing sentence retains the matching\
    \ endpoint, printed 121° and 15-minute duration. Link exact primary support, preserving\
    \ the original glyph/unit limitation.\"\n  },\n  {\n    \"decision_id\": \"q19\"\
    ,\n    \"subject\": \"Autoclave duration 15 minutes\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 5.5; autoclave at 121° for 15 minutes.\"\n      }\n    ],\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1064\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Adjust\
    \ pH'\",\n        \"exact_source_quote\": \"Adjust pH to 5.5; autoclave at 121\
    \ for 15 minutes.\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      }\n    ],\n    \"rationale\": \"The source duration is explicitly 15 minutes\
    \ and correctly retained by the DSMZ owner. It is not a growth duration or a different\
    \ stock sterilization cycle.\"\n  },\n  {\n    \"decision_id\": \"q20\",\n   \
    \ \"subject\": \"Titrant amount\",\n    \"decision\": \"not_quantified\",\n  \
    \  \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Adjust\
    \ pH'\",\n        \"exact_source_quote\": \"Adjust pH to 5.5; autoclave at 121\
    \ for 15 minutes.\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      }\n    ],\n    \"rationale\": \"The pH endpoint is explicit but no fixed\
    \ titrant identity or dose is printed. Do not infer one.\"\n  },\n  {\n    \"\
    decision_id\": \"q21\",\n    \"subject\": \"Incubation temperature\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml\",\n        \"field_path\"\
    : \"temperature_value\",\n        \"stored\": null\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1064\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1064.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Adjust\
    \ pH'\",\n        \"exact_source_quote\": \"Adjust pH to 5.5; autoclave at 121\
    \ for 15 minutes.\",\n        \"snapshot_sha256\": \"6e53455cb6f760ad7bcf363991ee2257bba3f55714527590a668d78d68826c02\"\
    ,\n        \"parsed_text_sha256\": \"69d740be11bea90d93fbb9a89570cde3e4c1c49bfc3732eb735b2490657516fb\"\
    \n      }\n    ],\n    \"rationale\": \"The only printed temperature-like value\
    \ belongs to autoclaving. No growth/incubation temperature is supplied, so a generic\
    \ incubation value remains unsupported.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: brevibacillus-water-preparation-completeness
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Restore water and preserve source preparation
  description: The 1000 ml water input is absent from all three layers. The generated
    and KOMODO layers omit the pH/autoclave procedure that the DSMZ owner already
    retains; their scalar pH 5.5 remains correct.
  target_ids:
  - CultureMech:003647
  field_paths:
  - ingredients
  - preparation_steps
  evidence_ids:
  - primary
  - record
  - owner-0
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml
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
  issue_key: brevibacillus-generated-amount-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Preserve authenticated owner amount claims in the generated record
  description: All fourteen attached owner amount excerpts match the recovered October
    7 API bytes and exact claimed raw hash. Generated rates remain correct but omit
    those claims. A current 503 response and rounded current calcium display do not
    invalidate or replace the authenticated historical values.
  target_ids:
  - CultureMech:003647
  field_paths:
  - ingredients
  evidence_ids:
  - historical-api
  - historical-inventory
  - current-provider
  - record
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml
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
  issue_key: brevibacillus-history-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical timestamp precision remains unresolved
  description: Original malformed or timezone-absent history values remain unchanged
    and do not prove a precise execution chronology.
  target_ids:
  - CultureMech:003647
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  - history-full
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml
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
  description: Add the source water batch input and exact preparation evidence to
    the appropriate maintained records, retain the existing correct DSMZ sentence,
    and regenerate through the conservative merge workflow without invented incubation
    conditions or final-volume claims.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003647
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml
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
  description: Carry exact evidence and original access metadata through authorized
    regeneration or a narrowly reviewed retention fix, preserving primary batch amounts
    separately from provider-declared g_l values.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003647
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml
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
  description: Append an evidenced clarification if available while retaining original
    historical values and exact raw recovery provenance.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003647
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Do not invent UTC normalization or infer old execution from current source code.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- Current exact MediaDive 1064 returned HTTP 503. Exact historical raw and the complete
  collection primary are available, so this optional refresh failure does not make
  historical authentication partial.
- Current KOMODO oxygen metadata is not treated as a required anaerobic culture condition.
  The exact printed autoclave temperature is 121°; the missing C letter remains a
  source unit-specificity limitation, not a replacement recipe instruction.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-045
- generated-medium
```
