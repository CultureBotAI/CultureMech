# Source and formulation review: acidiphilium_medium (CultureMech:002462)

- Review: 20261021T112127Z-culturemech-002462-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T11:17:43Z
- Finished UTC: 2026-10-21T11:21:27Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 129 is an Acidiphilium formulation with separately prepared solutions A and B and a small BD-BBL Trypticase soy broth addition. Both local layers replace that commercial addition with unscaled generic TSB/TSA constituents, including unconditional agar, and omit the two preparation stages. Exact supplier formulation correspondence remains unavailable, so the review is partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 172; batch 018 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seventeen task batches contain 170 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 172 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002462 | data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml | generated | acidiphilium_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002462 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002462 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch018/172/strict.tsv |
| validate-terms | passed | True | CultureMech:002462 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002462 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002462 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: bd211825PriorAttempt | unavailable | True | CultureMech:002462 | The exact asserted BD 211825 product attempt returned HTTP 403; the preserved prior metadata provides no product formulation bytes. BD-BBL Trypticase soy broth identity, catalog equivalence and constituent proportions cannot be verified from that failed request. |
| Exact source content access: bdManualPriorAttempt | unavailable | False | CultureMech:002462 | The preserved BD manual attempt returned HTTP 404. No manual content was inspected; it cannot corroborate a product or mixture recipe. |
| Exact source content access: sigma22092 | unavailable | True | CultureMech:002462 | The exact asserted Sigma 22092 specification attempt timed out without captured formula bytes. Its equivalence to the primary’s BD-BBL product and the stated multi-supplier constituent formula remain unresolved; no Sigma formula substitutes for BD-BBL. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002462.

The four documented recipes completed; interpret the scope of each separately.

### Exact source accession and commercial-product boundary

identity: concern. Targets: CultureMech:002462.

CultureMech:002462 resolves to JCM 129 and provider J129, with one exact normalized owner. Interchangeability between the primary’s BD-BBL Trypticase soy broth and the local multi-supplier TSB/TSA label or asserted catalog numbers is not established. The generic encyclopedia URL is a secondary lead, not verified product-specific evidence. The medium title and application do not establish a species or strain growth claim.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:002462.

29 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "input": "target",
    "field_path": "ingredients[0].concentration",
    "ingredient": "(NH4)2SO4",
    "existing": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "Solution A",
    "source_amount": {
      "value": 2,
      "unit": "g"
    },
    "basis": "JCM batch comprises separate 500 ml water portions; provider explicitly declares 1000 ml and g_l. Retain that declared basis rather than claim a measured final volume.",
    "proposed": "Retain the supported provider-basis value, add exact claim evidence and preserve the primary preparation stage.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, exact named ingredient row",
        "exact_source_quote": "(NH 4 ) 2 SO 4 2.0 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 15.1355,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ingredients[1].concentration",
    "ingredient": "KCl",
    "existing": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "Solution A",
    "source_amount": {
      "value": 0.1,
      "unit": "g"
    },
    "basis": "JCM batch comprises separate 500 ml water portions; provider explicitly declares 1000 ml and g_l. Retain that declared basis rather than claim a measured final volume.",
    "proposed": "Retain the supported provider-basis value, add exact claim evidence and preserve the primary preparation stage.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, exact named ingredient row",
        "exact_source_quote": "KCl 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.34138,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ingredients[2].concentration",
    "ingredient": "K2HPO4",
    "existing": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "Solution A",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "basis": "JCM batch comprises separate 500 ml water portions; provider explicitly declares 1000 ml and g_l. Retain that declared basis rather than claim a measured final volume.",
    "proposed": "Retain the supported provider-basis value, add exact claim evidence and preserve the primary preparation stage.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, exact named ingredient row",
        "exact_source_quote": "K 2 HPO 4 0.5 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.87066,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ingredients[3].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "existing": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "Solution A",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "basis": "JCM batch comprises separate 500 ml water portions; provider explicitly declares 1000 ml and g_l. Retain that declared basis rather than claim a measured final volume.",
    "proposed": "Retain the supported provider-basis value, add exact claim evidence and preserve the primary preparation stage.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, exact named ingredient row",
        "exact_source_quote": "MgSO 4 ·7H 2 O 0.5 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ingredients[4].concentration",
    "ingredient": "Pancreatic digest of casein",
    "existing": {
      "value": "17.0",
      "unit": "G_PER_L"
    },
    "decision": "correct",
    "source_stage": "Unverified commercial-product decomposition placed at receiving-medium root",
    "proposed": "Replace the unscaled generic constituent assertion with the exact source-supported opaque BD-BBL broth addition pending a verified product specification. No replacement constituent amount is calculated.",
    "source_amount": {
      "value": 0.1,
      "unit": "g",
      "material": "BD-BBL Trypticase soy broth as a whole"
    },
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, commercial broth row",
        "exact_source_quote": "Trypticase soy broth (BD-BBL) 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase soy broth\",\n                        \"compound_id\": 99,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ],
    "explanation": "The primary supports 0.1 g of the whole product, not this generic constituent amount. The five non-agar decomposition values total 30 g/L locally; even if a generic 30 g/L stock formula were independently verified, its values could not be inserted unchanged for this 0.1 g addition. Exact constituent proportions and product equivalence remain unavailable, so no scaling or substitute formulation is proposed."
  },
  {
    "input": "target",
    "field_path": "ingredients[5].concentration",
    "ingredient": "Peptic digest of soybean meal",
    "existing": {
      "value": "3.0",
      "unit": "G_PER_L"
    },
    "decision": "correct",
    "source_stage": "Unverified commercial-product decomposition placed at receiving-medium root",
    "proposed": "Replace the unscaled generic constituent assertion with the exact source-supported opaque BD-BBL broth addition pending a verified product specification. No replacement constituent amount is calculated.",
    "source_amount": {
      "value": 0.1,
      "unit": "g",
      "material": "BD-BBL Trypticase soy broth as a whole"
    },
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, commercial broth row",
        "exact_source_quote": "Trypticase soy broth (BD-BBL) 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase soy broth\",\n                        \"compound_id\": 99,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ],
    "explanation": "The primary supports 0.1 g of the whole product, not this generic constituent amount. The five non-agar decomposition values total 30 g/L locally; even if a generic 30 g/L stock formula were independently verified, its values could not be inserted unchanged for this 0.1 g addition. Exact constituent proportions and product equivalence remain unavailable, so no scaling or substitute formulation is proposed."
  },
  {
    "input": "target",
    "field_path": "ingredients[6].concentration",
    "ingredient": "Glucose",
    "existing": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "decision": "correct",
    "source_stage": "Unverified commercial-product decomposition placed at receiving-medium root",
    "proposed": "Replace the unscaled generic constituent assertion with the exact source-supported opaque BD-BBL broth addition pending a verified product specification. No replacement constituent amount is calculated.",
    "source_amount": {
      "value": 0.1,
      "unit": "g",
      "material": "BD-BBL Trypticase soy broth as a whole"
    },
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, commercial broth row",
        "exact_source_quote": "Trypticase soy broth (BD-BBL) 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase soy broth\",\n                        \"compound_id\": 99,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ],
    "explanation": "The primary supports 0.1 g of the whole product, not this generic constituent amount. The five non-agar decomposition values total 30 g/L locally; even if a generic 30 g/L stock formula were independently verified, its values could not be inserted unchanged for this 0.1 g addition. Exact constituent proportions and product equivalence remain unavailable, so no scaling or substitute formulation is proposed."
  },
  {
    "input": "target",
    "field_path": "ingredients[7].concentration",
    "ingredient": "Sodium chloride",
    "existing": {
      "value": "5.0",
      "unit": "G_PER_L"
    },
    "decision": "correct",
    "source_stage": "Unverified commercial-product decomposition placed at receiving-medium root",
    "proposed": "Replace the unscaled generic constituent assertion with the exact source-supported opaque BD-BBL broth addition pending a verified product specification. No replacement constituent amount is calculated.",
    "source_amount": {
      "value": 0.1,
      "unit": "g",
      "material": "BD-BBL Trypticase soy broth as a whole"
    },
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, commercial broth row",
        "exact_source_quote": "Trypticase soy broth (BD-BBL) 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase soy broth\",\n                        \"compound_id\": 99,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ],
    "explanation": "The primary supports 0.1 g of the whole product, not this generic constituent amount. The five non-agar decomposition values total 30 g/L locally; even if a generic 30 g/L stock formula were independently verified, its values could not be inserted unchanged for this 0.1 g addition. Exact constituent proportions and product equivalence remain unavailable, so no scaling or substitute formulation is proposed."
  },
  {
    "input": "target",
    "field_path": "ingredients[8].concentration",
    "ingredient": "Dipotassium phosphate",
    "existing": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "decision": "correct",
    "source_stage": "Unverified commercial-product decomposition placed at receiving-medium root",
    "proposed": "Replace the unscaled generic constituent assertion with the exact source-supported opaque BD-BBL broth addition pending a verified product specification. No replacement constituent amount is calculated.",
    "source_amount": {
      "value": 0.1,
      "unit": "g",
      "material": "BD-BBL Trypticase soy broth as a whole"
    },
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, commercial broth row",
        "exact_source_quote": "Trypticase soy broth (BD-BBL) 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase soy broth\",\n                        \"compound_id\": 99,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ],
    "explanation": "The primary supports 0.1 g of the whole product, not this generic constituent amount. The five non-agar decomposition values total 30 g/L locally; even if a generic 30 g/L stock formula were independently verified, its values could not be inserted unchanged for this 0.1 g addition. Exact constituent proportions and product equivalence remain unavailable, so no scaling or substitute formulation is proposed."
  },
  {
    "input": "target",
    "field_path": "ingredients[9].concentration",
    "ingredient": "Agar",
    "existing": {
      "value": "15.0",
      "unit": "G_PER_L"
    },
    "decision": "correct",
    "source_stage": "Conditional solid-medium branch; solution B before separate autoclaving",
    "proposed": "Remove unconditional agar from the liquid-base ingredient assertion and represent the source’s optional solution-B condition separately. Retain the exact 15 g/L wording and addition location in solution B; whether the denominator is solution B or the final mixed medium is unresolved. Do not calculate a B-basis or final concentration.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129, conditional solid-medium sentence",
        "exact_source_quote": "For preparation of solid medium, add 15.0 g/L agar in solution B before autoclaving.",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ingredients[10].concentration",
    "ingredient": "Glucose",
    "existing": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "Solution B",
    "source_amount": {
      "value": 1,
      "unit": "g"
    },
    "basis": "JCM batch comprises separate 500 ml water portions; provider explicitly declares 1000 ml and g_l. Retain that declared basis rather than claim a measured final volume.",
    "proposed": "Retain the supported provider-basis value, add exact claim evidence and preserve the primary preparation stage.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution B table, exact named ingredient row",
        "exact_source_quote": "Glucose 1.0 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration",
    "ingredient": "(NH4)2SO4",
    "existing": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "Solution A",
    "source_amount": {
      "value": 2,
      "unit": "g"
    },
    "basis": "JCM batch comprises separate 500 ml water portions; provider explicitly declares 1000 ml and g_l. Retain that declared basis rather than claim a measured final volume.",
    "proposed": "Retain the supported provider-basis value, add exact claim evidence and preserve the primary preparation stage.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, exact named ingredient row",
        "exact_source_quote": "(NH 4 ) 2 SO 4 2.0 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 15.1355,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration",
    "ingredient": "KCl",
    "existing": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "Solution A",
    "source_amount": {
      "value": 0.1,
      "unit": "g"
    },
    "basis": "JCM batch comprises separate 500 ml water portions; provider explicitly declares 1000 ml and g_l. Retain that declared basis rather than claim a measured final volume.",
    "proposed": "Retain the supported provider-basis value, add exact claim evidence and preserve the primary preparation stage.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, exact named ingredient row",
        "exact_source_quote": "KCl 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.34138,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration",
    "ingredient": "K2HPO4",
    "existing": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "Solution A",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "basis": "JCM batch comprises separate 500 ml water portions; provider explicitly declares 1000 ml and g_l. Retain that declared basis rather than claim a measured final volume.",
    "proposed": "Retain the supported provider-basis value, add exact claim evidence and preserve the primary preparation stage.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, exact named ingredient row",
        "exact_source_quote": "K 2 HPO 4 0.5 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.87066,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "existing": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "Solution A",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "basis": "JCM batch comprises separate 500 ml water portions; provider explicitly declares 1000 ml and g_l. Retain that declared basis rather than claim a measured final volume.",
    "proposed": "Retain the supported provider-basis value, add exact claim evidence and preserve the primary preparation stage.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, exact named ingredient row",
        "exact_source_quote": "MgSO 4 ·7H 2 O 0.5 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration",
    "ingredient": "Pancreatic digest of casein",
    "existing": {
      "value": "17.0",
      "unit": "G_PER_L"
    },
    "decision": "correct",
    "source_stage": "Unverified commercial-product decomposition placed at receiving-medium root",
    "proposed": "Replace the unscaled generic constituent assertion with the exact source-supported opaque BD-BBL broth addition pending a verified product specification. No replacement constituent amount is calculated.",
    "source_amount": {
      "value": 0.1,
      "unit": "g",
      "material": "BD-BBL Trypticase soy broth as a whole"
    },
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, commercial broth row",
        "exact_source_quote": "Trypticase soy broth (BD-BBL) 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase soy broth\",\n                        \"compound_id\": 99,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ],
    "explanation": "The primary supports 0.1 g of the whole product, not this generic constituent amount. The five non-agar decomposition values total 30 g/L locally; even if a generic 30 g/L stock formula were independently verified, its values could not be inserted unchanged for this 0.1 g addition. Exact constituent proportions and product equivalence remain unavailable, so no scaling or substitute formulation is proposed."
  },
  {
    "input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration",
    "ingredient": "Peptic digest of soybean meal",
    "existing": {
      "value": "3.0",
      "unit": "G_PER_L"
    },
    "decision": "correct",
    "source_stage": "Unverified commercial-product decomposition placed at receiving-medium root",
    "proposed": "Replace the unscaled generic constituent assertion with the exact source-supported opaque BD-BBL broth addition pending a verified product specification. No replacement constituent amount is calculated.",
    "source_amount": {
      "value": 0.1,
      "unit": "g",
      "material": "BD-BBL Trypticase soy broth as a whole"
    },
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, commercial broth row",
        "exact_source_quote": "Trypticase soy broth (BD-BBL) 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase soy broth\",\n                        \"compound_id\": 99,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ],
    "explanation": "The primary supports 0.1 g of the whole product, not this generic constituent amount. The five non-agar decomposition values total 30 g/L locally; even if a generic 30 g/L stock formula were independently verified, its values could not be inserted unchanged for this 0.1 g addition. Exact constituent proportions and product equivalence remain unavailable, so no scaling or substitute formulation is proposed."
  },
  {
    "input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration",
    "ingredient": "Glucose",
    "existing": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "decision": "correct",
    "source_stage": "Unverified commercial-product decomposition placed at receiving-medium root",
    "proposed": "Replace the unscaled generic constituent assertion with the exact source-supported opaque BD-BBL broth addition pending a verified product specification. No replacement constituent amount is calculated.",
    "source_amount": {
      "value": 0.1,
      "unit": "g",
      "material": "BD-BBL Trypticase soy broth as a whole"
    },
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, commercial broth row",
        "exact_source_quote": "Trypticase soy broth (BD-BBL) 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase soy broth\",\n                        \"compound_id\": 99,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ],
    "explanation": "The primary supports 0.1 g of the whole product, not this generic constituent amount. The five non-agar decomposition values total 30 g/L locally; even if a generic 30 g/L stock formula were independently verified, its values could not be inserted unchanged for this 0.1 g addition. Exact constituent proportions and product equivalence remain unavailable, so no scaling or substitute formulation is proposed."
  },
  {
    "input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration",
    "ingredient": "Sodium chloride",
    "existing": {
      "value": "5.0",
      "unit": "G_PER_L"
    },
    "decision": "correct",
    "source_stage": "Unverified commercial-product decomposition placed at receiving-medium root",
    "proposed": "Replace the unscaled generic constituent assertion with the exact source-supported opaque BD-BBL broth addition pending a verified product specification. No replacement constituent amount is calculated.",
    "source_amount": {
      "value": 0.1,
      "unit": "g",
      "material": "BD-BBL Trypticase soy broth as a whole"
    },
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, commercial broth row",
        "exact_source_quote": "Trypticase soy broth (BD-BBL) 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase soy broth\",\n                        \"compound_id\": 99,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ],
    "explanation": "The primary supports 0.1 g of the whole product, not this generic constituent amount. The five non-agar decomposition values total 30 g/L locally; even if a generic 30 g/L stock formula were independently verified, its values could not be inserted unchanged for this 0.1 g addition. Exact constituent proportions and product equivalence remain unavailable, so no scaling or substitute formulation is proposed."
  },
  {
    "input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration",
    "ingredient": "Dipotassium phosphate",
    "existing": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "decision": "correct",
    "source_stage": "Unverified commercial-product decomposition placed at receiving-medium root",
    "proposed": "Replace the unscaled generic constituent assertion with the exact source-supported opaque BD-BBL broth addition pending a verified product specification. No replacement constituent amount is calculated.",
    "source_amount": {
      "value": 0.1,
      "unit": "g",
      "material": "BD-BBL Trypticase soy broth as a whole"
    },
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, commercial broth row",
        "exact_source_quote": "Trypticase soy broth (BD-BBL) 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase soy broth\",\n                        \"compound_id\": 99,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ],
    "explanation": "The primary supports 0.1 g of the whole product, not this generic constituent amount. The five non-agar decomposition values total 30 g/L locally; even if a generic 30 g/L stock formula were independently verified, its values could not be inserted unchanged for this 0.1 g addition. Exact constituent proportions and product equivalence remain unavailable, so no scaling or substitute formulation is proposed."
  },
  {
    "input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration",
    "ingredient": "Agar",
    "existing": {
      "value": "15.0",
      "unit": "G_PER_L"
    },
    "decision": "correct",
    "source_stage": "Conditional solid-medium branch; solution B before separate autoclaving",
    "proposed": "Remove unconditional agar from the liquid-base ingredient assertion and represent the source’s optional solution-B condition separately. Retain the exact 15 g/L wording and addition location in solution B; whether the denominator is solution B or the final mixed medium is unresolved. Do not calculate a B-basis or final concentration.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129, conditional solid-medium sentence",
        "exact_source_quote": "For preparation of solid medium, add 15.0 g/L agar in solution B before autoclaving.",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration",
    "ingredient": "Glucose",
    "existing": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "decision": "evidence_only",
    "source_stage": "Solution B",
    "source_amount": {
      "value": 1,
      "unit": "g"
    },
    "basis": "JCM batch comprises separate 500 ml water portions; provider explicitly declares 1000 ml and g_l. Retain that declared basis rather than claim a measured final volume.",
    "proposed": "Retain the supported provider-basis value, add exact claim evidence and preserve the primary preparation stage.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution B table, exact named ingredient row",
        "exact_source_quote": "Glucose 1.0 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "target and owner",
    "field_path": "ingredients (missing intact source product)",
    "decision": "add",
    "source_stage": "Solution A",
    "source_amount": {
      "value": 0.1,
      "unit": "g",
      "material": "Trypticase soy broth (BD-BBL)"
    },
    "proposed": "Represent the exact opaque commercial addition and source identity; avoid duplicate counting with the unverified constituent expansion. Provider reports 0.1 g/L on its declared 1000 ml basis.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "Solution A commercial broth row",
        "exact_source_quote": "Trypticase soy broth (BD-BBL) 0.1 g",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase soy broth\",\n                        \"compound_id\": 99,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "target and owner",
    "field_path": "solutions / preparation_steps (missing A solvent)",
    "decision": "add",
    "source_stage": "Solution A before separate autoclaving",
    "source_amount": {
      "value": 500,
      "unit": "ml"
    },
    "proposed": "Preserve the two separate solvent aliquots and their stages. Provider’s aggregate 1000 ml row does not replace their individual preparation roles.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution A table, distilled-water row",
        "exact_source_quote": "Distilled water 500.0 ml",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "target and owner",
    "field_path": "solutions / preparation_steps (missing B solvent)",
    "decision": "add",
    "source_stage": "Solution B before separate autoclaving",
    "source_amount": {
      "value": 500,
      "unit": "ml"
    },
    "proposed": "Preserve the two separate solvent aliquots and their stages. Provider’s aggregate 1000 ml row does not replace their individual preparation roles.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129 Solution B table, distilled-water row",
        "exact_source_quote": "Distilled water 500.0 ml",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "mediadiveJ129api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J129",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ph_value; preparation_steps[0]",
    "existing": 3.0,
    "decision": "evidence_only",
    "source_stage": "Solution A before sterilization and combination",
    "proposed": "Retain target pH 3.0 with the explicitly supported solution-A context and claim evidence. Do not relabel it as measured final pH.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129, sentence between Solution A and Solution B tables",
        "exact_source_quote": "Adjust pH to 3.0.",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "field_path": "ph_value; preparation_steps[0]",
    "existing": 3.0,
    "decision": "evidence_only",
    "source_stage": "Solution A before sterilization and combination",
    "proposed": "Retain target pH 3.0 with the explicitly supported solution-A context and claim evidence. Do not relabel it as measured final pH.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129, sentence between Solution A and Solution B tables",
        "exact_source_quote": "Adjust pH to 3.0.",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      }
    ]
  },
  {
    "input": "target and owner",
    "field_path": "preparation_steps (missing qualified sterilization condition)",
    "decision": "add",
    "source_amount": {
      "value": 121,
      "unit": "C"
    },
    "source_stage": "Autoclave A and B separately; general JCM qualifier applies unless otherwise stated",
    "proposed": "Retain the primary’s separate sterilization and aseptic combination, with its qualified default condition; do not combine the stocks before autoclaving.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM page global qualifier before heading",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129, preparation after Solution B",
        "exact_source_quote": "Autoclave Solutions A and B separately, and mix aseptically.",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      }
    ]
  },
  {
    "input": "target and owner",
    "field_path": "preparation_steps (missing qualified sterilization condition)",
    "decision": "add",
    "source_amount": {
      "value": 15,
      "unit": "min"
    },
    "source_stage": "Autoclave A and B separately; general JCM qualifier applies unless otherwise stated",
    "proposed": "Retain the primary’s separate sterilization and aseptic combination, with its qualified default condition; do not combine the stocks before autoclaving.",
    "source_snippets": [
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM page global qualifier before heading",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      },
      {
        "source_key": "jcm129",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129",
        "source_locator": "JCM 129, preparation after Solution B",
        "exact_source_quote": "Autoclave Solutions A and B separately, and mix aseptically.",
        "snapshot_sha256": "78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d",
        "parsed_text_sha256": "a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27"
      }
    ]
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: supported. Targets: CultureMech:002462.

9 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 11/11 primary and 5/11 secondary instances; all asserted secondary keys have exact pinned MIM rows. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 11: primary 100.00%; secondary 45.45%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Actual source forms versus valid ingredient identifiers

grounding: concern. Targets: CultureMech:002462.

The direct source salts and glucose match the asserted primary forms; no hydrate conversion is needed. MICRO tryptone and FOODON hydrolyzed vegetable protein are valid broad ingredient identities, but their existence does not establish the exact BD-BBL product decomposition, Bacto-brand synonym equivalence or supplier interchangeability. The commercial constituent CHEBI labels identify chemicals, not their amounts or presence in this specific product.

### Separate source stages, water and physical-state branch

completeness: concern. Targets: CultureMech:002462.

The sole local pH-adjustment step omits Solution A/B separation, each 500 ml water aliquot, separate autoclaving and aseptic mixing. The source’s optional solid branch puts agar into B before autoclaving; the local record instead includes it unconditionally despite LIQUID. Source-stage information cannot be recovered from the flattened provider table alone.

### Composition, physical state and organism evidence

scope: concern. Targets: CultureMech:002462.

COMPLEX is compatible with a medium containing commercial broth. UNDEFINED is a broad permitted description; after source reconciliation, SEMI_DEFINED more precisely describes defined salts/glucose with a small complex supplement. LIQUID applies to the base recipe but conflicts with the current unconditional agar. Bacterial category and generic cultivation application do not establish particular Acidiphilium growth, optimal pH or a taxonomic identifier.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:002462.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

## Findings

### f1: Generic commercial constituents replace the small source broth addition

blocker / open / confirmed; issue key: culturemech.002462.unscaled-commercial-expansion.

Both target and owner replace the primary’s 0.1 g BD-BBL Trypticase soy broth with 17 g/L casein digest, 3 g/L soybean digest, 2.5 g/L glucose, 5 g/L NaCl, 2.5 g/L dipotassium phosphate and 15 g/L agar. The first five sum to 30 g/L; no product-specific scaling evidence supports them. Agar is not part of the liquid-base broth addition and the exact source’s solid branch is conditional within Solution B. The separate 1 g glucose in Solution B must remain distinct.

### f2: Two separately prepared source solutions are collapsed

major / open / confirmed; issue key: culturemech.002462.preparation-stage-omission.

Both local layers retain only Adjust pH to 3.0 and omit the source’s A/B grouping, two 500 ml water aliquots, separate autoclaving and aseptic combination. The JCM default is explicitly qualified and must be attached to the two stated autoclave stages. Missing these boundaries materially changes the preparation description.

### f3: Multi-supplier product claims lack exact specification support

major / open / confirmed; issue key: culturemech.002462.product-provenance-unresolved.

The local notes assert researched product specifications while citing a generic encyclopedia URL and mixing BD, Sigma and Neogen catalogs under TSB/TSA. The primary specifically names BD-BBL broth. Exact BD and Sigma attempts did not yield formula bytes, and the prior BD manual attempt failed. Brand-specific synonyms and supplier interchangeability cannot be authenticated from valid ingredient ontology labels.

### f4: Source-supported direct quantities have no claim-level evidence

minor / open / confirmed; issue key: culturemech.002462.claim-evidence-gap.

The four direct mineral amounts, separate glucose and target pH are supported on the recorded provider/source basis but have no attached evidence in either local layer. They remain evidence_only rather than verified. Commercial-product and physical-state failures are separate from this narrower provenance gap.

## Recommended Actions And Acceptance Checks

### a1

Restore the intact source-supported BD-BBL broth addition and conditional agar scope in the maintained owner. Only decompose an exact verified product with explicit dose and basis; preserve the independent Solution-B glucose and regenerate the target after owner review.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent the exact source stages and solvent portions in the normalized owner, with conditional solid-medium preparation separated. Preserve pH as the target of the source A stage; do not invent titrant identity or dose.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain the failed-attempt provenance and resolve the exact BD-BBL product/catalog before preserving product-specific constituents or supplier equivalence. Replace broad bibliographic claims with narrowly verified source support; leave unresolved product correspondence explicit.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach exact source snippets and stage/volume explanations to the supported direct claims without importing unsupported constituent evidence. Preserve existing append-only history and use normal owner/merge verification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch018/172/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch018/172/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml:1:id: CultureMech:002462<br>./data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml:1:id: CultureMech:002462<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch018/source-preflight-bound/172/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 14 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129; Complete JCM 129 heading, Solution A/B tables, preparation and conditional solid-medium clause | supports | Exact JCM identity and both stages inspected. The primary specifies BD-BBL broth, separate water aliquots and optional agar within solution B; it does not give that commercial broth’s constituent formula. |
| provider | https://mediadive.dsmz.de/rest/medium/J129; $.data.medium; $.data.solutions[0], all seven recipe rows and preparation | supports | Provider declares a 1000 ml main basis and one opaque 0.1 g BD-BBL broth addition. It flattens the two source stages and preserves only the pH instruction; no chronology between representations is established. |
| bd211825PriorAttempt-attempt | https://www.bd.com/en-us/products-and-solutions/products/product-page.211825; Preserved exact public retrieval result | context_only | The exact asserted BD 211825 product attempt returned HTTP 403; the preserved prior metadata provides no product formulation bytes. BD-BBL Trypticase soy broth identity, catalog equivalence and constituent proportions cannot be verified from that failed request. |
| bdManualPriorAttempt-attempt | https://static.bd.com/assets/product/Documents/Integrated%20Diagnostic%20Solutions%20%28IDS%29/DS_CM_Difco-and-BBL-culture-media-manual_UG_EN.pdf; Preserved exact public retrieval result | context_only | The preserved BD manual attempt returned HTTP 404. No manual content was inspected; it cannot corroborate a product or mixture recipe. |
| sigma22092-attempt | https://www.sigmaaldrich.com/deepweb/assets/sigmaaldrich/product/documents/288/904/22092dat.pdf; Preserved exact public retrieval result | context_only | The exact asserted Sigma 22092 specification attempt timed out without captured formula bytes. Its equivalence to the primary’s BD-BBL product and the stated multi-supplier constituent formula remain unresolved; no Sigma formula substitutes for BD-BBL. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch018/172/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| foodon03315720 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315720; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | FOODON:03315720 resolves to vegetable protein, hydrolyzed. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| micro0000182 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | MICRO:0000182 resolves to tryptone. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml; data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml", "events": 6, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current _parse_api_composition skips water and reads the main provider recipe; _normalize_unit distinguishes no original-batch basis. Current formulation-aware merge code preserves compatible assertions, not scientific validity. Neither was replayed to assign historical causation for the commercial expansion. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current _parse_api_composition skips water and reads the main provider recipe; _normalize_unit distinguishes no original-batch basis. Current formulation-aware merge code preserves compatible assertions, not scientific validity. Neither was replayed to assign historical causation for the commercial expansion. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact asserted BD 211825 product attempt returned HTTP 403; the preserved prior metadata provides no product formulation bytes. BD-BBL Trypticase soy broth identity, catalog equivalence and constituent proportions cannot be verified from that failed request.
- The preserved BD manual attempt returned HTTP 404. No manual content was inspected; it cannot corroborate a product or mixture recipe.
- The exact asserted Sigma 22092 specification attempt timed out without captured formula bytes. Its equivalence to the primary’s BD-BBL product and the stated multi-supplier constituent formula remain unresolved; no Sigma formula substitutes for BD-BBL.
- The generic Wikipedia source and multi-supplier catalogs are not treated as inspected product specifications. No commercial constituent proportions, titrant, final measured volume, strain growth or oxygen requirement were inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T112127Z-culturemech-002462-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidiphilium_medium (CultureMech:002462)'
started_at: '2026-10-21T11:17:43Z'
finished_at: '2026-10-21T11:21:27Z'
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
summary: JCM 129 is an Acidiphilium formulation with separately prepared solutions
  A and B and a small BD-BBL Trypticase soy broth addition. Both local layers replace
  that commercial addition with unscaled generic TSB/TSA constituents, including unconditional
  agar, and omit the two preparation stages. Exact supplier formulation correspondence
  remains unavailable, so the review is partial.
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
  - path: data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml
    sha256: 8b0178de7d3b918cf0766e6a1edb3deb1be98f2728232c62419d093fe59cfc9c
    role: target
  - path: data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
    sha256: 6ee70dd5b58cd8c3b4bc0af2b404b14be3f1a43b676cc19f702d84d26958687a
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
  selection: Task review 172; batch 018 item 2 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding seventeen task batches
    contain 170 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 172 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002462
targets:
- target_id: CultureMech:002462
  path: data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml
  label: acidiphilium_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch018/172/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch018/172/strict.tsv"
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002462
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
  - CultureMech:002462
- check_id: bd211825PriorAttempt-source-access
  name: 'Exact source content access: bd211825PriorAttempt'
  required: true
  status: unavailable
  summary: The exact asserted BD 211825 product attempt returned HTTP 403; the preserved
    prior metadata provides no product formulation bytes. BD-BBL Trypticase soy broth
    identity, catalog equivalence and constituent proportions cannot be verified from
    that failed request.
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - bd211825PriorAttempt-attempt
- check_id: bdManualPriorAttempt-source-access
  name: 'Exact source content access: bdManualPriorAttempt'
  required: false
  status: unavailable
  summary: The preserved BD manual attempt returned HTTP 404. No manual content was
    inspected; it cannot corroborate a product or mixture recipe.
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - bdManualPriorAttempt-attempt
- check_id: sigma22092-source-access
  name: 'Exact source content access: sigma22092'
  required: true
  status: unavailable
  summary: The exact asserted Sigma 22092 specification attempt timed out without
    captured formula bytes. Its equivalence to the primary’s BD-BBL product and the
    stated multi-supplier constituent formula remain unresolved; no Sigma formula
    substitutes for BD-BBL.
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - sigma22092-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:21:25Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:21:25Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:18:29.475100Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch018/172/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T11:18:33.922087Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch018/172/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:18:37.447670Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:18:39.643178Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:21:25Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml:1:id:
    CultureMech:002462

    ./data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml:1:id: CultureMech:002462

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch018/source-preflight-bound/172/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:21:25Z'
  support: supports
  summary: 14 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: a1bafefc4ff6a1d356018a99af94eabf24e44e1ca19d493c22dae5a3810bb6cb
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129
  locator: Complete JCM 129 heading, Solution A/B tables, preparation and conditional
    solid-medium clause
  accessed_at: '2026-10-21T11:02:39.370029Z'
  support: supports
  summary: Exact JCM identity and both stages inspected. The primary specifies BD-BBL
    broth, separate water aliquots and optional agar within solution B; it does not
    give that commercial broth’s constituent formula.
  snapshot_sha256: 78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J129
  locator: $.data.medium; $.data.solutions[0], all seven recipe rows and preparation
  accessed_at: '2026-10-21T11:02:37.423124Z'
  support: supports
  summary: Provider declares a 1000 ml main basis and one opaque 0.1 g BD-BBL broth
    addition. It flattens the two source stages and preserves only the pH instruction;
    no chronology between representations is established.
  snapshot_sha256: 84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f
- evidence_id: bd211825PriorAttempt-attempt
  kind: database
  reference: https://www.bd.com/en-us/products-and-solutions/products/product-page.211825
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T06:36:35.780635Z'
  support: context_only
  summary: The exact asserted BD 211825 product attempt returned HTTP 403; the preserved
    prior metadata provides no product formulation bytes. BD-BBL Trypticase soy broth
    identity, catalog equivalence and constituent proportions cannot be verified from
    that failed request.
- evidence_id: bdManualPriorAttempt-attempt
  kind: database
  reference: https://static.bd.com/assets/product/Documents/Integrated%20Diagnostic%20Solutions%20%28IDS%29/DS_CM_Difco-and-BBL-culture-media-manual_UG_EN.pdf
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T06:36:35.781064Z'
  support: context_only
  summary: The preserved BD manual attempt returned HTTP 404. No manual content was
    inspected; it cannot corroborate a product or mixture recipe.
- evidence_id: sigma22092-attempt
  kind: database
  reference: https://www.sigmaaldrich.com/deepweb/assets/sigmaaldrich/product/documents/288/904/22092dat.pdf
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T11:02:39.662475Z'
  support: context_only
  summary: The exact asserted Sigma 22092 specification attempt timed out without
    captured formula bytes. Its equivalence to the primary’s BD-BBL product and the
    stated multi-supplier constituent formula remain unresolved; no Sigma formula
    substitutes for BD-BBL.
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch018/172/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:21:25Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 621da6f371170845a4088671e34c7a5bfb2ae49332ad2429e854c3eb842aa7e6
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
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
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
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
- evidence_id: foodon03315720
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315720
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:37:22.786983Z'
  support: supports
  summary: FOODON:03315720 resolves to vegetable protein, hydrolyzed. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: aa063e8b88177611aba640828e84d3982b1b3b1c65b11647d89c9efbf6274c25
- evidence_id: micro0000182
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:37:21.973857Z'
  support: supports
  summary: MICRO:0000182 resolves to tryptone. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 01875997c482a49e4d41eb35c6c697e190afd236a8527625e94b6f96df3872b0
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T11:21:25Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label":
    "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml; data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:21:25Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:21:25Z'
  support: context_only
  summary: Current _parse_api_composition skips water and reads the main provider
    recipe; _normalize_unit distinguishes no original-batch basis. Current formulation-aware
    merge code preserves compatible assertions, not scientific validity. Neither was
    replayed to assign historical causation for the commercial expansion.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:21:25Z'
  support: context_only
  summary: Current _parse_api_composition skips water and reads the main provider
    recipe; _normalize_unit distinguishes no original-batch basis. Current formulation-aware
    merge code preserves compatible assertions, not scientific validity. Neither was
    replayed to assign historical causation for the commercial expansion.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact source accession and commercial-product boundary
  outcome: concern
  summary: CultureMech:002462 resolves to JCM 129 and provider J129, with one exact
    normalized owner. Interchangeability between the primary’s BD-BBL Trypticase soy
    broth and the local multi-supplier TSB/TSA label or asserted catalog numbers is
    not established. The generic encyclopedia URL is a secondary lead, not verified
    product-specific evidence. The medium title and application do not establish a
    species or strain growth claim.
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - bd211825PriorAttempt-attempt
  - sigma22092-attempt
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 29 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"input\": \"target\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"ingredient\": \"(NH4)2SO4\",\n    \"existing\": {\n      \"value\": \"\
    2\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"Solution A\",\n    \"source_amount\": {\n      \"value\"\
    : 2,\n      \"unit\": \"g\"\n    },\n    \"basis\": \"JCM batch comprises separate\
    \ 500 ml water portions; provider explicitly declares 1000 ml and g_l. Retain\
    \ that declared basis rather than claim a measured final volume.\",\n    \"proposed\"\
    : \"Retain the supported provider-basis value, add exact claim evidence and preserve\
    \ the primary preparation stage.\",\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, exact named ingredient\
    \ row\",\n        \"exact_source_quote\": \"(NH 4 ) 2 SO 4 2.0 g\",\n        \"\
    snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 2,\\n                        \\\
    \"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2,\\n          \
    \              \\\"mmol_l\\\": 15.1355,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ingredients[1].concentration\",\n    \"ingredient\": \"KCl\",\n    \"existing\"\
    : {\n      \"value\": \"0.1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Solution A\",\n    \"source_amount\"\
    : {\n      \"value\": 0.1,\n      \"unit\": \"g\"\n    },\n    \"basis\": \"JCM\
    \ batch comprises separate 500 ml water portions; provider explicitly declares\
    \ 1000 ml and g_l. Retain that declared basis rather than claim a measured final\
    \ volume.\",\n    \"proposed\": \"Retain the supported provider-basis value, add\
    \ exact claim evidence and preserve the primary preparation stage.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm129\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\",\n  \
    \      \"source_locator\": \"JCM 129 Solution A table, exact named ingredient\
    \ row\",\n        \"exact_source_quote\": \"KCl 0.1 g\",\n        \"snapshot_sha256\"\
    : \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\",\n    \
    \    \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                \
    \        \\\"mmol_l\\\": 1.34138,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ingredients[2].concentration\",\n    \"ingredient\": \"K2HPO4\",\n    \"existing\"\
    : {\n      \"value\": \"0.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Solution A\",\n    \"source_amount\"\
    : {\n      \"value\": 0.5,\n      \"unit\": \"g\"\n    },\n    \"basis\": \"JCM\
    \ batch comprises separate 500 ml water portions; provider explicitly declares\
    \ 1000 ml and g_l. Retain that declared basis rather than claim a measured final\
    \ volume.\",\n    \"proposed\": \"Retain the supported provider-basis value, add\
    \ exact claim evidence and preserve the primary preparation stage.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm129\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\",\n  \
    \      \"source_locator\": \"JCM 129 Solution A table, exact named ingredient\
    \ row\",\n        \"exact_source_quote\": \"K 2 HPO 4 0.5 g\",\n        \"snapshot_sha256\"\
    : \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\",\n    \
    \    \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n                \
    \        \\\"mmol_l\\\": 2.87066,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ingredients[3].concentration\",\n    \"ingredient\": \"MgSO4 x 7 H2O\",\n    \"\
    existing\": {\n      \"value\": \"0.5\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"decision\": \"evidence_only\",\n    \"source_stage\": \"Solution A\",\n\
    \    \"source_amount\": {\n      \"value\": 0.5,\n      \"unit\": \"g\"\n    },\n\
    \    \"basis\": \"JCM batch comprises separate 500 ml water portions; provider\
    \ explicitly declares 1000 ml and g_l. Retain that declared basis rather than\
    \ claim a measured final volume.\",\n    \"proposed\": \"Retain the supported\
    \ provider-basis value, add exact claim evidence and preserve the primary preparation\
    \ stage.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm129\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, exact named ingredient\
    \ row\",\n        \"exact_source_quote\": \"MgSO 4 ·7H 2 O 0.5 g\",\n        \"\
    snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n  \
    \                      \\\"mmol_l\\\": 2.02859,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ingredients[4].concentration\",\n    \"ingredient\": \"Pancreatic digest of casein\"\
    ,\n    \"existing\": {\n      \"value\": \"17.0\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"decision\": \"correct\",\n    \"source_stage\": \"Unverified commercial-product\
    \ decomposition placed at receiving-medium root\",\n    \"proposed\": \"Replace\
    \ the unscaled generic constituent assertion with the exact source-supported opaque\
    \ BD-BBL broth addition pending a verified product specification. No replacement\
    \ constituent amount is calculated.\",\n    \"source_amount\": {\n      \"value\"\
    : 0.1,\n      \"unit\": \"g\",\n      \"material\": \"BD-BBL Trypticase soy broth\
    \ as a whole\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, commercial broth row\"\
    ,\n        \"exact_source_quote\": \"Trypticase soy broth (BD-BBL) 0.1 g\",\n\
    \        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Trypticase soy broth\\\",\\n                        \\\"compound_id\\\
    \": 99,\\n                        \\\"attribute\\\": \\\"BD-BBL\\\",\\n      \
    \                  \\\"amount\\\": 0.1,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\n     \
    \ }\n    ],\n    \"explanation\": \"The primary supports 0.1 g of the whole product,\
    \ not this generic constituent amount. The five non-agar decomposition values\
    \ total 30 g/L locally; even if a generic 30 g/L stock formula were independently\
    \ verified, its values could not be inserted unchanged for this 0.1 g addition.\
    \ Exact constituent proportions and product equivalence remain unavailable, so\
    \ no scaling or substitute formulation is proposed.\"\n  },\n  {\n    \"input\"\
    : \"target\",\n    \"field_path\": \"ingredients[5].concentration\",\n    \"ingredient\"\
    : \"Peptic digest of soybean meal\",\n    \"existing\": {\n      \"value\": \"\
    3.0\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"correct\",\n\
    \    \"source_stage\": \"Unverified commercial-product decomposition placed at\
    \ receiving-medium root\",\n    \"proposed\": \"Replace the unscaled generic constituent\
    \ assertion with the exact source-supported opaque BD-BBL broth addition pending\
    \ a verified product specification. No replacement constituent amount is calculated.\"\
    ,\n    \"source_amount\": {\n      \"value\": 0.1,\n      \"unit\": \"g\",\n \
    \     \"material\": \"BD-BBL Trypticase soy broth as a whole\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm129\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\",\n  \
    \      \"source_locator\": \"JCM 129 Solution A table, commercial broth row\"\
    ,\n        \"exact_source_quote\": \"Trypticase soy broth (BD-BBL) 0.1 g\",\n\
    \        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Trypticase soy broth\\\",\\n                        \\\"compound_id\\\
    \": 99,\\n                        \\\"attribute\\\": \\\"BD-BBL\\\",\\n      \
    \                  \\\"amount\\\": 0.1,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\n     \
    \ }\n    ],\n    \"explanation\": \"The primary supports 0.1 g of the whole product,\
    \ not this generic constituent amount. The five non-agar decomposition values\
    \ total 30 g/L locally; even if a generic 30 g/L stock formula were independently\
    \ verified, its values could not be inserted unchanged for this 0.1 g addition.\
    \ Exact constituent proportions and product equivalence remain unavailable, so\
    \ no scaling or substitute formulation is proposed.\"\n  },\n  {\n    \"input\"\
    : \"target\",\n    \"field_path\": \"ingredients[6].concentration\",\n    \"ingredient\"\
    : \"Glucose\",\n    \"existing\": {\n      \"value\": \"2.5\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"correct\",\n    \"source_stage\": \"\
    Unverified commercial-product decomposition placed at receiving-medium root\"\
    ,\n    \"proposed\": \"Replace the unscaled generic constituent assertion with\
    \ the exact source-supported opaque BD-BBL broth addition pending a verified product\
    \ specification. No replacement constituent amount is calculated.\",\n    \"source_amount\"\
    : {\n      \"value\": 0.1,\n      \"unit\": \"g\",\n      \"material\": \"BD-BBL\
    \ Trypticase soy broth as a whole\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, commercial broth row\"\
    ,\n        \"exact_source_quote\": \"Trypticase soy broth (BD-BBL) 0.1 g\",\n\
    \        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Trypticase soy broth\\\",\\n                        \\\"compound_id\\\
    \": 99,\\n                        \\\"attribute\\\": \\\"BD-BBL\\\",\\n      \
    \                  \\\"amount\\\": 0.1,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\n     \
    \ }\n    ],\n    \"explanation\": \"The primary supports 0.1 g of the whole product,\
    \ not this generic constituent amount. The five non-agar decomposition values\
    \ total 30 g/L locally; even if a generic 30 g/L stock formula were independently\
    \ verified, its values could not be inserted unchanged for this 0.1 g addition.\
    \ Exact constituent proportions and product equivalence remain unavailable, so\
    \ no scaling or substitute formulation is proposed.\"\n  },\n  {\n    \"input\"\
    : \"target\",\n    \"field_path\": \"ingredients[7].concentration\",\n    \"ingredient\"\
    : \"Sodium chloride\",\n    \"existing\": {\n      \"value\": \"5.0\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Unverified commercial-product decomposition placed at receiving-medium root\"\
    ,\n    \"proposed\": \"Replace the unscaled generic constituent assertion with\
    \ the exact source-supported opaque BD-BBL broth addition pending a verified product\
    \ specification. No replacement constituent amount is calculated.\",\n    \"source_amount\"\
    : {\n      \"value\": 0.1,\n      \"unit\": \"g\",\n      \"material\": \"BD-BBL\
    \ Trypticase soy broth as a whole\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, commercial broth row\"\
    ,\n        \"exact_source_quote\": \"Trypticase soy broth (BD-BBL) 0.1 g\",\n\
    \        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Trypticase soy broth\\\",\\n                        \\\"compound_id\\\
    \": 99,\\n                        \\\"attribute\\\": \\\"BD-BBL\\\",\\n      \
    \                  \\\"amount\\\": 0.1,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\n     \
    \ }\n    ],\n    \"explanation\": \"The primary supports 0.1 g of the whole product,\
    \ not this generic constituent amount. The five non-agar decomposition values\
    \ total 30 g/L locally; even if a generic 30 g/L stock formula were independently\
    \ verified, its values could not be inserted unchanged for this 0.1 g addition.\
    \ Exact constituent proportions and product equivalence remain unavailable, so\
    \ no scaling or substitute formulation is proposed.\"\n  },\n  {\n    \"input\"\
    : \"target\",\n    \"field_path\": \"ingredients[8].concentration\",\n    \"ingredient\"\
    : \"Dipotassium phosphate\",\n    \"existing\": {\n      \"value\": \"2.5\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Unverified commercial-product decomposition placed at receiving-medium root\"\
    ,\n    \"proposed\": \"Replace the unscaled generic constituent assertion with\
    \ the exact source-supported opaque BD-BBL broth addition pending a verified product\
    \ specification. No replacement constituent amount is calculated.\",\n    \"source_amount\"\
    : {\n      \"value\": 0.1,\n      \"unit\": \"g\",\n      \"material\": \"BD-BBL\
    \ Trypticase soy broth as a whole\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, commercial broth row\"\
    ,\n        \"exact_source_quote\": \"Trypticase soy broth (BD-BBL) 0.1 g\",\n\
    \        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Trypticase soy broth\\\",\\n                        \\\"compound_id\\\
    \": 99,\\n                        \\\"attribute\\\": \\\"BD-BBL\\\",\\n      \
    \                  \\\"amount\\\": 0.1,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\n     \
    \ }\n    ],\n    \"explanation\": \"The primary supports 0.1 g of the whole product,\
    \ not this generic constituent amount. The five non-agar decomposition values\
    \ total 30 g/L locally; even if a generic 30 g/L stock formula were independently\
    \ verified, its values could not be inserted unchanged for this 0.1 g addition.\
    \ Exact constituent proportions and product equivalence remain unavailable, so\
    \ no scaling or substitute formulation is proposed.\"\n  },\n  {\n    \"input\"\
    : \"target\",\n    \"field_path\": \"ingredients[9].concentration\",\n    \"ingredient\"\
    : \"Agar\",\n    \"existing\": {\n      \"value\": \"15.0\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"decision\": \"correct\",\n    \"source_stage\": \"\
    Conditional solid-medium branch; solution B before separate autoclaving\",\n \
    \   \"proposed\": \"Remove unconditional agar from the liquid-base ingredient\
    \ assertion and represent the source’s optional solution-B condition separately.\
    \ Retain the exact 15 g/L wording and addition location in solution B; whether\
    \ the denominator is solution B or the final mixed medium is unresolved. Do not\
    \ calculate a B-basis or final concentration.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129, conditional solid-medium sentence\"\
    ,\n        \"exact_source_quote\": \"For preparation of solid medium, add 15.0\
    \ g/L agar in solution B before autoclaving.\",\n        \"snapshot_sha256\":\
    \ \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\",\n    \
    \    \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ingredients[10].concentration\",\n    \"ingredient\": \"Glucose\",\n    \"existing\"\
    : {\n      \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Solution B\",\n    \"source_amount\"\
    : {\n      \"value\": 1,\n      \"unit\": \"g\"\n    },\n    \"basis\": \"JCM\
    \ batch comprises separate 500 ml water portions; provider explicitly declares\
    \ 1000 ml and g_l. Retain that declared basis rather than claim a measured final\
    \ volume.\",\n    \"proposed\": \"Retain the supported provider-basis value, add\
    \ exact claim evidence and preserve the primary preparation stage.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm129\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\",\n  \
    \      \"source_locator\": \"JCM 129 Solution B table, exact named ingredient\
    \ row\",\n        \"exact_source_quote\": \"Glucose 1.0 g\",\n        \"snapshot_sha256\"\
    : \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\",\n    \
    \    \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\":\
    \ 5,\\n                        \\\"amount\\\": 1,\\n                        \\\
    \"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n          \
    \              \\\"mmol_l\\\": 5.55062,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"ingredient\":\
    \ \"(NH4)2SO4\",\n    \"existing\": {\n      \"value\": \"2\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"Solution A\",\n    \"source_amount\": {\n      \"value\": 2,\n      \"unit\"\
    : \"g\"\n    },\n    \"basis\": \"JCM batch comprises separate 500 ml water portions;\
    \ provider explicitly declares 1000 ml and g_l. Retain that declared basis rather\
    \ than claim a measured final volume.\",\n    \"proposed\": \"Retain the supported\
    \ provider-basis value, add exact claim evidence and preserve the primary preparation\
    \ stage.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm129\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, exact named ingredient\
    \ row\",\n        \"exact_source_quote\": \"(NH 4 ) 2 SO 4 2.0 g\",\n        \"\
    snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 2,\\n                        \\\
    \"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2,\\n          \
    \              \\\"mmol_l\\\": 15.1355,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[1].concentration\",\n    \"ingredient\":\
    \ \"KCl\",\n    \"existing\": {\n      \"value\": \"0.1\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"Solution A\",\n    \"source_amount\": {\n      \"value\": 0.1,\n      \"unit\"\
    : \"g\"\n    },\n    \"basis\": \"JCM batch comprises separate 500 ml water portions;\
    \ provider explicitly declares 1000 ml and g_l. Retain that declared basis rather\
    \ than claim a measured final volume.\",\n    \"proposed\": \"Retain the supported\
    \ provider-basis value, add exact claim evidence and preserve the primary preparation\
    \ stage.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm129\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, exact named ingredient\
    \ row\",\n        \"exact_source_quote\": \"KCl 0.1 g\",\n        \"snapshot_sha256\"\
    : \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\",\n    \
    \    \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                \
    \        \\\"mmol_l\\\": 1.34138,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[2].concentration\",\n    \"ingredient\":\
    \ \"K2HPO4\",\n    \"existing\": {\n      \"value\": \"0.5\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"Solution A\",\n    \"source_amount\": {\n      \"value\": 0.5,\n      \"unit\"\
    : \"g\"\n    },\n    \"basis\": \"JCM batch comprises separate 500 ml water portions;\
    \ provider explicitly declares 1000 ml and g_l. Retain that declared basis rather\
    \ than claim a measured final volume.\",\n    \"proposed\": \"Retain the supported\
    \ provider-basis value, add exact claim evidence and preserve the primary preparation\
    \ stage.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm129\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, exact named ingredient\
    \ row\",\n        \"exact_source_quote\": \"K 2 HPO 4 0.5 g\",\n        \"snapshot_sha256\"\
    : \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\",\n    \
    \    \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n                \
    \        \\\"mmol_l\\\": 2.87066,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[3].concentration\",\n    \"ingredient\":\
    \ \"MgSO4 x 7 H2O\",\n    \"existing\": {\n      \"value\": \"0.5\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"Solution A\",\n    \"source_amount\": {\n      \"value\": 0.5,\n      \"unit\"\
    : \"g\"\n    },\n    \"basis\": \"JCM batch comprises separate 500 ml water portions;\
    \ provider explicitly declares 1000 ml and g_l. Retain that declared basis rather\
    \ than claim a measured final volume.\",\n    \"proposed\": \"Retain the supported\
    \ provider-basis value, add exact claim evidence and preserve the primary preparation\
    \ stage.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm129\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, exact named ingredient\
    \ row\",\n        \"exact_source_quote\": \"MgSO 4 ·7H 2 O 0.5 g\",\n        \"\
    snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n  \
    \                      \\\"mmol_l\\\": 2.02859,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[4].concentration\",\n    \"ingredient\":\
    \ \"Pancreatic digest of casein\",\n    \"existing\": {\n      \"value\": \"17.0\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"correct\",\n    \"\
    source_stage\": \"Unverified commercial-product decomposition placed at receiving-medium\
    \ root\",\n    \"proposed\": \"Replace the unscaled generic constituent assertion\
    \ with the exact source-supported opaque BD-BBL broth addition pending a verified\
    \ product specification. No replacement constituent amount is calculated.\",\n\
    \    \"source_amount\": {\n      \"value\": 0.1,\n      \"unit\": \"g\",\n   \
    \   \"material\": \"BD-BBL Trypticase soy broth as a whole\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm129\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\",\n        \"source_locator\"\
    : \"JCM 129 Solution A table, commercial broth row\",\n        \"exact_source_quote\"\
    : \"Trypticase soy broth (BD-BBL) 0.1 g\",\n        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Trypticase soy broth\\\",\\n                        \\\"compound_id\\\
    \": 99,\\n                        \\\"attribute\\\": \\\"BD-BBL\\\",\\n      \
    \                  \\\"amount\\\": 0.1,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\n     \
    \ }\n    ],\n    \"explanation\": \"The primary supports 0.1 g of the whole product,\
    \ not this generic constituent amount. The five non-agar decomposition values\
    \ total 30 g/L locally; even if a generic 30 g/L stock formula were independently\
    \ verified, its values could not be inserted unchanged for this 0.1 g addition.\
    \ Exact constituent proportions and product equivalence remain unavailable, so\
    \ no scaling or substitute formulation is proposed.\"\n  },\n  {\n    \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml\",\n    \"\
    field_path\": \"ingredients[5].concentration\",\n    \"ingredient\": \"Peptic\
    \ digest of soybean meal\",\n    \"existing\": {\n      \"value\": \"3.0\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Unverified commercial-product decomposition placed at receiving-medium root\"\
    ,\n    \"proposed\": \"Replace the unscaled generic constituent assertion with\
    \ the exact source-supported opaque BD-BBL broth addition pending a verified product\
    \ specification. No replacement constituent amount is calculated.\",\n    \"source_amount\"\
    : {\n      \"value\": 0.1,\n      \"unit\": \"g\",\n      \"material\": \"BD-BBL\
    \ Trypticase soy broth as a whole\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, commercial broth row\"\
    ,\n        \"exact_source_quote\": \"Trypticase soy broth (BD-BBL) 0.1 g\",\n\
    \        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Trypticase soy broth\\\",\\n                        \\\"compound_id\\\
    \": 99,\\n                        \\\"attribute\\\": \\\"BD-BBL\\\",\\n      \
    \                  \\\"amount\\\": 0.1,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\n     \
    \ }\n    ],\n    \"explanation\": \"The primary supports 0.1 g of the whole product,\
    \ not this generic constituent amount. The five non-agar decomposition values\
    \ total 30 g/L locally; even if a generic 30 g/L stock formula were independently\
    \ verified, its values could not be inserted unchanged for this 0.1 g addition.\
    \ Exact constituent proportions and product equivalence remain unavailable, so\
    \ no scaling or substitute formulation is proposed.\"\n  },\n  {\n    \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml\",\n    \"\
    field_path\": \"ingredients[6].concentration\",\n    \"ingredient\": \"Glucose\"\
    ,\n    \"existing\": {\n      \"value\": \"2.5\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"decision\": \"correct\",\n    \"source_stage\": \"Unverified commercial-product\
    \ decomposition placed at receiving-medium root\",\n    \"proposed\": \"Replace\
    \ the unscaled generic constituent assertion with the exact source-supported opaque\
    \ BD-BBL broth addition pending a verified product specification. No replacement\
    \ constituent amount is calculated.\",\n    \"source_amount\": {\n      \"value\"\
    : 0.1,\n      \"unit\": \"g\",\n      \"material\": \"BD-BBL Trypticase soy broth\
    \ as a whole\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, commercial broth row\"\
    ,\n        \"exact_source_quote\": \"Trypticase soy broth (BD-BBL) 0.1 g\",\n\
    \        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Trypticase soy broth\\\",\\n                        \\\"compound_id\\\
    \": 99,\\n                        \\\"attribute\\\": \\\"BD-BBL\\\",\\n      \
    \                  \\\"amount\\\": 0.1,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\n     \
    \ }\n    ],\n    \"explanation\": \"The primary supports 0.1 g of the whole product,\
    \ not this generic constituent amount. The five non-agar decomposition values\
    \ total 30 g/L locally; even if a generic 30 g/L stock formula were independently\
    \ verified, its values could not be inserted unchanged for this 0.1 g addition.\
    \ Exact constituent proportions and product equivalence remain unavailable, so\
    \ no scaling or substitute formulation is proposed.\"\n  },\n  {\n    \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml\",\n    \"\
    field_path\": \"ingredients[7].concentration\",\n    \"ingredient\": \"Sodium\
    \ chloride\",\n    \"existing\": {\n      \"value\": \"5.0\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"correct\",\n    \"source_stage\": \"\
    Unverified commercial-product decomposition placed at receiving-medium root\"\
    ,\n    \"proposed\": \"Replace the unscaled generic constituent assertion with\
    \ the exact source-supported opaque BD-BBL broth addition pending a verified product\
    \ specification. No replacement constituent amount is calculated.\",\n    \"source_amount\"\
    : {\n      \"value\": 0.1,\n      \"unit\": \"g\",\n      \"material\": \"BD-BBL\
    \ Trypticase soy broth as a whole\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, commercial broth row\"\
    ,\n        \"exact_source_quote\": \"Trypticase soy broth (BD-BBL) 0.1 g\",\n\
    \        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Trypticase soy broth\\\",\\n                        \\\"compound_id\\\
    \": 99,\\n                        \\\"attribute\\\": \\\"BD-BBL\\\",\\n      \
    \                  \\\"amount\\\": 0.1,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\n     \
    \ }\n    ],\n    \"explanation\": \"The primary supports 0.1 g of the whole product,\
    \ not this generic constituent amount. The five non-agar decomposition values\
    \ total 30 g/L locally; even if a generic 30 g/L stock formula were independently\
    \ verified, its values could not be inserted unchanged for this 0.1 g addition.\
    \ Exact constituent proportions and product equivalence remain unavailable, so\
    \ no scaling or substitute formulation is proposed.\"\n  },\n  {\n    \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml\",\n    \"\
    field_path\": \"ingredients[8].concentration\",\n    \"ingredient\": \"Dipotassium\
    \ phosphate\",\n    \"existing\": {\n      \"value\": \"2.5\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"decision\": \"correct\",\n    \"source_stage\": \"\
    Unverified commercial-product decomposition placed at receiving-medium root\"\
    ,\n    \"proposed\": \"Replace the unscaled generic constituent assertion with\
    \ the exact source-supported opaque BD-BBL broth addition pending a verified product\
    \ specification. No replacement constituent amount is calculated.\",\n    \"source_amount\"\
    : {\n      \"value\": 0.1,\n      \"unit\": \"g\",\n      \"material\": \"BD-BBL\
    \ Trypticase soy broth as a whole\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, commercial broth row\"\
    ,\n        \"exact_source_quote\": \"Trypticase soy broth (BD-BBL) 0.1 g\",\n\
    \        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Trypticase soy broth\\\",\\n                        \\\"compound_id\\\
    \": 99,\\n                        \\\"attribute\\\": \\\"BD-BBL\\\",\\n      \
    \                  \\\"amount\\\": 0.1,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\n     \
    \ }\n    ],\n    \"explanation\": \"The primary supports 0.1 g of the whole product,\
    \ not this generic constituent amount. The five non-agar decomposition values\
    \ total 30 g/L locally; even if a generic 30 g/L stock formula were independently\
    \ verified, its values could not be inserted unchanged for this 0.1 g addition.\
    \ Exact constituent proportions and product equivalence remain unavailable, so\
    \ no scaling or substitute formulation is proposed.\"\n  },\n  {\n    \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml\",\n    \"\
    field_path\": \"ingredients[9].concentration\",\n    \"ingredient\": \"Agar\"\
    ,\n    \"existing\": {\n      \"value\": \"15.0\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"decision\": \"correct\",\n    \"source_stage\": \"Conditional\
    \ solid-medium branch; solution B before separate autoclaving\",\n    \"proposed\"\
    : \"Remove unconditional agar from the liquid-base ingredient assertion and represent\
    \ the source’s optional solution-B condition separately. Retain the exact 15 g/L\
    \ wording and addition location in solution B; whether the denominator is solution\
    \ B or the final mixed medium is unresolved. Do not calculate a B-basis or final\
    \ concentration.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129, conditional solid-medium sentence\"\
    ,\n        \"exact_source_quote\": \"For preparation of solid medium, add 15.0\
    \ g/L agar in solution B before autoclaving.\",\n        \"snapshot_sha256\":\
    \ \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\",\n    \
    \    \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ingredients[10].concentration\",\n    \"ingredient\"\
    : \"Glucose\",\n    \"existing\": {\n      \"value\": \"1\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"Solution B\",\n    \"source_amount\": {\n      \"value\": 1,\n      \"unit\"\
    : \"g\"\n    },\n    \"basis\": \"JCM batch comprises separate 500 ml water portions;\
    \ provider explicitly declares 1000 ml and g_l. Retain that declared basis rather\
    \ than claim a measured final volume.\",\n    \"proposed\": \"Retain the supported\
    \ provider-basis value, add exact claim evidence and preserve the primary preparation\
    \ stage.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm129\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution B table, exact named ingredient\
    \ row\",\n        \"exact_source_quote\": \"Glucose 1.0 g\",\n        \"snapshot_sha256\"\
    : \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\",\n    \
    \    \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\":\
    \ 5,\\n                        \\\"amount\\\": 1,\\n                        \\\
    \"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n          \
    \              \\\"mmol_l\\\": 5.55062,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target and owner\",\n    \"field_path\"\
    : \"ingredients (missing intact source product)\",\n    \"decision\": \"add\"\
    ,\n    \"source_stage\": \"Solution A\",\n    \"source_amount\": {\n      \"value\"\
    : 0.1,\n      \"unit\": \"g\",\n      \"material\": \"Trypticase soy broth (BD-BBL)\"\
    \n    },\n    \"proposed\": \"Represent the exact opaque commercial addition and\
    \ source identity; avoid duplicate counting with the unverified constituent expansion.\
    \ Provider reports 0.1 g/L on its declared 1000 ml basis.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm129\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\",\n        \"source_locator\"\
    : \"Solution A commercial broth row\",\n        \"exact_source_quote\": \"Trypticase\
    \ soy broth (BD-BBL) 0.1 g\",\n        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Trypticase soy broth\\\",\\n                        \\\"compound_id\\\
    \": 99,\\n                        \\\"attribute\\\": \\\"BD-BBL\\\",\\n      \
    \                  \\\"amount\\\": 0.1,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\n     \
    \ }\n    ]\n  },\n  {\n    \"input\": \"target and owner\",\n    \"field_path\"\
    : \"solutions / preparation_steps (missing A solvent)\",\n    \"decision\": \"\
    add\",\n    \"source_stage\": \"Solution A before separate autoclaving\",\n  \
    \  \"source_amount\": {\n      \"value\": 500,\n      \"unit\": \"ml\"\n    },\n\
    \    \"proposed\": \"Preserve the two separate solvent aliquots and their stages.\
    \ Provider’s aggregate 1000 ml row does not replace their individual preparation\
    \ roles.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm129\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution A table, distilled-water row\"\
    ,\n        \"exact_source_quote\": \"Distilled water 500.0 ml\",\n        \"snapshot_sha256\"\
    : \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\",\n    \
    \    \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target and owner\",\n    \"field_path\"\
    : \"solutions / preparation_steps (missing B solvent)\",\n    \"decision\": \"\
    add\",\n    \"source_stage\": \"Solution B before separate autoclaving\",\n  \
    \  \"source_amount\": {\n      \"value\": 500,\n      \"unit\": \"ml\"\n    },\n\
    \    \"proposed\": \"Preserve the two separate solvent aliquots and their stages.\
    \ Provider’s aggregate 1000 ml row does not replace their individual preparation\
    \ roles.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm129\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129 Solution B table, distilled-water row\"\
    ,\n        \"exact_source_quote\": \"Distilled water 500.0 ml\",\n        \"snapshot_sha256\"\
    : \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\",\n    \
    \    \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ129api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J129\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"84f491180acbee5166da42b9c5b972c81251645851fbc504ef609ff2b196c09f\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ph_value; preparation_steps[0]\",\n    \"existing\": 3.0,\n    \"decision\": \"\
    evidence_only\",\n    \"source_stage\": \"Solution A before sterilization and\
    \ combination\",\n    \"proposed\": \"Retain target pH 3.0 with the explicitly\
    \ supported solution-A context and claim evidence. Do not relabel it as measured\
    \ final pH.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129, sentence between Solution A and Solution\
    \ B tables\",\n        \"exact_source_quote\": \"Adjust pH to 3.0.\",\n      \
    \  \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml\"\
    ,\n    \"field_path\": \"ph_value; preparation_steps[0]\",\n    \"existing\":\
    \ 3.0,\n    \"decision\": \"evidence_only\",\n    \"source_stage\": \"Solution\
    \ A before sterilization and combination\",\n    \"proposed\": \"Retain target\
    \ pH 3.0 with the explicitly supported solution-A context and claim evidence.\
    \ Do not relabel it as measured final pH.\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm129\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\"\
    ,\n        \"source_locator\": \"JCM 129, sentence between Solution A and Solution\
    \ B tables\",\n        \"exact_source_quote\": \"Adjust pH to 3.0.\",\n      \
    \  \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target and owner\",\n    \"field_path\"\
    : \"preparation_steps (missing qualified sterilization condition)\",\n    \"decision\"\
    : \"add\",\n    \"source_amount\": {\n      \"value\": 121,\n      \"unit\": \"\
    C\"\n    },\n    \"source_stage\": \"Autoclave A and B separately; general JCM\
    \ qualifier applies unless otherwise stated\",\n    \"proposed\": \"Retain the\
    \ primary’s separate sterilization and aseptic combination, with its qualified\
    \ default condition; do not combine the stocks before autoclaving.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm129\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\",\n  \
    \      \"source_locator\": \"JCM page global qualifier before heading\",\n   \
    \     \"exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"jcm129\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\",\n        \"source_locator\"\
    : \"JCM 129, preparation after Solution B\",\n        \"exact_source_quote\":\
    \ \"Autoclave Solutions A and B separately, and mix aseptically.\",\n        \"\
    snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target and owner\",\n    \"field_path\"\
    : \"preparation_steps (missing qualified sterilization condition)\",\n    \"decision\"\
    : \"add\",\n    \"source_amount\": {\n      \"value\": 15,\n      \"unit\": \"\
    min\"\n    },\n    \"source_stage\": \"Autoclave A and B separately; general JCM\
    \ qualifier applies unless otherwise stated\",\n    \"proposed\": \"Retain the\
    \ primary’s separate sterilization and aseptic combination, with its qualified\
    \ default condition; do not combine the stocks before autoclaving.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm129\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\",\n  \
    \      \"source_locator\": \"JCM page global qualifier before heading\",\n   \
    \     \"exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      },\n      {\n        \"source_key\": \"jcm129\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=129\",\n        \"source_locator\"\
    : \"JCM 129, preparation after Solution B\",\n        \"exact_source_quote\":\
    \ \"Autoclave Solutions A and B separately, and mix aseptically.\",\n        \"\
    snapshot_sha256\": \"78408a1d99924c5fe08a5150b7fd008e06bac481bd2095674e57111dd8d8bb0d\"\
    ,\n        \"parsed_text_sha256\": \"a730eeb56b4fb5be22781d9aeb2cb07162480d6326a61aef1b35fa1a048a9a27\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: supported
  summary: '9 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 11/11 primary and 5/11 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Source forms
    are assessed separately.'
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi17234
  - chebi2509
  - chebi26710
  - chebi31795
  - chebi32588
  - chebi62946
  - foodon03315720
  - micro0000182
  details: 'Instance coverage on a 0–100 percent scale, denominator 11: primary 100.00%;
    secondary 45.45%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: chemical-forms
  area: grounding
  topic: Actual source forms versus valid ingredient identifiers
  outcome: concern
  summary: The direct source salts and glucose match the asserted primary forms; no
    hydrate conversion is needed. MICRO tryptone and FOODON hydrolyzed vegetable protein
    are valid broad ingredient identities, but their existence does not establish
    the exact BD-BBL product decomposition, Bacto-brand synonym equivalence or supplier
    interchangeability. The commercial constituent CHEBI labels identify chemicals,
    not their amounts or presence in this specific product.
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - primary
  - provider
  - micro0000182
  - foodon03315720
  - mim
- assessment_id: preparation
  area: completeness
  topic: Separate source stages, water and physical-state branch
  outcome: concern
  summary: The sole local pH-adjustment step omits Solution A/B separation, each 500
    ml water aliquot, separate autoclaving and aseptic mixing. The source’s optional
    solid branch puts agar into B before autoclaving; the local record instead includes
    it unconditionally despite LIQUID. Source-stage information cannot be recovered
    from the flattened provider table alone.
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Composition, physical state and organism evidence
  outcome: concern
  summary: COMPLEX is compatible with a medium containing commercial broth. UNDEFINED
    is a broad permitted description; after source reconciliation, SEMI_DEFINED more
    precisely describes defined salts/glucose with a small complex supplement. LIQUID
    applies to the base recipe but conflicts with the current unconditional agar.
    Bacterial category and generic cultivation application do not establish particular
    Acidiphilium growth, optimal pH or a taxonomic identifier.
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - record
  - primary
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:002462
  evidence_ids:
  - record
  - history-metadata
  - owner-0
findings:
- finding_id: f1
  issue_key: culturemech.002462.unscaled-commercial-expansion
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Generic commercial constituents replace the small source broth addition
  description: Both target and owner replace the primary’s 0.1 g BD-BBL Trypticase
    soy broth with 17 g/L casein digest, 3 g/L soybean digest, 2.5 g/L glucose, 5
    g/L NaCl, 2.5 g/L dipotassium phosphate and 15 g/L agar. The first five sum to
    30 g/L; no product-specific scaling evidence supports them. Agar is not part of
    the liquid-base broth addition and the exact source’s solid branch is conditional
    within Solution B. The separate 1 g glucose in Solution B must remain distinct.
  target_ids:
  - CultureMech:002462
  field_paths:
  - ingredients[4:10]
  - ingredients[10]
  - physical_state
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
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
  issue_key: culturemech.002462.preparation-stage-omission
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Two separately prepared source solutions are collapsed
  description: Both local layers retain only Adjust pH to 3.0 and omit the source’s
    A/B grouping, two 500 ml water aliquots, separate autoclaving and aseptic combination.
    The JCM default is explicitly qualified and must be attached to the two stated
    autoclave stages. Missing these boundaries materially changes the preparation
    description.
  target_ids:
  - CultureMech:002462
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.002462.product-provenance-unresolved
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Multi-supplier product claims lack exact specification support
  description: The local notes assert researched product specifications while citing
    a generic encyclopedia URL and mixing BD, Sigma and Neogen catalogs under TSB/TSA.
    The primary specifically names BD-BBL broth. Exact BD and Sigma attempts did not
    yield formula bytes, and the prior BD manual attempt failed. Brand-specific synonyms
    and supplier interchangeability cannot be authenticated from valid ingredient
    ontology labels.
  target_ids:
  - CultureMech:002462
  field_paths:
  - notes
  - ingredients[4:10].supplier_catalog
  - ingredients[4:6].synonyms
  evidence_ids:
  - record
  - owner-0
  - primary
  - bd211825PriorAttempt-attempt
  - bdManualPriorAttempt-attempt
  - sigma22092-attempt
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
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
  issue_key: culturemech.002462.claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source-supported direct quantities have no claim-level evidence
  description: The four direct mineral amounts, separate glucose and target pH are
    supported on the recorded provider/source basis but have no attached evidence
    in either local layer. They remain evidence_only rather than verified. Commercial-product
    and physical-state failures are separate from this narrower provenance gap.
  target_ids:
  - CultureMech:002462
  field_paths:
  - ingredients[0:4]
  - ingredients[10]
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
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
  description: Restore the intact source-supported BD-BBL broth addition and conditional
    agar scope in the maintained owner. Only decompose an exact verified product with
    explicit dose and basis; preserve the independent Solution-B glucose and regenerate
    the target after owner review.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002462
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
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
  description: Represent the exact source stages and solvent portions in the normalized
    owner, with conditional solid-medium preparation separated. Preserve pH as the
    target of the source A stage; do not invent titrant identity or dose.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002462
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
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
  description: Retain the failed-attempt provenance and resolve the exact BD-BBL product/catalog
    before preserving product-specific constituents or supplier equivalence. Replace
    broad bibliographic claims with narrowly verified source support; leave unresolved
    product correspondence explicit.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002462
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
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
  description: Attach exact source snippets and stage/volume explanations to the supported
    direct claims without importing unsupported constituent evidence. Preserve existing
    append-only history and use normal owner/merge verification.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002462
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
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
- The exact asserted BD 211825 product attempt returned HTTP 403; the preserved prior
  metadata provides no product formulation bytes. BD-BBL Trypticase soy broth identity,
  catalog equivalence and constituent proportions cannot be verified from that failed
  request.
- The preserved BD manual attempt returned HTTP 404. No manual content was inspected;
  it cannot corroborate a product or mixture recipe.
- The exact asserted Sigma 22092 specification attempt timed out without captured
  formula bytes. Its equivalence to the primary’s BD-BBL product and the stated multi-supplier
  constituent formula remain unresolved; no Sigma formula substitutes for BD-BBL.
- The generic Wikipedia source and multi-supplier catalogs are not treated as inspected
  product specifications. No commercial constituent proportions, titrant, final measured
  volume, strain growth or oxygen requirement were inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-018
- generated-medium
```
