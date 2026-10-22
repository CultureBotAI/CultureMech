# Source and formulation review: blastococcus_aggregatus_medium (CultureMech:006077)

- Review: 20261022T003735Z-culturemech-006077-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T00:25:09Z
- Finished UTC: 2026-10-22T00:37:35Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM596 establishes five base solutes, 999 ml artificial seawater and a 1 ml addition of a separate eight-solute trace stock. The target flattens all eight stock-preparation amounts represented as rates; both maintained owners nest only three, leaving five as stock-preparation rates in the main medium. Seawater has a mass-unit error, Tris HCl is mapped to tris base, and current provider and legacy-link uncertainty require a partial review.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 429; batch 043 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-two task batches contain 420 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 423 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006077 | data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml | generated | blastococcus_aggregatus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006077 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006077 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch043/429/strict.tsv |
| validate-terms | passed | True | CultureMech:006077 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006077 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006077 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: api596 | unavailable | False | CultureMech:006077 | The exact current MediaDive REST596 request returned HTTP503 once. The DSM primary remains usable; the failure is not recipe absence. |
| Authenticate original legacy000170 correspondence | unavailable | True | CultureMech:006077 | Current negative lookup is available; historical original mapping bytes are not authenticated. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006077.

The four documented recipes completed; interpret the scope of each separately.

### DSM596 and linked KOMODO contributor

identity: supported. Targets: CultureMech:006077.

The exact generated target derives from two maintained source records with distinct IDs; their current SOURCE_DUPLICATE relation and local copied signatures establish local relationship context. Current KOMODO contents differ from the DSM primary and cannot establish contemporary whole-formula equivalence.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:006077.

10 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 10/14 primary and 8/14 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 14: primary 71.43%; secondary 57.14%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Source salt, hydrate and stereochemistry

grounding: concern. Targets: CultureMech:006077.

Tris HCl is explicitly a hydrochloride while CHEBI:9754 defines the free base C4H11NO3. CHEBI:63017 is stereospecific sodium L-tartrate although the primary only says Na-tartrate; CHEBI:75832 is anhydrous while FeSO4 hydration is unstated. Those latter two are unsupported specificity, not proof that another hydrate or enantiomer is required. KNO3, boric acid and explicit Mn tetrahydrate, Cu dihydrate, Co hexahydrate and molybdate dihydrate correspond to the asserted forms; zinc chloride is compatible with ZnCl2. Tryptone/yeast extract remain complex, and sodium glycerophosphate is not assigned an invented isomer.

### Legacy linkage versus current CHEBI identity

grounding: unknown. Targets: CultureMech:006077.

All three KNO3 instances retain MediaIngredientMech:000170. Current exact lookup is absent; historical original-ID meaning is unresolved rather than proven wrong. Do not infer its historical identity from the valid potassium-nitrate CHEBI term.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006077.

30 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Layer-specific preparation and provider flags

completeness: concern. Targets: CultureMech:006077.

The DSM owner retains pH7.0 and aquarium-salt preparation text; the KOMODO owner and target omit those preparation arrays although pH is structured. Preserve the existing DSM information. Is Aerobic false is a provider metadata flag, not primary evidence of anaerobic growth. No organisms or growth measurements are asserted.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006077.

53 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "KNO3",
    "stage": "Main printed batch formulation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.50",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " KNO3                                                            0.50     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. "
  },
  {
    "decision_id": "q2",
    "name": "Sodium glycerophosphate",
    "stage": "Main printed batch formulation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.10",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Na-glycerophosphate                                             0.10     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. "
  },
  {
    "decision_id": "q3",
    "name": "Tris HCl",
    "stage": "Main printed batch formulation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.00",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Tris HCl                                                        1.00     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. The separate Tris hydrochloride/base mismatch remains."
  },
  {
    "decision_id": "q4",
    "name": "Tryptone",
    "stage": "Main printed batch formulation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "2.00",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Tryptone (Difco 0123)                                           2.00     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. "
  },
  {
    "decision_id": "q5",
    "name": "Yeast extract",
    "stage": "Main printed batch formulation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "2.00",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Yeast extract                                                   2.00     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. "
  },
  {
    "decision_id": "q6",
    "name": "Sea water",
    "stage": "Main solvent",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "999",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "999",
      "printed_unit": "ml",
      "material": "artificial seawater",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": "Artificial sea water is prepared from a marine aquarium salts mixture.",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The source gives 999 ml artificial seawater; the local 999 G_PER_L has the wrong volume dimension. Correct to the printed batch volume without asserting ML_PER_L or assuming density. Aquarium-salt composition remains qualitatively specified; no salinity or exact salt mass is supplied."
  },
  {
    "decision_id": "q7",
    "name": "H3BO3",
    "stage": "Trace-stock preparation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.85",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "2.85",
      "printed_unit": "g",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " H3BO3                                                          2.85      g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q8",
    "name": "MnCl2 x 4 H2O",
    "stage": "Trace-stock preparation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.80",
      "printed_unit": "g",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " MnCl2 x 4 H2O                                                  1.80      g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q9",
    "name": "FeSO4",
    "stage": "Trace-stock preparation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.36",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.36",
      "printed_unit": "g",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " FeSO4                                                          1.36      g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q10",
    "name": "Na-tartrate",
    "stage": "Trace-stock preparation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1.77",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.77",
      "printed_unit": "g",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Na-tartrate                                                    1.77      g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q11",
    "name": "CuCl2 x 2 H2O",
    "stage": "Trace-stock preparation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.0269",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "26.90",
      "printed_unit": "mg",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " CuCl2 x 2 H2O                                                 26.90     mg",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q12",
    "name": "ZnCl2",
    "stage": "Trace-stock preparation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.0208",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "20.80",
      "printed_unit": "mg",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " ZnCl2                                                         20.80     mg",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q13",
    "name": "CoCl2 x 6 H2O",
    "stage": "Trace-stock preparation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.0404",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "40.40",
      "printed_unit": "mg",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " CoCl2 x 6 H2O                                                 40.40     mg",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q14",
    "name": "Na2MoO4 x 2 H2O",
    "stage": "Trace-stock preparation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.0252",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "25.20",
      "printed_unit": "mg",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Na2MoO4 x 2 H2O                                               25.20     mg",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q15",
    "name": "pH",
    "stage": "Main medium",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.0
      }
    ],
    "desired": 7.0,
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": "pH 7.0",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "Current pH agrees; attach the source statement. No adjustment reagent or titration amount is specified."
  },
  {
    "decision_id": "q16",
    "name": "KNO3",
    "stage": "Main printed batch formulation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.50",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " KNO3                                                            0.50     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. "
  },
  {
    "decision_id": "q17",
    "name": "Sodium glycerophosphate",
    "stage": "Main printed batch formulation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.10",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Na-glycerophosphate                                             0.10     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. "
  },
  {
    "decision_id": "q18",
    "name": "Tris HCl",
    "stage": "Main printed batch formulation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.00",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Tris HCl                                                        1.00     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. The separate Tris hydrochloride/base mismatch remains."
  },
  {
    "decision_id": "q19",
    "name": "Tryptone",
    "stage": "Main printed batch formulation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "2.00",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Tryptone (Difco 0123)                                           2.00     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. "
  },
  {
    "decision_id": "q20",
    "name": "Yeast extract",
    "stage": "Main printed batch formulation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "2.00",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Yeast extract                                                   2.00     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. "
  },
  {
    "decision_id": "q21",
    "name": "Sea water",
    "stage": "Main solvent",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "999",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "999",
      "printed_unit": "ml",
      "material": "artificial seawater",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": "Artificial sea water is prepared from a marine aquarium salts mixture.",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The source gives 999 ml artificial seawater; the local 999 G_PER_L has the wrong volume dimension. Correct to the printed batch volume without asserting ML_PER_L or assuming density. Aquarium-salt composition remains qualitatively specified; no salinity or exact salt mass is supplied."
  },
  {
    "decision_id": "q22",
    "name": "Na-tartrate",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1.77",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.77",
      "printed_unit": "g",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Na-tartrate                                                    1.77      g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q23",
    "name": "CuCl2 x 2 H2O",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.0269",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "26.90",
      "printed_unit": "mg",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " CuCl2 x 2 H2O                                                 26.90     mg",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q24",
    "name": "ZnCl2",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.0208",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "20.80",
      "printed_unit": "mg",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " ZnCl2                                                         20.80     mg",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q25",
    "name": "CoCl2 x 6 H2O",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.0404",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "40.40",
      "printed_unit": "mg",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " CoCl2 x 6 H2O                                                 40.40     mg",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q26",
    "name": "Na2MoO4 x 2 H2O",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.0252",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "25.20",
      "printed_unit": "mg",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Na2MoO4 x 2 H2O                                               25.20     mg",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q27",
    "name": "H3BO3",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "2.85",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "2.85",
      "printed_unit": "g",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " H3BO3                                                          2.85      g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The component is correctly nested, but its per-final-stock-litre denominator is unsupported. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q28",
    "name": "MnCl2 x 4 H2O",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "1.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.80",
      "printed_unit": "g",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " MnCl2 x 4 H2O                                                  1.80      g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The component is correctly nested, but its per-final-stock-litre denominator is unsupported. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q29",
    "name": "FeSO4",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "solutions[0].composition[2].concentration",
        "stored": {
          "value": "1.36",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.36",
      "printed_unit": "g",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " FeSO4                                                          1.36      g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The component is correctly nested, but its per-final-stock-litre denominator is unsupported. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q30",
    "name": "Trace stock dose",
    "stage": "Main addition",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1",
      "printed_unit": "ml",
      "final_receiving_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The maintained owner preserves the correct 1 ml dose numerator and partial stock membership, but the source does not establish a per-litre receiving denominator. Preserve the printed batch dose and complete all eight stock components."
  },
  {
    "decision_id": "q31",
    "name": "Stock preparation volume",
    "stage": "Trace stock only",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
      }
    ],
    "desired": {
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1",
      "final_stock_volume": null,
      "final_receiving_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The note partly preserves the printed 1000 ml stock-water input and 1 ml batch dose, but its final-stock and per-litre receiving claims are not established by this primary. Retain the literal inputs and mark both denominator assumptions unresolved. The current primary does not authenticate the historical MediaDive bytes."
  },
  {
    "decision_id": "q32",
    "name": "pH",
    "stage": "Main medium",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.0
      }
    ],
    "desired": 7.0,
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": "pH 7.0",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "Current pH agrees; attach the source statement. No adjustment reagent or titration amount is specified."
  },
  {
    "decision_id": "q33",
    "name": "KNO3",
    "stage": "Main printed batch formulation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.50",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " KNO3                                                            0.50     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. "
  },
  {
    "decision_id": "q34",
    "name": "Sodium glycerophosphate",
    "stage": "Main printed batch formulation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.10",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Na-glycerophosphate                                             0.10     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. "
  },
  {
    "decision_id": "q35",
    "name": "Tris HCl",
    "stage": "Main printed batch formulation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.00",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Tris HCl                                                        1.00     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. The separate Tris hydrochloride/base mismatch remains."
  },
  {
    "decision_id": "q36",
    "name": "Tryptone",
    "stage": "Main printed batch formulation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "2.00",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Tryptone (Difco 0123)                                           2.00     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. "
  },
  {
    "decision_id": "q37",
    "name": "Yeast extract",
    "stage": "Main printed batch formulation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "2.00",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Yeast extract                                                   2.00     g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The numerical mass agrees with the printed batch amount. The source lists 999 ml artificial seawater plus 1 ml trace stock, but does not declare final or make-up volume; the stored G_PER_L denominator is therefore unsupported. Preserve the batch mass and resolve its basis before attaching rate evidence. "
  },
  {
    "decision_id": "q38",
    "name": "Sea water",
    "stage": "Main solvent",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "999",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "999",
      "printed_unit": "ml",
      "material": "artificial seawater",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Artificial sea water                                          999.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": "Artificial sea water is prepared from a marine aquarium salts mixture.",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The source gives 999 ml artificial seawater; the local 999 G_PER_L has the wrong volume dimension. Correct to the printed batch volume without asserting ML_PER_L or assuming density. Aquarium-salt composition remains qualitatively specified; no salinity or exact salt mass is supplied."
  },
  {
    "decision_id": "q39",
    "name": "Na-tartrate",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1.77",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.77",
      "printed_unit": "g",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Na-tartrate                                                    1.77      g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q40",
    "name": "CuCl2 x 2 H2O",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.0269",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "26.90",
      "printed_unit": "mg",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " CuCl2 x 2 H2O                                                 26.90     mg",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q41",
    "name": "ZnCl2",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.0208",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "20.80",
      "printed_unit": "mg",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " ZnCl2                                                         20.80     mg",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q42",
    "name": "CoCl2 x 6 H2O",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.0404",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "40.40",
      "printed_unit": "mg",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " CoCl2 x 6 H2O                                                 40.40     mg",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q43",
    "name": "Na2MoO4 x 2 H2O",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.0252",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "25.20",
      "printed_unit": "mg",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Na2MoO4 x 2 H2O                                               25.20     mg",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "This printed stock-preparation amount is incorrectly represented as a direct main-medium rate; restore its stock stage. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q44",
    "name": "H3BO3",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "2.85",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "2.85",
      "printed_unit": "g",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " H3BO3                                                          2.85      g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The component is correctly nested, but its per-final-stock-litre denominator is unsupported. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q45",
    "name": "MnCl2 x 4 H2O",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "1.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.80",
      "printed_unit": "g",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " MnCl2 x 4 H2O                                                  1.80      g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The component is correctly nested, but its per-final-stock-litre denominator is unsupported. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q46",
    "name": "FeSO4",
    "stage": "Trace-stock preparation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "solutions[0].composition[2].concentration",
        "stored": {
          "value": "1.36",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.36",
      "printed_unit": "g",
      "final_volume": null,
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " FeSO4                                                          1.36      g",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The component is correctly nested, but its per-final-stock-litre denominator is unsupported. The primary lists 1000 ml water, not a final or make-up stock volume. Preserve the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass fraction applies only if final stock volume is independently established as 1000 ml; it is not source-established here. Hydration/stereochemistry issues do not change the literal batch mass."
  },
  {
    "decision_id": "q47",
    "name": "Trace stock dose",
    "stage": "Main addition",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1",
      "printed_unit": "ml",
      "final_receiving_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The maintained owner preserves the correct 1 ml dose numerator and partial stock membership, but the source does not establish a per-litre receiving denominator. Preserve the printed batch dose and complete all eight stock components."
  },
  {
    "decision_id": "q48",
    "name": "Stock preparation volume",
    "stage": "Trace stock only",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
      }
    ],
    "desired": {
      "listed_stock_water_ml": "1000",
      "receiving_batch_dose_ml": "1",
      "final_stock_volume": null,
      "final_receiving_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      },
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The note partly preserves the printed 1000 ml stock-water input and 1 ml batch dose, but its final-stock and per-litre receiving claims are not established by this primary. Retain the literal inputs and mark both denominator assumptions unresolved. The current primary does not authenticate the historical MediaDive bytes."
  },
  {
    "decision_id": "q49",
    "name": "pH",
    "stage": "Main medium",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0
      }
    ],
    "desired": 7.0,
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": "pH 7.0",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "Current pH agrees; attach the source statement. No adjustment reagent or titration amount is specified."
  },
  {
    "decision_id": "q50",
    "name": "Trace stock dose",
    "stage": "Generated target omission",
    "decision": "add",
    "local_fields": [],
    "desired": {
      "printed_batch_amount": "1",
      "printed_unit": "ml",
      "final_receiving_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": " Trace elements (see below)                                      1.00    ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "Restore the complete scoped stock and the printed 1 ml batch dose through maintained-owner correction and authorized regeneration. The primary does not declare the receiving final volume; do not supply ML_PER_L or duplicate flattened and nested components."
  },
  {
    "decision_id": "q51",
    "name": "Stock water",
    "stage": "Trace preparation only",
    "decision": "add",
    "local_fields": [],
    "desired": {
      "value": "1000",
      "unit": "ML",
      "basis": "stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 Trace elements stock; exact printed row",
        "exact_source_quote": " Distilled water                                             1000.00     ml",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "Stock water is described in owner notes but absent as a composition solvent; keep it separate from the main999 ml artificial seawater. Do not add another litre of water to the main medium."
  },
  {
    "decision_id": "q52",
    "name": "Aquarium salts quantity, sterilization and growth conditions",
    "stage": "Source-only unresolved protocol",
    "decision": "not_quantified",
    "local_fields": [],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "dsm596",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf",
        "source_locator": "DSM596 main table/preparation; exact printed row",
        "exact_source_quote": "Artificial sea water is prepared from a marine aquarium salts mixture.",
        "snapshot_sha256": "203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96",
        "parsed_text_sha256": "d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be"
      }
    ],
    "interpretation": "The source names a marine aquarium salts mixture but gives no salt mass/salinity. It specifies no sterilization cycle, incubation temperature, gas, rate or empirical growth measurement; no defaults are supplied."
  },
  {
    "decision_id": "q53",
    "name": "Entire conflicting KOMODO quantity tables",
    "stage": "Provider comparison only; excluded from DSM formula transfer",
    "decision": "conflict",
    "local_fields": [],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "komodo596",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=596",
        "source_locator": "HTML table2 rows0–45 and table3 rows0–41",
        "snapshot_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
        "decoded_table_rows": [
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 0,
            "cells": [
              "Name",
              "Semi unique name",
              "Unique Name",
              "Gram Amount",
              "Mol Amount"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 1,
            "cells": [
              "NaHCO3",
              "sodium bicarbonate",
              "SEED-cpd00242#cpd00971#cpd09249#",
              "2.46",
              "0.03"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 2,
            "cells": [
              "D(+)-Biotin",
              "D(+)-Biotin",
              "SEED-cpd00104###",
              "1.97E-5",
              "8.11E-8"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 3,
            "cells": [
              "D-Ca-pantothenate",
              "D-Ca-pantothenate",
              "SEED-cpd00063#cpd00644##",
              "4.93E-5",
              "1.91E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 4,
            "cells": [
              "Lipoic acid",
              "Lipoic acid",
              "SEED-cpd00541###",
              "4.93E-5",
              "2.40E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 5,
            "cells": [
              "Calcium pantothenate",
              "Calcium pantothenate",
              "SEED-cpd00063#cpd00644##",
              "9.85E-5",
              "3.82E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 6,
            "cells": [
              "Tris HCl",
              "Tris-HCl",
              "Tris#",
              "1.00",
              "0.01"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 7,
            "cells": [
              "KNO3",
              "KNO3",
              "SEED-cpd00205#cpd00209##",
              "0.50",
              "0.00"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 8,
            "cells": [
              "Na2S x 9 H2O",
              "Sodium sulfide hydrate",
              "SEED-cpd00239#cpd00971##",
              "0.49",
              "0.00"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 9,
            "cells": [
              "Nicotinic acid",
              "Niacin",
              "SEED-cpd00218###",
              "2.46E-4",
              "2.02E-6"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 10,
            "cells": [
              "Riboflavin",
              "Riboflavin",
              "SEED-cpd00220###",
              "4.93E-5",
              "1.31E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 11,
            "cells": [
              "NaOH",
              "Sodium hydroxide",
              "SEED-cpd09244###",
              "4.93E-4",
              "2.74E-5"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 12,
            "cells": [
              "MgCl2 x 6 H2O",
              "Magnesium chloride",
              "SEED-cpd00099#cpd00254#cpd04877#",
              "5.62",
              "0.03"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 13,
            "cells": [
              "KH2PO4",
              "Potassium dihydrogen phosphate",
              "SEED-cpd00009#cpd00205##",
              "0.20",
              "0.00"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 14,
            "cells": [
              "CoCl2 x 6 H2O",
              "CoCl2",
              "SEED-cpd00099#cpd00149##",
              "2.67E-4",
              "1.12E-6"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 15,
            "cells": [
              "CuCl2 x 2 H2O",
              "CuCl2",
              "SEED-cpd00058#cpd00099##",
              "5.57E-5",
              "3.29E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 16,
            "cells": [
              "Vitamin B12",
              "Coenzyme B12",
              "SEED-cpd00166###",
              "9.95E-5",
              "6.30E-8"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 17,
            "cells": [
              "FeCl2 x 4 H2O",
              "Iron chloride",
              "SEED-cpd00099#cpd10516##",
              "1.47E-3",
              "7.42E-6"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 18,
            "cells": [
              "MgSO4 x 7 H2O",
              "Magnesium sulfate",
              "SEED-cpd00048#cpd00254##",
              "6.70",
              "0.03"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 19,
            "cells": [
              "Folic acid",
              "Folic acid",
              "SEED-cpd00393###",
              "1.97E-5",
              "4.49E-8"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 20,
            "cells": [
              "Thiamine-HCl x 2 H2O",
              "Thiamine-HCl",
              "SEED-cpd00099#cpd00305##",
              "2.46E-4",
              "7.32E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 21,
            "cells": [
              "HCl",
              "HCl",
              "SEED-cpd00099###",
              "6.62E-4",
              "1.89E-5"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 22,
            "cells": [
              "FeSO4",
              "Iron sulfate",
              "SEED-cpd00048#cpd10515##",
              "2.72E-3",
              "1.79E-5"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 23,
            "cells": [
              "ZnCl2",
              "ZnCl2",
              "SEED-cpd00034#cpd00099##",
              "1.10E-4",
              "8.17E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 24,
            "cells": [
              "MnCl2 x 4 H2O",
              "MnCl2",
              "SEED-cpd00030#cpd00099##",
              "3.69E-3",
              "1.87E-5"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 25,
            "cells": [
              "Yeast extract",
              "Yeast extract",
              "rich-peptone#",
              "2.00",
              "null"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 26,
            "cells": [
              "Pyridoxine HCl",
              "Pyridoxine HCl",
              "SEED-cpd00099#cpd00263##",
              "3.94E-4",
              "1.93E-6"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 27,
            "cells": [
              "Na2MoO4 x 2 H2O",
              "Na2MoO4",
              "SEED-cpd00971#cpd11145##",
              "8.57E-5",
              "3.54E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 28,
            "cells": [
              "KCl",
              "KCl",
              "SEED-cpd00099#cpd00205##",
              "0.65",
              "0.01"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 29,
            "cells": [
              "Resazurin",
              "Resazurin",
              "SEED-cpd08053###",
              "4.93E-4",
              "2.15E-6"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 30,
            "cells": [
              "p-Aminobenzoic acid",
              "p Aminobenzoic acid (PABA)",
              "SEED-cpd00443###",
              "1.28E-4",
              "9.42E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 31,
            "cells": [
              "Na2WO4 x 2 H2O",
              "Na2WO4",
              "SEED-cpd00971#cpd15574##",
              "3.94E-6",
              "2.68E-8"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 32,
            "cells": [
              "Tryptone",
              "Tryptone",
              "rich-peptone#",
              "2.00",
              "null"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 33,
            "cells": [
              "H2O",
              "H2O",
              "SEED-cpd00001###",
              "null",
              "null"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 34,
            "cells": [
              "Na-tartrate",
              "L-tartarate",
              "SEED-cpd00666#cpd00971##",
              "3.54E-3",
              "2.07E-5"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 35,
            "cells": [
              "Na2SeO3 x 5 H2O",
              "Sodium selenite",
              "SEED-cpd00971#cpd03387##",
              "2.96E-6",
              "1.11E-8"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 36,
            "cells": [
              "Distilled water",
              "H2O",
              "SEED-cpd00001###",
              "null",
              "null"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 37,
            "cells": [
              "Biotin",
              "Biotin",
              "SEED-cpd00104###",
              "1.97E-5",
              "8.11E-8"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 38,
            "cells": [
              "NH4Cl",
              "Ammonium chloride",
              "SEED-cpd00013#cpd00099##",
              "0.25",
              "0.00"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 39,
            "cells": [
              "Na-glycerophosphate",
              "Na-glycerophosphate",
              "SEED-cpd00971#cpd12183##",
              "0.10",
              "0.00"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 40,
            "cells": [
              "CaCl2 x 2 H2O",
              "Calcium chloride ",
              "SEED-cpd00063#cpd00099##",
              "1.45",
              "0.01"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 41,
            "cells": [
              "NiCl2 x 6 H2O",
              "NiCl2",
              "SEED-cpd00099#cpd00244##",
              "2.36E-5",
              "9.91E-8"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 42,
            "cells": [
              "H3BO3",
              "Boric acid",
              "SEED-cpd09225###",
              "5.70E-3",
              "9.19E-5"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 43,
            "cells": [
              "NaCl",
              "NaCl",
              "SEED-cpd00099#cpd00971##",
              "26.01",
              "0.45"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 44,
            "cells": [
              "KBr",
              "KBr",
              "SEED-cpd00205#cpd00966##",
              "0.09",
              "0.00"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 2,
            "row_index": 45,
            "cells": [
              "Na-Lactate",
              "Na-Lactate",
              "SEED-cpd00971#cpd01022##",
              "2.27",
              "0.02"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 0,
            "cells": [
              "Seed ID",
              "Name",
              "Mol Concentration"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 1,
            "cells": [
              "cpd12183",
              "(Glycerophosphate)n",
              "2.87896541498847E-4"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 2,
            "cells": [
              "cpd15574",
              "tungstate",
              "2.67534139821693E-8"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 3,
            "cells": [
              "cpd00239",
              "H2S",
              "0.0020242335522773465"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 4,
            "cells": [
              "cpd00218",
              "Niacin",
              "2.018841126830706E-6"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 5,
            "cells": [
              "cpd00048",
              "Sulfate",
              "0.02713515026728839"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 6,
            "cells": [
              "cpd00443",
              "ABEE",
              "9.417300079863235E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 7,
            "cells": [
              "cpd00644",
              "PAN",
              "5.727874824961537E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 8,
            "cells": [
              "cpd00149",
              "Co2+",
              "1.1241674217181804E-6"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 9,
            "cells": [
              "cpd00666",
              "Tartrate",
              "2.0681073312652265E-5"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 10,
            "cells": [
              "cpd00104",
              "BIOT",
              "1.6217192920055714E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 11,
            "cells": [
              "cpd00242",
              "H2CO3",
              "0.029321263984922154"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 12,
            "cells": [
              "cpd00220",
              "RIBF",
              "1.3100990291135432E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 13,
            "cells": [
              "cpd00263",
              "Pyridoxol",
              "1.9317538625360478E-6"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 14,
            "cells": [
              "cpd00541",
              "Lipoate",
              "2.4029133412033766E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 15,
            "cells": [
              "cpd00244",
              "Ni2+",
              "9.91412485073203E-8"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 16,
            "cells": [
              "cpd00166",
              "Calomide",
              "6.301750567399103E-8"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 17,
            "cells": [
              "cpd00001",
              "H2O",
              "0.9999975431559356"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 18,
            "cells": [
              "cpd10516",
              "fe3",
              "7.422489621063538E-6"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 19,
            "cells": [
              "cpd00063",
              "Ca2+",
              "0.009899655977798799"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 20,
            "cells": [
              "cpd10515",
              "Fe2+",
              "1.787685998212314E-5"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 21,
            "cells": [
              "cpd09244",
              "Sodium hydroxide",
              "2.7366513052594012E-5"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 22,
            "cells": [
              "cpd09225",
              "Boric acid",
              "9.193874387194626E-5"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 23,
            "cells": [
              "cpd09249",
              "Sodium bicarbonate",
              "0.0"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 24,
            "cells": [
              "cpd11145",
              "Sodium molybdate",
              "3.5381017284146763E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 25,
            "cells": [
              "cpd00209",
              "Nitrate",
              "0.004945549500004946"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 26,
            "cells": [
              "cpd00305",
              "THI",
              "7.323776909704017E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 27,
            "cells": [
              "cpd00205",
              "K+",
              "0.015937071520420266"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 28,
            "cells": [
              "cpd00009",
              "Phosphate",
              "0.001459547362805014"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 29,
            "cells": [
              "cpd00966",
              "HBr",
              "7.45105061263904E-4"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 30,
            "cells": [
              "cpd00971",
              "Na+",
              "0.502344109141384"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 31,
            "cells": [
              "cpd00058",
              "Cu2+",
              "3.290710513757317E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 32,
            "cells": [
              "cpd04877",
              "Magnesium chloride",
              "0.0"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 33,
            "cells": [
              "cpd00099",
              "Cl-",
              "0.5370975461446161"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 34,
            "cells": [
              "cpd00013",
              "NH3",
              "0.004647143725912191"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 35,
            "cells": [
              "cpd01022",
              "Lactate",
              "0.020231672149596286"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 36,
            "cells": [
              "cpd00254",
              "Mg",
              "0.05479400321702677"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 37,
            "cells": [
              "cpd00034",
              "Zn2+",
              "8.1740796567747E-7"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 38,
            "cells": [
              "cpd03387",
              "Selenite",
              "1.1121668521844414E-8"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 39,
            "cells": [
              "cpd00393",
              "FOL",
              "4.4883574938195196E-8"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 40,
            "cells": [
              "cpd00030",
              "Mn2+",
              "1.8697759913899182E-5"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          },
          {
            "source_key": "komodo596",
            "source_sha256": "efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78",
            "table_index": 3,
            "row_index": 41,
            "cells": [
              "cpd08053",
              "Resazurin",
              "2.1510796285881757E-6"
            ],
            "representation": "Exact decoded DOM cell text; not claimed as a literal HTML substring.",
            "scope": "Optional detail link resolved from the actual catalogue href. Preserve any failure; do not infer historical equivalence.",
            "usable": true
          }
        ],
        "representation": "Exact decoded DOM text, not a literal raw-HTML quotation"
      }
    ],
    "interpretation": "All printed provider gram/mol/model-concentration quantities are preserved together with their headers. They describe an incompatible current expansion; no model amount is silently converted to a primary-medium concentration."
  }
]

## Findings

### f1: Eight stock solutes are incompletely separated from the medium

major / open / confirmed; issue key: culturemech.006077.partial-trace-nesting.

All eight trace components are stock ingredients. The target flattens all eight; both maintained owners nest only boric acid, manganese chloride and ferrous sulfate, leaving five stock-preparation amounts represented as rates among main ingredients.

### f2: Main artificial seawater is recorded as a mass

major / open / confirmed; issue key: culturemech.006077.seawater-unit.

All three layers store999 G_PER_L for source999 ml artificial seawater. Its aquarium-salt composition differs from distilled water and is not quantitatively specified.

### f3: Tris hydrochloride is grounded to free-base tris

major / open / confirmed; issue key: culturemech.006077.tris-salt.

The source and local names say Tris HCl; CHEBI:9754 has no chloride and explicitly denotes tris base. Valid label metadata does not make it the supplied salt.

### f4: Two asserted forms exceed the primary description

major / open / provisional; issue key: culturemech.006077.form-specificity.

Source Na-tartrate does not establish L stereochemistry; source FeSO4 does not establish hydration. The local L-tartrate and anhydrous ferrous-sulfate assertions require supplier/source confirmation.

### f5: Legacy000170 remains unauthenticated

major / open / provisional; issue key: culturemech.006077.legacy-link-history.

Current exact lookup is absent for the three retained legacy KNO3 links; original historical correspondence is unknown, independent of the valid CHEBI potassium-nitrate identity.

### f6: Artificial seawater preparation is not retained across contributors and target

major / open / confirmed; issue key: culturemech.006077.preparation-projection.

The DSM owner already states that artificial seawater uses a marine aquarium salts mixture. The other owner and target lack this preparation context; the source does not provide a sterilization cycle to add.

### f7: Quantity claims lack attached source evidence

minor / open / confirmed; issue key: culturemech.006077.quantity-evidence.

Printed batch masses/doses and pH lack attached scoped evidence. The source supports those literal inputs, but final-medium and final-stock concentration denominators remain unsupported. Only the unchanged pH decisions are evidence_only; structural/unit corrections remain separate.

## Recommended Actions And Acceptance Checks

### a1

Complete the eight-component trace stock in both maintained owners, preserve1 ml dose and1000 ml stock water, then regenerate once. Avoid duplicate direct and nested ingredients.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Correct the maintained solvent volume basis and material description, retaining unquantified salinity; regenerate without density assumptions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve the exact hydrochloride term from authoritative ontology evidence or remove the incompatible link pending resolution; retain the source1 g amount and do not invent a replacement ID.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Resolve the exact supplied materials without guessing an opposite enantiomer or hydrate. Preserve literal source names/masses and flag unsupported specificity pending evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Recover historical mapping provenance or explicitly retire/replace the legacy link using verified current correspondence; preserve append-only history and do not invent its earlier meaning.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Preserve the DSM owner’s existing scoped preparation in the corrected maintained contribution and later target projection, without inventing salinity, oxygen or an autoclave cycle.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a7

Attach short versioned DSM rows to the exact maintained batch quantities and pH; establish any final-volume basis before attaching evidence to a normalized rate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch043/429/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch043/429/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml:1:id: CultureMech:006077<br>./data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml:1:id: CultureMech:006077<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch043/source-preflight-bound/429/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 16 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| dsm-main | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf; Main recipe and complete Trace elements subsection | supports | The full primary distinguishes 999 ml artificial seawater and 1 ml trace-stock dose from the eight-solute stock prepared with 1000 ml distilled water. No sterilization cycle or growth conditions beyond pH7.0 are stated. |
| provider-conflict | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=596; All detail tables, particularly table2 ingredient rows and table3 SEED amounts | supports | Current KOMODO596 gives45 ingredient rows plus41 model-metabolite rows unlike the scoped DSM596 primary. Treat this as provider inconsistency; do not import additional minerals/vitamins or interpret its Is Aerobic false flag as primary growth evidence. |
| api596-attempt | https://mediadive.dsmz.de/rest/medium/596; Preserved exact public retrieval result | context_only | The exact current MediaDive REST596 request returned HTTP503 once. The DSM primary remains usable; the failure is not recipe absence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63017; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63017 resolves to sodium L-tartrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63043 resolves to potassium nitrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75832 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75832; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75832 resolves to iron(2+) sulfate (anhydrous). Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi9754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:9754 resolves to tris. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63017": [{"label": "Sodium tartrate", "match_type": "preferred_term", "identifier": "CHEBI:63017", "preferred_term": "Sodium tartrate", "ontology_id": "CHEBI:63017", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75832": [{"label": "FeSO4", "match_type": "preferred_term", "identifier": "CHEBI:75832", "preferred_term": "FeSO4", "ontology_id": "CHEBI:75832", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| legacy-mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact current lookup of MediaIngredientMech:000170 in all three KNO3 fields; pinned current catalog/tree | context_only | The current index has no exact legacy000170 row; catalog/tree snapshots likewise do not authenticate its historical KNO3 identity. The primary CHEBI63043 potassium nitrate match is separate. |
| history-metadata | data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:15.858768"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:15.858768"}]}, {"input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml", "events": 9, "timestamp_issues": []}] |
| writer-0 | scripts/record_review.py; Current review/validation infrastructure; exact inspected input hash | context_only | Review serialization, reference checks or strict validation infrastructure only. This code is not an importer, recipe merger or repair transform and does not establish historical formulation causation. |
| writer-1 | scripts/validate_recipe_references.py; Current review/validation infrastructure; exact inspected input hash | context_only | Review serialization, reference checks or strict validation infrastructure only. This code is not an importer, recipe merger or repair transform and does not establish historical formulation causation. |
| writer-2 | scripts/validate_strict.py; Current review/validation infrastructure; exact inspected input hash | context_only | Review serialization, reference checks or strict validation infrastructure only. This code is not an importer, recipe merger or repair transform and does not establish historical formulation causation. |
| writer-3 | src/culturemech/merge/fingerprint.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current resolver/nesting/merge functions provide context only. August7 owner nesting postdates the August6 generated projection. Credit the partial owner repair and correct its scope; do not claim the present guarded merger was executed historically or necessarily caused every missing field. |
| writer-4 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current resolver/nesting/merge functions provide context only. August7 owner nesting postdates the August6 generated projection. Credit the partial owner repair and correct its scope; do not claim the present guarded merger was executed historically or necessarily caused every missing field. |
| writer-5 | src/culturemech/merge/matcher.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current resolver/nesting/merge functions provide context only. August7 owner nesting postdates the August6 generated projection. Credit the partial owner repair and correct its scope; do not claim the present guarded merger was executed historically or necessarily caused every missing field. |
| writer-6 | src/culturemech/merge/merge_recipes.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current resolver/nesting/merge functions provide context only. August7 owner nesting postdates the August6 generated projection. Credit the partial owner repair and correct its scope; do not claim the present guarded merger was executed historically or necessarily caused every missing field. |
| writer-7 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current resolver/nesting/merge functions provide context only. August7 owner nesting postdates the August6 generated projection. Credit the partial owner repair and correct its scope; do not claim the present guarded merger was executed historically or necessarily caused every missing field. |
| writer-8 | scripts/apply_cocktail_nesting.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current resolver/nesting/merge functions provide context only. August7 owner nesting postdates the August6 generated projection. Credit the partial owner repair and correct its scope; do not claim the present guarded merger was executed historically or necessarily caused every missing field. |
| writer-9 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current resolver/nesting/merge functions provide context only. August7 owner nesting postdates the August6 generated projection. Credit the partial owner repair and correct its scope; do not claim the present guarded merger was executed historically or necessarily caused every missing field. |
| historical-report-0 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml.md; Exact identity-matched report header and preserved full report context | context_only | Derivative historical concentration triage only; no source response hash is authenticated by this report alone, and no complete manual report-row read is claimed here. |
| historical-report-1 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/blastococcus_aggregatus_medium.yaml.md; Exact identity-matched report header and preserved full report context | context_only | Derivative historical concentration triage only; no source response hash is authenticated by this report alone, and no complete manual report-row read is claimed here. |
| historical-report-2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.md; Exact identity-matched report header and preserved full report context | context_only | Derivative historical concentration triage only; no source response hash is authenticated by this report alone, and no complete manual report-row read is claimed here. |
| historical-report-3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.md; Exact identity-matched report header and preserved full report context | context_only | Derivative historical concentration triage only; no source response hash is authenticated by this report alone, and no complete manual report-row read is claimed here. |
| historical-report-4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/blastococcus_aggregatus_medium.md; Exact identity-matched report header and preserved full report context | context_only | Derivative historical concentration triage only; no source response hash is authenticated by this report alone, and no complete manual report-row read is claimed here. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch043/429/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact current MediaDive REST596 request returned HTTP503 once. The DSM primary remains usable; the failure is not recipe absence.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T003735Z-culturemech-006077-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: blastococcus_aggregatus_medium (CultureMech:006077)'
started_at: '2026-10-22T00:25:09Z'
finished_at: '2026-10-22T00:37:35Z'
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
summary: DSM596 establishes five base solutes, 999 ml artificial seawater and a 1
  ml addition of a separate eight-solute trace stock. The target flattens all eight
  stock-preparation amounts represented as rates; both maintained owners nest only
  three, leaving five as stock-preparation rates in the main medium. Seawater has
  a mass-unit error, Tris HCl is mapped to tris base, and current provider and legacy-link
  uncertainty require a partial review.
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
  - path: data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    sha256: cc153923bd4ca830f66c9762086a1370323f8fa146d88c3a390edc0b581edba5
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    sha256: cecd630282ed22be68b61121967bc23c29e12d190715bfc045e1cddf11f760d6
    role: context
  - path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
    sha256: 72bec7f3e2be0629489d414930b65e721ff6406bbda7431a520db1b5e9c2de0a
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml.md
    sha256: dc50ad52019ab773f77174e756ad020069d802a7d0d964d1acb4eb859c6f95bf
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/blastococcus_aggregatus_medium.yaml.md
    sha256: 0cee08270e51e65a5f02dbde4e44ca1cb3230c035855bd1519a78a147cc4ff7d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.md
    sha256: c831521c97f6359375aed9d61b0904c7743463f45f48320e5576c9c1eb71dfa4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.md
    sha256: c7a9dba9a6f98ad1841049a3c5fbc8dbd096ab49512ea7b1cb36ae30f45f7739
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/blastococcus_aggregatus_medium.md
    sha256: 5e224bb7dfbec54a7e206f4b41146819df8860ed215cbea3b77f1e2dd2370297
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
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
  selection: Task review 429; batch 043 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding forty-two task batches
    contain 420 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 423 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006077
targets:
- target_id: CultureMech:006077
  path: data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
  label: blastococcus_aggregatus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch043/429/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch043/429/strict.tsv"
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006077
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
  - CultureMech:006077
- check_id: api596-source-access
  name: 'Exact source content access: api596'
  required: false
  status: unavailable
  summary: The exact current MediaDive REST596 request returned HTTP503 once. The
    DSM primary remains usable; the failure is not recipe absence.
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - api596-attempt
- check_id: legacy-id-history
  name: Authenticate original legacy000170 correspondence
  required: true
  status: unavailable
  summary: Current negative lookup is available; historical original mapping bytes
    are not authenticated.
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - legacy-mim
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T00:26:02.629949Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch043/429/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T00:26:03.623860Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch043/429/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T00:26:04.690804Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T00:26:05.410473Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T00:29:25Z'
  support: supports
  summary: './data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml:1:id: CultureMech:006077

    ./data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml:1:id:
    CultureMech:006077

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/source-preflight-bound/429/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T00:29:25Z'
  support: supports
  summary: 16 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 68cb098cc8dd6b12b7ae16a667c99597c1aeb0d4fd9db14e66dd7075f61311e0
- evidence_id: dsm-main
  kind: database
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf
  locator: Main recipe and complete Trace elements subsection
  accessed_at: '2026-10-22T00:07:26.299540Z'
  support: supports
  summary: The full primary distinguishes 999 ml artificial seawater and 1 ml trace-stock
    dose from the eight-solute stock prepared with 1000 ml distilled water. No sterilization
    cycle or growth conditions beyond pH7.0 are stated.
  snapshot_sha256: 203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96
- evidence_id: provider-conflict
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=596
  locator: All detail tables, particularly table2 ingredient rows and table3 SEED
    amounts
  accessed_at: '2026-10-22T00:07:27.304266Z'
  support: supports
  summary: Current KOMODO596 gives45 ingredient rows plus41 model-metabolite rows
    unlike the scoped DSM596 primary. Treat this as provider inconsistency; do not
    import additional minerals/vitamins or interpret its Is Aerobic false flag as
    primary growth evidence.
  snapshot_sha256: efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78
- evidence_id: api596-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/596
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T00:07:26.786791Z'
  support: context_only
  summary: The exact current MediaDive REST596 request returned HTTP503 once. The
    DSM primary remains usable; the failure is not recipe absence.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to zinc dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63017
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63017
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-22T00:17:21.640183Z'
  support: supports
  summary: CHEBI:63017 resolves to sodium L-tartrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 48a690e4e88e827561077dffff4f26c28a8cfd4328580168538e1b635221ecea
- evidence_id: chebi63043
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:40.679699Z'
  support: supports
  summary: CHEBI:63043 resolves to potassium nitrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: c324450e6330a169c708c32a7908b6df0276f4dc76da413e473b563928f61c13
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75832
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75832
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:01:47.645147Z'
  support: supports
  summary: CHEBI:75832 resolves to iron(2+) sulfate (anhydrous). Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b9119cb3893b1a8171f719ef3e8fe6e5775a4fd59575baec8cd6da953801d089
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi9754
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:13.713319Z'
  support: supports
  summary: CHEBI:9754 resolves to tris. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b9f921dfa34f343d4ef51ee217fc47702a8f03e2b9a8353effa10de89e9c6659
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-22T00:29:25Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:33118":
    [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label":
    "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63017": [{"label":
    "Sodium tartrate", "match_type": "preferred_term", "identifier": "CHEBI:63017",
    "preferred_term": "Sodium tartrate", "ontology_id": "CHEBI:63017", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75832": [{"label": "FeSO4", "match_type": "preferred_term",
    "identifier": "CHEBI:75832", "preferred_term": "FeSO4", "ontology_id": "CHEBI:75832",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label":
    "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term":
    "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: legacy-mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact current lookup of MediaIngredientMech:000170 in all three KNO3 fields;
    pinned current catalog/tree
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: The current index has no exact legacy000170 row; catalog/tree snapshots
    likewise do not authenticate its historical KNO3 identity. The primary CHEBI63043
    potassium nitrate match is separate.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml;
    data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:15.858768"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml",
    "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:15.858768"}]}, {"input": "data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml",
    "events": 9, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: scripts/record_review.py
  locator: Current review/validation infrastructure; exact inspected input hash
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Review serialization, reference checks or strict validation infrastructure
    only. This code is not an importer, recipe merger or repair transform and does
    not establish historical formulation causation.
  snapshot_sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
- evidence_id: writer-1
  kind: record_content
  reference: scripts/validate_recipe_references.py
  locator: Current review/validation infrastructure; exact inspected input hash
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Review serialization, reference checks or strict validation infrastructure
    only. This code is not an importer, recipe merger or repair transform and does
    not establish historical formulation causation.
  snapshot_sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
- evidence_id: writer-2
  kind: record_content
  reference: scripts/validate_strict.py
  locator: Current review/validation infrastructure; exact inspected input hash
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Review serialization, reference checks or strict validation infrastructure
    only. This code is not an importer, recipe merger or repair transform and does
    not establish historical formulation causation.
  snapshot_sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/fingerprint.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Current resolver/nesting/merge functions provide context only. August7
    owner nesting postdates the August6 generated projection. Credit the partial owner
    repair and correct its scope; do not claim the present guarded merger was executed
    historically or necessarily caused every missing field.
  snapshot_sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
- evidence_id: writer-4
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Current resolver/nesting/merge functions provide context only. August7
    owner nesting postdates the August6 generated projection. Credit the partial owner
    repair and correct its scope; do not claim the present guarded merger was executed
    historically or necessarily caused every missing field.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-5
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Current resolver/nesting/merge functions provide context only. August7
    owner nesting postdates the August6 generated projection. Credit the partial owner
    repair and correct its scope; do not claim the present guarded merger was executed
    historically or necessarily caused every missing field.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-6
  kind: record_content
  reference: src/culturemech/merge/merge_recipes.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Current resolver/nesting/merge functions provide context only. August7
    owner nesting postdates the August6 generated projection. Credit the partial owner
    repair and correct its scope; do not claim the present guarded merger was executed
    historically or necessarily caused every missing field.
  snapshot_sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
- evidence_id: writer-7
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Current resolver/nesting/merge functions provide context only. August7
    owner nesting postdates the August6 generated projection. Credit the partial owner
    repair and correct its scope; do not claim the present guarded merger was executed
    historically or necessarily caused every missing field.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-8
  kind: record_content
  reference: scripts/apply_cocktail_nesting.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Current resolver/nesting/merge functions provide context only. August7
    owner nesting postdates the August6 generated projection. Credit the partial owner
    repair and correct its scope; do not claim the present guarded merger was executed
    historically or necessarily caused every missing field.
  snapshot_sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
- evidence_id: writer-9
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Current resolver/nesting/merge functions provide context only. August7
    owner nesting postdates the August6 generated projection. Credit the partial owner
    repair and correct its scope; do not claim the present guarded merger was executed
    historically or necessarily caused every missing field.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: historical-report-0
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml.md
  locator: Exact identity-matched report header and preserved full report context
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Derivative historical concentration triage only; no source response hash
    is authenticated by this report alone, and no complete manual report-row read
    is claimed here.
  snapshot_sha256: dc50ad52019ab773f77174e756ad020069d802a7d0d964d1acb4eb859c6f95bf
- evidence_id: historical-report-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/blastococcus_aggregatus_medium.yaml.md
  locator: Exact identity-matched report header and preserved full report context
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Derivative historical concentration triage only; no source response hash
    is authenticated by this report alone, and no complete manual report-row read
    is claimed here.
  snapshot_sha256: 0cee08270e51e65a5f02dbde4e44ca1cb3230c035855bd1519a78a147cc4ff7d
- evidence_id: historical-report-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.md
  locator: Exact identity-matched report header and preserved full report context
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Derivative historical concentration triage only; no source response hash
    is authenticated by this report alone, and no complete manual report-row read
    is claimed here.
  snapshot_sha256: c831521c97f6359375aed9d61b0904c7743463f45f48320e5576c9c1eb71dfa4
- evidence_id: historical-report-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.md
  locator: Exact identity-matched report header and preserved full report context
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Derivative historical concentration triage only; no source response hash
    is authenticated by this report alone, and no complete manual report-row read
    is claimed here.
  snapshot_sha256: c7a9dba9a6f98ad1841049a3c5fbc8dbd096ab49512ea7b1cb36ae30f45f7739
- evidence_id: historical-report-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/blastococcus_aggregatus_medium.md
  locator: Exact identity-matched report header and preserved full report context
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Derivative historical concentration triage only; no source response hash
    is authenticated by this report alone, and no complete manual report-row read
    is claimed here.
  snapshot_sha256: 5e224bb7dfbec54a7e206f4b41146819df8860ed215cbea3b77f1e2dd2370297
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/429/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T00:29:25Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 5f3f51c35cb7ad472d5b9e21ee59cbe6b00ca2f3941b5b3ecd5aa54cb8b6e082
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: DSM596 and linked KOMODO contributor
  outcome: supported
  summary: The exact generated target derives from two maintained source records with
    distinct IDs; their current SOURCE_DUPLICATE relation and local copied signatures
    establish local relationship context. Current KOMODO contents differ from the
    DSM primary and cannot establish contemporary whole-formula equivalence.
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - id-search
  - dsm-main
  - provider-conflict
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '10 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 10/14
    primary and 8/14 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi33118
  - chebi49976
  - chebi53503
  - chebi63017
  - chebi63043
  - chebi75213
  - chebi75832
  - chebi86318
  - chebi86368
  - chebi9754
  details: 'Instance coverage on a 0–100 percent scale, denominator 14: primary 71.43%;
    secondary 57.14%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: forms
  area: grounding
  topic: Source salt, hydrate and stereochemistry
  outcome: concern
  summary: Tris HCl is explicitly a hydrochloride while CHEBI:9754 defines the free
    base C4H11NO3. CHEBI:63017 is stereospecific sodium L-tartrate although the primary
    only says Na-tartrate; CHEBI:75832 is anhydrous while FeSO4 hydration is unstated.
    Those latter two are unsupported specificity, not proof that another hydrate or
    enantiomer is required. KNO3, boric acid and explicit Mn tetrahydrate, Cu dihydrate,
    Co hexahydrate and molybdate dihydrate correspond to the asserted forms; zinc
    chloride is compatible with ZnCl2. Tryptone/yeast extract remain complex, and
    sodium glycerophosphate is not assigned an invented isomer.
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - dsm-main
  - chebi33118
  - chebi49976
  - chebi53503
  - chebi63017
  - chebi63043
  - chebi75213
  - chebi75832
  - chebi86318
  - chebi86368
  - chebi9754
- assessment_id: legacy-link
  area: grounding
  topic: Legacy linkage versus current CHEBI identity
  outcome: unknown
  summary: All three KNO3 instances retain MediaIngredientMech:000170. Current exact
    lookup is absent; historical original-ID meaning is unresolved rather than proven
    wrong. Do not infer its historical identity from the valid potassium-nitrate CHEBI
    term.
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - legacy-mim
  - chebi63043
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 30 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: preparation
  area: completeness
  topic: Layer-specific preparation and provider flags
  outcome: concern
  summary: The DSM owner retains pH7.0 and aquarium-salt preparation text; the KOMODO
    owner and target omit those preparation arrays although pH is structured. Preserve
    the existing DSM information. Is Aerobic false is a provider metadata flag, not
    primary evidence of anaerobic growth. No organisms or growth measurements are
    asserted.
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsm-main
  - provider-conflict
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 53 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006077
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"KNO3\",\n    \"\
    stage\": \"Main printed batch formulation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.50\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" KNO3                            \
    \                                0.50     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. \"\n  },\n  {\n    \"decision_id\": \"\
    q2\",\n    \"name\": \"Sodium glycerophosphate\",\n    \"stage\": \"Main printed\
    \ batch formulation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.10\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Na-glycerophosphate             \
    \                                0.10     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. \"\n  },\n  {\n    \"decision_id\": \"\
    q3\",\n    \"name\": \"Tris HCl\",\n    \"stage\": \"Main printed batch formulation;\
    \ data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.00\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Tris HCl                        \
    \                                1.00     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. The separate Tris hydrochloride/base mismatch\
    \ remains.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n    \"name\": \"Tryptone\"\
    ,\n    \"stage\": \"Main printed batch formulation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"2.00\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Tryptone (Difco 0123)           \
    \                                2.00     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. \"\n  },\n  {\n    \"decision_id\": \"\
    q5\",\n    \"name\": \"Yeast extract\",\n    \"stage\": \"Main printed batch formulation;\
    \ data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"2.00\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Yeast extract                   \
    \                                2.00     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. \"\n  },\n  {\n    \"decision_id\": \"\
    q6\",\n    \"name\": \"Sea water\",\n    \"stage\": \"Main solvent\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"999\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n\
    \    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"999\",\n      \"\
    printed_unit\": \"ml\",\n      \"material\": \"artificial seawater\",\n      \"\
    final_volume\": null\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Artificial sea water            \
    \                              999.00    ml\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \"Artificial sea water is prepared from a marine\
    \ aquarium salts mixture.\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The source gives 999 ml artificial\
    \ seawater; the local 999 G_PER_L has the wrong volume dimension. Correct to the\
    \ printed batch volume without asserting ML_PER_L or assuming density. Aquarium-salt\
    \ composition remains qualitatively specified; no salinity or exact salt mass\
    \ is supplied.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"name\": \"H3BO3\"\
    ,\n    \"stage\": \"Trace-stock preparation; data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2.85\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"2.85\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null,\n      \"listed_stock_water_ml\"\
    : \"1000\",\n      \"receiving_batch_dose_ml\": \"1\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n        \"\
    source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n      \
    \  \"exact_source_quote\": \" H3BO3                                          \
    \                2.85      g\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q8\",\n    \"name\": \"MnCl2 x 4 H2O\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.80\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null,\n      \"listed_stock_water_ml\"\
    : \"1000\",\n      \"receiving_batch_dose_ml\": \"1\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n        \"\
    source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n      \
    \  \"exact_source_quote\": \" MnCl2 x 4 H2O                                  \
    \                1.80      g\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q9\",\n    \"name\": \"FeSO4\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.36\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.36\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null,\n      \"listed_stock_water_ml\"\
    : \"1000\",\n      \"receiving_batch_dose_ml\": \"1\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n        \"\
    source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n      \
    \  \"exact_source_quote\": \" FeSO4                                          \
    \                1.36      g\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q10\",\n    \"name\": \"Na-tartrate\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.77\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.77\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null,\n      \"listed_stock_water_ml\"\
    : \"1000\",\n      \"receiving_batch_dose_ml\": \"1\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n        \"\
    source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n      \
    \  \"exact_source_quote\": \" Na-tartrate                                    \
    \                1.77      g\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q11\",\n    \"name\": \"CuCl2 x 2 H2O\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0269\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    26.90\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null,\n   \
    \   \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\": \"\
    1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" CuCl2 x 2 H2O                          \
    \                       26.90     mg\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q12\",\n    \"name\": \"ZnCl2\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0208\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    20.80\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null,\n   \
    \   \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\": \"\
    1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" ZnCl2                                  \
    \                       20.80     mg\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q13\",\n    \"name\": \"CoCl2 x 6 H2O\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0404\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    40.40\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null,\n   \
    \   \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\": \"\
    1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" CoCl2 x 6 H2O                          \
    \                       40.40     mg\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q14\",\n    \"name\": \"Na2MoO4 x 2 H2O\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0252\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    25.20\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null,\n   \
    \   \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\": \"\
    1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Na2MoO4 x 2 H2O                        \
    \                       25.20     mg\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"name\": \"pH\",\n    \"stage\": \"Main medium\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ph_value\",\n        \"stored\": 7.0\n      }\n    ],\n    \"desired\": 7.0,\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \"pH 7.0\",\n        \"snapshot_sha256\"\
    : \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n    \
    \    \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"Current pH agrees; attach the source\
    \ statement. No adjustment reagent or titration amount is specified.\"\n  },\n\
    \  {\n    \"decision_id\": \"q16\",\n    \"name\": \"KNO3\",\n    \"stage\": \"\
    Main printed batch formulation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.50\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" KNO3                            \
    \                                0.50     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. \"\n  },\n  {\n    \"decision_id\": \"\
    q17\",\n    \"name\": \"Sodium glycerophosphate\",\n    \"stage\": \"Main printed\
    \ batch formulation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.10\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Na-glycerophosphate             \
    \                                0.10     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. \"\n  },\n  {\n    \"decision_id\": \"\
    q18\",\n    \"name\": \"Tris HCl\",\n    \"stage\": \"Main printed batch formulation;\
    \ data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.00\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Tris HCl                        \
    \                                1.00     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. The separate Tris hydrochloride/base mismatch\
    \ remains.\"\n  },\n  {\n    \"decision_id\": \"q19\",\n    \"name\": \"Tryptone\"\
    ,\n    \"stage\": \"Main printed batch formulation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"2.00\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Tryptone (Difco 0123)           \
    \                                2.00     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. \"\n  },\n  {\n    \"decision_id\": \"\
    q20\",\n    \"name\": \"Yeast extract\",\n    \"stage\": \"Main printed batch\
    \ formulation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"2.00\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Yeast extract                   \
    \                                2.00     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. \"\n  },\n  {\n    \"decision_id\": \"\
    q21\",\n    \"name\": \"Sea water\",\n    \"stage\": \"Main solvent\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"999\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"999\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"material\": \"artificial seawater\"\
    ,\n      \"final_volume\": null\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Artificial sea water            \
    \                              999.00    ml\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \"Artificial sea water is prepared from a marine\
    \ aquarium salts mixture.\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The source gives 999 ml artificial\
    \ seawater; the local 999 G_PER_L has the wrong volume dimension. Correct to the\
    \ printed batch volume without asserting ML_PER_L or assuming density. Aquarium-salt\
    \ composition remains qualitatively specified; no salinity or exact salt mass\
    \ is supplied.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"name\": \"Na-tartrate\"\
    ,\n    \"stage\": \"Trace-stock preparation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.77\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.77\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null,\n      \"listed_stock_water_ml\"\
    : \"1000\",\n      \"receiving_batch_dose_ml\": \"1\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n        \"\
    source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n      \
    \  \"exact_source_quote\": \" Na-tartrate                                    \
    \                1.77      g\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q23\",\n    \"name\": \"CuCl2 x 2 H2O\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0269\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    26.90\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null,\n   \
    \   \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\": \"\
    1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" CuCl2 x 2 H2O                          \
    \                       26.90     mg\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q24\",\n    \"name\": \"ZnCl2\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0208\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    20.80\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null,\n   \
    \   \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\": \"\
    1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" ZnCl2                                  \
    \                       20.80     mg\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q25\",\n    \"name\": \"CoCl2 x 6 H2O\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0404\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    40.40\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null,\n   \
    \   \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\": \"\
    1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" CoCl2 x 6 H2O                          \
    \                       40.40     mg\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q26\",\n    \"name\": \"Na2MoO4 x 2 H2O\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0252\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    25.20\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null,\n   \
    \   \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\": \"\
    1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Na2MoO4 x 2 H2O                        \
    \                       25.20     mg\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q27\",\n    \"name\": \"H3BO3\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.85\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"2.85\",\n      \"printed_unit\": \"g\",\n      \"final_volume\": null,\n \
    \     \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\"\
    : \"1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" H3BO3                                  \
    \                        2.85      g\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The component is correctly nested,\
    \ but its per-final-stock-litre denominator is unsupported. The primary lists\
    \ 1000 ml water, not a final or make-up stock volume. Preserve the printed g or\
    \ mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass\
    \ fraction applies only if final stock volume is independently established as\
    \ 1000 ml; it is not source-established here. Hydration/stereochemistry issues\
    \ do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\": \"\
    q28\",\n    \"name\": \"MnCl2 x 4 H2O\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.8\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"1.80\",\n      \"printed_unit\": \"g\",\n      \"final_volume\": null,\n \
    \     \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\"\
    : \"1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" MnCl2 x 4 H2O                          \
    \                        1.80      g\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The component is correctly nested,\
    \ but its per-final-stock-litre denominator is unsupported. The primary lists\
    \ 1000 ml water, not a final or make-up stock volume. Preserve the printed g or\
    \ mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass\
    \ fraction applies only if final stock volume is independently established as\
    \ 1000 ml; it is not source-established here. Hydration/stereochemistry issues\
    \ do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\": \"\
    q29\",\n    \"name\": \"FeSO4\",\n    \"stage\": \"Trace-stock preparation; data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.36\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"1.36\",\n      \"printed_unit\": \"g\",\n      \"final_volume\": null,\n \
    \     \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\"\
    : \"1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" FeSO4                                  \
    \                        1.36      g\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The component is correctly nested,\
    \ but its per-final-stock-litre denominator is unsupported. The primary lists\
    \ 1000 ml water, not a final or make-up stock volume. Preserve the printed g or\
    \ mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass\
    \ fraction applies only if final stock volume is independently established as\
    \ 1000 ml; it is not source-established here. Hydration/stereochemistry issues\
    \ do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\": \"\
    q30\",\n    \"name\": \"Trace stock dose\",\n    \"stage\": \"Main addition\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"ML_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1\",\n\
    \      \"printed_unit\": \"ml\",\n      \"final_receiving_volume\": null\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Trace elements (see below)      \
    \                                1.00    ml\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The maintained owner preserves the\
    \ correct 1 ml dose numerator and partial stock membership, but the source does\
    \ not establish a per-litre receiving denominator. Preserve the printed batch\
    \ dose and complete all eight stock components.\"\n  },\n  {\n    \"decision_id\"\
    : \"q31\",\n    \"name\": \"Stock preparation volume\",\n    \"stage\": \"Trace\
    \ stock only\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition\
    \ and volume from MediaDive (#150).\"\n      }\n    ],\n    \"desired\": {\n \
    \     \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\"\
    : \"1\",\n      \"final_stock_volume\": null,\n      \"final_receiving_volume\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Distilled water                        \
    \                     1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The note partly preserves the printed\
    \ 1000 ml stock-water input and 1 ml batch dose, but its final-stock and per-litre\
    \ receiving claims are not established by this primary. Retain the literal inputs\
    \ and mark both denominator assumptions unresolved. The current primary does not\
    \ authenticate the historical MediaDive bytes.\"\n  },\n  {\n    \"decision_id\"\
    : \"q32\",\n    \"name\": \"pH\",\n    \"stage\": \"Main medium\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0\n      }\n \
    \   ],\n    \"desired\": 7.0,\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \"pH 7.0\",\n        \"snapshot_sha256\"\
    : \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n    \
    \    \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"Current pH agrees; attach the source\
    \ statement. No adjustment reagent or titration amount is specified.\"\n  },\n\
    \  {\n    \"decision_id\": \"q33\",\n    \"name\": \"KNO3\",\n    \"stage\": \"\
    Main printed batch formulation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.50\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" KNO3                            \
    \                                0.50     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. \"\n  },\n  {\n    \"decision_id\": \"\
    q34\",\n    \"name\": \"Sodium glycerophosphate\",\n    \"stage\": \"Main printed\
    \ batch formulation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.10\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Na-glycerophosphate             \
    \                                0.10     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. \"\n  },\n  {\n    \"decision_id\": \"\
    q35\",\n    \"name\": \"Tris HCl\",\n    \"stage\": \"Main printed batch formulation;\
    \ data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[2].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.00\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Tris HCl                        \
    \                                1.00     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. The separate Tris hydrochloride/base mismatch\
    \ remains.\"\n  },\n  {\n    \"decision_id\": \"q36\",\n    \"name\": \"Tryptone\"\
    ,\n    \"stage\": \"Main printed batch formulation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"2.00\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Tryptone (Difco 0123)           \
    \                                2.00     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. \"\n  },\n  {\n    \"decision_id\": \"\
    q37\",\n    \"name\": \"Yeast extract\",\n    \"stage\": \"Main printed batch\
    \ formulation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"2.00\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsm596\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Yeast extract                   \
    \                                2.00     g\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Artificial sea water                   \
    \                       999.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical mass agrees with the\
    \ printed batch amount. The source lists 999 ml artificial seawater plus 1 ml\
    \ trace stock, but does not declare final or make-up volume; the stored G_PER_L\
    \ denominator is therefore unsupported. Preserve the batch mass and resolve its\
    \ basis before attaching rate evidence. \"\n  },\n  {\n    \"decision_id\": \"\
    q38\",\n    \"name\": \"Sea water\",\n    \"stage\": \"Main solvent\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[5].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"999\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"999\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"material\": \"artificial seawater\"\
    ,\n      \"final_volume\": null\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Artificial sea water            \
    \                              999.00    ml\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \"Artificial sea water is prepared from a marine\
    \ aquarium salts mixture.\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The source gives 999 ml artificial\
    \ seawater; the local 999 G_PER_L has the wrong volume dimension. Correct to the\
    \ printed batch volume without asserting ML_PER_L or assuming density. Aquarium-salt\
    \ composition remains qualitatively specified; no salinity or exact salt mass\
    \ is supplied.\"\n  },\n  {\n    \"decision_id\": \"q39\",\n    \"name\": \"Na-tartrate\"\
    ,\n    \"stage\": \"Trace-stock preparation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.77\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.77\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null,\n      \"listed_stock_water_ml\"\
    : \"1000\",\n      \"receiving_batch_dose_ml\": \"1\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n        \"\
    source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n      \
    \  \"exact_source_quote\": \" Na-tartrate                                    \
    \                1.77      g\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q40\",\n    \"name\": \"CuCl2 x 2 H2O\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[7].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.0269\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    26.90\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null,\n   \
    \   \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\": \"\
    1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" CuCl2 x 2 H2O                          \
    \                       26.90     mg\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q41\",\n    \"name\": \"ZnCl2\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[8].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.0208\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    20.80\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null,\n   \
    \   \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\": \"\
    1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" ZnCl2                                  \
    \                       20.80     mg\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q42\",\n    \"name\": \"CoCl2 x 6 H2O\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[9].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.0404\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    40.40\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null,\n   \
    \   \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\": \"\
    1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" CoCl2 x 6 H2O                          \
    \                       40.40     mg\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q43\",\n    \"name\": \"Na2MoO4 x 2 H2O\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0252\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    25.20\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null,\n   \
    \   \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\": \"\
    1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Na2MoO4 x 2 H2O                        \
    \                       25.20     mg\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"This printed stock-preparation amount\
    \ is incorrectly represented as a direct main-medium rate; restore its stock stage.\
    \ The primary lists 1000 ml water, not a final or make-up stock volume. Preserve\
    \ the printed g or mg amount and the receiving 1 ml batch dose. A one-thousandth\
    \ delivered-mass fraction applies only if final stock volume is independently\
    \ established as 1000 ml; it is not source-established here. Hydration/stereochemistry\
    \ issues do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\"\
    : \"q44\",\n    \"name\": \"H3BO3\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n  \
    \      \"field_path\": \"solutions[0].composition[0].concentration\",\n      \
    \  \"stored\": {\n          \"value\": \"2.85\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"2.85\",\n      \"printed_unit\": \"g\",\n      \"final_volume\": null,\n \
    \     \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\"\
    : \"1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" H3BO3                                  \
    \                        2.85      g\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The component is correctly nested,\
    \ but its per-final-stock-litre denominator is unsupported. The primary lists\
    \ 1000 ml water, not a final or make-up stock volume. Preserve the printed g or\
    \ mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass\
    \ fraction applies only if final stock volume is independently established as\
    \ 1000 ml; it is not source-established here. Hydration/stereochemistry issues\
    \ do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\": \"\
    q45\",\n    \"name\": \"MnCl2 x 4 H2O\",\n    \"stage\": \"Trace-stock preparation;\
    \ data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n  \
    \      \"field_path\": \"solutions[0].composition[1].concentration\",\n      \
    \  \"stored\": {\n          \"value\": \"1.8\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"1.80\",\n      \"printed_unit\": \"g\",\n      \"final_volume\": null,\n \
    \     \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\"\
    : \"1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" MnCl2 x 4 H2O                          \
    \                        1.80      g\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The component is correctly nested,\
    \ but its per-final-stock-litre denominator is unsupported. The primary lists\
    \ 1000 ml water, not a final or make-up stock volume. Preserve the printed g or\
    \ mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass\
    \ fraction applies only if final stock volume is independently established as\
    \ 1000 ml; it is not source-established here. Hydration/stereochemistry issues\
    \ do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\": \"\
    q46\",\n    \"name\": \"FeSO4\",\n    \"stage\": \"Trace-stock preparation; data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.36\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"1.36\",\n      \"printed_unit\": \"g\",\n      \"final_volume\": null,\n \
    \     \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\"\
    : \"1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" FeSO4                                  \
    \                        1.36      g\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 Trace elements stock; exact printed row\",\n\
    \        \"exact_source_quote\": \" Distilled water                          \
    \                   1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The component is correctly nested,\
    \ but its per-final-stock-litre denominator is unsupported. The primary lists\
    \ 1000 ml water, not a final or make-up stock volume. Preserve the printed g or\
    \ mg amount and the receiving 1 ml batch dose. A one-thousandth delivered-mass\
    \ fraction applies only if final stock volume is independently established as\
    \ 1000 ml; it is not source-established here. Hydration/stereochemistry issues\
    \ do not change the literal batch mass.\"\n  },\n  {\n    \"decision_id\": \"\
    q47\",\n    \"name\": \"Trace stock dose\",\n    \"stage\": \"Main addition\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"ML_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1\",\n\
    \      \"printed_unit\": \"ml\",\n      \"final_receiving_volume\": null\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Trace elements (see below)      \
    \                                1.00    ml\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The maintained owner preserves the\
    \ correct 1 ml dose numerator and partial stock membership, but the source does\
    \ not establish a per-litre receiving denominator. Preserve the printed batch\
    \ dose and complete all eight stock components.\"\n  },\n  {\n    \"decision_id\"\
    : \"q48\",\n    \"name\": \"Stock preparation volume\",\n    \"stage\": \"Trace\
    \ stock only\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition\
    \ and volume from MediaDive (#150).\"\n      }\n    ],\n    \"desired\": {\n \
    \     \"listed_stock_water_ml\": \"1000\",\n      \"receiving_batch_dose_ml\"\
    : \"1\",\n      \"final_stock_volume\": null,\n      \"final_receiving_volume\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Distilled water                        \
    \                     1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      },\n      {\n        \"source_key\": \"dsm596\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\",\n    \
    \    \"source_locator\": \"DSM596 main table/preparation; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Trace elements (see below)             \
    \                         1.00    ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The note partly preserves the printed\
    \ 1000 ml stock-water input and 1 ml batch dose, but its final-stock and per-litre\
    \ receiving claims are not established by this primary. Retain the literal inputs\
    \ and mark both denominator assumptions unresolved. The current primary does not\
    \ authenticate the historical MediaDive bytes.\"\n  },\n  {\n    \"decision_id\"\
    : \"q49\",\n    \"name\": \"pH\",\n    \"stage\": \"Main medium\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml\",\n      \
    \  \"field_path\": \"ph_value\",\n        \"stored\": 7.0\n      }\n    ],\n \
    \   \"desired\": 7.0,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \"pH 7.0\",\n        \"snapshot_sha256\"\
    : \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n    \
    \    \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"Current pH agrees; attach the source\
    \ statement. No adjustment reagent or titration amount is specified.\"\n  },\n\
    \  {\n    \"decision_id\": \"q50\",\n    \"name\": \"Trace stock dose\",\n   \
    \ \"stage\": \"Generated target omission\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [],\n    \"desired\": {\n      \"printed_batch_amount\": \"1\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_receiving_volume\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsm596\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \" Trace elements (see below)      \
    \                                1.00    ml\",\n        \"snapshot_sha256\": \"\
    203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\",\n        \"\
    parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the complete scoped stock\
    \ and the printed 1 ml batch dose through maintained-owner correction and authorized\
    \ regeneration. The primary does not declare the receiving final volume; do not\
    \ supply ML_PER_L or duplicate flattened and nested components.\"\n  },\n  {\n\
    \    \"decision_id\": \"q51\",\n    \"name\": \"Stock water\",\n    \"stage\"\
    : \"Trace preparation only\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [],\n    \"desired\": {\n      \"value\": \"1000\",\n      \"unit\": \"ML\"\
    ,\n      \"basis\": \"stock preparation\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 Trace elements stock; exact printed row\"\
    ,\n        \"exact_source_quote\": \" Distilled water                        \
    \                     1000.00     ml\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"Stock water is described in owner\
    \ notes but absent as a composition solvent; keep it separate from the main999\
    \ ml artificial seawater. Do not add another litre of water to the main medium.\"\
    \n  },\n  {\n    \"decision_id\": \"q52\",\n    \"name\": \"Aquarium salts quantity,\
    \ sterilization and growth conditions\",\n    \"stage\": \"Source-only unresolved\
    \ protocol\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\": [],\n\
    \    \"desired\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsm596\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium596.pdf\"\
    ,\n        \"source_locator\": \"DSM596 main table/preparation; exact printed\
    \ row\",\n        \"exact_source_quote\": \"Artificial sea water is prepared from\
    \ a marine aquarium salts mixture.\",\n        \"snapshot_sha256\": \"203c54ba06836274a831541df4ba79ad2d36a985a4720fe0fc5a15a9ed953c96\"\
    ,\n        \"parsed_text_sha256\": \"d39dbe24194674a5c6f9f363cae1009e1eac54534254e6f41a5199eb5004c7be\"\
    \n      }\n    ],\n    \"interpretation\": \"The source names a marine aquarium\
    \ salts mixture but gives no salt mass/salinity. It specifies no sterilization\
    \ cycle, incubation temperature, gas, rate or empirical growth measurement; no\
    \ defaults are supplied.\"\n  },\n  {\n    \"decision_id\": \"q53\",\n    \"name\"\
    : \"Entire conflicting KOMODO quantity tables\",\n    \"stage\": \"Provider comparison\
    \ only; excluded from DSM formula transfer\",\n    \"decision\": \"conflict\"\
    ,\n    \"local_fields\": [],\n    \"desired\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodo596\",\n        \"source_url\":\
    \ \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=596\"\
    ,\n        \"source_locator\": \"HTML table2 rows0–45 and table3 rows0–41\",\n\
    \        \"snapshot_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n        \"decoded_table_rows\": [\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 0,\n          \
    \  \"cells\": [\n              \"Name\",\n              \"Semi unique name\",\n\
    \              \"Unique Name\",\n              \"Gram Amount\",\n            \
    \  \"Mol Amount\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 1,\n          \
    \  \"cells\": [\n              \"NaHCO3\",\n              \"sodium bicarbonate\"\
    ,\n              \"SEED-cpd00242#cpd00971#cpd09249#\",\n              \"2.46\"\
    ,\n              \"0.03\"\n            ],\n            \"representation\": \"\
    Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n   \
    \         \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 2,\n          \
    \  \"cells\": [\n              \"D(+)-Biotin\",\n              \"D(+)-Biotin\"\
    ,\n              \"SEED-cpd00104###\",\n              \"1.97E-5\",\n         \
    \     \"8.11E-8\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 3,\n          \
    \  \"cells\": [\n              \"D-Ca-pantothenate\",\n              \"D-Ca-pantothenate\"\
    ,\n              \"SEED-cpd00063#cpd00644##\",\n              \"4.93E-5\",\n \
    \             \"1.91E-7\"\n            ],\n            \"representation\": \"\
    Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n   \
    \         \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 4,\n          \
    \  \"cells\": [\n              \"Lipoic acid\",\n              \"Lipoic acid\"\
    ,\n              \"SEED-cpd00541###\",\n              \"4.93E-5\",\n         \
    \     \"2.40E-7\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 5,\n          \
    \  \"cells\": [\n              \"Calcium pantothenate\",\n              \"Calcium\
    \ pantothenate\",\n              \"SEED-cpd00063#cpd00644##\",\n             \
    \ \"9.85E-5\",\n              \"3.82E-7\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 6,\n          \
    \  \"cells\": [\n              \"Tris HCl\",\n              \"Tris-HCl\",\n  \
    \            \"Tris#\",\n              \"1.00\",\n              \"0.01\"\n   \
    \         ],\n            \"representation\": \"Exact decoded DOM cell text; not\
    \ claimed as a literal HTML substring.\",\n            \"scope\": \"Optional detail\
    \ link resolved from the actual catalogue href. Preserve any failure; do not infer\
    \ historical equivalence.\",\n            \"usable\": true\n          },\n   \
    \       {\n            \"source_key\": \"komodo596\",\n            \"source_sha256\"\
    : \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\",\n    \
    \        \"table_index\": 2,\n            \"row_index\": 7,\n            \"cells\"\
    : [\n              \"KNO3\",\n              \"KNO3\",\n              \"SEED-cpd00205#cpd00209##\"\
    ,\n              \"0.50\",\n              \"0.00\"\n            ],\n         \
    \   \"representation\": \"Exact decoded DOM cell text; not claimed as a literal\
    \ HTML substring.\",\n            \"scope\": \"Optional detail link resolved from\
    \ the actual catalogue href. Preserve any failure; do not infer historical equivalence.\"\
    ,\n            \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 8,\n          \
    \  \"cells\": [\n              \"Na2S x 9 H2O\",\n              \"Sodium sulfide\
    \ hydrate\",\n              \"SEED-cpd00239#cpd00971##\",\n              \"0.49\"\
    ,\n              \"0.00\"\n            ],\n            \"representation\": \"\
    Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n   \
    \         \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 9,\n          \
    \  \"cells\": [\n              \"Nicotinic acid\",\n              \"Niacin\",\n\
    \              \"SEED-cpd00218###\",\n              \"2.46E-4\",\n           \
    \   \"2.02E-6\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 10,\n         \
    \   \"cells\": [\n              \"Riboflavin\",\n              \"Riboflavin\"\
    ,\n              \"SEED-cpd00220###\",\n              \"4.93E-5\",\n         \
    \     \"1.31E-7\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 11,\n         \
    \   \"cells\": [\n              \"NaOH\",\n              \"Sodium hydroxide\"\
    ,\n              \"SEED-cpd09244###\",\n              \"4.93E-4\",\n         \
    \     \"2.74E-5\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 12,\n         \
    \   \"cells\": [\n              \"MgCl2 x 6 H2O\",\n              \"Magnesium\
    \ chloride\",\n              \"SEED-cpd00099#cpd00254#cpd04877#\",\n         \
    \     \"5.62\",\n              \"0.03\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 13,\n         \
    \   \"cells\": [\n              \"KH2PO4\",\n              \"Potassium dihydrogen\
    \ phosphate\",\n              \"SEED-cpd00009#cpd00205##\",\n              \"\
    0.20\",\n              \"0.00\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 14,\n         \
    \   \"cells\": [\n              \"CoCl2 x 6 H2O\",\n              \"CoCl2\",\n\
    \              \"SEED-cpd00099#cpd00149##\",\n              \"2.67E-4\",\n   \
    \           \"1.12E-6\"\n            ],\n            \"representation\": \"Exact\
    \ decoded DOM cell text; not claimed as a literal HTML substring.\",\n       \
    \     \"scope\": \"Optional detail link resolved from the actual catalogue href.\
    \ Preserve any failure; do not infer historical equivalence.\",\n            \"\
    usable\": true\n          },\n          {\n            \"source_key\": \"komodo596\"\
    ,\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 15,\n         \
    \   \"cells\": [\n              \"CuCl2 x 2 H2O\",\n              \"CuCl2\",\n\
    \              \"SEED-cpd00058#cpd00099##\",\n              \"5.57E-5\",\n   \
    \           \"3.29E-7\"\n            ],\n            \"representation\": \"Exact\
    \ decoded DOM cell text; not claimed as a literal HTML substring.\",\n       \
    \     \"scope\": \"Optional detail link resolved from the actual catalogue href.\
    \ Preserve any failure; do not infer historical equivalence.\",\n            \"\
    usable\": true\n          },\n          {\n            \"source_key\": \"komodo596\"\
    ,\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 16,\n         \
    \   \"cells\": [\n              \"Vitamin B12\",\n              \"Coenzyme B12\"\
    ,\n              \"SEED-cpd00166###\",\n              \"9.95E-5\",\n         \
    \     \"6.30E-8\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 17,\n         \
    \   \"cells\": [\n              \"FeCl2 x 4 H2O\",\n              \"Iron chloride\"\
    ,\n              \"SEED-cpd00099#cpd10516##\",\n              \"1.47E-3\",\n \
    \             \"7.42E-6\"\n            ],\n            \"representation\": \"\
    Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n   \
    \         \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 18,\n         \
    \   \"cells\": [\n              \"MgSO4 x 7 H2O\",\n              \"Magnesium\
    \ sulfate\",\n              \"SEED-cpd00048#cpd00254##\",\n              \"6.70\"\
    ,\n              \"0.03\"\n            ],\n            \"representation\": \"\
    Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n   \
    \         \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 19,\n         \
    \   \"cells\": [\n              \"Folic acid\",\n              \"Folic acid\"\
    ,\n              \"SEED-cpd00393###\",\n              \"1.97E-5\",\n         \
    \     \"4.49E-8\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 20,\n         \
    \   \"cells\": [\n              \"Thiamine-HCl x 2 H2O\",\n              \"Thiamine-HCl\"\
    ,\n              \"SEED-cpd00099#cpd00305##\",\n              \"2.46E-4\",\n \
    \             \"7.32E-7\"\n            ],\n            \"representation\": \"\
    Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n   \
    \         \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 21,\n         \
    \   \"cells\": [\n              \"HCl\",\n              \"HCl\",\n           \
    \   \"SEED-cpd00099###\",\n              \"6.62E-4\",\n              \"1.89E-5\"\
    \n            ],\n            \"representation\": \"Exact decoded DOM cell text;\
    \ not claimed as a literal HTML substring.\",\n            \"scope\": \"Optional\
    \ detail link resolved from the actual catalogue href. Preserve any failure; do\
    \ not infer historical equivalence.\",\n            \"usable\": true\n       \
    \   },\n          {\n            \"source_key\": \"komodo596\",\n            \"\
    source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 22,\n         \
    \   \"cells\": [\n              \"FeSO4\",\n              \"Iron sulfate\",\n\
    \              \"SEED-cpd00048#cpd10515##\",\n              \"2.72E-3\",\n   \
    \           \"1.79E-5\"\n            ],\n            \"representation\": \"Exact\
    \ decoded DOM cell text; not claimed as a literal HTML substring.\",\n       \
    \     \"scope\": \"Optional detail link resolved from the actual catalogue href.\
    \ Preserve any failure; do not infer historical equivalence.\",\n            \"\
    usable\": true\n          },\n          {\n            \"source_key\": \"komodo596\"\
    ,\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 23,\n         \
    \   \"cells\": [\n              \"ZnCl2\",\n              \"ZnCl2\",\n       \
    \       \"SEED-cpd00034#cpd00099##\",\n              \"1.10E-4\",\n          \
    \    \"8.17E-7\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 24,\n         \
    \   \"cells\": [\n              \"MnCl2 x 4 H2O\",\n              \"MnCl2\",\n\
    \              \"SEED-cpd00030#cpd00099##\",\n              \"3.69E-3\",\n   \
    \           \"1.87E-5\"\n            ],\n            \"representation\": \"Exact\
    \ decoded DOM cell text; not claimed as a literal HTML substring.\",\n       \
    \     \"scope\": \"Optional detail link resolved from the actual catalogue href.\
    \ Preserve any failure; do not infer historical equivalence.\",\n            \"\
    usable\": true\n          },\n          {\n            \"source_key\": \"komodo596\"\
    ,\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 25,\n         \
    \   \"cells\": [\n              \"Yeast extract\",\n              \"Yeast extract\"\
    ,\n              \"rich-peptone#\",\n              \"2.00\",\n              \"\
    null\"\n            ],\n            \"representation\": \"Exact decoded DOM cell\
    \ text; not claimed as a literal HTML substring.\",\n            \"scope\": \"\
    Optional detail link resolved from the actual catalogue href. Preserve any failure;\
    \ do not infer historical equivalence.\",\n            \"usable\": true\n    \
    \      },\n          {\n            \"source_key\": \"komodo596\",\n         \
    \   \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 26,\n         \
    \   \"cells\": [\n              \"Pyridoxine HCl\",\n              \"Pyridoxine\
    \ HCl\",\n              \"SEED-cpd00099#cpd00263##\",\n              \"3.94E-4\"\
    ,\n              \"1.93E-6\"\n            ],\n            \"representation\":\
    \ \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 27,\n         \
    \   \"cells\": [\n              \"Na2MoO4 x 2 H2O\",\n              \"Na2MoO4\"\
    ,\n              \"SEED-cpd00971#cpd11145##\",\n              \"8.57E-5\",\n \
    \             \"3.54E-7\"\n            ],\n            \"representation\": \"\
    Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n   \
    \         \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 28,\n         \
    \   \"cells\": [\n              \"KCl\",\n              \"KCl\",\n           \
    \   \"SEED-cpd00099#cpd00205##\",\n              \"0.65\",\n              \"0.01\"\
    \n            ],\n            \"representation\": \"Exact decoded DOM cell text;\
    \ not claimed as a literal HTML substring.\",\n            \"scope\": \"Optional\
    \ detail link resolved from the actual catalogue href. Preserve any failure; do\
    \ not infer historical equivalence.\",\n            \"usable\": true\n       \
    \   },\n          {\n            \"source_key\": \"komodo596\",\n            \"\
    source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 29,\n         \
    \   \"cells\": [\n              \"Resazurin\",\n              \"Resazurin\",\n\
    \              \"SEED-cpd08053###\",\n              \"4.93E-4\",\n           \
    \   \"2.15E-6\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 30,\n         \
    \   \"cells\": [\n              \"p-Aminobenzoic acid\",\n              \"p Aminobenzoic\
    \ acid (PABA)\",\n              \"SEED-cpd00443###\",\n              \"1.28E-4\"\
    ,\n              \"9.42E-7\"\n            ],\n            \"representation\":\
    \ \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 31,\n         \
    \   \"cells\": [\n              \"Na2WO4 x 2 H2O\",\n              \"Na2WO4\"\
    ,\n              \"SEED-cpd00971#cpd15574##\",\n              \"3.94E-6\",\n \
    \             \"2.68E-8\"\n            ],\n            \"representation\": \"\
    Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n   \
    \         \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 32,\n         \
    \   \"cells\": [\n              \"Tryptone\",\n              \"Tryptone\",\n \
    \             \"rich-peptone#\",\n              \"2.00\",\n              \"null\"\
    \n            ],\n            \"representation\": \"Exact decoded DOM cell text;\
    \ not claimed as a literal HTML substring.\",\n            \"scope\": \"Optional\
    \ detail link resolved from the actual catalogue href. Preserve any failure; do\
    \ not infer historical equivalence.\",\n            \"usable\": true\n       \
    \   },\n          {\n            \"source_key\": \"komodo596\",\n            \"\
    source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 33,\n         \
    \   \"cells\": [\n              \"H2O\",\n              \"H2O\",\n           \
    \   \"SEED-cpd00001###\",\n              \"null\",\n              \"null\"\n \
    \           ],\n            \"representation\": \"Exact decoded DOM cell text;\
    \ not claimed as a literal HTML substring.\",\n            \"scope\": \"Optional\
    \ detail link resolved from the actual catalogue href. Preserve any failure; do\
    \ not infer historical equivalence.\",\n            \"usable\": true\n       \
    \   },\n          {\n            \"source_key\": \"komodo596\",\n            \"\
    source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 34,\n         \
    \   \"cells\": [\n              \"Na-tartrate\",\n              \"L-tartarate\"\
    ,\n              \"SEED-cpd00666#cpd00971##\",\n              \"3.54E-3\",\n \
    \             \"2.07E-5\"\n            ],\n            \"representation\": \"\
    Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n   \
    \         \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 35,\n         \
    \   \"cells\": [\n              \"Na2SeO3 x 5 H2O\",\n              \"Sodium selenite\"\
    ,\n              \"SEED-cpd00971#cpd03387##\",\n              \"2.96E-6\",\n \
    \             \"1.11E-8\"\n            ],\n            \"representation\": \"\
    Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n   \
    \         \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 36,\n         \
    \   \"cells\": [\n              \"Distilled water\",\n              \"H2O\",\n\
    \              \"SEED-cpd00001###\",\n              \"null\",\n              \"\
    null\"\n            ],\n            \"representation\": \"Exact decoded DOM cell\
    \ text; not claimed as a literal HTML substring.\",\n            \"scope\": \"\
    Optional detail link resolved from the actual catalogue href. Preserve any failure;\
    \ do not infer historical equivalence.\",\n            \"usable\": true\n    \
    \      },\n          {\n            \"source_key\": \"komodo596\",\n         \
    \   \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 37,\n         \
    \   \"cells\": [\n              \"Biotin\",\n              \"Biotin\",\n     \
    \         \"SEED-cpd00104###\",\n              \"1.97E-5\",\n              \"\
    8.11E-8\"\n            ],\n            \"representation\": \"Exact decoded DOM\
    \ cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 38,\n         \
    \   \"cells\": [\n              \"NH4Cl\",\n              \"Ammonium chloride\"\
    ,\n              \"SEED-cpd00013#cpd00099##\",\n              \"0.25\",\n    \
    \          \"0.00\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 39,\n         \
    \   \"cells\": [\n              \"Na-glycerophosphate\",\n              \"Na-glycerophosphate\"\
    ,\n              \"SEED-cpd00971#cpd12183##\",\n              \"0.10\",\n    \
    \          \"0.00\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 40,\n         \
    \   \"cells\": [\n              \"CaCl2 x 2 H2O\",\n              \"Calcium chloride\
    \ \",\n              \"SEED-cpd00063#cpd00099##\",\n              \"1.45\",\n\
    \              \"0.01\"\n            ],\n            \"representation\": \"Exact\
    \ decoded DOM cell text; not claimed as a literal HTML substring.\",\n       \
    \     \"scope\": \"Optional detail link resolved from the actual catalogue href.\
    \ Preserve any failure; do not infer historical equivalence.\",\n            \"\
    usable\": true\n          },\n          {\n            \"source_key\": \"komodo596\"\
    ,\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 41,\n         \
    \   \"cells\": [\n              \"NiCl2 x 6 H2O\",\n              \"NiCl2\",\n\
    \              \"SEED-cpd00099#cpd00244##\",\n              \"2.36E-5\",\n   \
    \           \"9.91E-8\"\n            ],\n            \"representation\": \"Exact\
    \ decoded DOM cell text; not claimed as a literal HTML substring.\",\n       \
    \     \"scope\": \"Optional detail link resolved from the actual catalogue href.\
    \ Preserve any failure; do not infer historical equivalence.\",\n            \"\
    usable\": true\n          },\n          {\n            \"source_key\": \"komodo596\"\
    ,\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 42,\n         \
    \   \"cells\": [\n              \"H3BO3\",\n              \"Boric acid\",\n  \
    \            \"SEED-cpd09225###\",\n              \"5.70E-3\",\n             \
    \ \"9.19E-5\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 43,\n         \
    \   \"cells\": [\n              \"NaCl\",\n              \"NaCl\",\n         \
    \     \"SEED-cpd00099#cpd00971##\",\n              \"26.01\",\n              \"\
    0.45\"\n            ],\n            \"representation\": \"Exact decoded DOM cell\
    \ text; not claimed as a literal HTML substring.\",\n            \"scope\": \"\
    Optional detail link resolved from the actual catalogue href. Preserve any failure;\
    \ do not infer historical equivalence.\",\n            \"usable\": true\n    \
    \      },\n          {\n            \"source_key\": \"komodo596\",\n         \
    \   \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 44,\n         \
    \   \"cells\": [\n              \"KBr\",\n              \"KBr\",\n           \
    \   \"SEED-cpd00205#cpd00966##\",\n              \"0.09\",\n              \"0.00\"\
    \n            ],\n            \"representation\": \"Exact decoded DOM cell text;\
    \ not claimed as a literal HTML substring.\",\n            \"scope\": \"Optional\
    \ detail link resolved from the actual catalogue href. Preserve any failure; do\
    \ not infer historical equivalence.\",\n            \"usable\": true\n       \
    \   },\n          {\n            \"source_key\": \"komodo596\",\n            \"\
    source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 2,\n            \"row_index\": 45,\n         \
    \   \"cells\": [\n              \"Na-Lactate\",\n              \"Na-Lactate\"\
    ,\n              \"SEED-cpd00971#cpd01022##\",\n              \"2.27\",\n    \
    \          \"0.02\"\n            ],\n            \"representation\": \"Exact decoded\
    \ DOM cell text; not claimed as a literal HTML substring.\",\n            \"scope\"\
    : \"Optional detail link resolved from the actual catalogue href. Preserve any\
    \ failure; do not infer historical equivalence.\",\n            \"usable\": true\n\
    \          },\n          {\n            \"source_key\": \"komodo596\",\n     \
    \       \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 0,\n          \
    \  \"cells\": [\n              \"Seed ID\",\n              \"Name\",\n       \
    \       \"Mol Concentration\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 1,\n          \
    \  \"cells\": [\n              \"cpd12183\",\n              \"(Glycerophosphate)n\"\
    ,\n              \"2.87896541498847E-4\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 2,\n          \
    \  \"cells\": [\n              \"cpd15574\",\n              \"tungstate\",\n \
    \             \"2.67534139821693E-8\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 3,\n          \
    \  \"cells\": [\n              \"cpd00239\",\n              \"H2S\",\n       \
    \       \"0.0020242335522773465\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 4,\n          \
    \  \"cells\": [\n              \"cpd00218\",\n              \"Niacin\",\n    \
    \          \"2.018841126830706E-6\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 5,\n          \
    \  \"cells\": [\n              \"cpd00048\",\n              \"Sulfate\",\n   \
    \           \"0.02713515026728839\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 6,\n          \
    \  \"cells\": [\n              \"cpd00443\",\n              \"ABEE\",\n      \
    \        \"9.417300079863235E-7\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 7,\n          \
    \  \"cells\": [\n              \"cpd00644\",\n              \"PAN\",\n       \
    \       \"5.727874824961537E-7\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 8,\n          \
    \  \"cells\": [\n              \"cpd00149\",\n              \"Co2+\",\n      \
    \        \"1.1241674217181804E-6\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 9,\n          \
    \  \"cells\": [\n              \"cpd00666\",\n              \"Tartrate\",\n  \
    \            \"2.0681073312652265E-5\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 10,\n         \
    \   \"cells\": [\n              \"cpd00104\",\n              \"BIOT\",\n     \
    \         \"1.6217192920055714E-7\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 11,\n         \
    \   \"cells\": [\n              \"cpd00242\",\n              \"H2CO3\",\n    \
    \          \"0.029321263984922154\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 12,\n         \
    \   \"cells\": [\n              \"cpd00220\",\n              \"RIBF\",\n     \
    \         \"1.3100990291135432E-7\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 13,\n         \
    \   \"cells\": [\n              \"cpd00263\",\n              \"Pyridoxol\",\n\
    \              \"1.9317538625360478E-6\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 14,\n         \
    \   \"cells\": [\n              \"cpd00541\",\n              \"Lipoate\",\n  \
    \            \"2.4029133412033766E-7\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 15,\n         \
    \   \"cells\": [\n              \"cpd00244\",\n              \"Ni2+\",\n     \
    \         \"9.91412485073203E-8\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 16,\n         \
    \   \"cells\": [\n              \"cpd00166\",\n              \"Calomide\",\n \
    \             \"6.301750567399103E-8\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 17,\n         \
    \   \"cells\": [\n              \"cpd00001\",\n              \"H2O\",\n      \
    \        \"0.9999975431559356\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 18,\n         \
    \   \"cells\": [\n              \"cpd10516\",\n              \"fe3\",\n      \
    \        \"7.422489621063538E-6\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 19,\n         \
    \   \"cells\": [\n              \"cpd00063\",\n              \"Ca2+\",\n     \
    \         \"0.009899655977798799\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 20,\n         \
    \   \"cells\": [\n              \"cpd10515\",\n              \"Fe2+\",\n     \
    \         \"1.787685998212314E-5\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 21,\n         \
    \   \"cells\": [\n              \"cpd09244\",\n              \"Sodium hydroxide\"\
    ,\n              \"2.7366513052594012E-5\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 22,\n         \
    \   \"cells\": [\n              \"cpd09225\",\n              \"Boric acid\",\n\
    \              \"9.193874387194626E-5\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 23,\n         \
    \   \"cells\": [\n              \"cpd09249\",\n              \"Sodium bicarbonate\"\
    ,\n              \"0.0\"\n            ],\n            \"representation\": \"Exact\
    \ decoded DOM cell text; not claimed as a literal HTML substring.\",\n       \
    \     \"scope\": \"Optional detail link resolved from the actual catalogue href.\
    \ Preserve any failure; do not infer historical equivalence.\",\n            \"\
    usable\": true\n          },\n          {\n            \"source_key\": \"komodo596\"\
    ,\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 24,\n         \
    \   \"cells\": [\n              \"cpd11145\",\n              \"Sodium molybdate\"\
    ,\n              \"3.5381017284146763E-7\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 25,\n         \
    \   \"cells\": [\n              \"cpd00209\",\n              \"Nitrate\",\n  \
    \            \"0.004945549500004946\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 26,\n         \
    \   \"cells\": [\n              \"cpd00305\",\n              \"THI\",\n      \
    \        \"7.323776909704017E-7\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 27,\n         \
    \   \"cells\": [\n              \"cpd00205\",\n              \"K+\",\n       \
    \       \"0.015937071520420266\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 28,\n         \
    \   \"cells\": [\n              \"cpd00009\",\n              \"Phosphate\",\n\
    \              \"0.001459547362805014\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 29,\n         \
    \   \"cells\": [\n              \"cpd00966\",\n              \"HBr\",\n      \
    \        \"7.45105061263904E-4\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 30,\n         \
    \   \"cells\": [\n              \"cpd00971\",\n              \"Na+\",\n      \
    \        \"0.502344109141384\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 31,\n         \
    \   \"cells\": [\n              \"cpd00058\",\n              \"Cu2+\",\n     \
    \         \"3.290710513757317E-7\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 32,\n         \
    \   \"cells\": [\n              \"cpd04877\",\n              \"Magnesium chloride\"\
    ,\n              \"0.0\"\n            ],\n            \"representation\": \"Exact\
    \ decoded DOM cell text; not claimed as a literal HTML substring.\",\n       \
    \     \"scope\": \"Optional detail link resolved from the actual catalogue href.\
    \ Preserve any failure; do not infer historical equivalence.\",\n            \"\
    usable\": true\n          },\n          {\n            \"source_key\": \"komodo596\"\
    ,\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 33,\n         \
    \   \"cells\": [\n              \"cpd00099\",\n              \"Cl-\",\n      \
    \        \"0.5370975461446161\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 34,\n         \
    \   \"cells\": [\n              \"cpd00013\",\n              \"NH3\",\n      \
    \        \"0.004647143725912191\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 35,\n         \
    \   \"cells\": [\n              \"cpd01022\",\n              \"Lactate\",\n  \
    \            \"0.020231672149596286\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 36,\n         \
    \   \"cells\": [\n              \"cpd00254\",\n              \"Mg\",\n       \
    \       \"0.05479400321702677\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 37,\n         \
    \   \"cells\": [\n              \"cpd00034\",\n              \"Zn2+\",\n     \
    \         \"8.1740796567747E-7\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 38,\n         \
    \   \"cells\": [\n              \"cpd03387\",\n              \"Selenite\",\n \
    \             \"1.1121668521844414E-8\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 39,\n         \
    \   \"cells\": [\n              \"cpd00393\",\n              \"FOL\",\n      \
    \        \"4.4883574938195196E-8\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 40,\n         \
    \   \"cells\": [\n              \"cpd00030\",\n              \"Mn2+\",\n     \
    \         \"1.8697759913899182E-5\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          },\n          {\n            \"source_key\"\
    : \"komodo596\",\n            \"source_sha256\": \"efd248d15ed9592b7eba92aea78e62581b610963f944598420feb33fdcd4fb78\"\
    ,\n            \"table_index\": 3,\n            \"row_index\": 41,\n         \
    \   \"cells\": [\n              \"cpd08053\",\n              \"Resazurin\",\n\
    \              \"2.1510796285881757E-6\"\n            ],\n            \"representation\"\
    : \"Exact decoded DOM cell text; not claimed as a literal HTML substring.\",\n\
    \            \"scope\": \"Optional detail link resolved from the actual catalogue\
    \ href. Preserve any failure; do not infer historical equivalence.\",\n      \
    \      \"usable\": true\n          }\n        ],\n        \"representation\":\
    \ \"Exact decoded DOM text, not a literal raw-HTML quotation\"\n      }\n    ],\n\
    \    \"interpretation\": \"All printed provider gram/mol/model-concentration quantities\
    \ are preserved together with their headers. They describe an incompatible current\
    \ expansion; no model amount is silently converted to a primary-medium concentration.\"\
    \n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.006077.partial-trace-nesting
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Eight stock solutes are incompletely separated from the medium
  description: All eight trace components are stock ingredients. The target flattens
    all eight; both maintained owners nest only boric acid, manganese chloride and
    ferrous sulfate, leaving five stock-preparation amounts represented as rates among
    main ingredients.
  target_ids:
  - CultureMech:006077
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - dsm-main
  - record
  - owner-0
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
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
  issue_key: culturemech.006077.seawater-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Main artificial seawater is recorded as a mass
  description: All three layers store999 G_PER_L for source999 ml artificial seawater.
    Its aquarium-salt composition differs from distilled water and is not quantitatively
    specified.
  target_ids:
  - CultureMech:006077
  field_paths:
  - ingredients[5].concentration
  - ingredients[5].preferred_term
  evidence_ids:
  - dsm-main
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.006077.tris-salt
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Tris hydrochloride is grounded to free-base tris
  description: The source and local names say Tris HCl; CHEBI:9754 has no chloride
    and explicitly denotes tris base. Valid label metadata does not make it the supplied
    salt.
  target_ids:
  - CultureMech:006077
  field_paths:
  - ingredients[2].term
  evidence_ids:
  - dsm-main
  - chebi9754
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.006077.form-specificity
  category: grounding
  severity: major
  status: open
  certainty: provisional
  title: Two asserted forms exceed the primary description
  description: Source Na-tartrate does not establish L stereochemistry; source FeSO4
    does not establish hydration. The local L-tartrate and anhydrous ferrous-sulfate
    assertions require supplier/source confirmation.
  target_ids:
  - CultureMech:006077
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - dsm-main
  - chebi63017
  - chebi75832
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: culturemech.006077.legacy-link-history
  category: grounding
  severity: major
  status: open
  certainty: provisional
  title: Legacy000170 remains unauthenticated
  description: Current exact lookup is absent for the three retained legacy KNO3 links;
    original historical correspondence is unknown, independent of the valid CHEBI
    potassium-nitrate identity.
  target_ids:
  - CultureMech:006077
  field_paths:
  - ingredients[0].mediaingredientmech_term
  evidence_ids:
  - legacy-mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.1
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: culturemech.006077.preparation-projection
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Artificial seawater preparation is not retained across contributors and target
  description: The DSM owner already states that artificial seawater uses a marine
    aquarium salts mixture. The other owner and target lack this preparation context;
    the source does not provide a sterilization cycle to add.
  target_ids:
  - CultureMech:006077
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsm-main
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3.4 is major here because solvent identity affects reproducibility;
    the action preserves known preparation rather than requesting a generic missing
    protocol.
- finding_id: f7
  issue_key: culturemech.006077.quantity-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Quantity claims lack attached source evidence
  description: Printed batch masses/doses and pH lack attached scoped evidence. The
    source supports those literal inputs, but final-medium and final-stock concentration
    denominators remain unsupported. Only the unchanged pH decisions are evidence_only;
    structural/unit corrections remain separate.
  target_ids:
  - CultureMech:006077
  field_paths:
  - ingredients
  - solutions
  - ph_value
  evidence_ids:
  - dsm-main
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: 'P4.3 remains a minor traceability exception: attach evidence
    to literal batch claims and supported pH only after substantive stage, unit, form
    and denominator issues are resolved; it does not endorse the existing rates.'
actions:
- action_id: a1
  description: Complete the eight-component trace stock in both maintained owners,
    preserve1 ml dose and1000 ml stock water, then regenerate once. Avoid duplicate
    direct and nested ingredients.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006077
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
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
  description: Correct the maintained solvent volume basis and material description,
    retaining unquantified salinity; regenerate without density assumptions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006077
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
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
  description: Resolve the exact hydrochloride term from authoritative ontology evidence
    or remove the incompatible link pending resolution; retain the source1 g amount
    and do not invent a replacement ID.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006077
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
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
  description: Resolve the exact supplied materials without guessing an opposite enantiomer
    or hydrate. Preserve literal source names/masses and flag unsupported specificity
    pending evidence.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006077
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
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
  description: Recover historical mapping provenance or explicitly retire/replace
    the legacy link using verified current correspondence; preserve append-only history
    and do not invent its earlier meaning.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006077
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
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
- action_id: a6
  description: Preserve the DSM owner’s existing scoped preparation in the corrected
    maintained contribution and later target projection, without inventing salinity,
    oxygen or an autoclave cycle.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:006077
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
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
- action_id: a7
  description: Attach short versioned DSM rows to the exact maintained batch quantities
    and pH; establish any final-volume basis before attaching evidence to a normalized
    rate.
  finding_ids:
  - f7
  target_ids:
  - CultureMech:006077
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml
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
- The exact current MediaDive REST596 request returned HTTP503 once. The DSM primary
  remains usable; the failure is not recipe absence.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-043
- generated-medium
```
