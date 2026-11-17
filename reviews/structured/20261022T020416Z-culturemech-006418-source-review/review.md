# Source and formulation review: bosea_thiooxidans_medium (CultureMech:006418)

- Review: 20261022T020416Z-culturemech-006418-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T02:02:36Z
- Finished UTC: 2026-10-22T02:04:16Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 763 and the exact recovered historical provider response support the seven retained ingredient rates and source identity. Both maintained owners omit the 1000 ml water input; the generated record also loses the owner preparation text and attached amount evidence. Catalog oxygen metadata and nonspecific chemical forms require bounded interpretation.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 441; batch 045 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-four task batches contain 440 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 443 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006418 | data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml | generated | bosea_thiooxidans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006418 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006418 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch045/441/strict.tsv |
| validate-terms | passed | True | CultureMech:006418 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006418 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006418 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive763api | unavailable | False | CultureMech:006418 | The current MediaDive 763 request returned HTTP 503. Exact historical raw is recovered and authenticated, so this optional current refresh failure does not make the historical amount check unavailable. |
| Exact source content access: komodoDetail763 | unavailable | False | CultureMech:006418 | The current exact KOMODO detail page returned HTTP 403. Exact catalog identity and independent primary plus historical formulation evidence remain usable. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006418.

The four documented recipes completed; interpret the scope of each separately.

### Complete current ontology and secondary linkage inventory

grounding: supported. Targets: CultureMech:006418.

6 distinct bound ontology IDs resolve and are nonobsolete. 0 literal canonical-label mismatches, 0 unverified provider slots and 0 legacy slots are retained explicitly. 6/6 asserted current secondary keys have exact pinned index rows. Target primary linkage is 6/7 (85.71%) and current secondary linkage is 6/7 (85.71%) on a 0–100 linkage scale, not a correctness score. Current missing keys do not prove historical invalidity; compatible generic source wording does not establish a stereochemical conflict.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006418.

27 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Same source accession with exact maintained ownership

identity: supported. Targets: CultureMech:006418.

The two maintained owners identify KOMODO 763 and DSMZ 763, with an explicit source-duplicate relationship and matching seven ingredient signatures. The exact catalog link and primary title support this source correspondence. No strain-resolved growth experiment, species-level guarantee or strict anaerobic requirement follows from the collection title or catalog flag.

### Provider-declared rates and primary batch quantities

quantity: supported. Targets: CultureMech:006418.

All seven nominal PDF masses correspond to the local numerals. Separately, the recovered API declares solution volume 1000 ml and exact g_l values, authenticating all fourteen attached owner amount excerpts. The target lacks those attached claims. This supports provider-declared rates without upgrading listed water to a measured final volume.

### Water and final pH completeness

representation: concern. Targets: CultureMech:006418.

The primary water input is absent from all three layers. Both owners and the target retain the structured pH range 7.5–8.5, while only the DSMZ owner has the preparation sentence. The source supplies no heating cycle, incubation temperature, gas composition or titrant dose; no conventional values are inferred.

### Supplied chemical forms and unresolved specificity

grounding: supported. Targets: CultureMech:006418.

The explicit anhydrous phosphate, magnesium chloride and thiosulfate pentahydrate names are compatible with their terms. CHEBI:64220 is stereo-unspecified monosodium glutamate, not a D- or L-specific contradiction. Sodium succinate is generic in the primary; the anhydrous disodium term is a specificity limitation rather than a demonstrated wrong identity. No hydrate or stereochemical replacement is inferred.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006418.

20 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "Na2HPO4 generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Na2HPO4'",
        "exact_source_quote": "Na2HPO4                                     4.0    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"mmol_l\": 28.1771,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "The exact value and G_PER_L basis match the authenticated provider-declared g_l value. The generated descriptor lacks the matching attached amount evidence retained by both owners. Add claim linkage without claiming an independently measured final volume."
  },
  {
    "decision_id": "q2",
    "subject": "Na2HPO4 maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Na2HPO4'",
        "exact_source_quote": "Na2HPO4                                     4.0    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"mmol_l\": 28.1771,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "Both maintained descriptors carry the exact matching amount excerpt, cited hash and original source metadata. The recovered response authenticates the provider-declared g_l basis; the PDF independently corroborates the nominal batch mass. Preserve that distinction."
  },
  {
    "decision_id": "q3",
    "subject": "KH2PO4 generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'KH2PO4'",
        "exact_source_quote": "KH2PO4                                      1.5    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 11.0225,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "The exact value and G_PER_L basis match the authenticated provider-declared g_l value. The generated descriptor lacks the matching attached amount evidence retained by both owners. Add claim linkage without claiming an independently measured final volume."
  },
  {
    "decision_id": "q4",
    "subject": "KH2PO4 maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'KH2PO4'",
        "exact_source_quote": "KH2PO4                                      1.5    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 11.0225,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "Both maintained descriptors carry the exact matching amount excerpt, cited hash and original source metadata. The recovered response authenticates the provider-declared g_l basis; the PDF independently corroborates the nominal batch mass. Preserve that distinction."
  },
  {
    "decision_id": "q5",
    "subject": "MgCl2 generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'MgCl2'",
        "exact_source_quote": "MgCl2                                       0.1    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2\",\n                        \"compound_id\": 453,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.05031,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "The exact value and G_PER_L basis match the authenticated provider-declared g_l value. The generated descriptor lacks the matching attached amount evidence retained by both owners. Add claim linkage without claiming an independently measured final volume."
  },
  {
    "decision_id": "q6",
    "subject": "MgCl2 maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'MgCl2'",
        "exact_source_quote": "MgCl2                                       0.1    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2\",\n                        \"compound_id\": 453,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.05031,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "Both maintained descriptors carry the exact matching amount excerpt, cited hash and original source metadata. The recovered response authenticates the provider-declared g_l basis; the PDF independently corroborates the nominal batch mass. Preserve that distinction."
  },
  {
    "decision_id": "q7",
    "subject": "Na glutamate generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Na-glutamate'",
        "exact_source_quote": "Na-glutamate                                0.5    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na glutamate\",\n                        \"compound_id\": 839,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.95664,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "The exact value and G_PER_L basis match the authenticated provider-declared g_l value. The generated descriptor lacks the matching attached amount evidence retained by both owners. Add claim linkage without claiming an independently measured final volume."
  },
  {
    "decision_id": "q8",
    "subject": "Na glutamate maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Na-glutamate'",
        "exact_source_quote": "Na-glutamate                                0.5    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na glutamate\",\n                        \"compound_id\": 839,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.95664,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "Both maintained descriptors carry the exact matching amount excerpt, cited hash and original source metadata. The recovered response authenticates the provider-declared g_l basis; the PDF independently corroborates the nominal batch mass. Preserve that distinction."
  },
  {
    "decision_id": "q9",
    "subject": "Yeast extract generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Yeast extract'",
        "exact_source_quote": "Yeast extract                               0.1    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "The exact value and G_PER_L basis match the authenticated provider-declared g_l value. The generated descriptor lacks the matching attached amount evidence retained by both owners. Add claim linkage without claiming an independently measured final volume."
  },
  {
    "decision_id": "q10",
    "subject": "Yeast extract maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Yeast extract'",
        "exact_source_quote": "Yeast extract                               0.1    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "Both maintained descriptors carry the exact matching amount excerpt, cited hash and original source metadata. The recovered response authenticates the provider-declared g_l basis; the PDF independently corroborates the nominal batch mass. Preserve that distinction."
  },
  {
    "decision_id": "q11",
    "subject": "Na2S2O3 x 5 H2O generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Na2S2O3'",
        "exact_source_quote": "Na2S2O3 x 5 H2O                             5.0    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\": 65,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 20.1462,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "The exact value and G_PER_L basis match the authenticated provider-declared g_l value. The generated descriptor lacks the matching attached amount evidence retained by both owners. Add claim linkage without claiming an independently measured final volume."
  },
  {
    "decision_id": "q12",
    "subject": "Na2S2O3 x 5 H2O maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Na2S2O3'",
        "exact_source_quote": "Na2S2O3 x 5 H2O                             5.0    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\": 65,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 20.1462,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "Both maintained descriptors carry the exact matching amount excerpt, cited hash and original source metadata. The recovered response authenticates the provider-declared g_l basis; the PDF independently corroborates the nominal batch mass. Preserve that distinction."
  },
  {
    "decision_id": "q13",
    "subject": "Sodium succinate generated rate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Na-succinate'",
        "exact_source_quote": "Na-succinate                                5.0    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sodium succinate\",\n                        \"compound_id\": 730,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 30.8547,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "The exact value and G_PER_L basis match the authenticated provider-declared g_l value. The generated descriptor lacks the matching attached amount evidence retained by both owners. Add claim linkage without claiming an independently measured final volume."
  },
  {
    "decision_id": "q14",
    "subject": "Sodium succinate maintained rates",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Na-succinate'",
        "exact_source_quote": "Na-succinate                                5.0    g",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sodium succinate\",\n                        \"compound_id\": 730,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 30.8547,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "Both maintained descriptors carry the exact matching amount excerpt, cited hash and original source metadata. The recovered response authenticates the provider-declared g_l basis; the PDF independently corroborates the nominal batch mass. Preserve that distinction."
  },
  {
    "decision_id": "q15",
    "subject": "Missing source water input",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Na2HPO4",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "4",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
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
            "preferred_term": "MgCl2",
            "term": {
              "id": "CHEBI:6636",
              "label": "magnesium dichloride"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:6636",
              "label": "magnesium dichloride"
            }
          },
          {
            "preferred_term": "Na glutamate",
            "term": {
              "id": "CHEBI:64220",
              "label": "monosodium glutamate"
            },
            "concentration": {
              "value": "0.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:64220",
              "label": "monosodium glutamate"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Na2S2O3 x 5 H2O",
            "term": {
              "id": "CHEBI:32150",
              "label": "sodium thiosulfate pentahydrate"
            },
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32150",
              "label": "sodium thiosulfate pentahydrate"
            }
          },
          {
            "preferred_term": "Sodium succinate",
            "term": {
              "id": "CHEBI:63675",
              "label": "sodium succinate (anhydrous)"
            },
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63675",
              "label": "sodium succinate (anhydrous)"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Na2HPO4",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "4",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"mmol_l\": 28.1771,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[0].concentration (Na2HPO4) in MediaDive medium 763; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=4; check: 4 g * 1 g/g / (1000 ml / 1000 ml per L) = 4 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207. KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
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
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 11.0225,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[1].concentration (KH2PO4) in MediaDive medium 763; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207. KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "MgCl2",
            "term": {
              "id": "CHEBI:6636",
              "label": "magnesium dichloride"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:6636",
              "label": "magnesium dichloride"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2\",\n                        \"compound_id\": 453,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.05031,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[2].concentration (MgCl2) in MediaDive medium 763; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207. KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "Na glutamate",
            "term": {
              "id": "CHEBI:64220",
              "label": "monosodium glutamate"
            },
            "concentration": {
              "value": "0.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:64220",
              "label": "monosodium glutamate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na glutamate\",\n                        \"compound_id\": 839,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.95664,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[3].concentration (Na glutamate) in MediaDive medium 763; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207. KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[4].concentration (Yeast extract) in MediaDive medium 763; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207. KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "Na2S2O3 x 5 H2O",
            "term": {
              "id": "CHEBI:32150",
              "label": "sodium thiosulfate pentahydrate"
            },
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32150",
              "label": "sodium thiosulfate pentahydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\": 65,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 20.1462,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[5].concentration (Na2S2O3 x 5 H2O) in MediaDive medium 763; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=5; check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207. KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "Sodium succinate",
            "term": {
              "id": "CHEBI:63675",
              "label": "sodium succinate (anhydrous)"
            },
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63675",
              "label": "sodium succinate (anhydrous)"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sodium succinate\",\n                        \"compound_id\": 730,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 30.8547,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[6].concentration (Sodium succinate) in MediaDive medium 763; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports g_l=5; check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207. KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Na2HPO4",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "4",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"mmol_l\": 28.1771,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[0].concentration (Na2HPO4) in MediaDive medium 763; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=4; check: 4 g * 1 g/g / (1000 ml / 1000 ml per L) = 4 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207."
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
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 11.0225,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[1].concentration (KH2PO4) in MediaDive medium 763; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207."
              }
            ]
          },
          {
            "preferred_term": "MgCl2",
            "term": {
              "id": "CHEBI:6636",
              "label": "magnesium dichloride"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:6636",
              "label": "magnesium dichloride"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2\",\n                        \"compound_id\": 453,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.05031,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[2].concentration (MgCl2) in MediaDive medium 763; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207."
              }
            ]
          },
          {
            "preferred_term": "Na glutamate",
            "term": {
              "id": "CHEBI:64220",
              "label": "monosodium glutamate"
            },
            "concentration": {
              "value": "0.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:64220",
              "label": "monosodium glutamate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na glutamate\",\n                        \"compound_id\": 839,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.95664,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[3].concentration (Na glutamate) in MediaDive medium 763; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207."
              }
            ]
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[4].concentration (Yeast extract) in MediaDive medium 763; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207."
              }
            ]
          },
          {
            "preferred_term": "Na2S2O3 x 5 H2O",
            "term": {
              "id": "CHEBI:32150",
              "label": "sodium thiosulfate pentahydrate"
            },
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32150",
              "label": "sodium thiosulfate pentahydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\": 65,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 20.1462,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[5].concentration (Na2S2O3 x 5 H2O) in MediaDive medium 763; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=5; check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207."
              }
            ]
          },
          {
            "preferred_term": "Sodium succinate",
            "term": {
              "id": "CHEBI:63675",
              "label": "sodium succinate (anhydrous)"
            },
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63675",
              "label": "sodium succinate (anhydrous)"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/763",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sodium succinate\",\n                        \"compound_id\": 730,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 30.8547,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[6].concentration (Sodium succinate) in MediaDive medium 763; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports g_l=5; check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207."
              }
            ]
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Distilled water'",
        "exact_source_quote": "Distilled water                          1000.0   ml",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      },
      {
        "source_key": "historical763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/763",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207"
      }
    ],
    "rationale": "Represent the explicit 1000 ml water batch input, not 1000 g/L or a measured final-volume statement."
  },
  {
    "decision_id": "q16",
    "subject": "Final pH range",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.5,
          "max": 8.5
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.5,
          "max": 8.5
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.5,
          "max": 8.5
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Final pH'",
        "exact_source_quote": "Final pH 7.5-8.5.",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      }
    ],
    "rationale": "The existing 7.5–8.5 range matches the primary. Add direct claim-level support; the catalog identity snippet is not a preparation claim."
  },
  {
    "decision_id": "q17",
    "subject": "Generated and KOMODO preparation sentence",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Final pH'",
        "exact_source_quote": "Final pH 7.5-8.5.",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      }
    ],
    "rationale": "Preserve the source final-pH instruction at the maintained and generated layers. The DSMZ owner already retains this sentence."
  },
  {
    "decision_id": "q18",
    "subject": "Existing DSMZ preparation sentence",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Final pH 7.5-8.5."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Final pH'",
        "exact_source_quote": "Final pH 7.5-8.5.",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      }
    ],
    "rationale": "Retain this existing matching preparation text and link the exact primary evidence."
  },
  {
    "decision_id": "q19",
    "subject": "Titrant dose",
    "decision": "not_quantified",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Final pH'",
        "exact_source_quote": "Final pH 7.5-8.5.",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      }
    ],
    "rationale": "The endpoint range is explicit but no fixed titrant or dose is specified. No amount is invented."
  },
  {
    "decision_id": "q20",
    "subject": "Incubation or sterilization parameters",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz763",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf",
        "source_locator": "Exact extracted source line containing 'Final pH'",
        "exact_source_quote": "Final pH 7.5-8.5.",
        "snapshot_sha256": "81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da",
        "parsed_text_sha256": "7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165"
      }
    ],
    "rationale": "The complete primary gives no incubation temperature, heating temperature or duration. Absence is not an explicit no-fixed-value instruction."
  }
]

## Findings

### f1: Restore the source water input and retain preparation scope

major / open / confirmed; issue key: bosea-water-and-preparation.

All layers omit 1000 ml water; the generated record and KOMODO owner lack the preparation sentence retained by the DSMZ owner. The pH range itself is correct.

### f2: Retain authenticated owner amount evidence in generated output

major / open / confirmed; issue key: bosea-generated-evidence-retention.

Fourteen attached owner amount claims authenticate against the recovered October 7 API bytes. Their generated counterparts retain rates but omit the claims; current failed API/detail requests do not negate the recovered evidence.

### f3: Historical timestamp precision remains unresolved

minor / open / confirmed; issue key: bosea-history-timestamp-shape.

Some original history values lack timezone or valid timestamp syntax. Their original bytes remain preserved and do not establish a reliable exact ordering.

## Recommended Actions And Acceptance Checks

### a1

Add the explicit water batch volume and claim-linked final-pH instruction to the appropriate maintained inputs; preserve existing correct rates and avoid invented sterilization or growth conditions. Use the current conservative merge workflow to reconcile and regenerate after authorized curation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the exact original owner evidence and source timestamp through authorized regeneration or a narrowly reviewed evidence-retention fix. Keep current retrieval status separate from historical authentication.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Append a source-backed historical clarification if available; do not silently normalize or rewrite old events.

- Preserve original events and distinguish unknown timezone from a known UTC time.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch045/441/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch045/441/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml:1:id: CultureMech:006418<br>./data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml:1:id: CultureMech:006418<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch045/source-preflight-bound/441/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 13 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch045/441/grounding-inventory.json; Complete path-qualified sidecar | context_only | Every asserted ingredient primary/secondary/legacy slot in target and exact owners, full OLS scientific properties, current exact index rows and any unverified provider identifiers. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi6636 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_6636; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi64220 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64220; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi32150 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi63675 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63675; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact asserted current secondary identifiers in pinned 9077-row label index | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:34683": [{"label": "Dibasic sodium phosphate", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Disodium hydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium hydrogenphosphate", "match_type": "ontology_label", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium hydrogenphosphate", "match_type": "ontology_label", "identifier": "CHEBI:34683", "preferred_term": "Sodium phosphate dibasic", "ontology_id": "CHEBI:34683", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Disodium Phosphate", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na HPO", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na HPO anydrous", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2H2PO4", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium phosphate dibasic", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Sodium phosphate dibasic", "ontology_id": "CHEBI:34683", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Sodium phosphate dibasic", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH PO", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4 (0.4 g/l)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4 (7% w/v)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4(Sigma P 0662)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MKP", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium dihydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium monophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium orthophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Orthophosphoric acid, monopotassium salt", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid, monopotassium salt", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid, potassium salt (1:1)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium acid phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dihydrogen orthophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dihydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium Phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium phosphate monobasic", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sorensen's potassium phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:6636": [{"label": "[MgCl2]", "match_type": "synonym", "identifier": "CHEBI:6636", "preferred_term": "MgCl2", "ontology_id": "CHEBI:6636", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride", "match_type": "synonym", "identifier": "CHEBI:6636", "preferred_term": "MgCl2", "ontology_id": "CHEBI:6636", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesiumchlorid", "match_type": "synonym", "identifier": "CHEBI:6636", "preferred_term": "MgCl2", "ontology_id": "CHEBI:6636", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2", "match_type": "preferred_term", "identifier": "CHEBI:6636", "preferred_term": "MgCl2", "ontology_id": "CHEBI:6636", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:64220": [{"label": "Monosodium glutamate", "match_type": "synonym", "identifier": "CHEBI:64220", "preferred_term": "Na glutamate", "ontology_id": "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na glutamate", "match_type": "preferred_term", "identifier": "CHEBI:64220", "preferred_term": "Na glutamate", "ontology_id": "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2-glutamate", "match_type": "synonym", "identifier": "CHEBI:64220", "preferred_term": "Na glutamate", "ontology_id": "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium 2-ammoniopentanedioate", "match_type": "synonym", "identifier": "CHEBI:64220", "preferred_term": "Na glutamate", "ontology_id": "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium 2-azaniumylpentanedioate", "match_type": "synonym", "identifier": "CHEBI:64220", "preferred_term": "Na glutamate", "ontology_id": "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium glutamate", "match_type": "synonym", "identifier": "CHEBI:64220", "preferred_term": "Na glutamate", "ontology_id": "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32150": [{"label": "disodium thiosulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium thiosulphate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3 . 5H2O", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3 x 5 H20", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3 x 5 H2O (10% solution)", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3 x 5 H2O(24 % w/v)", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3 x 5H2O", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3.5H2O", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3x5H2O", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3·5H2O", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3・5H2O", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaS2O3 x 5 H2O", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium sulfurothioate hydrate (2:1:5)", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium sulfurothioate--water (1/5)", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium sulfurothioate--water (1/5)", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Sodium Thiosulfate Pentahydrate", "ontology_id": "CHEBI:32150", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Sodium Thiosulfate Pentahydrate", "match_type": "preferred_term", "identifier": "CHEBI:32150", "preferred_term": "Sodium Thiosulfate Pentahydrate", "ontology_id": "CHEBI:32150", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Sodium thiosulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Thiosulfate Pentahydrate (agar media only,sterile)(Baker 3946)", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Thiosulfate Pentahydrate (agar media only,sterile)(Baker 3946)", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Sodium Thiosulfate Pentahydrate", "ontology_id": "CHEBI:32150", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "thiosulfuric acid, disodium salt, pentahydrate", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63675": [{"label": "disodium butanedioate", "match_type": "synonym", "identifier": "CHEBI:63675", "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Disodium succinate", "match_type": "synonym", "identifier": "CHEBI:63675", "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium succinate (anh.)", "match_type": "synonym", "identifier": "CHEBI:63675", "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium succinate", "match_type": "preferred_term", "identifier": "CHEBI:63675", "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium succinate (anhydrous)", "match_type": "ontology_label", "identifier": "CHEBI:63675", "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Succinic acid disodium salt", "match_type": "synonym", "identifier": "CHEBI:63675", "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "legacy": []} |
| history-metadata | data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml; data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:10.094047"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:10.094047"}]}, {"input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml", "events": 8, "timestamp_issues": []}] |
| history-full | /private/tmp/culturemech-review-work-batch045/441/history-inventory.json; Complete path-qualified sidecar | context_only | Full target and maintained-owner history events retained without rewriting malformed or timezone-absent values. |
| historical-inventory | /private/tmp/culturemech-review-work-batch045/441/historical-evidence-inventory.json; Complete path-qualified sidecar | context_only | Exact attached claim objects and decoded historical report joins; a decoded match is not original API-response authentication. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf; Complete DSMZ 763 recipe and final pH | supports | Seven nominal batch masses, 1000 ml water and pH 7.5–8.5 are explicit. The PDF does not state a measured final volume. |
| historical-api | https://mediadive.dsmz.de/rest/medium/763; $.data.medium and $.data.solutions[0].volume, recipe | supports | Exact original October 7 response recovered from a hash-pinned report. Declared volume 1000 ml and seven g_l values support provider-declared rates independently from the primary batch amounts. Original timestamp is retained. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact seven-column header and accession 763 row | supports | KOMODO accession 763 explicitly links DSMZ 763. Its Is Aerobic=false field is a catalog attribute, not a demonstrated strict anaerobic requirement. The current captured catalog has the cited raw hash but its October 19 access time differs from the historical October 7 claim timestamp. |
| mediadive763api-attempt | https://mediadive.dsmz.de/rest/medium/763; Preserved exact public retrieval result | context_only | The current MediaDive 763 request returned HTTP 503. Exact historical raw is recovered and authenticated, so this optional current refresh failure does not make the historical amount check unavailable. |
| komodoDetail763-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=763; Preserved exact public retrieval result | context_only | The current exact KOMODO detail page returned HTTP 403. Exact catalog identity and independent primary plus historical formulation evidence remain usable. |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current CLI grouping uses conservative scientific-field equality. Source-duplicate provenance is not permission to discard differing preparation/evidence. The generated record is compared with current owners; no historical execution or continued blind set-based merging is inferred. |
| writer-1 | src/culturemech/merge/merge_recipes.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current CLI grouping uses conservative scientific-field equality. Source-duplicate provenance is not permission to discard differing preparation/evidence. The generated record is compared with current owners; no historical execution or continued blind set-based merging is inferred. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current CLI grouping uses conservative scientific-field equality. Source-duplicate provenance is not permission to discard differing preparation/evidence. The generated record is compared with current owners; no historical execution or continued blind set-based merging is inferred. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch045/441/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The current MediaDive 763 request returned HTTP 503. Exact historical raw is recovered and authenticated, so this optional current refresh failure does not make the historical amount check unavailable.
- The current exact KOMODO detail page returned HTTP 403. Exact catalog identity and independent primary plus historical formulation evidence remain usable.
- The review verifies source and chemical-name correspondence, not an experiment or a specific sodium-succinate supplier grade. Current catalog Is Aerobic=false is not treated as a required anaerobic culture condition.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T020416Z-culturemech-006418-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bosea_thiooxidans_medium (CultureMech:006418)'
started_at: '2026-10-22T02:02:36Z'
finished_at: '2026-10-22T02:04:16Z'
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
summary: DSMZ 763 and the exact recovered historical provider response support the
  seven retained ingredient rates and source identity. Both maintained owners omit
  the 1000 ml water input; the generated record also loses the owner preparation text
  and attached amount evidence. Catalog oxygen metadata and nonspecific chemical forms
  require bounded interpretation.
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
  - path: data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml
    sha256: 36374e6164331eed1f47df7a7c3438bc3860ff82ece55ddceb059e771aab7dc3
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml
    sha256: e2a3d24abab47040b418992c32b71278d7914a97caec9a270ced1ce72985ac92
    role: context
  - path: data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml
    sha256: 2c52f5f6a6fa7d839c1977efcbb436cb43cc5e2e483b0d69c8ffa921da5537ab
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json
    sha256: 65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
    sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml.md
    sha256: b2d5f7858f47e24a2a47093e01b8439a0952eff248e8d3a85b091b3b0a043620
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/bosea_thiooxidans_medium.yaml.md
    sha256: 6c1aaaddf339f0194dc3921f0b88732a1c709c2b3717225f0d7d251f2c7f1de2
    role: context
  - path: reports/yaml_record_review/20260921T232304Z-BOSEA_THIOOXIDANS_MEDIUM.md
    sha256: 915932ae0ac95ac3a3e293fc855054f7321e572d479c43deacfbd844df19e919
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
  selection: Task review 441; batch 045 item 1 of 10, selected in Python lexicographic
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
  - CultureMech:006418
targets:
- target_id: CultureMech:006418
  path: data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml
  label: bosea_thiooxidans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006418
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch045/441/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch045/441/strict.tsv"
  target_ids:
  - CultureMech:006418
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006418
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006418
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
  - CultureMech:006418
- check_id: mediadive763api-source-access
  name: 'Exact source content access: mediadive763api'
  required: false
  status: unavailable
  summary: The current MediaDive 763 request returned HTTP 503. Exact historical raw
    is recovered and authenticated, so this optional current refresh failure does
    not make the historical amount check unavailable.
  target_ids:
  - CultureMech:006418
  evidence_ids:
  - mediadive763api-attempt
- check_id: komodoDetail763-source-access
  name: 'Exact source content access: komodoDetail763'
  required: false
  status: unavailable
  summary: The current exact KOMODO detail page returned HTTP 403. Exact catalog identity
    and independent primary plus historical formulation evidence remain usable.
  target_ids:
  - CultureMech:006418
  evidence_ids:
  - komodoDetail763-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T02:04:15Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:04:15Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:04:15Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:02:58.074053Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch045/441/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T02:02:59.781144Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch045/441/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:02.062331Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:03.279918Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T02:04:15Z'
  support: supports
  summary: './data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml:1:id: CultureMech:006418

    ./data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml:1:id:
    CultureMech:006418

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/source-preflight-bound/441/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T02:04:15Z'
  support: supports
  summary: 13 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 3bdea62b12fe8eacba4421562ef0f53e26e06307886e5a7b073873c99a545973
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/441/grounding-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:04:15Z'
  support: context_only
  summary: Every asserted ingredient primary/secondary/legacy slot in target and exact
    owners, full OLS scientific properties, current exact index rows and any unverified
    provider identifiers.
  snapshot_sha256: eeddd52e6c5d0982a8636707d34d5d94589d4911f590eb87af595261f36b4158
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
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
- evidence_id: chebi6636
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_6636
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T07:16:25.486015Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 62283ffd3dce5ed835af343e697602b91b9230da436a122769d7821dee39a272
- evidence_id: chebi64220
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64220
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T07:31:18.147552Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: f365c8a94dc3b7bb63e10235e8728f2333b34fb60943ea59c357ebd3456fb25b
- evidence_id: chebi32150
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T11:01:47.429763Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 910d65eb9be29c9371cb79a32bcbe81bdb57d8143d21fbf7c4a1a915b5a79999
- evidence_id: chebi63675
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63675
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T09:27:41.075057Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 4c54df9f2d63f54dea26d64e4ec9fedeb486c2c2abe44b70c5c621512f1fdd3c
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact asserted current secondary identifiers in pinned 9077-row label index
  accessed_at: '2026-10-22T02:04:15Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:34683":
    [{"label": "Dibasic sodium phosphate", "match_type": "synonym", "identifier":
    "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Disodium hydrogen phosphate", "match_type":
    "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id":
    "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium
    hydrogenphosphate", "match_type": "ontology_label", "identifier": "CHEBI:34683",
    "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "disodium hydrogenphosphate", "match_type":
    "ontology_label", "identifier": "CHEBI:34683", "preferred_term": "Sodium phosphate
    dibasic", "ontology_id": "CHEBI:34683", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Disodium Phosphate", "match_type": "synonym", "identifier":
    "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na HPO", "match_type": "synonym",
    "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na HPO anydrous",
    "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4",
    "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Na2H2PO4", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term":
    "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2HPO4", "match_type": "preferred_term", "identifier":
    "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Sodium phosphate dibasic", "match_type":
    "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Sodium phosphate
    dibasic", "ontology_id": "CHEBI:34683", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Sodium phosphate dibasic", "match_type": "synonym", "identifier":
    "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH PO", "match_type":
    "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4",
    "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "KH2PO4 (0.4 g/l)", "match_type": "synonym", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4 (7% w/v)", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4(Sigma P
    0662)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MKP", "match_type": "synonym", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Monopotassium dihydrogen phosphate", "match_type":
    "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium
    monophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Monopotassium orthophosphate", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium phosphate",
    "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4",
    "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Orthophosphoric acid, monopotassium salt", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid,
    monopotassium salt", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Phosphoric acid, potassium salt (1:1)", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium acid
    phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
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
    "unique"}], "CHEBI:6636": [{"label": "[MgCl2]", "match_type": "synonym", "identifier":
    "CHEBI:6636", "preferred_term": "MgCl2", "ontology_id": "CHEBI:6636", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride", "match_type":
    "synonym", "identifier": "CHEBI:6636", "preferred_term": "MgCl2", "ontology_id":
    "CHEBI:6636", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesiumchlorid",
    "match_type": "synonym", "identifier": "CHEBI:6636", "preferred_term": "MgCl2",
    "ontology_id": "CHEBI:6636", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgCl2", "match_type": "preferred_term", "identifier": "CHEBI:6636",
    "preferred_term": "MgCl2", "ontology_id": "CHEBI:6636", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:64220": [{"label": "Monosodium glutamate", "match_type":
    "synonym", "identifier": "CHEBI:64220", "preferred_term": "Na glutamate", "ontology_id":
    "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na
    glutamate", "match_type": "preferred_term", "identifier": "CHEBI:64220", "preferred_term":
    "Na glutamate", "ontology_id": "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2-glutamate", "match_type": "synonym", "identifier": "CHEBI:64220",
    "preferred_term": "Na glutamate", "ontology_id": "CHEBI:64220", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sodium 2-ammoniopentanedioate", "match_type":
    "synonym", "identifier": "CHEBI:64220", "preferred_term": "Na glutamate", "ontology_id":
    "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium
    2-azaniumylpentanedioate", "match_type": "synonym", "identifier": "CHEBI:64220",
    "preferred_term": "Na glutamate", "ontology_id": "CHEBI:64220", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Sodium glutamate", "match_type":
    "synonym", "identifier": "CHEBI:64220", "preferred_term": "Na glutamate", "ontology_id":
    "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32150":
    [{"label": "disodium thiosulfate pentahydrate", "match_type": "synonym", "identifier":
    "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium thiosulphate
    pentahydrate", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term":
    "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S2O3 . 5H2O", "match_type": "synonym", "identifier":
    "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3 x 5 H20",
    "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3
    x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S2O3 x 5 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3 x 5 H2O
    (10% solution)", "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term":
    "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S2O3 x 5 H2O(24 % w/v)", "match_type": "synonym", "identifier":
    "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3 x 5H2O",
    "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3
    x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S2O3.5H2O", "match_type": "synonym", "identifier": "CHEBI:32150",
    "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3x5H2O", "match_type": "synonym",
    "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id":
    "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S2O3·5H2O",
    "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3
    x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S2O3・5H2O", "match_type": "synonym", "identifier": "CHEBI:32150",
    "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "NaS2O3 x 5 H2O", "match_type": "synonym",
    "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id":
    "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium
    sulfurothioate hydrate (2:1:5)", "match_type": "synonym", "identifier": "CHEBI:32150",
    "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sodium sulfurothioate--water (1/5)",
    "match_type": "synonym", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3
    x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "sodium sulfurothioate--water (1/5)", "match_type": "synonym",
    "identifier": "CHEBI:32150", "preferred_term": "Sodium Thiosulfate Pentahydrate",
    "ontology_id": "CHEBI:32150", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "Sodium Thiosulfate Pentahydrate", "match_type": "preferred_term", "identifier":
    "CHEBI:32150", "preferred_term": "Sodium Thiosulfate Pentahydrate", "ontology_id":
    "CHEBI:32150", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "Sodium thiosulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:32150",
    "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Thiosulfate Pentahydrate (agar
    media only,sterile)(Baker 3946)", "match_type": "synonym", "identifier": "CHEBI:32150",
    "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Thiosulfate Pentahydrate (agar
    media only,sterile)(Baker 3946)", "match_type": "synonym", "identifier": "CHEBI:32150",
    "preferred_term": "Sodium Thiosulfate Pentahydrate", "ontology_id": "CHEBI:32150",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "thiosulfuric
    acid, disodium salt, pentahydrate", "match_type": "synonym", "identifier": "CHEBI:32150",
    "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63675": [{"label": "disodium butanedioate",
    "match_type": "synonym", "identifier": "CHEBI:63675", "preferred_term": "Sodium
    succinate", "ontology_id": "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Disodium succinate", "match_type": "synonym", "identifier":
    "CHEBI:63675", "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium succinate
    (anh.)", "match_type": "synonym", "identifier": "CHEBI:63675", "preferred_term":
    "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium succinate", "match_type": "preferred_term",
    "identifier": "CHEBI:63675", "preferred_term": "Sodium succinate", "ontology_id":
    "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium
    succinate (anhydrous)", "match_type": "ontology_label", "identifier": "CHEBI:63675",
    "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Succinic acid disodium salt", "match_type":
    "synonym", "identifier": "CHEBI:63675", "preferred_term": "Sodium succinate",
    "ontology_id": "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity": "unique"}]},
    "legacy": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml;
    data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T02:04:15Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:10.094047"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml",
    "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:10.094047"}]}, {"input": "data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml",
    "events": 8, "timestamp_issues": []}]'
- evidence_id: history-full
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/441/history-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:04:15Z'
  support: context_only
  summary: Full target and maintained-owner history events retained without rewriting
    malformed or timezone-absent values.
  snapshot_sha256: 5202403435a7deacb56417d34caa40f7868520c89b67fae075d9673ec45cdbb6
- evidence_id: historical-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/441/historical-evidence-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:04:15Z'
  support: context_only
  summary: Exact attached claim objects and decoded historical report joins; a decoded
    match is not original API-response authentication.
  snapshot_sha256: b48fdd8e8d61f7a171903186e35358ea236dbf7e1a29db8c16406fdf7d9b72d7
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf
  locator: Complete DSMZ 763 recipe and final pH
  accessed_at: '2026-10-22T01:49:17.202773Z'
  support: supports
  summary: Seven nominal batch masses, 1000 ml water and pH 7.5–8.5 are explicit.
    The PDF does not state a measured final volume.
  quote: 763. BOSEA THIOOXIDANS MEDIUM
  snapshot_sha256: 81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da
- evidence_id: historical-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/763
  locator: $.data.medium and $.data.solutions[0].volume, recipe
  accessed_at: '2026-10-07T12:18:32.710564Z'
  support: supports
  summary: Exact original October 7 response recovered from a hash-pinned report.
    Declared volume 1000 ml and seven g_l values support provider-declared rates independently
    from the primary batch amounts. Original timestamp is retained.
  snapshot_sha256: 8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact seven-column header and accession 763 row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: KOMODO accession 763 explicitly links DSMZ 763. Its Is Aerobic=false field
    is a catalog attribute, not a demonstrated strict anaerobic requirement. The current
    captured catalog has the cited raw hash but its October 19 access time differs
    from the historical October 7 claim timestamp.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: mediadive763api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/763
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T01:49:17.202870Z'
  support: context_only
  summary: The current MediaDive 763 request returned HTTP 503. Exact historical raw
    is recovered and authenticated, so this optional current refresh failure does
    not make the historical amount check unavailable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodoDetail763-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=763
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T01:51:10.278679Z'
  support: context_only
  summary: The current exact KOMODO detail page returned HTTP 403. Exact catalog identity
    and independent primary plus historical formulation evidence remain usable.
  snapshot_sha256: f8001ccf1f2ca95c1cb063ea30d75e7e232759fc76616a7f4cf89755c0cf1e05
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:04:15Z'
  support: context_only
  summary: Current CLI grouping uses conservative scientific-field equality. Source-duplicate
    provenance is not permission to discard differing preparation/evidence. The generated
    record is compared with current owners; no historical execution or continued blind
    set-based merging is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merge_recipes.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:04:15Z'
  support: context_only
  summary: Current CLI grouping uses conservative scientific-field equality. Source-duplicate
    provenance is not permission to discard differing preparation/evidence. The generated
    record is compared with current owners; no historical execution or continued blind
    set-based merging is inferred.
  snapshot_sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:04:15Z'
  support: context_only
  summary: Current CLI grouping uses conservative scientific-field equality. Source-duplicate
    provenance is not permission to discard differing preparation/evidence. The generated
    record is compared with current owners; no historical execution or continued blind
    set-based merging is inferred.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/441/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T02:04:15Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: a4e8027e60e76142bbb029242cbe32e55c400345ed286d72eb3afe53eb5bc155
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006418
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
  - CultureMech:006418
  evidence_ids:
  - grounding-inventory
  - mim
  - chebi34683
  - chebi63036
  - chebi6636
  - chebi64220
  - chebi32150
  - chebi63675
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 27 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006418
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: identity
  area: identity
  topic: Same source accession with exact maintained ownership
  outcome: supported
  summary: The two maintained owners identify KOMODO 763 and DSMZ 763, with an explicit
    source-duplicate relationship and matching seven ingredient signatures. The exact
    catalog link and primary title support this source correspondence. No strain-resolved
    growth experiment, species-level guarantee or strict anaerobic requirement follows
    from the collection title or catalog flag.
  target_ids:
  - CultureMech:006418
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - catalog
- assessment_id: amount-source
  area: quantity
  topic: Provider-declared rates and primary batch quantities
  outcome: supported
  summary: All seven nominal PDF masses correspond to the local numerals. Separately,
    the recovered API declares solution volume 1000 ml and exact g_l values, authenticating
    all fourteen attached owner amount excerpts. The target lacks those attached claims.
    This supports provider-declared rates without upgrading listed water to a measured
    final volume.
  target_ids:
  - CultureMech:006418
  evidence_ids:
  - primary
  - historical-api
  - historical-inventory
- assessment_id: preparation
  area: representation
  topic: Water and final pH completeness
  outcome: concern
  summary: The primary water input is absent from all three layers. Both owners and
    the target retain the structured pH range 7.5–8.5, while only the DSMZ owner has
    the preparation sentence. The source supplies no heating cycle, incubation temperature,
    gas composition or titrant dose; no conventional values are inferred.
  target_ids:
  - CultureMech:006418
  evidence_ids:
  - record
  - primary
  - owner-0
  - owner-1
- assessment_id: forms
  area: grounding
  topic: Supplied chemical forms and unresolved specificity
  outcome: supported
  summary: The explicit anhydrous phosphate, magnesium chloride and thiosulfate pentahydrate
    names are compatible with their terms. CHEBI:64220 is stereo-unspecified monosodium
    glutamate, not a D- or L-specific contradiction. Sodium succinate is generic in
    the primary; the anhydrous disodium term is a specificity limitation rather than
    a demonstrated wrong identity. No hydrate or stereochemical replacement is inferred.
  target_ids:
  - CultureMech:006418
  evidence_ids:
  - primary
  - grounding-inventory
  - chebi64220
  - chebi63675
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 20 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006418
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"Na2HPO4 generated\
    \ rate\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Na2HPO4'\"\
    ,\n        \"exact_source_quote\": \"Na2HPO4                                 \
    \    4.0    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Na2HPO4\\\",\\n                        \\\"compound_id\\\":\
    \ 233,\\n                        \\\"amount\\\": 4,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 4,\\n      \
    \                  \\\"mmol_l\\\": 28.1771,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"The exact value and G_PER_L basis match\
    \ the authenticated provider-declared g_l value. The generated descriptor lacks\
    \ the matching attached amount evidence retained by both owners. Add claim linkage\
    \ without claiming an independently measured final volume.\"\n  },\n  {\n    \"\
    decision_id\": \"q2\",\n    \"subject\": \"Na2HPO4 maintained rates\",\n    \"\
    decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Na2HPO4'\"\
    ,\n        \"exact_source_quote\": \"Na2HPO4                                 \
    \    4.0    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Na2HPO4\\\",\\n                        \\\"compound_id\\\":\
    \ 233,\\n                        \\\"amount\\\": 4,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 4,\\n      \
    \                  \\\"mmol_l\\\": 28.1771,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"Both maintained descriptors carry the\
    \ exact matching amount excerpt, cited hash and original source metadata. The\
    \ recovered response authenticates the provider-declared g_l basis; the PDF independently\
    \ corroborates the nominal batch mass. Preserve that distinction.\"\n  },\n  {\n\
    \    \"decision_id\": \"q3\",\n    \"subject\": \"KH2PO4 generated rate\",\n \
    \   \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'KH2PO4'\"\
    ,\n        \"exact_source_quote\": \"KH2PO4                                  \
    \    1.5    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 1.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n                \
    \        \\\"mmol_l\\\": 11.0225,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"The exact value and G_PER_L basis match\
    \ the authenticated provider-declared g_l value. The generated descriptor lacks\
    \ the matching attached amount evidence retained by both owners. Add claim linkage\
    \ without claiming an independently measured final volume.\"\n  },\n  {\n    \"\
    decision_id\": \"q4\",\n    \"subject\": \"KH2PO4 maintained rates\",\n    \"\
    decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'KH2PO4'\"\
    ,\n        \"exact_source_quote\": \"KH2PO4                                  \
    \    1.5    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 1.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n                \
    \        \\\"mmol_l\\\": 11.0225,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"Both maintained descriptors carry the\
    \ exact matching amount excerpt, cited hash and original source metadata. The\
    \ recovered response authenticates the provider-declared g_l basis; the PDF independently\
    \ corroborates the nominal batch mass. Preserve that distinction.\"\n  },\n  {\n\
    \    \"decision_id\": \"q5\",\n    \"subject\": \"MgCl2 generated rate\",\n  \
    \  \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'MgCl2'\"\
    ,\n        \"exact_source_quote\": \"MgCl2                                   \
    \    0.1    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgCl2\\\",\\n                        \\\"compound_id\\\": 453,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                \
    \        \\\"mmol_l\\\": 1.05031,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"The exact value and G_PER_L basis match\
    \ the authenticated provider-declared g_l value. The generated descriptor lacks\
    \ the matching attached amount evidence retained by both owners. Add claim linkage\
    \ without claiming an independently measured final volume.\"\n  },\n  {\n    \"\
    decision_id\": \"q6\",\n    \"subject\": \"MgCl2 maintained rates\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'MgCl2'\"\
    ,\n        \"exact_source_quote\": \"MgCl2                                   \
    \    0.1    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgCl2\\\",\\n                        \\\"compound_id\\\": 453,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                \
    \        \\\"mmol_l\\\": 1.05031,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"Both maintained descriptors carry the\
    \ exact matching amount excerpt, cited hash and original source metadata. The\
    \ recovered response authenticates the provider-declared g_l basis; the PDF independently\
    \ corroborates the nominal batch mass. Preserve that distinction.\"\n  },\n  {\n\
    \    \"decision_id\": \"q7\",\n    \"subject\": \"Na glutamate generated rate\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Na-glutamate'\"\
    ,\n        \"exact_source_quote\": \"Na-glutamate                            \
    \    0.5    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Na glutamate\\\",\\n                        \\\"compound_id\\\
    \": 839,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n\
    \                        \\\"mmol_l\\\": 2.95664,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\n      }\n\
    \    ],\n    \"rationale\": \"The exact value and G_PER_L basis match the authenticated\
    \ provider-declared g_l value. The generated descriptor lacks the matching attached\
    \ amount evidence retained by both owners. Add claim linkage without claiming\
    \ an independently measured final volume.\"\n  },\n  {\n    \"decision_id\": \"\
    q8\",\n    \"subject\": \"Na glutamate maintained rates\",\n    \"decision\":\
    \ \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Na-glutamate'\"\
    ,\n        \"exact_source_quote\": \"Na-glutamate                            \
    \    0.5    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Na glutamate\\\",\\n                        \\\"compound_id\\\
    \": 839,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n\
    \                        \\\"mmol_l\\\": 2.95664,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\n      }\n\
    \    ],\n    \"rationale\": \"Both maintained descriptors carry the exact matching\
    \ amount excerpt, cited hash and original source metadata. The recovered response\
    \ authenticates the provider-declared g_l basis; the PDF independently corroborates\
    \ the nominal batch mass. Preserve that distinction.\"\n  },\n  {\n    \"decision_id\"\
    : \"q9\",\n    \"subject\": \"Yeast extract generated rate\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz763\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Yeast\
    \ extract'\",\n        \"exact_source_quote\": \"Yeast extract               \
    \                0.1    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"optional\\\": 0\\n                    }\",\n     \
    \   \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"The exact value and G_PER_L basis match\
    \ the authenticated provider-declared g_l value. The generated descriptor lacks\
    \ the matching attached amount evidence retained by both owners. Add claim linkage\
    \ without claiming an independently measured final volume.\"\n  },\n  {\n    \"\
    decision_id\": \"q10\",\n    \"subject\": \"Yeast extract maintained rates\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Yeast\
    \ extract'\",\n        \"exact_source_quote\": \"Yeast extract               \
    \                0.1    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"optional\\\": 0\\n                    }\",\n     \
    \   \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"Both maintained descriptors carry the\
    \ exact matching amount excerpt, cited hash and original source metadata. The\
    \ recovered response authenticates the provider-declared g_l basis; the PDF independently\
    \ corroborates the nominal batch mass. Preserve that distinction.\"\n  },\n  {\n\
    \    \"decision_id\": \"q11\",\n    \"subject\": \"Na2S2O3 x 5 H2O generated rate\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Na2S2O3'\"\
    ,\n        \"exact_source_quote\": \"Na2S2O3 x 5 H2O                         \
    \    5.0    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Na2S2O3 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 65,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n     \
    \                   \\\"mmol_l\\\": 20.1462,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"The exact value and G_PER_L basis match\
    \ the authenticated provider-declared g_l value. The generated descriptor lacks\
    \ the matching attached amount evidence retained by both owners. Add claim linkage\
    \ without claiming an independently measured final volume.\"\n  },\n  {\n    \"\
    decision_id\": \"q12\",\n    \"subject\": \"Na2S2O3 x 5 H2O maintained rates\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Na2S2O3'\"\
    ,\n        \"exact_source_quote\": \"Na2S2O3 x 5 H2O                         \
    \    5.0    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Na2S2O3 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 65,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n     \
    \                   \\\"mmol_l\\\": 20.1462,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"Both maintained descriptors carry the\
    \ exact matching amount excerpt, cited hash and original source metadata. The\
    \ recovered response authenticates the provider-declared g_l basis; the PDF independently\
    \ corroborates the nominal batch mass. Preserve that distinction.\"\n  },\n  {\n\
    \    \"decision_id\": \"q13\",\n    \"subject\": \"Sodium succinate generated\
    \ rate\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Na-succinate'\"\
    ,\n        \"exact_source_quote\": \"Na-succinate                            \
    \    5.0    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Sodium succinate\\\",\\n                        \\\"compound_id\\\
    \": 730,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n    \
    \                    \\\"mmol_l\\\": 30.8547,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"The exact value and G_PER_L basis match\
    \ the authenticated provider-declared g_l value. The generated descriptor lacks\
    \ the matching attached amount evidence retained by both owners. Add claim linkage\
    \ without claiming an independently measured final volume.\"\n  },\n  {\n    \"\
    decision_id\": \"q14\",\n    \"subject\": \"Sodium succinate maintained rates\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Na-succinate'\"\
    ,\n        \"exact_source_quote\": \"Na-succinate                            \
    \    5.0    g\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Sodium succinate\\\",\\n                        \\\"compound_id\\\
    \": 730,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n    \
    \                    \\\"mmol_l\\\": 30.8547,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"Both maintained descriptors carry the\
    \ exact matching amount excerpt, cited hash and original source metadata. The\
    \ recovered response authenticates the provider-declared g_l basis; the PDF independently\
    \ corroborates the nominal batch mass. Preserve that distinction.\"\n  },\n  {\n\
    \    \"decision_id\": \"q15\",\n    \"subject\": \"Missing source water input\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients\",\n        \"stored\": [\n          {\n            \"preferred_term\"\
    : \"Na2HPO4\",\n            \"term\": {\n              \"id\": \"CHEBI:34683\"\
    ,\n              \"label\": \"disodium hydrogenphosphate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"4\",\n          \
    \    \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium\
    \ hydrogenphosphate\"\n            }\n          },\n          {\n            \"\
    preferred_term\": \"KH2PO4\",\n            \"term\": {\n              \"id\":\
    \ \"CHEBI:63036\",\n              \"label\": \"potassium dihydrogen phosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    1.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"MgCl2\",\n            \"term\": {\n              \"\
    id\": \"CHEBI:6636\",\n              \"label\": \"magnesium dichloride\"\n   \
    \         },\n            \"concentration\": {\n              \"value\": \"0.1\"\
    ,\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:6636\",\n              \"label\": \"magnesium\
    \ dichloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na glutamate\",\n            \"term\": {\n              \"id\": \"CHEBI:64220\"\
    ,\n              \"label\": \"monosodium glutamate\"\n            },\n       \
    \     \"concentration\": {\n              \"value\": \"0.5\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:64220\",\n              \"label\": \"monosodium\
    \ glutamate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"0.1\",\n              \"unit\": \"G_PER_L\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"Na2S2O3 x 5 H2O\",\n         \
    \   \"term\": {\n              \"id\": \"CHEBI:32150\",\n              \"label\"\
    : \"sodium thiosulfate pentahydrate\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:32150\",\n              \"label\": \"sodium thiosulfate pentahydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Sodium succinate\",\n            \"term\": {\n              \"id\": \"CHEBI:63675\"\
    ,\n              \"label\": \"sodium succinate (anhydrous)\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"5\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63675\",\n              \"label\": \"sodium\
    \ succinate (anhydrous)\"\n            }\n          }\n        ]\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Na2HPO4\",\n            \"term\": {\n \
    \             \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    4\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium\
    \ hydrogenphosphate\"\n            },\n            \"evidence\": [\n         \
    \     {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 1,\\n                      \
    \  \\\"compound\\\": \\\"Na2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 233,\\n                        \\\"amount\\\": 4,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 4,\\n    \
    \                    \\\"mmol_l\\\": 28.1771,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n                \"explanation\": \"Concentration\
    \ evidence for ingredients[0].concentration (Na2HPO4) in MediaDive medium 763;\
    \ locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=4; check:\
    \ 4 g * 1 g/g / (1000 ml / 1000 ml per L) = 4 g/L. This supports the provider-declared\
    \ main-recipe concentration, not an independently measured final volume, a stock\
    \ composition, or a downstream assay dilution. Water alone does not establish\
    \ final volume. Exact source ingredient labels/forms are matched; secondary ontology\
    \ mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume\
    \ (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\
    \ KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"KH2PO4\",\n            \"term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"1.5\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 2,\\n                      \
    \  \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 1.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n \
    \                       \\\"mmol_l\\\": 11.0225,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[1].concentration (KH2PO4) in MediaDive\
    \ medium 763; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports\
    \ g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00;\
    \ response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\
    \ KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"MgCl2\",\n            \"term\": {\n              \"id\": \"CHEBI:6636\",\n\
    \              \"label\": \"magnesium dichloride\"\n            },\n         \
    \   \"concentration\": {\n              \"value\": \"0.1\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:6636\",\n              \"label\": \"magnesium\
    \ dichloride\"\n            },\n            \"evidence\": [\n              {\n\
    \                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 3,\\n                      \
    \  \\\"compound\\\": \\\"MgCl2\\\",\\n                        \\\"compound_id\\\
    \": 453,\\n                        \\\"amount\\\": 0.1,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 1.05031,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[2].concentration (MgCl2) in MediaDive\
    \ medium 763; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports\
    \ g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00;\
    \ response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\
    \ KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Na glutamate\",\n            \"term\": {\n              \"id\": \"CHEBI:64220\"\
    ,\n              \"label\": \"monosodium glutamate\"\n            },\n       \
    \     \"concentration\": {\n              \"value\": \"0.5\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:64220\",\n              \"label\": \"monosodium\
    \ glutamate\"\n            },\n            \"evidence\": [\n              {\n\
    \                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 4,\\n                      \
    \  \\\"compound\\\": \\\"Na glutamate\\\",\\n                        \\\"compound_id\\\
    \": 839,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n\
    \                        \\\"mmol_l\\\": 2.95664,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[3].concentration (Na glutamate) in\
    \ MediaDive medium 763; locator=$.data.solutions[0].recipe[3]. Provider explicitly\
    \ reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L.\
    \ This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00;\
    \ response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\
    \ KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"0.1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    evidence\": [\n              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 5,\\n                      \
    \  \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"optional\\\": 0\\n                    }\",\n     \
    \           \"explanation\": \"Concentration evidence for ingredients[4].concentration\
    \ (Yeast extract) in MediaDive medium 763; locator=$.data.solutions[0].recipe[4].\
    \ Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000\
    \ ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\
    \ KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Na2S2O3 x 5 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:32150\"\
    ,\n              \"label\": \"sodium thiosulfate pentahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"5\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32150\",\n              \"label\": \"sodium\
    \ thiosulfate pentahydrate\"\n            },\n            \"evidence\": [\n  \
    \            {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 6,\\n                      \
    \  \\\"compound\\\": \\\"Na2S2O3 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 65,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n     \
    \                   \\\"mmol_l\\\": 20.1462,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n                \"explanation\": \"Concentration\
    \ evidence for ingredients[5].concentration (Na2S2O3 x 5 H2O) in MediaDive medium\
    \ 763; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=5;\
    \ check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L. This supports the provider-declared\
    \ main-recipe concentration, not an independently measured final volume, a stock\
    \ composition, or a downstream assay dilution. Water alone does not establish\
    \ final volume. Exact source ingredient labels/forms are matched; secondary ontology\
    \ mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume\
    \ (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\
    \ KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Sodium succinate\",\n            \"term\": {\n              \"id\": \"CHEBI:63675\"\
    ,\n              \"label\": \"sodium succinate (anhydrous)\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"5\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63675\",\n              \"label\": \"sodium\
    \ succinate (anhydrous)\"\n            },\n            \"evidence\": [\n     \
    \         {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 7,\\n                      \
    \  \\\"compound\\\": \\\"Sodium succinate\\\",\\n                        \\\"\
    compound_id\\\": 730,\\n                        \\\"amount\\\": 5,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 5,\\n                        \\\"mmol_l\\\": 30.8547,\\n                   \
    \     \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[6].concentration (Sodium succinate)\
    \ in MediaDive medium 763; locator=$.data.solutions[0].recipe[6]. Provider explicitly\
    \ reports g_l=5; check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L. This\
    \ supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00;\
    \ response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\
    \ KOMODO accession 763 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          }\n        ]\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Na2HPO4\",\n            \"term\": {\n \
    \             \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    4\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium\
    \ hydrogenphosphate\"\n            },\n            \"evidence\": [\n         \
    \     {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 1,\\n                      \
    \  \\\"compound\\\": \\\"Na2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 233,\\n                        \\\"amount\\\": 4,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 4,\\n    \
    \                    \\\"mmol_l\\\": 28.1771,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n                \"explanation\": \"Concentration\
    \ evidence for ingredients[0].concentration (Na2HPO4) in MediaDive medium 763;\
    \ locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=4; check:\
    \ 4 g * 1 g/g / (1000 ml / 1000 ml per L) = 4 g/L. This supports the provider-declared\
    \ main-recipe concentration, not an independently measured final volume, a stock\
    \ composition, or a downstream assay dilution. Water alone does not establish\
    \ final volume. Exact source ingredient labels/forms are matched; secondary ontology\
    \ mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume\
    \ (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"KH2PO4\",\n            \"term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"1.5\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 2,\\n                      \
    \  \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 1.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n \
    \                       \\\"mmol_l\\\": 11.0225,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[1].concentration (KH2PO4) in MediaDive\
    \ medium 763; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports\
    \ g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00;\
    \ response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"MgCl2\",\n            \"term\": {\n              \"id\": \"CHEBI:6636\",\n\
    \              \"label\": \"magnesium dichloride\"\n            },\n         \
    \   \"concentration\": {\n              \"value\": \"0.1\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:6636\",\n              \"label\": \"magnesium\
    \ dichloride\"\n            },\n            \"evidence\": [\n              {\n\
    \                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 3,\\n                      \
    \  \\\"compound\\\": \\\"MgCl2\\\",\\n                        \\\"compound_id\\\
    \": 453,\\n                        \\\"amount\\\": 0.1,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 1.05031,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[2].concentration (MgCl2) in MediaDive\
    \ medium 763; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports\
    \ g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00;\
    \ response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Na glutamate\",\n            \"term\": {\n              \"id\": \"CHEBI:64220\"\
    ,\n              \"label\": \"monosodium glutamate\"\n            },\n       \
    \     \"concentration\": {\n              \"value\": \"0.5\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:64220\",\n              \"label\": \"monosodium\
    \ glutamate\"\n            },\n            \"evidence\": [\n              {\n\
    \                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 4,\\n                      \
    \  \\\"compound\\\": \\\"Na glutamate\\\",\\n                        \\\"compound_id\\\
    \": 839,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n\
    \                        \\\"mmol_l\\\": 2.95664,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[3].concentration (Na glutamate) in\
    \ MediaDive medium 763; locator=$.data.solutions[0].recipe[3]. Provider explicitly\
    \ reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L.\
    \ This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00;\
    \ response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"0.1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    evidence\": [\n              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 5,\\n                      \
    \  \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"optional\\\": 0\\n                    }\",\n     \
    \           \"explanation\": \"Concentration evidence for ingredients[4].concentration\
    \ (Yeast extract) in MediaDive medium 763; locator=$.data.solutions[0].recipe[4].\
    \ Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000\
    \ ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Na2S2O3 x 5 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:32150\"\
    ,\n              \"label\": \"sodium thiosulfate pentahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"5\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32150\",\n              \"label\": \"sodium\
    \ thiosulfate pentahydrate\"\n            },\n            \"evidence\": [\n  \
    \            {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 6,\\n                      \
    \  \\\"compound\\\": \\\"Na2S2O3 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 65,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n     \
    \                   \\\"mmol_l\\\": 20.1462,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n                \"explanation\": \"Concentration\
    \ evidence for ingredients[5].concentration (Na2S2O3 x 5 H2O) in MediaDive medium\
    \ 763; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=5;\
    \ check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L. This supports the provider-declared\
    \ main-recipe concentration, not an independently measured final volume, a stock\
    \ composition, or a downstream assay dilution. Water alone does not establish\
    \ final volume. Exact source ingredient labels/forms are matched; secondary ontology\
    \ mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume\
    \ (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00; response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Sodium succinate\",\n            \"term\": {\n              \"id\": \"CHEBI:63675\"\
    ,\n              \"label\": \"sodium succinate (anhydrous)\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"5\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63675\",\n              \"label\": \"sodium\
    \ succinate (anhydrous)\"\n            },\n            \"evidence\": [\n     \
    \         {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/763\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 7,\\n                      \
    \  \\\"compound\\\": \\\"Sodium succinate\\\",\\n                        \\\"\
    compound_id\\\": 730,\\n                        \\\"amount\\\": 5,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 5,\\n                        \\\"mmol_l\\\": 30.8547,\\n                   \
    \     \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[6].concentration (Sodium succinate)\
    \ in MediaDive medium 763; locator=$.data.solutions[0].recipe[6]. Provider explicitly\
    \ reports g_l=5; check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L. This\
    \ supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:18:32.710564+00:00;\
    \ response SHA256=8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207.\"\
    \n              }\n            ]\n          }\n        ]\n      }\n    ],\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz763\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Distilled\
    \ water'\",\n        \"exact_source_quote\": \"Distilled water               \
    \           1000.0   ml\",\n        \"snapshot_sha256\": \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\"\
    ,\n        \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      },\n      {\n        \"source_key\": \"historical763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"8466ea35ac5a349745f39f47614104814adc6b6ec1340111702d0af0475a6207\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the explicit 1000 ml water batch\
    \ input, not 1000 g/L or a measured final-volume statement.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q16\",\n    \"subject\": \"Final pH range\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ph_range\",\n        \"stored\": {\n          \"min\": 7.5,\n          \"\
    max\": 8.5\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.5,\n          \"max\": 8.5\n        }\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml\",\n \
    \       \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"min\"\
    : 7.5,\n          \"max\": 8.5\n        }\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz763\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\",\n        \"\
    source_locator\": \"Exact extracted source line containing 'Final pH'\",\n   \
    \     \"exact_source_quote\": \"Final pH 7.5-8.5.\",\n        \"snapshot_sha256\"\
    : \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\",\n    \
    \    \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      }\n    ],\n    \"rationale\": \"The existing 7.5–8.5 range matches the\
    \ primary. Add direct claim-level support; the catalog identity snippet is not\
    \ a preparation claim.\"\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"subject\"\
    : \"Generated and KOMODO preparation sentence\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Final\
    \ pH'\",\n        \"exact_source_quote\": \"Final pH 7.5-8.5.\",\n        \"snapshot_sha256\"\
    : \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\",\n    \
    \    \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the source final-pH instruction\
    \ at the maintained and generated layers. The DSMZ owner already retains this\
    \ sentence.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n    \"subject\": \"Existing\
    \ DSMZ preparation sentence\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Final pH 7.5-8.5.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Final\
    \ pH'\",\n        \"exact_source_quote\": \"Final pH 7.5-8.5.\",\n        \"snapshot_sha256\"\
    : \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\",\n    \
    \    \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      }\n    ],\n    \"rationale\": \"Retain this existing matching preparation\
    \ text and link the exact primary evidence.\"\n  },\n  {\n    \"decision_id\"\
    : \"q19\",\n    \"subject\": \"Titrant dose\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Final\
    \ pH'\",\n        \"exact_source_quote\": \"Final pH 7.5-8.5.\",\n        \"snapshot_sha256\"\
    : \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\",\n    \
    \    \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      }\n    ],\n    \"rationale\": \"The endpoint range is explicit but no\
    \ fixed titrant or dose is specified. No amount is invented.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q20\",\n    \"subject\": \"Incubation or sterilization parameters\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml\",\n  \
    \      \"field_path\": \"temperature_value\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz763\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Final\
    \ pH'\",\n        \"exact_source_quote\": \"Final pH 7.5-8.5.\",\n        \"snapshot_sha256\"\
    : \"81dca6f8c15499f4bc061b64e640fdfca2fffad7dc8907d9bbc725685e8868da\",\n    \
    \    \"parsed_text_sha256\": \"7152af2269b3075cf6abdeb949dbe569abfbac86b5dd30080aee40963d741165\"\
    \n      }\n    ],\n    \"rationale\": \"The complete primary gives no incubation\
    \ temperature, heating temperature or duration. Absence is not an explicit no-fixed-value\
    \ instruction.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: bosea-water-and-preparation
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Restore the source water input and retain preparation scope
  description: All layers omit 1000 ml water; the generated record and KOMODO owner
    lack the preparation sentence retained by the DSMZ owner. The pH range itself
    is correct.
  target_ids:
  - CultureMech:006418
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
    path: data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml
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
  issue_key: bosea-generated-evidence-retention
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Retain authenticated owner amount evidence in generated output
  description: Fourteen attached owner amount claims authenticate against the recovered
    October 7 API bytes. Their generated counterparts retain rates but omit the claims;
    current failed API/detail requests do not negate the recovered evidence.
  target_ids:
  - CultureMech:006418
  field_paths:
  - ingredients
  evidence_ids:
  - historical-api
  - historical-inventory
  - record
  - owner-0
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml
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
  issue_key: bosea-history-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical timestamp precision remains unresolved
  description: Some original history values lack timezone or valid timestamp syntax.
    Their original bytes remain preserved and do not establish a reliable exact ordering.
  target_ids:
  - CultureMech:006418
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  - history-full
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml
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
  description: Add the explicit water batch volume and claim-linked final-pH instruction
    to the appropriate maintained inputs; preserve existing correct rates and avoid
    invented sterilization or growth conditions. Use the current conservative merge
    workflow to reconcile and regenerate after authorized curation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006418
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml
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
  description: Preserve the exact original owner evidence and source timestamp through
    authorized regeneration or a narrowly reviewed evidence-retention fix. Keep current
    retrieval status separate from historical authentication.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006418
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml
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
  description: Append a source-backed historical clarification if available; do not
    silently normalize or rewrite old events.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006418
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Preserve original events and distinguish unknown timezone from a known UTC time.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- The current MediaDive 763 request returned HTTP 503. Exact historical raw is recovered
  and authenticated, so this optional current refresh failure does not make the historical
  amount check unavailable.
- The current exact KOMODO detail page returned HTTP 403. Exact catalog identity and
  independent primary plus historical formulation evidence remain usable.
- The review verifies source and chemical-name correspondence, not an experiment or
  a specific sodium-succinate supplier grade. Current catalog Is Aerobic=false is
  not treated as a required anaerobic culture condition.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-045
- generated-medium
```
