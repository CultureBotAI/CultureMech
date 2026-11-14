# Scientific review of chloroflexus_aggregans_medium

- Review: 20261028T090556Z-chloroflexus-aggregans-medium-batch061
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T08:33:15.477685Z
- Finished UTC: 2026-10-28T09:05:56.857631Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The valid DSM 87a record needs source-branch reconciliation and full stock-stage reconstruction. Correct basal provider rates, five-component owner nesting and explicit CA doses are credited. Fe solution units, flattened stocks, missing generated preparation and nickel hydrate linkage require curation; exact KOMODO and strain-variant support remains unresolved.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch061 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006721 | data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml | generated | chloroflexus_aggregans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006721 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:006721 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:006721 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:006721 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Base, supplement and strain identities

identity: concern. Targets: CultureMech:006721.

The selected DSM 87a identity is valid, but source 87, source 87a and the unverified strain-13941 modifier are not proven duplicates. DSM 87a explicitly adds CA to 87. Current owners copied the same ingredient signature, then three gained a partial CA repair; similarity and copied history are not independent equivalence evidence.

### Existing repairs and retained preparation

completeness: concern. Targets: CultureMech:006721.

Three maintained owners already nest five CA components, and the two base-87a owners assert the correct 1 ML_PER_L dose. The strain owner keeps the dose candidate unasserted. Four CA components, all seven SL-6 components and sulfide remain flat; the target drops all nested stocks and DSM preparation. Preserve these correct partial repairs.

### Collection instructions versus growth claims

evidence: unknown. Targets: CultureMech:006721.

The primary sheets prescribe conditions but do not supply a reviewed experiment for strain DSM 13941 or independently establish the collection references 3365/3366. No strain-specific growth claim is added.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:006721.

All ten exact historical reports and current histories were read. Current API 87a bytes authenticate matching October excerpts; API 87 raw differs, with the sulfide object now adding g_l and mmol_l. Historical blanket conflict labels do not invalidate correctly retained basal provider rates or nested stock values. The separate KOMODO catalogue and exact variant remain unavailable. Stored .fZ timestamps are malformed and must remain as original events. All historical API excerpts with matching current raw digests are independently authenticated in historical-authentication.json. Matching bytes do not verify old execution or the separate KOMODO catalogue. Current MediaDive code separates stock additions but gathers all solution preparation into a root list; current conservative merging preserves scientific fields and rejects incompatible formulations. Those present behaviors do not prove how the old generated records were produced.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:006721.

All 132 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{
  "schema": "private explicit quantity decisions v1",
  "target_id": "CultureMech:006721",
  "selected_concentration_field_count": 132,
  "selected_concentration_fields_covered": 132,
  "decisions": [
    {
      "decision_id": "q1",
      "subject": "Yeast extract in selected and base-87a layers",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[0].concentration",
          "original": {
            "value": "0.952381",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[0].concentration",
          "original": {
            "value": "0.952381",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[0].concentration",
          "original": {
            "value": "0.952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Basal medium; provider-declared normalization",
      "interpretation": "The stored value exactly matches current API 87a g_l on its declared 1050 ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured final volume is stated. Retain the supplied hydrate and the current scalar with an explicit provider basis, without claiming that listed water is final volume. The copied KOMODO layer does not independently authenticate its unavailable provider page.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[0]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.952381,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 4-4",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Yeast extract                                                     1.00        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q2",
      "subject": "Yeast extract in KOMODO 87 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[0].concentration",
          "original": {
            "value": "0.952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source-87 branch",
      "interpretation": "This copied scalar follows API 87a, while current API 87 uses a declared 1056 ml normalization. Both primary absolute masses are the same. This does not justify replacing the KOMODO scalar with API 87 arithmetic without verifying the exact unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[0]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.952381,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 4-4",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Yeast extract                                                     1.00        g",
          "quote_representation": "captured extracted text"
        },
        {
          "locator": "$.data.solutions[0].recipe[0]",
          "source_key": "api87",
          "reference": "https://mediadive.dsmz.de/rest/medium/87",
          "source_raw_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "source_text_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "accessed_at": "2026-10-28T08:33:55.974764Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.94697,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q3",
      "subject": "Yeast extract in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[0].concentration",
          "original": {
            "value": "0.952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved strain variant",
      "interpretation": "The stored scalar matches base 87a, but the variant recipe remains unavailable. Base-source agreement is contextual and does not authenticate an unknown strain modification or final-volume basis.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[0]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.952381,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 4-4",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Yeast extract                                                     1.00        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q4",
      "subject": "Glycyl-glycine in selected and base-87a layers",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[1].concentration",
          "original": {
            "value": "0.952381",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[1].concentration",
          "original": {
            "value": "0.952381",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[1].concentration",
          "original": {
            "value": "0.952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Basal medium; provider-declared normalization",
      "interpretation": "The stored value exactly matches current API 87a g_l on its declared 1050 ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured final volume is stated. Retain the supplied hydrate and the current scalar with an explicit provider basis, without claiming that listed water is final volume. The copied KOMODO layer does not independently authenticate its unavailable provider page.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Glycyl-glycine\",\n                        \"compound_id\": 192,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.952381,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 5-5",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Glycyl-glycine                                                    1.00        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q5",
      "subject": "Glycyl-glycine in KOMODO 87 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[1].concentration",
          "original": {
            "value": "0.952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source-87 branch",
      "interpretation": "This copied scalar follows API 87a, while current API 87 uses a declared 1056 ml normalization. Both primary absolute masses are the same. This does not justify replacing the KOMODO scalar with API 87 arithmetic without verifying the exact unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Glycyl-glycine\",\n                        \"compound_id\": 192,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.952381,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 5-5",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Glycyl-glycine                                                    1.00        g",
          "quote_representation": "captured extracted text"
        },
        {
          "locator": "$.data.solutions[0].recipe[1]",
          "source_key": "api87",
          "reference": "https://mediadive.dsmz.de/rest/medium/87",
          "source_raw_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "source_text_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "accessed_at": "2026-10-28T08:33:55.974764Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Glycyl-glycine\",\n                        \"compound_id\": 192,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.94697,\n                        \"mmol_l\": 7.16761,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q6",
      "subject": "Glycyl-glycine in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[1].concentration",
          "original": {
            "value": "0.952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved strain variant",
      "interpretation": "The stored scalar matches base 87a, but the variant recipe remains unavailable. Base-source agreement is contextual and does not authenticate an unknown strain modification or final-volume basis.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Glycyl-glycine\",\n                        \"compound_id\": 192,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.952381,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 5-5",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Glycyl-glycine                                                    1.00        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q7",
      "subject": "Na2HPO4 x 2 H2O in selected and base-87a layers",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[2].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[2].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[2].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Basal medium; provider-declared normalization",
      "interpretation": "The stored value exactly matches current API 87a g_l on its declared 1050 ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured final volume is stated. Retain the supplied hydrate and the current scalar with an explicit provider basis, without claiming that listed water is final volume. The copied KOMODO layer does not independently authenticate its unavailable provider page.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[2]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2HPO4 x 2 H2O\",\n                        \"compound_id\": 181,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0952381,\n                        \"mmol_l\": 0.670884,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 6-6",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Na2HPO4 x 2 H2O                                                   0.10        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q8",
      "subject": "Na2HPO4 x 2 H2O in KOMODO 87 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[2].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source-87 branch",
      "interpretation": "This copied scalar follows API 87a, while current API 87 uses a declared 1056 ml normalization. Both primary absolute masses are the same. This does not justify replacing the KOMODO scalar with API 87 arithmetic without verifying the exact unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[2]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2HPO4 x 2 H2O\",\n                        \"compound_id\": 181,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0952381,\n                        \"mmol_l\": 0.670884,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 6-6",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Na2HPO4 x 2 H2O                                                   0.10        g",
          "quote_representation": "captured extracted text"
        },
        {
          "locator": "$.data.solutions[0].recipe[2]",
          "source_key": "api87",
          "reference": "https://mediadive.dsmz.de/rest/medium/87",
          "source_raw_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "source_text_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "accessed_at": "2026-10-28T08:33:55.974764Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2HPO4 x 2 H2O\",\n                        \"compound_id\": 181,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.094697,\n                        \"mmol_l\": 0.667073,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q9",
      "subject": "Na2HPO4 x 2 H2O in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[2].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved strain variant",
      "interpretation": "The stored scalar matches base 87a, but the variant recipe remains unavailable. Base-source agreement is contextual and does not authenticate an unknown strain modification or final-volume basis.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[2]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2HPO4 x 2 H2O\",\n                        \"compound_id\": 181,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0952381,\n                        \"mmol_l\": 0.670884,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 6-6",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Na2HPO4 x 2 H2O                                                   0.10        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q10",
      "subject": "MgSO4 x 7 H2O in selected and base-87a layers",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[3].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[3].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[3].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Basal medium; provider-declared normalization",
      "interpretation": "The stored value exactly matches current API 87a g_l on its declared 1050 ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured final volume is stated. Retain the supplied hydrate and the current scalar with an explicit provider basis, without claiming that listed water is final volume. The copied KOMODO layer does not independently authenticate its unavailable provider page.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[3]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0952381,\n                        \"mmol_l\": 0.386399,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 7-7",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "MgSO4 x 7 H2O                                                     0.10        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q11",
      "subject": "MgSO4 x 7 H2O in KOMODO 87 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[3].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source-87 branch",
      "interpretation": "This copied scalar follows API 87a, while current API 87 uses a declared 1056 ml normalization. Both primary absolute masses are the same. This does not justify replacing the KOMODO scalar with API 87 arithmetic without verifying the exact unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[3]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0952381,\n                        \"mmol_l\": 0.386399,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 7-7",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "MgSO4 x 7 H2O                                                     0.10        g",
          "quote_representation": "captured extracted text"
        },
        {
          "locator": "$.data.solutions[0].recipe[3]",
          "source_key": "api87",
          "reference": "https://mediadive.dsmz.de/rest/medium/87",
          "source_raw_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "source_text_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "accessed_at": "2026-10-28T08:33:55.974764Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.094697,\n                        \"mmol_l\": 0.384204,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q12",
      "subject": "MgSO4 x 7 H2O in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[3].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved strain variant",
      "interpretation": "The stored scalar matches base 87a, but the variant recipe remains unavailable. Base-source agreement is contextual and does not authenticate an unknown strain modification or final-volume basis.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[3]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0952381,\n                        \"mmol_l\": 0.386399,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 7-7",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "MgSO4 x 7 H2O                                                     0.10        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q13",
      "subject": "KNO3 in selected and base-87a layers",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[4].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[4].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[4].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Basal medium; provider-declared normalization",
      "interpretation": "The stored value exactly matches current API 87a g_l on its declared 1050 ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured final volume is stated. Retain the supplied hydrate and the current scalar with an explicit provider basis, without claiming that listed water is final volume. The copied KOMODO layer does not independently authenticate its unavailable provider page.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[4]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0952381,\n                        \"mmol_l\": 0.941991,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 8-8",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "KNO3                                                              0.10        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q14",
      "subject": "KNO3 in KOMODO 87 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[4].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source-87 branch",
      "interpretation": "This copied scalar follows API 87a, while current API 87 uses a declared 1056 ml normalization. Both primary absolute masses are the same. This does not justify replacing the KOMODO scalar with API 87 arithmetic without verifying the exact unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[4]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0952381,\n                        \"mmol_l\": 0.941991,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 8-8",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "KNO3                                                              0.10        g",
          "quote_representation": "captured extracted text"
        },
        {
          "locator": "$.data.solutions[0].recipe[4]",
          "source_key": "api87",
          "reference": "https://mediadive.dsmz.de/rest/medium/87",
          "source_raw_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "source_text_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "accessed_at": "2026-10-28T08:33:55.974764Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.094697,\n                        \"mmol_l\": 0.936639,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q15",
      "subject": "KNO3 in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[4].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved strain variant",
      "interpretation": "The stored scalar matches base 87a, but the variant recipe remains unavailable. Base-source agreement is contextual and does not authenticate an unknown strain modification or final-volume basis.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[4]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0952381,\n                        \"mmol_l\": 0.941991,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 8-8",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "KNO3                                                              0.10        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q16",
      "subject": "NaNO3 in selected and base-87a layers",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[5].concentration",
          "original": {
            "value": "0.47619",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[5].concentration",
          "original": {
            "value": "0.47619",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[5].concentration",
          "original": {
            "value": "0.47619",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Basal medium; provider-declared normalization",
      "interpretation": "The stored value exactly matches current API 87a g_l on its declared 1050 ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured final volume is stated. Retain the supplied hydrate and the current scalar with an explicit provider basis, without claiming that listed water is final volume. The copied KOMODO layer does not independently authenticate its unavailable provider page.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[5]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\": 187,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.47619,\n                        \"mmol_l\": 5.60257,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 9-9",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "NaNO3                                                             0.50        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q17",
      "subject": "NaNO3 in KOMODO 87 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[5].concentration",
          "original": {
            "value": "0.47619",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source-87 branch",
      "interpretation": "This copied scalar follows API 87a, while current API 87 uses a declared 1056 ml normalization. Both primary absolute masses are the same. This does not justify replacing the KOMODO scalar with API 87 arithmetic without verifying the exact unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[5]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\": 187,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.47619,\n                        \"mmol_l\": 5.60257,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 9-9",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "NaNO3                                                             0.50        g",
          "quote_representation": "captured extracted text"
        },
        {
          "locator": "$.data.solutions[0].recipe[5]",
          "source_key": "api87",
          "reference": "https://mediadive.dsmz.de/rest/medium/87",
          "source_raw_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "source_text_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "accessed_at": "2026-10-28T08:33:55.974764Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\": 187,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.473485,\n                        \"mmol_l\": 5.57074,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q18",
      "subject": "NaNO3 in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[5].concentration",
          "original": {
            "value": "0.47619",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved strain variant",
      "interpretation": "The stored scalar matches base 87a, but the variant recipe remains unavailable. Base-source agreement is contextual and does not authenticate an unknown strain modification or final-volume basis.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[5]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\": 187,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.47619,\n                        \"mmol_l\": 5.60257,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 9-9",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "NaNO3                                                             0.50        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q19",
      "subject": "NaCl in selected and base-87a layers",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[6].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[6].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[6].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Basal medium; provider-declared normalization",
      "interpretation": "The stored value exactly matches current API 87a g_l on its declared 1050 ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured final volume is stated. Retain the supplied hydrate and the current scalar with an explicit provider basis, without claiming that listed water is final volume. The copied KOMODO layer does not independently authenticate its unavailable provider page.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[6]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0952381,\n                        \"mmol_l\": 1.62967,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 10-10",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "NaCl                                                              0.10        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q20",
      "subject": "NaCl in KOMODO 87 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[6].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source-87 branch",
      "interpretation": "This copied scalar follows API 87a, while current API 87 uses a declared 1056 ml normalization. Both primary absolute masses are the same. This does not justify replacing the KOMODO scalar with API 87 arithmetic without verifying the exact unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[6]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0952381,\n                        \"mmol_l\": 1.62967,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 10-10",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "NaCl                                                              0.10        g",
          "quote_representation": "captured extracted text"
        },
        {
          "locator": "$.data.solutions[0].recipe[6]",
          "source_key": "api87",
          "reference": "https://mediadive.dsmz.de/rest/medium/87",
          "source_raw_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "source_text_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "accessed_at": "2026-10-28T08:33:55.974764Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.094697,\n                        \"mmol_l\": 1.62041,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q21",
      "subject": "NaCl in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[6].concentration",
          "original": {
            "value": "0.0952381",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved strain variant",
      "interpretation": "The stored scalar matches base 87a, but the variant recipe remains unavailable. Base-source agreement is contextual and does not authenticate an unknown strain modification or final-volume basis.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[6]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0952381,\n                        \"mmol_l\": 1.62967,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 10-10",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "NaCl                                                              0.10        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q22",
      "subject": "CaCl2 x 2 H2O in selected and base-87a layers",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[7].concentration",
          "original": {
            "value": "0.047619",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[7].concentration",
          "original": {
            "value": "0.047619",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[7].concentration",
          "original": {
            "value": "0.047619",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Basal medium; provider-declared normalization",
      "interpretation": "The stored value exactly matches current API 87a g_l on its declared 1050 ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured final volume is stated. Retain the supplied hydrate and the current scalar with an explicit provider basis, without claiming that listed water is final volume. The copied KOMODO layer does not independently authenticate its unavailable provider page.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[7]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.047619,\n                        \"mmol_l\": 0.323906,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 11-11",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "CaCl2 x 2 H2O                                                     0.05        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q23",
      "subject": "CaCl2 x 2 H2O in KOMODO 87 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[7].concentration",
          "original": {
            "value": "0.047619",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source-87 branch",
      "interpretation": "This copied scalar follows API 87a, while current API 87 uses a declared 1056 ml normalization. Both primary absolute masses are the same. This does not justify replacing the KOMODO scalar with API 87 arithmetic without verifying the exact unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[7]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.047619,\n                        \"mmol_l\": 0.323906,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 11-11",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "CaCl2 x 2 H2O                                                     0.05        g",
          "quote_representation": "captured extracted text"
        },
        {
          "locator": "$.data.solutions[0].recipe[7]",
          "source_key": "api87",
          "reference": "https://mediadive.dsmz.de/rest/medium/87",
          "source_raw_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "source_text_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "accessed_at": "2026-10-28T08:33:55.974764Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0473485,\n                        \"mmol_l\": 0.322066,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q24",
      "subject": "CaCl2 x 2 H2O in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[7].concentration",
          "original": {
            "value": "0.047619",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved strain variant",
      "interpretation": "The stored scalar matches base 87a, but the variant recipe remains unavailable. Base-source agreement is contextual and does not authenticate an unknown strain modification or final-volume basis.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[7]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.047619,\n                        \"mmol_l\": 0.323906,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 11-11",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "CaCl2 x 2 H2O                                                     0.05        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q25",
      "subject": "Fe(III) citrate solution",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[8].concentration",
          "original": {
            "value": "5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[8].concentration",
          "original": {
            "value": "5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[8].concentration",
          "original": {
            "value": "5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[8].concentration",
          "original": {
            "value": "5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "Separate stock and receiving dose",
      "interpretation": "The source specifies 5 ml of solution prepared with 0.1 g in 100 ml water, not 5 g/L of Fe(III) citrate in the medium. Preserve the supplied complex identity and separate stock recipe from receiving batch dose. Do not infer a measured final volume or assert a final mass-per-litre conversion.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[8]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Fe(III) citrate\",\n                        \"compound_id\": 45,\n                        \"attribute\": \"0.1 g in 100 ml H2O\",\n                        \"amount\": 5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 12-13",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Fe(III) citrate solution\n(0.1 g in 100 ml H2O)                                             5.00      ml",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q26",
      "subject": "Fe(III) citrate in unresolved strain variant",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[8].concentration",
          "original": {
            "value": "5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Variant stock stage",
      "interpretation": "The base source demonstrates a stock/dose representation problem, but the exact variant cannot be reconstructed from a copied signature. Keep 5 G_PER_L unsupported rather than manufacture a variant-specific replacement.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[8]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Fe(III) citrate\",\n                        \"compound_id\": 45,\n                        \"attribute\": \"0.1 g in 100 ml H2O\",\n                        \"amount\": 5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q27",
      "subject": "Nicotinic acid flattened CA component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[9].concentration",
          "original": {
            "value": "1",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "Vitamin solution CA, not basal final concentration",
      "interpretation": "The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L value equals provider stock g_l, not the receiving-medium concentration. Restore the complete nine-component stock and retain the explicit 1 ml/litre receiving dose separately; do not infer a physical final stock volume merely from water.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 8.12282,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 8-8",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Nicotinic acid                                              100.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q28",
      "subject": "Nicotinic acid already nested CA component",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "solutions[0].composition[0].concentration",
          "original": {
            "value": "1",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "solutions[0].composition[0].concentration",
          "original": {
            "value": "1",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Already repaired stock composition",
      "interpretation": "The current owner correctly places this component under Vitamin solution CA and its value matches provider stock g_l. Credit this partial repair and preserve it while adding the four omitted CA components; do not flatten it again.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 8.12282,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 8-8",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Nicotinic acid                                              100.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q29",
      "subject": "Nicotinic acid in source-87 and strain-variant owners",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[9].concentration",
          "original": {
            "value": "1",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "solutions[0].composition[0].concentration",
          "original": {
            "value": "1",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source branches",
      "interpretation": "The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe is unavailable. These owner fields cannot be authenticated by base-87a stock membership alone. The strain owner already nests five components and retains its dose as a candidate; this useful uncertainty is preserved.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 8.12282,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 8-8",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Nicotinic acid                                              100.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q30",
      "subject": "Thiamine-HCl x 2 H2O flattened CA component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[10].concentration",
          "original": {
            "value": "1",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "Vitamin solution CA, not basal final concentration",
      "interpretation": "The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L value equals provider stock g_l, not the receiving-medium concentration. Restore the complete nine-component stock and retain the explicit 1 ml/litre receiving dose separately; do not infer a physical final stock volume merely from water.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[2]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 2.6788,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 9-9",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Thiamine-HCl x 2 H2O                                        100.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q31",
      "subject": "Thiamine-HCl x 2 H2O already nested CA component",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "solutions[0].composition[1].concentration",
          "original": {
            "value": "1",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "solutions[0].composition[1].concentration",
          "original": {
            "value": "1",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Already repaired stock composition",
      "interpretation": "The current owner correctly places this component under Vitamin solution CA and its value matches provider stock g_l. Credit this partial repair and preserve it while adding the four omitted CA components; do not flatten it again.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[2]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 2.6788,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 9-9",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Thiamine-HCl x 2 H2O                                        100.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q32",
      "subject": "Thiamine-HCl x 2 H2O in source-87 and strain-variant owners",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[10].concentration",
          "original": {
            "value": "1",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "solutions[0].composition[1].concentration",
          "original": {
            "value": "1",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source branches",
      "interpretation": "The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe is unavailable. These owner fields cannot be authenticated by base-87a stock membership alone. The strain owner already nests five components and retains its dose as a candidate; this useful uncertainty is preserved.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[2]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 2.6788,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 9-9",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Thiamine-HCl x 2 H2O                                        100.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q33",
      "subject": "Biotin flattened CA component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[11].concentration",
          "original": {
            "value": "0.05",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[9].concentration",
          "original": {
            "value": "0.05",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[9].concentration",
          "original": {
            "value": "0.05",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "Vitamin solution CA, not basal final concentration",
      "interpretation": "The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L value equals provider stock g_l, not the receiving-medium concentration. Restore the complete nine-component stock and retain the explicit 1 ml/litre receiving dose separately; do not infer a physical final stock volume merely from water.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[3]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.204658,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 10-10",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Biotin                                                        5.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q34",
      "subject": "Biotin in source-87 and strain-variant owners",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[11].concentration",
          "original": {
            "value": "0.05",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[9].concentration",
          "original": {
            "value": "0.05",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source branches",
      "interpretation": "The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe is unavailable. These owner fields cannot be authenticated by base-87a stock membership alone. The strain owner already nests five components and retains its dose as a candidate; this useful uncertainty is preserved.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[3]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.204658,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 10-10",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Biotin                                                        5.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q35",
      "subject": "p-Aminobenzoic acid flattened CA component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[12].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "Vitamin solution CA, not basal final concentration",
      "interpretation": "The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L value equals provider stock g_l, not the receiving-medium concentration. Restore the complete nine-component stock and retain the explicit 1 ml/litre receiving dose separately; do not infer a physical final stock volume merely from water.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[4]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 3.64591,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 11-11",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "p-Aminobenzoic acid                                          50.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q36",
      "subject": "p-Aminobenzoic acid already nested CA component",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "solutions[0].composition[2].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "solutions[0].composition[2].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Already repaired stock composition",
      "interpretation": "The current owner correctly places this component under Vitamin solution CA and its value matches provider stock g_l. Credit this partial repair and preserve it while adding the four omitted CA components; do not flatten it again.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[4]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 3.64591,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 11-11",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "p-Aminobenzoic acid                                          50.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q37",
      "subject": "p-Aminobenzoic acid in source-87 and strain-variant owners",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[12].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "solutions[0].composition[2].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source branches",
      "interpretation": "The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe is unavailable. These owner fields cannot be authenticated by base-87a stock membership alone. The strain owner already nests five components and retains its dose as a candidate; this useful uncertainty is preserved.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[4]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 3.64591,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 11-11",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "p-Aminobenzoic acid                                          50.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q38",
      "subject": "Vitamin B12 flattened CA component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[13].concentration",
          "original": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[10].concentration",
          "original": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[10].concentration",
          "original": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "Vitamin solution CA, not basal final concentration",
      "interpretation": "The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L value equals provider stock g_l, not the receiving-medium concentration. Restore the complete nine-component stock and retain the explicit 1 ml/litre receiving dose separately; do not infer a physical final stock volume merely from water.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[5]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0073779,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 12-12",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Vitamin B12                                                   1.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q39",
      "subject": "Vitamin B12 in source-87 and strain-variant owners",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[13].concentration",
          "original": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[10].concentration",
          "original": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source branches",
      "interpretation": "The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe is unavailable. These owner fields cannot be authenticated by base-87a stock membership alone. The strain owner already nests five components and retains its dose as a candidate; this useful uncertainty is preserved.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[5]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0073779,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 12-12",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Vitamin B12                                                   1.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q40",
      "subject": "Calcium pantothenate flattened CA component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[14].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[11].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[11].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "Vitamin solution CA, not basal final concentration",
      "interpretation": "The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L value equals provider stock g_l, not the receiving-medium concentration. Restore the complete nine-component stock and retain the explicit 1 ml/litre receiving dose separately; do not infer a physical final stock volume merely from water.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[6]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 1.04925,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 13-13",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Ca-pantothenate                                              50.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q41",
      "subject": "Calcium pantothenate in source-87 and strain-variant owners",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[14].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[11].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source branches",
      "interpretation": "The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe is unavailable. These owner fields cannot be authenticated by base-87a stock membership alone. The strain owner already nests five components and retains its dose as a candidate; this useful uncertainty is preserved.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[6]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 1.04925,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 13-13",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Ca-pantothenate                                              50.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q42",
      "subject": "Pyridoxine hydrochloride flattened CA component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[15].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "Vitamin solution CA, not basal final concentration",
      "interpretation": "The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L value equals provider stock g_l, not the receiving-medium concentration. Restore the complete nine-component stock and retain the explicit 1 ml/litre receiving dose separately; do not infer a physical final stock volume merely from water.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[7]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.43143,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 14-14",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Pyridoxine-HCl                                               50.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q43",
      "subject": "Pyridoxine hydrochloride already nested CA component",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "solutions[0].composition[3].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "solutions[0].composition[3].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Already repaired stock composition",
      "interpretation": "The current owner correctly places this component under Vitamin solution CA and its value matches provider stock g_l. Credit this partial repair and preserve it while adding the four omitted CA components; do not flatten it again.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[7]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.43143,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 14-14",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Pyridoxine-HCl                                               50.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q44",
      "subject": "Pyridoxine hydrochloride in source-87 and strain-variant owners",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[15].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "solutions[0].composition[3].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source branches",
      "interpretation": "The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe is unavailable. These owner fields cannot be authenticated by base-87a stock membership alone. The strain owner already nests five components and retains its dose as a candidate; this useful uncertainty is preserved.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[7]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.43143,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 14-14",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Pyridoxine-HCl                                               50.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q45",
      "subject": "Folic acid flattened CA component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[16].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "Vitamin solution CA, not basal final concentration",
      "interpretation": "The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L value equals provider stock g_l, not the receiving-medium concentration. Restore the complete nine-component stock and retain the explicit 1 ml/litre receiving dose separately; do not infer a physical final stock volume merely from water.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[8]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 1.13276,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 15-15",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Folic acid                                                   50.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q46",
      "subject": "Folic acid already nested CA component",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "solutions[0].composition[4].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "solutions[0].composition[4].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Already repaired stock composition",
      "interpretation": "The current owner correctly places this component under Vitamin solution CA and its value matches provider stock g_l. Credit this partial repair and preserve it while adding the four omitted CA components; do not flatten it again.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[8]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 1.13276,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 15-15",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Folic acid                                                   50.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q47",
      "subject": "Folic acid in source-87 and strain-variant owners",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[16].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "solutions[0].composition[4].concentration",
          "original": {
            "value": "0.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source branches",
      "interpretation": "The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe is unavailable. These owner fields cannot be authenticated by base-87a stock membership alone. The strain owner already nests five components and retains its dose as a candidate; this useful uncertainty is preserved.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[8]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 1.13276,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 15-15",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Folic acid                                                   50.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q48",
      "subject": "Na3-EDTA flattened CA component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[17].concentration",
          "original": {
            "value": "2",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[12].concentration",
          "original": {
            "value": "2",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[12].concentration",
          "original": {
            "value": "2",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "Vitamin solution CA, not basal final concentration",
      "interpretation": "The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L value equals provider stock g_l, not the receiving-medium concentration. Restore the complete nine-component stock and retain the explicit 1 ml/litre receiving dose separately; do not infer a physical final stock volume merely from water.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[9]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na3-EDTA\",\n                        \"compound_id\": 194,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 5.58366,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 16-16",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Na3-EDTA                                                    200.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q49",
      "subject": "Na3-EDTA in source-87 and strain-variant owners",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[17].concentration",
          "original": {
            "value": "2",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[12].concentration",
          "original": {
            "value": "2",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Distinct source branches",
      "interpretation": "The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe is unavailable. These owner fields cannot be authenticated by base-87a stock membership alone. The strain owner already nests five components and retains its dose as a candidate; this useful uncertainty is preserved.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[9]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na3-EDTA\",\n                        \"compound_id\": 194,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 5.58366,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 16-16",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Na3-EDTA                                                    200.0   mg",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q50",
      "subject": "ZnSO4 x 7 H2O SL-6 component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[18].concentration",
          "original": {
            "value": "0.1",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[18].concentration",
          "original": {
            "value": "0.1",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[13].concentration",
          "original": {
            "value": "0.1",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[13].concentration",
          "original": {
            "value": "0.1",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "SL-6 stock composition",
      "interpretation": "The quoted amount is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving addition in medium 87. The flat G_PER_L is a provider stock-strength value, not final-medium concentration. Preserve all supplied hydrates; do not adopt provider mmol_l values that may use a different formula.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[0]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 26-26",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "ZnSO4 x 7 H2O                                                0.10        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q51",
      "subject": "ZnSO4 x 7 H2O in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[13].concentration",
          "original": {
            "value": "0.1",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved variant and stock scope",
      "interpretation": "The value agrees with base SL-6 stock composition, but the variant source and receiving dose are not authenticated. It must not be certified as a final-medium rate.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[0]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 26-26",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "ZnSO4 x 7 H2O                                                0.10        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q52",
      "subject": "MnCl2 x 4 H2O SL-6 component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[19].concentration",
          "original": {
            "value": "0.03",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[19].concentration",
          "original": {
            "value": "0.03",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[14].concentration",
          "original": {
            "value": "0.03",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[14].concentration",
          "original": {
            "value": "0.03",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "SL-6 stock composition",
      "interpretation": "The quoted amount is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving addition in medium 87. The flat G_PER_L is a provider stock-strength value, not final-medium concentration. Preserve all supplied hydrates; do not adopt provider mmol_l values that may use a different formula.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.151588,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 27-27",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "MnCl2 x 4 H2O                                                0.03        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q53",
      "subject": "MnCl2 x 4 H2O in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[14].concentration",
          "original": {
            "value": "0.03",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved variant and stock scope",
      "interpretation": "The value agrees with base SL-6 stock composition, but the variant source and receiving dose are not authenticated. It must not be certified as a final-medium rate.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.151588,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 27-27",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "MnCl2 x 4 H2O                                                0.03        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q54",
      "subject": "H3BO3 SL-6 component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[20].concentration",
          "original": {
            "value": "0.3",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[20].concentration",
          "original": {
            "value": "0.3",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[15].concentration",
          "original": {
            "value": "0.3",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[15].concentration",
          "original": {
            "value": "0.3",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "SL-6 stock composition",
      "interpretation": "The quoted amount is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving addition in medium 87. The flat G_PER_L is a provider stock-strength value, not final-medium concentration. Preserve all supplied hydrates; do not adopt provider mmol_l values that may use a different formula.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[2]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 28-28",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "H3BO3                                                        0.30        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q55",
      "subject": "H3BO3 in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[15].concentration",
          "original": {
            "value": "0.3",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved variant and stock scope",
      "interpretation": "The value agrees with base SL-6 stock composition, but the variant source and receiving dose are not authenticated. It must not be certified as a final-medium rate.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[2]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 28-28",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "H3BO3                                                        0.30        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q56",
      "subject": "CoCl2 x 6 H2O SL-6 component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[21].concentration",
          "original": {
            "value": "0.2",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[21].concentration",
          "original": {
            "value": "0.2",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[16].concentration",
          "original": {
            "value": "0.2",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[16].concentration",
          "original": {
            "value": "0.2",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "SL-6 stock composition",
      "interpretation": "The quoted amount is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving addition in medium 87. The flat G_PER_L is a provider stock-strength value, not final-medium concentration. Preserve all supplied hydrates; do not adopt provider mmol_l values that may use a different formula.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[3]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 29-29",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "CoCl2 x 6 H2O                                                0.20        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q57",
      "subject": "CoCl2 x 6 H2O in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[16].concentration",
          "original": {
            "value": "0.2",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved variant and stock scope",
      "interpretation": "The value agrees with base SL-6 stock composition, but the variant source and receiving dose are not authenticated. It must not be certified as a final-medium rate.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[3]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 29-29",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "CoCl2 x 6 H2O                                                0.20        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q58",
      "subject": "CuCl2 x 2 H2O SL-6 component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[22].concentration",
          "original": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[22].concentration",
          "original": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[17].concentration",
          "original": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[17].concentration",
          "original": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "SL-6 stock composition",
      "interpretation": "The quoted amount is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving addition in medium 87. The flat G_PER_L is a provider stock-strength value, not final-medium concentration. Preserve all supplied hydrates; do not adopt provider mmol_l values that may use a different formula.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[4]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0586569,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 30-30",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "CuCl2 x 2 H2O                                                0.01        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q59",
      "subject": "CuCl2 x 2 H2O in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[17].concentration",
          "original": {
            "value": "0.01",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved variant and stock scope",
      "interpretation": "The value agrees with base SL-6 stock composition, but the variant source and receiving dose are not authenticated. It must not be certified as a final-medium rate.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[4]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0586569,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 30-30",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "CuCl2 x 2 H2O                                                0.01        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q60",
      "subject": "NiCl2 x 6 H2O SL-6 component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[23].concentration",
          "original": {
            "value": "0.02",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[23].concentration",
          "original": {
            "value": "0.02",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[18].concentration",
          "original": {
            "value": "0.02",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[18].concentration",
          "original": {
            "value": "0.02",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "SL-6 stock composition",
      "interpretation": "The quoted amount is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving addition in medium 87. The flat G_PER_L is a provider stock-strength value, not final-medium concentration. Preserve all supplied hydrates; do not adopt provider mmol_l values that may use a different formula.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[5]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 31-31",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "NiCl2 x 6 H2O                                                0.02        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q61",
      "subject": "NiCl2 x 6 H2O in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[18].concentration",
          "original": {
            "value": "0.02",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved variant and stock scope",
      "interpretation": "The value agrees with base SL-6 stock composition, but the variant source and receiving dose are not authenticated. It must not be certified as a final-medium rate.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[5]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 31-31",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "NiCl2 x 6 H2O                                                0.02        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q62",
      "subject": "Na2MoO4 x 2 H2O SL-6 component",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[24].concentration",
          "original": {
            "value": "0.03",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[24].concentration",
          "original": {
            "value": "0.03",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[19].concentration",
          "original": {
            "value": "0.03",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[19].concentration",
          "original": {
            "value": "0.03",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "SL-6 stock composition",
      "interpretation": "The quoted amount is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving addition in medium 87. The flat G_PER_L is a provider stock-strength value, not final-medium concentration. Preserve all supplied hydrates; do not adopt provider mmol_l values that may use a different formula.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[6]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 32-32",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "Na2MoO4 x 2 H2O                                              0.03        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q63",
      "subject": "Na2MoO4 x 2 H2O in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[19].concentration",
          "original": {
            "value": "0.03",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved variant and stock scope",
      "interpretation": "The value agrees with base SL-6 stock composition, but the variant source and receiving dose are not authenticated. It must not be certified as a final-medium rate.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[6]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 32-32",
          "source_key": "dsmz27",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
          "source_raw_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
          "source_text_sha256": "36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8",
          "accessed_at": "2026-10-28T08:39:36.126235Z",
          "exact_source_quote": "Na2MoO4 x 2 H2O                                              0.03        g",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q64",
      "subject": "Neutralized sulfide stock",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ingredients[25].concentration",
          "original": {
            "value": "30",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ingredients[25].concentration",
          "original": {
            "value": "30",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ingredients[20].concentration",
          "original": {
            "value": "30",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ingredients[20].concentration",
          "original": {
            "value": "30",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "correct",
      "stage": "Separate neutralized stock and later injection",
      "interpretation": "3 g nonahydrate with 100 ml water is the stock recipe; API calls it 3% (w/v) and reports 30 g/L on its stock basis. The flat 30 G_PER_L cannot describe the receiving medium. Preserve post-autoclave injection and source nominal 0.03% end concentration separately; the PDF does not explicitly type that end percentage.",
      "sources": [
        {
          "locator": "$.data.solutions[3].recipe[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 124.905,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 30-30",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Na2S x 9 H2O                                                      3.00       g",
          "quote_representation": "captured extracted text"
        },
        {
          "locator": "$.data.solutions[0].steps[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"step\": \"Boil the medium under a stream of nitrogen gas for a few minutes and distribute 90 ml medium into 100 ml screw-capped bottles. Bubble each bottle with nitrogen gas and close immediately with a rubber septum and screw tight. Autoclave at 121\\u00b0C for 15 min. After autoclaving inject 1.0 ml of neutralized sulfide solution (0.03% end concentration) to each bottle. This medium can be stored for several months. Incubate the culture at 50\\u00b0C at a light intensity of 300 - 500 lux. For heavy cell suspension supplement periodically with sterile yeast extract solution (0.1% end concentration, for more details see Ref. 3365, 3366).\"\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q65",
      "subject": "Neutralized sulfide in strain-13941 owner",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ingredients[20].concentration",
          "original": {
            "value": "30",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "unsupported",
      "stage": "Unresolved variant",
      "interpretation": "The base stock source does not authenticate a variant-specific stock dose or final rate. Retain the current 30 G_PER_L as unsupported at its asserted flat stage.",
      "sources": [
        {
          "locator": "$.data.solutions[3].recipe[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 124.905,\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q66",
      "subject": "CA receiving dose already repaired",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "solutions[0].concentration",
          "original": {
            "value": "1",
            "unit": "ML_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "solutions[0].concentration",
          "original": {
            "value": "1",
            "unit": "ML_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Receiving medium addition",
      "interpretation": "The explicit 1.0 ml/litre instruction supports the existing 1 ML_PER_L dose. This is stronger than treating the API batch dose as final-volume proof. Preserve the existing dose while completing stock composition.",
      "sources": [
        {
          "locator": "extracted-text lines 4-4",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "To medium 87 add 1.0 ml/litre sterile vitamin solution CA.",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q67",
      "subject": "CA strain dose remains a candidate",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "solutions[0].concentration_candidates[0]",
          "original": {
            "value": "1",
            "unit": "ML_PER_L",
            "basis": "CROSS_MEDIUM_INFERENCE",
            "support": "This record is a variant of medium 87a (KOMODO key '87a_13941'); volume read from base medium 87a ('CHLOROFLEXUS AGGREGANS MEDIUM').",
            "counterevidence": "The variant's own recipe was never read — only base medium 87a's — so the modification may change this volume. A stock's addition volume varies by citing medium: MediaDive medium 142 adds 'Trace element solution (Vishniac &amp; Santer)' at 0.2 ml and medium 69 adds the same stock at 5 ml.",
            "proposed_by": "apply_cocktail_nesting.py"
          }
        },
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "solutions[0].preparation_notes",
          "original": "Stock prepared in 100 ml. Composition and addition volume NOT asserted: proposed as 1 ml/l on basis CROSS_MEDIUM_INFERENCE; see concentration_candidates (#150)."
        }
      ],
      "decision": "unsupported",
      "stage": "Candidate, not an asserted concentration",
      "interpretation": "The 1 ML_PER_L value is explicitly CROSS_MEDIUM_INFERENCE with counterevidence that the variant was never read. Preserve that distinction. Clarify the note saying composition is not asserted, because five component concentrations are actually asserted in this stock.",
      "sources": [
        {
          "locator": "extracted-text lines 4-4",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "To medium 87 add 1.0 ml/litre sterile vitamin solution CA.",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q68",
      "subject": "Basal water 1050 ml",
      "local_fields": [],
      "decision": "evidence_only",
      "stage": "Source-only water and denominator boundary",
      "interpretation": "Preserve this absolute water input at its own stage. Listed water and provider solution-volume metadata do not establish a measured final volume, so no receiving-medium dilution is manufactured.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[11]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1050,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q69",
      "subject": "CA stock water 100 ml",
      "local_fields": [],
      "decision": "evidence_only",
      "stage": "Source-only water and denominator boundary",
      "interpretation": "Preserve this absolute water input at its own stage. Listed water and provider solution-volume metadata do not establish a measured final volume, so no receiving-medium dilution is manufactured.",
      "sources": [
        {
          "locator": "$.data.solutions[1].recipe[0]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q70",
      "subject": "SL-6 stock water 1000 ml",
      "local_fields": [],
      "decision": "evidence_only",
      "stage": "Source-only water and denominator boundary",
      "interpretation": "Preserve this absolute water input at its own stage. Listed water and provider solution-volume metadata do not establish a measured final volume, so no receiving-medium dilution is manufactured.",
      "sources": [
        {
          "locator": "$.data.solutions[2].recipe[7]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q71",
      "subject": "Sulfide stock water 100 ml",
      "local_fields": [],
      "decision": "evidence_only",
      "stage": "Source-only water and denominator boundary",
      "interpretation": "Preserve this absolute water input at its own stage. Listed water and provider solution-volume metadata do not establish a measured final volume, so no receiving-medium dilution is manufactured.",
      "sources": [
        {
          "locator": "$.data.solutions[3].recipe[0]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q72",
      "subject": "SL-6 receiving dose",
      "local_fields": [],
      "decision": "evidence_only",
      "stage": "Main-medium stock addition",
      "interpretation": "Medium 87 explicitly uses 1 ml of SL-6 in the listed batch. Add the missing stock descriptor and dose on that basis, without silently converting it to 1 ml/L final medium.",
      "sources": [
        {
          "locator": "$.data.solutions[0].recipe[9]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 14-15",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Trace element solution SL-6\n(see medium 27)                                                  1.00       ml",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q73",
      "subject": "Main pH",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml",
          "field_path": "ph_value",
          "original": 8.2
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml",
          "field_path": "ph_value",
          "original": 8.2
        },
        {
          "record_path": "data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml",
          "field_path": "ph_value",
          "original": 8.2
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "ph_value",
          "original": 8.2
        },
        {
          "record_path": "data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml",
          "field_path": "ph_value",
          "original": 8.2
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "preparation_steps[0].description",
          "original": "Adjust pH to 8.2."
        }
      ],
      "decision": "evidence_only",
      "stage": "Main medium",
      "interpretation": "pH 8.2 is directly supported for medium 87 and inherited by defined 87a. The exact KOMODO and strain-variant pages remain unavailable, so copied owner pH is not independent variant authentication.",
      "sources": [
        {
          "locator": "extracted-text lines 18-18",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Adjust pH to 8.2.",
          "quote_representation": "captured extracted text"
        },
        {
          "locator": "$.data.solutions[0].steps[0]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 8.2.\"\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q74",
      "subject": "Main preparation and incubation",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "preparation_steps[1].description",
          "original": "Boil the medium under a stream of nitrogen gas for a few minutes and distribute 90 ml medium into 100 ml screw-capped bottles. Bubble each bottle with nitrogen gas and close immediately with a rubber septum and screw tight. Autoclave at 121°C for 15 min. After autoclaving inject 1.0 ml of neutralized sulfide solution (0.03% end concentration) to each bottle. This medium can be stored for several months. Incubate the culture at 50°C at a light intensity of 300 - 500 lux. For heavy cell suspension supplement periodically with sterile yeast extract solution (0.1% end concentration, for more details see Ref. 3365, 3366)."
        }
      ],
      "decision": "evidence_only",
      "stage": "Basal preparation, post-autoclave injection and source prescriptions",
      "interpretation": "Credit the DSM owner: nitrogen boiling for a few minutes, 90 ml in 100 ml screw-cap bottles, nitrogen seal, 121 C for 15 min, later 1 ml neutralized sulfide, nominal 0.03% end concentration, storage for several months, 50 C and 300–500 lux, optional sterile yeast-extract supplementation at nominal 0.1%. Preserve qualitative durations and unspecified percentage bases. These are collection instructions, not independently read experimental growth results. The generated target omits them.",
      "sources": [
        {
          "locator": "$.data.solutions[0].steps[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"step\": \"Boil the medium under a stream of nitrogen gas for a few minutes and distribute 90 ml medium into 100 ml screw-capped bottles. Bubble each bottle with nitrogen gas and close immediately with a rubber septum and screw tight. Autoclave at 121\\u00b0C for 15 min. After autoclaving inject 1.0 ml of neutralized sulfide solution (0.03% end concentration) to each bottle. This medium can be stored for several months. Incubate the culture at 50\\u00b0C at a light intensity of 300 - 500 lux. For heavy cell suspension supplement periodically with sterile yeast extract solution (0.1% end concentration, for more details see Ref. 3365, 3366).\"\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "extracted-text lines 19-20",
          "source_key": "dsmz87",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf",
          "source_raw_sha256": "99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc",
          "source_text_sha256": "5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7",
          "accessed_at": "2026-10-28T08:33:55.975133Z",
          "exact_source_quote": "Boil the medium under a stream of nitrogen gas for a few minutes and distribute 90 ml\nmedium into 100 ml screw-capped bottles.",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q75",
      "subject": "Current source-87 preparation version",
      "local_fields": [],
      "decision": "evidence_only",
      "stage": "Provider version comparison only",
      "interpretation": "Current API 87 instead says 10 ml in 15 ml Hungate tubes and 0.1 ml sulfide. Preserve this version difference from the current PDF and API 87a; do not silently substitute either preparation into the unavailable KOMODO 87 recipe.",
      "sources": [
        {
          "locator": "$.data.solutions[0].steps[1]",
          "source_key": "api87",
          "reference": "https://mediadive.dsmz.de/rest/medium/87",
          "source_raw_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "source_text_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "accessed_at": "2026-10-28T08:33:55.974764Z",
          "exact_source_quote": "{\n                        \"step\": \"Boil the medium under a stream of nitrogen gas for a few minutes and distribute 10 ml medium into 15 ml hungate tubes. Bubble each tube with nitrogen gas and close immediately with a rubber septum and screw tight.\"\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "$.data.solutions[0].steps[3]",
          "source_key": "api87",
          "reference": "https://mediadive.dsmz.de/rest/medium/87",
          "source_raw_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "source_text_sha256": "4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7",
          "accessed_at": "2026-10-28T08:33:55.974764Z",
          "exact_source_quote": "{\n                        \"step\": \"After autoclaving inject 0.1 ml of neutralized sulfide solution (0.03% end concentration) to each tube.\"\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q76",
      "subject": "CA stock preparation",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "preparation_steps[2].description",
          "original": "Adjust pH to 7.5. The solution is filter-sterilized."
        }
      ],
      "decision": "evidence_only",
      "stage": "CA stock, not main medium",
      "interpretation": "The pH 7.5 and filter sterilization belong only to CA. The DSM owner retains the prose but it is pooled in a root list; attach clear stock scope and preserve main pH 8.2.",
      "sources": [
        {
          "locator": "extracted-text lines 18-18",
          "source_key": "dsmz87a",
          "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf",
          "source_raw_sha256": "4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d",
          "source_text_sha256": "4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a",
          "accessed_at": "2026-10-28T08:33:56.018620Z",
          "exact_source_quote": "Adjust pH to 7.5. The solution is filter-sterilized.",
          "quote_representation": "captured extracted text"
        },
        {
          "locator": "$.data.solutions[1].steps[0]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 7.5. The solution is filter-sterilized.\"\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    },
    {
      "decision_id": "q77",
      "subject": "Neutralized sulfide preparation",
      "local_fields": [
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "preparation_steps[3].description",
          "original": "The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle."
        },
        {
          "record_path": "data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml",
          "field_path": "preparation_steps[4].description",
          "original": "Appearance of a yellow colour indicates the drop of pH to about 8. The solution should be stirred continuously to avoid precipitation of elemental sulfur. The final solution should be clear and is yellow in colour."
        }
      ],
      "decision": "evidence_only",
      "stage": "Sulfide stock",
      "interpretation": "Preserve the 250 ml vessel, nitrogen treatment, 121 C for 15 min, cooling to room temperature, then sterile 2 M H2SO4 dropwise to about pH 7.0 with no stated acid volume. Yellow colour around pH 8 is an intermediate indicator, not the final target. Continuous stirring avoids sulfur precipitation. Do not treat acid stock molarity as final medium molarity.",
      "sources": [
        {
          "locator": "$.data.solutions[3].steps[0]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"step\": \"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121\\u00b0C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n                    }",
          "quote_representation": "raw JSON object"
        },
        {
          "locator": "$.data.solutions[3].steps[1]",
          "source_key": "api87a",
          "reference": "https://mediadive.dsmz.de/rest/medium/87a",
          "source_raw_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "source_text_sha256": "999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884",
          "accessed_at": "2026-10-28T08:33:55.983518Z",
          "exact_source_quote": "{\n                        \"step\": \"Appearance of a yellow colour indicates the drop of pH to about 8. The solution should be stirred continuously to avoid precipitation of elemental sulfur. The final solution should be clear and is yellow in colour.\"\n                    }",
          "quote_representation": "raw JSON object"
        }
      ]
    }
  ],
  "local_field_census_reference": "REVIEW_WORK/batch061/record05/grounding-inventory.json",
  "source_only_gaps_are_explicit": true,
  "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."
}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:006721.

data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml: primary 25/26, secondary 23/26; data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml: primary 25/26, secondary 23/26; data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml: primary 20/21, secondary 18/21; data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml: primary 20/21, secondary 18/21; data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml: primary 20/21, secondary 18/21. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 10 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:006721.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:006721.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Distinct source branches are consolidated without independent equivalence

major / open / confirmed; issue key: culturemech-006721-source-branches-not-proven-duplicates.

The target and relationship claims collapse base 87, defined 87a and a strain-13941 modifier on copied signatures. DSM 87a explicitly adds CA; base 87 does not. The three exact KOMODO routes returned 403. Current full-formulation merge guards reject incompatible scientific content, so old generated consolidation must not be justified by the current merger or copied histories.

### f2: Stock recipes and receiving doses are represented as flat final concentrations

major / open / confirmed; issue key: culturemech-006721-stock-stage-and-volume-errors.

Fe(III) citrate is a 5 ml solution addition, not 5 g/L. Nine CA components, seven SL-6 components and neutralized sulfide need distinct stock/dose stages. Three owners already nest five CA components; preserve them and the two supported 1 ML_PER_L additions. The generated target retains all stock-strength rows flat. No final-volume conversion follows merely from 1050 ml listed water.

### f3: Generated content omits existing owner repairs and preparation

major / open / confirmed; issue key: culturemech-006721-stale-preparation-and-partial-repairs.

The DSM owner retains five preparation entries including nitrogen, vessels, sterilization, incubation, CA and sulfide controls, while the generated target retains none. Three owners contain partial nested CA composition absent from the target. Pooled owner preparation still needs clear stock stages. Current merger guards preserve these fields and reject incompatible formulas; persisted loss is a stale-output/owner-reconciliation issue.

### f4: Nickel hexahydrate asserts the anhydrous ontology identity

major / open / confirmed; issue key: culturemech-006721-nickel-hydrate-link.

All five selected layers name nickel chloride hexahydrate but assert CHEBI:34887 in both primary and secondary slots. Current OLS identifies this as anhydrous nickel dichloride; CHEBI:53542 is the independently retrieved hexahydrate candidate. Literal label agreement and provider mmol_l do not fix a supplied-form mismatch. Other hydrate labels were checked independently.

### f5: Legacy nitrate identifiers have no current exact MIM rows

minor / open / confirmed; issue key: culturemech-006721-legacy-nitrate-linkage.

The ten numeric legacy mentions are the two nitrate secondary IDs repeated across five complete selected documents. Exact current CSV/catalog lookup finds no MediaIngredientMech:000170 or :000171; valid primary CHEBI nitrate identities are retained. Current absence does not establish that these historical IDs were never valid.

### f6: Malformed history and contradictory variant notes need append-only clarification

minor / open / confirmed; issue key: culturemech-006721-append-only-history-and-variant-note.

KOMODO histories retain literal .fZ timestamps. The strain stock note says composition is not asserted although five component concentrations are present; its dose correctly remains only a cross-medium candidate. These distinctions should be explicit rather than silently rewriting old events.

## Recommended Actions And Acceptance Checks

### action1

Retain the valid DSM 87a identity. Reassess each maintained branch against its exact source before treating it as a duplicate; preserve unresolved strain modifications and the current candidate dose. Review variant-proposal criteria and regenerate only scientifically compatible records.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Reconstruct the complete source-scoped stocks and explicit receiving additions in maintained owners, keeping current correct nested components and candidate uncertainty. Represent Fe stock composition, liquid dose, sulfide stock preparation and later injection separately. Use source batch amounts or explicitly attributed provider normalization; do not invent final-volume rates.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Preserve the existing DSM preparation and nested repairs. Complete stage-specific owner content, including stock-only pH and sterilization, then regenerate through current guarded merging after resolving branch identity. Keep source-only incubation instructions distinct from measured growth evidence.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Resolve the exact hexahydrate through authoritative ontology and current MIM mappings, preserving source mass and stock stage. Do not replace hydrate mass with an anhydrous molar conversion. Treat generic source calcium pantothenate versus the more specific D-pantothenate assertion as unresolved stereochemical support, not an automatic replacement.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Resolve the legacy secondary nitrate references against current authoritative MIM identity evidence, retaining correct primary CHEBI terms and historical provenance. Do not force a fuzzy or substring match.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action6

Preserve malformed original events and all old evidence unchanged. Append a verified corrective/context event with the actual current curation date, identifying only evidence-supported prior context. Clarify asserted composition versus unasserted candidate dose, and repair the writer timestamp format for future events.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local3 | data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local4 | data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch061/record05/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch061/record05/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch061/record05/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch061/record05/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsmz87a | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api87a | https://mediadive.dsmz.de/rest/medium/87a; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| dsmz87 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api87 | https://mediadive.dsmz.de/rest/medium/87; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| komodo87 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=87; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| komodo87a | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=87a; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| komodo87a13941 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=87a_13941; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53542 = nickel chloride hexahydrate; definition ['A hydrate of nickel chloride containing nickel (in the +2 oxidation state), chloride and water moeities in the ratio 1:2:6.']; formula ['2Cl.6H2O.Ni']; mass ['237.689']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi132751 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:132751 = thiamine hydrochloride dihydrate; definition ['A hydrate that is the dihydrate form of thiamine hydrochloride.']; formula ['C12H18N4OS.2Cl.2H2O']; mass ['373.306']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi144421 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_144421; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:144421 = iron(III) citrate; definition ['An iron chelate resulting from the combination of iron(3+) and citrate(3−).']; formula ['C6H5FeO7']; mass ['244.944']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17201 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17201; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17201 = glycylglycine; definition ['A dipeptide formed from glycine residues.']; formula ['C4H8N2O3']; mass ['132.119']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:27470 = folic acid; definition ['An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6']; mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32312 = zinc sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of zinc sulfate.']; formula ['7H2O.O4S.Zn']; mass ['287.558']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63005 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63005 = sodium nitrate; definition ['The inorganic nitrate salt of sodium.']; formula ['NO3.Na']; mass ['84.994']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63043 = potassium nitrate; definition ['The inorganic nitrate salt of potassium.']; formula ['K.NO3']; mass ['101.102']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63125 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63125; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63125 = EDTA trisodium salt; definition ['The organic sodium salt of ethylenediaminetetraacetic acid (EDTA) in which three sodium cations are associated with one trianion of EDTA.']; formula ['C10H13N2O8.3Na']; mass ['358.19']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition ['A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O.']; formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi91258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:91258 = disodium hydrogenphosphate dihydrate; definition ['A hydrate that is the dihydrate form of disodium hydrogenphosphate']; formula ['2H2O.HO4P.2Na']; mass ['177.988']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| dsmz27 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete captured PDF text and page 1 visually read; only the explicitly referenced Trace element solution SL-6 subsection supports this receiving record. The unrelated DSM 27 main recipe, vitamins, dose, pH and growth instructions do not transfer. |
| grounding | REVIEW_WORK/batch061/record05/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T070528Z-CHLOROFLEXUS_AGGREGANS_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/chloroflexus_aggregans_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api87a raw bytes exactly match the cited historical SHA, and 37 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history2 | reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_87a_modified_for_dsm_13941.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api87a raw bytes exactly match the cited historical SHA, and 37 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history3 | reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api87a raw bytes exactly match the cited historical SHA, and 37 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history4 | reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history7 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chloroflexus_aggregans_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history8 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history9 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch061/record05/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer55 | scripts/apply_cocktail_nesting.py; relevant functions named in summary | context_only | Current plan_record skips already nested solutions; match_components/match_stock_signature match stored signatures, and apply_plan moves selected components while retaining cross-medium doses as candidates. The existing five-component repair and unasserted strain dose are credited. Current code does not authenticate unseen variants or complete an incomplete stock. |
| writer56 | scripts/apply_mim_groundings.py; relevant functions named in summary | context_only | target_slot preserves existing CHEBI assertions, groundable excludes conflicting corpus opinions and apply_to_record fills only ungrounded names. This current CHEBI-only writer does not automatically replace legacy secondary MIM links or authenticate quantities. |
| writer57 | scripts/propose_cocktail_nesting.py; relevant functions named in summary | context_only | Current build_proposals uses audited cocktail flags and stored component values; recover_volume searches preparation/notes, while provider additions take precedence when present. These proposals are not independent source verification and do not prove complete stock membership or variant equivalence. |
| writer58 | scripts/propose_media_variant_links.py; relevant functions named in summary | context_only | Current infer_relationship/modification_text compares names and concentration signatures to propose source-duplicate or variant links for review. A copied signature cannot authenticate equivalence, and the proposal language explicitly calls for source verification. |
| writer59 | scripts/resolve_komodo_compositions.py; relevant functions named in summary | context_only | Full CLI wrapper read: it delegates empty KOMODO ingredient enrichment to DSMZCompositionResolver and exposes dry-run/report modes. The wrapper documents copied ingredients/solutions but does not independently authenticate a particular past execution or variant. The underlying resolver is an inspected input and is assessed separately. |
| writer60 | src/culturemech/enrich/dsmz_resolver.py; relevant functions named in summary | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients, solutions, pH, physical state and medium type; it does not copy preparation or independently establish source equivalence. resolve_recipe skips already populated ingredient lists. Current behavior does not authenticate the historical enrichment execution. |
| writer61 | src/culturemech/import/komodo_web_importer.py; relevant functions named in summary | context_only | Current _convert_to_culturemech builds KOMODO identity, is_aerobic notes and initially empty ingredients for later DSMZ enrichment; its strftime format uses literal %f. Read code does not authenticate the past table values or source-copy execution. |
| writer62 | src/culturemech/import/mediadive_importer.py; relevant functions named in summary | context_only | Current _parse_api_composition uses only the primary recipe and prefers provider g_l; it excludes a fixed list of solvent names, which does not include Tap water. The ml fallback maps to ML_PER_L, requiring an independent denominator check. _is_api_stock_addition recognizes explicit stock IDs and percentage attributes, but not molar-only attributes such as 1M. _parse_preparation_steps collects prose from all solution sections without separate stage fields. These present behaviors do not establish historical execution. |
| writer63 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer64 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer65 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| quantity-inventory | REVIEW_WORK/batch061/record05/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Exact KOMODO 87, 87a and 87a_13941 routes returned HTTP 403; no equivalence or strain-specific formulation is inferred from copied signatures.
- Listed water is not measured final volume. API 87a and 87 use different declared normalization bases and preparation versions; neither is silently transferred to the other.
- DSM 27 supports only the named SL-6 subsection. Its basal recipe and growth/preparation instructions do not transfer.
- Current MIM lookup is pinned to the packaged CSV metadata commit 6643131b0f12ab40b66f98135245fca04027e0e9; current negatives do not establish historical invalidity. Source-generic calcium pantothenate does not conclusively establish D stereochemistry.
- All ten reports were fully read; matching current API 87a raw authenticates those bytes and excerpts, not old retrieval time, execution or the separately cited KOMODO catalogue. No paper-level growth experiment was newly verified.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T090556Z-chloroflexus-aggregans-medium-batch061
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of chloroflexus_aggregans_medium
started_at: '2026-10-28T08:33:15.477685Z'
finished_at: '2026-10-28T09:05:56.857631Z'
reviewer:
  identity: Codex independent record reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh review of existing unchanged repository records; this
    reviewer did not author or curate the selected target/owners. Historical reports
    were independently reassessed against current exact sources.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The valid DSM 87a record needs source-branch reconciliation and full stock-stage
  reconstruction. Correct basal provider rates, five-component owner nesting and explicit
  CA doses are credited. Fe solution units, flattened stocks, missing generated preparation
  and nickel hydrate linkage require curation; exact KOMODO and strain-variant support
  remains unresolved.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
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
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml
    sha256: 51fb57e178be00bd37f6ec1922efe7bc54d20d5f75f1b56f443b091365f1ada8
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    sha256: 6ef391b68527c7acefb906cf628d73a13430eacef2330f90b970ecd2df412046
    role: context
  - path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    sha256: ed7c8066a7982b4b423c5d30cd431e553a640272465c35aa20af572610e2a2dc
    role: context
  - path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    sha256: acf505d44a3f7ff66d4bbcfce01c29408f568b3bac1655560d511cf5ec0a2d17
    role: context
  - path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    sha256: 12a6c538dd99af56a57ff118bd58c18632682c231e735c6d3d0f4bed398a7968
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml.md
    sha256: 5ea384022030e6a0a55c3f0e4f9b951304a176ee07eb398ff34b7a0b632eef5b
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml.md
    sha256: 40b183c53d69eb9d89b0ecc42045eda6f115e30e15da25739ffe2c221ed03682
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_87a_modified_for_dsm_13941.yaml.md
    sha256: 751b951ef2be6a0ed494288fcc4894ac420a9624e7fc359f9427e3570c52bff2
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/chloroflexus_aggregans_medium.yaml.md
    sha256: 785a9edda146311d4ab1d90ab8b9692f6b73813d726031e877cc81e175edb10e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.md
    sha256: b1a9d0260391e343ae15af2afd90fe54ceac21dbc253514ac45e9b8b34b3d520
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.md
    sha256: 19e9280e59d9a56a360c103b5f6e791df2f6f98e4ec33d725b9cd974c45c44ee
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.md
    sha256: 80a0faa3d50ce129c2b071bb772f8c385a117912bc211cb6443af6fa64c40e12
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chloroflexus_aggregans_medium.md
    sha256: 04bd043b9df015721568366b31cddfafc583dc06b5a20de3523c160da583a1b8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.md
    sha256: 0c558850e9c9a485ac1eadd127e714bad54ad98ecbe0ac5b40e5fe3692813243
    role: context
  - path: reports/yaml_record_review/20260922T070528Z-CHLOROFLEXUS_AGGREGANS_MEDIUM.md
    sha256: 74817b15ff1f2065ca52549e267792c613a59177bb9ce06744dfad9d97e6885e
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/propose_cocktail_nesting.py
    sha256: e886c446a8398f08f1cc735b1c3a9812c5fc6371a36b69ef5325f1c53f14e6c0
    role: context
  - path: scripts/propose_media_variant_links.py
    sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
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
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
scope:
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch061 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006721
targets:
- target_id: CultureMech:006721
  path: data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml
  label: chloroflexus_aggregans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006721
  command: just validate-schema data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006721
  command: just validate-strict data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch061/record05/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006721
  command: just validate-terms data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:006721
  command: just validate-references data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T08:49:05.868113Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 51fb57e178be00bd37f6ec1922efe7bc54d20d5f75f1b56f443b091365f1ada8
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T08:49:05.868266Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 6ef391b68527c7acefb906cf628d73a13430eacef2330f90b970ecd2df412046
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T08:49:05.868288Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: ed7c8066a7982b4b423c5d30cd431e553a640272465c35aa20af572610e2a2dc
- evidence_id: local3
  kind: record_content
  reference: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T08:49:05.868308Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: acf505d44a3f7ff66d4bbcfce01c29408f568b3bac1655560d511cf5ec0a2d17
- evidence_id: local4
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T08:49:05.868330Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 12a6c538dd99af56a57ff118bd58c18632682c231e735c6d3d0f4bed398a7968
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch061/record05/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T08:33:16.481481Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 3105703787f9a6d8afa5bfe85db169ba443276affeb676d5efd5c83de994096d
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch061/record05/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T08:33:17.397759Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 701460b5c587dc34713d1b4a2c98a60c344cae80c41463e08ee1193e3f06b0a3
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch061/record05/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T08:33:18.400563Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: cc522297be316343ecd0815b88398e426151473d277da85df280facb1254d191
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch061/record05/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T08:33:19.114002Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 3f06736c8a6021c043846d7aa3e2eb38b38464734e0e1d17ff55c6d4ede4f697
- evidence_id: dsmz87a
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:56.018620Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d
- evidence_id: api87a
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/87a
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:55.983518Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884
- evidence_id: dsmz87
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:55.975133Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc
- evidence_id: api87
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/87
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:55.974764Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7
- evidence_id: komodo87
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=87
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:55.974620Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 23b6e61dcc7a69f3ef4f72c29584625f22430d6df764c0618024bc0b4b12aed0
- evidence_id: komodo87a
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=87a
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:55.839236Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 3ab749e77ebc77f0ca4cab4fd6e54ba3d1270c54fb2a0bd67096ec15b8d95f8e
- evidence_id: komodo87a13941
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=87a_13941
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:55.798114Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: f160d63de4290f7fd8356c668fc1905a350196f1978d4d2f0872c4d8fdb0957b
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:55.705448Z'
  support: supports
  summary: OLS current exact CHEBI:53542 = nickel chloride hexahydrate; definition
    ['A hydrate of nickel chloride containing nickel (in the +2 oxidation state),
    chloride and water moeities in the ratio 1:2:6.']; formula ['2Cl.6H2O.Ni']; mass
    ['237.689']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: chebi132751
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:55.580721Z'
  support: supports
  summary: OLS current exact CHEBI:132751 = thiamine hydrochloride dihydrate; definition
    ['A hydrate that is the dihydrate form of thiamine hydrochloride.']; formula ['C12H18N4OS.2Cl.2H2O'];
    mass ['373.306']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 509a9cc0fafffbbccf4801dc30121b1cf3d5d176746d0003356be395faf625e9
- evidence_id: chebi144421
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_144421
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:55.374241Z'
  support: supports
  summary: OLS current exact CHEBI:144421 = iron(III) citrate; definition ['An iron
    chelate resulting from the combination of iron(3+) and citrate(3−).']; formula
    ['C6H5FeO7']; mass ['244.944']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 283ce05a4ff7d7b60c46f1b8447bc5f217ea1d84543f59ad566eb9f893b768a1
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:53.502195Z'
  support: supports
  summary: OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic
    acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy
    group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:53.479372Z'
  support: supports
  summary: OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic
    compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi17201
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17201
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:55.373296Z'
  support: supports
  summary: OLS current exact CHEBI:17201 = glycylglycine; definition ['A dipeptide
    formed from glycine residues.']; formula ['C4H8N2O3']; mass ['132.119']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: c306991e1da011a6b109f535689d73641a76513fbafa4e9e7264aaa6b515dc61
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:53.435372Z'
  support: supports
  summary: OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of
    a group of cobalamin vitamers that exhibit biological activity against vitamin
    B<small><sub>12</sub></small> deficiency. Vitamin B<small><sub>12</sub></small>
    deficiency is associated with low red blood cell count and anemia. The vitamers
    are found in foods such as cereals, meat, fish, and poultry. The vitamers include
    adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin
    and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).'];
    formula None; mass None; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.909743Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.848896Z'
  support: supports
  summary: OLS current exact CHEBI:27470 = folic acid; definition ['An <em>N</em>-acyl-amino
    acid that is a form of the water-soluble vitamin B<small><sub>9</sub></small>.
    Its biologically active forms (tetrahydrofolate and others) are essential for
    nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6'];
    mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.834752Z'
  support: supports
  summary: OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic
    acid in which the amino group is <em>para</em> to the carboxy group.']; formula
    ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.766950Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.267651Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:55.220842Z'
  support: supports
  summary: OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S'];
    mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.155309Z'
  support: supports
  summary: OLS current exact CHEBI:32312 = zinc sulfate heptahydrate; definition ['A
    hydrate that is the heptahydrate form of zinc sulfate.']; formula ['7H2O.O4S.Zn'];
    mass ['287.558']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:51.674201Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:51.606222Z'
  support: supports
  summary: OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound
    of nickel and chloride in which the ratio of nickel (in the +2 oxidation state)
    to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:55.139534Z'
  support: supports
  summary: OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition
    ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride
    and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63005
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:55.103049Z'
  support: supports
  summary: OLS current exact CHEBI:63005 = sodium nitrate; definition ['The inorganic
    nitrate salt of sodium.']; formula ['NO3.Na']; mass ['84.994']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 1ec6a815a0e22ba0d12f84ad998bef39b9e6b80cf90c25cd1ab51903bbb54da3
- evidence_id: chebi63043
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:54.977216Z'
  support: supports
  summary: OLS current exact CHEBI:63043 = potassium nitrate; definition ['The inorganic
    nitrate salt of potassium.']; formula ['K.NO3']; mass ['101.102']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: c324450e6330a169c708c32a7908b6df0276f4dc76da413e473b563928f61c13
- evidence_id: chebi63125
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63125
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:54.776283Z'
  support: supports
  summary: OLS current exact CHEBI:63125 = EDTA trisodium salt; definition ['The organic
    sodium salt of ethylenediaminetetraacetic acid (EDTA) in which three sodium cations
    are associated with one trianion of EDTA.']; formula ['C10H13N2O8.3Na']; mass
    ['358.19']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f3035b7105cc035a216a9f1a1da3f3171ba5b64cc2ff47813fd5a98cc3b7b11f
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:50.796078Z'
  support: supports
  summary: OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition
    ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na'];
    mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:54.760504Z'
  support: supports
  summary: OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition
    ['A hydrate with formula Na<small><sub>2</sub></small>S·9H<small><sub>2</sub></small>O.'];
    formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:54.578965Z'
  support: supports
  summary: OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O'];
    mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:50.795954Z'
  support: supports
  summary: OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally
    as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:50.795587Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi91258
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:54.390398Z'
  support: supports
  summary: OLS current exact CHEBI:91258 = disodium hydrogenphosphate dihydrate; definition
    ['A hydrate that is the dihydrate form of disodium hydrogenphosphate']; formula
    ['2H2O.HO4P.2Na']; mass ['177.988']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: f6c74e6e0b876aadf2fe47494521d320abb79244773bf4c44da7b288b1e27319
- evidence_id: dsmz27
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:39:36.126235Z'
  support: supports
  summary: Complete captured PDF text and page 1 visually read; only the explicitly
    referenced Trace element solution SL-6 subsection supports this receiving record.
    The unrelated DSM 27 main recipe, vitamins, dose, pH and growth instructions do
    not transfer.
  snapshot_sha256: e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch061/record05/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T08:49:05.878967Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 1605ad6ab4334479134631fe57cb2e5b1945000ba470aed27be63b4e295ab010
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T070528Z-CHLOROFLEXUS_AGGREGANS_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:49:05.880821Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 74817b15ff1f2065ca52549e267792c613a59177bb9ce06744dfad9d97e6885e
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/chloroflexus_aggregans_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:49:05.880855Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api87a raw bytes exactly match the cited historical SHA, and 37
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 785a9edda146311d4ab1d90ab8b9692f6b73813d726031e877cc81e175edb10e
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_87a_modified_for_dsm_13941.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:49:05.880888Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api87a raw bytes exactly match the cited historical SHA, and 37
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 751b951ef2be6a0ed494288fcc4894ac420a9624e7fc359f9427e3570c52bff2
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:49:05.880919Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api87a raw bytes exactly match the cited historical SHA, and 37
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 40b183c53d69eb9d89b0ecc42045eda6f115e30e15da25739ffe2c221ed03682
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:49:05.880947Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 5ea384022030e6a0a55c3f0e4f9b951304a176ee07eb398ff34b7a0b632eef5b
- evidence_id: history5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:49:05.880967Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 19e9280e59d9a56a360c103b5f6e791df2f6f98e4ec33d725b9cd974c45c44ee
- evidence_id: history6
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:49:05.880987Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 80a0faa3d50ce129c2b071bb772f8c385a117912bc211cb6443af6fa64c40e12
- evidence_id: history7
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chloroflexus_aggregans_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:49:05.881006Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 04bd043b9df015721568366b31cddfafc583dc06b5a20de3523c160da583a1b8
- evidence_id: history8
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:49:05.881025Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 0c558850e9c9a485ac1eadd127e714bad54ad98ecbe0ac5b40e5fe3692813243
- evidence_id: history9
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:49:05.881044Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: b1a9d0260391e343ae15af2afd90fe54ceac21dbc253514ac45e9b8b34b3d520
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch061/record05/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T08:49:05.881073Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 3277cedc9184dba234699c0407e6c9895b277001151807ca45d3752a33cda7be
- evidence_id: writer55
  kind: record_content
  reference: scripts/apply_cocktail_nesting.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:49:05.881101Z'
  support: context_only
  summary: Current plan_record skips already nested solutions; match_components/match_stock_signature
    match stored signatures, and apply_plan moves selected components while retaining
    cross-medium doses as candidates. The existing five-component repair and unasserted
    strain dose are credited. Current code does not authenticate unseen variants or
    complete an incomplete stock.
  snapshot_sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
- evidence_id: writer56
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:49:05.881124Z'
  support: context_only
  summary: target_slot preserves existing CHEBI assertions, groundable excludes conflicting
    corpus opinions and apply_to_record fills only ungrounded names. This current
    CHEBI-only writer does not automatically replace legacy secondary MIM links or
    authenticate quantities.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer57
  kind: record_content
  reference: scripts/propose_cocktail_nesting.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:49:05.881143Z'
  support: context_only
  summary: Current build_proposals uses audited cocktail flags and stored component
    values; recover_volume searches preparation/notes, while provider additions take
    precedence when present. These proposals are not independent source verification
    and do not prove complete stock membership or variant equivalence.
  snapshot_sha256: e886c446a8398f08f1cc735b1c3a9812c5fc6371a36b69ef5325f1c53f14e6c0
- evidence_id: writer58
  kind: record_content
  reference: scripts/propose_media_variant_links.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:49:05.881170Z'
  support: context_only
  summary: Current infer_relationship/modification_text compares names and concentration
    signatures to propose source-duplicate or variant links for review. A copied signature
    cannot authenticate equivalence, and the proposal language explicitly calls for
    source verification.
  snapshot_sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
- evidence_id: writer59
  kind: record_content
  reference: scripts/resolve_komodo_compositions.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:49:05.881189Z'
  support: context_only
  summary: 'Full CLI wrapper read: it delegates empty KOMODO ingredient enrichment
    to DSMZCompositionResolver and exposes dry-run/report modes. The wrapper documents
    copied ingredients/solutions but does not independently authenticate a particular
    past execution or variant. The underlying resolver is an inspected input and is
    assessed separately.'
  snapshot_sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
- evidence_id: writer60
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:49:05.881214Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients, solutions,
    pH, physical state and medium type; it does not copy preparation or independently
    establish source equivalence. resolve_recipe skips already populated ingredient
    lists. Current behavior does not authenticate the historical enrichment execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer61
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:49:05.881235Z'
  support: context_only
  summary: Current _convert_to_culturemech builds KOMODO identity, is_aerobic notes
    and initially empty ingredients for later DSMZ enrichment; its strftime format
    uses literal %f. Read code does not authenticate the past table values or source-copy
    execution.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer62
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:49:05.881266Z'
  support: context_only
  summary: Current _parse_api_composition uses only the primary recipe and prefers
    provider g_l; it excludes a fixed list of solvent names, which does not include
    Tap water. The ml fallback maps to ML_PER_L, requiring an independent denominator
    check. _is_api_stock_addition recognizes explicit stock IDs and percentage attributes,
    but not molar-only attributes such as 1M. _parse_preparation_steps collects prose
    from all solution sections without separate stage fields. These present behaviors
    do not establish historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer63
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:49:05.881287Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer64
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:49:05.881308Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer65
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:49:05.881327Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch061/record05/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T09:05:56.857631Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 602d70688c95b4df3433380972b519c08a09dc7b273bcc9dbe241ec98cb8fce7
assessments:
- assessment_id: a1
  area: identity
  topic: Base, supplement and strain identities
  outcome: concern
  summary: The selected DSM 87a identity is valid, but source 87, source 87a and the
    unverified strain-13941 modifier are not proven duplicates. DSM 87a explicitly
    adds CA to 87. Current owners copied the same ingredient signature, then three
    gained a partial CA repair; similarity and copied history are not independent
    equivalence evidence.
  target_ids:
  - CultureMech:006721
  evidence_ids:
  - dsmz87a
  - dsmz87
  - api87a
  - api87
  - komodo87
  - komodo87a
  - komodo87a13941
- assessment_id: a2
  area: completeness
  topic: Existing repairs and retained preparation
  outcome: concern
  summary: Three maintained owners already nest five CA components, and the two base-87a
    owners assert the correct 1 ML_PER_L dose. The strain owner keeps the dose candidate
    unasserted. Four CA components, all seven SL-6 components and sulfide remain flat;
    the target drops all nested stocks and DSM preparation. Preserve these correct
    partial repairs.
  target_ids:
  - CultureMech:006721
  evidence_ids:
  - local0
  - local2
  - local3
  - local4
  - dsmz87a
- assessment_id: a3
  area: evidence
  topic: Collection instructions versus growth claims
  outcome: unknown
  summary: The primary sheets prescribe conditions but do not supply a reviewed experiment
    for strain DSM 13941 or independently establish the collection references 3365/3366.
    No strain-specific growth claim is added.
  target_ids:
  - CultureMech:006721
  evidence_ids:
  - dsmz87
  - dsmz87a
- assessment_id: a4
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: All ten exact historical reports and current histories were read. Current
    API 87a bytes authenticate matching October excerpts; API 87 raw differs, with
    the sulfide object now adding g_l and mmol_l. Historical blanket conflict labels
    do not invalidate correctly retained basal provider rates or nested stock values.
    The separate KOMODO catalogue and exact variant remain unavailable. Stored .fZ
    timestamps are malformed and must remain as original events. All historical API
    excerpts with matching current raw digests are independently authenticated in
    historical-authentication.json. Matching bytes do not verify old execution or
    the separate KOMODO catalogue. Current MediaDive code separates stock additions
    but gathers all solution preparation into a root list; current conservative merging
    preserves scientific fields and rejects incompatible formulations. Those present
    behaviors do not prove how the old generated records were produced.
  target_ids:
  - CultureMech:006721
  evidence_ids:
  - history-auth
  - writer55
  - writer56
  - writer57
  - writer58
  - writer59
  - writer60
  - writer61
  - writer62
  - writer63
  - writer64
  - writer65
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 132 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:006721
  evidence_ids:
  - quantity-inventory
  details: "{\n  \"schema\": \"private explicit quantity decisions v1\",\n  \"target_id\"\
    : \"CultureMech:006721\",\n  \"selected_concentration_field_count\": 132,\n  \"\
    selected_concentration_fields_covered\": 132,\n  \"decisions\": [\n    {\n   \
    \   \"decision_id\": \"q1\",\n      \"subject\": \"Yeast extract in selected and\
    \ base-87a layers\",\n      \"local_fields\": [\n        {\n          \"record_path\"\
    : \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\",\n          \"\
    field_path\": \"ingredients[0].concentration\",\n          \"original\": {\n \
    \           \"value\": \"0.952381\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[0].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[0].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n  \
    \    \"stage\": \"Basal medium; provider-declared normalization\",\n      \"interpretation\"\
    : \"The stored value exactly matches current API 87a g_l on its declared 1050\
    \ ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured\
    \ final volume is stated. Retain the supplied hydrate and the current scalar with\
    \ an explicit provider basis, without claiming that listed water is final volume.\
    \ The copied KOMODO layer does not independently authenticate its unavailable\
    \ provider page.\",\n      \"sources\": [\n        {\n          \"locator\": \"\
    $.data.solutions[0].recipe[0]\",\n          \"source_key\": \"api87a\",\n    \
    \      \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n       \
    \   \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"\
    compound_id\\\": 16,\\n                        \\\"amount\\\": 1,\\n         \
    \               \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.952381,\\n                        \\\"optional\\\": 0\\n                 \
    \   }\",\n          \"quote_representation\": \"raw JSON object\"\n        },\n\
    \        {\n          \"locator\": \"extracted-text lines 4-4\",\n          \"\
    source_key\": \"dsmz87\",\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\"\
    ,\n          \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Yeast extract                                                     1.00   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q2\",\n      \"subject\"\
    : \"Yeast extract in KOMODO 87 owner\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[0].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Distinct source-87 branch\",\n      \"interpretation\": \"This\
    \ copied scalar follows API 87a, while current API 87 uses a declared 1056 ml\
    \ normalization. Both primary absolute masses are the same. This does not justify\
    \ replacing the KOMODO scalar with API 87 arithmetic without verifying the exact\
    \ unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[0].recipe[0]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"\
    compound_id\\\": 16,\\n                        \\\"amount\\\": 1,\\n         \
    \               \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.952381,\\n                        \\\"optional\\\": 0\\n                 \
    \   }\",\n          \"quote_representation\": \"raw JSON object\"\n        },\n\
    \        {\n          \"locator\": \"extracted-text lines 4-4\",\n          \"\
    source_key\": \"dsmz87\",\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\"\
    ,\n          \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Yeast extract                                                     1.00   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        },\n        {\n          \"locator\": \"$.data.solutions[0].recipe[0]\"\
    ,\n          \"source_key\": \"api87\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87\"\
    ,\n          \"source_raw_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"source_text_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.974764Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"\
    compound_id\\\": 16,\\n                        \\\"amount\\\": 1,\\n         \
    \               \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.94697,\\n                        \\\"optional\\\": 0\\n                  \
    \  }\",\n          \"quote_representation\": \"raw JSON object\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q3\",\n      \"subject\": \"\
    Yeast extract in strain-13941 owner\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[0].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Unresolved strain variant\",\n      \"interpretation\": \"The\
    \ stored scalar matches base 87a, but the variant recipe remains unavailable.\
    \ Base-source agreement is contextual and does not authenticate an unknown strain\
    \ modification or final-volume basis.\",\n      \"sources\": [\n        {\n  \
    \        \"locator\": \"$.data.solutions[0].recipe[0]\",\n          \"source_key\"\
    : \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"\
    compound_id\\\": 16,\\n                        \\\"amount\\\": 1,\\n         \
    \               \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.952381,\\n                        \\\"optional\\\": 0\\n                 \
    \   }\",\n          \"quote_representation\": \"raw JSON object\"\n        },\n\
    \        {\n          \"locator\": \"extracted-text lines 4-4\",\n          \"\
    source_key\": \"dsmz87\",\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\"\
    ,\n          \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Yeast extract                                                     1.00   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q4\",\n      \"subject\"\
    : \"Glycyl-glycine in selected and base-87a layers\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[1].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[1].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[1].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n  \
    \    \"stage\": \"Basal medium; provider-declared normalization\",\n      \"interpretation\"\
    : \"The stored value exactly matches current API 87a g_l on its declared 1050\
    \ ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured\
    \ final volume is stated. Retain the supplied hydrate and the current scalar with\
    \ an explicit provider basis, without claiming that listed water is final volume.\
    \ The copied KOMODO layer does not independently authenticate its unavailable\
    \ provider page.\",\n      \"sources\": [\n        {\n          \"locator\": \"\
    $.data.solutions[0].recipe[1]\",\n          \"source_key\": \"api87a\",\n    \
    \      \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n       \
    \   \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"Glycyl-glycine\\\",\\n                        \\\"\
    compound_id\\\": 192,\\n                        \\\"amount\\\": 1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.952381,\\n                        \\\"optional\\\": 0\\n                 \
    \   }\",\n          \"quote_representation\": \"raw JSON object\"\n        },\n\
    \        {\n          \"locator\": \"extracted-text lines 5-5\",\n          \"\
    source_key\": \"dsmz87\",\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\"\
    ,\n          \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Glycyl-glycine                                                    1.00   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q5\",\n      \"subject\"\
    : \"Glycyl-glycine in KOMODO 87 owner\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[1].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Distinct source-87 branch\",\n      \"interpretation\": \"This\
    \ copied scalar follows API 87a, while current API 87 uses a declared 1056 ml\
    \ normalization. Both primary absolute masses are the same. This does not justify\
    \ replacing the KOMODO scalar with API 87 arithmetic without verifying the exact\
    \ unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[0].recipe[1]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"Glycyl-glycine\\\",\\n                        \\\"\
    compound_id\\\": 192,\\n                        \\\"amount\\\": 1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.952381,\\n                        \\\"optional\\\": 0\\n                 \
    \   }\",\n          \"quote_representation\": \"raw JSON object\"\n        },\n\
    \        {\n          \"locator\": \"extracted-text lines 5-5\",\n          \"\
    source_key\": \"dsmz87\",\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\"\
    ,\n          \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Glycyl-glycine                                                    1.00   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        },\n        {\n          \"locator\": \"$.data.solutions[0].recipe[1]\"\
    ,\n          \"source_key\": \"api87\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87\"\
    ,\n          \"source_raw_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"source_text_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.974764Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"Glycyl-glycine\\\",\\n                        \\\"\
    compound_id\\\": 192,\\n                        \\\"amount\\\": 1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.94697,\\n                        \\\"mmol_l\\\": 7.16761,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q6\",\n      \"subject\": \"Glycyl-glycine in strain-13941 owner\",\n    \
    \  \"local_fields\": [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[1].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Unresolved strain variant\",\n      \"interpretation\": \"The\
    \ stored scalar matches base 87a, but the variant recipe remains unavailable.\
    \ Base-source agreement is contextual and does not authenticate an unknown strain\
    \ modification or final-volume basis.\",\n      \"sources\": [\n        {\n  \
    \        \"locator\": \"$.data.solutions[0].recipe[1]\",\n          \"source_key\"\
    : \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"Glycyl-glycine\\\",\\n                        \\\"\
    compound_id\\\": 192,\\n                        \\\"amount\\\": 1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.952381,\\n                        \\\"optional\\\": 0\\n                 \
    \   }\",\n          \"quote_representation\": \"raw JSON object\"\n        },\n\
    \        {\n          \"locator\": \"extracted-text lines 5-5\",\n          \"\
    source_key\": \"dsmz87\",\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\"\
    ,\n          \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Glycyl-glycine                                                    1.00   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q7\",\n      \"subject\"\
    : \"Na2HPO4 x 2 H2O in selected and base-87a layers\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[2].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[2].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[2].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n  \
    \    \"stage\": \"Basal medium; provider-declared normalization\",\n      \"interpretation\"\
    : \"The stored value exactly matches current API 87a g_l on its declared 1050\
    \ ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured\
    \ final volume is stated. Retain the supplied hydrate and the current scalar with\
    \ an explicit provider basis, without claiming that listed water is final volume.\
    \ The copied KOMODO layer does not independently authenticate its unavailable\
    \ provider page.\",\n      \"sources\": [\n        {\n          \"locator\": \"\
    $.data.solutions[0].recipe[2]\",\n          \"source_key\": \"api87a\",\n    \
    \      \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n       \
    \   \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Na2HPO4 x 2 H2O\\\",\\n                        \\\
    \"compound_id\\\": 181,\\n                        \\\"amount\\\": 0.1,\\n    \
    \                    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.0952381,\\n                        \\\"mmol_l\\\": 0.670884,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n          \"\
    quote_representation\": \"raw JSON object\"\n        },\n        {\n         \
    \ \"locator\": \"extracted-text lines 6-6\",\n          \"source_key\": \"dsmz87\"\
    ,\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\"\
    ,\n          \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Na2HPO4 x 2 H2O                                                   0.10   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q8\",\n      \"subject\"\
    : \"Na2HPO4 x 2 H2O in KOMODO 87 owner\",\n      \"local_fields\": [\n       \
    \ {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[2].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Distinct source-87 branch\",\n      \"interpretation\": \"This\
    \ copied scalar follows API 87a, while current API 87 uses a declared 1056 ml\
    \ normalization. Both primary absolute masses are the same. This does not justify\
    \ replacing the KOMODO scalar with API 87 arithmetic without verifying the exact\
    \ unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[0].recipe[2]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Na2HPO4 x 2 H2O\\\",\\n                        \\\
    \"compound_id\\\": 181,\\n                        \\\"amount\\\": 0.1,\\n    \
    \                    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.0952381,\\n                        \\\"mmol_l\\\": 0.670884,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n          \"\
    quote_representation\": \"raw JSON object\"\n        },\n        {\n         \
    \ \"locator\": \"extracted-text lines 6-6\",\n          \"source_key\": \"dsmz87\"\
    ,\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\"\
    ,\n          \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Na2HPO4 x 2 H2O                                                   0.10   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        },\n        {\n          \"locator\": \"$.data.solutions[0].recipe[2]\"\
    ,\n          \"source_key\": \"api87\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87\"\
    ,\n          \"source_raw_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"source_text_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.974764Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Na2HPO4 x 2 H2O\\\",\\n                        \\\
    \"compound_id\\\": 181,\\n                        \\\"amount\\\": 0.1,\\n    \
    \                    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.094697,\\n                        \\\"mmol_l\\\": 0.667073,\\n         \
    \               \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q9\",\n      \"subject\": \"Na2HPO4 x 2 H2O in strain-13941 owner\",\n   \
    \   \"local_fields\": [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[2].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Unresolved strain variant\",\n      \"interpretation\": \"The\
    \ stored scalar matches base 87a, but the variant recipe remains unavailable.\
    \ Base-source agreement is contextual and does not authenticate an unknown strain\
    \ modification or final-volume basis.\",\n      \"sources\": [\n        {\n  \
    \        \"locator\": \"$.data.solutions[0].recipe[2]\",\n          \"source_key\"\
    : \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Na2HPO4 x 2 H2O\\\",\\n                        \\\
    \"compound_id\\\": 181,\\n                        \\\"amount\\\": 0.1,\\n    \
    \                    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.0952381,\\n                        \\\"mmol_l\\\": 0.670884,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n          \"\
    quote_representation\": \"raw JSON object\"\n        },\n        {\n         \
    \ \"locator\": \"extracted-text lines 6-6\",\n          \"source_key\": \"dsmz87\"\
    ,\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\"\
    ,\n          \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Na2HPO4 x 2 H2O                                                   0.10   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q10\",\n      \"\
    subject\": \"MgSO4 x 7 H2O in selected and base-87a layers\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[3].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[3].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[3].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n  \
    \    \"stage\": \"Basal medium; provider-declared normalization\",\n      \"interpretation\"\
    : \"The stored value exactly matches current API 87a g_l on its declared 1050\
    \ ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured\
    \ final volume is stated. Retain the supplied hydrate and the current scalar with\
    \ an explicit provider basis, without claiming that listed water is final volume.\
    \ The copied KOMODO layer does not independently authenticate its unavailable\
    \ provider page.\",\n      \"sources\": [\n        {\n          \"locator\": \"\
    $.data.solutions[0].recipe[3]\",\n          \"source_key\": \"api87a\",\n    \
    \      \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n       \
    \   \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 0.1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.0952381,\\n                        \\\"mmol_l\\\": 0.386399,\\n          \
    \              \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 7-7\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O                                                     0.10   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q11\",\n      \"\
    subject\": \"MgSO4 x 7 H2O in KOMODO 87 owner\",\n      \"local_fields\": [\n\
    \        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[3].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Distinct source-87 branch\",\n      \"interpretation\": \"This\
    \ copied scalar follows API 87a, while current API 87 uses a declared 1056 ml\
    \ normalization. Both primary absolute masses are the same. This does not justify\
    \ replacing the KOMODO scalar with API 87 arithmetic without verifying the exact\
    \ unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[0].recipe[3]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 0.1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.0952381,\\n                        \\\"mmol_l\\\": 0.386399,\\n          \
    \              \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 7-7\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O                                                     0.10   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        },\n        {\n          \"locator\": \"$.data.solutions[0].recipe[3]\"\
    ,\n          \"source_key\": \"api87\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87\"\
    ,\n          \"source_raw_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"source_text_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.974764Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 0.1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.094697,\\n                        \\\"mmol_l\\\": 0.384204,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q12\",\n      \"subject\": \"MgSO4 x 7 H2O in strain-13941 owner\",\n    \
    \  \"local_fields\": [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[3].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Unresolved strain variant\",\n      \"interpretation\": \"The\
    \ stored scalar matches base 87a, but the variant recipe remains unavailable.\
    \ Base-source agreement is contextual and does not authenticate an unknown strain\
    \ modification or final-volume basis.\",\n      \"sources\": [\n        {\n  \
    \        \"locator\": \"$.data.solutions[0].recipe[3]\",\n          \"source_key\"\
    : \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 0.1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.0952381,\\n                        \\\"mmol_l\\\": 0.386399,\\n          \
    \              \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 7-7\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O                                                     0.10   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q13\",\n      \"\
    subject\": \"KNO3 in selected and base-87a layers\",\n      \"local_fields\":\
    \ [\n        {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[4].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[4].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[4].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n  \
    \    \"stage\": \"Basal medium; provider-declared normalization\",\n      \"interpretation\"\
    : \"The stored value exactly matches current API 87a g_l on its declared 1050\
    \ ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured\
    \ final volume is stated. Retain the supplied hydrate and the current scalar with\
    \ an explicit provider basis, without claiming that listed water is final volume.\
    \ The copied KOMODO layer does not independently authenticate its unavailable\
    \ provider page.\",\n      \"sources\": [\n        {\n          \"locator\": \"\
    $.data.solutions[0].recipe[4]\",\n          \"source_key\": \"api87a\",\n    \
    \      \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n       \
    \   \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"KNO3\\\",\\n                        \\\"compound_id\\\
    \": 191,\\n                        \\\"amount\\\": 0.1,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0952381,\\\
    n                        \\\"mmol_l\\\": 0.941991,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 8-8\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"KNO3                                                              0.10   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q14\",\n      \"\
    subject\": \"KNO3 in KOMODO 87 owner\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[4].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Distinct source-87 branch\",\n      \"interpretation\": \"This\
    \ copied scalar follows API 87a, while current API 87 uses a declared 1056 ml\
    \ normalization. Both primary absolute masses are the same. This does not justify\
    \ replacing the KOMODO scalar with API 87 arithmetic without verifying the exact\
    \ unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[0].recipe[4]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"KNO3\\\",\\n                        \\\"compound_id\\\
    \": 191,\\n                        \\\"amount\\\": 0.1,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0952381,\\\
    n                        \\\"mmol_l\\\": 0.941991,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 8-8\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"KNO3                                                              0.10   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        },\n        {\n          \"locator\": \"$.data.solutions[0].recipe[4]\"\
    ,\n          \"source_key\": \"api87\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87\"\
    ,\n          \"source_raw_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"source_text_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.974764Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"KNO3\\\",\\n                        \\\"compound_id\\\
    \": 191,\\n                        \\\"amount\\\": 0.1,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.094697,\\\
    n                        \\\"mmol_l\\\": 0.936639,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q15\",\n      \"subject\": \"KNO3 in strain-13941 owner\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[4].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Unresolved strain variant\",\n      \"interpretation\": \"The\
    \ stored scalar matches base 87a, but the variant recipe remains unavailable.\
    \ Base-source agreement is contextual and does not authenticate an unknown strain\
    \ modification or final-volume basis.\",\n      \"sources\": [\n        {\n  \
    \        \"locator\": \"$.data.solutions[0].recipe[4]\",\n          \"source_key\"\
    : \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"KNO3\\\",\\n                        \\\"compound_id\\\
    \": 191,\\n                        \\\"amount\\\": 0.1,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0952381,\\\
    n                        \\\"mmol_l\\\": 0.941991,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 8-8\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"KNO3                                                              0.10   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q16\",\n      \"\
    subject\": \"NaNO3 in selected and base-87a layers\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[5].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.47619\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[5].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.47619\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[5].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.47619\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n  \
    \    \"stage\": \"Basal medium; provider-declared normalization\",\n      \"interpretation\"\
    : \"The stored value exactly matches current API 87a g_l on its declared 1050\
    \ ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured\
    \ final volume is stated. Retain the supplied hydrate and the current scalar with\
    \ an explicit provider basis, without claiming that listed water is final volume.\
    \ The copied KOMODO layer does not independently authenticate its unavailable\
    \ provider page.\",\n      \"sources\": [\n        {\n          \"locator\": \"\
    $.data.solutions[0].recipe[5]\",\n          \"source_key\": \"api87a\",\n    \
    \      \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n       \
    \   \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"NaNO3\\\",\\n                        \\\"compound_id\\\
    \": 187,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.47619,\\\
    n                        \\\"mmol_l\\\": 5.60257,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 9-9\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"NaNO3                                                             0.50   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q17\",\n      \"\
    subject\": \"NaNO3 in KOMODO 87 owner\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[5].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.47619\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Distinct source-87 branch\",\n      \"interpretation\": \"This\
    \ copied scalar follows API 87a, while current API 87 uses a declared 1056 ml\
    \ normalization. Both primary absolute masses are the same. This does not justify\
    \ replacing the KOMODO scalar with API 87 arithmetic without verifying the exact\
    \ unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[0].recipe[5]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"NaNO3\\\",\\n                        \\\"compound_id\\\
    \": 187,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.47619,\\\
    n                        \\\"mmol_l\\\": 5.60257,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 9-9\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"NaNO3                                                             0.50   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        },\n        {\n          \"locator\": \"$.data.solutions[0].recipe[5]\"\
    ,\n          \"source_key\": \"api87\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87\"\
    ,\n          \"source_raw_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"source_text_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.974764Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"NaNO3\\\",\\n                        \\\"compound_id\\\
    \": 187,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.473485,\\\
    n                        \\\"mmol_l\\\": 5.57074,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q18\",\n      \"subject\": \"NaNO3 in strain-13941 owner\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[5].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.47619\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Unresolved strain variant\",\n      \"interpretation\": \"The\
    \ stored scalar matches base 87a, but the variant recipe remains unavailable.\
    \ Base-source agreement is contextual and does not authenticate an unknown strain\
    \ modification or final-volume basis.\",\n      \"sources\": [\n        {\n  \
    \        \"locator\": \"$.data.solutions[0].recipe[5]\",\n          \"source_key\"\
    : \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"NaNO3\\\",\\n                        \\\"compound_id\\\
    \": 187,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.47619,\\\
    n                        \\\"mmol_l\\\": 5.60257,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 9-9\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"NaNO3                                                             0.50   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q19\",\n      \"\
    subject\": \"NaCl in selected and base-87a layers\",\n      \"local_fields\":\
    \ [\n        {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[6].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[6].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[6].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n  \
    \    \"stage\": \"Basal medium; provider-declared normalization\",\n      \"interpretation\"\
    : \"The stored value exactly matches current API 87a g_l on its declared 1050\
    \ ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured\
    \ final volume is stated. Retain the supplied hydrate and the current scalar with\
    \ an explicit provider basis, without claiming that listed water is final volume.\
    \ The copied KOMODO layer does not independently authenticate its unavailable\
    \ provider page.\",\n      \"sources\": [\n        {\n          \"locator\": \"\
    $.data.solutions[0].recipe[6]\",\n          \"source_key\": \"api87a\",\n    \
    \      \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n       \
    \   \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\
    \": 43,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0952381,\\\
    n                        \\\"mmol_l\\\": 1.62967,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 10-10\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"NaCl                                                              0.10   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q20\",\n      \"\
    subject\": \"NaCl in KOMODO 87 owner\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[6].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Distinct source-87 branch\",\n      \"interpretation\": \"This\
    \ copied scalar follows API 87a, while current API 87 uses a declared 1056 ml\
    \ normalization. Both primary absolute masses are the same. This does not justify\
    \ replacing the KOMODO scalar with API 87 arithmetic without verifying the exact\
    \ unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[0].recipe[6]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\
    \": 43,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0952381,\\\
    n                        \\\"mmol_l\\\": 1.62967,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 10-10\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"NaCl                                                              0.10   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        },\n        {\n          \"locator\": \"$.data.solutions[0].recipe[6]\"\
    ,\n          \"source_key\": \"api87\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87\"\
    ,\n          \"source_raw_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"source_text_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.974764Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\
    \": 43,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.094697,\\\
    n                        \\\"mmol_l\\\": 1.62041,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q21\",\n      \"subject\": \"NaCl in strain-13941 owner\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[6].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.0952381\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Unresolved strain variant\",\n      \"interpretation\": \"The\
    \ stored scalar matches base 87a, but the variant recipe remains unavailable.\
    \ Base-source agreement is contextual and does not authenticate an unknown strain\
    \ modification or final-volume basis.\",\n      \"sources\": [\n        {\n  \
    \        \"locator\": \"$.data.solutions[0].recipe[6]\",\n          \"source_key\"\
    : \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\
    \": 43,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0952381,\\\
    n                        \\\"mmol_l\\\": 1.62967,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 10-10\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"NaCl                                                              0.10   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q22\",\n      \"\
    subject\": \"CaCl2 x 2 H2O in selected and base-87a layers\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[7].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.047619\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[7].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.047619\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[7].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.047619\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n  \
    \    \"stage\": \"Basal medium; provider-declared normalization\",\n      \"interpretation\"\
    : \"The stored value exactly matches current API 87a g_l on its declared 1050\
    \ ml basis. The primary gives the quoted absolute mass and 1050 ml water; no measured\
    \ final volume is stated. Retain the supplied hydrate and the current scalar with\
    \ an explicit provider basis, without claiming that listed water is final volume.\
    \ The copied KOMODO layer does not independently authenticate its unavailable\
    \ provider page.\",\n      \"sources\": [\n        {\n          \"locator\": \"\
    $.data.solutions[0].recipe[7]\",\n          \"source_key\": \"api87a\",\n    \
    \      \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n       \
    \   \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 7,\\n                        \\\"amount\\\": 0.05,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.047619,\\n                        \\\"mmol_l\\\": 0.323906,\\n         \
    \               \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 11-11\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O                                                     0.05   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q23\",\n      \"\
    subject\": \"CaCl2 x 2 H2O in KOMODO 87 owner\",\n      \"local_fields\": [\n\
    \        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[7].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.047619\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Distinct source-87 branch\",\n      \"interpretation\": \"This\
    \ copied scalar follows API 87a, while current API 87 uses a declared 1056 ml\
    \ normalization. Both primary absolute masses are the same. This does not justify\
    \ replacing the KOMODO scalar with API 87 arithmetic without verifying the exact\
    \ unavailable KOMODO recipe; retain the discrepancy as an identity/basis issue.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[0].recipe[7]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 7,\\n                        \\\"amount\\\": 0.05,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.047619,\\n                        \\\"mmol_l\\\": 0.323906,\\n         \
    \               \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 11-11\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O                                                     0.05   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        },\n        {\n          \"locator\": \"$.data.solutions[0].recipe[7]\"\
    ,\n          \"source_key\": \"api87\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87\"\
    ,\n          \"source_raw_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"source_text_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.974764Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 7,\\n                        \\\"amount\\\": 0.05,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.0473485,\\n                        \\\"mmol_l\\\": 0.322066,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n          \"\
    quote_representation\": \"raw JSON object\"\n        }\n      ]\n    },\n    {\n\
    \      \"decision_id\": \"q24\",\n      \"subject\": \"CaCl2 x 2 H2O in strain-13941\
    \ owner\",\n      \"local_fields\": [\n        {\n          \"record_path\": \"\
    data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\",\n   \
    \       \"field_path\": \"ingredients[7].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.047619\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n    \
    \  \"stage\": \"Unresolved strain variant\",\n      \"interpretation\": \"The\
    \ stored scalar matches base 87a, but the variant recipe remains unavailable.\
    \ Base-source agreement is contextual and does not authenticate an unknown strain\
    \ modification or final-volume basis.\",\n      \"sources\": [\n        {\n  \
    \        \"locator\": \"$.data.solutions[0].recipe[7]\",\n          \"source_key\"\
    : \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 7,\\n                        \\\"amount\\\": 0.05,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.047619,\\n                        \\\"mmol_l\\\": 0.323906,\\n         \
    \               \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 11-11\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O                                                     0.05   \
    \     g\",\n          \"quote_representation\": \"captured extracted text\"\n\
    \        }\n      ]\n    },\n    {\n      \"decision_id\": \"q25\",\n      \"\
    subject\": \"Fe(III) citrate solution\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[8].concentration\",\n          \"original\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[8].concentration\",\n          \"original\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[8].concentration\",\n          \"original\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[8].concentration\",\n          \"original\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"stage\"\
    : \"Separate stock and receiving dose\",\n      \"interpretation\": \"The source\
    \ specifies 5 ml of solution prepared with 0.1 g in 100 ml water, not 5 g/L of\
    \ Fe(III) citrate in the medium. Preserve the supplied complex identity and separate\
    \ stock recipe from receiving batch dose. Do not infer a measured final volume\
    \ or assert a final mass-per-litre conversion.\",\n      \"sources\": [\n    \
    \    {\n          \"locator\": \"$.data.solutions[0].recipe[8]\",\n          \"\
    source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Fe(III) citrate\\\",\\n                        \\\
    \"compound_id\\\": 45,\\n                        \\\"attribute\\\": \\\"0.1 g\
    \ in 100 ml H2O\\\",\\n                        \\\"amount\\\": 5,\\n         \
    \               \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n          \"quote_representation\": \"raw JSON\
    \ object\"\n        },\n        {\n          \"locator\": \"extracted-text lines\
    \ 12-13\",\n          \"source_key\": \"dsmz87\",\n          \"reference\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n         \
    \ \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Fe(III) citrate solution\\n(0.1 g in 100 ml H2O)                         \
    \                    5.00      ml\",\n          \"quote_representation\": \"captured\
    \ extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\":\
    \ \"q26\",\n      \"subject\": \"Fe(III) citrate in unresolved strain variant\"\
    ,\n      \"local_fields\": [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[8].concentration\",\n          \"original\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        }\n      ],\n      \"decision\": \"unsupported\",\n      \"stage\"\
    : \"Variant stock stage\",\n      \"interpretation\": \"The base source demonstrates\
    \ a stock/dose representation problem, but the exact variant cannot be reconstructed\
    \ from a copied signature. Keep 5 G_PER_L unsupported rather than manufacture\
    \ a variant-specific replacement.\",\n      \"sources\": [\n        {\n      \
    \    \"locator\": \"$.data.solutions[0].recipe[8]\",\n          \"source_key\"\
    : \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Fe(III) citrate\\\",\\n                        \\\
    \"compound_id\\\": 45,\\n                        \\\"attribute\\\": \\\"0.1 g\
    \ in 100 ml H2O\\\",\\n                        \\\"amount\\\": 5,\\n         \
    \               \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n          \"quote_representation\": \"raw JSON\
    \ object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\": \"q27\"\
    ,\n      \"subject\": \"Nicotinic acid flattened CA component\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[9].concentration\",\n          \"original\"\
    : {\n            \"value\": \"1\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"stage\"\
    : \"Vitamin solution CA, not basal final concentration\",\n      \"interpretation\"\
    : \"The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L\
    \ value equals provider stock g_l, not the receiving-medium concentration. Restore\
    \ the complete nine-component stock and retain the explicit 1 ml/litre receiving\
    \ dose separately; do not infer a physical final stock volume merely from water.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[1]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"Nicotinic acid\\\",\\n                        \\\"\
    compound_id\\\": 139,\\n                        \\\"amount\\\": 100,\\n      \
    \                  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 1,\\n                        \\\"mmol_l\\\": 8.12282,\\n                 \
    \       \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 8-8\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Nicotinic acid                                              100.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q28\",\n      \"subject\": \"\
    Nicotinic acid already nested CA component\",\n      \"local_fields\": [\n   \
    \     {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"solutions[0].composition[0].concentration\",\n\
    \          \"original\": {\n            \"value\": \"1\",\n            \"unit\"\
    : \"G_PER_L\"\n          }\n        },\n        {\n          \"record_path\":\
    \ \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\",\n   \
    \       \"field_path\": \"solutions[0].composition[0].concentration\",\n     \
    \     \"original\": {\n            \"value\": \"1\",\n            \"unit\": \"\
    G_PER_L\"\n          }\n        }\n      ],\n      \"decision\": \"evidence_only\"\
    ,\n      \"stage\": \"Already repaired stock composition\",\n      \"interpretation\"\
    : \"The current owner correctly places this component under Vitamin solution CA\
    \ and its value matches provider stock g_l. Credit this partial repair and preserve\
    \ it while adding the four omitted CA components; do not flatten it again.\",\n\
    \      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[1]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"Nicotinic acid\\\",\\n                        \\\"\
    compound_id\\\": 139,\\n                        \\\"amount\\\": 100,\\n      \
    \                  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 1,\\n                        \\\"mmol_l\\\": 8.12282,\\n                 \
    \       \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 8-8\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Nicotinic acid                                              100.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q29\",\n      \"subject\": \"\
    Nicotinic acid in source-87 and strain-variant owners\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[9].concentration\",\n          \"original\"\
    : {\n            \"value\": \"1\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"solutions[0].composition[0].concentration\",\n\
    \          \"original\": {\n            \"value\": \"1\",\n            \"unit\"\
    : \"G_PER_L\"\n          }\n        }\n      ],\n      \"decision\": \"unsupported\"\
    ,\n      \"stage\": \"Distinct source branches\",\n      \"interpretation\": \"\
    The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe\
    \ is unavailable. These owner fields cannot be authenticated by base-87a stock\
    \ membership alone. The strain owner already nests five components and retains\
    \ its dose as a candidate; this useful uncertainty is preserved.\",\n      \"\
    sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[1]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"Nicotinic acid\\\",\\n                        \\\"\
    compound_id\\\": 139,\\n                        \\\"amount\\\": 100,\\n      \
    \                  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 1,\\n                        \\\"mmol_l\\\": 8.12282,\\n                 \
    \       \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 8-8\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Nicotinic acid                                              100.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q30\",\n      \"subject\": \"\
    Thiamine-HCl x 2 H2O flattened CA component\",\n      \"local_fields\": [\n  \
    \      {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[10].concentration\",\n          \"\
    original\": {\n            \"value\": \"1\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"Vitamin solution CA, not basal final concentration\",\n      \"interpretation\"\
    : \"The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L\
    \ value equals provider stock g_l, not the receiving-medium concentration. Restore\
    \ the complete nine-component stock and retain the explicit 1 ml/litre receiving\
    \ dose separately; do not infer a physical final stock volume merely from water.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[2]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Thiamine-HCl x 2 H2O\\\",\\n                    \
    \    \\\"compound_id\\\": 77,\\n                        \\\"amount\\\": 100,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 1,\\n                        \\\"mmol_l\\\": 2.6788,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 9-9\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Thiamine-HCl x 2 H2O                                        100.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q31\",\n      \"subject\": \"\
    Thiamine-HCl x 2 H2O already nested CA component\",\n      \"local_fields\": [\n\
    \        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"solutions[0].composition[1].concentration\",\n\
    \          \"original\": {\n            \"value\": \"1\",\n            \"unit\"\
    : \"G_PER_L\"\n          }\n        },\n        {\n          \"record_path\":\
    \ \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\",\n   \
    \       \"field_path\": \"solutions[0].composition[1].concentration\",\n     \
    \     \"original\": {\n            \"value\": \"1\",\n            \"unit\": \"\
    G_PER_L\"\n          }\n        }\n      ],\n      \"decision\": \"evidence_only\"\
    ,\n      \"stage\": \"Already repaired stock composition\",\n      \"interpretation\"\
    : \"The current owner correctly places this component under Vitamin solution CA\
    \ and its value matches provider stock g_l. Credit this partial repair and preserve\
    \ it while adding the four omitted CA components; do not flatten it again.\",\n\
    \      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[2]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Thiamine-HCl x 2 H2O\\\",\\n                    \
    \    \\\"compound_id\\\": 77,\\n                        \\\"amount\\\": 100,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 1,\\n                        \\\"mmol_l\\\": 2.6788,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 9-9\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Thiamine-HCl x 2 H2O                                        100.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q32\",\n      \"subject\": \"\
    Thiamine-HCl x 2 H2O in source-87 and strain-variant owners\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[10].concentration\",\n          \"\
    original\": {\n            \"value\": \"1\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"solutions[0].composition[1].concentration\",\n\
    \          \"original\": {\n            \"value\": \"1\",\n            \"unit\"\
    : \"G_PER_L\"\n          }\n        }\n      ],\n      \"decision\": \"unsupported\"\
    ,\n      \"stage\": \"Distinct source branches\",\n      \"interpretation\": \"\
    The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe\
    \ is unavailable. These owner fields cannot be authenticated by base-87a stock\
    \ membership alone. The strain owner already nests five components and retains\
    \ its dose as a candidate; this useful uncertainty is preserved.\",\n      \"\
    sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[2]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Thiamine-HCl x 2 H2O\\\",\\n                    \
    \    \\\"compound_id\\\": 77,\\n                        \\\"amount\\\": 100,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 1,\\n                        \\\"mmol_l\\\": 2.6788,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 9-9\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Thiamine-HCl x 2 H2O                                        100.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q33\",\n      \"subject\": \"\
    Biotin flattened CA component\",\n      \"local_fields\": [\n        {\n     \
    \     \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[11].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.05\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[9].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.05\",\n            \"unit\": \"G_PER_L\"\n   \
    \       }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[9].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.05\",\n            \"unit\": \"G_PER_L\"\n   \
    \       }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"stage\"\
    : \"Vitamin solution CA, not basal final concentration\",\n      \"interpretation\"\
    : \"The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L\
    \ value equals provider stock g_l, not the receiving-medium concentration. Restore\
    \ the complete nine-component stock and retain the explicit 1 ml/litre receiving\
    \ dose separately; do not infer a physical final stock volume merely from water.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[3]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"Biotin\\\",\\n                        \\\"compound_id\\\
    \": 46,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.05,\\n \
    \                       \\\"mmol_l\\\": 0.204658,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 10-10\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Biotin                                                        5.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q34\",\n      \"subject\": \"\
    Biotin in source-87 and strain-variant owners\",\n      \"local_fields\": [\n\
    \        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[11].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.05\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[9].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.05\",\n            \"unit\": \"G_PER_L\"\n   \
    \       }\n        }\n      ],\n      \"decision\": \"unsupported\",\n      \"\
    stage\": \"Distinct source branches\",\n      \"interpretation\": \"The source-87\
    \ primary lacks CA; 87a explicitly adds it. The strain-13941 recipe is unavailable.\
    \ These owner fields cannot be authenticated by base-87a stock membership alone.\
    \ The strain owner already nests five components and retains its dose as a candidate;\
    \ this useful uncertainty is preserved.\",\n      \"sources\": [\n        {\n\
    \          \"locator\": \"$.data.solutions[1].recipe[3]\",\n          \"source_key\"\
    : \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"Biotin\\\",\\n                        \\\"compound_id\\\
    \": 46,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.05,\\n \
    \                       \\\"mmol_l\\\": 0.204658,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 10-10\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Biotin                                                        5.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q35\",\n      \"subject\": \"\
    p-Aminobenzoic acid flattened CA component\",\n      \"local_fields\": [\n   \
    \     {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[12].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.5\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"Vitamin solution CA, not basal final concentration\",\n      \"interpretation\"\
    : \"The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L\
    \ value equals provider stock g_l, not the receiving-medium concentration. Restore\
    \ the complete nine-component stock and retain the explicit 1 ml/litre receiving\
    \ dose separately; do not infer a physical final stock volume merely from water.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[4]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"p-Aminobenzoic acid\\\",\\n                     \
    \   \\\"compound_id\\\": 47,\\n                        \\\"amount\\\": 50,\\n\
    \                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.5,\\n                        \\\"mmol_l\\\": 3.64591,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n          \"\
    quote_representation\": \"raw JSON object\"\n        },\n        {\n         \
    \ \"locator\": \"extracted-text lines 11-11\",\n          \"source_key\": \"dsmz87a\"\
    ,\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\"\
    ,\n          \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"p-Aminobenzoic acid                                          50.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q36\",\n      \"subject\": \"\
    p-Aminobenzoic acid already nested CA component\",\n      \"local_fields\": [\n\
    \        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"solutions[0].composition[2].concentration\",\n\
    \          \"original\": {\n            \"value\": \"0.5\",\n            \"unit\"\
    : \"G_PER_L\"\n          }\n        },\n        {\n          \"record_path\":\
    \ \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\",\n   \
    \       \"field_path\": \"solutions[0].composition[2].concentration\",\n     \
    \     \"original\": {\n            \"value\": \"0.5\",\n            \"unit\":\
    \ \"G_PER_L\"\n          }\n        }\n      ],\n      \"decision\": \"evidence_only\"\
    ,\n      \"stage\": \"Already repaired stock composition\",\n      \"interpretation\"\
    : \"The current owner correctly places this component under Vitamin solution CA\
    \ and its value matches provider stock g_l. Credit this partial repair and preserve\
    \ it while adding the four omitted CA components; do not flatten it again.\",\n\
    \      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[4]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"p-Aminobenzoic acid\\\",\\n                     \
    \   \\\"compound_id\\\": 47,\\n                        \\\"amount\\\": 50,\\n\
    \                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.5,\\n                        \\\"mmol_l\\\": 3.64591,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n          \"\
    quote_representation\": \"raw JSON object\"\n        },\n        {\n         \
    \ \"locator\": \"extracted-text lines 11-11\",\n          \"source_key\": \"dsmz87a\"\
    ,\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\"\
    ,\n          \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"p-Aminobenzoic acid                                          50.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q37\",\n      \"subject\": \"\
    p-Aminobenzoic acid in source-87 and strain-variant owners\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[12].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.5\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"solutions[0].composition[2].concentration\",\n\
    \          \"original\": {\n            \"value\": \"0.5\",\n            \"unit\"\
    : \"G_PER_L\"\n          }\n        }\n      ],\n      \"decision\": \"unsupported\"\
    ,\n      \"stage\": \"Distinct source branches\",\n      \"interpretation\": \"\
    The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe\
    \ is unavailable. These owner fields cannot be authenticated by base-87a stock\
    \ membership alone. The strain owner already nests five components and retains\
    \ its dose as a candidate; this useful uncertainty is preserved.\",\n      \"\
    sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[4]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"p-Aminobenzoic acid\\\",\\n                     \
    \   \\\"compound_id\\\": 47,\\n                        \\\"amount\\\": 50,\\n\
    \                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.5,\\n                        \\\"mmol_l\\\": 3.64591,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n          \"\
    quote_representation\": \"raw JSON object\"\n        },\n        {\n         \
    \ \"locator\": \"extracted-text lines 11-11\",\n          \"source_key\": \"dsmz87a\"\
    ,\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\"\
    ,\n          \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"p-Aminobenzoic acid                                          50.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q38\",\n      \"subject\": \"\
    Vitamin B12 flattened CA component\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[13].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[10].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[10].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"Vitamin solution CA, not basal final concentration\",\n      \"interpretation\"\
    : \"The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L\
    \ value equals provider stock g_l, not the receiving-medium concentration. Restore\
    \ the complete nine-component stock and retain the explicit 1 ml/litre receiving\
    \ dose separately; do not infer a physical final stock volume merely from water.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[5]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"Vitamin B12\\\",\\n                        \\\"compound_id\\\
    \": 18,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.01,\\n \
    \                       \\\"mmol_l\\\": 0.0073779,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 12-12\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Vitamin B12                                                   1.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q39\",\n      \"subject\": \"\
    Vitamin B12 in source-87 and strain-variant owners\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[13].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[10].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n   \
    \   \"stage\": \"Distinct source branches\",\n      \"interpretation\": \"The\
    \ source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe\
    \ is unavailable. These owner fields cannot be authenticated by base-87a stock\
    \ membership alone. The strain owner already nests five components and retains\
    \ its dose as a candidate; this useful uncertainty is preserved.\",\n      \"\
    sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[5]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"Vitamin B12\\\",\\n                        \\\"compound_id\\\
    \": 18,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.01,\\n \
    \                       \\\"mmol_l\\\": 0.0073779,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 12-12\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Vitamin B12                                                   1.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q40\",\n      \"subject\": \"\
    Calcium pantothenate flattened CA component\",\n      \"local_fields\": [\n  \
    \      {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[14].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.5\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[11].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.5\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[11].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.5\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"Vitamin solution CA, not basal final concentration\",\n      \"interpretation\"\
    : \"The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L\
    \ value equals provider stock g_l, not the receiving-medium concentration. Restore\
    \ the complete nine-component stock and retain the explicit 1 ml/litre receiving\
    \ dose separately; do not infer a physical final stock volume merely from water.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[6]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"Calcium pantothenate\\\",\\n                    \
    \    \\\"compound_id\\\": 518,\\n                        \\\"amount\\\": 50,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.5,\\n                        \\\"mmol_l\\\": 1.04925,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n          \"\
    quote_representation\": \"raw JSON object\"\n        },\n        {\n         \
    \ \"locator\": \"extracted-text lines 13-13\",\n          \"source_key\": \"dsmz87a\"\
    ,\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\"\
    ,\n          \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Ca-pantothenate                                              50.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q41\",\n      \"subject\": \"\
    Calcium pantothenate in source-87 and strain-variant owners\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[14].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.5\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[11].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.5\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n   \
    \   \"stage\": \"Distinct source branches\",\n      \"interpretation\": \"The\
    \ source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe\
    \ is unavailable. These owner fields cannot be authenticated by base-87a stock\
    \ membership alone. The strain owner already nests five components and retains\
    \ its dose as a candidate; this useful uncertainty is preserved.\",\n      \"\
    sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[6]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"Calcium pantothenate\\\",\\n                    \
    \    \\\"compound_id\\\": 518,\\n                        \\\"amount\\\": 50,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.5,\\n                        \\\"mmol_l\\\": 1.04925,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n          \"\
    quote_representation\": \"raw JSON object\"\n        },\n        {\n         \
    \ \"locator\": \"extracted-text lines 13-13\",\n          \"source_key\": \"dsmz87a\"\
    ,\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\"\
    ,\n          \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Ca-pantothenate                                              50.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q42\",\n      \"subject\": \"\
    Pyridoxine hydrochloride flattened CA component\",\n      \"local_fields\": [\n\
    \        {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[15].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.5\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"Vitamin solution CA, not basal final concentration\",\n      \"interpretation\"\
    : \"The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L\
    \ value equals provider stock g_l, not the receiving-medium concentration. Restore\
    \ the complete nine-component stock and retain the explicit 1 ml/litre receiving\
    \ dose separately; do not infer a physical final stock volume merely from water.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[7]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"Pyridoxine hydrochloride\\\",\\n                \
    \        \\\"compound_id\\\": 519,\\n                        \\\"amount\\\": 50,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.5,\\n                        \\\"mmol_l\\\": 2.43143,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n          \"\
    quote_representation\": \"raw JSON object\"\n        },\n        {\n         \
    \ \"locator\": \"extracted-text lines 14-14\",\n          \"source_key\": \"dsmz87a\"\
    ,\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\"\
    ,\n          \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Pyridoxine-HCl                                               50.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q43\",\n      \"subject\": \"\
    Pyridoxine hydrochloride already nested CA component\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"solutions[0].composition[3].concentration\",\n\
    \          \"original\": {\n            \"value\": \"0.5\",\n            \"unit\"\
    : \"G_PER_L\"\n          }\n        },\n        {\n          \"record_path\":\
    \ \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\",\n   \
    \       \"field_path\": \"solutions[0].composition[3].concentration\",\n     \
    \     \"original\": {\n            \"value\": \"0.5\",\n            \"unit\":\
    \ \"G_PER_L\"\n          }\n        }\n      ],\n      \"decision\": \"evidence_only\"\
    ,\n      \"stage\": \"Already repaired stock composition\",\n      \"interpretation\"\
    : \"The current owner correctly places this component under Vitamin solution CA\
    \ and its value matches provider stock g_l. Credit this partial repair and preserve\
    \ it while adding the four omitted CA components; do not flatten it again.\",\n\
    \      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[7]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"Pyridoxine hydrochloride\\\",\\n                \
    \        \\\"compound_id\\\": 519,\\n                        \\\"amount\\\": 50,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.5,\\n                        \\\"mmol_l\\\": 2.43143,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n          \"\
    quote_representation\": \"raw JSON object\"\n        },\n        {\n         \
    \ \"locator\": \"extracted-text lines 14-14\",\n          \"source_key\": \"dsmz87a\"\
    ,\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\"\
    ,\n          \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Pyridoxine-HCl                                               50.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q44\",\n      \"subject\": \"\
    Pyridoxine hydrochloride in source-87 and strain-variant owners\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[15].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.5\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"solutions[0].composition[3].concentration\",\n\
    \          \"original\": {\n            \"value\": \"0.5\",\n            \"unit\"\
    : \"G_PER_L\"\n          }\n        }\n      ],\n      \"decision\": \"unsupported\"\
    ,\n      \"stage\": \"Distinct source branches\",\n      \"interpretation\": \"\
    The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe\
    \ is unavailable. These owner fields cannot be authenticated by base-87a stock\
    \ membership alone. The strain owner already nests five components and retains\
    \ its dose as a candidate; this useful uncertainty is preserved.\",\n      \"\
    sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[7]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"Pyridoxine hydrochloride\\\",\\n                \
    \        \\\"compound_id\\\": 519,\\n                        \\\"amount\\\": 50,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.5,\\n                        \\\"mmol_l\\\": 2.43143,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n          \"\
    quote_representation\": \"raw JSON object\"\n        },\n        {\n         \
    \ \"locator\": \"extracted-text lines 14-14\",\n          \"source_key\": \"dsmz87a\"\
    ,\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\"\
    ,\n          \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Pyridoxine-HCl                                               50.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q45\",\n      \"subject\": \"\
    Folic acid flattened CA component\",\n      \"local_fields\": [\n        {\n \
    \         \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[16].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.5\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"Vitamin solution CA, not basal final concentration\",\n      \"interpretation\"\
    : \"The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L\
    \ value equals provider stock g_l, not the receiving-medium concentration. Restore\
    \ the complete nine-component stock and retain the explicit 1 ml/litre receiving\
    \ dose separately; do not infer a physical final stock volume merely from water.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[8]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Folic acid\\\",\\n                        \\\"compound_id\\\
    \": 138,\\n                        \\\"amount\\\": 50,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.5,\\n\
    \                        \\\"mmol_l\\\": 1.13276,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 15-15\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Folic acid                                                   50.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q46\",\n      \"subject\": \"\
    Folic acid already nested CA component\",\n      \"local_fields\": [\n       \
    \ {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"solutions[0].composition[4].concentration\",\n\
    \          \"original\": {\n            \"value\": \"0.5\",\n            \"unit\"\
    : \"G_PER_L\"\n          }\n        },\n        {\n          \"record_path\":\
    \ \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\",\n   \
    \       \"field_path\": \"solutions[0].composition[4].concentration\",\n     \
    \     \"original\": {\n            \"value\": \"0.5\",\n            \"unit\":\
    \ \"G_PER_L\"\n          }\n        }\n      ],\n      \"decision\": \"evidence_only\"\
    ,\n      \"stage\": \"Already repaired stock composition\",\n      \"interpretation\"\
    : \"The current owner correctly places this component under Vitamin solution CA\
    \ and its value matches provider stock g_l. Credit this partial repair and preserve\
    \ it while adding the four omitted CA components; do not flatten it again.\",\n\
    \      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[8]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Folic acid\\\",\\n                        \\\"compound_id\\\
    \": 138,\\n                        \\\"amount\\\": 50,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.5,\\n\
    \                        \\\"mmol_l\\\": 1.13276,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 15-15\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Folic acid                                                   50.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q47\",\n      \"subject\": \"\
    Folic acid in source-87 and strain-variant owners\",\n      \"local_fields\":\
    \ [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[16].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.5\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"solutions[0].composition[4].concentration\",\n\
    \          \"original\": {\n            \"value\": \"0.5\",\n            \"unit\"\
    : \"G_PER_L\"\n          }\n        }\n      ],\n      \"decision\": \"unsupported\"\
    ,\n      \"stage\": \"Distinct source branches\",\n      \"interpretation\": \"\
    The source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe\
    \ is unavailable. These owner fields cannot be authenticated by base-87a stock\
    \ membership alone. The strain owner already nests five components and retains\
    \ its dose as a candidate; this useful uncertainty is preserved.\",\n      \"\
    sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[8]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Folic acid\\\",\\n                        \\\"compound_id\\\
    \": 138,\\n                        \\\"amount\\\": 50,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.5,\\n\
    \                        \\\"mmol_l\\\": 1.13276,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 15-15\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Folic acid                                                   50.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q48\",\n      \"subject\": \"\
    Na3-EDTA flattened CA component\",\n      \"local_fields\": [\n        {\n   \
    \       \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[17].concentration\",\n          \"\
    original\": {\n            \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[12].concentration\",\n          \"\
    original\": {\n            \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[12].concentration\",\n          \"\
    original\": {\n            \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"Vitamin solution CA, not basal final concentration\",\n      \"interpretation\"\
    : \"The primary mass belongs to the 100 ml-water CA stock. The stored G_PER_L\
    \ value equals provider stock g_l, not the receiving-medium concentration. Restore\
    \ the complete nine-component stock and retain the explicit 1 ml/litre receiving\
    \ dose separately; do not infer a physical final stock volume merely from water.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[9]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 10,\\n                 \
    \       \\\"compound\\\": \\\"Na3-EDTA\\\",\\n                        \\\"compound_id\\\
    \": 194,\\n                        \\\"amount\\\": 200,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 2,\\n \
    \                       \\\"mmol_l\\\": 5.58366,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 16-16\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Na3-EDTA                                                    200.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q49\",\n      \"subject\": \"\
    Na3-EDTA in source-87 and strain-variant owners\",\n      \"local_fields\": [\n\
    \        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[17].concentration\",\n          \"\
    original\": {\n            \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[12].concentration\",\n          \"\
    original\": {\n            \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n   \
    \   \"stage\": \"Distinct source branches\",\n      \"interpretation\": \"The\
    \ source-87 primary lacks CA; 87a explicitly adds it. The strain-13941 recipe\
    \ is unavailable. These owner fields cannot be authenticated by base-87a stock\
    \ membership alone. The strain owner already nests five components and retains\
    \ its dose as a candidate; this useful uncertainty is preserved.\",\n      \"\
    sources\": [\n        {\n          \"locator\": \"$.data.solutions[1].recipe[9]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 10,\\n                 \
    \       \\\"compound\\\": \\\"Na3-EDTA\\\",\\n                        \\\"compound_id\\\
    \": 194,\\n                        \\\"amount\\\": 200,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 2,\\n \
    \                       \\\"mmol_l\\\": 5.58366,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 16-16\",\n          \"source_key\": \"dsmz87a\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\",\n    \
    \      \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Na3-EDTA                                                    200.0   mg\",\n\
    \          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q50\",\n      \"subject\": \"\
    ZnSO4 x 7 H2O SL-6 component\",\n      \"local_fields\": [\n        {\n      \
    \    \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[18].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.1\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[18].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.1\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[13].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.1\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[13].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.1\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"SL-6 stock composition\",\n      \"interpretation\": \"The quoted amount\
    \ is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving\
    \ addition in medium 87. The flat G_PER_L is a provider stock-strength value,\
    \ not final-medium concentration. Preserve all supplied hydrates; do not adopt\
    \ provider mmol_l values that may use a different formula.\",\n      \"sources\"\
    : [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[0]\",\n  \
    \        \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 35,\\n                        \\\"amount\\\": 0.1,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.1,\\n                        \\\"mmol_l\\\": 0.347752,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 26-26\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"ZnSO4 x 7 H2O                                                0.10        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q51\",\n      \"subject\": \"\
    ZnSO4 x 7 H2O in strain-13941 owner\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[13].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.1\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n   \
    \   \"stage\": \"Unresolved variant and stock scope\",\n      \"interpretation\"\
    : \"The value agrees with base SL-6 stock composition, but the variant source\
    \ and receiving dose are not authenticated. It must not be certified as a final-medium\
    \ rate.\",\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[0]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 35,\\n                        \\\"amount\\\": 0.1,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.1,\\n                        \\\"mmol_l\\\": 0.347752,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 26-26\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"ZnSO4 x 7 H2O                                                0.10        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q52\",\n      \"subject\": \"\
    MnCl2 x 4 H2O SL-6 component\",\n      \"local_fields\": [\n        {\n      \
    \    \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[19].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.03\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[19].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.03\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[14].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.03\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[14].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.03\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"SL-6 stock composition\",\n      \"interpretation\": \"The quoted amount\
    \ is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving\
    \ addition in medium 87. The flat G_PER_L is a provider stock-strength value,\
    \ not final-medium concentration. Preserve all supplied hydrates; do not adopt\
    \ provider mmol_l values that may use a different formula.\",\n      \"sources\"\
    : [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[1]\",\n  \
    \        \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"\
    compound_id\\\": 36,\\n                        \\\"amount\\\": 0.03,\\n      \
    \                  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.03,\\n                        \\\"mmol_l\\\": 0.151588,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 27-27\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O                                                0.03        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q53\",\n      \"subject\": \"\
    MnCl2 x 4 H2O in strain-13941 owner\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[14].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.03\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n   \
    \   \"stage\": \"Unresolved variant and stock scope\",\n      \"interpretation\"\
    : \"The value agrees with base SL-6 stock composition, but the variant source\
    \ and receiving dose are not authenticated. It must not be certified as a final-medium\
    \ rate.\",\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[1]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"\
    compound_id\\\": 36,\\n                        \\\"amount\\\": 0.03,\\n      \
    \                  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.03,\\n                        \\\"mmol_l\\\": 0.151588,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 27-27\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O                                                0.03        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q54\",\n      \"subject\": \"\
    H3BO3 SL-6 component\",\n      \"local_fields\": [\n        {\n          \"record_path\"\
    : \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\",\n          \"\
    field_path\": \"ingredients[20].concentration\",\n          \"original\": {\n\
    \            \"value\": \"0.3\",\n            \"unit\": \"G_PER_L\"\n        \
    \  }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[20].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.3\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[15].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.3\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[15].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.3\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"SL-6 stock composition\",\n      \"interpretation\": \"The quoted amount\
    \ is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving\
    \ addition in medium 87. The flat G_PER_L is a provider stock-strength value,\
    \ not final-medium concentration. Preserve all supplied hydrates; do not adopt\
    \ provider mmol_l values that may use a different formula.\",\n      \"sources\"\
    : [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[2]\",\n  \
    \        \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\
    \": 37,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n \
    \                       \\\"mmol_l\\\": 4.85123,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 28-28\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"H3BO3                                                        0.30        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q55\",\n      \"subject\": \"\
    H3BO3 in strain-13941 owner\",\n      \"local_fields\": [\n        {\n       \
    \   \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[15].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.3\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n   \
    \   \"stage\": \"Unresolved variant and stock scope\",\n      \"interpretation\"\
    : \"The value agrees with base SL-6 stock composition, but the variant source\
    \ and receiving dose are not authenticated. It must not be certified as a final-medium\
    \ rate.\",\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[2]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\
    \": 37,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n \
    \                       \\\"mmol_l\\\": 4.85123,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 28-28\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"H3BO3                                                        0.30        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q56\",\n      \"subject\": \"\
    CoCl2 x 6 H2O SL-6 component\",\n      \"local_fields\": [\n        {\n      \
    \    \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[21].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.2\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[21].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.2\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[16].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.2\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[16].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.2\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"SL-6 stock composition\",\n      \"interpretation\": \"The quoted amount\
    \ is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving\
    \ addition in medium 87. The flat G_PER_L is a provider stock-strength value,\
    \ not final-medium concentration. Preserve all supplied hydrates; do not adopt\
    \ provider mmol_l values that may use a different formula.\",\n      \"sources\"\
    : [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[3]\",\n  \
    \        \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 38,\\n                        \\\"amount\\\": 0.2,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.2,\\n                        \\\"mmol_l\\\": 1.54037,\\n               \
    \         \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 29-29\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O                                                0.20        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q57\",\n      \"subject\": \"\
    CoCl2 x 6 H2O in strain-13941 owner\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[16].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.2\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n   \
    \   \"stage\": \"Unresolved variant and stock scope\",\n      \"interpretation\"\
    : \"The value agrees with base SL-6 stock composition, but the variant source\
    \ and receiving dose are not authenticated. It must not be certified as a final-medium\
    \ rate.\",\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[3]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 38,\\n                        \\\"amount\\\": 0.2,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.2,\\n                        \\\"mmol_l\\\": 1.54037,\\n               \
    \         \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 29-29\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O                                                0.20        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q58\",\n      \"subject\": \"\
    CuCl2 x 2 H2O SL-6 component\",\n      \"local_fields\": [\n        {\n      \
    \    \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[22].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[22].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[17].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[17].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"SL-6 stock composition\",\n      \"interpretation\": \"The quoted amount\
    \ is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving\
    \ addition in medium 87. The flat G_PER_L is a provider stock-strength value,\
    \ not final-medium concentration. Preserve all supplied hydrates; do not adopt\
    \ provider mmol_l values that may use a different formula.\",\n      \"sources\"\
    : [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[4]\",\n  \
    \        \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 39,\\n                        \\\"amount\\\": 0.01,\\n      \
    \                  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.01,\\n                        \\\"mmol_l\\\": 0.0586569,\\n            \
    \            \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 30-30\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"CuCl2 x 2 H2O                                                0.01        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q59\",\n      \"subject\": \"\
    CuCl2 x 2 H2O in strain-13941 owner\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[17].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.01\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n   \
    \   \"stage\": \"Unresolved variant and stock scope\",\n      \"interpretation\"\
    : \"The value agrees with base SL-6 stock composition, but the variant source\
    \ and receiving dose are not authenticated. It must not be certified as a final-medium\
    \ rate.\",\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[4]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 39,\\n                        \\\"amount\\\": 0.01,\\n      \
    \                  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.01,\\n                        \\\"mmol_l\\\": 0.0586569,\\n            \
    \            \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 30-30\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"CuCl2 x 2 H2O                                                0.01        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q60\",\n      \"subject\": \"\
    NiCl2 x 6 H2O SL-6 component\",\n      \"local_fields\": [\n        {\n      \
    \    \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[23].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.02\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[23].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.02\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[18].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.02\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[18].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.02\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"SL-6 stock composition\",\n      \"interpretation\": \"The quoted amount\
    \ is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving\
    \ addition in medium 87. The flat G_PER_L is a provider stock-strength value,\
    \ not final-medium concentration. Preserve all supplied hydrates; do not adopt\
    \ provider mmol_l values that may use a different formula.\",\n      \"sources\"\
    : [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[5]\",\n  \
    \        \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 40,\\n                        \\\"amount\\\": 0.02,\\n      \
    \                  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.02,\\n                        \\\"mmol_l\\\": 0.154322,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 31-31\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O                                                0.02        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q61\",\n      \"subject\": \"\
    NiCl2 x 6 H2O in strain-13941 owner\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[18].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.02\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n   \
    \   \"stage\": \"Unresolved variant and stock scope\",\n      \"interpretation\"\
    : \"The value agrees with base SL-6 stock composition, but the variant source\
    \ and receiving dose are not authenticated. It must not be certified as a final-medium\
    \ rate.\",\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[5]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 40,\\n                        \\\"amount\\\": 0.02,\\n      \
    \                  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.02,\\n                        \\\"mmol_l\\\": 0.154322,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 31-31\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O                                                0.02        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q62\",\n      \"subject\": \"\
    Na2MoO4 x 2 H2O SL-6 component\",\n      \"local_fields\": [\n        {\n    \
    \      \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[24].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.03\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[24].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.03\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[19].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.03\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[19].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.03\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"SL-6 stock composition\",\n      \"interpretation\": \"The quoted amount\
    \ is an SL-6 stock ingredient with 1000 ml listed water and a separate 1 ml receiving\
    \ addition in medium 87. The flat G_PER_L is a provider stock-strength value,\
    \ not final-medium concentration. Preserve all supplied hydrates; do not adopt\
    \ provider mmol_l values that may use a different formula.\",\n      \"sources\"\
    : [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[6]\",\n  \
    \        \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\
    \"compound_id\\\": 9,\\n                        \\\"amount\\\": 0.03,\\n     \
    \                   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.03,\\n                        \\\"mmol_l\\\": 0.123993,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 32-32\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O                                              0.03        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q63\",\n      \"subject\": \"\
    Na2MoO4 x 2 H2O in strain-13941 owner\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[19].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.03\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n   \
    \   \"stage\": \"Unresolved variant and stock scope\",\n      \"interpretation\"\
    : \"The value agrees with base SL-6 stock composition, but the variant source\
    \ and receiving dose are not authenticated. It must not be certified as a final-medium\
    \ rate.\",\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[2].recipe[6]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\
    \"compound_id\\\": 9,\\n                        \\\"amount\\\": 0.03,\\n     \
    \                   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.03,\\n                        \\\"mmol_l\\\": 0.123993,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 32-32\",\n          \"source_key\": \"dsmz27\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\",\n     \
    \     \"source_raw_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n          \"source_text_sha256\": \"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:39:36.126235Z\",\n          \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O                                              0.03        g\"\
    ,\n          \"quote_representation\": \"captured extracted text\"\n        }\n\
    \      ]\n    },\n    {\n      \"decision_id\": \"q64\",\n      \"subject\": \"\
    Neutralized sulfide stock\",\n      \"local_fields\": [\n        {\n         \
    \ \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ingredients[25].concentration\",\n          \"\
    original\": {\n            \"value\": \"30\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ingredients[25].concentration\",\n          \"\
    original\": {\n            \"value\": \"30\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[20].concentration\",\n          \"\
    original\": {\n            \"value\": \"30\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ingredients[20].concentration\",\n          \"\
    original\": {\n            \"value\": \"30\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"correct\",\n      \"\
    stage\": \"Separate neutralized stock and later injection\",\n      \"interpretation\"\
    : \"3 g nonahydrate with 100 ml water is the stock recipe; API calls it 3% (w/v)\
    \ and reports 30 g/L on its stock basis. The flat 30 G_PER_L cannot describe the\
    \ receiving medium. Preserve post-autoclave injection and source nominal 0.03%\
    \ end concentration separately; the PDF does not explicitly type that end percentage.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[3].recipe[1]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"Na2S x 9 H2O\\\",\\n                        \\\"\
    compound_id\\\": 54,\\n                        \\\"amount\\\": 3,\\n         \
    \               \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 30,\\n                        \\\"mmol_l\\\": 124.905,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 30-30\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Na2S x 9 H2O                                                      3.00   \
    \    g\",\n          \"quote_representation\": \"captured extracted text\"\n \
    \       },\n        {\n          \"locator\": \"$.data.solutions[0].steps[1]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Boil the medium under a stream\
    \ of nitrogen gas for a few minutes and distribute 90 ml medium into 100 ml screw-capped\
    \ bottles. Bubble each bottle with nitrogen gas and close immediately with a rubber\
    \ septum and screw tight. Autoclave at 121\\\\u00b0C for 15 min. After autoclaving\
    \ inject 1.0 ml of neutralized sulfide solution (0.03% end concentration) to each\
    \ bottle. This medium can be stored for several months. Incubate the culture at\
    \ 50\\\\u00b0C at a light intensity of 300 - 500 lux. For heavy cell suspension\
    \ supplement periodically with sterile yeast extract solution (0.1% end concentration,\
    \ for more details see Ref. 3365, 3366).\\\"\\n                    }\",\n    \
    \      \"quote_representation\": \"raw JSON object\"\n        }\n      ]\n   \
    \ },\n    {\n      \"decision_id\": \"q65\",\n      \"subject\": \"Neutralized\
    \ sulfide in strain-13941 owner\",\n      \"local_fields\": [\n        {\n   \
    \       \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ingredients[20].concentration\",\n          \"\
    original\": {\n            \"value\": \"30\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"unsupported\",\n   \
    \   \"stage\": \"Unresolved variant\",\n      \"interpretation\": \"The base stock\
    \ source does not authenticate a variant-specific stock dose or final rate. Retain\
    \ the current 30 G_PER_L as unsupported at its asserted flat stage.\",\n     \
    \ \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[3].recipe[1]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"Na2S x 9 H2O\\\",\\n                        \\\"\
    compound_id\\\": 54,\\n                        \\\"amount\\\": 3,\\n         \
    \               \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 30,\\n                        \\\"mmol_l\\\": 124.905,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q66\",\n      \"subject\": \"CA receiving dose already repaired\",\n     \
    \ \"local_fields\": [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"solutions[0].concentration\",\n          \"original\"\
    : {\n            \"value\": \"1\",\n            \"unit\": \"ML_PER_L\"\n     \
    \     }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"solutions[0].concentration\",\n          \"original\"\
    : {\n            \"value\": \"1\",\n            \"unit\": \"ML_PER_L\"\n     \
    \     }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n      \"\
    stage\": \"Receiving medium addition\",\n      \"interpretation\": \"The explicit\
    \ 1.0 ml/litre instruction supports the existing 1 ML_PER_L dose. This is stronger\
    \ than treating the API batch dose as final-volume proof. Preserve the existing\
    \ dose while completing stock composition.\",\n      \"sources\": [\n        {\n\
    \          \"locator\": \"extracted-text lines 4-4\",\n          \"source_key\"\
    : \"dsmz87a\",\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\"\
    ,\n          \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"To medium 87 add 1.0 ml/litre sterile vitamin solution CA.\",\n          \"\
    quote_representation\": \"captured extracted text\"\n        }\n      ]\n    },\n\
    \    {\n      \"decision_id\": \"q67\",\n      \"subject\": \"CA strain dose remains\
    \ a candidate\",\n      \"local_fields\": [\n        {\n          \"record_path\"\
    : \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\",\n\
    \          \"field_path\": \"solutions[0].concentration_candidates[0]\",\n   \
    \       \"original\": {\n            \"value\": \"1\",\n            \"unit\":\
    \ \"ML_PER_L\",\n            \"basis\": \"CROSS_MEDIUM_INFERENCE\",\n        \
    \    \"support\": \"This record is a variant of medium 87a (KOMODO key '87a_13941');\
    \ volume read from base medium 87a ('CHLOROFLEXUS AGGREGANS MEDIUM').\",\n   \
    \         \"counterevidence\": \"The variant's own recipe was never read — only\
    \ base medium 87a's — so the modification may change this volume. A stock's addition\
    \ volume varies by citing medium: MediaDive medium 142 adds 'Trace element solution\
    \ (Vishniac & Santer)' at 0.2 ml and medium 69 adds the same stock at 5 ml.\"\
    ,\n            \"proposed_by\": \"apply_cocktail_nesting.py\"\n          }\n \
    \       },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"solutions[0].preparation_notes\",\n          \"\
    original\": \"Stock prepared in 100 ml. Composition and addition volume NOT asserted:\
    \ proposed as 1 ml/l on basis CROSS_MEDIUM_INFERENCE; see concentration_candidates\
    \ (#150).\"\n        }\n      ],\n      \"decision\": \"unsupported\",\n     \
    \ \"stage\": \"Candidate, not an asserted concentration\",\n      \"interpretation\"\
    : \"The 1 ML_PER_L value is explicitly CROSS_MEDIUM_INFERENCE with counterevidence\
    \ that the variant was never read. Preserve that distinction. Clarify the note\
    \ saying composition is not asserted, because five component concentrations are\
    \ actually asserted in this stock.\",\n      \"sources\": [\n        {\n     \
    \     \"locator\": \"extracted-text lines 4-4\",\n          \"source_key\": \"\
    dsmz87a\",\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\"\
    ,\n          \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"To medium 87 add 1.0 ml/litre sterile vitamin solution CA.\",\n          \"\
    quote_representation\": \"captured extracted text\"\n        }\n      ]\n    },\n\
    \    {\n      \"decision_id\": \"q68\",\n      \"subject\": \"Basal water 1050\
    \ ml\",\n      \"local_fields\": [],\n      \"decision\": \"evidence_only\",\n\
    \      \"stage\": \"Source-only water and denominator boundary\",\n      \"interpretation\"\
    : \"Preserve this absolute water input at its own stage. Listed water and provider\
    \ solution-volume metadata do not establish a measured final volume, so no receiving-medium\
    \ dilution is manufactured.\",\n      \"sources\": [\n        {\n          \"\
    locator\": \"$.data.solutions[0].recipe[11]\",\n          \"source_key\": \"api87a\"\
    ,\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n \
    \         \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 12,\\n                 \
    \       \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 1050,\\n     \
    \                   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n          \"quote_representation\": \"raw JSON\
    \ object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\": \"q69\"\
    ,\n      \"subject\": \"CA stock water 100 ml\",\n      \"local_fields\": [],\n\
    \      \"decision\": \"evidence_only\",\n      \"stage\": \"Source-only water\
    \ and denominator boundary\",\n      \"interpretation\": \"Preserve this absolute\
    \ water input at its own stage. Listed water and provider solution-volume metadata\
    \ do not establish a measured final volume, so no receiving-medium dilution is\
    \ manufactured.\",\n      \"sources\": [\n        {\n          \"locator\": \"\
    $.data.solutions[1].recipe[0]\",\n          \"source_key\": \"api87a\",\n    \
    \      \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n       \
    \   \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 100,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n          \"quote_representation\": \"raw JSON\
    \ object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\": \"q70\"\
    ,\n      \"subject\": \"SL-6 stock water 1000 ml\",\n      \"local_fields\": [],\n\
    \      \"decision\": \"evidence_only\",\n      \"stage\": \"Source-only water\
    \ and denominator boundary\",\n      \"interpretation\": \"Preserve this absolute\
    \ water input at its own stage. Listed water and provider solution-volume metadata\
    \ do not establish a measured final volume, so no receiving-medium dilution is\
    \ manufactured.\",\n      \"sources\": [\n        {\n          \"locator\": \"\
    $.data.solutions[2].recipe[7]\",\n          \"source_key\": \"api87a\",\n    \
    \      \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n       \
    \   \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 1000,\\n     \
    \                   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n          \"quote_representation\": \"raw JSON\
    \ object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\": \"q71\"\
    ,\n      \"subject\": \"Sulfide stock water 100 ml\",\n      \"local_fields\"\
    : [],\n      \"decision\": \"evidence_only\",\n      \"stage\": \"Source-only\
    \ water and denominator boundary\",\n      \"interpretation\": \"Preserve this\
    \ absolute water input at its own stage. Listed water and provider solution-volume\
    \ metadata do not establish a measured final volume, so no receiving-medium dilution\
    \ is manufactured.\",\n      \"sources\": [\n        {\n          \"locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n          \"source_key\": \"api87a\",\n\
    \          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n   \
    \       \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 100,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n          \"quote_representation\": \"raw JSON\
    \ object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\": \"q72\"\
    ,\n      \"subject\": \"SL-6 receiving dose\",\n      \"local_fields\": [],\n\
    \      \"decision\": \"evidence_only\",\n      \"stage\": \"Main-medium stock\
    \ addition\",\n      \"interpretation\": \"Medium 87 explicitly uses 1 ml of SL-6\
    \ in the listed batch. Add the missing stock descriptor and dose on that basis,\
    \ without silently converting it to 1 ml/L final medium.\",\n      \"sources\"\
    : [\n        {\n          \"locator\": \"$.data.solutions[0].recipe[9]\",\n  \
    \        \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 10,\\n                 \
    \       \\\"solution\\\": \\\"Trace element solution SL-6\\\",\\n            \
    \            \\\"solution_id\\\": 25,\\n                        \\\"amount\\\"\
    : 1,\\n                        \\\"unit\\\": \\\"ml\\\",\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"extracted-text\
    \ lines 14-15\",\n          \"source_key\": \"dsmz87\",\n          \"reference\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\",\n     \
    \     \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Trace element solution SL-6\\n(see medium 27)                            \
    \                      1.00       ml\",\n          \"quote_representation\": \"\
    captured extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q73\",\n      \"subject\": \"Main pH\",\n      \"local_fields\": [\n     \
    \   {\n          \"record_path\": \"data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml\"\
    ,\n          \"field_path\": \"ph_value\",\n          \"original\": 8.2\n    \
    \    },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml\"\
    ,\n          \"field_path\": \"ph_value\",\n          \"original\": 8.2\n    \
    \    },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml\"\
    ,\n          \"field_path\": \"ph_value\",\n          \"original\": 8.2\n    \
    \    },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"ph_value\",\n          \"original\": 8.2\n    \
    \    },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml\"\
    ,\n          \"field_path\": \"ph_value\",\n          \"original\": 8.2\n    \
    \    },\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"preparation_steps[0].description\",\n         \
    \ \"original\": \"Adjust pH to 8.2.\"\n        }\n      ],\n      \"decision\"\
    : \"evidence_only\",\n      \"stage\": \"Main medium\",\n      \"interpretation\"\
    : \"pH 8.2 is directly supported for medium 87 and inherited by defined 87a. The\
    \ exact KOMODO and strain-variant pages remain unavailable, so copied owner pH\
    \ is not independent variant authentication.\",\n      \"sources\": [\n      \
    \  {\n          \"locator\": \"extracted-text lines 18-18\",\n          \"source_key\"\
    : \"dsmz87\",\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\"\
    ,\n          \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Adjust pH to 8.2.\",\n          \"quote_representation\": \"captured extracted\
    \ text\"\n        },\n        {\n          \"locator\": \"$.data.solutions[0].steps[0]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 8.2.\\\"\\n   \
    \                 }\",\n          \"quote_representation\": \"raw JSON object\"\
    \n        }\n      ]\n    },\n    {\n      \"decision_id\": \"q74\",\n      \"\
    subject\": \"Main preparation and incubation\",\n      \"local_fields\": [\n \
    \       {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"preparation_steps[1].description\",\n         \
    \ \"original\": \"Boil the medium under a stream of nitrogen gas for a few minutes\
    \ and distribute 90 ml medium into 100 ml screw-capped bottles. Bubble each bottle\
    \ with nitrogen gas and close immediately with a rubber septum and screw tight.\
    \ Autoclave at 121°C for 15 min. After autoclaving inject 1.0 ml of neutralized\
    \ sulfide solution (0.03% end concentration) to each bottle. This medium can be\
    \ stored for several months. Incubate the culture at 50°C at a light intensity\
    \ of 300 - 500 lux. For heavy cell suspension supplement periodically with sterile\
    \ yeast extract solution (0.1% end concentration, for more details see Ref. 3365,\
    \ 3366).\"\n        }\n      ],\n      \"decision\": \"evidence_only\",\n    \
    \  \"stage\": \"Basal preparation, post-autoclave injection and source prescriptions\"\
    ,\n      \"interpretation\": \"Credit the DSM owner: nitrogen boiling for a few\
    \ minutes, 90 ml in 100 ml screw-cap bottles, nitrogen seal, 121 C for 15 min,\
    \ later 1 ml neutralized sulfide, nominal 0.03% end concentration, storage for\
    \ several months, 50 C and 300–500 lux, optional sterile yeast-extract supplementation\
    \ at nominal 0.1%. Preserve qualitative durations and unspecified percentage bases.\
    \ These are collection instructions, not independently read experimental growth\
    \ results. The generated target omits them.\",\n      \"sources\": [\n       \
    \ {\n          \"locator\": \"$.data.solutions[0].steps[1]\",\n          \"source_key\"\
    : \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Boil the medium under a stream\
    \ of nitrogen gas for a few minutes and distribute 90 ml medium into 100 ml screw-capped\
    \ bottles. Bubble each bottle with nitrogen gas and close immediately with a rubber\
    \ septum and screw tight. Autoclave at 121\\\\u00b0C for 15 min. After autoclaving\
    \ inject 1.0 ml of neutralized sulfide solution (0.03% end concentration) to each\
    \ bottle. This medium can be stored for several months. Incubate the culture at\
    \ 50\\\\u00b0C at a light intensity of 300 - 500 lux. For heavy cell suspension\
    \ supplement periodically with sterile yeast extract solution (0.1% end concentration,\
    \ for more details see Ref. 3365, 3366).\\\"\\n                    }\",\n    \
    \      \"quote_representation\": \"raw JSON object\"\n        },\n        {\n\
    \          \"locator\": \"extracted-text lines 19-20\",\n          \"source_key\"\
    : \"dsmz87\",\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87.pdf\"\
    ,\n          \"source_raw_sha256\": \"99d5799eb50563779fcb3f6b3345b4c329cf32d3ba7d9e736be5e7fc5bf4cffc\"\
    ,\n          \"source_text_sha256\": \"5ea42b75382ae99fb5b3c986a755b18417feccb478bff2ad44550775e5f268c7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.975133Z\",\n          \"exact_source_quote\"\
    : \"Boil the medium under a stream of nitrogen gas for a few minutes and distribute\
    \ 90 ml\\nmedium into 100 ml screw-capped bottles.\",\n          \"quote_representation\"\
    : \"captured extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q75\",\n      \"subject\": \"Current source-87 preparation version\",\n  \
    \    \"local_fields\": [],\n      \"decision\": \"evidence_only\",\n      \"stage\"\
    : \"Provider version comparison only\",\n      \"interpretation\": \"Current API\
    \ 87 instead says 10 ml in 15 ml Hungate tubes and 0.1 ml sulfide. Preserve this\
    \ version difference from the current PDF and API 87a; do not silently substitute\
    \ either preparation into the unavailable KOMODO 87 recipe.\",\n      \"sources\"\
    : [\n        {\n          \"locator\": \"$.data.solutions[0].steps[1]\",\n   \
    \       \"source_key\": \"api87\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87\"\
    ,\n          \"source_raw_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"source_text_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.974764Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Boil the medium under a stream\
    \ of nitrogen gas for a few minutes and distribute 10 ml medium into 15 ml hungate\
    \ tubes. Bubble each tube with nitrogen gas and close immediately with a rubber\
    \ septum and screw tight.\\\"\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"$.data.solutions[0].steps[3]\"\
    ,\n          \"source_key\": \"api87\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87\"\
    ,\n          \"source_raw_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"source_text_sha256\": \"4c5772a9866aa8a308f2787c7d35d731903dbaed13ff965675d546ee10ba29a7\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.974764Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"After autoclaving inject 0.1\
    \ ml of neutralized sulfide solution (0.03% end concentration) to each tube.\\\
    \"\\n                    }\",\n          \"quote_representation\": \"raw JSON\
    \ object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\": \"q76\"\
    ,\n      \"subject\": \"CA stock preparation\",\n      \"local_fields\": [\n \
    \       {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"preparation_steps[2].description\",\n         \
    \ \"original\": \"Adjust pH to 7.5. The solution is filter-sterilized.\"\n   \
    \     }\n      ],\n      \"decision\": \"evidence_only\",\n      \"stage\": \"\
    CA stock, not main medium\",\n      \"interpretation\": \"The pH 7.5 and filter\
    \ sterilization belong only to CA. The DSM owner retains the prose but it is pooled\
    \ in a root list; attach clear stock scope and preserve main pH 8.2.\",\n    \
    \  \"sources\": [\n        {\n          \"locator\": \"extracted-text lines 18-18\"\
    ,\n          \"source_key\": \"dsmz87a\",\n          \"reference\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium87a.pdf\"\
    ,\n          \"source_raw_sha256\": \"4ff9b711ae36b935f2f3cb31997aeacf3c70ff154b550a0c1ea52ba6dcde091d\"\
    ,\n          \"source_text_sha256\": \"4168500818114d2733a4445b983ad41bd98d08bdb244b1eae52b38681b9abe6a\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:56.018620Z\",\n          \"exact_source_quote\"\
    : \"Adjust pH to 7.5. The solution is filter-sterilized.\",\n          \"quote_representation\"\
    : \"captured extracted text\"\n        },\n        {\n          \"locator\": \"\
    $.data.solutions[1].steps[0]\",\n          \"source_key\": \"api87a\",\n     \
    \     \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\",\n        \
    \  \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 7.5. The solution\
    \ is filter-sterilized.\\\"\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q77\",\n      \"subject\": \"Neutralized sulfide preparation\",\n      \"\
    local_fields\": [\n        {\n          \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"preparation_steps[3].description\",\n         \
    \ \"original\": \"The sulfide solution is prepared in a 250 ml screw-capped bottle\
    \ with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with\
    \ nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room\
    \ temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise\
    \ with a syringe without opening the bottle.\"\n        },\n        {\n      \
    \    \"record_path\": \"data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml\"\
    ,\n          \"field_path\": \"preparation_steps[4].description\",\n         \
    \ \"original\": \"Appearance of a yellow colour indicates the drop of pH to about\
    \ 8. The solution should be stirred continuously to avoid precipitation of elemental\
    \ sulfur. The final solution should be clear and is yellow in colour.\"\n    \
    \    }\n      ],\n      \"decision\": \"evidence_only\",\n      \"stage\": \"\
    Sulfide stock\",\n      \"interpretation\": \"Preserve the 250 ml vessel, nitrogen\
    \ treatment, 121 C for 15 min, cooling to room temperature, then sterile 2 M H2SO4\
    \ dropwise to about pH 7.0 with no stated acid volume. Yellow colour around pH\
    \ 8 is an intermediate indicator, not the final target. Continuous stirring avoids\
    \ sulfur precipitation. Do not treat acid stock molarity as final medium molarity.\"\
    ,\n      \"sources\": [\n        {\n          \"locator\": \"$.data.solutions[3].steps[0]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"The sulfide solution is prepared\
    \ in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer.\
    \ The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min.\
    \ at 121\\\\u00b0C. After cooling to room temperature the pH is adjusted to about\
    \ 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening\
    \ the bottle.\\\"\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        },\n        {\n          \"locator\": \"$.data.solutions[3].steps[1]\"\
    ,\n          \"source_key\": \"api87a\",\n          \"reference\": \"https://mediadive.dsmz.de/rest/medium/87a\"\
    ,\n          \"source_raw_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"source_text_sha256\": \"999041b8eaad7d41361daee0bdc316f31a619f7318b1723f43aab9e7687fc884\"\
    ,\n          \"accessed_at\": \"2026-10-28T08:33:55.983518Z\",\n          \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Appearance of a yellow colour\
    \ indicates the drop of pH to about 8. The solution should be stirred continuously\
    \ to avoid precipitation of elemental sulfur. The final solution should be clear\
    \ and is yellow in colour.\\\"\\n                    }\",\n          \"quote_representation\"\
    : \"raw JSON object\"\n        }\n      ]\n    }\n  ],\n  \"local_field_census_reference\"\
    : \"REVIEW_WORK/batch061/record05/grounding-inventory.json\",\n  \"source_only_gaps_are_explicit\"\
    : true,\n  \"note\": \"Batch amounts, provider normalization, stock composition,\
    \ working dose and preparation controls are separate. No source edits or automatic\
    \ curation performed.\"\n}"
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml: primary 25/26,
    secondary 23/26; data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml:
    primary 25/26, secondary 23/26; data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml:
    primary 20/21, secondary 18/21; data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml:
    primary 20/21, secondary 18/21; data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml:
    primary 20/21, secondary 18/21. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    10 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:006721
  evidence_ids:
  - grounding
- assessment_id: a7
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected target and exact maintained owners reviewed. Dependencies
    transfer only their explicitly named stock subsection; unrelated parent media
    and source prescriptions are not growth evidence.
  target_ids:
  - CultureMech:006721
  evidence_ids:
  - local0
- assessment_id: a8
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical commands passed once; strict schema TSV contains only
    its header and reference validation checked zero references on the generated target.
    This does not certify quantities or chemical forms.
  target_ids:
  - CultureMech:006721
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-006721-source-branches-not-proven-duplicates
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Distinct source branches are consolidated without independent equivalence
  description: The target and relationship claims collapse base 87, defined 87a and
    a strain-13941 modifier on copied signatures. DSM 87a explicitly adds CA; base
    87 does not. The three exact KOMODO routes returned 403. Current full-formulation
    merge guards reject incompatible scientific content, so old generated consolidation
    must not be justified by the current merger or copied histories.
  target_ids:
  - CultureMech:006721
  field_paths:
  - merged_from
  - ingredients
  - data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml::variant_children
  - data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml::variant_relationship
  - data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml::variant_relationship
  - data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml::variant_relationship
  evidence_ids:
  - dsmz87
  - dsmz87a
  - api87
  - api87a
  - local0
  rule_id: source-specific-formulation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-006721-stock-stage-and-volume-errors
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock recipes and receiving doses are represented as flat final concentrations
  description: Fe(III) citrate is a 5 ml solution addition, not 5 g/L. Nine CA components,
    seven SL-6 components and neutralized sulfide need distinct stock/dose stages.
    Three owners already nest five CA components; preserve them and the two supported
    1 ML_PER_L additions. The generated target retains all stock-strength rows flat.
    No final-volume conversion follows merely from 1050 ml listed water.
  target_ids:
  - CultureMech:006721
  field_paths:
  - ingredients
  - solutions
  - data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml::solutions[0]
  - data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml::solutions[0]
  - data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml::solutions[0]
  evidence_ids:
  - quantity-inventory
  - dsmz87a
  - dsmz87
  - dsmz27
  - api87a
  rule_id: source-specific-formulation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-006721-stale-preparation-and-partial-repairs
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated content omits existing owner repairs and preparation
  description: The DSM owner retains five preparation entries including nitrogen,
    vessels, sterilization, incubation, CA and sulfide controls, while the generated
    target retains none. Three owners contain partial nested CA composition absent
    from the target. Pooled owner preparation still needs clear stock stages. Current
    merger guards preserve these fields and reject incompatible formulas; persisted
    loss is a stale-output/owner-reconciliation issue.
  target_ids:
  - CultureMech:006721
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - local0
  - local2
  - local3
  - local4
  - dsmz87
  - dsmz87a
  rule_id: source-specific-formulation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-006721-nickel-hydrate-link
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate asserts the anhydrous ontology identity
  description: All five selected layers name nickel chloride hexahydrate but assert
    CHEBI:34887 in both primary and secondary slots. Current OLS identifies this as
    anhydrous nickel dichloride; CHEBI:53542 is the independently retrieved hexahydrate
    candidate. Literal label agreement and provider mmol_l do not fix a supplied-form
    mismatch. Other hydrate labels were checked independently.
  target_ids:
  - CultureMech:006721
  field_paths:
  - data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml::ingredients[23].term
  - data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml::ingredients[23].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml::ingredients[23].term
  - data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml::ingredients[23].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml::ingredients[18].term
  - data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml::ingredients[18].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml::ingredients[18].term
  - data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml::ingredients[18].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml::ingredients[18].term
  - data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml::ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - dsmz27
  - chebi34887
  - chebi53542
  - grounding
  rule_id: supplied-chemical-form-correspondence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-006721-legacy-nitrate-linkage
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Legacy nitrate identifiers have no current exact MIM rows
  description: The ten numeric legacy mentions are the two nitrate secondary IDs repeated
    across five complete selected documents. Exact current CSV/catalog lookup finds
    no MediaIngredientMech:000170 or :000171; valid primary CHEBI nitrate identities
    are retained. Current absence does not establish that these historical IDs were
    never valid.
  target_ids:
  - CultureMech:006721
  field_paths:
  - data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml::ingredients[4].mediaingredientmech_term
  - data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml::ingredients[4].mediaingredientmech_term
  - data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml::ingredients[4].mediaingredientmech_term
  - data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml::ingredients[4].mediaingredientmech_term
  - data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml::ingredients[4].mediaingredientmech_term
  - data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml::ingredients[5].mediaingredientmech_term
  - data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml::ingredients[5].mediaingredientmech_term
  - data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml::ingredients[5].mediaingredientmech_term
  - data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml::ingredients[5].mediaingredientmech_term
  - data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml::ingredients[5].mediaingredientmech_term
  evidence_ids:
  - grounding
  rule_id: mediaingredientmech-exact-identifier-linkage
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
- finding_id: f6
  issue_key: culturemech-006721-append-only-history-and-variant-note
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Malformed history and contradictory variant notes need append-only clarification
  description: KOMODO histories retain literal .fZ timestamps. The strain stock note
    says composition is not asserted although five component concentrations are present;
    its dose correctly remains only a cross-medium candidate. These distinctions should
    be explicit rather than silently rewriting old events.
  target_ids:
  - CultureMech:006721
  field_paths:
  - data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml::curation_history
  - data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml::curation_history
  - data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml::curation_history
  - data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml::solutions[0].preparation_notes
  evidence_ids:
  - local1
  - local2
  - local4
  - history-auth
  rule_id: source-specific-formulation-fidelity
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Retain the valid DSM 87a identity. Reassess each maintained branch
    against its exact source before treating it as a duplicate; preserve unresolved
    strain modifications and the current candidate dose. Review variant-proposal criteria
    and regenerate only scientifically compatible records.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006721
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action2
  description: Reconstruct the complete source-scoped stocks and explicit receiving
    additions in maintained owners, keeping current correct nested components and
    candidate uncertainty. Represent Fe stock composition, liquid dose, sulfide stock
    preparation and later injection separately. Use source batch amounts or explicitly
    attributed provider normalization; do not invent final-volume rates.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006721
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action3
  description: Preserve the existing DSM preparation and nested repairs. Complete
    stage-specific owner content, including stock-only pH and sterilization, then
    regenerate through current guarded merging after resolving branch identity. Keep
    source-only incubation instructions distinct from measured growth evidence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006721
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action4
  description: Resolve the exact hexahydrate through authoritative ontology and current
    MIM mappings, preserving source mass and stock stage. Do not replace hydrate mass
    with an anhydrous molar conversion. Treat generic source calcium pantothenate
    versus the more specific D-pantothenate assertion as unresolved stereochemical
    support, not an automatic replacement.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006721
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action5
  description: Resolve the legacy secondary nitrate references against current authoritative
    MIM identity evidence, retaining correct primary CHEBI terms and historical provenance.
    Do not force a fuzzy or substring match.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006721
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action6
  description: Preserve malformed original events and all old evidence unchanged.
    Append a verified corrective/context event with the actual current curation date,
    identifying only evidence-supported prior context. Clarify asserted composition
    versus unasserted candidate dose, and repair the writer timestamp format for future
    events.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:006721
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
limitations:
- Exact KOMODO 87, 87a and 87a_13941 routes returned HTTP 403; no equivalence or strain-specific
  formulation is inferred from copied signatures.
- Listed water is not measured final volume. API 87a and 87 use different declared
  normalization bases and preparation versions; neither is silently transferred to
  the other.
- DSM 27 supports only the named SL-6 subsection. Its basal recipe and growth/preparation
  instructions do not transfer.
- Current MIM lookup is pinned to the packaged CSV metadata commit 6643131b0f12ab40b66f98135245fca04027e0e9;
  current negatives do not establish historical invalidity. Source-generic calcium
  pantothenate does not conclusively establish D stereochemistry.
- All ten reports were fully read; matching current API 87a raw authenticates those
  bytes and excerpts, not old retrieval time, execution or the separately cited KOMODO
  catalogue. No paper-level growth experiment was newly verified.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
