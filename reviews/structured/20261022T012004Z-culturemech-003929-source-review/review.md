# Source and formulation review: bm_medium (CultureMech:003929)

- Review: 20261022T012004Z-culturemech-003929-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T01:04:28Z
- Finished UTC: 2026-10-22T01:20:04Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM1192 supports the BM recipe as printed batch additions, including methanol 4 ml, water 1000 ml and optional agar. All three local layers instead store five g/L values and omit water. The historical MediaDive derivative reports explicitly contain methanol g_l 3.168, but their cited raw was not recovered; current KOMODO has null methanol mass and a different expanded formulation. Missing final-volume and methanol conversion provenance remain unresolved. Review is partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 438; batch 044 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-three task batches contain 430 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 433 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003929 | data/merge_yaml/merged/BM_MEDIUM.yaml | generated | bm_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003929 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003929 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch044/438/strict.tsv |
| validate-terms | passed | True | CultureMech:003929 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003929 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003929 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: api1192 | unavailable | True | CultureMech:003929 | The current exact MediaDive REST1192 request returned HTTP 503. The cited historical raw digest 711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182 was not recovered in the bounded captured surfaces. Historical report objects remain derivative, so their g_l declaration cannot be independently authenticated here. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003929.

The four documented recipes completed; interpret the scope of each separately.

### Exact maintained contributors and source identity

identity: supported. Targets: CultureMech:003929.

The target has the exact KOMODO1192 and DSM1192 maintained contributors. Both owners and target share all five ingredients and rates; the source-duplicate relationship is locally reciprocal. Exact medium-number identity supports comparison, not equivalence of the current expanded provider page and the collection recipe.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:003929.

4 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 4/5 primary and 4/5 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 5: primary 80.00%; secondary 80.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### All four asserted chemicals and commercial base identity

grounding: supported. Targets: CultureMech:003929.

Biotin CHEBI15956 has the biotin stereochemistry and D-biotin synonyms; the unqualified primary name gives no contrary stereoisomer. CHEBI176843 is the vitamin B12 class, compatible with the unspecific primary name without choosing a vitamer. CHEBI17790 is methanol and CHEBI2509 is agar. None supplies a liquid density or final-volume basis. Difco marine broth is explicitly Difco2216 in the primary and remains a commercial complex base; the current provider expansion is not adopted as its verified manufacturer composition.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003929.

19 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Preparation, conditions, classification and growth limits

scope: unknown. Targets: CultureMech:003929.

The complete primary contains only the formulation table. No sterilization cycle, pH, temperature, oxygen requirement or strain-level growth is established. No target_organisms or growth metrics are asserted locally. Complex/undefined composition is appropriate to the commercial broth; the optional agar note is retained and the fixed solid classification needs a branch decision. The current provider Aerobic=false flag is not biological evidence.

### Source linkage and historic provider basis

evidence: concern. Targets: CultureMech:003929.

No quantity evidence is attached to the five concentrations in any of the three layers. The two historical derivative reports agree on a provider-normalized methanol value, but are not two independent raw-source authentications. Current primary batch quantities and current provider composition are kept distinct.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003929.

17 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "Difco marine broth (Difco 2216)",
    "stage": "DSM1192 printed batch; data/merge_yaml/merged/BM_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BM_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "37.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 37.4,
      "unit": "g",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Difco marine broth",
        "exact_source_quote": " Difco marine broth (Difco 2216)           37.4    g",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer."
  },
  {
    "decision_id": "q2",
    "name": "Biotin",
    "stage": "DSM1192 printed batch; data/merge_yaml/merged/BM_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BM_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2e-05",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 20,
      "unit": "µg",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Biotin",
        "exact_source_quote": " Biotin                                    20.0   µg",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer. The exact unit conversion is 20 µg = 0.000020 g; that arithmetic alone does not establish the denominator."
  },
  {
    "decision_id": "q3",
    "name": "Vitamin B12",
    "stage": "DSM1192 printed batch; data/merge_yaml/merged/BM_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BM_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1e-06",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 1,
      "unit": "µg",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Vitamin B12",
        "exact_source_quote": " Vitamin B12                                1.0   µg",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer. The exact unit conversion is 1 µg = 0.000001 g; that arithmetic alone does not establish the denominator."
  },
  {
    "decision_id": "q4",
    "name": "Methanol",
    "stage": "DSM1192 printed batch; data/merge_yaml/merged/BM_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BM_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "3.168",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 4,
      "unit": "ml",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Methanol",
        "exact_source_quote": " Methanol                                   4.0   ml",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      },
      {
        "historical_report": "reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/bm_medium.yaml.md",
        "snapshot_sha256": "5991fc14bc42c3f7ec1937c308aaa71458509ccf28b2fb8f3afecb282e8138c3",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1192",
        "source_locator": "Historical report source.data.solutions[0].recipe methanol row",
        "historical_raw_sha256": "711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182",
        "historical_accessed_at": "2026-10-07T13:18:36.667926Z",
        "reported_amount": {
          "amount": 4,
          "unit": "ml",
          "g_l": 3.168,
          "mmol_l": 98.8702
        },
        "limit": "Derivative report object only; exact cited raw unavailable."
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer. The historical reports explicitly preserve provider g_l=3.168 for amount 4 ml, so the value is not unsupported by all historical documentation. Their cited raw is unrecovered; the current KOMODO mass cell is null. No density, concentration or volume conversion is inferred from those derivative rows."
  },
  {
    "decision_id": "q5",
    "name": "Agar, optional",
    "stage": "DSM1192 printed batch; data/merge_yaml/merged/BM_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BM_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 15,
      "unit": "g",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: (Agar, if necessary",
        "exact_source_quote": " (Agar, if necessary                       15.0   g)",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer. The existing note already preserves if necessary. Fifteen grams applies only to the agar branch; no mandatory agar addition or fixed 15 g/L claim is established."
  },
  {
    "decision_id": "q6",
    "name": "Difco marine broth (Difco 2216)",
    "stage": "DSM1192 printed batch; data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "37.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 37.4,
      "unit": "g",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Difco marine broth",
        "exact_source_quote": " Difco marine broth (Difco 2216)           37.4    g",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer."
  },
  {
    "decision_id": "q7",
    "name": "Biotin",
    "stage": "DSM1192 printed batch; data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2e-05",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 20,
      "unit": "µg",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Biotin",
        "exact_source_quote": " Biotin                                    20.0   µg",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer. The exact unit conversion is 20 µg = 0.000020 g; that arithmetic alone does not establish the denominator."
  },
  {
    "decision_id": "q8",
    "name": "Vitamin B12",
    "stage": "DSM1192 printed batch; data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1e-06",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 1,
      "unit": "µg",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Vitamin B12",
        "exact_source_quote": " Vitamin B12                                1.0   µg",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer. The exact unit conversion is 1 µg = 0.000001 g; that arithmetic alone does not establish the denominator."
  },
  {
    "decision_id": "q9",
    "name": "Methanol",
    "stage": "DSM1192 printed batch; data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "3.168",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 4,
      "unit": "ml",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Methanol",
        "exact_source_quote": " Methanol                                   4.0   ml",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      },
      {
        "historical_report": "reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/bm_medium.yaml.md",
        "snapshot_sha256": "5991fc14bc42c3f7ec1937c308aaa71458509ccf28b2fb8f3afecb282e8138c3",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1192",
        "source_locator": "Historical report source.data.solutions[0].recipe methanol row",
        "historical_raw_sha256": "711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182",
        "historical_accessed_at": "2026-10-07T13:18:36.667926Z",
        "reported_amount": {
          "amount": 4,
          "unit": "ml",
          "g_l": 3.168,
          "mmol_l": 98.8702
        },
        "limit": "Derivative report object only; exact cited raw unavailable."
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer. The historical reports explicitly preserve provider g_l=3.168 for amount 4 ml, so the value is not unsupported by all historical documentation. Their cited raw is unrecovered; the current KOMODO mass cell is null. No density, concentration or volume conversion is inferred from those derivative rows."
  },
  {
    "decision_id": "q10",
    "name": "Agar, optional",
    "stage": "DSM1192 printed batch; data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 15,
      "unit": "g",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: (Agar, if necessary",
        "exact_source_quote": " (Agar, if necessary                       15.0   g)",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer. The existing note already preserves if necessary. Fifteen grams applies only to the agar branch; no mandatory agar addition or fixed 15 g/L claim is established."
  },
  {
    "decision_id": "q11",
    "name": "Difco marine broth (Difco 2216)",
    "stage": "DSM1192 printed batch; data/normalized_yaml/bacterial/bm_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bm_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "37.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 37.4,
      "unit": "g",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Difco marine broth",
        "exact_source_quote": " Difco marine broth (Difco 2216)           37.4    g",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer."
  },
  {
    "decision_id": "q12",
    "name": "Biotin",
    "stage": "DSM1192 printed batch; data/normalized_yaml/bacterial/bm_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bm_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2e-05",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 20,
      "unit": "µg",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Biotin",
        "exact_source_quote": " Biotin                                    20.0   µg",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer. The exact unit conversion is 20 µg = 0.000020 g; that arithmetic alone does not establish the denominator."
  },
  {
    "decision_id": "q13",
    "name": "Vitamin B12",
    "stage": "DSM1192 printed batch; data/normalized_yaml/bacterial/bm_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bm_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1e-06",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 1,
      "unit": "µg",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Vitamin B12",
        "exact_source_quote": " Vitamin B12                                1.0   µg",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer. The exact unit conversion is 1 µg = 0.000001 g; that arithmetic alone does not establish the denominator."
  },
  {
    "decision_id": "q14",
    "name": "Methanol",
    "stage": "DSM1192 printed batch; data/normalized_yaml/bacterial/bm_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bm_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "3.168",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 4,
      "unit": "ml",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Methanol",
        "exact_source_quote": " Methanol                                   4.0   ml",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      },
      {
        "historical_report": "reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/bm_medium.yaml.md",
        "snapshot_sha256": "5991fc14bc42c3f7ec1937c308aaa71458509ccf28b2fb8f3afecb282e8138c3",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1192",
        "source_locator": "Historical report source.data.solutions[0].recipe methanol row",
        "historical_raw_sha256": "711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182",
        "historical_accessed_at": "2026-10-07T13:18:36.667926Z",
        "reported_amount": {
          "amount": 4,
          "unit": "ml",
          "g_l": 3.168,
          "mmol_l": 98.8702
        },
        "limit": "Derivative report object only; exact cited raw unavailable."
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer. The historical reports explicitly preserve provider g_l=3.168 for amount 4 ml, so the value is not unsupported by all historical documentation. Their cited raw is unrecovered; the current KOMODO mass cell is null. No density, concentration or volume conversion is inferred from those derivative rows."
  },
  {
    "decision_id": "q15",
    "name": "Agar, optional",
    "stage": "DSM1192 printed batch; data/normalized_yaml/bacterial/bm_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bm_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 15,
      "unit": "g",
      "final_volume": "not declared"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: (Agar, if necessary",
        "exact_source_quote": " (Agar, if necessary                       15.0   g)",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary gives this batch addition, with 1000 ml listed water rather than an explicit final-volume or make-up instruction. The stored final-medium g/L basis is therefore unverified; retain the printed amount and stage without treating listed water as measured final volume. No quantity evidence is attached in this layer. The existing note already preserves if necessary. Fifteen grams applies only to the agar branch; no mandatory agar addition or fixed 15 g/L claim is established."
  },
  {
    "decision_id": "q16",
    "name": "Distilled water",
    "stage": "Printed batch solvent omitted from all three ingredient lists",
    "decision": "add",
    "local_fields": [],
    "desired": {
      "batch_volume": 1000,
      "unit": "ml"
    },
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: Distilled water",
        "exact_source_quote": " Distilled water                         1000.0   ml",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "The primary directly lists 1000 ml water. Add only as a batch solvent after source-scoped curation; do not turn it into 1000 g/L or a final-volume declaration."
  },
  {
    "decision_id": "q17",
    "name": "Optional agar branch and physical state",
    "stage": "Broth versus optional solid branch",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BM_MEDIUM.yaml",
        "field_path": "physical_state",
        "stored": "SOLID_AGAR"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
        "field_path": "physical_state",
        "stored": "SOLID_AGAR"
      },
      {
        "input": "data/normalized_yaml/bacterial/bm_medium.yaml",
        "field_path": "physical_state",
        "stored": "SOLID_AGAR"
      },
      {
        "input": "data/merge_yaml/merged/BM_MEDIUM.yaml",
        "field_path": "ingredients[4].notes",
        "stored": " (if necessary)"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
        "field_path": "ingredients[4].notes",
        "stored": " (if necessary)"
      },
      {
        "input": "data/normalized_yaml/bacterial/bm_medium.yaml",
        "field_path": "ingredients[4].notes",
        "stored": " (if necessary)"
      }
    ],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "dsm1192",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf",
        "source_locator": "Page 1 recipe row: (Agar, if necessary",
        "exact_source_quote": " (Agar, if necessary                       15.0   g)",
        "snapshot_sha256": "52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241",
        "parsed_text_sha256": "c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a"
      }
    ],
    "interpretation": "All layers already retain the optional agar note, but their SOLID_AGAR classification selects the solid branch. Clarify the represented variant before regeneration; the primary permits an agar-free branch and supplies no culture-specific rule for choosing it."
  }
]

## Findings

### f1: Batch quantities lack a verified final-medium basis and solvent representation

major / open / confirmed; issue key: culturemech.003929.quantity-basis-and-solvent.

All five local concentrations use g/L, while DSM1192 lists batch masses, methanol 4 ml and water 1000 ml without a final-volume declaration. Water is absent. Historical API-derived reports explicitly support the origin of 3.168 g/L as a provider declaration, but the cited raw is unrecovered and current KOMODO mass is null. This is an unresolved basis/conversion issue, not proof that every stored mass is numerically false.

### f2: The optional agar branch needs explicit representation

minor / open / confirmed; issue key: culturemech.003929.optional-agar-variant.

The primary permits agar only if necessary. Every layer retains that note, so optionality has not disappeared, but every top-level physical_state is SOLID_AGAR without a declared branch selection.

### f3: Current quantities have no attached claim-level evidence

minor / open / confirmed; issue key: culturemech.003929.amount-traceability.

All three scientific layers omit attached evidence for their five quantity assertions. Earlier reports preserve useful but bounded source statements outside the active ingredients.

### f4: KOMODO-derived history includes malformed and timezone-naive timestamps

minor / open / confirmed; issue key: culturemech.003929.history-timestamps.

The KOMODO owner and target retain 2026-01-27T01:15:01.fZ and a timezone-naive February 3 timestamp. The DSM owner timestamps are valid. Historical timing cannot be silently repaired by guessing an offset.

## Recommended Actions And Acceptance Checks

### a1

Curate the exact printed batch and solvent, recover the historical provider calculation if possible, and document any final-volume and methanol conversion basis before asserting final-medium rates. Preserve provider and collection variants separately.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain the existing optionality and explicitly represent the selected solid or broth variant before changing state or amounts. Do not silently remove agar or call it mandatory.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

After resolving the basis, attach short exact quotations and source version/hash, original units, stage and calculation separately. Preserve the historical reports and failed current API attempt.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve the original events and append an authorized provenance clarification if the original timing can be recovered; limit remediation to the affected KOMODO lineage before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/bm_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch044/438/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch044/438/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml:1:id: CultureMech:003929<br>./data/merge_yaml/merged/BM_MEDIUM.yaml:1:id: CultureMech:003929<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch044/source-preflight-bound/438/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 62 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf; Complete DSM1192 recipe, page 1 | supports | The primary specifies Difco marine broth (Difco 2216), five additions and distilled water. It does not declare final volume, methanol density, a preparation cycle, pH, incubation temperature, gas condition or organism-specific growth. |
| provider | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1192; Complete current Medium1192 page: ingredient table, SEED table, identity and provider flags | supports | The provider labels its composition table per litre, but its methanol Gram Amount and Mol Amount are null; the separate SEED methanol row is 0.001996007984031936 mol/L. It expands broth constituents and reports biotin 9.98e-6 g/L and B12 4.99e-7 g/L. This distinct current provider formulation does not establish the stored methanol mass or replace DSM1192. |
| catalogue | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact seven-column catalogue header and Medium1192 row only | supports | The exact 1192 identity points to DSM1192. The provider IsAerobic=false flag is a database assertion, not a growth experiment or an independently verified oxygen requirement. |
| api1192-attempt | https://mediadive.dsmz.de/rest/medium/1192; Preserved exact public retrieval result | context_only | The current exact MediaDive REST1192 request returned HTTP 503. The cited historical raw digest 711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182 was not recovered in the bounded captured surfaces. Historical report objects remain derivative, so their g_l declaration cannot be independently authenticated here. |
| report-0 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/bm_medium.yaml.md; Full exact-identity historical report; claim-specific derivative scope | context_only | Full exact-identity October curation report read. It preserves historical API1192 amount 4 ml, g_l 3.168 and mmol_l 98.8702, cited raw 711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182 and access 2026-10-07T13:18:36.667926Z. All amount claims remain unresolved in that report. This is derivative provider support, not recovered raw or a current KOMODO mass claim. |
| report-1 | reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1192_BM_MEDIUM.yaml.md; Full exact-identity historical report; claim-specific derivative scope | context_only | Full exact-identity October curation report read. It preserves historical API1192 amount 4 ml, g_l 3.168 and mmol_l 98.8702, cited raw 711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182 and access 2026-10-07T13:18:36.667926Z. All amount claims remain unresolved in that report. This is derivative provider support, not recovered raw or a current KOMODO mass claim. |
| report-2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BM_MEDIUM.md; Full exact-identity historical report; claim-specific derivative scope | context_only | Full October 5 inventory report read: zero of five quantities source-checked. It is historical triage, not independent confirmation or a source raw capture. |
| report-3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.md; Full exact-identity historical report; claim-specific derivative scope | context_only | Full October 5 inventory report read: zero of five quantities source-checked. It is historical triage, not independent confirmation or a source raw capture. |
| report-4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/bm_medium.md; Full exact-identity historical report; claim-specific derivative scope | context_only | Full October 5 inventory report read: zero of five quantities source-checked. It is historical triage, not independent confirmation or a source raw capture. |
| report-5 | reports/yaml_record_review/20260921T230106Z-BM_MEDIUM.md; Full exact-identity historical report; claim-specific derivative scope | context_only | Full September ad hoc review read. Its primary-source observations and earlier source-access limits are historical context; its g/L interpretation is not adopted without final-volume support, and its then-unavailable provider does not override the separately captured current page. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17790 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17790; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17790 resolves to methanol. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17790": [{"label": "Methanol", "match_type": "preferred_term", "identifier": "CHEBI:17790", "preferred_term": "Methanol", "ontology_id": "CHEBI:17790", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/BM_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml; data/normalized_yaml/bacterial/bm_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:57.003791"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml", "events": 6, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:57.003791"}]}, {"input": "data/normalized_yaml/bacterial/bm_medium.yaml", "events": 5, "timestamp_issues": []}] |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Read the full formulation guard, relevant merge_group and resolver composition-copy functions. Current code gives mechanism context only; the scientific-formulation equality guard does not establish which historical transformation produced these rates. No universal present-merger fault is inferred. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Read the full formulation guard, relevant merge_group and resolver composition-copy functions. Current code gives mechanism context only; the scientific-formulation equality guard does not establish which historical transformation produced these rates. No universal present-merger fault is inferred. |
| writer-2 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Read the full formulation guard, relevant merge_group and resolver composition-copy functions. Current code gives mechanism context only; the scientific-formulation equality guard does not establish which historical transformation produced these rates. No universal present-merger fault is inferred. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch044/438/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The current exact MediaDive REST1192 request returned HTTP 503. The cited historical raw digest 711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182 was not recovered in the bounded captured surfaces. Historical report objects remain derivative, so their g_l declaration cannot be independently authenticated here.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T012004Z-culturemech-003929-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bm_medium (CultureMech:003929)'
started_at: '2026-10-22T01:04:28Z'
finished_at: '2026-10-22T01:20:04Z'
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
summary: DSM1192 supports the BM recipe as printed batch additions, including methanol
  4 ml, water 1000 ml and optional agar. All three local layers instead store five
  g/L values and omit water. The historical MediaDive derivative reports explicitly
  contain methanol g_l 3.168, but their cited raw was not recovered; current KOMODO
  has null methanol mass and a different expanded formulation. Missing final-volume
  and methanol conversion provenance remain unresolved. Review is partial.
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
  - path: data/merge_yaml/merged/BM_MEDIUM.yaml
    sha256: f65869b33d5c9874156e2e592e2174c7d3592ef823ba2dce407a3fadd725ce42
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml
    sha256: 443356164beab26bd0466f1be4680f8274148317c772bdae9e901759bb0e201f
    role: context
  - path: data/normalized_yaml/bacterial/bm_medium.yaml
    sha256: 387dc1a1dc623ff3b2783d97cd8a3785e2d3b97a5607e5aaf5684dfa6d732eb1
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/bm_medium.yaml.md
    sha256: 5991fc14bc42c3f7ec1937c308aaa71458509ccf28b2fb8f3afecb282e8138c3
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1192_BM_MEDIUM.yaml.md
    sha256: b051da065c6f044f9ddc91fbe3567ccbb181699f67c4054a0ae8ac1df9094fcd
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BM_MEDIUM.md
    sha256: e892d40b9c10370198c449dde2e5a17a485ae6324feb52e0a0fb0a7107104e60
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.md
    sha256: d387717d0473b8e478ecedee62b26e5d87979d82b2b6509388e7693e59dc806a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/bm_medium.md
    sha256: 8cbbc517e25befcfd28fe7da461eb16816c60c31506af4867f412c4b8e1c6a8f
    role: context
  - path: reports/yaml_record_review/20260921T230106Z-BM_MEDIUM.md
    sha256: 3a8847eecbc162baad6b31cadb217558bfdabe0e1d46e40a1fb4be6deb890b6f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_jcm_missing_from_togo.py
    sha256: 3e7c9547e5fceda8ced6b556de50b6a0af17e0805be021af6b3e5a6b8eb70570
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
  selection: Task review 438; batch 044 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding forty-three task batches
    contain 430 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 433 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003929
targets:
- target_id: CultureMech:003929
  path: data/merge_yaml/merged/BM_MEDIUM.yaml
  label: bm_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003929
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BM_MEDIUM.yaml --workers 1
    --out /private/tmp/culturemech-review-work-batch044/438/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch044/438/strict.tsv"
  target_ids:
  - CultureMech:003929
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003929
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003929
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
  - CultureMech:003929
- check_id: api1192-source-access
  name: 'Exact source content access: api1192'
  required: true
  status: unavailable
  summary: The current exact MediaDive REST1192 request returned HTTP 503. The cited
    historical raw digest 711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182
    was not recovered in the bounded captured surfaces. Historical report objects
    remain derivative, so their g_l declaration cannot be independently authenticated
    here.
  target_ids:
  - CultureMech:003929
  evidence_ids:
  - api1192-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/bm_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T01:08:13.328119Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BM_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch044/438/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T01:08:14.821587Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch044/438/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T01:08:16.506451Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T01:08:17.573925Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T01:20:03Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml:1:id: CultureMech:003929

    ./data/merge_yaml/merged/BM_MEDIUM.yaml:1:id: CultureMech:003929

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch044/source-preflight-bound/438/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T01:20:03Z'
  support: supports
  summary: 62 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 2cbf1c3b6b085f5acd3f189ed055047e039780262b764058bbb90df31f3133be
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf
  locator: Complete DSM1192 recipe, page 1
  accessed_at: '2026-10-22T00:53:56.774170Z'
  support: supports
  summary: The primary specifies Difco marine broth (Difco 2216), five additions and
    distilled water. It does not declare final volume, methanol density, a preparation
    cycle, pH, incubation temperature, gas condition or organism-specific growth.
  snapshot_sha256: 52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241
- evidence_id: provider
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1192
  locator: 'Complete current Medium1192 page: ingredient table, SEED table, identity
    and provider flags'
  accessed_at: '2026-10-22T00:53:57.843086Z'
  support: supports
  summary: The provider labels its composition table per litre, but its methanol Gram
    Amount and Mol Amount are null; the separate SEED methanol row is 0.001996007984031936
    mol/L. It expands broth constituents and reports biotin 9.98e-6 g/L and B12 4.99e-7
    g/L. This distinct current provider formulation does not establish the stored
    methanol mass or replace DSM1192.
  snapshot_sha256: de0f921fb31c6729355a6183be67e3532383cc8c79632ca434847032ae83875c
- evidence_id: catalogue
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact seven-column catalogue header and Medium1192 row only
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The exact 1192 identity points to DSM1192. The provider IsAerobic=false
    flag is a database assertion, not a growth experiment or an independently verified
    oxygen requirement.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: api1192-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1192
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T00:53:56.816303Z'
  support: context_only
  summary: The current exact MediaDive REST1192 request returned HTTP 503. The cited
    historical raw digest 711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182
    was not recovered in the bounded captured surfaces. Historical report objects
    remain derivative, so their g_l declaration cannot be independently authenticated
    here.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: report-0
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/bm_medium.yaml.md
  locator: Full exact-identity historical report; claim-specific derivative scope
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: Full exact-identity October curation report read. It preserves historical
    API1192 amount 4 ml, g_l 3.168 and mmol_l 98.8702, cited raw 711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182
    and access 2026-10-07T13:18:36.667926Z. All amount claims remain unresolved in
    that report. This is derivative provider support, not recovered raw or a current
    KOMODO mass claim.
  snapshot_sha256: 5991fc14bc42c3f7ec1937c308aaa71458509ccf28b2fb8f3afecb282e8138c3
- evidence_id: report-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1192_BM_MEDIUM.yaml.md
  locator: Full exact-identity historical report; claim-specific derivative scope
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: Full exact-identity October curation report read. It preserves historical
    API1192 amount 4 ml, g_l 3.168 and mmol_l 98.8702, cited raw 711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182
    and access 2026-10-07T13:18:36.667926Z. All amount claims remain unresolved in
    that report. This is derivative provider support, not recovered raw or a current
    KOMODO mass claim.
  snapshot_sha256: b051da065c6f044f9ddc91fbe3567ccbb181699f67c4054a0ae8ac1df9094fcd
- evidence_id: report-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BM_MEDIUM.md
  locator: Full exact-identity historical report; claim-specific derivative scope
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: 'Full October 5 inventory report read: zero of five quantities source-checked.
    It is historical triage, not independent confirmation or a source raw capture.'
  snapshot_sha256: e892d40b9c10370198c449dde2e5a17a485ae6324feb52e0a0fb0a7107104e60
- evidence_id: report-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.md
  locator: Full exact-identity historical report; claim-specific derivative scope
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: 'Full October 5 inventory report read: zero of five quantities source-checked.
    It is historical triage, not independent confirmation or a source raw capture.'
  snapshot_sha256: d387717d0473b8e478ecedee62b26e5d87979d82b2b6509388e7693e59dc806a
- evidence_id: report-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/bm_medium.md
  locator: Full exact-identity historical report; claim-specific derivative scope
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: 'Full October 5 inventory report read: zero of five quantities source-checked.
    It is historical triage, not independent confirmation or a source raw capture.'
  snapshot_sha256: 8cbbc517e25befcfd28fe7da461eb16816c60c31506af4867f412c4b8e1c6a8f
- evidence_id: report-5
  kind: record_content
  reference: reports/yaml_record_review/20260921T230106Z-BM_MEDIUM.md
  locator: Full exact-identity historical report; claim-specific derivative scope
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: Full September ad hoc review read. Its primary-source observations and
    earlier source-access limits are historical context; its g/L interpretation is
    not adopted without final-volume support, and its then-unavailable provider does
    not override the separately captured current page.
  snapshot_sha256: 3a8847eecbc162baad6b31cadb217558bfdabe0e1d46e40a1fb4be6deb890b6f
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: CHEBI:15956 resolves to biotin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
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
- evidence_id: chebi17790
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17790
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:00:47.448030Z'
  support: supports
  summary: CHEBI:17790 resolves to methanol. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 9954cafff5982d415d5fbed82fa4630ac9958247ed636b3c770976752ebd50de
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:37.629610Z'
  support: supports
  summary: CHEBI:2509 resolves to agar. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-22T01:20:03Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15956":
    [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956",
    "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:17790": [{"label": "Methanol", "match_type": "preferred_term", "identifier":
    "CHEBI:17790", "preferred_term": "Methanol", "ontology_id": "CHEBI:17790", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type":
    "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BM_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml;
    data/normalized_yaml/bacterial/bm_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:57.003791"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml",
    "events": 6, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:57.003791"}]}, {"input": "data/normalized_yaml/bacterial/bm_medium.yaml",
    "events": 5, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: Read the full formulation guard, relevant merge_group and resolver composition-copy
    functions. Current code gives mechanism context only; the scientific-formulation
    equality guard does not establish which historical transformation produced these
    rates. No universal present-merger fault is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: Read the full formulation guard, relevant merge_group and resolver composition-copy
    functions. Current code gives mechanism context only; the scientific-formulation
    equality guard does not establish which historical transformation produced these
    rates. No universal present-merger fault is inferred.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: Read the full formulation guard, relevant merge_group and resolver composition-copy
    functions. Current code gives mechanism context only; the scientific-formulation
    equality guard does not establish which historical transformation produced these
    rates. No universal present-merger fault is inferred.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch044/438/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T01:20:03Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 4adcc4e57339f60edeed01190cb11386d1b65bad7561b2b88a96019739283c62
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003929
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact maintained contributors and source identity
  outcome: supported
  summary: The target has the exact KOMODO1192 and DSM1192 maintained contributors.
    Both owners and target share all five ingredients and rates; the source-duplicate
    relationship is locally reciprocal. Exact medium-number identity supports comparison,
    not equivalence of the current expanded provider page and the collection recipe.
  target_ids:
  - CultureMech:003929
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - id-search
  - primary
  - catalogue
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '4 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 4/5 primary
    and 4/5 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:003929
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi15956
  - chebi176843
  - chebi17790
  - chebi2509
  details: 'Instance coverage on a 0–100 percent scale, denominator 5: primary 80.00%;
    secondary 80.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: forms
  area: grounding
  topic: All four asserted chemicals and commercial base identity
  outcome: supported
  summary: Biotin CHEBI15956 has the biotin stereochemistry and D-biotin synonyms;
    the unqualified primary name gives no contrary stereoisomer. CHEBI176843 is the
    vitamin B12 class, compatible with the unspecific primary name without choosing
    a vitamer. CHEBI17790 is methanol and CHEBI2509 is agar. None supplies a liquid
    density or final-volume basis. Difco marine broth is explicitly Difco2216 in the
    primary and remains a commercial complex base; the current provider expansion
    is not adopted as its verified manufacturer composition.
  target_ids:
  - CultureMech:003929
  evidence_ids:
  - primary
  - provider
  - chebi15956
  - chebi176843
  - chebi17790
  - chebi2509
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 19 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003929
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: preparation-growth
  area: scope
  topic: Preparation, conditions, classification and growth limits
  outcome: unknown
  summary: The complete primary contains only the formulation table. No sterilization
    cycle, pH, temperature, oxygen requirement or strain-level growth is established.
    No target_organisms or growth metrics are asserted locally. Complex/undefined
    composition is appropriate to the commercial broth; the optional agar note is
    retained and the fixed solid classification needs a branch decision. The current
    provider Aerobic=false flag is not biological evidence.
  target_ids:
  - CultureMech:003929
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
- assessment_id: traceability
  area: evidence
  topic: Source linkage and historic provider basis
  outcome: concern
  summary: No quantity evidence is attached to the five concentrations in any of the
    three layers. The two historical derivative reports agree on a provider-normalized
    methanol value, but are not two independent raw-source authentications. Current
    primary batch quantities and current provider composition are kept distinct.
  target_ids:
  - CultureMech:003929
  evidence_ids:
  - primary
  - provider
  - api1192-attempt
  - report-0
  - report-1
  - report-2
  - report-3
  - report-4
  - report-5
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 17 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003929
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Difco marine broth\
    \ (Difco 2216)\",\n    \"stage\": \"DSM1192 printed batch; data/merge_yaml/merged/BM_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BM_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"37.4\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n   \
    \ \"desired\": {\n      \"printed_batch_amount\": 37.4,\n      \"unit\": \"g\"\
    ,\n      \"final_volume\": \"not declared\"\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsm1192\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\",\n       \
    \ \"source_locator\": \"Page 1 recipe row: Difco marine broth\",\n        \"exact_source_quote\"\
    : \" Difco marine broth (Difco 2216)           37.4    g\",\n        \"snapshot_sha256\"\
    : \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\",\n    \
    \    \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer.\"\n  },\n  {\n    \"decision_id\"\
    : \"q2\",\n    \"name\": \"Biotin\",\n    \"stage\": \"DSM1192 printed batch;\
    \ data/merge_yaml/merged/BM_MEDIUM.yaml\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2e-05\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 20,\n\
    \      \"unit\": \"µg\",\n      \"final_volume\": \"not declared\"\n    },\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsm1192\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\"\
    ,\n        \"source_locator\": \"Page 1 recipe row: Biotin\",\n        \"exact_source_quote\"\
    : \" Biotin                                    20.0   µg\",\n        \"snapshot_sha256\"\
    : \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\",\n    \
    \    \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer. The exact unit conversion is 20\
    \ µg = 0.000020 g; that arithmetic alone does not establish the denominator.\"\
    \n  },\n  {\n    \"decision_id\": \"q3\",\n    \"name\": \"Vitamin B12\",\n  \
    \  \"stage\": \"DSM1192 printed batch; data/merge_yaml/merged/BM_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BM_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1e-06\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n  \
    \  \"desired\": {\n      \"printed_batch_amount\": 1,\n      \"unit\": \"µg\"\
    ,\n      \"final_volume\": \"not declared\"\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsm1192\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\",\n       \
    \ \"source_locator\": \"Page 1 recipe row: Vitamin B12\",\n        \"exact_source_quote\"\
    : \" Vitamin B12                                1.0   µg\",\n        \"snapshot_sha256\"\
    : \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\",\n    \
    \    \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer. The exact unit conversion is 1\
    \ µg = 0.000001 g; that arithmetic alone does not establish the denominator.\"\
    \n  },\n  {\n    \"decision_id\": \"q4\",\n    \"name\": \"Methanol\",\n    \"\
    stage\": \"DSM1192 printed batch; data/merge_yaml/merged/BM_MEDIUM.yaml\",\n \
    \   \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/BM_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"3.168\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n  \
    \  \"desired\": {\n      \"printed_batch_amount\": 4,\n      \"unit\": \"ml\"\
    ,\n      \"final_volume\": \"not declared\"\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsm1192\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\",\n       \
    \ \"source_locator\": \"Page 1 recipe row: Methanol\",\n        \"exact_source_quote\"\
    : \" Methanol                                   4.0   ml\",\n        \"snapshot_sha256\"\
    : \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\",\n    \
    \    \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      },\n      {\n        \"historical_report\": \"reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/bm_medium.yaml.md\"\
    ,\n        \"snapshot_sha256\": \"5991fc14bc42c3f7ec1937c308aaa71458509ccf28b2fb8f3afecb282e8138c3\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1192\",\n \
    \       \"source_locator\": \"Historical report source.data.solutions[0].recipe\
    \ methanol row\",\n        \"historical_raw_sha256\": \"711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182\"\
    ,\n        \"historical_accessed_at\": \"2026-10-07T13:18:36.667926Z\",\n    \
    \    \"reported_amount\": {\n          \"amount\": 4,\n          \"unit\": \"\
    ml\",\n          \"g_l\": 3.168,\n          \"mmol_l\": 98.8702\n        },\n\
    \        \"limit\": \"Derivative report object only; exact cited raw unavailable.\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer. The historical reports explicitly\
    \ preserve provider g_l=3.168 for amount 4 ml, so the value is not unsupported\
    \ by all historical documentation. Their cited raw is unrecovered; the current\
    \ KOMODO mass cell is null. No density, concentration or volume conversion is\
    \ inferred from those derivative rows.\"\n  },\n  {\n    \"decision_id\": \"q5\"\
    ,\n    \"name\": \"Agar, optional\",\n    \"stage\": \"DSM1192 printed batch;\
    \ data/merge_yaml/merged/BM_MEDIUM.yaml\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 15,\n  \
    \    \"unit\": \"g\",\n      \"final_volume\": \"not declared\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm1192\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\"\
    ,\n        \"source_locator\": \"Page 1 recipe row: (Agar, if necessary\",\n \
    \       \"exact_source_quote\": \" (Agar, if necessary                       15.0\
    \   g)\",\n        \"snapshot_sha256\": \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\"\
    ,\n        \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer. The existing note already preserves\
    \ if necessary. Fifteen grams applies only to the agar branch; no mandatory agar\
    \ addition or fixed 15 g/L claim is established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q6\",\n    \"name\": \"Difco marine broth (Difco 2216)\",\n    \"stage\":\
    \ \"DSM1192 printed batch; data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"37.4\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 37.4,\n\
    \      \"unit\": \"g\",\n      \"final_volume\": \"not declared\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsm1192\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\"\
    ,\n        \"source_locator\": \"Page 1 recipe row: Difco marine broth\",\n  \
    \      \"exact_source_quote\": \" Difco marine broth (Difco 2216)           37.4\
    \    g\",\n        \"snapshot_sha256\": \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\"\
    ,\n        \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer.\"\n  },\n  {\n    \"decision_id\"\
    : \"q7\",\n    \"name\": \"Biotin\",\n    \"stage\": \"DSM1192 printed batch;\
    \ data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2e-05\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 20,\n\
    \      \"unit\": \"µg\",\n      \"final_volume\": \"not declared\"\n    },\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsm1192\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\"\
    ,\n        \"source_locator\": \"Page 1 recipe row: Biotin\",\n        \"exact_source_quote\"\
    : \" Biotin                                    20.0   µg\",\n        \"snapshot_sha256\"\
    : \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\",\n    \
    \    \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer. The exact unit conversion is 20\
    \ µg = 0.000020 g; that arithmetic alone does not establish the denominator.\"\
    \n  },\n  {\n    \"decision_id\": \"q8\",\n    \"name\": \"Vitamin B12\",\n  \
    \  \"stage\": \"DSM1192 printed batch; data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1e-06\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 1,\n\
    \      \"unit\": \"µg\",\n      \"final_volume\": \"not declared\"\n    },\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsm1192\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\"\
    ,\n        \"source_locator\": \"Page 1 recipe row: Vitamin B12\",\n        \"\
    exact_source_quote\": \" Vitamin B12                                1.0   µg\"\
    ,\n        \"snapshot_sha256\": \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\"\
    ,\n        \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer. The exact unit conversion is 1\
    \ µg = 0.000001 g; that arithmetic alone does not establish the denominator.\"\
    \n  },\n  {\n    \"decision_id\": \"q9\",\n    \"name\": \"Methanol\",\n    \"\
    stage\": \"DSM1192 printed batch; data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.168\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 4,\n\
    \      \"unit\": \"ml\",\n      \"final_volume\": \"not declared\"\n    },\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsm1192\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\"\
    ,\n        \"source_locator\": \"Page 1 recipe row: Methanol\",\n        \"exact_source_quote\"\
    : \" Methanol                                   4.0   ml\",\n        \"snapshot_sha256\"\
    : \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\",\n    \
    \    \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      },\n      {\n        \"historical_report\": \"reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/bm_medium.yaml.md\"\
    ,\n        \"snapshot_sha256\": \"5991fc14bc42c3f7ec1937c308aaa71458509ccf28b2fb8f3afecb282e8138c3\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1192\",\n \
    \       \"source_locator\": \"Historical report source.data.solutions[0].recipe\
    \ methanol row\",\n        \"historical_raw_sha256\": \"711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182\"\
    ,\n        \"historical_accessed_at\": \"2026-10-07T13:18:36.667926Z\",\n    \
    \    \"reported_amount\": {\n          \"amount\": 4,\n          \"unit\": \"\
    ml\",\n          \"g_l\": 3.168,\n          \"mmol_l\": 98.8702\n        },\n\
    \        \"limit\": \"Derivative report object only; exact cited raw unavailable.\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer. The historical reports explicitly\
    \ preserve provider g_l=3.168 for amount 4 ml, so the value is not unsupported\
    \ by all historical documentation. Their cited raw is unrecovered; the current\
    \ KOMODO mass cell is null. No density, concentration or volume conversion is\
    \ inferred from those derivative rows.\"\n  },\n  {\n    \"decision_id\": \"q10\"\
    ,\n    \"name\": \"Agar, optional\",\n    \"stage\": \"DSM1192 printed batch;\
    \ data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 15,\n  \
    \    \"unit\": \"g\",\n      \"final_volume\": \"not declared\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm1192\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\"\
    ,\n        \"source_locator\": \"Page 1 recipe row: (Agar, if necessary\",\n \
    \       \"exact_source_quote\": \" (Agar, if necessary                       15.0\
    \   g)\",\n        \"snapshot_sha256\": \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\"\
    ,\n        \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer. The existing note already preserves\
    \ if necessary. Fifteen grams applies only to the agar branch; no mandatory agar\
    \ addition or fixed 15 g/L claim is established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q11\",\n    \"name\": \"Difco marine broth (Difco 2216)\",\n    \"stage\"\
    : \"DSM1192 printed batch; data/normalized_yaml/bacterial/bm_medium.yaml\",\n\
    \    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bm_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"37.4\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n   \
    \ \"desired\": {\n      \"printed_batch_amount\": 37.4,\n      \"unit\": \"g\"\
    ,\n      \"final_volume\": \"not declared\"\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsm1192\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\",\n       \
    \ \"source_locator\": \"Page 1 recipe row: Difco marine broth\",\n        \"exact_source_quote\"\
    : \" Difco marine broth (Difco 2216)           37.4    g\",\n        \"snapshot_sha256\"\
    : \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\",\n    \
    \    \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer.\"\n  },\n  {\n    \"decision_id\"\
    : \"q12\",\n    \"name\": \"Biotin\",\n    \"stage\": \"DSM1192 printed batch;\
    \ data/normalized_yaml/bacterial/bm_medium.yaml\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bm_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2e-05\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 20,\n\
    \      \"unit\": \"µg\",\n      \"final_volume\": \"not declared\"\n    },\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsm1192\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\"\
    ,\n        \"source_locator\": \"Page 1 recipe row: Biotin\",\n        \"exact_source_quote\"\
    : \" Biotin                                    20.0   µg\",\n        \"snapshot_sha256\"\
    : \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\",\n    \
    \    \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer. The exact unit conversion is 20\
    \ µg = 0.000020 g; that arithmetic alone does not establish the denominator.\"\
    \n  },\n  {\n    \"decision_id\": \"q13\",\n    \"name\": \"Vitamin B12\",\n \
    \   \"stage\": \"DSM1192 printed batch; data/normalized_yaml/bacterial/bm_medium.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/bm_medium.yaml\",\n        \"\
    field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1e-06\",\n          \"unit\": \"G_PER_L\"\n        }\n    \
    \  }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 1,\n      \"\
    unit\": \"µg\",\n      \"final_volume\": \"not declared\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsm1192\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\",\n       \
    \ \"source_locator\": \"Page 1 recipe row: Vitamin B12\",\n        \"exact_source_quote\"\
    : \" Vitamin B12                                1.0   µg\",\n        \"snapshot_sha256\"\
    : \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\",\n    \
    \    \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer. The exact unit conversion is 1\
    \ µg = 0.000001 g; that arithmetic alone does not establish the denominator.\"\
    \n  },\n  {\n    \"decision_id\": \"q14\",\n    \"name\": \"Methanol\",\n    \"\
    stage\": \"DSM1192 printed batch; data/normalized_yaml/bacterial/bm_medium.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/bm_medium.yaml\",\n        \"\
    field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"3.168\",\n          \"unit\": \"G_PER_L\"\n        }\n    \
    \  }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 4,\n      \"\
    unit\": \"ml\",\n      \"final_volume\": \"not declared\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsm1192\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\",\n       \
    \ \"source_locator\": \"Page 1 recipe row: Methanol\",\n        \"exact_source_quote\"\
    : \" Methanol                                   4.0   ml\",\n        \"snapshot_sha256\"\
    : \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\",\n    \
    \    \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      },\n      {\n        \"historical_report\": \"reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/bm_medium.yaml.md\"\
    ,\n        \"snapshot_sha256\": \"5991fc14bc42c3f7ec1937c308aaa71458509ccf28b2fb8f3afecb282e8138c3\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1192\",\n \
    \       \"source_locator\": \"Historical report source.data.solutions[0].recipe\
    \ methanol row\",\n        \"historical_raw_sha256\": \"711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182\"\
    ,\n        \"historical_accessed_at\": \"2026-10-07T13:18:36.667926Z\",\n    \
    \    \"reported_amount\": {\n          \"amount\": 4,\n          \"unit\": \"\
    ml\",\n          \"g_l\": 3.168,\n          \"mmol_l\": 98.8702\n        },\n\
    \        \"limit\": \"Derivative report object only; exact cited raw unavailable.\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer. The historical reports explicitly\
    \ preserve provider g_l=3.168 for amount 4 ml, so the value is not unsupported\
    \ by all historical documentation. Their cited raw is unrecovered; the current\
    \ KOMODO mass cell is null. No density, concentration or volume conversion is\
    \ inferred from those derivative rows.\"\n  },\n  {\n    \"decision_id\": \"q15\"\
    ,\n    \"name\": \"Agar, optional\",\n    \"stage\": \"DSM1192 printed batch;\
    \ data/normalized_yaml/bacterial/bm_medium.yaml\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bm_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 15,\n  \
    \    \"unit\": \"g\",\n      \"final_volume\": \"not declared\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm1192\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\"\
    ,\n        \"source_locator\": \"Page 1 recipe row: (Agar, if necessary\",\n \
    \       \"exact_source_quote\": \" (Agar, if necessary                       15.0\
    \   g)\",\n        \"snapshot_sha256\": \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\"\
    ,\n        \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary gives this batch addition,\
    \ with 1000 ml listed water rather than an explicit final-volume or make-up instruction.\
    \ The stored final-medium g/L basis is therefore unverified; retain the printed\
    \ amount and stage without treating listed water as measured final volume. No\
    \ quantity evidence is attached in this layer. The existing note already preserves\
    \ if necessary. Fifteen grams applies only to the agar branch; no mandatory agar\
    \ addition or fixed 15 g/L claim is established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q16\",\n    \"name\": \"Distilled water\",\n    \"stage\": \"Printed batch\
    \ solvent omitted from all three ingredient lists\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [],\n    \"desired\": {\n      \"batch_volume\": 1000,\n\
    \      \"unit\": \"ml\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"dsm1192\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\"\
    ,\n        \"source_locator\": \"Page 1 recipe row: Distilled water\",\n     \
    \   \"exact_source_quote\": \" Distilled water                         1000.0\
    \   ml\",\n        \"snapshot_sha256\": \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\"\
    ,\n        \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary directly lists 1000 ml\
    \ water. Add only as a batch solvent after source-scoped curation; do not turn\
    \ it into 1000 g/L or a final-volume declaration.\"\n  },\n  {\n    \"decision_id\"\
    : \"q17\",\n    \"name\": \"Optional agar branch and physical state\",\n    \"\
    stage\": \"Broth versus optional solid branch\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"physical_state\",\n        \"stored\": \"SOLID_AGAR\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"physical_state\",\n        \"stored\": \"SOLID_AGAR\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bm_medium.yaml\"\
    ,\n        \"field_path\": \"physical_state\",\n        \"stored\": \"SOLID_AGAR\"\
    \n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \" (if\
    \ necessary)\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \" (if\
    \ necessary)\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bm_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \" (if\
    \ necessary)\"\n      }\n    ],\n    \"desired\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsm1192\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf\",\n       \
    \ \"source_locator\": \"Page 1 recipe row: (Agar, if necessary\",\n        \"\
    exact_source_quote\": \" (Agar, if necessary                       15.0   g)\"\
    ,\n        \"snapshot_sha256\": \"52ad908bbf2d5f31a534483795166c7051c67d848215f2c478be13b598332241\"\
    ,\n        \"parsed_text_sha256\": \"c3d15cc89dbb1af9c0e1356c5f31340b95ce0333e6d6bec818dca180f70f648a\"\
    \n      }\n    ],\n    \"interpretation\": \"All layers already retain the optional\
    \ agar note, but their SOLID_AGAR classification selects the solid branch. Clarify\
    \ the represented variant before regeneration; the primary permits an agar-free\
    \ branch and supplies no culture-specific rule for choosing it.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.003929.quantity-basis-and-solvent
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Batch quantities lack a verified final-medium basis and solvent representation
  description: All five local concentrations use g/L, while DSM1192 lists batch masses,
    methanol 4 ml and water 1000 ml without a final-volume declaration. Water is absent.
    Historical API-derived reports explicitly support the origin of 3.168 g/L as a
    provider declaration, but the cited raw is unrecovered and current KOMODO mass
    is null. This is an unresolved basis/conversion issue, not proof that every stored
    mass is numerically false.
  target_ids:
  - CultureMech:003929
  field_paths:
  - ingredients
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - api1192-attempt
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: culturemech.003929.optional-agar-variant
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: The optional agar branch needs explicit representation
  description: The primary permits agar only if necessary. Every layer retains that
    note, so optionality has not disappeared, but every top-level physical_state is
    SOLID_AGAR without a declared branch selection.
  target_ids:
  - CultureMech:003929
  field_paths:
  - physical_state
  - ingredients[4].notes
  evidence_ids:
  - primary
  - record
  - owner-0
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.003929.amount-traceability
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Current quantities have no attached claim-level evidence
  description: All three scientific layers omit attached evidence for their five quantity
    assertions. Earlier reports preserve useful but bounded source statements outside
    the active ingredients.
  target_ids:
  - CultureMech:003929
  field_paths:
  - ingredients
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: 'P4.3 is a minor traceability exception: adding reliable claim
    linkage is separate from the major unresolved quantity basis and does not itself
    establish a new numerical correction.'
- finding_id: f4
  issue_key: culturemech.003929.history-timestamps
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO-derived history includes malformed and timezone-naive timestamps
  description: The KOMODO owner and target retain 2026-01-27T01:15:01.fZ and a timezone-naive
    February 3 timestamp. The DSM owner timestamps are valid. Historical timing cannot
    be silently repaired by guessing an offset.
  target_ids:
  - CultureMech:003929
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  evidence_ids:
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml
    role: authoritative normalized source
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4.3 is minor because malformed historical timing impedes
    traceability while leaving the current formulation bytes unchanged; no source
    amount or scientific date is inferred.
actions:
- action_id: a1
  description: Curate the exact printed batch and solvent, recover the historical
    provider calculation if possible, and document any final-volume and methanol conversion
    basis before asserting final-medium rates. Preserve provider and collection variants
    separately.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003929
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bm_medium.yaml
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
  description: Retain the existing optionality and explicitly represent the selected
    solid or broth variant before changing state or amounts. Do not silently remove
    agar or call it mandatory.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003929
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bm_medium.yaml
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
  description: After resolving the basis, attach short exact quotations and source
    version/hash, original units, stage and calculation separately. Preserve the historical
    reports and failed current API attempt.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003929
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bm_medium.yaml
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
  description: Preserve the original events and append an authorized provenance clarification
    if the original timing can be recovered; limit remediation to the affected KOMODO
    lineage before regeneration.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003929
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml
    role: authoritative normalized source
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
- The current exact MediaDive REST1192 request returned HTTP 503. The cited historical
  raw digest 711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182 was
  not recovered in the bounded captured surfaces. Historical report objects remain
  derivative, so their g_l declaration cannot be independently authenticated here.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-044
- generated-medium
```
