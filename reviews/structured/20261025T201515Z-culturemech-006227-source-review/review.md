# Source and formulation review: centenum_medium (CultureMech:006227)

- Review: 20261025T201515Z-culturemech-006227-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-25T20:08:40Z
- Finished UTC: 2026-10-25T20:15:15Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The selected CENTENUM target is stale relative to two repaired DSM650 base owners: they already preserve a volume-based water input, source-explicit 20 mM pyruvate and complete preparation. Fourteen attached claims authenticate against the exact recovered historical API650 response. The separate DSM8319 owner has no corresponding source verification, so old copied composition and identical ingredient signatures cannot establish variant equivalence. Preserve the valid base identity and existing repairs while resolving the generated target and variant boundary.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 528; batch 053 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fifty-two task batches contain 520 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 231e0ba71b41d45362168d539efebe7991823464 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 523 of 6325 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 231e0ba71b41d45362168d539efebe7991823464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006227 | data/merge_yaml/merged/CENTENUM_MEDIUM.yaml | generated | centenum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006227 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006227 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch053/528/strict.tsv |
| validate-terms | passed | True | CultureMech:006227 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006227 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006227 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: api650 | unavailable | False | CultureMech:006227 | The current exact api650 request returned HTTP 503. Its unusable maintenance/challenge body remains separate from the usable DSM650 primary and recovered historical API650 response. |
| Exact source content access: komodo650 | unavailable | False | CultureMech:006227 | The current exact komodo650 request returned HTTP 403. Its unusable maintenance/challenge body remains separate from the usable DSM650 primary and recovered historical API650 response. |
| Exact source content access: komodo650_8319 | unavailable | True | CultureMech:006227 | The exact KOMODO650/DSM8319 variant request returned HTTP 403. No usable variant formulation was obtained; base DSM650 evidence cannot establish the variant changes or equivalence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006227.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:006227.

5 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels across the selected target and its exact maintained owners. Target linkage: 5/6 primary and 5/6 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Complete recursive inspection of these selected documents found zero legacy mediaingredientmech_term slots and zero numeric legacy MediaIngredientMech identifiers. Generic placeholder text in history is not an asserted identifier. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 6: primary 83.33%; secondary 83.33%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006227.

32 timestamp instances inspected; 6 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006227.

23 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "K2HPO4 in generated base target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENTENUM_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 4: K2HPO4",
        "exact_source_quote": "K2HPO4                                                         1.0       g",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "The historical API explicitly supplies this nominal g_l value and the primary supplies the matching batch mass. The target lacks the current owner explanation/evidence. Add qualified support for the base recipe; do not call it an independently measured final-medium concentration or source support for DSM8319."
  },
  {
    "decision_id": "q2",
    "subject": "K2HPO4 in the two repaired base owners",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/centenum_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 4: K2HPO4",
        "exact_source_quote": "K2HPO4                                                         1.0       g",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "Each current base owner independently carries a literal, cited-raw-hash-matched claim and explicitly qualifies the retained G_PER_L as a provider nominal main rate. Verification is limited to that representation and its scope; listed water is not an independently declared final volume."
  },
  {
    "decision_id": "q3",
    "subject": "K2HPO4 in DSM8319 variant",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 4: K2HPO4",
        "exact_source_quote": "K2HPO4                                                         1.0       g",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "These snippets describe base DSM650 only and are included as comparison context. The exact variant provider is unavailable and no attached variant claim authenticates this value. No source-derived replacement is proposed for the variant.",
    "proposed_source_representation": {
      "stage": "DSM8319 variant",
      "replacement": null,
      "reason": "exact variant formulation unresolved"
    }
  },
  {
    "decision_id": "q4",
    "subject": "MgSO4 in generated base target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENTENUM_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 5: MgSO4",
        "exact_source_quote": "MgSO4                                                          0.5       g",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4\",\n                        \"compound_id\": 325,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 4.15386,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "The historical API explicitly supplies this nominal g_l value and the primary supplies the matching batch mass. The target lacks the current owner explanation/evidence. Add qualified support for the base recipe; do not call it an independently measured final-medium concentration or source support for DSM8319."
  },
  {
    "decision_id": "q5",
    "subject": "MgSO4 in the two repaired base owners",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/centenum_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 5: MgSO4",
        "exact_source_quote": "MgSO4                                                          0.5       g",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4\",\n                        \"compound_id\": 325,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 4.15386,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "Each current base owner independently carries a literal, cited-raw-hash-matched claim and explicitly qualifies the retained G_PER_L as a provider nominal main rate. Verification is limited to that representation and its scope; listed water is not an independently declared final volume."
  },
  {
    "decision_id": "q6",
    "subject": "MgSO4 in DSM8319 variant",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 5: MgSO4",
        "exact_source_quote": "MgSO4                                                          0.5       g",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4\",\n                        \"compound_id\": 325,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 4.15386,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "These snippets describe base DSM650 only and are included as comparison context. The exact variant provider is unavailable and no attached variant claim authenticates this value. No source-derived replacement is proposed for the variant.",
    "proposed_source_representation": {
      "stage": "DSM8319 variant",
      "replacement": null,
      "reason": "exact variant formulation unresolved"
    }
  },
  {
    "decision_id": "q7",
    "subject": "Yeast extract in generated base target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENTENUM_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 6: Yeast extract",
        "exact_source_quote": "Yeast extract                                                 10.0       g",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "The historical API explicitly supplies this nominal g_l value and the primary supplies the matching batch mass. The target lacks the current owner explanation/evidence. Add qualified support for the base recipe; do not call it an independently measured final-medium concentration or source support for DSM8319."
  },
  {
    "decision_id": "q8",
    "subject": "Yeast extract in the two repaired base owners",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/centenum_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 6: Yeast extract",
        "exact_source_quote": "Yeast extract                                                 10.0       g",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "Each current base owner independently carries a literal, cited-raw-hash-matched claim and explicitly qualifies the retained G_PER_L as a provider nominal main rate. Verification is limited to that representation and its scope; listed water is not an independently declared final volume."
  },
  {
    "decision_id": "q9",
    "subject": "Yeast extract in DSM8319 variant",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 6: Yeast extract",
        "exact_source_quote": "Yeast extract                                                 10.0       g",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "These snippets describe base DSM650 only and are included as comparison context. The exact variant provider is unavailable and no attached variant claim authenticates this value. No source-derived replacement is proposed for the variant.",
    "proposed_source_representation": {
      "stage": "DSM8319 variant",
      "replacement": null,
      "reason": "exact variant formulation unresolved"
    }
  },
  {
    "decision_id": "q10",
    "subject": "Vitamin B12 in generated base target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENTENUM_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2e-05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 7: Vitamin B12",
        "exact_source_quote": "Vitamin B12                                                   20.0      μg",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 20,\n                        \"unit\": \"\\u00b5g\",\n                        \"g_l\": 2.0e-5,\n                        \"mmol_l\": 1.47558e-5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "The historical API explicitly supplies this nominal g_l value and the primary supplies the matching batch mass. The target lacks the current owner explanation/evidence. Add qualified support for the base recipe; do not call it an independently measured final-medium concentration or source support for DSM8319."
  },
  {
    "decision_id": "q11",
    "subject": "Vitamin B12 in the two repaired base owners",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2e-05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/centenum_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2e-05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 7: Vitamin B12",
        "exact_source_quote": "Vitamin B12                                                   20.0      μg",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 20,\n                        \"unit\": \"\\u00b5g\",\n                        \"g_l\": 2.0e-5,\n                        \"mmol_l\": 1.47558e-5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "Each current base owner independently carries a literal, cited-raw-hash-matched claim and explicitly qualifies the retained G_PER_L as a provider nominal main rate. Verification is limited to that representation and its scope; listed water is not an independently declared final volume."
  },
  {
    "decision_id": "q12",
    "subject": "Vitamin B12 in DSM8319 variant",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2e-05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 7: Vitamin B12",
        "exact_source_quote": "Vitamin B12                                                   20.0      μg",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 20,\n                        \"unit\": \"\\u00b5g\",\n                        \"g_l\": 2.0e-5,\n                        \"mmol_l\": 1.47558e-5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "These snippets describe base DSM650 only and are included as comparison context. The exact variant provider is unavailable and no attached variant claim authenticates this value. No source-derived replacement is proposed for the variant.",
    "proposed_source_representation": {
      "stage": "DSM8319 variant",
      "replacement": null,
      "reason": "exact variant formulation unresolved"
    }
  },
  {
    "decision_id": "q13",
    "subject": "Target tap-water dimension",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENTENUM_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1000",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\": 322,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      }
    ],
    "rationale": "Base DSM650 prints 1000 ml tap water, equivalent to 1 L batch input. The target stores a mass-per-volume unit. This correction concerns the water input dimension and does not establish final medium volume.",
    "proposed_source_representation": {
      "stage": "base main batch",
      "amount": 1,
      "unit": "L",
      "basis": "water input"
    }
  },
  {
    "decision_id": "q14",
    "subject": "Repaired base-owner water input",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/centenum_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\": 322,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      }
    ],
    "rationale": "Both base owners already retain 1 L tap-water input with independently authenticated claims. Preserve this repair and its explicit limit: it is not water mass or measured final volume."
  },
  {
    "decision_id": "q15",
    "subject": "Variant water dimension and unresolved recipe",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1000",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 8: Tap water",
        "exact_source_quote": "Tap water                                                   1000.0      ml",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\": 322,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      }
    ],
    "rationale": "The existing G_PER_L represents water as a mass concentration, but these available source quantities belong to base650. The exact variant water amount remains unverified; do not copy the base amount into DSM8319 as an authenticated correction.",
    "proposed_source_representation": {
      "stage": "DSM8319 variant",
      "replacement": null,
      "reason": "source amount unresolved; current dimensional representation also requires review"
    }
  },
  {
    "decision_id": "q16",
    "subject": "Target post-autoclave pyruvate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENTENUM_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1.741",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text lines 12–13",
        "exact_source_quote": "Boil under nitrogen gas and autoclave at 121C for 15 min. Add 20 mM pyruvate after\nautoclaving.",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyruvate\",\n                        \"compound_id\": 1386,\n                        \"amount\": 20,\n                        \"unit\": \"mM\",\n                        \"g_l\": 1.741,\n                        \"mmol_l\": 20,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      }
    ],
    "rationale": "The historical provider explicitly contains g_l 1.741, so that number is not unsupported by every source. The current primary and API preparation explicitly prescribe 20 mM after autoclaving. Restore that source basis and stage in the base target rather than treating the imported mass field as a complete operational representation.",
    "proposed_source_representation": {
      "stage": "after autoclaving",
      "amount": 20,
      "unit": "MILLIMOLAR",
      "mass_conversion_required": false
    }
  },
  {
    "decision_id": "q17",
    "subject": "Repaired base-owner pyruvate",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "20",
          "unit": "MILLIMOLAR"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/centenum_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "20",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text lines 12–13",
        "exact_source_quote": "Boil under nitrogen gas and autoclave at 121C for 15 min. Add 20 mM pyruvate after\nautoclaving.",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyruvate\",\n                        \"compound_id\": 1386,\n                        \"amount\": 20,\n                        \"unit\": \"mM\",\n                        \"g_l\": 1.741,\n                        \"mmol_l\": 20,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      }
    ],
    "rationale": "Both base owners already retain source-explicit 20 mM with post-autoclave preparation and independently matched claims. No salt, molecular-weight or stock-dilution assumption is needed."
  },
  {
    "decision_id": "q18",
    "subject": "Variant pyruvate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1.741",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text lines 12–13",
        "exact_source_quote": "Boil under nitrogen gas and autoclave at 121C for 15 min. Add 20 mM pyruvate after\nautoclaving.",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "api650Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/650",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyruvate\",\n                        \"compound_id\": 1386,\n                        \"amount\": 20,\n                        \"unit\": \"mM\",\n                        \"g_l\": 1.741,\n                        \"mmol_l\": 20,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8",
        "accessed_at": "2026-10-07T12:17:00.953143+00:00"
      }
    ],
    "rationale": "API650 g_l 1.741 and the base post-autoclave 20 mM instruction are comparison context only. Neither authenticates DSM8319 formulation or timing. Resolve its own source before any replacement.",
    "proposed_source_representation": {
      "stage": "DSM8319 variant",
      "replacement": null,
      "reason": "exact variant source unavailable"
    }
  },
  {
    "decision_id": "q19",
    "subject": "Base target and owners pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENTENUM_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.0
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0
      },
      {
        "input": "data/normalized_yaml/bacterial/centenum_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 10: Adjust pH",
        "exact_source_quote": "Adjust pH to 7.0.",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "The primary explicitly states pH 7.0; all three base representations agree. This supports the base recipe pH, not an unstated optimum, buffer capacity or strain-specific growth result."
  },
  {
    "decision_id": "q20",
    "subject": "Variant pH",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml",
        "field_path": "ph_value",
        "stored": 7.0
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 10: Adjust pH",
        "exact_source_quote": "Adjust pH to 7.0.",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "The quoted pH is base650 context only. Exact DSM8319 pH remains unverified and no replacement is proposed."
  },
  {
    "decision_id": "q21",
    "subject": "Current base-owner preparation step 1",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
        "field_path": "preparation_steps[0].step_number",
        "stored": 1
      },
      {
        "input": "data/normalized_yaml/bacterial/centenum_medium.yaml",
        "field_path": "preparation_steps[0].step_number",
        "stored": 1
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.0."
      },
      {
        "input": "data/normalized_yaml/bacterial/centenum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.0."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 10: Adjust pH",
        "exact_source_quote": "Adjust pH to 7.0.",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "The retained instruction is source-supported and already present in both repaired owners. The step number is local ordering metadata. Preserve the exact source scope; a valid recipe instruction is not experimental growth evidence."
  },
  {
    "decision_id": "q22",
    "subject": "Current base-owner preparation step 2",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
        "field_path": "preparation_steps[1].step_number",
        "stored": 2
      },
      {
        "input": "data/normalized_yaml/bacterial/centenum_medium.yaml",
        "field_path": "preparation_steps[1].step_number",
        "stored": 2
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Boil under nitrogen gas and autoclave at 121°C for 15 min. Add 20 mM pyruvate after autoclaving."
      },
      {
        "input": "data/normalized_yaml/bacterial/centenum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Boil under nitrogen gas and autoclave at 121°C for 15 min. Add 20 mM pyruvate after autoclaving."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text lines 12–13",
        "exact_source_quote": "Boil under nitrogen gas and autoclave at 121C for 15 min. Add 20 mM pyruvate after\nautoclaving.",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "The retained instruction is source-supported and already present in both repaired owners. The step number is local ordering metadata. Preserve the exact source scope; a valid recipe instruction is not experimental growth evidence."
  },
  {
    "decision_id": "q23",
    "subject": "Missing base-target preparation",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text line 10: Adjust pH",
        "exact_source_quote": "Adjust pH to 7.0.",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      },
      {
        "source_key": "dsmz650",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf",
        "source_locator": "PDF page 1; extracted text lines 12–13",
        "exact_source_quote": "Boil under nitrogen gas and autoclave at 121C for 15 min. Add 20 mM pyruvate after\nautoclaving.",
        "snapshot_sha256": "aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b",
        "parsed_text_sha256": "36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d",
        "accessed_at": "2026-10-22T09:27:21.504255+00:00"
      }
    ],
    "rationale": "The generated target omits the now-retained owner preparation. Restore pH adjustment, nitrogen boiling, 121 degrees C for 15 minutes and post-autoclave 20 mM pyruvate only for the verified base650 formulation; do not transfer these as variant evidence.",
    "proposed_source_representation": {
      "stage": "base650 preparation",
      "pH": 7,
      "gas": "nitrogen",
      "autoclave_temperature_C": 121,
      "autoclave_duration_min": 15,
      "post_autoclave_pyruvate_mM": 20
    }
  }
]

### Valid base identity and unresolved DSM8319 merge boundary

identity: concern. Targets: CultureMech:006227.

DSM650 is a valid source for the selected base target and two maintained base owners. The third owner is explicitly a DSM8319 modifier, whose exact source is unavailable. Old copied DSM composition and matching signatures cannot independently establish that the modifier is identical to the base.

### Existing owner repairs versus generated staleness

consistency: concern. Targets: CultureMech:006227.

The two base owners already contain water 1 L, pyruvate 20 mM, source preparation and fourteen authenticated claims. The generated target predates these repairs and retains the old water unit, mass-only pyruvate and absent preparation. Current merge code protects exact scientific fields; this is stale generated content, not proof the current guard still performs ingredient-only consolidation.

### Exact raw recovery and time/claim boundaries

evidence: supported. Targets: CultureMech:006227.

The historical API650 raw matches the cited digest and fourteen owner snippets. The original access time is retained and finish is unknown. Current failed retrievals remain separate. Reports are derivative accounts, and base evidence is not promoted into a verified DSM8319 recipe.

### Record type, category and growth claims

scope: unknown. Targets: CultureMech:006227.

The selected documents are bacterial liquid MediaRecipe records. The bounded collection formulation establishes a recipe identity, not strain-specific experimental growth. No organism growth assertion, incubation optimum or literature-wide evidence claim is added.

## Findings

### f1: Resolve DSM8319 membership independently of copied base composition

major / open / confirmed; issue key: CENTENUM_VARIANT_BOUNDARY.

The generated target includes medium650_modified_for_dsm8319 among its merge sources. That owner has a distinct variant identity and lacks exact source authentication, while the two base owners now have materially different quantities and preparation. Base API650 claims cannot resolve the modifier. The confirmed defect is the unsubstantiated equivalence claim, not proof that every variant ingredient is numerically wrong.

### f2: Regenerate the base target from the repaired owners after identity resolution

major / open / confirmed; issue key: CENTENUM_GENERATED_STALENESS.

The base owners already correct tap water from 1000 G_PER_L to 1 L input, retain 20 mM pyruvate added after autoclaving, and preserve the pH/nitrogen/autoclave preparation. The target still has the old mass-unit water and mass-only pyruvate and no preparation. Main g_l values are explicit historical provider nominal fields, not a fabricated mass discrepancy.

### f3: Qualify malformed import times without replacing their history

minor / open / confirmed; issue key: CENTENUM_HISTORY_TIMESTAMP.

The target and KOMODO-derived owners retain literal .fZ timestamps that are not valid UTC instants. Exact historical API access time is separately recoverable and must not be substituted for an unknown importer execution time.

## Recommended Actions And Acceptance Checks

### a1

Resolve the exact DSM8319 variant identity and source independently. Retain a distinct owner/variant boundary until equivalence is supported; do not discard the valid DSM650 identity or copy base corrections into the modifier without evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Credit and preserve both owner repairs. Resolve merge membership, then regenerate the base target with the corrected source basis, preparation and claim-level evidence. Keep nominal provider rates qualified and final-volume assumptions unresolved.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve existing history and append a bounded clarification of malformed import timestamps; verify the current timestamp writer separately without inventing original execution times.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/CENTENUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/centenum_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/CENTENUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/CENTENUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch053/528/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch053/528/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/CENTENUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/CENTENUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/CENTENUM_MEDIUM.yaml:1:id: CultureMech:006227<br>./data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml:1:id: CultureMech:006227<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch053/source-preflight-bound/528/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 13 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| source-reading | /private/tmp/culturemech-review-work-batch053/records527-528-source-reading-20261025T201126Z/source-reading.json; Complete selected documents, primary pages, fourteen historical reports and named current writer functions | context_only | The pinned reading receipt distinguishes complete source reads from derivative historical interpretation and from current writer behavior. |
| context | /private/tmp/culturemech-review-work-batch053/source-preflight-bound/528/evidence-context-original.json; Full per-record source context and scoped inventories | context_only | Frozen local inventories, source captures, source-access outcomes and exact owner/parent scope; context is an index, not additional independent scientific evidence. |
| dsm650-main | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf; Complete page 1 main table, lines 4–8 | supports | Current DSM650 lists the original main batch masses and 1000 ml tap water. The water input alone is not a final-medium volume declaration. |
| dsm650-preparation | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf; Page 1 pH and preparation, lines 10–13 | supports | The primary explicitly specifies pH 7, nitrogen boiling, 121 degrees C for 15 minutes and post-autoclave 20 mM pyruvate. |
| api650-historical | https://mediadive.dsmz.de/rest/medium/650; $.data.medium; $.data.solutions[0].recipe and steps; exact recovered parent $[30] | supports | The original UTF-8 response and original metadata were recovered by exact hash. It states provider nominal g_l values, original batch inputs and the same preparation. Access time remains 2026-10-07T12:17:00.953143+00:00; finish time is unknown. This is historical API650 evidence, not a new successful API request or automatic support for DSM8319. |
| api650-attempt | https://mediadive.dsmz.de/rest/medium/650; Preserved exact public retrieval result | context_only | The current exact api650 request returned HTTP 503. Its unusable maintenance/challenge body remains separate from the usable DSM650 primary and recovered historical API650 response. |
| komodo650-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=650; Preserved exact public retrieval result | context_only | The current exact komodo650 request returned HTTP 403. Its unusable maintenance/challenge body remains separate from the usable DSM650 primary and recovered historical API650 response. |
| komodo650_8319-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=650_8319; Preserved exact public retrieval result | context_only | The exact KOMODO650/DSM8319 variant request returned HTTP 403. No usable variant formulation was obtained; base DSM650 evidence cannot establish the variant changes or equivalence. |
| owner-claim-authentication | /private/tmp/culturemech-review-work-batch053/source-preflight-bound/528/evidence-context-original.json; Fourteen independently checked base-owner ingredient/preparation claims; separate catalog identity claim | supports | {"authenticated_claims": [{"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path": "$.ingredients[0].evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path": "$.ingredients[1].evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path": "$.ingredients[2].evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path": "$.ingredients[3].evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path": "$.ingredients[4].evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path": "$.ingredients[5].evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path": "$.evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path": "$.ingredients[0].evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path": "$.ingredients[1].evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path": "$.ingredients[2].evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path": "$.ingredients[3].evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path": "$.ingredients[4].evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path": "$.ingredients[5].evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path": "$.evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}], "target_attached_claims": 0, "variant_attached_claims": 0, "limit": "No transfer to the target, DSM8319 variant or another formulation."} |
| catalog-identity | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact accession650 catalog row; identity only | supports | The KOMODO catalog can establish the accession label/cross-reference used by the owner. It does not authenticate a formulation, modifier or cultivation outcome. |
| report-0 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_650_CENTENUM_medium.yaml.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Entire Oct7 KOMODO650 report read. It withheld quantities because the post-autoclave pyruvate stage was absent. Its exact historical raw is now recovered, but the report precedes and does not erase the later owner repairs. |
| report-1 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/medium_650_modified_for_dsm_8319.yaml.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Entire Oct7 DSM8319 report read. It explicitly withholds variant equivalence and source-derived quantity corrections; the base650 response cannot prove the variant recipe. |
| report-2 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/centenum_medium.yaml.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Entire Oct7 DSM650 report read. Four main rows were evidence-only provider nominal rates; water and pyruvate remained unsupported at that time. Later Oct8 owner repairs are current and receive credit. |
| report-3 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CENTENUM_MEDIUM.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Oct5 generated-target inventory has 0/6 source-checked rows; it is not independent recipe evidence. |
| report-4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Oct5 KOMODO650 owner inventory has 0/6 source-checked rows; it precedes the current repairs. |
| report-5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/centenum_medium.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Oct5 DSM650 owner inventory has 0/6 source-checked rows; it precedes the current repairs. |
| report-6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Oct5 DSM8319 inventory has 0/6 source-checked rows; it cannot authenticate the variant. |
| report-7 | reports/yaml_record_review/20260922T064817Z-CENTENUM_MEDIUM.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Entire September review read. Its old identical-signature and mass-conversion discussion predates the two owner repairs; neither a shared old signature nor the API mass field proves DSM8319 equivalence or replaces the primary post-autoclave 20 mM instruction. |
| writer-0 | scripts/repair_komodo650_752_762_preparations.py; Pinned source checks and complete medium650 build_changes branch | context_only | The current bounded repair targets the base KOMODO650 owner, authenticates the specified API response, retains explicitly qualified provider nominal main rates, and repairs water, pyruvate and preparation. It does not target or validate the DSM8319 variant; unrelated medium branches were not used as evidence. |
| writer-1 | scripts/repair_dsmz650_752_762_preparations.py; check_sources and complete medium650 build_changes branch | context_only | The current DSM650 repair checks paired medium/solution identities and recipe equality, retains previous history, and adds the qualified main-rate evidence plus source water/pyruvate/preparation. Its guard is current implementation context; the assessed owner and attached exact claims supply the observed repair evidence. |
| writer-2 | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit, _parse_preparation_steps | context_only | Current import separates main composition from referenced stock additions and maps provider units. Unit mapping alone cannot establish final volume. Preparation parsing still iterates solution steps, so their receiving-medium versus stock scope must be preserved. These functions do not prove which historical version produced the assessed record. |
| writer-3 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current web import builds source identity and a composition placeholder; it does not independently verify a later copied DSM formulation. Its time.strftime format includes %f, consistent with the malformed literal history timestamp, but current source code alone does not establish historical execution. |
| writer-4 | src/culturemech/enrich/dsmz_resolver.py; merge_composition | context_only | Current resolver copies non-placeholder DSM ingredients and solutions plus missing pH. Copied DSM data are shared provenance, not independent confirmation of KOMODO or strain-specific equivalence; the function does not transfer complete preparation. |
| writer-5 | src/culturemech/merge/formulation.py; Entire file: scientific projection, formulation_signature, merge_formulation_evidence | context_only | Current scientific comparison retains exact quantities, notes, preparation, solution structure and list order, and rejects incompatible formulations before provenance union. It is not an ingredient-only equivalence test. |
| writer-6 | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group invokes the exact scientific-formulation guard before combining evidence. Old generated content and old ingredient-signature merge history do not establish that the current guard would merge the now-divergent maintained owners. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15361 resolves to pyruvate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32599 resolves to magnesium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15361": [{"label": "Pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:15361", "preferred_term": "Pyruvate", "ontology_id": "CHEBI:15361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:32599": [{"label": "Magnesium sulfate", "match_type": "preferred_term", "identifier": "CHEBI:32599", "preferred_term": "Magnesium sulfate", "ontology_id": "CHEBI:32599", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/CENTENUM_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml; data/normalized_yaml/bacterial/centenum_medium.yaml; data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:05.825349"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:05.825349"}]}, {"input": "data/normalized_yaml/bacterial/centenum_medium.yaml", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:14.306730"}]}] |
| quantity-inventory | /private/tmp/culturemech-review-work-batch053/528/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The current exact api650 request returned HTTP 503. Its unusable maintenance/challenge body remains separate from the usable DSM650 primary and recovered historical API650 response.
- The current exact komodo650 request returned HTTP 403. Its unusable maintenance/challenge body remains separate from the usable DSM650 primary and recovered historical API650 response.
- The exact KOMODO650/DSM8319 variant request returned HTTP 403. No usable variant formulation was obtained; base DSM650 evidence cannot establish the variant changes or equivalence.
- The exact DSM8319 source remains unavailable; its quantities, preparation and equivalence are unresolved. Available base650 snippets are comparison context for that owner, not accepted replacements.
- Historical provider g_l values are authenticated as provider fields, not independently measured final concentrations. The primary lists 1000 ml water without declaring the final volume of the complete medium.
- No growth outcome or incubation optimum is inferred from the medium name, variant strain label, catalog listing or recipe instructions.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T201515Z-culturemech-006227-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: centenum_medium (CultureMech:006227)'
started_at: '2026-10-25T20:08:40Z'
finished_at: '2026-10-25T20:15:15Z'
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
summary: 'The selected CENTENUM target is stale relative to two repaired DSM650 base
  owners: they already preserve a volume-based water input, source-explicit 20 mM
  pyruvate and complete preparation. Fourteen attached claims authenticate against
  the exact recovered historical API650 response. The separate DSM8319 owner has no
  corresponding source verification, so old copied composition and identical ingredient
  signatures cannot establish variant equivalence. Preserve the valid base identity
  and existing repairs while resolving the generated target and variant boundary.'
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
  - path: data/merge_yaml/merged/CENTENUM_MEDIUM.yaml
    sha256: 8b7537e1f2d0238ce452963181599452de7a28f787bda5ae20f45b6fba5869d0
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml
    sha256: ad839535ab919eccd393580dbfb76ce0a7c671172d9ee5caf83ca289921ae488
    role: context
  - path: data/normalized_yaml/bacterial/centenum_medium.yaml
    sha256: 9fa412036e9c354447ce60eee9f278d5a479723534f0c9e7254c68c83a34d144
    role: context
  - path: data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml
    sha256: daaa3420b9bd6e2090e4f0a54e5c125650810fe1b3f2d4be6f4689c9dbd60696
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
  selection: Task review 528; batch 053 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding fifty-two task batches
    contain 520 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 231e0ba71b41d45362168d539efebe7991823464
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 523 of 6325 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006227
targets:
- target_id: CultureMech:006227
  path: data/merge_yaml/merged/CENTENUM_MEDIUM.yaml
  label: centenum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/centenum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/CENTENUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/CENTENUM_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch053/528/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch053/528/strict.tsv"
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/CENTENUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/CENTENUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006227
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
  - CultureMech:006227
- check_id: api650-source-access
  name: 'Exact source content access: api650'
  required: false
  status: unavailable
  summary: The current exact api650 request returned HTTP 503. Its unusable maintenance/challenge
    body remains separate from the usable DSM650 primary and recovered historical
    API650 response.
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - api650-attempt
- check_id: komodo650-source-access
  name: 'Exact source content access: komodo650'
  required: false
  status: unavailable
  summary: The current exact komodo650 request returned HTTP 403. Its unusable maintenance/challenge
    body remains separate from the usable DSM650 primary and recovered historical
    API650 response.
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - komodo650-attempt
- check_id: komodo650_8319-source-access
  name: 'Exact source content access: komodo650_8319'
  required: true
  status: unavailable
  summary: The exact KOMODO650/DSM8319 variant request returned HTTP 403. No usable
    variant formulation was obtained; base DSM650 evidence cannot establish the variant
    changes or equivalence.
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - komodo650_8319-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/CENTENUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/centenum_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/CENTENUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:46.174675Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/CENTENUM_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch053/528/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:50.292163Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch053/528/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/CENTENUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:55.348711Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/CENTENUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:57.814859Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-25T20:15:14Z'
  support: supports
  summary: './data/merge_yaml/merged/CENTENUM_MEDIUM.yaml:1:id: CultureMech:006227

    ./data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml:1:id: CultureMech:006227

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/source-preflight-bound/528/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-25T20:15:14Z'
  support: supports
  summary: 13 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 36741093b3276cb8e711ff72716106d6c989a45f2303323c68db0f9b3785be79
- evidence_id: source-reading
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/records527-528-source-reading-20261025T201126Z/source-reading.json
  locator: Complete selected documents, primary pages, fourteen historical reports
    and named current writer functions
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: The pinned reading receipt distinguishes complete source reads from derivative
    historical interpretation and from current writer behavior.
  snapshot_sha256: 3abfdc0608b7fe1ec45fe129effbc097de9262f7552d2edccbcaedf257015727
- evidence_id: context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/source-preflight-bound/528/evidence-context-original.json
  locator: Full per-record source context and scoped inventories
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Frozen local inventories, source captures, source-access outcomes and exact
    owner/parent scope; context is an index, not additional independent scientific
    evidence.
  snapshot_sha256: 8a29c767e300b60b41fd53d9a7ee1bcaa8f47805007dc3c25bd92ab212658993
- evidence_id: dsm650-main
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf
  locator: Complete page 1 main table, lines 4–8
  accessed_at: '2026-10-22T09:27:21.504255Z'
  support: supports
  summary: Current DSM650 lists the original main batch masses and 1000 ml tap water.
    The water input alone is not a final-medium volume declaration.
  quote: 650. CENTENUM MEDIUM
  snapshot_sha256: aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b
- evidence_id: dsm650-preparation
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf
  locator: Page 1 pH and preparation, lines 10–13
  accessed_at: '2026-10-22T09:27:21.504255Z'
  support: supports
  summary: The primary explicitly specifies pH 7, nitrogen boiling, 121 degrees C
    for 15 minutes and post-autoclave 20 mM pyruvate.
  quote: 'Boil under nitrogen gas and autoclave at 121C for 15 min. Add 20 mM pyruvate
    after

    autoclaving.'
  snapshot_sha256: aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b
- evidence_id: api650-historical
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/650
  locator: $.data.medium; $.data.solutions[0].recipe and steps; exact recovered parent
    $[30]
  accessed_at: '2026-10-07T12:17:00.953143Z'
  support: supports
  summary: The original UTF-8 response and original metadata were recovered by exact
    hash. It states provider nominal g_l values, original batch inputs and the same
    preparation. Access time remains 2026-10-07T12:17:00.953143+00:00; finish time
    is unknown. This is historical API650 evidence, not a new successful API request
    or automatic support for DSM8319.
  snapshot_sha256: fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8
- evidence_id: api650-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/650
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T09:27:22.389223Z'
  support: context_only
  summary: The current exact api650 request returned HTTP 503. Its unusable maintenance/challenge
    body remains separate from the usable DSM650 primary and recovered historical
    API650 response.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo650-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=650
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T09:27:23.076235Z'
  support: context_only
  summary: The current exact komodo650 request returned HTTP 403. Its unusable maintenance/challenge
    body remains separate from the usable DSM650 primary and recovered historical
    API650 response.
  snapshot_sha256: 6f362e3a338911a30d9b51e77242c95e9120a7cd747422ffdaaf29eaf9c7596a
- evidence_id: komodo650_8319-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=650_8319
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T09:27:23.136946Z'
  support: context_only
  summary: The exact KOMODO650/DSM8319 variant request returned HTTP 403. No usable
    variant formulation was obtained; base DSM650 evidence cannot establish the variant
    changes or equivalence.
  snapshot_sha256: 8d56b139095bc2275de75f5f3f0fc00ed0c47e697cc671b2e403212ee4563633
- evidence_id: owner-claim-authentication
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/source-preflight-bound/528/evidence-context-original.json
  locator: Fourteen independently checked base-owner ingredient/preparation claims;
    separate catalog identity claim
  accessed_at: '2026-10-25T20:15:14Z'
  support: supports
  summary: '{"authenticated_claims": [{"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
    "field_path": "$.ingredients[0].evidence[0]", "mode": "cited raw recovered and
    literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"},
    {"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path":
    "$.ingredients[1].evidence[0]", "mode": "cited raw recovered and literal matched",
    "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"},
    {"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path":
    "$.ingredients[2].evidence[0]", "mode": "cited raw recovered and literal matched",
    "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"},
    {"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path":
    "$.ingredients[3].evidence[0]", "mode": "cited raw recovered and literal matched",
    "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"},
    {"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path":
    "$.ingredients[4].evidence[0]", "mode": "cited raw recovered and literal matched",
    "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"},
    {"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path":
    "$.ingredients[5].evidence[0]", "mode": "cited raw recovered and literal matched",
    "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"},
    {"path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml", "field_path":
    "$.evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256":
    "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}, {"path":
    "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path": "$.ingredients[0].evidence[0]",
    "mode": "cited raw recovered and literal matched", "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"},
    {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path":
    "$.ingredients[1].evidence[0]", "mode": "cited raw recovered and literal matched",
    "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"},
    {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path":
    "$.ingredients[2].evidence[0]", "mode": "cited raw recovered and literal matched",
    "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"},
    {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path":
    "$.ingredients[3].evidence[0]", "mode": "cited raw recovered and literal matched",
    "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"},
    {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path":
    "$.ingredients[4].evidence[0]", "mode": "cited raw recovered and literal matched",
    "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"},
    {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path":
    "$.ingredients[5].evidence[0]", "mode": "cited raw recovered and literal matched",
    "source_sha256": "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"},
    {"path": "data/normalized_yaml/bacterial/centenum_medium.yaml", "field_path":
    "$.evidence[0]", "mode": "cited raw recovered and literal matched", "source_sha256":
    "fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8"}], "target_attached_claims":
    0, "variant_attached_claims": 0, "limit": "No transfer to the target, DSM8319
    variant or another formulation."}'
  snapshot_sha256: 8a29c767e300b60b41fd53d9a7ee1bcaa8f47805007dc3c25bd92ab212658993
- evidence_id: catalog-identity
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact accession650 catalog row; identity only
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The KOMODO catalog can establish the accession label/cross-reference used
    by the owner. It does not authenticate a formulation, modifier or cultivation
    outcome.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: report-0
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_650_CENTENUM_medium.yaml.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Entire Oct7 KOMODO650 report read. It withheld quantities because the post-autoclave
    pyruvate stage was absent. Its exact historical raw is now recovered, but the
    report precedes and does not erase the later owner repairs.
  snapshot_sha256: cea95c8bef224d7988c89e55916e6bfc1c85e40e1e04644c416ba76677bfaf5c
- evidence_id: report-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/medium_650_modified_for_dsm_8319.yaml.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Entire Oct7 DSM8319 report read. It explicitly withholds variant equivalence
    and source-derived quantity corrections; the base650 response cannot prove the
    variant recipe.
  snapshot_sha256: bf8b812d7257fd833fe40a0c3d65ecca0d062d667e5d7ef32e8da45fdc400b8d
- evidence_id: report-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/centenum_medium.yaml.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Entire Oct7 DSM650 report read. Four main rows were evidence-only provider
    nominal rates; water and pyruvate remained unsupported at that time. Later Oct8
    owner repairs are current and receive credit.
  snapshot_sha256: 11adfae044a191efafa6569efa6dae001a26c2b4186bb1c4165f15ec06fb5aa7
- evidence_id: report-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CENTENUM_MEDIUM.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Oct5 generated-target inventory has 0/6 source-checked rows; it is not
    independent recipe evidence.
  snapshot_sha256: 64359ed6e4f323a585a64a19e0259164f4e54dd0e8d5c90443fca6183b6c91e1
- evidence_id: report-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Oct5 KOMODO650 owner inventory has 0/6 source-checked rows; it precedes
    the current repairs.
  snapshot_sha256: 9305c9cfd434cbb5f857fd99357fe9a811cb31a48a3d05d779959557c84250b2
- evidence_id: report-5
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/centenum_medium.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Oct5 DSM650 owner inventory has 0/6 source-checked rows; it precedes the
    current repairs.
  snapshot_sha256: fabcbe826c085e4f317e0f4dffb71c125ef8c93ca6d7c378eb5aa003bcbc9f94
- evidence_id: report-6
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Oct5 DSM8319 inventory has 0/6 source-checked rows; it cannot authenticate
    the variant.
  snapshot_sha256: f8616b950028d94561a0c4a986c40d5fdcdfa14324af5f8fa130447d9f7d7bdb
- evidence_id: report-7
  kind: record_content
  reference: reports/yaml_record_review/20260922T064817Z-CENTENUM_MEDIUM.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Entire September review read. Its old identical-signature and mass-conversion
    discussion predates the two owner repairs; neither a shared old signature nor
    the API mass field proves DSM8319 equivalence or replaces the primary post-autoclave
    20 mM instruction.
  snapshot_sha256: 5a517b2db46fa7608fa93b1fd6f7ca36633e65d9e9187b38ed2f820fc9ff5c4c
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_komodo650_752_762_preparations.py
  locator: Pinned source checks and complete medium650 build_changes branch
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: The current bounded repair targets the base KOMODO650 owner, authenticates
    the specified API response, retains explicitly qualified provider nominal main
    rates, and repairs water, pyruvate and preparation. It does not target or validate
    the DSM8319 variant; unrelated medium branches were not used as evidence.
  snapshot_sha256: 477e2e14b5ff6284e4e291986b333552215f44dca2473fc64cf1d60e0028c0bd
- evidence_id: writer-1
  kind: record_content
  reference: scripts/repair_dsmz650_752_762_preparations.py
  locator: check_sources and complete medium650 build_changes branch
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: The current DSM650 repair checks paired medium/solution identities and
    recipe equality, retains previous history, and adds the qualified main-rate evidence
    plus source water/pyruvate/preparation. Its guard is current implementation context;
    the assessed owner and attached exact claims supply the observed repair evidence.
  snapshot_sha256: 0b955dd562a885fec75dd73bed1eaa00af707b3e2f9d35f7f16b066feb743e1a
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit,
    _parse_preparation_steps
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Current import separates main composition from referenced stock additions
    and maps provider units. Unit mapping alone cannot establish final volume. Preparation
    parsing still iterates solution steps, so their receiving-medium versus stock
    scope must be preserved. These functions do not prove which historical version
    produced the assessed record.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Current web import builds source identity and a composition placeholder;
    it does not independently verify a later copied DSM formulation. Its time.strftime
    format includes %f, consistent with the malformed literal history timestamp, but
    current source code alone does not establish historical execution.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer-4
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: merge_composition
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Current resolver copies non-placeholder DSM ingredients and solutions plus
    missing pH. Copied DSM data are shared provenance, not independent confirmation
    of KOMODO or strain-specific equivalence; the function does not transfer complete
    preparation.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-5
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: 'Entire file: scientific projection, formulation_signature, merge_formulation_evidence'
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Current scientific comparison retains exact quantities, notes, preparation,
    solution structure and list order, and rejects incompatible formulations before
    provenance union. It is not an ingredient-only equivalence test.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-6
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Current merge_group invokes the exact scientific-formulation guard before
    combining evidence. Old generated content and old ingredient-signature merge history
    do not establish that the current guard would merge the now-divergent maintained
    owners.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:00:46.687620Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15361
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T17:04:22.664513Z'
  support: supports
  summary: CHEBI:15361 resolves to pyruvate. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 961a069a15db5bfd8c497d805e6d3cfb6ac1dc89ca248f4f22e208c407b993d2
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:30.346522Z'
  support: supports
  summary: CHEBI:15377 resolves to water. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi32599
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.640268Z'
  support: supports
  summary: CHEBI:32599 resolves to magnesium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-25T20:15:14Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:15361": [{"label": "Pyruvate", "match_type": "preferred_term",
    "identifier": "CHEBI:15361", "preferred_term": "Pyruvate", "ontology_id": "CHEBI:15361",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label":
    "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:32599": [{"label": "Magnesium sulfate", "match_type": "preferred_term",
    "identifier": "CHEBI:32599", "preferred_term": "Magnesium sulfate", "ontology_id":
    "CHEBI:32599", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/CENTENUM_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml;
    data/normalized_yaml/bacterial/centenum_medium.yaml; data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:05.825349"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:05.825349"}]}, {"input": "data/normalized_yaml/bacterial/centenum_medium.yaml",
    "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:14.306730"}]}]'
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/528/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-25T20:15:14Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 31827c603cfd188179c61c394d6db99048ea07369e669175d3e427ea65099b46
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '5 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels across the selected target and its exact maintained
    owners. Target linkage: 5/6 primary and 5/6 secondary instances; all asserted
    current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Complete
    recursive inspection of these selected documents found zero legacy mediaingredientmech_term
    slots and zero numeric legacy MediaIngredientMech identifiers. Generic placeholder
    text in history is not an asserted identifier. Source forms are assessed separately.'
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - owner-2
  - chebi131527
  - chebi15361
  - chebi15377
  - chebi176843
  - chebi32599
  details: 'Instance coverage on a 0–100 percent scale, denominator 6: primary 83.33%;
    secondary 83.33%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 32 timestamp instances inspected; 6 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 23 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"K2HPO4 in generated\
    \ base target\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/CENTENUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 4: K2HPO4\",\n\
    \        \"exact_source_quote\": \"K2HPO4                                    \
    \                     1.0       g\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n                  \
    \      \\\"mmol_l\\\": 5.74132,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The historical API explicitly supplies this nominal\
    \ g_l value and the primary supplies the matching batch mass. The target lacks\
    \ the current owner explanation/evidence. Add qualified support for the base recipe;\
    \ do not call it an independently measured final-medium concentration or source\
    \ support for DSM8319.\"\n  },\n  {\n    \"decision_id\": \"q2\",\n    \"subject\"\
    : \"K2HPO4 in the two repaired base owners\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/centenum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 4: K2HPO4\",\n\
    \        \"exact_source_quote\": \"K2HPO4                                    \
    \                     1.0       g\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n                  \
    \      \\\"mmol_l\\\": 5.74132,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Each current base owner independently carries a literal,\
    \ cited-raw-hash-matched claim and explicitly qualifies the retained G_PER_L as\
    \ a provider nominal main rate. Verification is limited to that representation\
    \ and its scope; listed water is not an independently declared final volume.\"\
    \n  },\n  {\n    \"decision_id\": \"q3\",\n    \"subject\": \"K2HPO4 in DSM8319\
    \ variant\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 4: K2HPO4\",\n\
    \        \"exact_source_quote\": \"K2HPO4                                    \
    \                     1.0       g\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n                  \
    \      \\\"mmol_l\\\": 5.74132,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"These snippets describe base DSM650 only and are included\
    \ as comparison context. The exact variant provider is unavailable and no attached\
    \ variant claim authenticates this value. No source-derived replacement is proposed\
    \ for the variant.\",\n    \"proposed_source_representation\": {\n      \"stage\"\
    : \"DSM8319 variant\",\n      \"replacement\": null,\n      \"reason\": \"exact\
    \ variant formulation unresolved\"\n    }\n  },\n  {\n    \"decision_id\": \"\
    q4\",\n    \"subject\": \"MgSO4 in generated base target\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/CENTENUM_MEDIUM.yaml\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 5: MgSO4\",\n\
    \        \"exact_source_quote\": \"MgSO4                                     \
    \                     0.5       g\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MgSO4\\\",\\n                        \\\"compound_id\\\": 325,\\\
    n                        \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n                \
    \        \\\"mmol_l\\\": 4.15386,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The historical API explicitly supplies this nominal\
    \ g_l value and the primary supplies the matching batch mass. The target lacks\
    \ the current owner explanation/evidence. Add qualified support for the base recipe;\
    \ do not call it an independently measured final-medium concentration or source\
    \ support for DSM8319.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"subject\"\
    : \"MgSO4 in the two repaired base owners\",\n    \"decision\": \"verified\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/centenum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 5: MgSO4\",\n\
    \        \"exact_source_quote\": \"MgSO4                                     \
    \                     0.5       g\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MgSO4\\\",\\n                        \\\"compound_id\\\": 325,\\\
    n                        \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n                \
    \        \\\"mmol_l\\\": 4.15386,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Each current base owner independently carries a literal,\
    \ cited-raw-hash-matched claim and explicitly qualifies the retained G_PER_L as\
    \ a provider nominal main rate. Verification is limited to that representation\
    \ and its scope; listed water is not an independently declared final volume.\"\
    \n  },\n  {\n    \"decision_id\": \"q6\",\n    \"subject\": \"MgSO4 in DSM8319\
    \ variant\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 5: MgSO4\",\n\
    \        \"exact_source_quote\": \"MgSO4                                     \
    \                     0.5       g\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MgSO4\\\",\\n                        \\\"compound_id\\\": 325,\\\
    n                        \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n                \
    \        \\\"mmol_l\\\": 4.15386,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"These snippets describe base DSM650 only and are included\
    \ as comparison context. The exact variant provider is unavailable and no attached\
    \ variant claim authenticates this value. No source-derived replacement is proposed\
    \ for the variant.\",\n    \"proposed_source_representation\": {\n      \"stage\"\
    : \"DSM8319 variant\",\n      \"replacement\": null,\n      \"reason\": \"exact\
    \ variant formulation unresolved\"\n    }\n  },\n  {\n    \"decision_id\": \"\
    q7\",\n    \"subject\": \"Yeast extract in generated base target\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/CENTENUM_MEDIUM.yaml\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 6: Yeast extract\"\
    ,\n        \"exact_source_quote\": \"Yeast extract                           \
    \                      10.0       g\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n   \
    \                     \\\"optional\\\": 0\\n                    }\",\n       \
    \ \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The historical API explicitly supplies this nominal\
    \ g_l value and the primary supplies the matching batch mass. The target lacks\
    \ the current owner explanation/evidence. Add qualified support for the base recipe;\
    \ do not call it an independently measured final-medium concentration or source\
    \ support for DSM8319.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"subject\"\
    : \"Yeast extract in the two repaired base owners\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/centenum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 6: Yeast extract\"\
    ,\n        \"exact_source_quote\": \"Yeast extract                           \
    \                      10.0       g\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n   \
    \                     \\\"optional\\\": 0\\n                    }\",\n       \
    \ \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Each current base owner independently carries a literal,\
    \ cited-raw-hash-matched claim and explicitly qualifies the retained G_PER_L as\
    \ a provider nominal main rate. Verification is limited to that representation\
    \ and its scope; listed water is not an independently declared final volume.\"\
    \n  },\n  {\n    \"decision_id\": \"q9\",\n    \"subject\": \"Yeast extract in\
    \ DSM8319 variant\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 6: Yeast extract\"\
    ,\n        \"exact_source_quote\": \"Yeast extract                           \
    \                      10.0       g\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n   \
    \                     \\\"optional\\\": 0\\n                    }\",\n       \
    \ \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"These snippets describe base DSM650 only and are included\
    \ as comparison context. The exact variant provider is unavailable and no attached\
    \ variant claim authenticates this value. No source-derived replacement is proposed\
    \ for the variant.\",\n    \"proposed_source_representation\": {\n      \"stage\"\
    : \"DSM8319 variant\",\n      \"replacement\": null,\n      \"reason\": \"exact\
    \ variant formulation unresolved\"\n    }\n  },\n  {\n    \"decision_id\": \"\
    q10\",\n    \"subject\": \"Vitamin B12 in generated base target\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/CENTENUM_MEDIUM.yaml\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2e-05\",\n          \"unit\"\
    : \"G_PER_L\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 7: Vitamin B12\"\
    ,\n        \"exact_source_quote\": \"Vitamin B12                             \
    \                      20.0      μg\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Vitamin B12\\\",\\n                        \\\"compound_id\\\
    \": 18,\\n                        \\\"amount\\\": 20,\\n                     \
    \   \\\"unit\\\": \\\"\\\\u00b5g\\\",\\n                        \\\"g_l\\\": 2.0e-5,\\\
    n                        \\\"mmol_l\\\": 1.47558e-5,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\",\n    \
    \    \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The historical API explicitly supplies this nominal\
    \ g_l value and the primary supplies the matching batch mass. The target lacks\
    \ the current owner explanation/evidence. Add qualified support for the base recipe;\
    \ do not call it an independently measured final-medium concentration or source\
    \ support for DSM8319.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"subject\"\
    : \"Vitamin B12 in the two repaired base owners\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2e-05\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/centenum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2e-05\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 7: Vitamin B12\"\
    ,\n        \"exact_source_quote\": \"Vitamin B12                             \
    \                      20.0      μg\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Vitamin B12\\\",\\n                        \\\"compound_id\\\
    \": 18,\\n                        \\\"amount\\\": 20,\\n                     \
    \   \\\"unit\\\": \\\"\\\\u00b5g\\\",\\n                        \\\"g_l\\\": 2.0e-5,\\\
    n                        \\\"mmol_l\\\": 1.47558e-5,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\",\n    \
    \    \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Each current base owner independently carries a literal,\
    \ cited-raw-hash-matched claim and explicitly qualifies the retained G_PER_L as\
    \ a provider nominal main rate. Verification is limited to that representation\
    \ and its scope; listed water is not an independently declared final volume.\"\
    \n  },\n  {\n    \"decision_id\": \"q12\",\n    \"subject\": \"Vitamin B12 in\
    \ DSM8319 variant\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2e-05\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 7: Vitamin B12\"\
    ,\n        \"exact_source_quote\": \"Vitamin B12                             \
    \                      20.0      μg\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Vitamin B12\\\",\\n                        \\\"compound_id\\\
    \": 18,\\n                        \\\"amount\\\": 20,\\n                     \
    \   \\\"unit\\\": \\\"\\\\u00b5g\\\",\\n                        \\\"g_l\\\": 2.0e-5,\\\
    n                        \\\"mmol_l\\\": 1.47558e-5,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\",\n    \
    \    \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"These snippets describe base DSM650 only and are included\
    \ as comparison context. The exact variant provider is unavailable and no attached\
    \ variant claim authenticates this value. No source-derived replacement is proposed\
    \ for the variant.\",\n    \"proposed_source_representation\": {\n      \"stage\"\
    : \"DSM8319 variant\",\n      \"replacement\": null,\n      \"reason\": \"exact\
    \ variant formulation unresolved\"\n    }\n  },\n  {\n    \"decision_id\": \"\
    q13\",\n    \"subject\": \"Target tap-water dimension\",\n    \"decision\": \"\
    correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CENTENUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Tap water\\\",\\n                        \\\"compound_id\\\"\
    : 322,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Base DSM650 prints 1000 ml tap water, equivalent to\
    \ 1 L batch input. The target stores a mass-per-volume unit. This correction concerns\
    \ the water input dimension and does not establish final medium volume.\",\n \
    \   \"proposed_source_representation\": {\n      \"stage\": \"base main batch\"\
    ,\n      \"amount\": 1,\n      \"unit\": \"L\",\n      \"basis\": \"water input\"\
    \n    }\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"subject\": \"Repaired\
    \ base-owner water input\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        }\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/centenum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        }\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz650\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Tap water\\\",\\n                        \\\"compound_id\\\"\
    : 322,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Both base owners already retain 1 L tap-water input\
    \ with independently authenticated claims. Preserve this repair and its explicit\
    \ limit: it is not water mass or measured final volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"subject\": \"Variant water dimension and unresolved recipe\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: Tap water\"\
    ,\n        \"exact_source_quote\": \"Tap water                               \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\"\
    ,\n        \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Tap water\\\",\\n                        \\\"compound_id\\\"\
    : 322,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The existing G_PER_L represents water as a mass concentration,\
    \ but these available source quantities belong to base650. The exact variant water\
    \ amount remains unverified; do not copy the base amount into DSM8319 as an authenticated\
    \ correction.\",\n    \"proposed_source_representation\": {\n      \"stage\":\
    \ \"DSM8319 variant\",\n      \"replacement\": null,\n      \"reason\": \"source\
    \ amount unresolved; current dimensional representation also requires review\"\
    \n    }\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"subject\": \"Target post-autoclave\
    \ pyruvate\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/CENTENUM_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.741\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 12–13\",\n \
    \       \"exact_source_quote\": \"Boil under nitrogen gas and autoclave at 121C\
    \ for 15 min. Add 20 mM pyruvate after\\nautoclaving.\",\n        \"snapshot_sha256\"\
    : \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\",\n    \
    \    \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Pyruvate\\\",\\n                        \\\"compound_id\\\"\
    : 1386,\\n                        \\\"amount\\\": 20,\\n                     \
    \   \\\"unit\\\": \\\"mM\\\",\\n                        \\\"g_l\\\": 1.741,\\\
    n                        \\\"mmol_l\\\": 20,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The historical provider explicitly contains g_l 1.741,\
    \ so that number is not unsupported by every source. The current primary and API\
    \ preparation explicitly prescribe 20 mM after autoclaving. Restore that source\
    \ basis and stage in the base target rather than treating the imported mass field\
    \ as a complete operational representation.\",\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"after autoclaving\",\n      \"amount\": 20,\n      \"\
    unit\": \"MILLIMOLAR\",\n      \"mass_conversion_required\": false\n    }\n  },\n\
    \  {\n    \"decision_id\": \"q17\",\n    \"subject\": \"Repaired base-owner pyruvate\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"MILLIMOLAR\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/centenum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"MILLIMOLAR\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 12–13\",\n \
    \       \"exact_source_quote\": \"Boil under nitrogen gas and autoclave at 121C\
    \ for 15 min. Add 20 mM pyruvate after\\nautoclaving.\",\n        \"snapshot_sha256\"\
    : \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\",\n    \
    \    \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Pyruvate\\\",\\n                        \\\"compound_id\\\"\
    : 1386,\\n                        \\\"amount\\\": 20,\\n                     \
    \   \\\"unit\\\": \\\"mM\\\",\\n                        \\\"g_l\\\": 1.741,\\\
    n                        \\\"mmol_l\\\": 20,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Both base owners already retain source-explicit 20\
    \ mM with post-autoclave preparation and independently matched claims. No salt,\
    \ molecular-weight or stock-dilution assumption is needed.\"\n  },\n  {\n    \"\
    decision_id\": \"q18\",\n    \"subject\": \"Variant pyruvate\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.741\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 12–13\",\n \
    \       \"exact_source_quote\": \"Boil under nitrogen gas and autoclave at 121C\
    \ for 15 min. Add 20 mM pyruvate after\\nautoclaving.\",\n        \"snapshot_sha256\"\
    : \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\",\n    \
    \    \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"api650Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/650\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Pyruvate\\\",\\n                        \\\"compound_id\\\"\
    : 1386,\\n                        \\\"amount\\\": 20,\\n                     \
    \   \\\"unit\\\": \\\"mM\\\",\\n                        \\\"g_l\\\": 1.741,\\\
    n                        \\\"mmol_l\\\": 20,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"fdbfb5a84dab70fc5ca5fb99ad20cfbc3f471adfbe90612cb18834a0c7805dc8\"\
    ,\n        \"accessed_at\": \"2026-10-07T12:17:00.953143+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"API650 g_l 1.741 and the base post-autoclave 20 mM\
    \ instruction are comparison context only. Neither authenticates DSM8319 formulation\
    \ or timing. Resolve its own source before any replacement.\",\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"DSM8319 variant\",\n      \"replacement\": null,\n   \
    \   \"reason\": \"exact variant source unavailable\"\n    }\n  },\n  {\n    \"\
    decision_id\": \"q19\",\n    \"subject\": \"Base target and owners pH\",\n   \
    \ \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/CENTENUM_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ph_value\",\n        \"stored\": 7.0\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml\",\n      \
    \  \"field_path\": \"ph_value\",\n        \"stored\": 7.0\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/centenum_medium.yaml\",\n\
    \        \"field_path\": \"ph_value\",\n        \"stored\": 7.0\n      }\n   \
    \ ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz650\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: Adjust pH\"\
    ,\n        \"exact_source_quote\": \"Adjust pH to 7.0.\",\n        \"snapshot_sha256\"\
    : \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\",\n    \
    \    \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The primary explicitly states pH 7.0; all three base\
    \ representations agree. This supports the base recipe pH, not an unstated optimum,\
    \ buffer capacity or strain-specific growth result.\"\n  },\n  {\n    \"decision_id\"\
    : \"q20\",\n    \"subject\": \"Variant pH\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz650\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: Adjust pH\"\
    ,\n        \"exact_source_quote\": \"Adjust pH to 7.0.\",\n        \"snapshot_sha256\"\
    : \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\",\n    \
    \    \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The quoted pH is base650 context only. Exact DSM8319\
    \ pH remains unverified and no replacement is proposed.\"\n  },\n  {\n    \"decision_id\"\
    : \"q21\",\n    \"subject\": \"Current base-owner preparation step 1\",\n    \"\
    decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml\",\n      \
    \  \"field_path\": \"preparation_steps[0].step_number\",\n        \"stored\":\
    \ 1\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/centenum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].step_number\",\n        \"stored\"\
    : 1\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.0.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/centenum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.0.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: Adjust pH\"\
    ,\n        \"exact_source_quote\": \"Adjust pH to 7.0.\",\n        \"snapshot_sha256\"\
    : \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\",\n    \
    \    \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The retained instruction is source-supported and already\
    \ present in both repaired owners. The step number is local ordering metadata.\
    \ Preserve the exact source scope; a valid recipe instruction is not experimental\
    \ growth evidence.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"subject\"\
    : \"Current base-owner preparation step 2\",\n    \"decision\": \"verified\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].step_number\",\n        \"stored\"\
    : 2\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/centenum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].step_number\",\n        \"stored\"\
    : 2\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Boil under nitrogen gas and autoclave at 121°C for 15 min. Add 20 mM pyruvate\
    \ after autoclaving.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/centenum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Boil under nitrogen gas and autoclave at 121°C for 15 min. Add 20 mM pyruvate\
    \ after autoclaving.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 12–13\",\n \
    \       \"exact_source_quote\": \"Boil under nitrogen gas and autoclave at 121C\
    \ for 15 min. Add 20 mM pyruvate after\\nautoclaving.\",\n        \"snapshot_sha256\"\
    : \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\",\n    \
    \    \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The retained instruction is source-supported and already\
    \ present in both repaired owners. The step number is local ordering metadata.\
    \ Preserve the exact source scope; a valid recipe instruction is not experimental\
    \ growth evidence.\"\n  },\n  {\n    \"decision_id\": \"q23\",\n    \"subject\"\
    : \"Missing base-target preparation\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz650\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: Adjust pH\"\
    ,\n        \"exact_source_quote\": \"Adjust pH to 7.0.\",\n        \"snapshot_sha256\"\
    : \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\",\n    \
    \    \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz650\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 12–13\",\n \
    \       \"exact_source_quote\": \"Boil under nitrogen gas and autoclave at 121C\
    \ for 15 min. Add 20 mM pyruvate after\\nautoclaving.\",\n        \"snapshot_sha256\"\
    : \"aaea38f1b4bf06121347206d7ac9786b2f6d663355757ad126c38db74aecee3b\",\n    \
    \    \"parsed_text_sha256\": \"36811a1605967bf4eec176b7b24763aa4dcd33692db93ac52c2586f4c9a5011d\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:21.504255+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The generated target omits the now-retained owner\
    \ preparation. Restore pH adjustment, nitrogen boiling, 121 degrees C for 15 minutes\
    \ and post-autoclave 20 mM pyruvate only for the verified base650 formulation;\
    \ do not transfer these as variant evidence.\",\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"base650 preparation\",\n      \"pH\": 7,\n      \"gas\"\
    : \"nitrogen\",\n      \"autoclave_temperature_C\": 121,\n      \"autoclave_duration_min\"\
    : 15,\n      \"post_autoclave_pyruvate_mM\": 20\n    }\n  }\n]"
- assessment_id: identity
  area: identity
  topic: Valid base identity and unresolved DSM8319 merge boundary
  outcome: concern
  summary: DSM650 is a valid source for the selected base target and two maintained
    base owners. The third owner is explicitly a DSM8319 modifier, whose exact source
    is unavailable. Old copied DSM composition and matching signatures cannot independently
    establish that the modifier is identical to the base.
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - dsm650-main
  - catalog-identity
  - komodo650_8319-attempt
- assessment_id: repair-credit
  area: consistency
  topic: Existing owner repairs versus generated staleness
  outcome: concern
  summary: The two base owners already contain water 1 L, pyruvate 20 mM, source preparation
    and fourteen authenticated claims. The generated target predates these repairs
    and retains the old water unit, mass-only pyruvate and absent preparation. Current
    merge code protects exact scientific fields; this is stale generated content,
    not proof the current guard still performs ingredient-only consolidation.
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - owner-0
  - owner-1
  - owner-2
  - owner-claim-authentication
  - record
  - quantity-inventory
  - writer-0
  - writer-1
  - writer-2
  - writer-3
  - writer-4
  - writer-5
  - writer-6
- assessment_id: historical-support
  area: evidence
  topic: Exact raw recovery and time/claim boundaries
  outcome: supported
  summary: The historical API650 raw matches the cited digest and fourteen owner snippets.
    The original access time is retained and finish is unknown. Current failed retrievals
    remain separate. Reports are derivative accounts, and base evidence is not promoted
    into a verified DSM8319 recipe.
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - api650-historical
  - owner-claim-authentication
  - api650-attempt
  - komodo650-attempt
  - report-0
  - report-1
  - report-2
  - report-3
  - report-4
  - report-5
  - report-6
  - report-7
- assessment_id: classification
  area: scope
  topic: Record type, category and growth claims
  outcome: unknown
  summary: The selected documents are bacterial liquid MediaRecipe records. The bounded
    collection formulation establishes a recipe identity, not strain-specific experimental
    growth. No organism growth assertion, incubation optimum or literature-wide evidence
    claim is added.
  target_ids:
  - CultureMech:006227
  evidence_ids:
  - record
  - dsm650-main
findings:
- finding_id: f1
  issue_key: CENTENUM_VARIANT_BOUNDARY
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Resolve DSM8319 membership independently of copied base composition
  description: The generated target includes medium650_modified_for_dsm8319 among
    its merge sources. That owner has a distinct variant identity and lacks exact
    source authentication, while the two base owners now have materially different
    quantities and preparation. Base API650 claims cannot resolve the modifier. The
    confirmed defect is the unsubstantiated equivalence claim, not proof that every
    variant ingredient is numerically wrong.
  target_ids:
  - CultureMech:006227
  field_paths:
  - merged_from
  - curation_history
  evidence_ids:
  - record
  - owner-2
  - komodo650_8319-attempt
  - api650-historical
  - report-1
  - writer-5
  - writer-6
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/centenum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: SOURCE_VARIANT_EQUIVALENCE
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CENTENUM_GENERATED_STALENESS
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Regenerate the base target from the repaired owners after identity resolution
  description: The base owners already correct tap water from 1000 G_PER_L to 1 L
    input, retain 20 mM pyruvate added after autoclaving, and preserve the pH/nitrogen/autoclave
    preparation. The target still has the old mass-unit water and mass-only pyruvate
    and no preparation. Main g_l values are explicit historical provider nominal fields,
    not a fabricated mass discrepancy.
  target_ids:
  - CultureMech:006227
  field_paths:
  - ingredients[4].concentration
  - ingredients[5].concentration
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-claim-authentication
  - dsm650-main
  - dsm650-preparation
  - quantity-inventory
  - writer-0
  - writer-1
  - writer-5
  - writer-6
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/centenum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: GENERATED_OWNER_FRESHNESS
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CENTENUM_HISTORY_TIMESTAMP
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify malformed import times without replacing their history
  description: The target and KOMODO-derived owners retain literal .fZ timestamps
    that are not valid UTC instants. Exact historical API access time is separately
    recoverable and must not be substituted for an unknown importer execution time.
  target_ids:
  - CultureMech:006227
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  - writer-3
  - api650-historical
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/centenum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: PROVENANCE_TIMESTAMP_SHAPE
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Resolve the exact DSM8319 variant identity and source independently.
    Retain a distinct owner/variant boundary until equivalence is supported; do not
    discard the valid DSM650 identity or copy base corrections into the modifier without
    evidence.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006227
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/centenum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml
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
  description: Credit and preserve both owner repairs. Resolve merge membership, then
    regenerate the base target with the corrected source basis, preparation and claim-level
    evidence. Keep nominal provider rates qualified and final-volume assumptions unresolved.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006227
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/centenum_medium.yaml
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
  description: Preserve existing history and append a bounded clarification of malformed
    import timestamps; verify the current timestamp writer separately without inventing
    original execution times.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006227
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/centenum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.yaml
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
- The current exact api650 request returned HTTP 503. Its unusable maintenance/challenge
  body remains separate from the usable DSM650 primary and recovered historical API650
  response.
- The current exact komodo650 request returned HTTP 403. Its unusable maintenance/challenge
  body remains separate from the usable DSM650 primary and recovered historical API650
  response.
- The exact KOMODO650/DSM8319 variant request returned HTTP 403. No usable variant
  formulation was obtained; base DSM650 evidence cannot establish the variant changes
  or equivalence.
- The exact DSM8319 source remains unavailable; its quantities, preparation and equivalence
  are unresolved. Available base650 snippets are comparison context for that owner,
  not accepted replacements.
- Historical provider g_l values are authenticated as provider fields, not independently
  measured final concentrations. The primary lists 1000 ml water without declaring
  the final volume of the complete medium.
- No growth outcome or incubation optimum is inferred from the medium name, variant
  strain label, catalog listing or recipe instructions.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-053
- generated-medium
```
